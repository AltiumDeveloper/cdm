"""Validation tests for Phase 8 BOM domain additions.

Tests confirm that generated Python dataclasses for pro_BomVariant,
extended pro_BomItem (ModelsProvider fields), and pro_ManagedBOM version work end-to-end.
"""

import os
import pytest

from linkml_runtime.loaders import yaml_loader

from common_data_model.datamodel.common_data_model import (
    ProBomItem,
    ProBomVariant,
    ProManagedBOM,
)

ROOT = os.path.join(os.path.dirname(__file__), "..")


class TestBomVariant:
    """Verify pro_BomVariant class creation and variant scoping."""

    def test_bom_variant_with_items(self):
        """Create BomVariant with variantId and BomItems, validate structure."""
        item1 = ProBomItem(
            quantity=2,
            designators=["R1", "R2"],
            designItemId="COMP-RES-10K",
            description="Resistor, 10K, 1%",
            comment="10K",
            mpn="RC0402FR-0710KL",
        )
        item2 = ProBomItem(
            quantity=3,
            designators=["C1", "C2", "C3"],
            designItemId="COMP-CAP-100NF",
            description="Capacitor, 100nF, 50V",
            comment="100nF",
            mpn="GRM155R71H104KE14D",
        )
        variant = ProBomVariant(
            variantId="Default",
            items=[item1, item2],
        )
        assert variant.variantId == "Default"
        assert len(variant.items) == 2
        assert variant.items[0].quantity == 2
        assert variant.items[1].mpn == "GRM155R71H104KE14D"

    def test_bom_variant_no_variant_sentinel(self):
        """BomVariant with 'NoVariant' id represents the base (unvaried) BOM."""
        variant = ProBomVariant(
            variantId="NoVariant",
            items=[ProBomItem(quantity=1)],
        )
        assert variant.variantId == "NoVariant"
        assert len(variant.items) == 1

    def test_bom_variant_required_variant_id(self):
        """variantId is required — omitting it raises ValueError."""
        with pytest.raises(ValueError, match="variantId must be supplied"):
            ProBomVariant(items=[ProBomItem(quantity=1)])


class TestBomItemModelsProviderFields:
    """Verify pro_BomItem has the 4 new ModelsProvider attributes."""

    def test_bom_item_with_all_models_provider_fields(self):
        """BomItem with designItemId, description, comment, mpn."""
        item = ProBomItem(
            quantity=5,
            designators=["U1", "U2", "U3", "U4", "U5"],
            designItemId="COMP-IC-STM32",
            description="MCU, ARM Cortex-M4, 168MHz",
            comment="STM32F407VGT6",
            mpn="STM32F407VGT6",
        )
        assert item.quantity == 5
        assert item.designItemId == "COMP-IC-STM32"
        assert item.description == "MCU, ARM Cortex-M4, 168MHz"
        assert item.comment == "STM32F407VGT6"
        assert item.mpn == "STM32F407VGT6"
        assert len(item.designators) == 5

    def test_bom_item_missing_required_quantity(self):
        """quantity is required — omitting it raises ValueError."""
        with pytest.raises(ValueError, match="quantity must be supplied"):
            ProBomItem(
                designItemId="COMP-001",
                mpn="ABC123",
            )

    def test_bom_item_backward_compatible(self):
        """Existing BomItem attributes still work unchanged after extension."""
        item = ProBomItem(
            quantity=1,
            designators=["J1"],
        )
        assert item.quantity == 1
        assert item.designators == ["J1"]
        # New fields default to None when not provided
        assert item.designItemId is None
        assert item.description is None
        assert item.comment is None
        assert item.mpn is None


class TestManagedBomVersion:
    """Verify pro_ManagedBOM carries the version attribute."""

    def test_managed_bom_with_version(self):
        """ManagedBOM with version string from ModelsProvider BomData."""
        bom = ProManagedBOM(
            id="bom-test-001",
            version="1.0.0.0",
        )
        assert bom.version == "1.0.0.0"

    def test_managed_bom_without_version(self):
        """Version is optional — ManagedBOM works without it."""
        bom = ProManagedBOM(id="bom-test-002")
        assert bom.version is None


class TestBomMixinVariants:
    """Verify pro_Bom mixin's variants slot is accessible on ManagedBOM."""

    def test_managed_bom_carries_variants(self):
        """ManagedBOM (via pro_Bom mixin) can carry variant-scoped BOM groupings."""
        variant = ProBomVariant(
            variantId="Production",
            items=[ProBomItem(quantity=10, mpn="LM317T")],
        )
        bom = ProManagedBOM(
            id="bom-test-003",
            version="1.0.0.0",
            variants=[variant],
        )
        assert len(bom.variants) == 1
        assert bom.variants[0].variantId == "Production"
        assert bom.variants[0].items[0].mpn == "LM317T"


class TestExampleYamlLoads:
    """Verify example YAML data loads through the generated datamodel."""

    def test_example_yaml_loads(self):
        path = os.path.join(
            ROOT, "src", "data", "examples", "procurement-bom-example.yaml"
        )
        assert os.path.exists(path), f"Example file not found: {path}"
        obj = yaml_loader.load(path, target_class=ProBomItem)
        assert obj is not None
        assert obj.quantity == 3
        assert obj.designItemId == "COMP-CAP-10UF"
        assert obj.mpn == "GRM188R61E106MA12D"
        assert len(obj.designators) == 3
