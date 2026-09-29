import json
from pathlib import Path

import jsonschema

from cdm_tools.hub_export import build_export, main

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")


def _export():
    return build_export(ROOT, registry_path=str(REPO / "src/docs/links/registry.yaml"),
                        api_dir=str(REPO / "src/docs/api"))


def test_export_validates_against_schema():
    schema = json.loads((REPO / "src/docs/hub.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(_export(), schema)


def test_export_content():
    data = _export()
    c = data["classes"]["plt_LifecycleDefinition"]
    assert c["title"] == "Lifecycle Definition"
    assert c["class_uri"] == "plt:LifecycleDefinition"
    assert c["subset"] == "platform"
    assert c["grid"] == "grid:workspace:{workspace-id}:platform:lifecycle-definition/{id}"
    assert c["hub"]["links"][0]["primary"] is True
    assert c["hub"]["api"]["type_name"] == "DesLifeCycleDefinition"
    assert "core_Entity" not in data["classes"]          # abstract/core classes excluded
    assert "Any" not in data["classes"]                  # linkml:Any excluded
    assert data["schema"]["id"] == "https://w3id.org/altium/cdm/"


def test_main_writes_file(tmp_path):
    out = tmp_path / "hub.json"
    assert main([ROOT, "-o", str(out), "--registry", str(REPO / "src/docs/links/registry.yaml"),
                 "--api-dir", str(REPO / "src/docs/api")]) == 0
    assert json.loads(out.read_text())["classes"]
