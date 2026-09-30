import importlib.util
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

import llms_txt
import llms_txt.core
import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.llms import LINK, build_llms, main, write_files
from cdm_tools.reference import build_reference

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")
REGISTRY = str(REPO / "src/docs/links/registry.yaml")
API = str(REPO / "src/docs/api")
DOC = "https://example.org/docs/port"
LANDING = "https://example.org/docs/alpha"
BASE = "https://example.org/site/"
PORT_GRID = "grid:workspace:{workspace-id}:system-design:port/{id}"

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
      core: {{description: The core.}}
      alpha: {{description: "Models ports, e.g. pins. Second sentence.", see_also: ["{LANDING}"]}}
      beta: {{description: The beta context., annotations: {{productDocs: none}}}}
    enums:
      ex_Kind:
        enum_uri: ex:Kind
        description: Kinds of port.
        permissible_values:
          IN: {{description: Input port., meaning: ex:In}}
          OUT: {{}}
    classes:
      Any: {{class_uri: linkml:Any}}
      core_Meta: {{abstract: true, in_subset: [alpha], description: meta}}
      core_WithX: {{is_a: core_Meta, mixin: true, in_subset: [alpha], description: A mixin.}}
      core_WithY: {{is_a: core_Meta, in_subset: [alpha], description: A core mixin without mixin true.}}
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
          grid: "{PORT_GRID}"
          platformAPI: DesX
        attributes:
          ex_Port_owner:
            is_a: core_partOf
            alias: owner
            range: ex_Project
            required: true
            description: The owning project. More.
          ex_Port_label: {{alias: label, range: string}}
          ex_Port_kind: {{alias: kind, range: ex_Kind}}
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
      ex_Loose: {{mixin: true, description: A mixin without a subset.}}
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

GLOSSARY = textwrap.dedent("""\
    # Glossary

    | Term | Class |
    | --- | --- |
    | Port | [Port](classes/ex_Port.md) |

    !!! note "Port — 2 meanings"

        - [Port](classes/ex_Port.md) — alpha.
        - [Sub port](classes/ex_SubPort.md) — alpha.

    ??? tip

        Collapsed body.

    ```text
    !!! note "inside code"
    ```
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
    "glossary.md": GLOSSARY,
}
SNIPPET = f"### alpha\n\n| [Port](classes/ex_Port.md) | `{PORT_GRID}` |\n"


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
                      docs_dir=str(env / "docs"), repo_url="https://example.org/repo", base_url=BASE)


@pytest.fixture(scope="module")
def files(env):
    return _build(env)


@pytest.fixture(scope="module")
def real_docs(tmp_path_factory):
    """src/docs/files plus the snippets and the glossary that `make gendoc` generates."""
    docs = tmp_path_factory.mktemp("real") / "docs"
    shutil.copytree(REPO / "src/docs/files", docs)
    build_reference(SchemaView(ROOT), registry_path=REGISTRY, api_dir=API,
                    findings_path=str(REPO / "MODEL-FINDINGS.md"), out_dir=docs)
    return docs


def _html_pages(sv) -> set[str]:
    """Site-relative paths of the HTML pages and data files that the generated files may link to."""
    pages = {"", "hub.json", "hub.schema.json"} | {f"{p}/" for p in
                                                   ("about", "grid-format", "domain-model", "entity-classification",
                                                    "relation-types", "glossary", "tags")}
    for folder, names in (("classes", sv.all_classes()), ("subsets", sv.all_subsets()), ("slots", sv.all_slots()),
                          ("enums", sv.all_enums()), ("types", sv.all_types())):
        pages |= {f"{folder}/{n}/" for n in names}
    return pages


def _unresolved(files: dict[str, str], known: set[str], base_url: str) -> list[tuple[str, str]]:
    """Links that resolve neither to a generated file nor to a known page; absolute links under *base_url* are
    checked too, other absolute links are skipped."""
    bad = []
    for path, text in files.items():
        for target in LINK.findall(text):
            link = target.split("#")[0]
            if target.startswith(base_url):
                resolved = link[len(base_url):]
            elif re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            else:
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), link))
                resolved = "" if resolved == "." else resolved + ("/" if link.endswith("/") else "")
            if resolved not in files and resolved not in known:
                bad.append((path, target))
    return bad


def test_llms_txt_parses(files):
    parsed = llms_txt.parse_llms_file(files["llms.txt"])
    assert parsed.title == "Altium Common Data Model (CDM)"
    assert parsed.summary == "The model describes things as a schema. For each class it records what it is."
    assert list(parsed.sections) == ["Start here", "Bounded contexts", "Machine-readable data", "Optional"]
    start = {l["title"]: l["url"] for l in parsed.sections["Start here"]}
    assert start == {t: BASE + f"llms/pages/{p}.md" for t, p in [
        ("About", "about"), ("GRIDs", "grid-format"), ("Domain Model", "domain-model"),
        ("Entity Classification", "entity-classification"), ("Relation Types", "relation-types"),
        ("Glossary", "glossary")]}
    contexts = {l["title"]: l for l in parsed.sections["Bounded contexts"]}
    assert list(contexts) == ["core", "alpha", "beta"]
    assert contexts["alpha"]["url"] == BASE + "llms/alpha.md"
    assert contexts["alpha"]["desc"] == "Models ports, e.g. pins. (3 classes; 8 base classes and mixins)"
    assert contexts["beta"]["desc"] == "The beta context. (1 class)"
    assert contexts["core"]["desc"] == "The core."
    data = [l["url"] for l in parsed.sections["Machine-readable data"]]
    assert data == [BASE + p for p in ("hub.json", "hub.schema.json", "llms-ctx.txt", "llms-full.txt")]
    optional = [l["url"] for l in parsed.sections["Optional"]]
    assert optional[0] == BASE and "https://example.org/repo" in optional
    assert "2026-01-02" in parsed.info
    assert ("The model has 14 classes: 4 concrete domain classes, listed in the catalogues below, and 10 core, "
            "abstract and mixin classes, including LinkML's `Any`. 12 of them belong to one of the 3 bounded "
            f"contexts (LinkML subsets); 2 classes belong to none and are listed in [llms/core.md]({BASE}llms/core.md)."
            ) in parsed.info


def test_every_llms_txt_link_is_absolute(files, monkeypatch):
    fetched = []
    monkeypatch.setattr(llms_txt.core, "get_doc_content", lambda url: fetched.append(url) or "")
    llms_txt.create_ctx(files["llms.txt"], optional=True)
    assert fetched and all(re.match(r"^https?://", u) for u in fetched)
    assert all(re.match(r"^https?://", t) for t in LINK.findall(files["llms.txt"]))


def test_one_card_per_class_and_enum(env, files):
    sv = SchemaView(str(env / "c.yaml"))
    assert {p for p in files if p.startswith("llms/classes/")} == {f"llms/classes/{n}.md" for n in sv.all_classes()}
    assert {p for p in files if p.startswith("llms/enums/")} == {"llms/enums/ex_Kind.md"}
    assert sorted(p for p in files if not p.startswith(("llms/classes/", "llms/enums/"))) == [
        "llms-ctx.txt", "llms-full.txt", "llms.txt", "llms/alpha.md", "llms/beta.md", "llms/core.md",
        "llms/pages/about.md", "llms/pages/domain-model.md", "llms/pages/entity-classification.md",
        "llms/pages/glossary.md", "llms/pages/grid-format.md", "llms/pages/relation-types.md"]


def test_every_link_resolves(env, files):
    assert _unresolved(files, _html_pages(SchemaView(str(env / "c.yaml"))), BASE) == []


def test_catalogue(files):
    t = files["llms/alpha.md"]
    assert t.startswith("# Bounded context: alpha\n\nModels ports, e.g. pins. Second sentence.\n")
    assert "- [Alpha landing](https://example.org/docs/alpha) (primary)" in t
    assert "HTML page: [subsets/alpha/](../subsets/alpha/)" in t
    classes = [l for l in t.split("## Classes")[1].split("##")[0].splitlines() if l.startswith("- ")]
    assert classes == [
        f"- [Port](classes/ex_Port.md) (`ex_Port`): A connection point. · Artifact · API DesX · GRID `{PORT_GRID}`",
        "- [Project](classes/ex_Project.md) (`ex_Project`): A project. · Activity",
        "- [Sub port](classes/ex_SubPort.md) (`ex_SubPort`): A special port. · Artifact",
    ]
    base = t.split("## Base classes and mixins")[1]
    assert "- [core_WithX](classes/core_WithX.md): A mixin. · mixin" in base
    assert "- [core_WithY](classes/core_WithY.md): A core mixin without mixin true. · mixin" in base
    assert "- [core_Artifact](classes/core_Artifact.md): An artifact. · Artifact, abstract" in base
    beta = files["llms/beta.md"]
    assert "No public product documentation exists for this bounded context." in beta
    assert "- [ex_Bare](classes/ex_Bare.md): Resource · Nexar SupPart" in beta
    assert "Base classes and mixins" not in beta and "without a bounded context" not in beta
    core = files["llms/core.md"]
    assert core.split("## Classes without a bounded context\n\n")[1] == (
        "- [Any](classes/Any.md)\n- [ex_Loose](classes/ex_Loose.md): A mixin without a subset. · mixin\n")


def test_class_card(files):
    t = files["llms/classes/ex_Port.md"]
    assert t.startswith("# Port (ex_Port)\n\n")
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
                 f"`{PORT_GRID}`",
                 "| Field | Range | Cardinality | Description | Relation | Inherited from |",
                 "| id | string | 0..1 |  |  | [core_Entity](core_Entity.md) |",
                 "| owner | [ex_Project](ex_Project.md) | 1 | The owning project. | core_partOf |  |",
                 "| label | string | 0..1 |  |  |  |",
                 "| kind | [ex_Kind](../enums/ex_Kind.md) | 0..1 |  |  |  |",
                 "- [ex_Project](ex_Project.md): `ports`"):
        assert line in t.splitlines(), line
    assert "Maturity" not in t and "Mixins" not in t
    project = files["llms/classes/ex_Project.md"]
    assert "- Maturity: EXPERIMENTAL" in project and "- Mixins: [ex_Named](ex_Named.md)" in project
    assert "| ports | [ex_Port](ex_Port.md) | * |  | core_hasPart |  |" in project
    assert "- [ex_Port](ex_Port.md): `owner`" in project
    assert "## GRID\n\nNone declared.\n" in project
    sub = files["llms/classes/ex_SubPort.md"]
    assert "| owner | [ex_Project](ex_Project.md) | 1 | The owning project. | core_partOf | [ex_Port](ex_Port.md) |" in sub
    assert "## In the product" not in sub and "## In the API" not in sub
    assert f"## GRID\n\nNone declared (nearest ancestor `ex_Port`: `{PORT_GRID}`).\n" in sub
    entity = files["llms/classes/core_Entity.md"]
    assert "- Kind: Entity, abstract" in entity and "- Mixins (instantiates): [core_WithX](core_WithX.md)" in entity
    assert "## GRID" not in entity                                    # abstract: no "None declared"
    assert "- Kind: mixin" in files["llms/classes/core_WithY.md"]
    bare = files["llms/classes/ex_Bare.md"]
    assert "- Nexar type: `SupPart` ([Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api))" in bare
    assert "TBD" not in bare and "## GRID" not in bare               # a Resource has no GRID
    assert files["llms/classes/Any.md"].startswith("# Any\n")
    assert "- Bounded context: none" in files["llms/classes/Any.md"]


def test_enum_card(files):
    t = files["llms/enums/ex_Kind.md"]
    assert t.startswith("# ex_Kind\n\n- Name: `ex_Kind`\n- IRI: `ex:Kind` (https://w3id.org/altium/cdm/alpha/Kind)\n")
    for line in ("- HTML page: [enums/ex_Kind/](../../enums/ex_Kind/)", "Kinds of port.",
                 "| Value | Description | Meaning |", "| `IN` | Input port. | ex:In |", "| `OUT` |  |  |",
                 "- [ex_Port](../classes/ex_Port.md): `kind`"):
        assert line in t.splitlines(), line


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


def test_admonitions_become_plain_markdown(files):
    t = files["llms/pages/glossary.md"]
    assert "!!!" not in t.split("```")[0] and "???" not in t
    assert ("**Port — 2 meanings**\n\n- [Port](../classes/ex_Port.md) — alpha.\n"
            "- [Sub port](../classes/ex_SubPort.md) — alpha.\n\n**Tip**\n\nCollapsed body.\n") in t
    assert '```text\n!!! note "inside code"\n```' in t


def test_bundles(files):
    for name in ("llms-ctx.txt", "llms-full.txt"):
        text = files[name]
        assert text.startswith(files["llms.txt"])
        assert not [t for t in LINK.findall(text) if not re.match(r"^(https?:|#)", t)], name
    full, ctx = files["llms-full.txt"], files["llms-ctx.txt"]
    assert full.count("\n# File: ") == len(files) - 3
    assert f"\n# File: llms/classes/ex_Port.md\n\n# Port (ex_Port)\n" in full
    assert f"[alpha]({BASE}llms/alpha.md)" in full and f"[ex_Project]({BASE}llms/classes/ex_Project.md)" in full
    assert f"[classes/ex_Port/]({BASE}classes/ex_Port/)" in full and f"[home]({BASE}llms.txt)" in full
    assert "# File: llms/alpha.md" in ctx and "# File: llms/pages/glossary.md" in ctx
    assert "# File: llms/classes/" not in ctx and "# File: llms/enums/" not in ctx
    assert f"[Port]({BASE}llms/classes/ex_Port.md) (`ex_Port`)" in ctx       # cards linked, not included


def test_deterministic(env, files):
    assert _build(env) == files


def test_deterministic_across_hash_seeds(env, tmp_path):
    outputs = []
    for seed in ("1", "2"):
        out = tmp_path / seed
        subprocess.run([sys.executable, "-m", "cdm_tools.llms", str(env / "c.yaml"), "-o", str(out),
                        "--registry", str(env / "registry.yaml"), "--api-dir", str(env / "api"),
                        "--docs-dir", str(env / "docs"), "--base-url", BASE],
                       check=True, env={**os.environ, "PYTHONHASHSEED": seed})
        outputs.append({str(p.relative_to(out)): p.read_text(encoding="utf-8") for p in out.rglob("*") if p.is_file()})
    assert outputs[0] == outputs[1] and len(outputs[0]) > 10


def test_write_files_replaces_stale_output(tmp_path, files):
    (tmp_path / "llms/classes").mkdir(parents=True)
    (tmp_path / "llms/classes/Old.md").write_text("x")
    write_files(tmp_path, files)
    assert not (tmp_path / "llms/classes/Old.md").exists()
    assert (tmp_path / "llms.txt").read_text(encoding="utf-8") == files["llms.txt"]


def test_main(env, tmp_path):
    args = [str(env / "c.yaml"), "--registry", str(env / "registry.yaml"), "--api-dir", str(env / "api")]
    assert main(args + ["--docs-dir", str(env / "docs"), "-o", str(tmp_path / "site"), "--base-url", BASE]) == 0
    assert (tmp_path / "site/llms/classes/ex_Port.md").is_file()
    assert f"]({BASE}llms/alpha.md)" in (tmp_path / "site/llms.txt").read_text(encoding="utf-8")
    assert main(args + ["--docs-dir", str(tmp_path / "missing"), "-o", str(tmp_path / "s")]) == 2
    assert main([str(env / "c.yaml"), "--registry", str(tmp_path / "none.yaml"), "--api-dir", str(env / "api"),
                 "--docs-dir", str(env / "docs"), "-o", str(tmp_path / "s")]) == 2


def test_real_schema(real_docs):
    sv = SchemaView(ROOT)
    files = build_llms(ROOT, registry_path=REGISTRY, api_dir=API, docs_dir=str(real_docs))
    parsed = llms_txt.parse_llms_file(files["llms.txt"])
    notes = {l["title"]: l["desc"] for l in parsed.sections["Bounded contexts"]}
    assert notes["insights"].endswith("(1 class; 1 base class or mixin)")
    assert _unresolved(files, _html_pages(sv), "https://altiumdeveloper.github.io/cdm/") == []
    card = files["llms/classes/plt_LifecycleDefinition.md"]
    assert card.startswith("# Lifecycle Definition (plt_LifecycleDefinition)\n")
    assert "- Platform API type: [`DesLifeCycleDefinition`](" in card
    assert "| stages | [plt_LifecycleStage](plt_LifecycleStage.md) | * |" in card
    assert "None declared (nearest ancestor `des_Project`: `grid:workspace:{workspace-id}:design:project/{id}`)." \
        in files["llms/classes/des_MultiboardProject.md"]
    no_grid = {p[len("llms/classes/"):-3] for p, t in files.items()
               if p.startswith("llms/classes/") and "\n## GRID\n\nNone declared" in t}
    finding = next(l for l in (REPO / "MODEL-FINDINGS.md").read_text(encoding="utf-8").splitlines()
                   if l.startswith("| MF-078 "))
    assert no_grid == set(re.findall(r"`(\w+)`", finding.split(" | ")[1]))
    used_enums = {r for n in sv.all_classes() for s in sv.class_induced_slots(n)
                  for r in ([str(x) for x in sv.slot_range_as_union(s)] if s.any_of or s.exactly_one_of
                            else [str(s.range)]) if r in sv.all_enums()}
    assert used_enums and all(f"](../enums/{e}.md)" in "".join(files[p] for p in files if p.startswith("llms/classes/"))
                              for e in used_enums)


def test_real_schema_follows_the_naming_rules_stated_in_llms_txt():
    """Class names are `{prefix}_{ClassName}`; the IRI prefix is the name prefix (`sys:` for `system_`); IRIs whose
    local name differs from the name are recorded in VIOLATIONS.md; every slot has an alias (the JSON key); every
    domain class other than a mixin specialises a core base class."""
    sv = SchemaView(ROOT)
    violations = (REPO / "VIOLATIONS.md").read_text(encoding="utf-8")
    bases = {"core_Artifact", "core_Activity", "core_Resource", "core_Event"}
    for name, cls in sv.all_classes().items():
        if name == "Any":
            continue
        prefix, local = name.split("_", 1)
        assert re.fullmatch(r"[a-z]+", prefix) and local[:1].isupper(), name
        curie_prefix, curie_local = sv.get_uri(cls, expand=False).split(":", 1)
        assert curie_prefix == ("sys" if prefix == "system" else prefix), name
        if curie_local != local:
            assert f"`{name}`" in violations, name
        mixin = cls.mixin or "core_Meta" in sv.class_ancestors(name)
        if not name.startswith("core_") and not mixin:
            assert bases & set(sv.class_ancestors(name)), name
        for slot in sv.class_induced_slots(name):
            assert slot.alias, (name, slot.name)


def _load_hook():
    spec = importlib.util.spec_from_file_location("llms_hook", REPO / "src/docs/hooks/llms.py")
    hook = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hook)
    return hook


def _mkdocs_config(docs: Path, site: Path, **extra):
    from mkdocs.config.defaults import MkDocsConfig
    config = MkDocsConfig(config_file_path=str(REPO / "mkdocs.yml"))
    config.load_dict({"site_name": "CDM", "docs_dir": str(docs), "site_dir": str(site),
                      "site_url": "https://example.org/fallback/", **extra})
    errors, _ = config.validate()
    assert not errors
    config.plugins._current_plugin = None      # set by MkDocs while it runs an event; File.generated reads it
    return config


def test_hook(real_docs, tmp_path):
    from mkdocs.structure.files import Files
    hook = _load_hook()
    config = _mkdocs_config(real_docs, tmp_path / "site", extra={"llms_base_url": BASE})
    files = hook.on_files(Files([]), config=config)
    generated = {f.src_uri: f for f in files}
    assert set(generated) == {"llms.txt", "llms-ctx.txt", "llms-full.txt"}
    assert f"]({BASE}llms/core.md)" in generated["llms.txt"].content_string
    hook.on_post_build(config=config)
    assert (tmp_path / "site/llms/classes/plt_LifecycleDefinition.md").is_file()
    assert not (tmp_path / "site/llms.txt").exists()                 # copied by MkDocs, not by the hook

    fallback = _mkdocs_config(real_docs, tmp_path / "site2")          # no llms_base_url, no repo_url
    text = {f.src_uri: f for f in hook.on_files(Files([]), config=fallback)}["llms.txt"].content_string
    assert "](https://example.org/fallback/llms/core.md)" in text and "](https://github.com/AltiumDeveloper/cdm)" in text


def test_hook_reports_missing_inputs(tmp_path):
    from mkdocs.exceptions import PluginError
    from mkdocs.structure.files import Files
    (tmp_path / "docs").mkdir()
    with pytest.raises(PluginError, match=r"cdm-gen-llms: pages not found in .*about\.md"):
        _load_hook().on_files(Files([]), config=_mkdocs_config(tmp_path / "docs", tmp_path / "site"))
