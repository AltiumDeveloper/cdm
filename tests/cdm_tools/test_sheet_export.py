import json
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.sheet_export import add_inherited_annotations, main

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")
INSIGHT_GRID = "grid:workspace:{workspace-id}:insights:insight/{id}"
MANAGED_GRID = "grid:workspace:{workspace-id}:procurement:bom/{id}"


def _data():
    """gen-linkml JSON for a few classes, with only their own annotations."""
    def ann(**kv):
        return {k: {"tag": k, "value": v} for k, v in kv.items()}
    return {"classes": {
        "ins_Insight": {"name": "ins_Insight", "annotations": ann(grid=INSIGHT_GRID, platformAPI="DesWorkspaceInsInsight")},
        "ins_PartInsight": {"name": "ins_PartInsight"},
        "pro_BomWIP": {"name": "pro_BomWIP", "annotations": ann(platformAPI="BomWip")},
        "pro_ManagedBOM": {"name": "pro_ManagedBOM", "annotations": ann(grid=MANAGED_GRID)},
        "pro_BomItemAlternate": {"name": "pro_BomItemAlternate", "annotations": ann(platformAPI="BomItemAlternate")},
        "core_Entity": {"name": "core_Entity"},
    }}


def test_inherited_grid_and_api_type_are_added():
    data = _data()
    added = add_inherited_annotations(data, SchemaView(ROOT))
    classes = data["classes"]
    assert added["grid"] == ["ins_PartInsight"]
    assert added["platformAPI"] == ["ins_PartInsight", "pro_ManagedBOM"]
    part = classes["ins_PartInsight"]["annotations"]
    assert part["grid"] == {"tag": "grid", "value": INSIGHT_GRID}
    assert part["platformAPI"] == {"tag": "platformAPI", "value": "DesWorkspaceInsInsight"}
    managed = classes["pro_ManagedBOM"]["annotations"]
    assert managed["grid"]["value"] == MANAGED_GRID                                       # own GRID kept
    assert managed["platformAPI"]["value"] == "BomWip"                                    # API type from BOM WIP
    assert classes["pro_BomItemAlternate"]["annotations"]["platformAPI"]["value"] == "BomItemAlternate"  # own wins
    assert "annotations" not in classes["core_Entity"]                                    # nothing to inherit


def test_main_updates_file_in_place(tmp_path):
    path = tmp_path / "google-sheet-schema.json"
    path.write_text(json.dumps(_data()), encoding="utf-8")
    assert main([ROOT, str(path)]) == 0
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["classes"]["ins_PartInsight"]["annotations"]["grid"]["value"] == INSIGHT_GRID
    assert data["classes"]["pro_ManagedBOM"]["annotations"]["platformAPI"]["value"] == "BomWip"
