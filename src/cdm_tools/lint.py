"""
cdm-lint — CDM Convention Linter

Validates CDM schema YAML files against AGENTS.md naming and metadata conventions.
Loads the schema via SchemaView from the root common_data_model.yaml.

Exit codes (D-08):
  0 — no errors (warnings allowed)
  1 — one or more errors
  2 — internal error (schema failed to load)
"""

from __future__ import annotations

import os
import sys
import yaml
from pathlib import Path
from typing import Optional

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.conventions import (
    CLASS_NAME_RE,
    SLOT_NAME_RE,
    SHARED_SLOT_NAME_RE,
    GRID_RE,
    CLASS_REQUIRED_FIELDS,
    SLOT_REQUIRED_FIELDS,
    LintIssue,
    is_url_safe_iri_local_name,
    SLOT_URI_CLASS_RE,
    ALIAS_RE,
    TITLE_UNDERSCORE_RE,
)

# ---------------------------------------------------------------------------
# YAML line-number extraction
# ---------------------------------------------------------------------------


class _MarkedLoader(yaml.SafeLoader):
    pass


def _construct_mapping_with_marks(
    loader: yaml.SafeLoader, node: yaml.MappingNode
) -> dict:
    loader.flatten_mapping(node)
    return {
        loader.construct_object(k): (loader.construct_object(v), k.start_mark.line + 1)
        for k, v in node.value
    }


_MarkedLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping_with_marks,
)


def _build_line_map(yaml_path: str) -> dict[str, int]:
    """Return {element_name: line_number} for classes, slots, and class attributes in a schema YAML file."""
    try:
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f, Loader=_MarkedLoader)
    except (OSError, yaml.YAMLError):
        return {}

    result: dict[str, int] = {}

    def _unwrap(val):
        """Unwrap a (value, line_no) tuple or return (val, 0) if not a tuple."""
        if isinstance(val, tuple) and len(val) == 2 and isinstance(val[1], int):
            return val[0], val[1]
        return val, 0

    # --- Top-level named slots ---
    slots_raw, _ = _unwrap(data.get("slots"))
    if isinstance(slots_raw, dict):
        for name, val in slots_raw.items():
            _, line = _unwrap(val)
            result[str(name)] = line

    # --- Classes (names) and their attributes ---
    classes_raw, _ = _unwrap(data.get("classes"))
    if isinstance(classes_raw, dict):
        for class_name, class_val in classes_raw.items():
            class_def, class_line = _unwrap(class_val)
            result[str(class_name)] = class_line

            if not isinstance(class_def, dict):
                continue
            attrs_raw, _ = _unwrap(class_def.get("attributes"))
            if not isinstance(attrs_raw, dict):
                continue
            for attr_name, attr_val in attrs_raw.items():
                _, attr_line = _unwrap(attr_val)
                result[str(attr_name)] = attr_line

    return result


# ---------------------------------------------------------------------------
# Schema-file mapping helpers
# ---------------------------------------------------------------------------

# ID prefixes for upstream (non-CDM) schemas — elements from these are skipped
_UPSTREAM_SCHEMA_ID_PREFIXES = ("https://w3id.org/linkml/",)


def _build_schema_file_map(sv: SchemaView, root_path: str) -> dict[str, str]:
    """
    Return {schema_id: absolute_file_path} for all loaded schemas.

    source_file on imported schemas is relative; resolve relative to root's directory.
    """
    root_dir = os.path.dirname(os.path.abspath(root_path))
    result: dict[str, str] = {}
    for schema_def in sv.all_schema(imports=True):
        src = getattr(schema_def, "source_file", None)
        if not src:
            continue
        abs_path = src if os.path.isabs(src) else os.path.join(root_dir, src)
        result[schema_def.id] = abs_path
    return result


def _is_cdm_schema(schema_id: str) -> bool:
    """Return True if the schema ID belongs to the CDM (not an upstream import)."""
    for prefix in _UPSTREAM_SCHEMA_ID_PREFIXES:
        if schema_id.startswith(prefix):
            return False
    return True


# ---------------------------------------------------------------------------
# Baseline config loader (D-01, D-02)
# ---------------------------------------------------------------------------


def _load_baseline(config_path: Optional[str]) -> dict[str, set[str]]:
    """
    Load cdm-lint.yaml baseline config.

    Returns a dict mapping violation_type -> set of exempt element names.
    Violation types: "naming", "missing_metadata", "naming_class"
    """
    if not config_path or not os.path.exists(config_path):
        return {}

    try:
        with open(config_path, encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}
    except (OSError, yaml.YAMLError):
        return {}

    result: dict[str, set[str]] = {}
    for key, value in raw.items():
        if isinstance(value, list):
            result[key] = set(str(v) for v in value)
        elif isinstance(value, dict):
            # Nested: missing_metadata.class_uri: [...]
            for subkey, sublist in value.items():
                compound = f"{key}.{subkey}"
                if isinstance(sublist, list):
                    result[compound] = set(str(v) for v in sublist)
    return result


def _apply_baseline(
    issue: LintIssue,
    baseline: dict[str, set[str]],
    element_name: str,
    violation_type: str,
) -> LintIssue:
    """
    Downgrade an error → warning if the element is in the baseline for this violation type.

    D-03: Warnings use same format but 'warning' severity; do not affect exit code.
    """
    exempt_set = baseline.get(violation_type, set())
    if element_name in exempt_set:
        return LintIssue(
            file=issue.file,
            line=issue.line,
            severity="warning",
            rule_id=issue.rule_id,
            message=issue.message,
        )
    return issue


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------


def _validate_class_naming(
    name: str,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
) -> Optional[LintIssue]:
    """LINT-03: class name must match CLASS_NAME_RE."""
    if CLASS_NAME_RE.match(name):
        return None
    issue = LintIssue(
        file=file_path,
        line=line,
        severity="error",
        rule_id="LINT-03",
        message=(
            f"class name '{name}' must match pattern "
            r"^[a-z][a-zA-Z0-9]*_[A-Z][a-zA-Z0-9]*$ "
            "(subsetName_ClassName)"
        ),
    )
    return _apply_baseline(issue, baseline, name, "naming_class")


def _validate_slot_naming(
    name: str,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
    *,
    is_shared: bool = True,
) -> Optional[LintIssue]:
    """LINT-04: slot name validation.

    Named slots (top-level ``slots:`` section, ``is_shared=True``) accept EITHER:
    - Shared pattern:  ``{subsetName}_{slotName}``    (e.g. core_id, pro_bom_items)
    - Class pattern:   ``{subsetName}_{ClassName}_{fieldName}``  (legacy; flag via LINT-08)

    Attribute slots (``attributes:`` in a class, ``is_shared=False``) must use:
    - Class pattern only: ``{subsetName}_{ClassName}_{fieldName}``
    """
    if is_shared:
        if SLOT_NAME_RE.match(name) or SHARED_SLOT_NAME_RE.match(name):
            return None
    else:
        if SLOT_NAME_RE.match(name):
            return None
    issue = LintIssue(
        file=file_path,
        line=line,
        severity="error",
        rule_id="LINT-04",
        message=(
            f"slot name '{name}' must match pattern "
            r"^[a-z][a-zA-Z0-9]*_[A-Z][a-zA-Z0-9]*_[a-z][a-zA-Z0-9]*$ "
            "(subsetName_ClassName_fieldName) for class-specific slots, or "
            r"^[a-z][a-zA-Z0-9]*_[a-z][a-zA-Z0-9_]*$ "
            "(subsetName_slotName) for shared slots"
        ),
    )
    return _apply_baseline(issue, baseline, name, "naming")


# Hard-coded permanent exemptions for core LinkML annotation/mixin keys.
# These keys appear as attribute names in core.yaml mixins but are framework-level
# metadata, not domain attributes — exempt from LINT-04 naming convention.
# Stored here (not only in cdm-lint.yaml) so they survive baseline regeneration.
_NAMING_EXEMPT_ANNOTATIONS: frozenset[str] = frozenset(
    {
        "grid",
        "platformAPI",
        "maturity",
        "contentType",
        "vaultLinkParent",
        "vaultLinkChild",
        "vaultLinkType",
    }
)


def _is_naming_exempt(name: str, baseline: dict[str, set[str]]) -> bool:
    """Return True if the slot name is permanently exempt or listed in the baseline exempt set."""
    return name in _NAMING_EXEMPT_ANNOTATIONS or name in baseline.get(
        "naming_exempt_annotations", set()
    )


def _validate_single_use_slot(
    name: str,
    file_path: str,
    line: int,
    usage_count: int,
) -> Optional[LintIssue]:
    """LINT-08: named slot defined in top-level ``slots:`` section used by ≤1 class.

    These are migration candidates — class-specific slots belong under ``attributes:``
    in their owning class definition.
    Severity is always *warning* (advisory, not a hard error).
    """
    if usage_count > 1:
        return None
    noun = "no classes" if usage_count == 0 else "only 1 class"
    return LintIssue(
        file=file_path,
        line=line,
        severity="warning",
        rule_id="LINT-08",
        message=(
            f"slot '{name}' is defined in the top-level slots section but used by "
            f"{noun} — consider migrating to `attributes:` in the owning class"
        ),
    )


def _validate_slot_uri_format(
    name: str,
    slot_def,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
    *,
    is_class_specific: bool,
) -> Optional[LintIssue]:
    """CONV-01: class-specific slot_uri must be {prefix}:{ClassName}_{field}."""
    if not is_class_specific:
        return None
    uri = getattr(slot_def, "slot_uri", None)
    if not uri:
        return None
    if SLOT_URI_CLASS_RE.match(str(uri)):
        return None
    issue = LintIssue(
        file=file_path,
        line=line,
        severity="error",
        rule_id="CONV-01",
        message=(
            f"slot '{name}' has slot_uri '{uri}' that does not follow "
            "the {prefix}:{ClassName}_{field} convention (e.g. 'lib:ComponentRevision_symbols'). "
            "Colon separates prefix from ClassName; underscore separates ClassName from field."
        ),
    )
    return _apply_baseline(issue, baseline, name, "slot_uri_format")


def _validate_alias_format(
    name: str,
    slot_def,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
) -> Optional[LintIssue]:
    """CONV-02: alias must be lowerCamelCase."""
    alias = getattr(slot_def, "alias", None)
    if not alias:
        return None  # LINT-06 flags missing alias
    if ALIAS_RE.match(str(alias)):
        return None
    issue = LintIssue(
        file=file_path,
        line=line,
        severity="error",
        rule_id="CONV-02",
        message=(
            f"slot '{name}' has alias '{alias}' that is not lowerCamelCase. "
            "Alias must start with a lowercase letter and contain only alphanumerics (no underscores)."
        ),
    )
    return _apply_baseline(issue, baseline, name, "alias_format")


def _validate_title_format(
    name: str,
    slot_def,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
) -> Optional[LintIssue]:
    """CONV-02: title must not contain underscores."""
    title = getattr(slot_def, "title", None)
    if not title:
        return None  # LINT-06 flags missing title
    if not TITLE_UNDERSCORE_RE.search(str(title)):
        return None
    issue = LintIssue(
        file=file_path,
        line=line,
        severity="error",
        rule_id="CONV-02",
        message=(
            f"slot '{name}' has title '{title}' containing underscores. "
            "Title must be a human-readable string with spaces (e.g. 'bom items', not 'bom_items')."
        ),
    )
    return _apply_baseline(issue, baseline, name, "title_format")


def _validate_class_metadata(
    name: str,
    cls_def,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
) -> list[LintIssue]:
    """LINT-05: required class metadata completeness."""
    issues: list[LintIssue] = []

    checks = {
        "class_uri": bool(getattr(cls_def, "class_uri", None)),
        "title": bool(getattr(cls_def, "title", None)),
        "description": bool(getattr(cls_def, "description", None)),
        "in_subset": bool(getattr(cls_def, "in_subset", None)),
    }

    for field, present in checks.items():
        if not present:
            issue = LintIssue(
                file=file_path,
                line=line,
                severity="error",
                rule_id="LINT-05",
                message=f"class '{name}' is missing required metadata field '{field}'",
            )
            issues.append(
                _apply_baseline(issue, baseline, name, f"missing_metadata.{field}")
            )

    return issues


def _validate_slot_metadata(
    name: str,
    slot_def,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
) -> list[LintIssue]:
    """LINT-06: required slot metadata completeness.

    Note: slot.required is None when not explicitly set in YAML (None ≠ False here).
    """
    issues: list[LintIssue] = []

    checks = {
        "slot_uri": bool(getattr(slot_def, "slot_uri", None)),
        "alias": bool(getattr(slot_def, "alias", None)),
        "title": bool(getattr(slot_def, "title", None)),
        "description": bool(getattr(slot_def, "description", None)),
        "range": bool(getattr(slot_def, "range", None)),
        "multivalued": getattr(slot_def, "multivalued", None) is not None,
        "required": getattr(slot_def, "required", None) is not None,
    }

    for field, present in checks.items():
        if not present:
            issue = LintIssue(
                file=file_path,
                line=line,
                severity="error",
                rule_id="LINT-06",
                message=f"slot '{name}' is missing required metadata field '{field}'",
            )
            issues.append(
                _apply_baseline(issue, baseline, name, f"missing_metadata.{field}")
            )

    return issues


def _validate_grid_annotation(
    name: str,
    element_def,
    file_path: str,
    line: int,
    baseline: dict[str, set[str]],
) -> Optional[LintIssue]:
    """LINT-07: GRID annotation format validation."""
    annotations = getattr(element_def, "annotations", None)
    if not annotations:
        return None
    grid_ann = annotations.get("grid")
    if not grid_ann:
        return None
    grid_value = str(grid_ann.value).strip()
    if GRID_RE.match(grid_value):
        return None
    issue = LintIssue(
        file=file_path,
        line=line,
        severity="error",
        rule_id="LINT-07",
        message=(
            f"element '{name}' has invalid GRID annotation: '{grid_value}'. "
            "Expected format: grid:{area}:{tenant-id}:{context}:{resource-type}[/{id}]"
        ),
    )
    return _apply_baseline(issue, baseline, name, "grid_format")


def validate_url_convention(sv: SchemaView, baseline: set[str]) -> list[LintIssue]:
    """
    Validate that every class's IRI local name is URL-safe and derivable
    from the docs slug produced by camelcase(element_name).

    This enforces the static htaccess convention:
      IRI .../subset/LocalName → docs /classes/{Prefix}LocalName/
    The rule works only when LocalName is PascalCase and URL-safe.

    :param sv: SchemaView over the loaded schema
    :param baseline: flat set of element names already known to violate convention;
                     elements in this set emit warnings instead of errors
    """
    from linkml_runtime.utils.formatutils import camelcase

    W3ID_PREFIX = "w3id.org/altium/cdm/"
    issues: list[LintIssue] = []

    for name, cd in sv.all_classes().items():
        uri = sv.get_uri(cd, expand=True)
        if not uri or W3ID_PREFIX not in str(uri):
            continue  # skip linkml: builtins and classes without w3id IRIs

        # Extract IRI local name (last path segment)
        local_name = str(uri).rstrip("/").rsplit("/", 1)[-1]

        # Check 1 — URL-safe (IRI-CONV-01)
        if not is_url_safe_iri_local_name(local_name):
            level = "warning" if name in baseline else "error"
            issues.append(
                LintIssue(
                    file="",
                    line=0,
                    severity=level,
                    rule_id="IRI-CONV-01",
                    element=name,
                    message=(
                        f"Class '{name}' has IRI local name '{local_name}' which is not "
                        f"URL-safe. IRI local names must match ^[A-Za-z][A-Za-z0-9]*$. "
                        f"The static htaccess pattern cannot route this class."
                    ),
                )
            )
            continue  # no point checking slug match if local_name itself is bad

        # Check 2 — docs slug ends with IRI local name (IRI-CONV-02)
        docs_slug = camelcase(name)
        if not docs_slug.endswith(local_name):
            level = "warning" if name in baseline else "error"
            issues.append(
                LintIssue(
                    file="",
                    line=0,
                    severity=level,
                    rule_id="IRI-CONV-02",
                    element=name,
                    message=(
                        f"Class '{name}' docs slug '{docs_slug}' does not end with "
                        f"IRI local name '{local_name}'. "
                        f"The static htaccess pattern would route to the wrong docs page. "
                        f"Fix: ensure class_uri local name matches the PascalCase suffix "
                        f"of the element name (expected suffix: '{local_name}')."
                    ),
                )
            )

    return issues


# ---------------------------------------------------------------------------
# Main lint runner
# ---------------------------------------------------------------------------


def run_lint(schema_path: str, config_path: Optional[str]) -> list[LintIssue]:
    """
    Load schema via SchemaView and run all CDM convention validators.

    Returns list of LintIssue objects (mix of error/warning severity).
    The caller determines exit code from presence of error-severity issues.
    """
    try:
        sv = SchemaView(schema_path)
    except Exception as exc:
        print(f"cdm-lint: internal error loading schema: {exc}", file=sys.stderr)
        sys.exit(2)

    baseline = _load_baseline(config_path)
    schema_file_map = _build_schema_file_map(sv, schema_path)

    # Build line maps per file (populated lazily)
    _line_map_cache: dict[str, dict[str, int]] = {}

    def get_line(file_path: str, name: str) -> int:
        if file_path not in _line_map_cache:
            _line_map_cache[file_path] = _build_line_map(file_path)
        return _line_map_cache[file_path].get(name, 1)

    def resolve_file(schema_id: str) -> str:
        return schema_file_map.get(schema_id, schema_path)

    issues: list[LintIssue] = []

    # Build set of TOP-LEVEL named slot names (from schema `slots:` sections only).
    # sv.all_slots() also returns attribute-defined slots; we process those separately
    # via cls_def.attributes to avoid double-reporting and incorrect LINT-08 triggers.
    top_level_slot_names: set[str] = set()
    for schema_def in sv.all_schema(imports=True):
        for slot_name in (schema_def.slots or {}).keys():
            top_level_slot_names.add(slot_name)

    # --- Build slot usage map for LINT-08 (named slots → count of classes that reference them) ---
    from collections import defaultdict

    slot_usage: dict[str, int] = defaultdict(int)
    for cls_def in sv.all_classes().values():
        for s in cls_def.slots or []:
            slot_usage[s] += 1

    # --- Validate classes ---
    for name, cls_def in sv.all_classes().items():
        schema_id = getattr(cls_def, "from_schema", "")
        if not _is_cdm_schema(schema_id):
            continue
        file_path = resolve_file(schema_id)
        line = get_line(file_path, name)

        naming_issue = _validate_class_naming(name, file_path, line, baseline)
        if naming_issue:
            issues.append(naming_issue)

        metadata_issues = _validate_class_metadata(
            name, cls_def, file_path, line, baseline
        )
        issues.extend(metadata_issues)

        grid_issue = _validate_grid_annotation(name, cls_def, file_path, line, baseline)
        if grid_issue:
            issues.append(grid_issue)

        # Validate inline attribute slots (class-specific naming required)
        for attr_name, attr_def in (cls_def.attributes or {}).items():
            attr_schema_id = getattr(attr_def, "from_schema", schema_id)
            if not _is_cdm_schema(attr_schema_id):
                continue
            if _is_naming_exempt(attr_name, baseline):
                continue  # annotation slot exempt from LINT-04
            attr_file = resolve_file(attr_schema_id)
            attr_line = get_line(attr_file, attr_name)
            naming_issue = _validate_slot_naming(
                attr_name, attr_file, attr_line, baseline, is_shared=False
            )
            if naming_issue:
                issues.append(naming_issue)

            # CONV-01: slot_uri format for class-specific attributes
            conv01_issue = _validate_slot_uri_format(
                attr_name,
                attr_def,
                attr_file,
                attr_line,
                baseline,
                is_class_specific=True,
            )
            if conv01_issue:
                issues.append(conv01_issue)

            # CONV-02: alias and title format
            alias_issue = _validate_alias_format(
                attr_name, attr_def, attr_file, attr_line, baseline
            )
            if alias_issue:
                issues.append(alias_issue)
            title_issue = _validate_title_format(
                attr_name, attr_def, attr_file, attr_line, baseline
            )
            if title_issue:
                issues.append(title_issue)

            # LINT-06: required slot metadata completeness for inline attributes
            metadata_issues = _validate_slot_metadata(
                attr_name, attr_def, attr_file, attr_line, baseline
            )
            issues.extend(metadata_issues)

    # --- Validate named slots (top-level slots: section only) ---
    for name, slot_def in sv.all_slots().items():
        if name not in top_level_slot_names:
            continue  # Skip attribute-defined slots; they are validated in the class loop above
        schema_id = getattr(slot_def, "from_schema", "")
        if not _is_cdm_schema(schema_id):
            continue
        file_path = resolve_file(schema_id)
        line = get_line(file_path, name)

        naming_issue = _validate_slot_naming(
            name, file_path, line, baseline, is_shared=True
        )
        if naming_issue:
            if not _is_naming_exempt(name, baseline):
                issues.append(naming_issue)

        metadata_issues = _validate_slot_metadata(
            name, slot_def, file_path, line, baseline
        )
        issues.extend(metadata_issues)

        grid_issue = _validate_grid_annotation(
            name, slot_def, file_path, line, baseline
        )
        if grid_issue:
            issues.append(grid_issue)

        # CONV-02: alias and title format (shared slots also need valid format when present)
        alias_issue = _validate_alias_format(name, slot_def, file_path, line, baseline)
        if alias_issue:
            issues.append(alias_issue)
        title_issue = _validate_title_format(name, slot_def, file_path, line, baseline)
        if title_issue:
            issues.append(title_issue)

        # LINT-08: flag single-use named slots as migration candidates
        single_use_issue = _validate_single_use_slot(
            name, file_path, line, slot_usage.get(name, 0)
        )
        if single_use_issue:
            issues.append(single_use_issue)

    # --- Validate URL convention (IRI-CONV-01, IRI-CONV-02) ---
    all_baseline_elements: set[str] = set()
    for s in baseline.values():
        all_baseline_elements.update(s)
    issues.extend(validate_url_convention(sv, all_baseline_elements))

    return issues


# ---------------------------------------------------------------------------
# Baseline writer (--baseline-out)
# ---------------------------------------------------------------------------

import re as _re


def _write_baseline(issues: list[LintIssue], path: str) -> None:
    """Write current violations as a new baseline YAML to *path*.

    Groups issues by violation type and element name.
    LINT-08 (warnings) are skipped — advisory only.
    """
    import collections

    _class_name_re = _re.compile(r"class name '([^']+)'")
    _slot_name_re = _re.compile(r"slot name '([^']+)'")
    _field_re = _re.compile(r"missing required metadata field '([^']+)'")
    _element_re = _re.compile(r"element '([^']+)'")

    buckets: dict[str, list[str]] = collections.defaultdict(list)

    for issue in issues:
        if issue.rule_id == "LINT-08":
            continue  # advisory warnings — not tracked in baseline

        if issue.rule_id == "LINT-03":
            m = _class_name_re.search(issue.message)
            key = "naming_class"
            elem = m.group(1) if m else "unknown"

        elif issue.rule_id == "LINT-04":
            m = _slot_name_re.search(issue.message)
            key = "naming"
            elem = m.group(1) if m else "unknown"

        elif issue.rule_id in ("LINT-05", "LINT-06"):
            m = _field_re.search(issue.message)
            field = m.group(1) if m else "unknown"
            key = f"missing_metadata.{field}"
            # Extract element name: "class 'X'" or "slot 'X'"
            em = _re.search(r"(?:class|slot) '([^']+)'", issue.message)
            elem = em.group(1) if em else "unknown"

        elif issue.rule_id == "LINT-07":
            m = _element_re.search(issue.message)
            key = "grid_format"
            elem = m.group(1) if m else "unknown"

        else:
            continue  # unknown rule — skip

        if elem not in buckets[key]:
            buckets[key].append(elem)

    # Sort each bucket
    for k in buckets:
        buckets[k].sort()

    # Build YAML manually to control ordering and formatting
    lines = [
        "# cdm-lint baseline — auto-generated from current schema violations",
        "# Elements listed here emit warnings instead of errors.",
        "# Remove an entry once the violation is fixed.",
        "",
    ]

    # Preferred key order: naming_class, naming, grid_format, then missing_metadata.*
    ordered_keys = ["naming_class", "naming", "grid_format"]
    meta_keys = sorted(k for k in buckets if k.startswith("missing_metadata."))
    ordered_keys += meta_keys

    # Include any remaining keys
    remaining = [k for k in sorted(buckets) if k not in ordered_keys]
    ordered_keys += remaining

    # Build nested structure for missing_metadata.*
    top: dict[str, object] = {}
    for k in ordered_keys:
        if k not in buckets:
            continue
        if "." in k:
            parent, child = k.split(".", 1)
            if parent not in top:
                top[parent] = {}
            top[parent][child] = buckets[k]  # type: ignore[index]
        else:
            top[k] = buckets[k]

    # Preserve naming_exempt_annotations — this section is manually curated and
    # never generated from live violations, so it must be round-tripped explicitly.
    # The hard-coded _NAMING_EXEMPT_ANNOTATIONS set is authoritative; we also
    # write it to the baseline YAML so it's visible and editable by humans.
    top["naming_exempt_annotations"] = sorted(_NAMING_EXEMPT_ANNOTATIONS)

    def _emit(data: dict, indent: int = 0) -> list[str]:
        out: list[str] = []
        pad = "  " * indent
        for k, v in data.items():
            if isinstance(v, dict):
                out.append(f"{pad}{k}:")
                out.extend(_emit(v, indent + 1))
            elif isinstance(v, list):
                out.append(f"{pad}{k}:")
                for item in v:
                    out.append(f"{pad}  - {item}")
            else:
                out.append(f"{pad}{k}: {v}")
        return out

    lines.extend(_emit(top))

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main() -> None:
    """Entry point for the `cdm-lint` CLI command. Full arg parsing wired in Plan 02."""
    import argparse

    parser = argparse.ArgumentParser(
        prog="cdm-lint",
        description="CDM Convention Linter — validates CDM schema YAML against AGENTS.md rules",
    )
    parser.add_argument(
        "schema",
        nargs="?",
        default="src/common_data_model/schema/common_data_model.yaml",
        help="Path to root schema YAML (default: CDM root)",
    )
    parser.add_argument(
        "--config",
        default="cdm-lint.yaml",
        help="Baseline violations config (default: cdm-lint.yaml)",
    )
    parser.add_argument(
        "--baseline-out",
        metavar="PATH",
        help="Write current violations as a new baseline YAML to PATH and exit 0",
    )
    args = parser.parse_args()

    issues = run_lint(args.schema, args.config)

    if args.baseline_out:
        _write_baseline(issues, args.baseline_out)
        sys.exit(0)

    error_count = 0
    for issue in sorted(issues, key=lambda i: (i.file, i.line)):
        print(str(issue))
        if issue.severity == "error":
            error_count += 1

    if error_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
