"""
cdm-gen-reference — generate the reference tables, the glossary and the documentation coverage page
from the schema: relations, prefixes, GRID templates, core class hierarchy, glossary, coverage.
Output is deterministic (sorted, no timestamps other than the API snapshot retrieval date).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, Optional, Union

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_snapshot import DEFAULT_API_DIR, load_snapshots
from cdm_tools.coverage import (
    NO_SUBSET, SubsetCoverage, is_concrete_domain_class, load_findings, subset_coverage, total_coverage,
)
from cdm_tools.hub import MAPPING_FIELDS, PREDICATES, build_hub, build_mapping, load_api_layers, schema_namespaces
from cdm_tools.registry import DEFAULT_REGISTRY_PATH, RegistryError, load_registry

FINDINGS_URL = "https://github.com/AltiumDeveloper/cdm/blob/main/MODEL-FINDINGS.md"
VIOLATIONS_URL = "https://github.com/AltiumDeveloper/cdm/blob/main/VIOLATIONS.md"
DEFAULT_FINDINGS_PATH = "MODEL-FINDINGS.md"
SENTENCE_END = re.compile(r"(?<!\be\.g)(?<!\bi\.e)\. ")   # "e.g. " and "i.e. " do not end a sentence
SUBSET_NAMESPACE = re.compile(r"^https://w3id\.org/altium/cdm/([^/]+)/$")


def _esc(text: str) -> str:
    """Make *text* safe inside a markdown table cell."""
    return " ".join(str(text).split()).replace("|", "\\|")


def _table(header: list[str], rows: Iterable[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return lines


def _first_sentence(description) -> str:
    text = " ".join(str(description or "").split())
    if not text or text.upper() == "TBD":
        return ""
    m = SENTENCE_END.search(text)
    return text[:m.start() + 1] if m else text


def _class_link(name: str, prefix: str, sv) -> str:
    return f"[{name}]({prefix}classes/{name}.md)" if name in sv.all_classes() else name


def _slot_link(name: str, prefix: str, sv) -> str:
    return f"[{name}]({prefix}slots/{name}.md)" if name in sv.all_slots() else name


# ---------------------------------------------------------------- relations

def _relation_slots(sv) -> dict:
    slots = {n: s for n, s in sv.all_slots().items() if n.startswith("core_")}
    found: dict = {}
    changed = True
    while changed:
        changed = False
        for name, slot in slots.items():
            if name not in found and (slot.abstract or (slot.is_a and str(slot.is_a) in found)):
                found[name] = slot
                changed = True
    return found


def _resolve(slots: dict, name: str, attr: str):
    """Value of *attr* for slot *name*, taken from the nearest slot on its is_a chain; (value, inherited)."""
    seen, current = set(), name
    while current in slots and current not in seen:
        seen.add(current)
        value = getattr(slots[current], attr, None)
        if value:
            return value, current != name
        current = str(slots[current].is_a) if slots[current].is_a else None
    return None, False


def write_relations(sv, registry, namespaces, path: Path) -> None:
    slots = _relation_slots(sv)
    inverses: dict[str, set[str]] = {n: set() for n in slots}
    for name, slot in slots.items():
        if slot.inverse:
            inverses[name].add(str(slot.inverse))
            if str(slot.inverse) in inverses:
                inverses[str(slot.inverse)].add(name)
    rows = []
    for name in sorted(slots):
        slot = slots[name]
        note = " *(inherited)*"
        ends = []
        for attr in ("domain", "range"):
            value, inherited = _resolve(slots, name, attr)
            if value:
                ends.append(_class_link(str(value), "../", sv) + (note if inherited else ""))
        transitive, trans_inherited = _resolve(slots, name, "transitive")
        maps = []
        for rel, attr in MAPPING_FIELDS:
            for value in getattr(slot, attr, None) or []:
                m = build_mapping(rel, str(value), registry, namespaces)
                maps.append(f"{rel}: [{_esc(m.text)}]({m.url})" if m.url else f"{rel}: {_esc(m.text)}")
        rows.append([
            _slot_link(name, "../", sv), _esc(slot.alias or ""), " → ".join(ends),
            ", ".join(_slot_link(i, "../", sv) for i in sorted(inverses[name])),
            ("yes" + (note if trans_inherited else "")) if transitive else "",
            _slot_link(str(slot.is_a), "../", sv) if slot.is_a else "",
            "; ".join(maps),
        ])
    lines = ["# Relation types", "",
             "Abstract relation slots defined in the core schema and their specialisations there. Domain "
             "relations specialise one of these through `is_a`; an inverse is shown when either side declares it.", ""]
    lines += _table(["Slot", "Alias", "Domain → Range", "Inverse", "Transitive", "Is a", "Mappings"], rows)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- prefixes

def write_prefixes(sv, path: Path) -> None:
    prefixes: dict[str, str] = {}
    for schema in sv.all_schema(imports=True):
        for prefix in (schema.prefixes or {}).values():
            prefixes.setdefault(str(prefix.prefix_prefix), str(prefix.prefix_reference))
    subsets = {str(s) for s in sv.all_subsets()}
    rows = []
    for prefix in sorted(prefixes):
        ns = prefixes[prefix]
        m = SUBSET_NAMESPACE.match(ns)
        owner = ""
        if m:
            owner = f"[{m.group(1)}](../subsets/{m.group(1)}.md)" if m.group(1) in subsets else m.group(1)
        rows.append([f"`{prefix}`", f"`{ns}`", owner])
    lines = ["# Prefixes", "", "Every prefix declared by the schema files, with the bounded context that owns "
             "the namespace where it has the form `https://w3id.org/altium/cdm/<subset>/`.", ""]
    lines += _table(["Prefix", "Namespace", "Bounded context"], rows)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- GRID templates

def _grid_parts(template: str) -> tuple[str, str]:
    parts = template.split(":")
    return (parts[1], parts[3]) if len(parts) >= 5 and parts[0] == "grid" else ("(unparsed)", "(unparsed)")


def write_grid_templates(sv, path: Path) -> None:
    by_context: dict[str, list[tuple[str, str]]] = {}
    areas: dict[str, int] = {}
    for name, cls in sv.all_classes().items():
        ann = cls.annotations or {}
        if "grid" not in ann:
            continue
        template = str(ann["grid"].value)
        area, context = _grid_parts(template)
        by_context.setdefault(context, []).append((name, template))
        areas[area] = areas.get(area, 0) + 1
    lines = ["# GRID templates", "",
             "Format: `grid:area:[tenant-id]:context:resource-type/resource-id`. Templates are informational "
             "and are declared per class in the `grid` annotation.", "", "## Areas", ""]
    lines += _table(["Area", "Classes"], [[f"`{a}`", str(areas[a])] for a in sorted(areas)])
    for context in sorted(by_context):
        lines += ["", f"## {context}", ""]
        lines += _table(["Class", "GRID template"],
                        [[_class_link(n, "../", sv), f"`{t}`"] for n, t in sorted(by_context[context])])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- class hierarchy

def write_class_hierarchy(sv, path: Path) -> None:
    nodes = {n: c for n, c in sv.all_classes().items() if n == "Any" or n.startswith("core_")}
    children: dict[str, list[str]] = {}
    roots = []
    for name in sorted(nodes):
        parent = str(nodes[name].is_a) if nodes[name].is_a else None
        if parent in nodes:
            children.setdefault(parent, []).append(name)
        else:
            roots.append(name)
    out: list[str] = []

    def emit(name: str, depth: int) -> None:
        mixins = [str(m) for m in (nodes[name].instantiates or [])]
        suffix = f"  [instantiates: {', '.join(mixins)}]" if mixins else ""
        out.append("  " * depth + name + suffix)
        for child in children.get(name, []):
            emit(child, depth + 1)

    for root in roots:
        emit(root, 0)
    lines = ["# Core class hierarchy", "",
             "Base classes and mixins of the core schema. Mixins are attached with `instantiates`, not `is_a`.",
             "", "```text"] + out + ["```"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- glossary

def write_glossary(sv, registry, platform, nexar_types, namespaces, path: Path) -> None:
    entries: dict[str, dict[str, dict]] = {}     # casefold term -> class name -> entry
    display: dict[str, str] = {}
    for name, cls in sorted(sv.all_classes().items()):
        if not is_concrete_domain_class(name, cls):
            continue
        hub = build_hub(cls, registry=registry, platform=platform, nexar_types=nexar_types, namespaces=namespaces)
        title = str(cls.title or "").strip()
        terms = ([(title, "title")] if title else []) + [(t.text, t.predicate or "alias") for t in hub.terms]
        for text, kind in terms:
            key = text.casefold()
            display.setdefault(key, text)
            entries.setdefault(key, {}).setdefault(name, {
                "kind": kind, "title": title or name,
                "subset": str(cls.in_subset[0]) if cls.in_subset else NO_SUBSET,
                "sentence": _first_sentence(cls.description),
                "doc": f"[{_esc(hub.links[0].text)}]({hub.links[0].url})" if hub.links else "",
            })
    by_letter: dict[str, list[str]] = {}
    for key in sorted(entries):
        first = display[key][0].upper()
        by_letter.setdefault(first if first.isalpha() else "#", []).append(key)
    lines = ["# Glossary", "",
             "Product terms and class names of the model. A term used by several classes is listed with each meaning."]
    for letter in sorted(by_letter, key=lambda c: (c == "#", c)):
        keys = by_letter[letter]
        rows, notes = [], []
        for key in keys:
            classes = entries[key]
            if len(classes) == 1:
                (name, e), = classes.items()
                rows.append([_esc(display[key]), f"[{_esc(e['title'])}](classes/{name}.md)", _esc(e["subset"]),
                             _esc(e["kind"]), e["doc"]])
            else:
                notes += ["", f'!!! note "{display[key].replace(chr(34), chr(39))} — {len(classes)} meanings"', ""]
                for name in sorted(classes):
                    e = classes[name]
                    tail = f"{e['subset']}. {e['sentence']}".rstrip() if e["sentence"] else f"{e['subset']}."
                    notes.append(f"    - [{e['title']}](classes/{name}.md) — {tail}")
        lines += ["", f"## {letter}", ""]
        if rows:
            lines += _table(["Term", "Class", "Bounded context", "Kind", "Product documentation"], rows)
        lines += notes
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- coverage

def _pct(part: int, whole: int) -> str:
    return f"{part} ({(part * 100 + whole // 2) // whole}%)" if whole else "0"


def write_coverage(sv, coverage: dict[str, SubsetCoverage], retrieved: Optional[str], path: Path) -> None:
    subsets = {str(s) for s in sv.all_subsets()}

    def row(label: str, c: SubsetCoverage) -> list[str]:
        return [label, str(c.classes), _pct(c.with_docs, c.classes), _pct(c.with_api, c.classes),
                _pct(c.with_terms, c.classes), _pct(c.with_mappings, c.classes), str(c.tbd),
                str(c.findings_open), str(c.findings_pending)]

    rows = [row(f"[{n}](subsets/{n}.md)" if n in subsets else n, coverage[n]) for n in sorted(coverage)]
    rows.append(row("**Total**", total_coverage(coverage)))
    lines = ["# Documentation coverage", "",
             "Concrete classes of each bounded context that carry product documentation links, a Platform API "
             "or Nexar type, product terms and standards mappings. Each class is counted in its first subset.", ""]
    if retrieved:
        lines += [f"Platform API snapshot retrieved: {retrieved}.", ""]
    lines += _table(["Bounded context", "Classes", "Product docs", "API type", "Product terms", "Standards mappings",
                     "TBD descriptions", "Open findings", "Fixed, pending review"], rows)
    lines += ["", f"Findings are tracked in [MODEL-FINDINGS.md]({FINDINGS_URL}); known naming violations in "
              f"[VIOLATIONS.md]({VIOLATIONS_URL}).", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------- driver

def build_reference(sv, *, registry_path: str, api_dir: str, findings_path: str, out_dir: Union[str, Path]) -> None:
    out = Path(out_dir)
    (out / "reference").mkdir(parents=True, exist_ok=True)
    registry = load_registry(registry_path)
    platform, nexar_types = load_api_layers(api_dir)
    namespaces = schema_namespaces(sv)
    coverage = subset_coverage(sv, platform_index=platform, nexar_types=nexar_types,
                               findings=load_findings(findings_path))
    write_relations(sv, registry, namespaces, out / "reference/relations.md")
    write_prefixes(sv, out / "reference/prefixes.md")
    write_grid_templates(sv, out / "reference/grid-templates.md")
    write_class_hierarchy(sv, out / "reference/class-hierarchy.md")
    write_glossary(sv, registry, platform, nexar_types, namespaces, out / "glossary.md")
    write_coverage(sv, coverage, load_snapshots(api_dir).get("platform", {}).get("retrieved"), out / "coverage.md")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-gen-reference", description=__doc__)
    parser.add_argument("schema")
    parser.add_argument("-o", "--output", required=True, help="Output directory (docs/)")
    parser.add_argument("--registry", default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--api-dir", default=DEFAULT_API_DIR)
    parser.add_argument("--findings", default=DEFAULT_FINDINGS_PATH)
    args = parser.parse_args(argv)
    if not Path(args.registry).is_file():
        print(f"cdm-gen-reference: link registry not found: {args.registry}", file=sys.stderr)
        return 2
    if not Path(args.api_dir).is_dir():
        print(f"cdm-gen-reference: API snapshot directory not found: {args.api_dir}", file=sys.stderr)
        return 2
    if not Path(args.findings).is_file():
        print(f"cdm-gen-reference: findings file not found: {args.findings}", file=sys.stderr)
        return 2
    try:
        build_reference(SchemaView(args.schema), registry_path=args.registry, api_dir=args.api_dir,
                        findings_path=args.findings, out_dir=args.output)
    except RegistryError as exc:
        print(f"cdm-gen-reference: invalid link registry: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
