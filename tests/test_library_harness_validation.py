"""Validation tests for Phase 7 library harness wiring additions.

Tests confirm that generated Python dataclasses for lib_harness_wiring,
lib_HarnessWiringType enum, and HasLibraryComponentFields mixin work end-to-end.
"""

import os

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.enumerations import EnumDefinitionImpl

from common_data_model.datamodel.common_data_model import (
    LibHarnessWiring,
    LibHarnessWiringType,
    LibComponentKind,
    LibComponentParameter,
    PltLifecycleState,
)

ROOT = os.path.join(os.path.dirname(__file__), "..")


def _enum_value_texts(enum_cls: type[EnumDefinitionImpl]) -> set[str]:
    """Extract all permissible value texts from a LinkML-generated enum class."""
    texts = set()
    for attr_name in dir(enum_cls):
        if attr_name.startswith("_"):
            continue
        attr = getattr(enum_cls, attr_name)
        if hasattr(attr, "text"):
            texts.add(attr.text)
    return texts


def _make_lifecycle(name: str = "Production") -> PltLifecycleState:
    """Helper to create a PltLifecycleState instance."""
    return PltLifecycleState(LifecycleState_name=name)


class TestHarnessWiringTypeEnum:
    """Verify lib_HarnessWiringType enum has exactly 3 values."""

    def test_all_three_values_exist(self):
        expected = {"WIRE", "CABLE", "CAVITY"}
        actual = _enum_value_texts(LibHarnessWiringType)
        assert expected == actual, (
            f"Missing: {expected - actual}, Extra: {actual - expected}"
        )


class TestHarnessWiringWithAllAttributes:
    """Verify lib_harness_wiring class accepts all 7 harness-specific attributes."""

    def test_cable_with_all_attributes(self):
        wiring = LibHarnessWiring(
            id="harness-wiring-test-001",
            wiringType="CABLE",
            plt_LifecycleState=_make_lifecycle(),
            conductorsCount=4,
            colors=["Blue", "Red", "Green", "#1111EE"],
            gauges=["22AWG", "24AWG"],
            shieldsCount=2,
            twistsCount=1,
            twistRates=["10/m"],
        )
        assert wiring is not None
        assert str(wiring.wiringType) == "CABLE"
        assert wiring.conductorsCount == 4
        assert wiring.colors == ["Blue", "Red", "Green", "#1111EE"]
        assert wiring.gauges == ["22AWG", "24AWG"]
        assert wiring.shieldsCount == 2
        assert wiring.twistsCount == 1
        assert wiring.twistRates == ["10/m"]


class TestHarnessWiringMixinFields:
    """Verify HasLibraryComponentFields mixin fields are accessible on LibHarnessWiring."""

    def test_mixin_fields_accessible(self):
        param = LibComponentParameter(
            ComponentParameter_name="weight",
            ComponentParameter_value="50g",
        )
        wiring = LibHarnessWiring(
            id="harness-wiring-test-002",
            wiringType="WIRE",
            plt_LifecycleState=_make_lifecycle(),
            designItemId="WIRE-22AWG-BLU",
            designator="W2",
            description="Single conductor blue wire",
            comment="For signal routing",
            kind="STANDARD",
            parameters=[param],
        )
        assert wiring.designItemId == "WIRE-22AWG-BLU"
        assert wiring.designator == "W2"
        assert wiring.description == "Single conductor blue wire"
        assert wiring.comment == "For signal routing"
        assert str(wiring.kind) == "STANDARD"
        assert wiring.parameters is not None
        assert len(wiring.parameters) == 1
        assert wiring.parameters[0].ComponentParameter_name == "weight"


class TestWireVsCableDiscrimination:
    """Verify wire and cable are distinguished by wiringType enum, not class."""

    def test_wire_has_zero_conductors(self):
        wire = LibHarnessWiring(
            id="harness-wiring-wire-001",
            wiringType="WIRE",
            plt_LifecycleState=_make_lifecycle(),
            conductorsCount=0,
        )
        assert str(wire.wiringType) == "WIRE"
        assert wire.conductorsCount == 0

    def test_cable_has_positive_conductors(self):
        cable = LibHarnessWiring(
            id="harness-wiring-cable-001",
            wiringType="CABLE",
            plt_LifecycleState=_make_lifecycle(),
            conductorsCount=4,
            shieldsCount=1,
            twistsCount=2,
        )
        assert str(cable.wiringType) == "CABLE"
        assert cable.conductorsCount > 0

    def test_both_are_same_class(self):
        wire = LibHarnessWiring(
            id="harness-wiring-wire-002",
            wiringType="WIRE",
            plt_LifecycleState=_make_lifecycle(),
        )
        cable = LibHarnessWiring(
            id="harness-wiring-cable-002",
            wiringType="CABLE",
            plt_LifecycleState=_make_lifecycle(),
        )
        assert type(wire) is type(cable)


class TestExampleYamlLoads:
    """Verify example YAML data loads through the generated datamodel."""

    def test_example_yaml_loads(self):
        path = os.path.join(
            ROOT, "src", "data", "examples", "library-harness-wiring-example.yaml"
        )
        assert os.path.exists(path), f"Example file not found: {path}"
        obj = yaml_loader.load(path, target_class=LibHarnessWiring)
        assert obj is not None
        assert str(obj.wiringType) == "CABLE"
        assert obj.conductorsCount == 4
        assert obj.designItemId == "CABLE-SH4-22AWG"
        assert obj.designator == "W1"


class TestExistingPinTestsNotBroken:
    """Verify mixin refactoring didn't break existing domain types."""

    def test_component_kind_still_has_seven_values(self):
        """Ensure lib_ComponentKind enum unchanged after mixin introduction."""
        expected = {
            "STANDARD",
            "MECHANICAL",
            "GRAPHICAL",
            "NET_TIE_BOM",
            "NET_TIE_NO_BOM",
            "STANDARD_NO_BOM",
            "JUMPER",
        }
        actual = _enum_value_texts(LibComponentKind)
        assert expected == actual, (
            f"Missing: {expected - actual}, Extra: {actual - expected}"
        )
