import json
import textwrap
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from cdm_tools.reference import build_reference, main

REPO = Path(__file__).resolve().parents[2]
ROOT = str(REPO / "src/common_data_model/schema/common_data_model.yaml")
DOC = "https://example.org/docs/port"

SCHEMA = textwrap.dedent(f"""
    id: https://example.org/c
    name: c
    prefixes:
      linkml: https://w3id.org/linkml/
      prov: http://www.w3.org/ns/prov#
      ex: https://w3id.org/altium/cdm/alpha/
      oth: https://example.org/other/
    default_prefix: ex
    imports: [linkml:types]
    subsets:
      alpha: {{description: a}}
      beta: {{description: b}}
    classes:
      Any: {{class_uri: linkml:Any}}
      core_Meta: {{abstract: true, in_subset: [alpha], description: meta}}
      core_Entity:
        abstract: true
        in_subset: [alpha]
        description: entity
        instantiates: [core_WithX]
      core_WithX: {{is_a: core_Meta, mixin: true, in_subset: [alpha], description: mixin}}
      core_Artifact: {{abstract: true, is_a: core_Entity, in_subset: [alpha], description: artifact}}
      ex_Port:
        is_a: core_Artifact
        title: Port
        in_subset: [alpha]
        description: A connection point. Second sentence | with pipe.
        see_also: ["{DOC}"]
        structured_aliases:
          - {{literal_form: Port, predicate: EXACT_SYNONYM}}
          - {{literal_form: Terminal, predicate: NARROW_SYNONYM}}
        annotations: {{grid: "grid:workspace:{{workspace-id}}:system-design:port/{{id}}"}}
      dm_Port:
        is_a: core_Artifact
        title: Port
        in_subset: [beta]
        description: Peripheral port
        annotations: {{grid: "grid:global::platform:port/{{id}}"}}
      ex_Bare:
        in_subset: [beta]
        title: Bare part
        description: TBD
        structured_aliases:
          - {{literal_form: part, predicate: RELATED_SYNONYM}}
    slots:
      core_id: {{range: string}}
      core_hasPart:
        abstract: true
        slot_uri: ex:hasPart
        alias: hasPart
        domain: core_Entity
        range: core_Entity
        transitive: true
        inverse: core_partOf
        exact_mappings: [prov:hadMember]
      core_partOf:
        abstract: true
        slot_uri: ex:partOf
        alias: partOf
        domain: core_Entity
        range: core_Entity
      core_revisions:
        is_a: core_hasPart
        slot_uri: ex:revisions
        alias: revisions
        domain: core_Artifact
      core_bare:
        is_a: core_revisions
        slot_uri: ex:bare
        alias: bare
""")

FINDINGS = textwrap.dedent("""
    | ID | Element | Finding | Evidence | Kind | Context | Status |
    |---|---|---|---|---|---|---|
    | MF-001 | `ex_Port` | t | `x` | gap | alpha | Needs SME |
    | MF-002 | `dm_Port` | t | `x` | gap | beta | Fixed — pending review |
""")


@pytest.fixture(scope="module")
def env(tmp_path_factory):
    d = tmp_path_factory.mktemp("ref")
    (d / "c.yaml").write_text(SCHEMA, encoding="utf-8")
    (d / "MF.md").write_text(FINDINGS, encoding="utf-8")
    (d / "registry.yaml").write_text(
        f"{DOC}:\n  title: Port docs\n  source: altium-docs\n  anchors: []\n", encoding="utf-8")
    api = d / "api"
    api.mkdir()
    (api / "platform-schema.json").write_text(json.dumps(
        {"endpoint": "e", "retrieved": "2026-01-02", "query_type": "Query", "mutation_type": None,
         "types": {"Query": {"kind": "OBJECT", "fields": {}}}}), encoding="utf-8")
    return d


def _build(env, out):
    return build_reference(SchemaView(str(env / "c.yaml")), registry_path=str(env / "registry.yaml"),
                           api_dir=str(env / "api"), findings_path=str(env / "MF.md"), out_dir=out)


def test_writes_all_pages(env, tmp_path):
    _build(env, tmp_path)
    got = sorted(str(p.relative_to(tmp_path)) for p in tmp_path.rglob("*.md"))
    assert got == ["coverage.md", "glossary.md", "reference/class-hierarchy.md", "reference/grid-templates.md",
                   "reference/prefixes.md", "reference/relations.md"]


def test_relations(env, tmp_path):
    _build(env, tmp_path)
    t = (tmp_path / "reference/relations.md").read_text()
    assert "| --- |" in t
    assert "core_id" not in t
    rows = {l.split("|")[1].strip(): l for l in t.splitlines() if l.startswith("| [")}
    assert set(rows) == {"[core_hasPart](../slots/core_hasPart.md)", "[core_partOf](../slots/core_partOf.md)",
                         "[core_revisions](../slots/core_revisions.md)", "[core_bare](../slots/core_bare.md)"}
    has = rows["[core_hasPart](../slots/core_hasPart.md)"]
    assert "hasPart" in has and "yes" in has
    assert "[core_partOf](../slots/core_partOf.md)" in has          # declared inverse
    assert "[prov:hadMember](http://www.w3.org/ns/prov#hadMember)" in has
    part = rows["[core_partOf](../slots/core_partOf.md)"]
    assert "[core_hasPart](../slots/core_hasPart.md)" in part       # inverse declared on the other side
    rev = rows["[core_revisions](../slots/core_revisions.md)"]
    assert "[core_Artifact](../classes/core_Artifact.md)" in rev
    assert "[core_hasPart](../slots/core_hasPart.md)" in rev        # is_a
    assert "[core_Artifact](../classes/core_Artifact.md) →" in rev and "(inherited)" in rev   # range inherited
    assert "[core_Entity](../classes/core_Entity.md) *(inherited)*" in rev
    bare = [l for l in t.splitlines() if l.startswith("| [core_bare]")][0]
    assert "[core_Artifact](../classes/core_Artifact.md) *(inherited)* → [core_Entity](../classes/core_Entity.md) *(inherited)*" in bare
    assert "yes *(inherited)*" in bare
    assert "*(inherited)*" not in has


def test_prefixes(env, tmp_path):
    _build(env, tmp_path)
    t = (tmp_path / "reference/prefixes.md").read_text()
    assert "| `ex` | `https://w3id.org/altium/cdm/alpha/` | [alpha](../subsets/alpha.md) |" in t
    assert "| `oth` | `https://example.org/other/` |  |" in t
    assert "| `prov` |" in t


def test_grid_templates(env, tmp_path):
    _build(env, tmp_path)
    t = (tmp_path / "reference/grid-templates.md").read_text()
    assert "## platform" in t and "## system-design" in t
    assert "| [dm_Port](../classes/dm_Port.md) | `grid:global::platform:port/{id}` |" in t
    assert "| `global` | 1 |" in t and "| `workspace` | 1 |" in t


def test_class_hierarchy(env, tmp_path):
    _build(env, tmp_path)
    t = (tmp_path / "reference/class-hierarchy.md").read_text()
    assert t.count("```") == 2
    assert "core_Entity  [instantiates: core_WithX]\n  core_Artifact" in t
    assert "core_Meta\n  core_WithX" in t
    assert "ex_Port" not in t


def test_glossary(env, tmp_path):
    _build(env, tmp_path)
    t = (tmp_path / "glossary.md").read_text()
    assert t.index("## B") < t.index("## P") < t.index("## T")
    # homonym Port: two classes, one entry each (title == alias listed once)
    assert '!!! note "Port — 2 meanings"' in t
    assert "    - [Port](classes/ex_Port.md) — alpha. A connection point." in t
    assert "    - [Port](classes/dm_Port.md) — beta. Peripheral port" in t
    assert "Second sentence" not in t
    # TBD description skipped
    assert "TBD" not in t
    assert "| Terminal | [Port](classes/ex_Port.md) | alpha | narrower | [Port docs](" in t
    assert "| Bare part | [Bare part](classes/ex_Bare.md) | beta | title |  |" in t
    assert "| part | [Bare part](classes/ex_Bare.md) | beta | related |  |" in t
    for line in t.splitlines():
        if line.startswith("|"):
            assert line.replace("\\|", "").count("|") == 6


def test_glossary_escapes_pipes(env, tmp_path):
    schema = SCHEMA.replace("Bare part", "Bare | part")
    p = tmp_path / "s.yaml"
    p.write_text(schema, encoding="utf-8")
    build_reference(SchemaView(str(p)), registry_path=str(env / "registry.yaml"), api_dir=str(env / "api"),
                    findings_path=str(env / "MF.md"), out_dir=tmp_path / "o")
    t = (tmp_path / "o/glossary.md").read_text()
    assert "| Bare \\| part |" in t


def test_coverage(env, tmp_path):
    _build(env, tmp_path)
    t = (tmp_path / "coverage.md").read_text()
    assert "2026-01-02" in t
    assert "| [alpha](subsets/alpha.md) | 1 | 1 (100%) |" in t
    assert "| [beta](subsets/beta.md) | 2 | 0 (0%) |" in t
    assert "| **Total** | 3 | 1 (33%) |" in t
    assert "https://github.com/AltiumDeveloper/cdm/blob/main/MODEL-FINDINGS.md" in t
    assert "https://github.com/AltiumDeveloper/cdm/blob/main/VIOLATIONS.md" in t


def test_deterministic(env, tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    _build(env, a)
    _build(env, b)
    files = sorted(p.relative_to(a) for p in a.rglob("*.md"))
    assert files and all((a / f).read_bytes() == (b / f).read_bytes() for f in files)


def test_real_schema_main(tmp_path):
    rc = main([ROOT, "-o", str(tmp_path), "--registry", str(REPO / "src/docs/links/registry.yaml"),
               "--api-dir", str(REPO / "src/docs/api"), "--findings", str(REPO / "MODEL-FINDINGS.md")])
    assert rc == 0
    assert "Port" in (tmp_path / "glossary.md").read_text()


def test_missing_inputs(tmp_path, capsys):
    base = [ROOT, "-o", str(tmp_path), "--registry", str(REPO / "src/docs/links/registry.yaml"),
            "--api-dir", str(REPO / "src/docs/api"), "--findings", str(REPO / "MODEL-FINDINGS.md")]
    for flag, bad in [("--registry", "nope.yaml"), ("--api-dir", "nope"), ("--findings", "nope.md")]:
        args = list(base)
        args[args.index(flag) + 1] = str(tmp_path / bad)
        assert main(args) == 2
    assert "cdm-gen-reference: link registry not found" in capsys.readouterr().err
    bad = tmp_path / "bad.yaml"
    bad.write_text("- not a mapping\n")
    args = list(base)
    args[args.index("--registry") + 1] = str(bad)
    assert main(args) == 2
    assert "invalid link registry" in capsys.readouterr().err


def test_first_sentence_skips_abbreviations():
    from cdm_tools.reference import _first_sentence
    assert _first_sentence("Shown as a block (e.g. a chip, i.e. a part). Next.") == "Shown as a block (e.g. a chip, i.e. a part)."
    assert _first_sentence("Only one") == "Only one"
    assert _first_sentence("TBD") == ""
