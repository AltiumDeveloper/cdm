"""Tests for the gen-doc Jinja templates in src/docs/templates."""

from pathlib import Path
from types import SimpleNamespace

import jinja2

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = REPO_ROOT / "src" / "docs" / "templates"

PLATFORM_API_BASE = "https://altiumdeveloper.github.io/platform-api-docs/types"
OCTOPART_API_DOC = "https://www.altium.com/documentation/altium-developer-center/octopart/api"
PUBLIC_GRID_DOC = (
    "https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/grid"
)


def _element(**annotations):
    """Minimal stand-in for a LinkML ClassDefinition as seen by the templates."""
    return SimpleNamespace(
        annotations={k: SimpleNamespace(value=v) for k, v in annotations.items()}
    )


def _render_macro(macro_name: str, element) -> str:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(TEMPLATES)))
    template = env.from_string(
        "{% from 'macros.jinja2' import " + macro_name + " with context %}"
        "{{ " + macro_name + "(element) }}"
    )
    return template.render(element=element).strip()


def test_platform_api_url_object_type():
    out = _render_macro("platform_api_url", _element(platformAPI="DesProject"))
    assert out == f"[DesProject]({PLATFORM_API_BASE}/objects/DesProject)"


def test_platform_api_url_absent_renders_nothing():
    assert _render_macro("platform_api_url", _element()) == ""


def test_platform_api_url_interface_type():
    out = _render_macro("platform_api_url", _element(platformAPI="BomItemElement"))
    assert out == f"[BomItemElement]({PLATFORM_API_BASE}/interfaces/BomItemElement)"


def test_platform_api_url_event_subscription_is_interface():
    out = _render_macro("platform_api_url", _element(platformAPI="GloEvtSubscription"))
    assert out == f"[GloEvtSubscription]({PLATFORM_API_BASE}/interfaces/GloEvtSubscription)"


def test_nexar_api_url_renders_type_and_doc_link():
    out = _render_macro("nexar_api_url", _element(nexarAPI="SupPart"))
    assert out == f"[SupPart (Nexar)]({OCTOPART_API_DOC})"


def test_nexar_api_url_absent_renders_nothing():
    assert _render_macro("nexar_api_url", _element(platformAPI="DesProject")) == ""


def test_class_template_links_public_grid_page_only():
    text = (TEMPLATES / "class.md.jinja2").read_text(encoding="utf-8")
    assert "atlassian.net" not in text
    assert PUBLIC_GRID_DOC in text


def test_see_also_rendered_once_on_class_page(tmp_path):
    from cdm_tools.docgen import CdmDocGenerator

    schema = REPO_ROOT / "src" / "common_data_model" / "schema" / "common_data_model.yaml"
    gen = CdmDocGenerator(
        str(schema),
        template_directory=str(TEMPLATES),
        registry_path=str(REPO_ROOT / "src" / "docs" / "links" / "registry.yaml"),
        subfolder_type_separation=True,
        preserve_names=True,
    )
    gen.serialize(directory=str(tmp_path))
    page = (tmp_path / "classes" / "plt_LifecycleDefinition.md").read_text()
    url = "https://www.altium.com/documentation/altium-365/lifecycle-management"
    assert page.count(url) == 1
