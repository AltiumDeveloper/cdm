"""
cdm-hub-export — write the documentation hub for every concrete CDM class as JSON
(product links and terms, API type and operations, standards mappings, GRID template).
Validated against src/docs/hub.schema.json; published with the docs site as hub.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_links import ApiIndex
from cdm_tools.api_snapshot import DEFAULT_API_DIR, load_docs_pages, load_snapshots
from cdm_tools.hub import build_hub, schema_namespaces
from cdm_tools.registry import DEFAULT_REGISTRY_PATH, RegistryError, load_registry


def build_export(schema_path: str, *, registry_path: str, api_dir: str) -> dict:
    sv = SchemaView(schema_path)
    registry = load_registry(registry_path)
    snapshots = load_snapshots(api_dir)
    platform = ApiIndex(snapshots["platform"], load_docs_pages(api_dir)) if "platform" in snapshots else None
    nexar_types = snapshots["nexar"]["types"] if "nexar" in snapshots else None
    namespaces = schema_namespaces(sv)
    classes: dict[str, dict] = {}
    for name, cls in sorted(sv.all_classes().items()):
        if cls.abstract or cls.mixin or name.startswith("core_"):
            continue
        if name == "Any" or str(cls.class_uri or "").startswith("linkml:"):
            continue
        ann = cls.annotations or {}
        classes[name] = {
            "title": cls.title,
            "class_uri": cls.class_uri,
            "subset": str(cls.in_subset[0]) if cls.in_subset else None,
            "grid": str(ann["grid"].value) if "grid" in ann else None,
            "hub": build_hub(cls, registry=registry, platform=platform, nexar_types=nexar_types,
                             namespaces=namespaces).to_dict(),
        }
    return {
        "schema": {"id": sv.schema.id, "name": sv.schema.name,
                   "api_snapshot_retrieved": snapshots.get("platform", {}).get("retrieved")},
        "classes": classes,
    }


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-hub-export", description=__doc__)
    parser.add_argument("schema")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--registry", default=DEFAULT_REGISTRY_PATH)
    parser.add_argument("--api-dir", default=DEFAULT_API_DIR)
    args = parser.parse_args(argv)
    if not Path(args.registry).is_file():
        print(f"cdm-hub-export: link registry not found: {args.registry}", file=sys.stderr)
        return 2
    if not Path(args.api_dir).is_dir():
        print(f"cdm-hub-export: API snapshot directory not found: {args.api_dir}", file=sys.stderr)
        return 2
    try:
        data = build_export(args.schema, registry_path=args.registry, api_dir=args.api_dir)
    except RegistryError as exc:
        print(f"cdm-hub-export: invalid link registry: {exc}", file=sys.stderr)
        return 2
    Path(args.output).write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
