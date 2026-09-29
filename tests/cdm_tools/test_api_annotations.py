"""Pins API type annotations verified against production introspection (2026-09-29).

Phase 1 replaces this with lint rule DOC-03 against a checked-in API snapshot.
"""

from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

ROOT_SCHEMA = (
    Path(__file__).resolve().parents[2]
    / "src" / "common_data_model" / "schema" / "common_data_model.yaml"
)


@pytest.fixture(scope="module")
def sv() -> SchemaView:
    return SchemaView(str(ROOT_SCHEMA))


def _annotation(sv: SchemaView, class_name: str, key: str):
    ann = sv.get_class(class_name).annotations
    return ann[key].value if key in ann else None


EXPECTED_PLATFORM_API = {
    "des_RuleCheck": "RuleCheck",
    "des_RuleCheckExecution": "RuleCheckExecution",
    "dm_ConfiguredDeviceModel": "DmDeviceModelAsConfigured",
    "dm_AddressMap": "DmAddressMapModel",
    "dm_Memory": "DmAmMemory",
    "dm_Register": "DmAmRegister",
    "dm_RegisterField": "DmAmRegisterField",
    "dm_FieldEnum": "DmAmFieldEnum",
    "dm_PortConfigurationEnumValue": "DmConfigEnumValue",
    "dm_PortConfigurationDependency": "DmConfigDependency",
    "sup_ReferenceDesign": "SupRefDesign",
    "dm_Processor": None,
    "sup_Part": None,
    "sup_Offer": None,
    "sup_Company": None,
}

EXPECTED_NEXAR_API = {
    "sup_Part": "SupPart",
    "sup_Offer": "SupOffer",
    "sup_Company": "SupCompany",
}


@pytest.mark.parametrize("class_name,expected", sorted(EXPECTED_PLATFORM_API.items()))
def test_platform_api(sv, class_name, expected):
    assert _annotation(sv, class_name, "platformAPI") == expected


@pytest.mark.parametrize("class_name,expected", sorted(EXPECTED_NEXAR_API.items()))
def test_nexar_api(sv, class_name, expected):
    assert _annotation(sv, class_name, "nexarAPI") == expected
