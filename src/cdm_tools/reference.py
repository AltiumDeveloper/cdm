"""
cdm-gen-reference — generate the reference tables, the glossary and the documentation coverage page
from the schema: relations, prefixes, core class hierarchy, glossary, coverage, and the GRID summary and catalogue.
Each reference table is also written without its H1 to `_snippets/` for inclusion in top-level pages; the GRID
summary and catalogue are written only as snippets, for the GRIDs page.
Output is deterministic (sorted, no timestamps other than the API snapshot retrieval date).
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Callable, Iterable, Optional, Union

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
SNIPPETS_DIR = "_snippets"
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


def relations_body(sv, registry, namespaces, prefix: str) -> list[str]:
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
                ends.append(_class_link(str(value), prefix, sv) + (note if inherited else ""))
        transitive, trans_inherited = _resolve(slots, name, "transitive")
        maps = []
        for rel, attr in MAPPING_FIELDS:
            for value in getattr(slot, attr, None) or []:
                m = build_mapping(rel, str(value), registry, namespaces)
                maps.append(f"{rel}: [{_esc(m.text)}]({m.url})" if m.url else f"{rel}: {_esc(m.text)}")
        rows.append([
            _slot_link(name, prefix, sv), _esc(slot.alias or ""), " → ".join(ends),
            ", ".join(_slot_link(i, prefix, sv) for i in sorted(inverses[name])),
            ("yes" + (note if trans_inherited else "")) if transitive else "",
            _slot_link(str(slot.is_a), prefix, sv) if slot.is_a else "",
            "; ".join(maps),
        ])
    lines = ["Abstract relation slots defined in the core schema and their specialisations there. Domain "
             "relations specialise one of these through `is_a`; an inverse is shown when either side declares it.", ""]
    return lines + _table(["Slot", "Alias", "Domain → Range", "Inverse", "Transitive", "Is a", "Mappings"], rows)


# ---------------------------------------------------------------- prefixes

def prefixes_body(sv, prefix: str) -> list[str]:
    prefixes: dict[str, str] = {}
    for schema in sv.all_schema(imports=True):
        for declared in (schema.prefixes or {}).values():
            prefixes.setdefault(str(declared.prefix_prefix), str(declared.prefix_reference))
    subsets = {str(s) for s in sv.all_subsets()}
    rows = []
    for name in sorted(prefixes):
        ns = prefixes[name]
        m = SUBSET_NAMESPACE.match(ns)
        owner = ""
        if m:
            owner = f"[{m.group(1)}]({prefix}subsets/{m.group(1)}.md)" if m.group(1) in subsets else m.group(1)
        rows.append([f"`{name}`", f"`{ns}`", owner])
    lines = ["Every prefix declared by the schema files, with the bounded context that owns "
             "the namespace where it has the form `https://w3id.org/altium/cdm/<subset>/`.", ""]
    return lines + _table(["Prefix", "Namespace", "Bounded context"], rows)


# ---------------------------------------------------------------- GRID templates

def _grid_parts(template: str) -> tuple[str, str]:
    parts = template.split(":")
    return (parts[1], parts[3]) if len(parts) >= 5 and parts[0] == "grid" else ("(unparsed)", "(unparsed)")


def grid_templates(sv) -> list[tuple[str, str, str, str]]:
    """(class name, first subset, GRID context, template) for every class with a non-empty `grid` annotation."""
    rows = []
    for name, cls in sv.all_classes().items():
        ann = cls.annotations or {}
        value = ann["grid"].value if "grid" in ann else None
        template = "" if value is None else str(value).strip()
        if not template:
            continue
        subset = str(cls.in_subset[0]) if cls.in_subset else ""
        rows.append((str(name), subset, _grid_parts(template)[1], template))
    return rows


def _grid_resource_type(template: str) -> str:
    """Resource types of a template's resource path: `part/{id}/offer/{offerID}` -> `part/offer`."""
    parts = template.split(":", 4)
    if len(parts) < 5 or parts[0] != "grid":
        return "(unparsed)"
    return "/".join(parts[4].split("/")[0::2])


def _anchor(text: str) -> str:
    """Heading id as generated by the default MkDocs (Python-Markdown toc) slugify."""
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def _grid_by_subset(sv) -> dict[str, list[tuple[str, str, str]]]:
    """Bounded context (first subset) -> sorted (class name, GRID context, template)."""
    groups: dict[str, list[tuple[str, str, str]]] = {}
    for name, subset, context, template in grid_templates(sv):
        groups.setdefault(subset or NO_SUBSET, []).append((name, context, template))
    return {k: sorted(groups[k]) for k in sorted(groups, key=lambda k: (k.casefold(), k))}


def _subset_page(subset: str, prefix: str, sv, text: str) -> str:
    return f"[{text}]({prefix}subsets/{subset}.md)" if subset in {str(s) for s in sv.all_subsets()} else ""


def _codes(values: Iterable[str]) -> str:
    return ", ".join(f"`{v}`" for v in sorted(set(values)))


def grid_summary_body(sv, prefix: str) -> list[str]:
    rows, areas = [], {}
    for subset, entries in _grid_by_subset(sv).items():
        page = _subset_page(subset, prefix, sv, "overview")
        label = f"[{_esc(subset)}](#{_anchor(subset)})" + (f" ({page})" if page else "")
        rows.append([label, _codes(c for _, c, _ in entries), _codes(_grid_parts(t)[0] for _, _, t in entries),
                     str(len(entries)), _codes(_grid_resource_type(t) for _, _, t in entries)])
        for _, _, template in entries:
            area = _grid_parts(template)[0]
            areas[area] = areas.get(area, 0) + 1
    lines = ["Classes with a GRID template, grouped by bounded context (the first subset of the class). "
             "The bounded context links to its catalogue section below and to its overview page.", ""]
    lines += _table(["Bounded context", "GRID context", "Area", "Classes", "Resource types"], rows)
    lines += ["", "Classes with a GRID template per area:", ""]
    return lines + _table(["Area", "Classes"], [[f"`{a}`", str(areas[a])] for a in sorted(areas)])


def grid_catalogue_body(sv, prefix: str) -> list[str]:
    lines: list[str] = []
    classes = sv.all_classes()
    for subset, entries in _grid_by_subset(sv).items():
        lines += [f"### {subset}", ""]
        page = _subset_page(subset, prefix, sv, subset)
        if page:
            lines += [f"Bounded context page: {page}.", ""]
        rows = []
        for name, context, template in entries:
            title = str(classes[name].title or "").strip()
            cell = f"[{_esc(title)}]({prefix}classes/{name}.md) (`{name}`)" if title else _class_link(name, prefix, sv)
            rows.append([cell, f"`{template}`", f"`{context}`"])
        lines += _table(["Class", "GRID template", "GRID context"], rows) + [""]
    return lines[:-1] if lines else ["No class declares a GRID template."]


def write_snippet(out: Path, name: str, body: list[str]) -> None:
    """Write `_snippets/<name>.md` (no H1, links relative to the docs root)."""
    (out / SNIPPETS_DIR / f"{name}.md").write_text("\n".join(body) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- class hierarchy

def class_hierarchy_body(sv, prefix: str) -> list[str]:
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
    return ["Base classes and mixins of the core schema. Core mixins are attached with `instantiates`; domain mixins use `mixins:`. Neither uses `is_a`.",
            "", "```text"] + out + ["```"]


# ---------------------------------------------------------------- reference pages and snippets

def _demote(lines: list[str]) -> list[str]:
    """Headings one level down (outside fenced code), so a snippet nests under a section of the including page."""
    out, fenced = [], False
    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
        out.append("#" + line if not fenced and re.match(r"#+ ", line) else line)
    return out


def write_reference_page(out: Path, name: str, title: str, body: Callable[[str], list[str]]) -> None:
    """Write `reference/<name>.md` (a page with its own H1) and `_snippets/<name>.md` (no H1, headings demoted,
    links relative to the docs root) for inclusion with `--8<-- "docs/_snippets/<name>.md"` in top-level pages."""
    page = [f"# {title}", ""] + body("../")
    (out / "reference" / f"{name}.md").write_text("\n".join(page) + "\n", encoding="utf-8")
    (out / SNIPPETS_DIR / f"{name}.md").write_text("\n".join(_demote(body(""))) + "\n", encoding="utf-8")


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
    (out / SNIPPETS_DIR).mkdir(parents=True, exist_ok=True)
    registry = load_registry(registry_path)
    platform, nexar_types = load_api_layers(api_dir)
    namespaces = schema_namespaces(sv)
    coverage = subset_coverage(sv, platform_index=platform, nexar_types=nexar_types,
                               findings=load_findings(findings_path))
    write_reference_page(out, "relations", "Relation types",
                         lambda p: relations_body(sv, registry, namespaces, p))
    write_reference_page(out, "prefixes", "Prefixes", lambda p: prefixes_body(sv, p))
    write_snippet(out, "grid-summary", grid_summary_body(sv, ""))
    write_snippet(out, "grid-catalogue", grid_catalogue_body(sv, ""))
    write_reference_page(out, "class-hierarchy", "Core class hierarchy", lambda p: class_hierarchy_body(sv, p))
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
