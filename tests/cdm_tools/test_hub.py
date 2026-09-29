import textwrap

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.api_links import ApiIndex
from cdm_tools.hub import OCTOPART_API_DOC, build_hub, load_api_layers
from cdm_tools.registry import LinkEntry
from tests.cdm_tools.test_api_links import SNAP

DOC = "https://www.altium.com/documentation/altium-365/lifecycle-management"
AD = "https://www.altium.com/documentation/altium-designer/x"
SVD = "https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html"

SCHEMA = textwrap.dedent(f"""
    id: https://example.org/h
    name: h
    prefixes:
      linkml: https://w3id.org/linkml/
      ex: https://example.org/h/
      prov: http://www.w3.org/ns/prov#
    default_prefix: ex
    imports: [linkml:types]
    classes:
      ex_Full:
        description: all layers
        see_also: ["{AD}", "{DOC}#states"]
        structured_aliases:
          - literal_form: Lifecycle Definition
            predicate: EXACT_SYNONYM
            contexts: [altium-designer, altium-365]
            source: "{AD}"
        exact_mappings: [prov:Entity]
        close_mappings: ["{SVD}#elem_register"]
        annotations: {{platformAPI: DesX}}
      ex_Nexar:
        description: nexar
        annotations: {{nexarAPI: SupPart}}
      ex_None:
        description: nothing
        annotations: {{productDocs: none}}
      ex_Missing:
        description: api type not in snapshot
        annotations: {{platformAPI: DmProcessor}}
""")


@pytest.fixture(scope="module")
def sv(tmp_path_factory):
    p = tmp_path_factory.mktemp("h") / "h.yaml"
    p.write_text(SCHEMA, encoding="utf-8")
    return SchemaView(str(p))


REGISTRY = {
    AD: LinkEntry(url=AD, title="AD Page", source="altium-docs"),
    DOC: LinkEntry(url=DOC, title="Lifecycle Management", source="altium-docs", anchors=["states"]),
    SVD: LinkEntry(url=SVD, title="raw", label="CMSIS-SVD register", source="standard", anchors=["elem_register"]),
}


def _hub(sv, name):
    return build_hub(sv.get_class(name), registry=REGISTRY, platform=ApiIndex(SNAP),
                     nexar_types={"SupPart": {"kind": "OBJECT"}}, namespaces=sv.namespaces())


def test_product_layer(sv):
    h = _hub(sv, "ex_Full")
    assert [(l.text, l.url, l.primary) for l in h.links] == [
        ("AD Page", AD, True), ("Lifecycle Management", DOC + "#states", False)]
    assert [(t.text, t.predicate, t.contexts) for t in h.terms] == [
        ("Lifecycle Definition", "exact", ["altium-designer", "altium-365"])]
    assert h.product_docs_none is False


def test_api_layer(sv):
    api = _hub(sv, "ex_Full").api
    assert api.type_name == "DesX" and api.kind == "OBJECT"
    assert api.url.endswith("/types/objects/DesX/")
    assert sorted(vars(api)) == ["kind", "type_name", "url"]


def test_standards_layer(sv):
    ms = _hub(sv, "ex_Full").mappings
    assert [(m.relation, m.text, m.url) for m in ms] == [
        ("exact", "prov:Entity", "http://www.w3.org/ns/prov#Entity"),
        ("close", "CMSIS-SVD register", SVD + "#elem_register"),
    ]


def test_nexar_and_empty_states(sv):
    n = _hub(sv, "ex_Nexar")
    assert n.api is None and n.nexar.type_name == "SupPart" and n.nexar.url == OCTOPART_API_DOC
    e = _hub(sv, "ex_None")
    assert e.links == [] and e.product_docs_none is True and e.api is None and e.api_missing is None
    m = _hub(sv, "ex_Missing")
    assert m.api is None and m.api_missing == "DmProcessor"


def test_to_dict_is_json_ready(sv):
    import json
    d = _hub(sv, "ex_Full").to_dict()
    json.dumps(d)
    assert d["api"] == {"type_name": "DesX", "kind": "OBJECT",
                        "url": "https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesX/"}


def test_nexar_missing_from_snapshot(sv):
    h = build_hub(sv.get_class("ex_Nexar"), registry=REGISTRY, platform=ApiIndex(SNAP),
                  nexar_types={"Other": {"kind": "OBJECT"}}, namespaces={})
    assert h.nexar is None and h.nexar_missing == "SupPart"


def test_no_platform_snapshot_keeps_type_name(sv):
    h = build_hub(sv.get_class("ex_Full"), registry=REGISTRY, platform=None, nexar_types=None, namespaces={})
    assert h.api_missing is None
    assert h.api.type_name == "DesX" and h.api.kind == "" and h.api.url is None


def test_schema_namespaces_merges_imports_and_defaults():
    from pathlib import Path
    from cdm_tools.hub import schema_namespaces
    root = Path(__file__).resolve().parents[2] / "src/common_data_model/schema/common_data_model.yaml"
    ns = schema_namespaces(SchemaView(str(root)))
    assert ns["sys"] == "https://w3id.org/altium/cdm/system/"
    assert ns["prov"] == "http://www.w3.org/ns/prov#"
    assert ns["obo"] == "http://purl.obolibrary.org/obo/"


def test_load_api_layers(tmp_path):
    from pathlib import Path
    api_dir = Path(__file__).resolve().parents[2] / "src/docs/api"
    platform, nexar_types = load_api_layers(api_dir)
    assert isinstance(platform, ApiIndex) and "DesLifeCycleDefinition" in platform.types
    assert platform.doc_pages is not None
    assert isinstance(nexar_types, dict) and nexar_types
    assert load_api_layers(tmp_path) == (None, None)
