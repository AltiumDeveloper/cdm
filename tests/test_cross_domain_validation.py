"""Validation tests for Phase 10 cross-domain harmonization.

Confirms that typed cross-domain links (design↔library, BOM↔library,
variant linkage) are properly wired, vault GUID attrs are deprecated,
and all new named slots have complete metadata per AGENTS.md.
"""

import os

import pytest
from linkml_runtime.utils.schemaview import SchemaView

SCHEMA_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "common_data_model",
    "schema",
)
SCHEMA_PATH = os.path.join(SCHEMA_DIR, "common_data_model.yaml")


@pytest.fixture(scope="module")
def schema_view():
    """Load the merged CDM schema once per module."""
    return SchemaView(SCHEMA_PATH)


# ---------------------------------------------------------------------------
# 1. XDOM-02: design → library link
# ---------------------------------------------------------------------------


class TestComponentLibrarySource:
    """Verify des_component_library_source links design to library."""

    def test_component_library_source_exists(self, schema_view):
        """des_component_library_source named slot exists."""
        slot = schema_view.get_slot("des_component_library_source")
        assert slot is not None, "des_component_library_source slot not found"

    def test_component_library_source_range(self, schema_view):
        """Range is lib_ComponentRevision."""
        slot = schema_view.get_slot("des_component_library_source")
        assert slot.range == "lib_ComponentRevision", (
            f"Expected range lib_ComponentRevision, got {slot.range}"
        )

    def test_component_library_source_is_derived_from(self, schema_view):
        """Inherits from core_derivedFrom."""
        slot = schema_view.get_slot("des_component_library_source")
        assert slot.is_a == "core_derivedFrom", (
            f"Expected is_a core_derivedFrom, got {slot.is_a}"
        )


# ---------------------------------------------------------------------------
# 2. XDOM-04: design component → variant link
# ---------------------------------------------------------------------------


class TestComponentVariant:
    """Verify des_component_variant links design component to variant."""

    def test_component_variant_exists(self, schema_view):
        """des_component_variant named slot exists."""
        slot = schema_view.get_slot("des_component_variant")
        assert slot is not None, "des_component_variant slot not found"

    def test_component_variant_range(self, schema_view):
        """Range is des_project_variant."""
        slot = schema_view.get_slot("des_component_variant")
        assert slot.range == "des_project_variant", (
            f"Expected range des_project_variant, got {slot.range}"
        )

    def test_component_variant_is_derived_from(self, schema_view):
        """Inherits from core_derivedFrom."""
        slot = schema_view.get_slot("des_component_variant")
        assert slot.is_a == "core_derivedFrom", (
            f"Expected is_a core_derivedFrom, got {slot.is_a}"
        )

    def test_component_variant_in_class(self, schema_view):
        """des_component_variant is wired into des_design_component."""
        cls = schema_view.get_class("des_design_component")
        slot_names = [s.name for s in schema_view.class_induced_slots(cls.name)]
        assert "des_component_variant" in slot_names, (
            "des_component_variant not found in des_design_component induced slots"
        )


# ---------------------------------------------------------------------------
# 3. XDOM-04: BOM variant → design variant link
# ---------------------------------------------------------------------------


class TestBomVariantDesignVariant:
    """Verify pro_bom_variant_design_variant links BOM to design variant."""

    def test_bom_variant_design_variant_exists(self, schema_view):
        """pro_bom_variant_design_variant named slot exists."""
        slot = schema_view.get_slot("pro_bom_variant_design_variant")
        assert slot is not None, "pro_bom_variant_design_variant slot not found"

    def test_bom_variant_design_variant_range(self, schema_view):
        """Range is des_project_variant."""
        slot = schema_view.get_slot("pro_bom_variant_design_variant")
        assert slot.range == "des_project_variant", (
            f"Expected range des_project_variant, got {slot.range}"
        )

    def test_bom_variant_design_variant_is_derived_from(self, schema_view):
        """Inherits from core_derivedFrom."""
        slot = schema_view.get_slot("pro_bom_variant_design_variant")
        assert slot.is_a == "core_derivedFrom", (
            f"Expected is_a core_derivedFrom, got {slot.is_a}"
        )

    def test_bom_variant_design_variant_in_class(self, schema_view):
        """pro_bom_variant_design_variant is wired into pro_BomVariant."""
        cls = schema_view.get_class("pro_BomVariant")
        slot_names = [s.name for s in schema_view.class_induced_slots(cls.name)]
        assert "pro_bom_variant_design_variant" in slot_names, (
            "pro_bom_variant_design_variant not found in pro_BomVariant induced slots"
        )


# ---------------------------------------------------------------------------
# 4. XDOM-03: BOM element → library component link
# ---------------------------------------------------------------------------


class TestBomElementComponent:
    """Verify BomItemElement_component links BOM to library."""

    def test_bom_element_component_range(self, schema_view):
        """BomItemElement_component has range lib_ComponentRevision."""
        # This is an attribute, so check via the class
        cls = schema_view.get_class("pro_BomItemElement")
        slot = schema_view.get_slot("BomItemElement_component")
        assert slot is not None, "BomItemElement_component slot not found"
        assert slot.range == "lib_ComponentRevision", (
            f"Expected range lib_ComponentRevision, got {slot.range}"
        )

    def test_bom_element_component_not_tbd(self, schema_view):
        """BomItemElement_component description is not TBD."""
        slot = schema_view.get_slot("BomItemElement_component")
        assert slot is not None, "BomItemElement_component slot not found"
        assert slot.description != "TBD", (
            "BomItemElement_component description is still TBD"
        )
        assert len(slot.description) > 10, (
            "BomItemElement_component description is too short"
        )


# ---------------------------------------------------------------------------
# 5. XDOM-02: Vault GUID attrs deprecated
# ---------------------------------------------------------------------------


class TestVaultGuidDeprecated:
    """Verify vault GUID string attrs have deprecation annotations."""

    @pytest.mark.parametrize(
        "slot_name",
        [
            "Component_vaultGuid",
            "Component_itemGuid",
            "Component_revisionGuid",
        ],
    )
    def test_vault_guid_attr_deprecated(self, schema_view, slot_name):
        """Vault GUID attributes must have deprecated annotation."""
        slot = schema_view.get_slot(slot_name)
        assert slot is not None, f"{slot_name} slot not found"
        assert slot.deprecated is not None, (
            f"{slot_name} is missing deprecated annotation"
        )
        assert "des_component_library_source" in slot.deprecated, (
            f"{slot_name} deprecated text should reference des_component_library_source"
        )


# ---------------------------------------------------------------------------
# 6. Named slot metadata completeness (AGENTS.md compliance)
# ---------------------------------------------------------------------------


class TestCrossDomainSlotMetadata:
    """All new named slots have complete metadata per AGENTS.md."""

    @pytest.mark.parametrize(
        "slot_name,expected_alias,expected_subset",
        [
            ("des_component_library_source", "librarySource", "design"),
            ("des_component_variant", "variant", "design"),
            ("pro_bom_variant_design_variant", "designVariant", "procurement"),
        ],
    )
    def test_named_slot_has_required_metadata(
        self, schema_view, slot_name, expected_alias, expected_subset
    ):
        """Named slots must have slot_uri, alias, title, description, range, multivalued, required."""
        slot = schema_view.get_slot(slot_name)
        assert slot is not None, f"{slot_name} not found"

        # slot_uri
        assert slot.slot_uri is not None, f"{slot_name} missing slot_uri"

        # alias
        assert slot.alias == expected_alias, (
            f"{slot_name} alias: expected {expected_alias!r}, got {slot.alias!r}"
        )

        # title
        assert slot.title is not None and len(slot.title) > 0, (
            f"{slot_name} missing title"
        )

        # description
        assert slot.description is not None and len(slot.description) > 10, (
            f"{slot_name} missing or too-short description"
        )

        # range
        assert slot.range is not None, f"{slot_name} missing range"

        # multivalued must be explicitly set (False for these)
        assert slot.multivalued is not None, f"{slot_name} missing multivalued"

        # in_subset
        subsets = [s for s in slot.in_subset]
        assert expected_subset in subsets, (
            f"{slot_name} not in expected subset {expected_subset!r}, got {subsets}"
        )
