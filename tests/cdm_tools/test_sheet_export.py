import json
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.sheet_export import add_inherited_grids, main

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")
BOM_GRID = "grid:workspace:{workspace-id}:procurement:bom/{id}"


def _data():
    return {"classes": {
        "pro_BomWIP": {"name": "pro_BomWIP", "annotations": {"grid": {"tag": "grid", "value": BOM_GRID}}},
        "pro_ManagedBOM": {"name": "pro_ManagedBOM", "annotations": {"platformAPI": {"tag": "platformAPI",
                                                                                     "value": "BomWip"}}},
        "pro_ConsolidatedBOM": {"name": "pro_ConsolidatedBOM"},
        "core_Entity": {"name": "core_Entity"},
    }}


def test_inherited_grid_is_added():
    data = _data()
    added = add_inherited_grids(data, SchemaView(ROOT))
    classes = data["classes"]
    assert added == ["pro_ConsolidatedBOM", "pro_ManagedBOM"]
    assert classes["pro_ManagedBOM"]["annotations"]["grid"] == {"tag": "grid", "value": BOM_GRID}
    assert classes["pro_ManagedBOM"]["annotations"]["platformAPI"]["value"] == "BomWip"   # others kept
    assert classes["pro_ConsolidatedBOM"]["annotations"]["grid"]["value"] == BOM_GRID
    assert "annotations" not in classes["core_Entity"]                                    # no GRID anywhere


def test_main_updates_file_in_place(tmp_path):
    path = tmp_path / "google-sheet-schema.json"
    path.write_text(json.dumps(_data()), encoding="utf-8")
    assert main([ROOT, str(path)]) == 0
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["classes"]["pro_ManagedBOM"]["annotations"]["grid"]["value"] == BOM_GRID
