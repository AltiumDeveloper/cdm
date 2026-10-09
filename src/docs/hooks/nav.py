"""
MkDocs hook: make every bounded context in the "Bounded Contexts" navigation section expandable, listing its
classes, as the Altium 365 API reference does.

mkdocs.yml lists the subset pages (subsets/<name>.md). Here each one becomes a section titled with the subset
title whose children are the subset page itself, as the section index (Material `navigation.indexes`), followed
by the pages of the subset's entity classes (descendants of core_Entity: Artifacts and Activities), sorted by
title. Resources, events, mixins and enumerations stay on the subset page. Where entity classes of a subset form a
hierarchy (e.g. BOM WIP with Managed BOM and Consolidated BOM), a subclass follows its parent and its page gets a
`cdm_depth`, which partials/nav-item.html turns into an indented item with a guide line (no expand/collapse).
Classes are read from the schema, so the sidebar follows it without edits to mkdocs.yml.
"""

from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView
from mkdocs.structure.nav import Section
from mkdocs.structure.pages import Page

SCHEMA = "src/common_data_model/schema/common_data_model.yaml"
SECTION_TITLE = "Bounded Contexts"
SUBSET_DIR = "subsets/"
ENTITY = "core_Entity"

_cache: dict = {}


class _SectionIndexPage(Page):
    """A subset page used as its section's index. Material attaches index pages by file name (index.md); subset
    pages are named after the subset, so the flag is set here instead."""

    @property
    def is_index(self) -> bool:
        return True


def _tree(view: SchemaView, names: list[str]) -> list[tuple[str, int]]:
    """*names* depth-first: a class follows its nearest ancestor (is_a) among *names*, siblings sorted by title.
    Returns (class name, depth) pairs; depth 0 is a class with no ancestor in *names*."""
    members = set(names)
    title = {n: (view.get_class(n).title or n).lower() for n in names}
    children: dict[str, list[str]] = {}
    roots = []
    for name in names:
        parent = next((a for a in view.class_ancestors(name, mixins=False, reflexive=False) if a in members), None)
        (children.setdefault(parent, []) if parent else roots).append(name)
    ordered: list[tuple[str, int]] = []

    def visit(name: str, depth: int) -> None:
        ordered.append((name, depth))
        for child in sorted(children.get(name, []), key=title.get):
            visit(child, depth + 1)

    for root in sorted(roots, key=title.get):
        visit(root, 0)
    return ordered


def _bounded_contexts(schema: Path) -> tuple[dict[str, str], dict[str, list[tuple[str, int]]]]:
    """(title by subset, entity classes by subset as (name, depth) in sidebar order), cached per schema mtime."""
    key = (schema, schema.stat().st_mtime)
    if _cache.get("key") != key:
        view = SchemaView(str(schema))
        titles = {name: s.title or name for name, s in view.all_subsets().items()}
        classes: dict[str, list[str]] = {}
        for name, cls in view.all_classes().items():
            if name == ENTITY or ENTITY not in view.class_ancestors(name, mixins=False):
                continue
            for subset in cls.in_subset or []:
                classes.setdefault(subset, []).append(name)
        _cache.update(key=key, value=(titles, {s: _tree(view, v) for s, v in classes.items()}))
    return _cache["value"]


def _walk(items):
    for item in items:
        yield item
        if isinstance(item, Section):
            yield from _walk(item.children)


def _set_parents(items, parent) -> None:
    for item in items:
        item.parent = parent
        if isinstance(item, Section):
            _set_parents(item.children, item)


def on_nav(nav, config, files):
    section = next((i for i in nav.items if isinstance(i, Section) and i.title == SECTION_TITLE), None)
    if section is None:
        return nav
    titles, classes = _bounded_contexts(Path(config.config_file_path).parent / SCHEMA)
    children = []
    for item in section.children:
        src = item.file.src_uri if isinstance(item, Page) else ""
        if not (src.startswith(SUBSET_DIR) and src.endswith(".md")):
            children.append(item)
            continue
        name = src[len(SUBSET_DIR):-len(".md")]
        item.__class__ = _SectionIndexPage
        pages = [item]
        for cls, depth in classes.get(name, []):
            file = files.get_file_from_path(f"classes/{cls}.md")
            if file is not None and file.page is not None:
                file.page.cdm_depth = depth   # read by partials/nav-item.html
                pages.append(file.page)
        context = Section(titles.get(name, name), pages)
        context.cdm_subset = name   # read by partials/nav-item.html (class bc-<subset>: colour and icon)
        children.append(context)
    section.children = children
    _set_parents(nav.items, None)

    # Previous / next links follow the new order
    pages = [item for item in _walk(nav.items) if isinstance(item, Page)]
    for previous, current in zip([None, *pages], pages):
        current.previous_page = previous
        if previous is not None:
            previous.next_page = current
    if pages:
        pages[-1].next_page = None
    nav.pages = pages
    return nav
