"""Every bounded context (subset) has a colour/icon rule in custom.css and a page in the site navigation."""
import re
from pathlib import Path

import yaml
from linkml_runtime.utils.schemaview import SchemaView

REPO = Path(__file__).resolve().parents[2]
SCHEMA = REPO / "src/common_data_model/schema/common_data_model.yaml"


def _subsets():
    return sorted(SchemaView(str(SCHEMA)).all_subsets())


def test_every_subset_has_a_title():
    view = SchemaView(str(SCHEMA))
    assert [name for name, s in view.all_subsets().items() if not s.title] == []


def test_every_subset_has_a_colour_and_icon_rule():
    css = (REPO / "src/docs/files/css/custom.css").read_text(encoding="utf-8")
    for name in _subsets():
        rule = re.compile(r"\.bc-" + re.escape(name) + r" \{\s*--bc-bg: #[0-9a-f]{6};\s*--bc-img: url\(\"data:image/svg\+xml,")
        assert rule.search(css), f"missing .bc-{name} rule in src/docs/files/css/custom.css"


def test_every_subset_page_is_in_the_navigation():
    text = (REPO / "mkdocs.yml").read_text(encoding="utf-8")
    # mkdocs.yml uses !!python/name tags; read the nav block only
    nav = yaml.safe_load(text[text.index("nav:\n"):text.index("# Not pages of the site")])["nav"]
    section = next(item["Bounded Contexts"] for item in nav if isinstance(item, dict) and "Bounded Contexts" in item)
    assert sorted(section) == sorted(f"subsets/{name}.md" for name in _subsets())


def test_navigation_lists_bounded_contexts_in_the_shared_order():
    from cdm_tools.contexts import subset_sort_key

    text = (REPO / "mkdocs.yml").read_text(encoding="utf-8")
    nav = yaml.safe_load(text[text.index("nav:\n"):text.index("# Not pages of the site")])["nav"]
    section = next(item["Bounded Contexts"] for item in nav if isinstance(item, dict) and "Bounded Contexts" in item)
    names = [entry[len("subsets/"):-len(".md")] for entry in section]
    assert names == sorted(names, key=subset_sort_key)


def test_every_subset_but_core_links_to_an_api_context():
    from cdm_tools.contexts import api_context

    missing = [name for name in _subsets() if name != "core" and api_context(name) is None]
    assert missing == []
    assert api_context("library") == (
        "Library Management", "https://altiumdeveloper.github.io/platform-api-docs/reference/library-management/overview")
    assert api_context("core") is None
