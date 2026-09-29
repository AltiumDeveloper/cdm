from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

REPO = Path(__file__).resolve().parents[2]


def test_schema_declares_version():
    sv = SchemaView(str(REPO / "src/common_data_model/schema/common_data_model.yaml"))
    assert sv.schema.version == "0.10.0"


def test_governance_files_exist():
    for name in ("VIOLATIONS.md", "MODEL-FINDINGS.md", "CHANGELOG.md"):
        assert (REPO / name).is_file(), name


def test_changelog_has_unreleased_section():
    assert "## [Unreleased]" in (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
