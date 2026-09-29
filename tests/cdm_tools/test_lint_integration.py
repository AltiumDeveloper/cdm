from pathlib import Path

import pytest

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


def _main_with(monkeypatch, tmp_path, *extra):
    from cdm_tools import lint

    monkeypatch.setattr(
        "sys.argv",
        ["cdm-lint", ROOT, "--config", str(REPO / "cdm-lint.yaml"), *extra],
    )
    with pytest.raises(SystemExit) as exc:
        lint.main()
    return exc.value.code


def test_main_fails_when_registry_missing(monkeypatch, tmp_path, capsys):
    missing = tmp_path / "missing.yaml"
    assert _main_with(monkeypatch, tmp_path, "--registry", str(missing)) == 2
    assert (
        f"cdm-lint: link registry not found: {missing} "
        "(run from the repo root or pass --registry)"
    ) in capsys.readouterr().err


def test_main_fails_when_api_dir_missing(monkeypatch, tmp_path, capsys):
    missing = tmp_path / "no-api"
    args = ["--registry", str(REPO / "src/docs/links/registry.yaml"), "--api-dir", str(missing)]
    assert _main_with(monkeypatch, tmp_path, *args) == 2
    assert (
        f"cdm-lint: API snapshot directory not found: {missing} "
        "(run from the repo root or pass --api-dir)"
    ) in capsys.readouterr().err


def test_main_fails_when_registry_malformed(monkeypatch, tmp_path, capsys):
    bad = tmp_path / "registry.yaml"
    bad.write_text(
        "https://example.com/x:\n  title: X\n  source: bogus\n", encoding="utf-8"
    )
    assert _main_with(monkeypatch, tmp_path, "--registry", str(bad)) == 2
    assert "cdm-lint: invalid link registry:" in capsys.readouterr().err
