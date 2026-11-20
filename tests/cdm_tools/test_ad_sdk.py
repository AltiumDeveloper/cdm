import json
import textwrap

from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools import ad_sdk_snapshot as sdk
from cdm_tools.hub import build_hub

DECLS = textwrap.dedent("""\
    // Altium Designer SDK: namespace PCB (PCB). Generated from Altium.SDK.Interfaces 1.0.0.0, Altium.SDK 1.0.1.2.
    namespace PCB
    {
        public class CoordPoint : ICoordPoint { int X { get; set; } }

        public interface IPCB_Track : IPCB_Primitive
        {
            int Width { get => GetState_Width; set => SetState_Width; }
        }

        public enum TShape { eNoShape = 0, eRounded = 1 }
    }
""")

SCHEMA = textwrap.dedent("""
    id: https://example.org/s
    name: s
    prefixes: {linkml: https://w3id.org/linkml/, ex: https://example.org/s/}
    default_prefix: ex
    imports: [linkml:types]
    classes:
      ex_Track:
        description: track
        annotations: {platformAPI: DesTrack, adSDK: "PCB.IPCB_Track, SCH.ISch_Nope"}
      ex_Plain:
        description: no sdk
""")


def test_parse_declarations():
    types, header = sdk.parse_declarations(DECLS)
    assert types == ["CoordPoint", "IPCB_Track", "TShape"]
    assert header == "Altium.SDK.Interfaces 1.0.0.0, Altium.SDK 1.0.1.2"


def test_urls_and_split():
    assert sdk.type_url("PCB.IPCB_Track") == "https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Track/"
    assert sdk.declarations_url("ComponentLib").endswith("/reference/componentlib/api.cs.txt")
    assert sdk.split_annotation(" EDP.INet, PCB.IPCB_Net ,") == ["EDP.INet", "PCB.IPCB_Net"]


def test_load_and_resolve(tmp_path):
    assert sdk.load_ad_sdk(tmp_path) is None
    (tmp_path / sdk.SNAPSHOT_FILE).write_text(json.dumps({"namespaces": {"PCB": ["IPCB_Track"]}}))
    snap = sdk.load_ad_sdk(tmp_path)
    assert sdk.resolves("PCB.IPCB_Track", snap) and not sdk.resolves("PCB.IPCB_Nope", snap)
    assert sdk.resolves("PCB.Anything", None)


def test_hub_ad_sdk_layer(tmp_path):
    p = tmp_path / "s.yaml"
    p.write_text(SCHEMA)
    sv = SchemaView(str(p))
    snap = {"PCB": {"IPCB_Track"}}
    h = build_hub(sv.get_class("ex_Track"), registry={}, platform=None, nexar_types=None, namespaces={},
                  ad_sdk=snap)
    assert [(t.type_name, t.url) for t in h.ad_sdk] == [("PCB.IPCB_Track", sdk.type_url("PCB.IPCB_Track"))]
    assert h.ad_sdk_missing == ["SCH.ISch_Nope"]
    plain = build_hub(sv.get_class("ex_Plain"), registry={}, platform=None, nexar_types=None, namespaces={},
                      ad_sdk=snap)
    assert plain.ad_sdk == [] and plain.ad_sdk_missing == []


def test_snapshot_covers_schema_annotations():
    """Every adSDK annotation in the CDM schema names a type in the checked-in AD SDK snapshot."""
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    snap = sdk.load_ad_sdk(root / "src/docs/api")
    sv = SchemaView(str(root / "src/common_data_model/schema/common_data_model.yaml"))
    missing = []
    for name, el in list(sv.all_classes().items()) + list(sv.all_enums().items()):
        ann = el.annotations or {}
        if "adSDK" in ann:
            missing += [f"{name}: {q}" for q in sdk.split_annotation(ann["adSDK"].value) if not sdk.resolves(q, snap)]
    assert missing == []
