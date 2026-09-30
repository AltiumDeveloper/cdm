import json
import posixpath
import re
import shutil
import textwrap
from pathlib import Path

import llms_txt
import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.llms import LINK, build_llms, main, write_files
from cdm_tools.reference import build_reference

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")
DOC = "https://example.org/docs/port"
LANDING = "https://example.org/docs/alpha"

SCHEMA = textwrap.dedent(f"""
    id: https://example.org/c
    name: c
    prefixes:
      linkml: https://w3id.org/linkml/
      prov: http://www.w3.org/ns/prov#
      ex: https://w3id.org/altium/cdm/alpha/
    default_prefix: ex
    imports: [linkml:types]
    subsets:
      alpha: {{description: "Models ports, e.g. pins. Second sentence.", see_also: ["{LANDING}"]}}
      beta: {{description: The beta context., annotations: {{productDocs: none}}}}
    classes:
      Any: {{class_uri: linkml:Any}}
      core_Meta: {{abstract: true, in_subset: [alpha], description: meta}}
      core_WithX: {{is_a: core_Meta, mixin: true, in_subset: [alpha], description: A mixin.}}
      core_Entity:
        abstract: true
        in_subset: [alpha]
        description: entity
        instantiates: [core_WithX]
        slots: [core_id]
      core_Artifact: {{abstract: true, is_a: core_Entity, in_subset: [alpha], description: An artifact.}}
      core_Activity: {{abstract: true, is_a: core_Entity, in_subset: [alpha], description: An activity.}}
      core_Resource: {{abstract: true, in_subset: [alpha], description: A resource.}}
      ex_Port:
        is_a: core_Artifact
        title: Port
        class_uri: ex:Port
        in_subset: [alpha]
        description: A connection point. Second sentence | with pipe.
        comments: [A comment.]
        see_also: ["{DOC}"]
        structured_aliases:
          - {{literal_form: Port, predicate: EXACT_SYNONYM, contexts: [altium-365]}}
        close_mappings: [prov:Entity]
        annotations:
          grid: "grid:workspace:{{workspace-id}}:system-design:port/{{id}}"
          platformAPI: DesX
        attributes:
          ex_Port_owner:
            is_a: core_partOf
            alias: owner
            range: ex_Project
            required: true
            description: The owning project. More.
          ex_Port_label: {{alias: label, range: string}}
      ex_SubPort:
        is_a: ex_Port
        title: Sub port
        class_uri: ex:SubPort
        in_subset: [alpha]
        description: A special port.
      ex_Project:
        is_a: core_Activity
        title: Project
        class_uri: ex:Project
        in_subset: [alpha]
        mixins: [ex_Named]
        description: A project.
        annotations: {{maturity: EXPERIMENTAL}}
        attributes:
          ex_Project_ports: {{is_a: core_hasPart, alias: ports, range: ex_Port, multivalued: true}}
      ex_Named: {{mixin: true, in_subset: [alpha], description: Adds a name.}}
      ex_Bare:
        is_a: core_Resource
        class_uri: ex:Bare
        in_subset: [beta]
        description: TBD
        annotations: {{nexarAPI: SupPart}}
    slots:
      core_id: {{range: string, alias: id}}
      core_hasPart: {{abstract: true, alias: hasPart, domain: core_Entity, range: core_Entity}}
      core_partOf: {{abstract: true, alias: partOf, domain: core_Entity, range: core_Entity}}
""")

ABOUT = textwrap.dedent("""\
    # About the model

    The model describes [things](https://example.org/things) as a schema. For each class it records what it is.
    A third sentence.

    See [the glossary](glossary.md) and [`llms.txt`](llms.txt).
""")

PAGES = {
    "grid-format.md": '# GRIDs\n\nThe catalogue:\n\n--8<-- "docs/_snippets/grid.md"\n\nMore [text](#format).\n',
    "domain-model.md": textwrap.dedent("""\
        # Domain Model

        - [alpha](subsets/alpha.md), [Port](classes/ex_Port.md), [home](index.md), [IRIs](grid-format.md#iris)
        - [slot](slots/core_id.md), [hub](hub.json), [ext](https://example.org/x), [top](#top)
    """),
    "entity-classification.md": "# Entity Classification\n\nBase classes.\n",
    "relation-types.md": "# Relation Types\n\nRelations.\n",
    "glossary.md": "# Glossary\n\n| Term | Class |\n| --- | --- |\n| Port | [Port](classes/ex_Port.md) |\n",
}
SNIPPET = "### alpha\n\n| [Port](classes/ex_Port.md) | `grid:workspace:{workspace-id}:system-design:port/{id}` |\n"


def _write_inputs(d: Path) -> None:
    (d / "c.yaml").write_text(SCHEMA, encoding="utf-8")
    (d / "registry.yaml").write_text(
        f"{DOC}:\n  title: Port docs\n  source: altium-docs\n  anchors: []\n"
        f"{LANDING}:\n  title: Alpha landing\n  source: altium-docs\n  anchors: []\n", encoding="utf-8")
    api = d / "api"
    api.mkdir()
    (api / "platform-schema.json").write_text(json.dumps(
        {"endpoint": "e", "retrieved": "2026-01-02", "query_type": "Query", "mutation_type": None,
         "types": {"Query": {"kind": "OBJECT", "fields": {}}, "DesX": {"kind": "OBJECT", "fields": {}}}}),
        encoding="utf-8")
    docs = d / "docs"
    (docs / "_snippets").mkdir(parents=True)
    (docs / "about.md").write_text(ABOUT, encoding="utf-8")
    for name, text in PAGES.items():
        (docs / name).write_text(text, encoding="utf-8")
    (docs / "_snippets/grid.md").write_text(SNIPPET, encoding="utf-8")


@pytest.fixture(scope="module")
def env(tmp_path_factory):
    d = tmp_path_factory.mktemp("llms")
    _write_inputs(d)
    return d


def _build(env):
    return build_llms(str(env / "c.yaml"), registry_path=str(env / "registry.yaml"), api_dir=str(env / "api"),
                      docs_dir=str(env / "docs"), repo_url="https://example.org/repo")


@pytest.fixture(scope="module")
def files(env):
    return _build(env)


def _html_pages(sv) -> set[str]:
    """Site-relative paths of the HTML pages and data files that the generated files may link to."""
    pages = {"", "hub.json", "hub.schema.json"} | {f"{p}/" for p in
                                                   ("about", "grid-format", "domain-model", "entity-classification",
                                                    "relation-types", "glossary", "tags")}
    for folder, names in (("classes", sv.all_classes()), ("subsets", sv.all_subsets()), ("slots", sv.all_slots()),
                          ("enums", sv.all_enums()), ("types", sv.all_types())):
        pages |= {f"{folder}/{n}/" for n in names}
    return pages


def _unresolved(files: dict[str, str], known: set[str]) -> list[tuple[str, str]]:
    bad = []
    for path, text in files.items():
        base = "" if path == "llms-full.txt" else posixpath.dirname(path)   # llms-full links are site-relative
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            resolved = posixpath.normpath(posixpath.join(base, target.split("#")[0]))
            resolved = "" if resolved == "." else resolved + ("/" if target.split("#")[0].endswith("/") else "")
            if resolved not in files and resolved not in known:
                bad.append((path, target))
    return bad


def test_llms_txt_parses(files):
    parsed = llms_txt.parse_llms_file(files["llms.txt"])
    assert parsed.title == "Altium Common Data Model (CDM)"
    assert parsed.summary == "The model describes things as a schema. For each class it records what it is."
    assert list(parsed.sections) == ["Start here", "Bounded contexts", "Machine-readable data", "Optional"]
    start = {l["title"]: l["url"] for l in parsed.sections["Start here"]}
    assert start == {"About":"llms/pages/about.md", "GRIDs": "llms/pages/grid-format.md",
                     "Domain Model": "llms/pages/domain-model.md",
                     "Entity Classification": "llms/pages/entity-classification.md",
                     "Relation Types": "llms/pages/relation-types.md", "Glossary": "llms/pages/glossary.md"}
    contexts = {l["title"]: l for l in parsed.sections["Bounded contexts"]}
    assert contexts["alpha"]["url"] == "llms/alpha.md"
    assert contexts["alpha"]["desc"] == "Models ports, e.g. pins. (3 classes; 7 base classes and mixins)"
    assert contexts["beta"]["desc"] == "The beta context. (1 class)"
    data = [l["url"] for l in parsed.sections["Machine-readable data"]]
    assert data == ["hub.json", "hub.schema.json", "llms-full.txt"]
    optional = [l["url"] for l in parsed.sections["Optional"]]
    assert optional[0] == "./" and "https://example.org/repo" in optional
    assert "2026-01-02" in parsed.info
    assert "12 classes" in parsed.info and "4 of them are concrete domain classes" in parsed.info


def test_one_card_per_class(env, files):
    sv = SchemaView(str(env / "c.yaml"))
    cards = {p for p in files if p.startswith("llms/classes/")}
    assert cards == {f"llms/classes/{n}.md" for n in sv.all_classes()}
    assert sorted(p for p in files if not p.startswith("llms/classes/")) == [
        "llms-full.txt", "llms.txt", "llms/alpha.md", "llms/beta.md",
        "llms/pages/about.md", "llms/pages/domain-model.md", "llms/pages/entity-classification.md",
        "llms/pages/glossary.md", "llms/pages/grid-format.md", "llms/pages/relation-types.md"]


def test_every_link_resolves(env, files):
    assert _unresolved(files, _html_pages(SchemaView(str(env / "c.yaml")))) == []


def test_catalogue(files):
    t = files["llms/alpha.md"]
    assert t.startswith("# Bounded context: alpha\n\nModels ports, e.g. pins. Second sentence.\n")
    assert "- [Alpha landing](https://example.org/docs/alpha) (primary)" in t
    assert "HTML page: [subsets/alpha/](../subsets/alpha/)" in t
    classes = [l for l in t.split("## Classes")[1].split("##")[0].splitlines() if l.startswith("- ")]
    assert classes == [
        "- [Port](classes/ex_Port.md): A connection point. · Artifact · API DesX"
        " · GRID `grid:workspace:{workspace-id}:system-design:port/{id}`",
        "- [Project](classes/ex_Project.md): A project. · Activity",
        "- [Sub port](classes/ex_SubPort.md): A special port. · Artifact",
    ]
    base = t.split("## Base classes and mixins")[1]
    assert "- [core_WithX](classes/core_WithX.md): A mixin. · mixin" in base
    assert "- [core_Artifact](classes/core_Artifact.md): An artifact. · Artifact, abstract" in base
    beta = files["llms/beta.md"]
    assert "No public product documentation exists for this bounded context." in beta
    assert "- [ex_Bare](classes/ex_Bare.md): Resource · Nexar SupPart" in beta
    assert "Base classes and mixins" not in beta


def test_class_card(files):
    t = files["llms/classes/ex_Port.md"]
    assert t.startswith("# Port\n\n")
    for line in ("- Name: `ex_Port`",
                 "- IRI: `ex:Port` (https://w3id.org/altium/cdm/alpha/Port)",
                 "- Bounded context: [alpha](../alpha.md)",
                 "- Kind: Artifact",
                 "- Is a: [core_Artifact](core_Artifact.md)",
                 "- HTML page: [classes/ex_Port/](../../classes/ex_Port/)",
                 "A connection point. Second sentence | with pipe.",
                 "- A comment.",
                 "- [Port docs](https://example.org/docs/port) (primary)",
                 "- Term: **Port** (exact; altium-365)",
                 "- Platform API type: [`DesX`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesX/)"
                 " (object)",
                 "- close: [prov:Entity](http://www.w3.org/ns/prov#Entity)",
                 "`grid:workspace:{workspace-id}:system-design:port/{id}`",
                 "| Field | Range | Cardinality | Description | Relation | Inherited from |",
                 "| id | string | 0..1 |  |  | [core_Entity](core_Entity.md) |",
                 "| owner | [ex_Project](ex_Project.md) | 1 | The owning project. | core_partOf |  |",
                 "| label | string | 0..1 |  |  |  |",
                 "- [ex_Project](ex_Project.md): `ports`"):
        assert line in t.splitlines(), line
    assert "Maturity" not in t and "Mixins" not in t
    project = files["llms/classes/ex_Project.md"]
    assert "- Maturity: EXPERIMENTAL" in project and "- Mixins: [ex_Named](ex_Named.md)" in project
    assert "| ports | [ex_Port](ex_Port.md) | * |  | core_hasPart |  |" in project
    assert "- [ex_Port](ex_Port.md): `owner`" in project
    sub = files["llms/classes/ex_SubPort.md"]
    assert "| owner | [ex_Project](ex_Project.md) | 1 | The owning project. | core_partOf | [ex_Port](ex_Port.md) |" in sub
    assert "## In the product" not in sub and "## In the API" not in sub
    entity = files["llms/classes/core_Entity.md"]
    assert "- Kind: Entity, abstract" in entity and "- Mixins: [core_WithX](core_WithX.md)" in entity
    bare = files["llms/classes/ex_Bare.md"]
    assert "- Nexar type: `SupPart` ([Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api))" in bare
    assert "TBD" not in bare
    assert "Bounded context" not in files["llms/classes/Any.md"]


def test_pages(files):
    grid = files["llms/pages/grid-format.md"]
    assert "--8<--" not in grid
    assert "| [Port](../classes/ex_Port.md) |" in grid and "[text](#format)" in grid
    dm = files["llms/pages/domain-model.md"]
    assert ("[alpha](../alpha.md), [Port](../classes/ex_Port.md), [home](../../llms.txt), "
            "[IRIs](grid-format.md#iris)") in dm
    assert "[slot](../../slots/core_id/), [hub](../../hub.json), [ext](https://example.org/x), [top](#top)" in dm
    about = files["llms/pages/about.md"]
    assert "[the glossary](glossary.md)" in about and "[`llms.txt`](../../llms.txt)" in about


def test_full(files):
    full = files["llms-full.txt"]
    assert full.startswith(files["llms.txt"])
    assert full.count("\n# File: ") == len(files) - 2
    assert "\n# File: llms/classes/ex_Port.md\n\n# Port\n" in full
    assert "[alpha](llms/alpha.md)" in full and "[ex_Project](llms/classes/ex_Project.md)" in full
    assert "[classes/ex_Port/](classes/ex_Port/)" in full and "[home](llms.txt)" in full


def test_deterministic(env, files):
    assert _build(env) == files


def test_write_files_replaces_stale_output(tmp_path, files):
    (tmp_path / "llms/classes").mkdir(parents=True)
    (tmp_path / "llms/classes/Old.md").write_text("x")
    write_files(tmp_path, files)
    assert not (tmp_path / "llms/classes/Old.md").exists()
    assert (tmp_path / "llms.txt").read_text(encoding="utf-8") == files["llms.txt"]


def test_main(env, tmp_path):
    args = [str(env / "c.yaml"), "--registry", str(env / "registry.yaml"), "--api-dir", str(env / "api")]
    assert main(args + ["--docs-dir", str(env / "docs"), "-o", str(tmp_path / "site")]) == 0
    assert (tmp_path / "site/llms/classes/ex_Port.md").is_file()
    assert main(args + ["--docs-dir", str(tmp_path / "missing"), "-o", str(tmp_path / "s")]) == 2
    assert main([str(env / "c.yaml"), "--registry", str(tmp_path / "none.yaml"), "--api-dir", str(env / "api"),
                 "--docs-dir", str(env / "docs"), "-o", str(tmp_path / "s")]) == 2


def test_real_schema(tmp_path):
    docs = tmp_path / "docs"
    shutil.copytree(REPO / "src/docs/files", docs)
    registry, api = str(REPO / "src/docs/links/registry.yaml"), str(REPO / "src/docs/api")
    sv = SchemaView(ROOT)
    build_reference(sv, registry_path=registry, api_dir=api, findings_path=str(REPO / "MODEL-FINDINGS.md"),
                    out_dir=docs)
    files = build_llms(ROOT, registry_path=registry, api_dir=api, docs_dir=str(docs))
    parsed = llms_txt.parse_llms_file(files["llms.txt"])
    notes = {l["title"]: l["desc"] for l in parsed.sections["Bounded contexts"]}
    assert notes["insights"].endswith("(1 class; 1 base class or mixin)")
    assert _unresolved(files, _html_pages(sv)) == []
    card = files["llms/classes/plt_LifecycleDefinition.md"]
    assert "- Platform API type: [`DesLifeCycleDefinition`](" in card
    assert "| stages | [plt_LifecycleStage](plt_LifecycleStage.md) | * |" in card
