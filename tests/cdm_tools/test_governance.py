from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

REPO = Path(__file__).resolve().parents[2]


def test_schema_has_no_hardcoded_version():
    """Release versions come from vX.Y.Z git tags (poetry-dynamic-versioning); a copy in the schema would drift."""
    sv = SchemaView(str(REPO / "src/common_data_model/schema/common_data_model.yaml"))
    assert sv.schema.version is None


def test_governance_files_exist():
    for name in ("VIOLATIONS.md", "MODEL-FINDINGS.md", "CHANGELOG.md"):
        assert (REPO / name).is_file(), name


def test_changelog_has_unreleased_section():
    assert "## [Unreleased]" in (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
