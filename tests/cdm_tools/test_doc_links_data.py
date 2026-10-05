from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.registry import load_registry, lookup

REPO = Path(__file__).resolve().parents[2]
AD = "https://www.altium.com/documentation/altium-designer/connected-workspace/"
A365_LIFECYCLE = "https://www.altium.com/documentation/altium-365/lifecycle-management"


@pytest.fixture(scope="module")
def sv():
    return SchemaView(str(REPO / "src/common_data_model/schema/common_data_model.yaml"))


@pytest.fixture(scope="module")
def registry():
    return load_registry(REPO / "src/docs/links/registry.yaml")


def test_no_class_uses_documentation_extension(sv):
    offenders = [n for n, c in sv.all_classes().items() if c.extensions and "documentation" in c.extensions]
    assert offenders == []


@pytest.mark.parametrize(
    "cls,expected",
    [
        ("plt_LifecycleDefinition", [AD + "defining-lifecycle-definitions", A365_LIFECYCLE]),
        ("plt_LifecycleStage", [A365_LIFECYCLE]),
        ("plt_LifecycleState", [A365_LIFECYCLE]),
        ("plt_NamingScheme", [AD + "defining-naming-schemes"]),
    ],
)
def test_migrated_see_also(sv, cls, expected):
    assert list(sv.get_class(cls).see_also) == expected


def test_every_see_also_is_registered(sv, registry):
    missing = [
        (n, u) for n, c in sv.all_classes().items() for u in (c.see_also or []) if lookup(registry, u) is None
    ]
    assert missing == []
