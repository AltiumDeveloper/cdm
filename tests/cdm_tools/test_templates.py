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


from cdm_tools.hub import ApiView, DocLink, HubView, Mapping, NexarView, Term


def _render_panel(h):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(TEMPLATES)))
    t = env.from_string("{% from 'macros.jinja2' import hub_panel %}{{ hub_panel(h) }}")
    return t.render(h=h)


def test_hub_panel_full():
    h = HubView(
        links=[DocLink("Primary Page", "https://a/p", True), DocLink("Other", "https://a/o", False)],
        terms=[Term("Company Account", "exact", ["altium-dashboard"], "https://a/p")],
        api=ApiView("DesX", "OBJECT", "https://api/types/objects/DesX/"),
        mappings=[Mapping("exact", "prov:Entity", "http://www.w3.org/ns/prov#Entity")],
    )
    out = _render_panel(h)
    assert '!!! abstract "In the product"' in out
    assert "Known as: **Company Account** (altium-dashboard)" in out
    assert "- [Primary Page](https://a/p) *(primary)*" in out
    assert "- [Other](https://a/o)" in out
    assert '!!! abstract "In the API"' in out
    assert "Type: [`DesX`](https://api/types/objects/DesX/)" in out
    assert "Type: [`DesX`](https://api/types/objects/DesX/) (object)" in out
    for absent in ("Read:", "Write", "Reached via", "node(id)"):
        assert absent not in out
    assert '!!! abstract "In standards"' in out
    assert "exact: [prov:Entity](http://www.w3.org/ns/prov#Entity)" in out


def test_hub_panel_empty_states():
    out = _render_panel(HubView(product_docs_none=True))
    assert "No public product documentation exists for this concept." in out
    assert "No Platform API type." in out
    assert "In standards" not in out
    out2 = _render_panel(HubView(api_missing="DmProcessor"))
    assert "No product documentation linked yet." in out2
    assert "`DmProcessor` is not in the Platform API snapshot." in out2


def test_hub_panel_nexar():
    out = _render_panel(HubView(nexar=NexarView("SupPart", "https://oct/api")))
    assert "Nexar type: `SupPart` ([Octopart API](https://oct/api))" in out
    assert "No Platform API type." not in out


def _render_link(h):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(TEMPLATES)))
    t = env.from_string("{% from 'macros.jinja2' import api_type_link %}[{{ api_type_link(h) }}]")
    return t.render(h=h)


def test_api_type_link_cases():
    assert _render_link(HubView(api=ApiView("DesX", "OBJECT", "https://api/DesX/"))) == "[[`DesX`](https://api/DesX/)]"
    assert _render_link(HubView(api=ApiView("DesX", "OBJECT", None))) == "[`DesX`]"
    assert _render_link(HubView(api_missing="DmX")) == "[`DmX` (not in Platform API snapshot)]"
    assert _render_link(HubView()) == "[]"


def test_hub_panel_nexar_missing_and_no_kind():
    out = _render_panel(HubView(nexar_missing="SupX"))
    assert "`SupX` is not in the Nexar API snapshot." in out
    assert "No Platform API type." not in out
    out2 = _render_panel(HubView(api=ApiView("DesX", "", None)))
    assert "Type: `DesX`" in out2 and "()" not in out2


def test_api_type_link_nexar_variants():
    assert _render_link(HubView(nexar=NexarView("SupPart", "https://o"))) == "[[`SupPart`](https://o) (Nexar)]"
    assert _render_link(HubView(nexar_missing="SupX")) == "[`SupX` (not in Nexar API snapshot)]"
