"""
cdm-sheet-export — complete the schema JSON published to the CDM Google Spreadsheet (`make gen-schema`).

`gen-linkml` writes only each class's own annotations, and LinkML does not inherit annotations, so a class whose
GRID template is declared on an ancestor (e.g. `pro_ManagedBOM`, template on `pro_BomWIP`) would be exported
without one. This adds the inherited `grid` annotation to those classes, in place.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.reference import effective_grid_templates


def add_inherited_grids(data: dict, sv: SchemaView) -> list[str]:
    """Give every class in *data* (gen-linkml JSON) without a `grid` annotation its inherited template.

    Returns the names of the classes that were completed.
    """
    added = []
    for name, (template, owner) in sorted(effective_grid_templates(sv).items()):
        cls = data.get("classes", {}).get(name)
        if cls is None or owner == name:
            continue
        annotations = cls.setdefault("annotations", {})
        if str((annotations.get("grid") or {}).get("value") or "").strip():
            continue
        annotations["grid"] = {"tag": "grid", "value": template}
        added.append(name)
    return added


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-sheet-export", description=__doc__)
    parser.add_argument("schema", help="root schema YAML")
    parser.add_argument("json", help="gen-linkml JSON output, updated in place")
    args = parser.parse_args(argv)
    path = Path(args.json)
    data = json.loads(path.read_text(encoding="utf-8"))
    add_inherited_grids(data, SchemaView(args.schema))
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
