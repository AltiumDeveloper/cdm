import textwrap
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_links import ApiIndex
from cdm_tools.coverage import Finding, is_concrete_domain_class, load_findings, subset_coverage, total_coverage
from cdm_tools.hub import load_api_layers
from tests.cdm_tools.test_api_links import SNAP

REPO = Path(__file__).resolve().parents[2]

SCHEMA = textwrap.dedent("""
    id: https://example.org/c
    name: c
    prefixes:
      linkml: https://w3id.org/linkml/
      ex: https://example.org/c/
    default_prefix: ex
    imports: [linkml:types]
    subsets:
      alpha: {description: a}
      beta: {description: b}
    classes:
      core_Thing: {abstract: true, in_subset: [alpha], description: core}
      ex_Abs: {abstract: true, in_subset: [alpha], description: abstract}
      ex_Mix: {mixin: true, in_subset: [alpha], description: mixin}
      ex_Full:
        in_subset: [alpha, beta]
        description: all layers
        see_also: ["https://example.org/doc"]
        structured_aliases:
          - {literal_form: Full, predicate: EXACT_SYNONYM}
        exact_mappings: ["prov:Entity"]
        annotations: {platformAPI: DesX}
      ex_Bare:
        in_subset: [alpha]
        description: TBD
      ex_Empty:
        in_subset: [beta]
        annotations: {nexarAPI: SupPart, productDocs: none}
      ex_Missing:
        in_subset: [beta]
        description: api not in snapshot
        annotations: {platformAPI: NoSuchType}
""")

FINDINGS = textwrap.dedent("""
    # Model Findings

    | ID | Element | Finding | Evidence | Kind | Context | Status |
    |---|---|---|---|---|---|---|
    | MF-001 | `ex_Full` | text | `x` | breaking | alpha | Needs SME |
    | MF-002 |  `ex_Bare`  | text | `x` | gap |  `beta`  | Fixed — pending review |
    | MF-003 | `ex_X_y` | text | `x` | additive | requirement | Needs SME (owner asked) |
    | MF-004 | `ex_Z` | text | `x` | description | alpha | Fixed (PR #1) |
    | not a row | a | b | c | d | e | f |
""")


@pytest.fixture(scope="module")
def sv(tmp_path_factory):
    p = tmp_path_factory.mktemp("c") / "c.yaml"
    p.write_text(SCHEMA, encoding="utf-8")
    return SchemaView(str(p))


def test_load_findings(tmp_path):
    p = tmp_path / "MF.md"
    p.write_text(FINDINGS, encoding="utf-8")
    fs = load_findings(p)
    assert [f.id for f in fs] == ["MF-001", "MF-002", "MF-003", "MF-004"]
    assert fs[1] == Finding("MF-002", "ex_Bare", "gap", "beta", "Fixed — pending review")
    assert fs[2].context == "requirements"
    assert fs[2].status == "Needs SME (owner asked)"


def test_concrete_predicate(sv):
    names = sorted(n for n, c in sv.all_classes().items() if is_concrete_domain_class(n, c))
    assert names == ["ex_Bare", "ex_Empty", "ex_Full", "ex_Missing"]


def test_subset_coverage(sv, tmp_path):
    p = tmp_path / "MF.md"
    p.write_text(FINDINGS, encoding="utf-8")
    cov = subset_coverage(sv, platform_index=ApiIndex(SNAP), nexar_types={"SupPart": {}},
                          findings=load_findings(p))
    a, b = cov["alpha"], cov["beta"]
    # ex_Full has two subsets but is counted once, in the first
    assert (a.classes, b.classes) == (2, 2)
    assert a.with_docs == 1 and a.with_terms == 1 and a.with_mappings == 1 and a.tbd == 1
    assert a.with_api == 1
    assert b.no_docs_declared == 1 and b.tbd == 1 and b.with_api == 1   # nexar ok, NoSuchType unresolved
    assert (a.findings_open, a.findings_pending) == (1, 0)
    assert (b.findings_open, b.findings_pending) == (0, 1)
    assert cov["requirements"].findings_open == 1 and cov["requirements"].classes == 0
    t = total_coverage(cov)
    assert t.classes == 4 and t.findings_open == 2 and t.findings_pending == 1
    assert t.to_dict()["classes"] == 4


def test_missing_snapshots_count_annotations(sv):
    cov = subset_coverage(sv, platform_index=None, nexar_types=None, findings=[])
    assert cov["alpha"].with_api == 1 and cov["beta"].with_api == 2


def test_real_schema():
    sv = SchemaView(str(REPO / "src/common_data_model/schema/common_data_model.yaml"))
    platform, nexar = load_api_layers(REPO / "src/docs/api")
    cov = subset_coverage(sv, platform_index=platform, nexar_types=nexar,
                          findings=load_findings(REPO / "MODEL-FINDINGS.md"))
    n = sum(1 for k, c in sv.all_classes().items() if is_concrete_domain_class(k, c))
    t = total_coverage(cov)
    assert t.classes == n > 0
    assert "system-sdm" in cov
    assert t.findings_open + t.findings_pending > 0
