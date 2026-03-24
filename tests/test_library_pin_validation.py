"""Validation tests for Phase 6 library pin, enum, and symbol revision additions.

Tests confirm that generated Python dataclasses for lib_pin, lib_pin_parameter,
lib_pin_function, lib_PinElectricalType, and lib_ComponentKind work end-to-end.
"""

import os

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.enumerations import EnumDefinitionImpl

from common_data_model.datamodel.common_data_model import (
    LibPin,
    LibPinParameter,
    LibPinFunction,
    LibPinElectricalType,
    LibComponentKind,
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


class TestPinElectricalTypeEnum:
    """Verify lib_PinElectricalType enum has all 8 Altium domain values."""

    def test_all_eight_values_exist(self):
        expected = {
            "INPUT",
            "IO",
            "OUTPUT",
            "OPEN_COLLECTOR",
            "PASSIVE",
            "HI_Z",
            "OPEN_EMITTER",
            "POWER",
        }
        actual = _enum_value_texts(LibPinElectricalType)
        assert expected == actual, (
            f"Missing: {expected - actual}, Extra: {actual - expected}"
        )


class TestComponentKindEnum:
    """Verify lib_ComponentKind enum has all 7 Altium domain values."""

    def test_all_seven_values_exist(self):
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


class TestLibPin:
    """Verify lib_pin class accepts all specified attributes."""

    def test_pin_with_all_core_attributes(self):
        pin = LibPin(
            name="GPIO_0",
            designator="A3",
            description="General purpose I/O pin with alternate UART function",
            electricalType="IO",
            propagationDelay="1.2ns",
            packageLength="3.5mm",
            partId="1",
        )
        assert pin is not None
        assert pin.name == "GPIO_0"
        assert pin.designator == "A3"
        assert pin.description == "General purpose I/O pin with alternate UART function"
        assert str(pin.electricalType) == "IO"
        assert pin.propagationDelay == "1.2ns"
        assert pin.packageLength == "3.5mm"
        assert pin.partId == "1"

    def test_pin_with_parameters(self):
        param = LibPinParameter(
            name="max_frequency",
            value="100MHz",
            type="frequency",
        )
        pin = LibPin(
            name="CLK",
            designator="B1",
            parameters=[param],
        )
        assert pin.parameters is not None
        assert len(pin.parameters) == 1
        assert pin.parameters[0].name == "max_frequency"
        assert pin.parameters[0].value == "100MHz"

    def test_pin_with_functions(self):
        func = LibPinFunction(
            name="UART_TX",
            electricalType="OUTPUT",
        )
        pin = LibPin(
            name="GPIO_0",
            designator="A3",
            functions=[func],
        )
        assert pin.functions is not None
        assert len(pin.functions) == 1
        assert pin.functions[0].name == "UART_TX"


class TestLibraryPinExampleData:
    """Verify example YAML data loads through the generated datamodel."""

    def test_example_yaml_loads(self):
        path = os.path.join(ROOT, "src", "data", "examples", "library-pin-example.yaml")
        assert os.path.exists(path), f"Example file not found: {path}"
        obj = yaml_loader.load(path, target_class=LibPin)
        assert obj is not None
        assert obj.name == "GPIO_0"
        assert obj.designator == "A3"
