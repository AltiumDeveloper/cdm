import textwrap

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.doc_rules import (
    check_api_types,
    check_coverage,
    check_doc_links,
    check_mappings,
    downgrade_baselined,
)
from cdm_tools.registry import LinkEntry

DOC = "https://www.altium.com/documentation/altium-365/lifecycle-management"

SCHEMA = textwrap.dedent(
    f"""
    id: https://example.org/t
    name: t
    prefixes:
      linkml: https://w3id.org/linkml/
      ex: https://example.org/t/
    default_prefix: ex
    imports: [linkml:types]
    classes:
      core_Entity:
        abstract: true
        description: e
      core_Resource:
        abstract: true
        description: r
      ex_ValueObject:
        is_a: core_Resource
        description: v
      ex_Linked:
        is_a: core_Entity
        description: has a registered link and an API type
        see_also: ["{DOC}"]
        annotations: {{platformAPI: DesProject}}
      ex_BadAnchor:
        description: fragment not registered
        see_also: ["{DOC}#nope"]
      ex_EmptyAnchor:
        description: empty fragment
        see_also: ["{DOC}#"]
      ex_Unregistered:
        description: link not in registry
        see_also: ["https://unknown.example/page"]
        structured_aliases:
          - literal_form: Thing
            source: https://unknown.example/source
      ex_Interface:
        is_a: core_Entity
        description: interface type is linkable
        annotations: {{platformAPI: BomItemElement}}
      ex_Input:
        description: input types are not linkable
        annotations: {{platformAPI: DesProjectFilterInput}}
      ex_Missing:
        description: no such type
        annotations: {{platformAPI: DmProcessor}}
      ex_Nexar:
        is_a: core_Entity
        description: nexar type
        annotations: {{nexarAPI: SupPart}}
      ex_Mapped:
        description: mappings
        exact_mappings: [prov:Entity, "https://std.example/x#y"]
        close_mappings: [svd:register]
      ex_MappedOk:
        description: registered mapping url with a listed anchor
        exact_mappings: ["https://std.example/ok#sec"]
      ex_Uncovered:
        is_a: core_Entity
        description: production class without links
      ex_Declared:
        is_a: core_Entity
        description: explicitly no product docs
        annotations: {{productDocs: none}}
      ex_Experimental:
        is_a: core_Entity
        description: experimental
        annotations: {{maturity: EXPERIMENTAL}}
      ex_Abstract:
        is_a: core_Entity
        abstract: true
        description: abstract
    """
)

SNAPSHOTS = {
    "platform": {"types": {"DesProject": {"kind": "OBJECT"}, "BomItemElement": {"kind": "INTERFACE"}, "DesProjectFilterInput": {"kind": "INPUT_OBJECT"}}},
    "nexar": {"types": {"SupPart": {"kind": "OBJECT"}}},
}


@pytest.fixture(scope="module")
def sv(tmp_path_factory):
    p = tmp_path_factory.mktemp("schema") / "t.yaml"
    p.write_text(SCHEMA, encoding="utf-8")
    return SchemaView(str(p))


def locate(name):
    return ("t.yaml", 7)


def is_cdm(_schema_id):
    return True


def _by_element(issues):
    return {(i.rule_id, i.element): i for i in issues}


def test_doc_links(sv):
    registry = {DOC: LinkEntry(url=DOC, title="Lifecycle Management", source="altium-docs"),
                "https://orphan.example/": LinkEntry(url="https://orphan.example/", title="O", source="standard"),
                "https://std.example/ok": LinkEntry(url="https://std.example/ok", title="Std", source="standard",
                                                    anchors=["sec"])}
    got = _by_element(check_doc_links(sv, registry, locate, is_cdm, "registry.yaml"))
    issues = check_doc_links(sv, registry, locate, is_cdm, "registry.yaml")
    def n(el):
        return [i for i in issues if i.rule_id == "DOC-01" and i.element == el]
    assert len(n("ex_BadAnchor")) == 1
    assert len(n("ex_EmptyAnchor")) == 1
    unreg = " ".join(i.message for i in n("ex_Unregistered"))
    assert len(n("ex_Unregistered")) == 2
    assert "https://unknown.example/page" in unreg and "https://unknown.example/source" in unreg
    assert n("ex_Linked") == []
    assert got[("DOC-01", "ex_EmptyAnchor")].severity == "error"
    assert ("DOC-01", "ex_Unregistered") in got
    assert got[("DOC-01", "ex_Unregistered")].severity == "error"
    assert "https://unknown.example/source" in str([i.message for i in got.values()])
    assert ("DOC-01", "ex_Linked") not in got
    assert got[("DOC-02", "https://orphan.example/")].severity == "warning"
    mapped = n("ex_Mapped")
    assert len(mapped) == 1
    assert "exact_mappings" in mapped[0].message and "https://std.example/x#y" in mapped[0].message
    assert n("ex_MappedOk") == []
    assert ("DOC-02", "https://std.example/ok") not in got


def test_api_types(sv):
    got = _by_element(check_api_types(sv, SNAPSHOTS, locate, is_cdm))
    assert set(k[1] for k in got) == {"ex_Input", "ex_Missing"}
    assert "INPUT_OBJECT" in got[("DOC-03", "ex_Input")].message
    assert "does not exist" in got[("DOC-03", "ex_Missing")].message


def test_api_types_skips_missing_snapshot(sv):
    assert check_api_types(sv, {}, locate, is_cdm) == []


def test_mappings(sv):
    issues = check_mappings(sv, locate, is_cdm)
    assert [(i.rule_id, i.element) for i in issues] == [("DOC-04", "ex_Mapped")]
    assert "svd:register" in issues[0].message


def test_coverage(sv):
    got = _by_element(check_coverage(sv, locate, is_cdm))
    flagged = {k[1] for k in got}
    assert "ex_Uncovered" in flagged
    assert flagged.isdisjoint({"ex_Linked", "ex_Declared", "ex_Experimental", "ex_Abstract", "ex_Nexar", "ex_Interface", "ex_ValueObject"})
    assert all(i.severity == "warning" for i in got.values())


def test_downgrade_baselined(sv):
    issues = check_api_types(sv, SNAPSHOTS, locate, is_cdm)
    out = _by_element(downgrade_baselined(issues, {"api_type": {"ex_Missing"}}))
    assert out[("DOC-03", "ex_Missing")].severity == "warning"
    assert out[("DOC-03", "ex_Input")].severity == "error"
