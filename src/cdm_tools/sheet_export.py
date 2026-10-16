"""
cdm-sheet-export — complete the schema JSON published to the CDM Google Spreadsheet (`make gen-schema`).

`gen-linkml` writes only each class's own annotations, and LinkML does not inherit annotations, so a class whose
GRID template or API type is declared on an ancestor (e.g. `pro_ManagedBOM`: template and `BomWip` on
`pro_BomWIP`) would be exported without them. This adds the inherited `grid`, `platformAPI` and `nexarAPI`
annotations to those classes, in place.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.hub import api_declaration
from cdm_tools.reference import effective_grid_templates


def _set(cls: dict, tag: str, value: str) -> bool:
    annotations = cls.setdefault("annotations", {})
    if str((annotations.get(tag) or {}).get("value") or "").strip():
        return False
    annotations[tag] = {"tag": tag, "value": value}
    return True


def add_inherited_annotations(data: dict, sv: SchemaView) -> dict[str, list[str]]:
    """Give every class in *data* (gen-linkml JSON) the GRID template and API type it inherits but does not declare.

    Returns annotation -> names of the classes that were completed.
    """
    added: dict[str, list[str]] = {"grid": [], "platformAPI": [], "nexarAPI": []}
    classes = data.get("classes", {})
    grids = effective_grid_templates(sv)
    for name in sorted(classes):
        if name not in sv.all_classes():
            continue
        cls = classes[name]
        template, owner = grids.get(name, (None, None))
        if template and owner != name and _set(cls, "grid", template):
            added["grid"].append(name)
        api, api_from = api_declaration(sv, name)
        if api_from:
            for tag, value in api.items():
                if _set(cls, tag, value):
                    added[tag].append(name)
    return added


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-sheet-export", description=__doc__)
    parser.add_argument("schema", help="root schema YAML")
    parser.add_argument("json", help="gen-linkml JSON output, updated in place")
    args = parser.parse_args(argv)
    path = Path(args.json)
    data = json.loads(path.read_text(encoding="utf-8"))
    add_inherited_annotations(data, SchemaView(args.schema))
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
