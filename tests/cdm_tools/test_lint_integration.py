from pathlib import Path

from cdm_tools.lint import run_lint

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")


def _run():
    return run_lint(
        ROOT,
        str(REPO / "cdm-lint.yaml"),
        registry_path=str(REPO / "src/docs/links/registry.yaml"),
        api_dir=str(REPO / "src/docs/api"),
    )


def test_doc_rules_run_and_report_files():
    issues = [i for i in _run() if i.rule_id.startswith("DOC-")]
    assert issues, "expected DOC-05 coverage warnings on the current schema"
    assert all(i.file.endswith(".yaml") for i in issues)


def test_no_doc_errors_after_baseline():
    errors = [str(i) for i in _run() if i.rule_id.startswith("DOC-") and i.severity == "error"]
    assert errors == []


def test_open_api_questions_are_baselined_warnings():
    doc03 = {i.element: i.severity for i in _run() if i.rule_id == "DOC-03"}
    assert doc03 == {
        "dm_PeripheralConfiguration": "warning",
        "dm_PeripheralPinConfig": "warning",
        "dm_PeripheralPinDependencyConfig": "warning",
        "dm_PeripheralParameter": "warning",
    }
