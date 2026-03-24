"""
UDM-to-CDM transformer — test utility.

<<<<<<< HEAD
Navigates the 6-level UDM wire-format wrapper structure in udm_cdm_test_data.json
=======
Navigates the 6-level UDM wire-format wrapper structure in Kame_fmu_desingdata.json
>>>>>>> udm-modelling-v2
and extracts CDM-shaped data dicts for all 6 entity families:
  Project, Document, Component, Pin, Net, Variant / Variation.

This is a test utility only. It lives in tests/ and is NOT production code.
"""

import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
<<<<<<< HEAD
SAMPLE_JSON_PATH = os.path.join(ROOT, "udm_cdm_test_data.json")


def load_design_data(json_path=SAMPLE_JSON_PATH):
=======
KAME_JSON_PATH = os.path.join(ROOT, "Kame_fmu_desingdata.json")


def load_design_data(json_path=KAME_JSON_PATH):
>>>>>>> udm-modelling-v2
    """Navigate 6-level UDM wrapper and return the designData dict.

    Path: data.design.preview.latestGeneration.designData
    """
    with open(json_path) as f:
        raw = json.load(f)
    return raw["data"]["design"]["preview"]["latestGeneration"]["designData"]


def extract_documents(design_data):
    """Extract document identity dicts from designData.documents[].

    Returns a list of {'documentId': str} dicts — one per document.
    """
    return [{"documentId": doc["documentId"]} for doc in design_data["documents"]]


def extract_components(document):
    """Flatten the parts layer: component.uniqueId + component.physicalDesignator + part fields.

    CDM merged the parts layer into components (Phase 2 decision).
    For each component, iterates parts[0] and merges relevant fields.

    Returns a list of dicts with:
      uniqueId, designator, vaultGuid, itemGuid, revisionGuid, variantId,
      variationKind, pins (list of pin dicts)
    """
    components = []
    for comp in document.get("components", []):
        for part in comp.get("parts", []):
            components.append(
                {
                    "uniqueId": comp["uniqueId"],
                    "designator": comp.get("physicalDesignator"),
                    "vaultGuid": part.get("vaultGuid"),
                    "itemGuid": part.get("itemGuid"),
                    "revisionGuid": part.get("revisionGuid"),
                    "variantId": part.get("variantId"),
                    "variationKind": part.get("variationKind"),
                    "pins": extract_pins(part),
                }
            )
    return components


def extract_pins(part):
    """Extract pin dicts from part.pins[].

    Returns a list of {'uniqueId': str, 'name': str|None, 'number': str|None} dicts.
    """
    return [
        {
            "uniqueId": p["uniqueId"],
            "name": p.get("name"),
            "number": p.get("number"),
        }
        for p in part.get("pins", [])
    ]


def extract_nets(document):
    """Extract net dicts from document.nets[].

    Returns a list of {'name': str} dicts — one per net.
    """
    return [{"name": net["name"]} for net in document.get("nets", [])]


def extract_variants(design_data):
    """Extract variant identity dicts from designData.variants[].

    Returns a list of {'name': str, 'uniqueId': str|None} dicts.
    """
    return [
        {
            "name": v["name"],
            "uniqueId": v.get("uniqueId"),
        }
        for v in design_data.get("variants", [])
    ]


def extract_variations(variant_raw):
    """Extract per-component variation dicts from variant.variations[].

    Maps componentDesignator -> name to align with DesDesignVariant.DesignVariant_name.

    Returns a list of {'name': str, 'kind': str, 'componentUniqueId': str} dicts.
    """
    return [
        {
            "name": var["componentDesignator"],
            "kind": var["kind"],
            "componentUniqueId": var.get("componentUniqueId"),
        }
        for var in variant_raw.get("variations", [])
    ]


# Net item kind normalisation map.
# Maps raw JSON netItem.kind strings (from the UDM wire format) to CDM DesNetItemKind enum values.
# The JSON uses human-readable strings with spaces; CDM uses UPPER_SNAKE_CASE.
NET_ITEM_KIND_MAP = {
    "Pin": "PIN",
    "Sheet Entry": "SHEET_ENTRY",
    "Net Label": "NET_LABEL",
    "Port": "PORT",
    "Power Object": "POWER_OBJECT",
}
