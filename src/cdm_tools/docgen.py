"""
cdm-gendoc — LinkML gen-doc with CDM documentation-hub helpers available to templates.

Adds the Jinja globals `doc_link(url)` (a markdown link titled from the link registry) and
`hub(element)` (the documentation-hub view of a class).
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from jinja2 import Environment
from linkml.generators.docgen import DocGenerator

from cdm_tools.api_links import ApiIndex
from cdm_tools.api_snapshot import DEFAULT_API_DIR, load_docs_pages, load_snapshots
from cdm_tools.hub import build_hub, schema_namespaces
from cdm_tools.registry import DEFAULT_REGISTRY_PATH, LinkEntry, RegistryError, load_registry, split_url


def make_doc_link(registry: dict[str, LinkEntry]) -> Callable[[str], str]:
    def doc_link(url: str) -> str:
        base, _ = split_url(url)
        entry = registry.get(base)
        if entry is None:
            return f"<{url}>"
        return f"[{entry.display_text}]({url})"

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
        snapshots = load_snapshots(self.api_dir) if self.api_dir and Path(self.api_dir).is_dir() else {}
        platform = ApiIndex(snapshots["platform"], load_docs_pages(self.api_dir)) if "platform" in snapshots else None
        nexar_types = snapshots["nexar"]["types"] if "nexar" in snapshots else None
        namespaces = schema_namespaces(self.schemaview)
        env.globals["hub"] = lambda element: build_hub(
            element, registry=registry, platform=platform, nexar_types=nexar_types, namespaces=namespaces
        )


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
