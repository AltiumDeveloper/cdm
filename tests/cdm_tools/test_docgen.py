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
               api_dir=str(REPO / "src/docs/api"), findings_path=str(REPO / "MODEL-FINDINGS.md"))
    page = (tmp_path / "subsets" / "library.md").read_text(encoding="utf-8")
    head = page.split("## Classes in Bounded Context")[0]
    assert "In the product" in head
    assert "Coverage" in head and "classes" in head and "(../coverage.md)" in head
    assert "GRID" in head and "(../classes/lib_Component.md)" in head and "`grid:" in head
    assert "## Classes in Bounded Context" in page


def test_subset_page_empty_product_docs_state(tmp_path):
    _serialize(tmp_path, registry_path=str(REPO / "src/docs/links/registry.yaml"),
               api_dir=str(REPO / "src/docs/api"), findings_path=str(REPO / "MODEL-FINDINGS.md"))
    ota = (tmp_path / "subsets" / "ota.md").read_text(encoding="utf-8")
    assert "No product documentation linked yet." in ota.split("## Classes in Bounded Context")[0]


def test_subset_hub_computed_once_per_subset():
    gen = CdmDocGenerator(
        str(REPO / "src/common_data_model/schema/common_data_model.yaml"),
        template_directory=str(REPO / "src/docs/templates"),
        registry_path=str(REPO / "src/docs/links/registry.yaml"),
        api_dir=str(REPO / "src/docs/api"),
        findings_path=str(REPO / "MODEL-FINDINGS.md"),
    )
    env = jinja2.Environment()
    gen.customize_environment(env)
    element = gen.schemaview.get_subset("library")
    assert env.globals["subset_hub"](element) is env.globals["subset_hub"](element)


def test_subset_page_without_subset_hub_still_renders(tmp_path):
    _serialize(tmp_path)  # no registry, api or findings
    page = (tmp_path / "subsets" / "library.md").read_text(encoding="utf-8")
    assert "## Classes in Bounded Context" in page
    assert "Coverage" not in page.split("## Classes in Bounded Context")[0]


def test_main_fails_on_missing_findings(tmp_path, capsys):
    from cdm_tools.docgen import main

    missing = tmp_path / "nope.md"
    rc = main([str(REPO / "src/common_data_model/schema/common_data_model.yaml"), "-d", str(tmp_path / "out"),
               "--template-directory", str(REPO / "src/docs/templates"),
               "--registry", str(REPO / "src/docs/links/registry.yaml"),
               "--api-dir", str(REPO / "src/docs/api"), "--findings", str(missing)])
    assert rc == 2
    assert f"cdm-gendoc: findings file not found: {missing}" in capsys.readouterr().err
