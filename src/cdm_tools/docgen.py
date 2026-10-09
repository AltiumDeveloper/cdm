"""
cdm-gendoc — LinkML gen-doc with CDM documentation-hub helpers available to templates.

Adds the Jinja globals `doc_link(url)` (a markdown link titled from the link registry) and
`hub(element)` (the documentation-hub view of a class).
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

from jinja2 import Environment
from linkml.generators.docgen import DocGenerator
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_snapshot import DEFAULT_API_DIR
from cdm_tools.contexts import BC_ORDER, api_context
from cdm_tools.hub import build_hub, load_api_layers, schema_namespaces
from cdm_tools.reference import grid_templates
from cdm_tools.registry import DEFAULT_REGISTRY_PATH, LinkEntry, RegistryError, load_registry, split_url


@dataclass
class SubsetHub:
    """Overview of one bounded context for its page."""

    links: list[str] = field(default_factory=list)
    grid: list[tuple[str, str]] = field(default_factory=list)
    product_docs_none: bool = False
    iri: Optional[str] = None
    api: Optional[tuple[str, str]] = None   # (title, URL) of the bounded context in the Altium 365 API reference


def darken(color: str, amount: float = 0.35) -> str:
    """A darker shade of a #rrggbb colour (mixed with black by *amount*), e.g. a node border for a fill colour."""
    value = color.strip().lstrip("#")
    if len(value) != 6:
        return color
    channels = [int(value[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(c * (1 - amount)):02x}" for c in channels)


def text_on(color: str) -> str:
    """Readable text colour on a #rrggbb fill: white or near-black, whichever has the higher WCAG contrast ratio."""
    value = color.strip().lstrip("#")
    if len(value) != 6:
        return "#14181f"

    def linear(c: int) -> float:
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (linear(int(value[i:i + 2], 16)) for i in (0, 2, 4))
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    dark = 0.0089   # relative luminance of #14181f
    on_white, on_dark = 1.05 / (luminance + 0.05), (luminance + 0.05) / (dark + 0.05)
    return "#ffffff" if on_white > on_dark else "#14181f"


def subset_iri(sv: SchemaView, name: str) -> str:
    """IRI of a bounded context: the root schema IRI followed by the subset name, without a trailing slash
    (https://w3id.org/altium/cdm/design). Subsets have no IRI of their own in LinkML; this form is the one w3id.org
    resolves to the subset page."""
    return f"{str(sv.schema.id).rstrip('/')}/{name}"


def make_doc_link(registry: dict[str, LinkEntry]) -> Callable[[str], str]:
    def doc_link(url: str) -> str:
        base, _ = split_url(url)
        entry = registry.get(base)
        if entry is None:
            return f"<{url}>"
        return f"[{entry.text_for(url)}]({url})"

    return doc_link


@dataclass
class CdmDocGenerator(DocGenerator):
    registry_path: Optional[str] = None
    api_dir: Optional[str] = None

    def customize_environment(self, env: Environment) -> None:
        super().customize_environment(env)
        registry: dict[str, LinkEntry] = {}
        if self.registry_path and Path(self.registry_path).exists():
            registry = load_registry(self.registry_path)
        env.globals["doc_link"] = make_doc_link(registry)
        env.globals["bc_order"] = BC_ORDER
        env.filters["darken"] = darken
        env.filters["text_on"] = text_on
        platform, nexar_types = (
            load_api_layers(self.api_dir) if self.api_dir and Path(self.api_dir).is_dir() else (None, None)
        )
        namespaces = schema_namespaces(self.schemaview)
        env.globals["hub"] = lambda element: build_hub(
            element, registry=registry, platform=platform, nexar_types=nexar_types, namespaces=namespaces
        )
        self._register_subset_hub(env)

    def _register_subset_hub(self, env: Environment) -> None:
        sv = self.schemaview
        cache: dict[str, SubsetHub] = {}

        def subset_hub(element) -> SubsetHub:
            name = str(element.name)
            if name not in cache:
                grid = [(c, t) for c, subset, _, t in grid_templates(sv) if subset == name]
                cache[name] = SubsetHub(
                    links=[str(u) for u in (element.see_also or [])],
                    grid=sorted(grid),
                    product_docs_none="productDocs" in element.annotations
                    and str(element.annotations["productDocs"].value) == "none",
                    iri=subset_iri(sv, name),
                    api=api_context(name),
                )
            return cache[name]

        env.globals["subset_hub"] = subset_hub


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-gendoc", description=__doc__)
    parser.add_argument("schema", help="Root schema YAML")
    parser.add_argument("-d", "--directory", required=True, help="Output directory")
    parser.add_argument("--template-directory", required=True)
    parser.add_argument("--registry", default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--api-dir", default=DEFAULT_API_DIR)
    args = parser.parse_args(argv)
    if not Path(args.api_dir).is_dir():
        print(f"cdm-gendoc: API snapshot directory not found: {args.api_dir}", file=sys.stderr)
        return 2
    if not Path(args.registry).exists():
        print(f"cdm-gendoc: link registry not found: {args.registry}", file=sys.stderr)
        return 2
    try:
        load_registry(args.registry)
    except RegistryError as exc:
        print(f"cdm-gendoc: invalid link registry: {exc}", file=sys.stderr)
        return 2
    gen = CdmDocGenerator(
        args.schema,
        template_directory=args.template_directory,
        subfolder_type_separation=True,
        preserve_names=True,
        registry_path=args.registry,
        api_dir=args.api_dir,
    )
    gen.serialize(directory=args.directory)
    return 0
