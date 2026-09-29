"""
Documentation-hub lint rules (design/cdm-doc-hub §3.2).

DOC-01 error    see_also / structured_aliases.source URL (and #fragment) must be in the link registry
DOC-02 warning  registry entry not used by any class
DOC-03 error    platformAPI / nexarAPI must exist in the API snapshot as OBJECT, INTERFACE or UNION
DOC-04 error    *_mappings values must be full http(s) URLs or allow-listed CURIEs
DOC-05 warning  PRODUCTION class with no see_also and no API type must declare `productDocs: none`
"""

from __future__ import annotations

import dataclasses
import re
from pathlib import Path
from typing import Callable, Iterable, Optional

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_snapshot import load_snapshots
from cdm_tools.conventions import LintIssue
from cdm_tools.registry import LinkEntry, load_registry, split_url

Locator = Callable[[str], tuple[str, int]]
IsCdm = Callable[[str], bool]

LINKABLE_KINDS = frozenset({"OBJECT", "INTERFACE", "UNION"})
API_ANNOTATIONS = {"platformAPI": "platform", "nexarAPI": "nexar"}
ALLOWED_MAPPING_PREFIXES = frozenset({"prov", "obo"})
MAPPING_FIELDS = ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings")
BASELINE_BUCKETS = {"DOC-01": "doc_link", "DOC-03": "api_type", "DOC-04": "mapping_format"}
_CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_.-]*):(?!//)")


def _classes(sv: SchemaView, is_cdm: IsCdm) -> Iterable[tuple[str, object]]:
    for name, cls in sv.all_classes().items():
        if is_cdm(getattr(cls, "from_schema", "") or ""):
            yield name, cls


def _alias_sources(cls) -> list[str]:
    aliases = cls.structured_aliases or {}
    values = aliases.values() if isinstance(aliases, dict) else aliases
    return [str(a.source) for a in values if getattr(a, "source", None)]


def _issue(locate: Locator, name: str, severity: str, rule: str, message: str) -> LintIssue:
    file, line = locate(name)
    return LintIssue(file=file, line=line, severity=severity, rule_id=rule, message=message, element=name)


def check_doc_links(sv: SchemaView, registry: dict[str, LinkEntry], locate: Locator, is_cdm: IsCdm,
                    registry_path: str) -> list[LintIssue]:
    issues: list[LintIssue] = []
    used: set[str] = set()
    for name, cls in _classes(sv, is_cdm):
        for url in [str(u) for u in (cls.see_also or [])] + _alias_sources(cls):
            base, frag = split_url(url)
            used.add(base)
            entry = registry.get(base)
            if entry is None:
                msg = f"class '{name}' links '{url}', which is not in the link registry ({registry_path})"
            elif frag is not None and frag not in entry.anchors:
                msg = f"class '{name}' links anchor '#{frag}', which is not listed in the registry entry for '{base}'"
            else:
                continue
            issues.append(_issue(locate, name, "error", "DOC-01", msg))
    for base in sorted(set(registry) - used):
        issues.append(LintIssue(file=registry_path, line=1, severity="warning", rule_id="DOC-02",
                                message=f"registry entry '{base}' is not used by any class", element=base))
    return issues


def check_api_types(sv: SchemaView, snapshots: dict[str, dict], locate: Locator, is_cdm: IsCdm) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for name, cls in _classes(sv, is_cdm):
        for key, target in API_ANNOTATIONS.items():
            if key not in cls.annotations or target not in snapshots:
                continue
            type_name = str(cls.annotations[key].value)
            info = snapshots[target]["types"].get(type_name)
            if info is None:
                msg = f"class '{name}' {key} '{type_name}' does not exist in the {target} API snapshot"
            elif info["kind"] not in LINKABLE_KINDS:
                msg = (f"class '{name}' {key} '{type_name}' is a {info['kind']} in the {target} API; "
                       "expected OBJECT, INTERFACE or UNION")
            else:
                continue
            issues.append(_issue(locate, name, "error", "DOC-03", msg))
    return issues


def check_mappings(sv: SchemaView, locate: Locator, is_cdm: IsCdm,
                   allowed_prefixes: frozenset[str] = ALLOWED_MAPPING_PREFIXES) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for name, cls in _classes(sv, is_cdm):
        for field in MAPPING_FIELDS:
            for value in getattr(cls, field, None) or []:
                v = str(value)
                if v.startswith(("http://", "https://")):
                    continue
                m = _CURIE_RE.match(v)
                if m and m.group(1) in allowed_prefixes:
                    continue
                issues.append(_issue(locate, name, "error", "DOC-04",
                                     f"class '{name}' {field} value '{v}' must be a full http(s) URL or a CURIE "
                                     f"with an allow-listed prefix ({', '.join(sorted(allowed_prefixes))})"))
    return issues


def check_coverage(sv: SchemaView, locate: Locator, is_cdm: IsCdm) -> list[LintIssue]:
    issues: list[LintIssue] = []
    for name, cls in _classes(sv, is_cdm):
        if cls.abstract or cls.mixin or name == "Any" or name.startswith("core_"):
            continue
        ann = cls.annotations
        maturity = str(ann["maturity"].value) if "maturity" in ann and ann["maturity"].value else "PRODUCTION"
        if maturity != "PRODUCTION":
            continue
        if cls.see_also or "platformAPI" in ann or "nexarAPI" in ann:
            continue
        if "productDocs" in ann and str(ann["productDocs"].value) == "none":
            continue
        issues.append(_issue(locate, name, "warning", "DOC-05",
                             f"class '{name}' has no product documentation (see_also) and no API type; add links, "
                             "or annotate 'productDocs: none' after confirming no public documentation exists"))
    return issues


def downgrade_baselined(issues: list[LintIssue], baseline: dict[str, set[str]]) -> list[LintIssue]:
    out: list[LintIssue] = []
    for issue in issues:
        bucket = BASELINE_BUCKETS.get(issue.rule_id)
        if bucket and issue.severity == "error" and issue.element in baseline.get(bucket, set()):
            issue = dataclasses.replace(issue, severity="warning")
        out.append(issue)
    return out


def run_doc_rules(sv: SchemaView, *, locate: Locator, is_cdm: IsCdm, registry_path: Optional[str],
                  api_dir: Optional[str], baseline: dict[str, set[str]]) -> list[LintIssue]:
    issues: list[LintIssue] = []
    if registry_path and Path(registry_path).is_file():
        issues += check_doc_links(sv, load_registry(registry_path), locate, is_cdm, registry_path)
    if api_dir and Path(api_dir).is_dir():
        issues += check_api_types(sv, load_snapshots(api_dir), locate, is_cdm)
    issues += check_mappings(sv, locate, is_cdm)
    issues += check_coverage(sv, locate, is_cdm)
    return downgrade_baselined(issues, baseline)
