"""
cdm-gen-llms — generate the llms.txt files of the docs site (https://llmstxt.org/) from the schema, the hub data
and the documentation pages:

- `llms.txt` — summary, navigation guide and links to everything below;
- `llms/<subset>.md` — the catalogue of a bounded context, one line per concrete class;
- `llms/classes/<class>.md` — a card for every class: identity, description, hub data, GRID, attributes, references;
- `llms/pages/<page>.md` — the concept pages and the glossary as plain markdown, snippets inlined;
- `llms-full.txt` — all of the above in one file, with links relative to the site root.

Links are relative, so the files work wherever the site is served. Output is deterministic (no timestamps other
than the API snapshot retrieval date). Run after `cdm-gen-reference`, which writes the glossary and the snippets.
"""

from __future__ import annotations

import argparse
import posixpath
import re
import shutil
import sys
from pathlib import Path
from typing import Callable, Optional, Union

from linkml.generators.docgen import DocGenerator
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_links import DOCS_BASE
from cdm_tools.api_snapshot import DEFAULT_API_DIR, load_snapshots
from cdm_tools.coverage import is_concrete_domain_class
from cdm_tools.hub import OCTOPART_API_DOC, HubView, build_hub, doc_link, load_api_layers, schema_namespaces
from cdm_tools.reference import FINDINGS_URL, SENTENCE_END, _esc, _table, first_sentence, grid_templates, relation_slots
from cdm_tools.registry import DEFAULT_REGISTRY_PATH, LinkEntry, RegistryError, load_registry

REPO_URL = "https://github.com/AltiumDeveloper/cdm"
ALTIUM_365_API_DOC = "https://www.altium.com/documentation/altium-developer-center/altium-365/api"
# Pages published under llms/pages/, in the order of the "Start here" section: (slug, title in the nav, note)
PAGES = [
    ("about", "About", "what the CDM is: bounded contexts, kinds of entities, the API behind the model and the hub data"),
    ("grid-format", "GRIDs", "the GRID format, the GRID template of every class that declares one, prefixes and IRIs"),
    ("domain-model", "Domain Model", "how the schema is organised: base classes, relations, identity, names; the bounded contexts"),
    ("entity-classification", "Entity Classification", "the base classes Entity, Artifact, Activity, Resource "
                                                        "and Event, the mixins, and how a class is classified"),
    ("relation-types", "Relation Types", "the core relations, their inverses and mappings, and how domain relations specialise them"),
    ("glossary", "Glossary", "product terms and class names, with the class each one names"),
]
BASE_KINDS = [("core_Artifact", "Artifact"), ("core_Activity", "Activity"), ("core_Resource", "Resource"),
              ("core_Event", "Event"), ("core_Entity", "Entity")]
MAX_REFERENCES = 20
LINK = re.compile(r"\]\(([^)\s]+)\)")                    # target of a markdown link or image
SNIPPET = re.compile(r'^--8<-- "([^"]+)"\s*$')
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#)")      # scheme (http:, mailto:) or a same-page anchor


# ---------------------------------------------------------------- links

def _rewrite_links(text: str, fn: Callable[[str], str]) -> str:
    """Apply *fn* to every relative link target in *text*; external links and anchors stay unchanged."""
    return LINK.sub(lambda m: f"]({m.group(1) if EXTERNAL.match(m.group(1)) else fn(m.group(1))})", text)


def _page_target(target: str, subsets: set[str]) -> str:
    """Map a link of a docs page (relative to the docs root) to its llms equivalent, relative to llms/pages/."""
    path, sep, frag = target.partition("#")
    anchor = sep + frag
    folder, _, name = path.rpartition("/")
    stem = name[:-3] if name.endswith(".md") else None
    if folder == "classes" and stem:
        return f"../classes/{name}{anchor}"
    if folder == "subsets" and stem in subsets:
        return f"../{name}{anchor}"
    if not folder and stem in {p for p, _, _ in PAGES}:
        return f"{name}{anchor}"
    if path == "index.md":                               # the bounded contexts list is in llms.txt
        return "../../llms.txt"
    if stem is not None:                                 # other pages: the HTML page
        return f"../../{path[:-3]}/{anchor}"
    return f"../../{target}"


def _site_relative(path: str, target: str) -> str:
    """*target*, a link in the generated file *path*, as a link relative to the site root."""
    link, sep, frag = target.partition("#")
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), link))
    resolved = "./" if resolved == "." else resolved + ("/" if link.endswith("/") else "")
    return resolved + sep + frag


# ---------------------------------------------------------------- model

class _Model:
    """The schema with the hub data of every class, and the lookups shared by the generated files."""

    def __init__(self, sv, registry: dict[str, LinkEntry], api_dir: str) -> None:
        self.sv = sv
        self.registry = registry
        self.classes = sv.all_classes()
        platform, nexar_types = load_api_layers(api_dir)
        namespaces = schema_namespaces(sv)
        self.hubs: dict[str, HubView] = {
            n: build_hub(c, registry=registry, platform=platform, nexar_types=nexar_types, namespaces=namespaces)
            for n, c in self.classes.items()}
        self.retrieved = load_snapshots(api_dir).get("platform", {}).get("retrieved")
        self.grids = {name: template for name, _, _, template in grid_templates(sv)}
        self.relations = set(relation_slots(sv))
        self.subsets = {str(n): s for n, s in sv.all_subsets().items()}
        self.referenced_by = self._references()

    def subset_of(self, name: str) -> Optional[str]:
        cls = self.classes[name]
        return str(cls.in_subset[0]) if cls.in_subset else None

    def concrete(self, name: str) -> bool:
        return is_concrete_domain_class(name, self.classes[name])

    def title(self, name: str) -> str:
        return str(self.classes[name].title or "").strip() or name

    def kind(self, name: str) -> str:
        """Base kind (Artifact, Activity, ...) from the is_a ancestors, then 'abstract' / 'mixin'."""
        cls = self.classes[name]
        ancestors = set(self.sv.class_ancestors(name, mixins=False))
        parts = [next((k for base, k in BASE_KINDS if base in ancestors), "")]
        parts += ["abstract"] * bool(cls.abstract) + ["mixin"] * bool(cls.mixin)
        return ", ".join(p for p in parts if p)

    def ranges(self, slot) -> list[str]:
        if slot.any_of or slot.exactly_one_of:
            return [str(r) for r in self.sv.slot_range_as_union(slot) if str(r) != "Any"]
        return [str(slot.range)] if slot.range else []

    def relation(self, slot) -> str:
        """The nearest core relation on the is_a chain of *slot* (itself included), or ''."""
        name, seen = str(slot.name), set()
        parent = slot.is_a
        while name not in self.relations:
            if not parent or name in seen:
                return ""
            seen.add(name)
            name = str(parent)
            parent = self.sv.get_slot(name).is_a if self.sv.get_slot(name) else None
        return name

    def _references(self) -> dict[str, list[tuple[str, str]]]:
        """Class -> sorted (owning class, field) of the slots of other classes whose range includes it."""
        refs: dict[str, set[tuple[str, str]]] = {}
        for owner in sorted(self.classes):
            cls = self.classes[owner]
            for sn in list(cls.slots or []) + list(cls.attributes or {}):
                slot = self.sv.induced_slot(sn, owner)
                for target in self.ranges(slot):
                    if target in self.classes and target != owner:
                        refs.setdefault(target, set()).add((owner, str(slot.alias or sn)))
        return {k: sorted(v) for k, v in refs.items()}


# ---------------------------------------------------------------- class cards

def _hub_sections(hub: HubView) -> list[str]:
    lines: list[str] = []
    product = [f"- [{l.text}]({l.url})" + (" (primary)" if l.primary else "") for l in hub.links]
    for t in hub.terms:
        qualifiers = "; ".join(q for q in (t.predicate, ", ".join(t.contexts)) if q)
        product.append(f"- Term: **{t.text}**" + (f" ({qualifiers})" if qualifiers else ""))
    if hub.product_docs_none:
        product.append("- No public product documentation exists for this concept.")
    if product:
        lines += ["", "## In the product", ""] + product
    api = []
    if hub.api:
        name = f"[`{hub.api.type_name}`]({hub.api.url})" if hub.api.url else f"`{hub.api.type_name}`"
        api.append(f"- Platform API type: {name}" + (f" ({hub.api.kind.lower()})" if hub.api.kind else ""))
    if hub.api_missing:
        api.append(f"- Platform API type `{hub.api_missing}` is named by the class but is not in the API snapshot.")
    if hub.nexar:
        api.append(f"- Nexar type: `{hub.nexar.type_name}` ([Octopart API]({hub.nexar.url}))")
    if hub.nexar_missing:
        api.append(f"- Nexar type `{hub.nexar_missing}` is named by the class but is not in the Nexar snapshot.")
    if api:
        lines += ["", "## In the API", ""] + api
    if hub.mappings:
        lines += ["", "## In standards", ""]
        lines += [f"- {m.relation}: " + (f"[{m.text}]({m.url})" if m.url else f"`{m.text}`") for m in hub.mappings]
    return lines


def _attribute_rows(m: _Model, name: str) -> list[list[str]]:
    rows = []
    ancestors = set(m.sv.class_ancestors(name, reflexive=False))
    direct = set(m.sv.class_slots(name, direct=True))
    for slot in m.sv.class_induced_slots(name):
        ranges = [f"[{r}]({r}.md)" if r in m.classes else r for r in m.ranges(slot)]
        owners = [] if slot.name in direct else sorted(set(slot.domain_of or []) & ancestors)
        rows.append([_esc(slot.alias or slot.name), " or ".join(ranges), DocGenerator.cardinality(slot),
                     _esc(first_sentence(slot.description)), m.relation(slot),
                     ", ".join(f"[{o}]({o}.md)" for o in owners)])
    return rows


def class_card(m: _Model, name: str) -> str:
    cls = m.classes[name]
    subset = m.subset_of(name)
    facts = [f"- Name: `{name}`",
             f"- IRI: `{m.sv.get_uri(cls, expand=False)}` ({m.sv.get_uri(cls, expand=True)})"]
    if subset:
        facts.append(f"- Bounded context: [{subset}](../{subset}.md)")
    if m.kind(name):
        facts.append(f"- Kind: {m.kind(name)}")
    if cls.is_a:
        facts.append(f"- Is a: [{cls.is_a}]({cls.is_a}.md)")
    mixins = [str(x) for x in list(cls.mixins or []) + list(cls.instantiates or [])]
    if mixins:
        facts.append("- Mixins: " + ", ".join(f"[{x}]({x}.md)" if x in m.classes else x for x in mixins))
    ann = cls.annotations or {}
    if "maturity" in ann:
        facts.append(f"- Maturity: {ann['maturity'].value}")
    facts.append(f"- HTML page: [classes/{name}/](../../classes/{name}/)")
    lines = [f"# {m.title(name)}", ""] + facts
    description = " ".join(str(cls.description or "").split())
    if description and description.upper() != "TBD":
        lines += ["", description]
    if cls.comments:
        lines += ["", "## Comments", ""] + [f"- {' '.join(str(c).split())}" for c in cls.comments]
    lines += _hub_sections(m.hubs[name])
    if name in m.grids:
        lines += ["", "## GRID", "", f"`{m.grids[name]}`"]
    rows = _attribute_rows(m, name)
    if rows:
        lines += ["", "## Attributes", ""]
        lines += _table(["Field", "Range", "Cardinality", "Description", "Relation", "Inherited from"], rows)
    refs = m.referenced_by.get(name, [])
    if refs:
        lines += ["", "## Referenced by", ""]
        lines += [f"- [{owner}]({owner}.md): `{field}`" for owner, field in refs[:MAX_REFERENCES]]
        if len(refs) > MAX_REFERENCES:
            lines.append(f"- … and {len(refs) - MAX_REFERENCES} more (see the HTML page)")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- catalogues

def _api_label(hub: HubView) -> str:
    if hub.api:
        return f"API {hub.api.type_name}"
    return f"Nexar {hub.nexar.type_name}" if hub.nexar else ""


def _catalogue_line(m: _Model, name: str, parts: list[str]) -> str:
    notes = " · ".join(p for p in [first_sentence(m.classes[name].description)] + parts if p)
    return f"- [{m.title(name)}](classes/{name}.md)" + (f": {notes}" if notes else "")


def _members(m: _Model, subset: str) -> tuple[list[str], list[str]]:
    """(concrete classes sorted by title, other classes sorted by name) whose first subset is *subset*."""
    names = [n for n in m.classes if m.subset_of(n) == subset]
    concrete = sorted((n for n in names if m.concrete(n)), key=lambda n: (m.title(n).casefold(), n))
    return concrete, sorted(n for n in names if not m.concrete(n))


def catalogue(m: _Model, subset: str) -> str:
    s = m.subsets[subset]
    lines = [f"# Bounded context: {s.title or subset}", ""]
    if s.description:
        lines += [" ".join(str(s.description).split()), ""]
    lines += [f"HTML page: [subsets/{subset}/](../subsets/{subset}/)"]
    links = [doc_link(str(u), m.registry, i == 0) for i, u in enumerate(s.see_also or [])]
    ann = s.annotations or {}
    if links or ("productDocs" in ann and str(ann["productDocs"].value) == "none"):
        lines += ["", "## In the product", ""]
        lines += [f"- [{l.text}]({l.url})" + (" (primary)" if l.primary else "") for l in links]
        if not links:
            lines.append("No public product documentation exists for this bounded context.")
    concrete, others = _members(m, subset)
    if concrete:
        lines += ["", "## Classes", ""]
        for n in concrete:
            grid = f"GRID `{m.grids[n]}`" if n in m.grids else ""
            lines.append(_catalogue_line(m, n, [m.kind(n), _api_label(m.hubs[n]), grid]))
    if others:
        lines += ["", "## Base classes and mixins", ""] + [_catalogue_line(m, n, [m.kind(n)]) for n in others]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- pages

def _inline_snippets(text: str, base: Path) -> str:
    """Replace `--8<-- "path"` lines by the file they name (relative to *base*, the directory mkdocs runs in)."""
    out = []
    for line in text.splitlines():
        match = SNIPPET.match(line.strip())
        out.append((base / match.group(1)).read_text(encoding="utf-8").rstrip("\n") if match else line)
    return "\n".join(out) + "\n"


def page(docs_dir: Path, slug: str, subsets: set[str]) -> str:
    text = _inline_snippets((docs_dir / f"{slug}.md").read_text(encoding="utf-8"), docs_dir.parent)
    return _rewrite_links(text, lambda t: _page_target(t, subsets))


def _summary(about: str) -> str:
    """The first two sentences of the first paragraph of the About page, links flattened to their text."""
    paragraph = about.split("\n\n")[1] if about.startswith("# ") else about.split("\n\n")[0]
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", " ".join(paragraph.split()))
    ends = [mt.start() + 1 for mt in SENTENCE_END.finditer(text)]
    return text[:ends[1]] if len(ends) > 1 else text


# ---------------------------------------------------------------- llms.txt

def _context_note(m: _Model, subset: str) -> str:
    concrete, others = _members(m, subset)
    counts = [f"{len(concrete)} class" + "es" * (len(concrete) != 1)] if concrete else []
    if others:
        counts.append(f"{len(others)} " + ("base classes and mixins" if len(others) > 1 else "base class or mixin"))
    sentence = first_sentence(m.subsets[subset].description)
    return " ".join(p for p in (sentence, f"({'; '.join(counts)})" if counts else "") if p)


def llms_txt(m: _Model, about: str, repo_url: str) -> str:
    concrete = sum(m.concrete(n) for n in m.classes)
    info = [
        "This file follows https://llmstxt.org/. Links in it and in the files under `llms/` are relative to the "
        "file that contains them; `llms-full.txt` holds all of them in one file, with links relative to the site "
        "root.",
        "",
        f"The model has {len(m.classes)} classes in {len(m.subsets)} bounded contexts (LinkML subsets); "
        f"{concrete} of them are concrete domain classes, listed in the catalogues below, and the others are core, "
        "abstract and mixin classes.",
        "",
        "- Class names are `{prefix}_{ClassName}`, where the prefix is the short prefix of the bounded context "
        "(`lib_Component`, `des_Project`); class IRIs are `prefix:ClassName` (`lib:Component`). Class-specific "
        "slots are named `{prefix}_{ClassName}_{fieldName}`; the field name is the slot's `alias`, used as the "
        "JSON key.",
        "- Every domain class other than a mixin specialises a base class of the `core` subset: Artifact or "
        "Activity (entities, identified by a GRID), Resource (a lightweight object, usually part of an entity, "
        "with no GRID) or Event (a record of something that happened, with no GRID).",
        "- `llms/<bounded context>.md` lists the classes of a bounded context with their kind, API type and GRID "
        "template. `llms/classes/<class>.md` is a class card: name, IRI, bounded context, kind, parent and mixins; "
        "the description; product documentation and product terms (In the product); the Platform API or Nexar "
        "type (In the API); mappings to standards (In standards); the GRID template; the attributes with range, "
        "cardinality and the core relation each specialises; and the slots of other classes that refer to it.",
        "- `hub.json` holds the product, API and standards data and the GRID template of every concrete domain "
        "class.",
    ]
    if m.retrieved:
        info.append(f"- API types are checked against a snapshot of the Platform API schema retrieved on "
                    f"{m.retrieved}.")
    lines = ["# Altium Common Data Model (CDM)", "", f"> {_summary(about)}", ""] + info
    lines += ["", "## Start here", ""]
    lines += [f"- [{title}](llms/pages/{slug}.md): {note}" for slug, title, note in PAGES]
    lines += ["", "## Bounded contexts", ""]
    lines += [f"- [{s}](llms/{s}.md): {_context_note(m, s)}" for s in m.subsets]
    lines += ["", "## Machine-readable data", "",
              "- [hub.json](hub.json): product documentation links and terms, API type, standards mappings and "
              "GRID template of every concrete domain class",
              "- [hub.schema.json](hub.schema.json): JSON Schema of hub.json",
              "- [llms-full.txt](llms-full.txt): this file, the pages, the catalogues and all class cards in one file",
              "", "## Optional", "",
              "- [Documentation site](./): the HTML pages, including a page for every class, slot and enumeration",
              f"- [Platform API GraphQL documentation]({DOCS_BASE}/): the types, queries and mutations of the "
              "Platform API",
              f"- [{_registry_title(m, ALTIUM_365_API_DOC)}]({ALTIUM_365_API_DOC}): the GraphQL API to Altium 365 "
              "Workspace data, its endpoints and authentication",
              f"- [{_registry_title(m, OCTOPART_API_DOC)}]({OCTOPART_API_DOC}): the GraphQL API for supply chain "
              "data (Nexar types)",
              f"- [Schema repository]({repo_url}): the LinkML source (`src/common_data_model/schema/`) and the "
              "generators of JSON Schema, OWL, SHACL, GraphQL, Python and other artifacts",
              f"- [MODEL-FINDINGS.md]({FINDINGS_URL}): open questions where the model and the product "
              "documentation or standards disagree"]
    return "\n".join(lines) + "\n"


def _registry_title(m: _Model, url: str) -> str:
    return doc_link(url, m.registry, False).text


# ---------------------------------------------------------------- driver

def build_llms(schema_path: Union[str, Path], *, registry_path: Union[str, Path], api_dir: Union[str, Path],
               docs_dir: Union[str, Path], repo_url: str = REPO_URL) -> dict[str, str]:
    """Every generated file as {path relative to the site root: text}."""
    m = _Model(SchemaView(str(schema_path)), load_registry(registry_path), str(api_dir))
    docs = Path(docs_dir)
    pages = {slug: page(docs, slug, set(m.subsets)) for slug, _, _ in PAGES}
    files = {"llms.txt": llms_txt(m, (docs / "about.md").read_text(encoding="utf-8"), repo_url)}
    files |= {f"llms/pages/{slug}.md": text for slug, text in pages.items()}
    files |= {f"llms/{s}.md": catalogue(m, s) for s in m.subsets}
    files |= {f"llms/classes/{n}.md": class_card(m, n) for n in sorted(m.classes)}
    parts = [files["llms.txt"]]
    for path, text in files.items():
        if path != "llms.txt":
            parts.append(f"---\n\n# File: {path}\n\n" + _rewrite_links(text, lambda t, p=path: _site_relative(p, t)))
    files["llms-full.txt"] = "\n".join(parts)
    return files


def write_files(site_dir: Union[str, Path], files: dict[str, str]) -> None:
    """Write *files* under *site_dir*, replacing an existing llms/ directory."""
    site = Path(site_dir)
    shutil.rmtree(site / "llms", ignore_errors=True)
    for path, text in files.items():
        (site / path).parent.mkdir(parents=True, exist_ok=True)
        (site / path).write_text(text, encoding="utf-8")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-gen-llms", description=__doc__)
    parser.add_argument("schema")
    parser.add_argument("-o", "--output", required=True, help="Site directory")
    parser.add_argument("--registry", default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--api-dir", default=DEFAULT_API_DIR)
    parser.add_argument("--docs-dir", default="docs", help="Generated docs directory (after make gendoc)")
    parser.add_argument("--repo-url", default=REPO_URL)
    args = parser.parse_args(argv)
    if not Path(args.registry).is_file():
        print(f"cdm-gen-llms: link registry not found: {args.registry}", file=sys.stderr)
        return 2
    if not Path(args.api_dir).is_dir():
        print(f"cdm-gen-llms: API snapshot directory not found: {args.api_dir}", file=sys.stderr)
        return 2
    missing = [f"{slug}.md" for slug, _, _ in PAGES if not (Path(args.docs_dir) / f"{slug}.md").is_file()]
    if missing:
        print(f"cdm-gen-llms: pages not found in {args.docs_dir}: {', '.join(missing)}", file=sys.stderr)
        return 2
    try:
        files = build_llms(args.schema, registry_path=args.registry, api_dir=args.api_dir, docs_dir=args.docs_dir,
                           repo_url=args.repo_url)
    except RegistryError as exc:
        print(f"cdm-gen-llms: invalid link registry: {exc}", file=sys.stderr)
        return 2
    write_files(args.output, files)
    return 0


if __name__ == "__main__":
    sys.exit(main())
