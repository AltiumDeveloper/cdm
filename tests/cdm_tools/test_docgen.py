from pathlib import Path

import jinja2

from cdm_tools.docgen import CdmDocGenerator, make_doc_link
from cdm_tools.registry import LinkEntry

REPO = Path(__file__).resolve().parents[2]
URL = "https://www.altium.com/documentation/altium-365/lifecycle-management"


def _registry():
    return {
        URL: LinkEntry(url=URL, title="Lifecycle Management", source="altium-docs", anchors=["states"]),
        "https://std.example/svd.html": LinkEntry(
            url="https://std.example/svd.html", title="Raw Title", label="Nice Label", source="standard"
        ),
    }


def test_doc_link_uses_registry_title():
    assert make_doc_link(_registry())(URL) == f"[Lifecycle Management]({URL})"


def test_doc_link_keeps_fragment_in_href():
    assert make_doc_link(_registry())(URL + "#states") == f"[Lifecycle Management]({URL}#states)"


def test_doc_link_prefers_label():
    assert make_doc_link(_registry())("https://std.example/svd.html") == "[Nice Label](https://std.example/svd.html)"


def test_doc_link_uses_anchor_label():
    reg = _registry()
    reg[URL].anchor_labels = {"states": "Lifecycle states"}
    assert make_doc_link(reg)(URL + "#states") == f"[Lifecycle states]({URL}#states)"
    assert make_doc_link(reg)(URL) == f"[Lifecycle Management]({URL})"


def test_doc_link_unknown_url_renders_autolink():
    assert make_doc_link({})("https://unknown.example/") == "<https://unknown.example/>"


def test_generator_registers_doc_link_global(tmp_path):
    reg = tmp_path / "registry.yaml"
    reg.write_text(f"{URL}:\n  title: Lifecycle Management\n  source: altium-docs\n", encoding="utf-8")
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        registry_path=str(reg),
    )
    env = jinja2.Environment()
    gen.customize_environment(env)
    assert env.globals["doc_link"](URL) == f"[Lifecycle Management]({URL})"


def _main_args(tmp_path, registry):
    return [
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        "-d", str(tmp_path / "out"),
        "--template-directory", str(REPO / "src/docs/templates"),
        "--registry", str(registry),
    ]


def test_main_fails_on_missing_registry(tmp_path, capsys):
    from cdm_tools.docgen import main

    missing = tmp_path / "nope.yaml"
    assert main(_main_args(tmp_path, missing)) == 2
    assert f"cdm-gendoc: link registry not found: {missing}" in capsys.readouterr().err
    assert not (tmp_path / "out").exists()


def test_main_fails_on_malformed_registry(tmp_path, capsys):
    from cdm_tools.docgen import main

    reg = tmp_path / "registry.yaml"
    reg.write_text(f"{URL}:\n  source: altium-docs\n", encoding="utf-8")
    assert main(_main_args(tmp_path, reg)) == 2
    assert "cdm-gendoc: invalid link registry:" in capsys.readouterr().err
    assert not (tmp_path / "out").exists()


def test_rendered_class_page_has_hub_panel(tmp_path):
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        registry_path=str(REPO / "src/docs/links/registry.yaml"),
        api_dir=str(REPO / "src/docs/api"),
        subfolder_type_separation=True,
        preserve_names=True,
    )
    gen.serialize(directory=str(tmp_path))
    page = (tmp_path / "classes" / "plt_LifecycleDefinition.md").read_text(encoding="utf-8")
    assert "- [Defining Lifecycle Definitions for a Workspace](https://www.altium.com/documentation/altium-designer/connected-workspace/defining-lifecycle-definitions) *(primary)*" in page
    assert "Type: [`DesLifeCycleDefinition`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesLifeCycleDefinition/)" in page
    for absent in ("Read:", "Write", "Reached via", "node(id)"):
        assert absent not in page
    sup = (tmp_path / "classes" / "sup_Part.md").read_text(encoding="utf-8")
    assert "Nexar type: `SupPart`" in sup
    assert 'quote "Platform API"' not in page
    index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "[`DesLifeCycleDefinition`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesLifeCycleDefinition/)" in index


def test_main_exits_2_when_api_dir_missing(tmp_path, capsys):
    from cdm_tools.docgen import main
    rc = main([str(REPO / "src/common_data_model/schema/common_data_model.yaml"), "-d", str(tmp_path),
               "--template-directory", str(REPO / "src/docs/templates"),
               "--api-dir", str(tmp_path / "nope")])
    assert rc == 2
    assert "API snapshot directory not found" in capsys.readouterr().err


def _serialize(tmp_path, **kw):
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        subfolder_type_separation=True,
        preserve_names=True,
        **kw,
    )
    gen.serialize(directory=str(tmp_path))
    return gen


def test_subset_page_has_overview(tmp_path):
    _serialize(tmp_path, registry_path=str(REPO / "src/docs/links/registry.yaml"),
               api_dir=str(REPO / "src/docs/api"))
    page = (tmp_path / "subsets" / "library.md").read_text(encoding="utf-8")
    head = page.split("## Entities")[0]
    assert "In the product" in head
    assert "Coverage" not in head and "coverage.md" not in page
    # Root IRI + subset name, which w3id.org resolves; GRID templates are on the class pages and the GRIDs page
    assert "IRI: [https://w3id.org/altium/cdm/library](https://w3id.org/altium/cdm/library)" in head
    assert "`grid:" not in head and "Identifier and Mapping Information" not in page
    assert "## Entities" in page


def test_subset_page_empty_product_docs_state(tmp_path):
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        registry_path=str(REPO / "src/docs/links/registry.yaml"),
        api_dir=str(REPO / "src/docs/api"),
        subfolder_type_separation=True,
        preserve_names=True,
    )
    gen.schemaview.get_subset("library").see_also = []
    gen.serialize(directory=str(tmp_path))
    head = (tmp_path / "subsets" / "library.md").read_text(encoding="utf-8").split("## Entities")[0]
    assert "No product documentation linked yet." in head


def test_subset_page_product_docs_none(tmp_path):
    _serialize(tmp_path, registry_path=str(REPO / "src/docs/links/registry.yaml"),
               api_dir=str(REPO / "src/docs/api"))
    core = (tmp_path / "subsets" / "core.md").read_text(encoding="utf-8").split("## Entities")[0]
    assert "No public product documentation exists for this bounded context." in core
    assert "No product documentation linked yet." not in core


def test_subset_hub_computed_once_per_subset():
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        registry_path=str(REPO / "src/docs/links/registry.yaml"),
        api_dir=str(REPO / "src/docs/api"),
    )
    env = jinja2.Environment()
    gen.customize_environment(env)
    element = gen.schemaview.get_subset("library")
    assert env.globals["subset_hub"](element) is env.globals["subset_hub"](element)


def test_subset_page_overview_without_registry(tmp_path):
    _serialize(tmp_path)  # no registry or api: links render as autolinks
    head = (tmp_path / "subsets" / "library.md").read_text(encoding="utf-8").split("## Entities")[0]
    assert "## In the product" in head and "- <https://" in head
    assert "IRI: [https://w3id.org/altium/cdm/library]" in head


def test_subset_see_also_rendered_once(tmp_path):
    url = "https://www.altium.com/documentation/altium-365/lifecycle-management"
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        registry_path=str(REPO / "src/docs/links/registry.yaml"),
        api_dir=str(REPO / "src/docs/api"),
        subfolder_type_separation=True,
        preserve_names=True,
    )
    gen.schemaview.get_subset("library").see_also = [url]
    gen.serialize(directory=str(tmp_path))
    page = (tmp_path / "subsets" / "library.md").read_text(encoding="utf-8")
    assert page.count(url) == 1
    assert "## See Also" not in page


def test_grid_templates_shared_helper():
    from linkml_runtime.utils.schemaview import SchemaView

    from cdm_tools.reference import grid_templates

    sv = SchemaView(str(REPO / "src/common_data_model/schema/common_data_model.yaml"))
    rows = {r[0]: r for r in grid_templates(sv)}
    assert rows["lib_Component"] == (
        "lib_Component", "library", "library", "grid:workspace:{workspace-id}:library:component/{id}")


def test_main_writes_schema_index_as_home_page(tmp_path):
    from cdm_tools.docgen import main

    out = tmp_path / "out"
    out.mkdir()
    about = REPO / "src/docs/files/about.md"
    (out / "about.md").write_text(about.read_text(encoding="utf-8"), encoding="utf-8")
    rc = main([str(REPO / "src/common_data_model/schema/common_data_model.yaml"), "-d", str(out),
               "--template-directory", str(REPO / "src/docs/templates"),
               "--registry", str(REPO / "src/docs/links/registry.yaml"), "--api-dir", str(REPO / "src/docs/api")])
    assert rc == 0
    assert (out / "about.md").read_text(encoding="utf-8") == about.read_text(encoding="utf-8")
    assert not (out / "bounded-contexts.md").exists()
    page = (out / "index.md").read_text(encoding="utf-8")
    assert page.lstrip().startswith("# Bounded Contexts\n")
    assert "## Bounded Contexts" in page and "| Name | Description | Platform API |" in page
    assert "( classes/lib_Component.md )" in page


def test_subset_iri_is_root_plus_subset_name_without_trailing_slash():
    from linkml_runtime.utils.schemaview import SchemaView

    from cdm_tools.docgen import subset_iri

    sv = SchemaView(str(REPO / "src/common_data_model/schema/common_data_model.yaml"))
    assert subset_iri(sv, "design") == "https://w3id.org/altium/cdm/design"
    assert subset_iri(sv, "requirements") == "https://w3id.org/altium/cdm/requirements"
    assert subset_iri(sv, "system-sdm") == "https://w3id.org/altium/cdm/system-sdm"


def test_class_page_identifiers_under_title(tmp_path):
    _serialize(tmp_path, registry_path=str(REPO / "src/docs/links/registry.yaml"), api_dir=str(REPO / "src/docs/api"))
    page = (tmp_path / "classes" / "des_Project.md").read_text(encoding="utf-8")
    assert "\nGRID: `grid:workspace:{workspace-id}:design:project/{id}`" in page
    assert page.index("IRI: ") < page.index("GRID: ")
    assert "!!! quote" not in page and "Identifier and Mapping Information" not in page
    assert "Bounded context:" not in page   # the breadcrumbs name the bounded context
    assert "* [Entity](../classes/core_Entity.md)" in page and "core_Entity](" not in page.replace("(../classes/core_Entity", "")


def test_field_page_uses_titles_and_drops_technical_sections(tmp_path):
    _serialize(tmp_path, registry_path=str(REPO / "src/docs/links/registry.yaml"), api_dir=str(REPO / "src/docs/api"))
    page = (tmp_path / "slots" / "core_releases.md").read_text(encoding="utf-8")
    assert "* [has output](core_hasOutput.md)" in page          # parent field by title
    parent = (tmp_path / "slots" / "core_hasOutput.md").read_text(encoding="utf-8")
    assert "* Range: [Artifact]( ../classes/core_Artifact.md )" in parent   # range class by title
    assert page.lstrip().startswith("# Field: releases") and "(core_releases)" not in page
    assert page.index("## Properties") < page.index("## Used by")
    for absent in ("IRI:", "LinkML Source", "Identifier and Mapping Information", "Applicable Classes"):
        assert absent not in page and absent not in parent


def test_diagram_node_colour_helpers():
    from cdm_tools.docgen import darken, text_on

    assert darken("#93c47d") == "#607f51" and darken("#cccccc") == "#858585" and darken("bad") == "bad"
    assert text_on("#0c559c") == "#ffffff" and text_on("#3c78d8") == "#ffffff" and text_on("#a64d79") == "#ffffff"
    assert text_on("#93c47d") == "#14181f" and text_on("#ffe599") == "#14181f" and text_on("#cccccc") == "#14181f"


def test_class_diagram_styles_nodes_and_hides_core_parents(tmp_path):
    _serialize(tmp_path, registry_path=str(REPO / "src/docs/links/registry.yaml"), api_dir=str(REPO / "src/docs/api"))
    page = (tmp_path / "classes" / "des_Project.md").read_text(encoding="utf-8")
    assert "style des_Project fill:#93c47d,stroke:#607f51,color:#14181f,stroke-width:2.5px" in page   # current node
    assert "style des_HarnessProject fill:#93c47d,stroke:#607f51,color:#14181f,stroke-width:1px" in page
    assert "core_Activity <|-- des_Project" not in page    # core base types are not drawn as parents
