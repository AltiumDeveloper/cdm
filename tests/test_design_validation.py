"""
Validation test suite for the refactored design.yaml CDM schema.

Proves that the schema can represent real ModelsProvider data from
<<<<<<< HEAD
udm_cdm_test_data.json (a single Kame FMU project).
=======
Kame_fmu_desingdata.json (a single Kame FMU project).
>>>>>>> udm-modelling-v2

Coverage:
  - Project family (wrapper navigation + data presence)
  - Document family (9 documents with documentId)
  - Component family (102 components via parts-layer flattening)
  - Pin family (583 pins with uniqueId / name / number)
  - Net family (442 nets with name)
  - Variant family (1 "Default" variant with 5 variations)
  - Enum validation: DesComponentVariationKind (NOT_FITTED / ALTERNATE)
  - Enum mapping: DesNetItemKind (JSON space-strings → CDM UPPER_SNAKE_CASE)
  - Cross-reference: variant.componentUniqueId → component.uniqueId linkage

Note: This validates a single JSON sample. Edge cases (empty projects,
no-variant projects, etc.) require additional samples not yet available.
"""

import subprocess
import sys
import os

import pytest

from udm_to_cdm_transformer import (
    load_design_data,
    extract_documents,
    extract_components,
    extract_pins,
    extract_nets,
    extract_variants,
    extract_variations,
    NET_ITEM_KIND_MAP,
<<<<<<< HEAD
    SAMPLE_JSON_PATH,
=======
    KAME_JSON_PATH,
>>>>>>> udm-modelling-v2
)
from linkml_runtime.linkml_model.meta import PermissibleValue
from common_data_model.datamodel.common_data_model import (
    DesComponentVariationKind,
    DesNetItemKind,
)


def _enum_values(enum_cls):
    """Return the set of text values for a LinkML EnumDefinitionImpl class.

    LinkML enums are not standard Python enums — they store PermissibleValue
    objects as class attributes. This helper extracts the text values.
    """
    return {
        v.text
        for k, v in enum_cls.__dict__.items()
        if not k.startswith("_") and isinstance(v, PermissibleValue)
    }


ROOT = os.path.join(os.path.dirname(__file__), "..")

# ---------------------------------------------------------------------------
# Module-level fixture — load once (69K-line file)
# ---------------------------------------------------------------------------

_design_data = None


def _get_design_data():
    """Lazily load and cache design data."""
    global _design_data
    if _design_data is None:
<<<<<<< HEAD
        _design_data = load_design_data(SAMPLE_JSON_PATH)
=======
        _design_data = load_design_data(KAME_JSON_PATH)
>>>>>>> udm-modelling-v2
    return _design_data


# ---------------------------------------------------------------------------
# 1. Transformer / UDM wrapper navigation
# ---------------------------------------------------------------------------


def test_transformer_navigates_udm_wrapper():
    """load_design_data() must return a dict with 'documents' and 'variants' keys."""
    dd = _get_design_data()
    assert isinstance(dd, dict), "designData should be a dict"
    assert "documents" in dd, "designData must have a 'documents' key"
    assert "variants" in dd, "designData must have a 'variants' key"


# ---------------------------------------------------------------------------
# 2. Document family — 9 documents, each with a non-empty documentId
# ---------------------------------------------------------------------------


def test_documents_extracted():
    """9 documents extracted; each has a non-empty documentId string."""
    dd = _get_design_data()
    docs = extract_documents(dd)
    assert len(docs) == 9, f"Expected 9 documents, got {len(docs)}"
    for doc in docs:
        assert isinstance(doc["documentId"], str), "documentId should be a string"
        assert doc["documentId"], "documentId should be non-empty"


# ---------------------------------------------------------------------------
# 3. Component family — documents 1-7 have components; each has uniqueId
# ---------------------------------------------------------------------------


def test_components_extracted():
    """At least one document contains components; each component has a uniqueId string."""
    dd = _get_design_data()
    raw_docs = dd["documents"]

    all_components = []
    for doc in raw_docs:
        all_components.extend(extract_components(doc))

<<<<<<< HEAD
    assert (
        len(all_components) > 0
    ), "Expected at least one component across all documents"

    for comp in all_components:
        assert isinstance(
            comp["uniqueId"], str
        ), "Component uniqueId should be a string"
=======
    assert len(all_components) > 0, (
        "Expected at least one component across all documents"
    )

    for comp in all_components:
        assert isinstance(comp["uniqueId"], str), (
            "Component uniqueId should be a string"
        )
>>>>>>> udm-modelling-v2
        assert comp["uniqueId"], "Component uniqueId should be non-empty"


def test_total_component_count():
    """Total component count via parts-layer flattening is 102."""
    dd = _get_design_data()
    total = sum(len(extract_components(doc)) for doc in dd["documents"])
    assert total == 102, f"Expected 102 total components (via parts), got {total}"


# ---------------------------------------------------------------------------
# 4. Pin family — pins on components; each has uniqueId, name, number
# ---------------------------------------------------------------------------


def test_component_pins_extracted():
    """Components with parts have pins; each pin has uniqueId, name, number (all strings)."""
    dd = _get_design_data()

    found_pins = False
    for doc in dd["documents"]:
        for comp in doc.get("components", []):
            for part in comp.get("parts", []):
                pins = extract_pins(part)
                if pins:
                    found_pins = True
                    for pin in pins:
                        assert "uniqueId" in pin
                        assert "name" in pin
                        assert "number" in pin
<<<<<<< HEAD
                        assert isinstance(
                            pin["uniqueId"], str
                        ), "Pin uniqueId should be a string"
=======
                        assert isinstance(pin["uniqueId"], str), (
                            "Pin uniqueId should be a string"
                        )
>>>>>>> udm-modelling-v2
                        assert pin["uniqueId"], "Pin uniqueId should be non-empty"

    assert found_pins, "Expected to find at least one component with pins"


def test_total_pin_count():
    """Total pin count across all components is 583."""
    dd = _get_design_data()
    total = 0
    for doc in dd["documents"]:
        for comp in doc.get("components", []):
            for part in comp.get("parts", []):
                total += len(extract_pins(part))
    assert total == 583, f"Expected 583 total pins, got {total}"


# ---------------------------------------------------------------------------
# 5. Net family — documents have nets; each net has a non-empty name
# ---------------------------------------------------------------------------


def test_nets_extracted():
    """At least one document has nets; each net has a non-empty name string."""
    dd = _get_design_data()

    all_nets = []
    for doc in dd["documents"]:
        all_nets.extend(extract_nets(doc))

    assert len(all_nets) > 0, "Expected at least one net across all documents"

    for net in all_nets:
        assert isinstance(net["name"], str), "Net name should be a string"
        assert net["name"], "Net name should be non-empty"


def test_total_net_count():
    """Total net count across all documents is 442."""
    dd = _get_design_data()
    total = sum(len(extract_nets(doc)) for doc in dd["documents"])
    assert total == 442, f"Expected 442 total nets, got {total}"


# ---------------------------------------------------------------------------
# 6. Variant family — 1 "Default" variant
# ---------------------------------------------------------------------------


def test_variants_extracted():
    """1 variant extracted with name 'Default'."""
    dd = _get_design_data()
    variants = extract_variants(dd)
    assert len(variants) == 1, f"Expected 1 variant, got {len(variants)}"
<<<<<<< HEAD
    assert (
        variants[0]["name"] == "Default"
    ), f"Expected variant name 'Default', got {variants[0]['name']!r}"
=======
    assert variants[0]["name"] == "Default", (
        f"Expected variant name 'Default', got {variants[0]['name']!r}"
    )
>>>>>>> udm-modelling-v2


# ---------------------------------------------------------------------------
# 7. Variation family — 5 variations; kind values are valid CDM enum
# ---------------------------------------------------------------------------


def test_variations_extracted():
    """Default variant has 5 variations; first has kind 'NOT_FITTED'."""
    dd = _get_design_data()
    raw_variants = dd["variants"]
    first_variant_raw = raw_variants[0]
    variations = extract_variations(first_variant_raw)

    assert len(variations) == 5, f"Expected 5 variations, got {len(variations)}"
<<<<<<< HEAD
    assert (
        variations[0]["kind"] == "NOT_FITTED"
    ), f"Expected first variation kind 'NOT_FITTED', got {variations[0]['kind']!r}"
=======
    assert variations[0]["kind"] == "NOT_FITTED", (
        f"Expected first variation kind 'NOT_FITTED', got {variations[0]['kind']!r}"
    )
>>>>>>> udm-modelling-v2


def test_variation_kind_is_valid_enum():
    """All variation kinds from the JSON are valid DesComponentVariationKind values."""
    dd = _get_design_data()
    valid_kinds = _enum_values(DesComponentVariationKind)

    for variant_raw in dd["variants"]:
        for var in variant_raw.get("variations", []):
            kind = var.get("kind")
            assert kind in valid_kinds, (
                f"Variation kind {kind!r} is not a valid DesComponentVariationKind. "
                f"Valid values: {valid_kinds}"
            )


# ---------------------------------------------------------------------------
# 8. Enum mapping — all raw JSON netItem.kind values are in NET_ITEM_KIND_MAP
# ---------------------------------------------------------------------------


def test_net_item_kinds_in_json():
    """All raw JSON netItem.kind values map to DesNetItemKind enum values via NET_ITEM_KIND_MAP."""
    dd = _get_design_data()

    # Collect all raw kind strings from the JSON
    raw_kinds = set()
    for doc in dd["documents"]:
        for net in doc.get("nets", []):
            for item in net.get("netItems", []):
                raw_kinds.add(item.get("kind"))

    assert raw_kinds, "Expected to find at least one net item kind in the JSON"

    # Every raw kind must be in the normalisation map
    for raw_kind in raw_kinds:
        assert raw_kind in NET_ITEM_KIND_MAP, (
            f"Raw net item kind {raw_kind!r} has no entry in NET_ITEM_KIND_MAP. "
            f"Add it to the normalisation map."
        )

    # Every mapped value must be a valid DesNetItemKind
    valid_cdm_kinds = _enum_values(DesNetItemKind)
    for raw_kind, cdm_kind in NET_ITEM_KIND_MAP.items():
        assert cdm_kind in valid_cdm_kinds, (
            f"NET_ITEM_KIND_MAP maps {raw_kind!r} -> {cdm_kind!r} but {cdm_kind!r} "
            f"is not a valid DesNetItemKind. Valid: {valid_cdm_kinds}"
        )


# ---------------------------------------------------------------------------
# 9. Cross-reference — variant.componentUniqueId must resolve to a known component
# ---------------------------------------------------------------------------


def test_cross_reference_variant_to_component():
    """Variation componentUniqueId values exist in the set of component uniqueIds across all docs."""
    dd = _get_design_data()

    # Build set of all component uniqueIds across all documents
    all_component_ids = set()
    for doc in dd["documents"]:
        for comp in doc.get("components", []):
            all_component_ids.add(comp["uniqueId"])

<<<<<<< HEAD
    assert (
        all_component_ids
    ), "Expected to find component uniqueIds for cross-reference check"
=======
    assert all_component_ids, (
        "Expected to find component uniqueIds for cross-reference check"
    )
>>>>>>> udm-modelling-v2

    # Check that each variation's componentUniqueId resolves
    unresolved = []
    for variant_raw in dd["variants"]:
        for var in variant_raw.get("variations", []):
            comp_uid = var.get("componentUniqueId")
            if comp_uid is not None and comp_uid not in all_component_ids:
                unresolved.append(comp_uid)

    assert not unresolved, (
        f"Variation componentUniqueId values not found in any document's component list: "
        f"{unresolved}"
    )


# ---------------------------------------------------------------------------
# 10. Build regression — make gen-project must exit 0
# ---------------------------------------------------------------------------


def test_make_gen_project_clean():
    """make gen-project exits 0 (no regressions from Phase 2 schema changes)."""
    result = subprocess.run(
        ["make", "gen-project"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, (
        f"make gen-project failed with exit code {result.returncode}.\n"
        f"STDOUT:\n{result.stdout[-2000:]}\n"
        f"STDERR:\n{result.stderr[-2000:]}"
    )
