import json

from cdm_tools.api_snapshot import (
    diff_snapshots,
    fetch_introspection,
    format_diff,
    load_snapshots,
    to_snapshot,
    type_ref_str,
    write_snapshot,
)


def _ref(kind, name=None, of=None):
    return {"kind": kind, "name": name, "ofType": of}


INTROSPECTION = {
    "queryType": {"name": "Query"},
    "mutationType": {"name": "Mutation"},
    "types": [
        {"name": "__Schema", "kind": "OBJECT", "fields": [], "interfaces": [], "possibleTypes": None},
        {
            "name": "Query",
            "kind": "OBJECT",
            "fields": [
                {"name": "desProjectById", "type": _ref("OBJECT", "DesProject")},
                {"name": "desProjects", "type": _ref("NON_NULL", of=_ref("LIST", of=_ref("NON_NULL", of=_ref("OBJECT", "DesProject"))))},
            ],
            "interfaces": [],
            "possibleTypes": None,
        },
        {"name": "DesProject", "kind": "OBJECT", "fields": [{"name": "id", "type": _ref("NON_NULL", of=_ref("SCALAR", "ID"))}], "interfaces": [{"name": "Node"}], "possibleTypes": None},
        {"name": "Node", "kind": "INTERFACE", "fields": [{"name": "id", "type": _ref("SCALAR", "ID")}], "interfaces": [], "possibleTypes": [{"name": "DesProject"}]},
        {"name": "DesProjectType", "kind": "ENUM", "fields": None, "interfaces": None, "possibleTypes": None},
    ],
}


def test_type_ref_str():
    assert type_ref_str(_ref("NON_NULL", of=_ref("LIST", of=_ref("OBJECT", "X")))) == "[X]!"


def test_to_snapshot_shape():
    snap = to_snapshot(INTROSPECTION, "https://api.example/graphql", "2026-09-29")
    assert snap["endpoint"] == "https://api.example/graphql"
    assert snap["retrieved"] == "2026-09-29"
    assert snap["query_type"] == "Query"
    assert "__Schema" not in snap["types"]
    assert snap["types"]["Query"]["fields"]["desProjects"] == "[DesProject!]!"
    assert snap["types"]["DesProject"]["interfaces"] == ["Node"]
    assert snap["types"]["Node"]["possible_types"] == ["DesProject"]
    assert snap["types"]["DesProjectType"] == {"kind": "ENUM"}


def test_fetch_introspection_uses_injected_post():
    calls = []

    def fake_post(endpoint, payload):
        calls.append((endpoint, payload))
        return {"data": {"__schema": INTROSPECTION}}

    assert fetch_introspection("https://api.example/graphql", post=fake_post) == INTROSPECTION
    assert "__schema" in calls[0][1]["query"]


def test_diff_and_format():
    old = {"types": {"A": {"kind": "OBJECT"}, "B": {"kind": "OBJECT"}}}
    new = {"types": {"A": {"kind": "INTERFACE"}, "C": {"kind": "OBJECT"}}}
    d = diff_snapshots(old, new)
    assert d == {"added": ["C"], "removed": ["B"], "kind_changed": ["A"]}
    text = format_diff("platform", d)
    assert "removed: B" in text and "added: C" in text and "kind changed: A" in text


def test_write_and_load_snapshots(tmp_path):
    snap = to_snapshot(INTROSPECTION, "https://api.example/graphql", "2026-09-29")
    write_snapshot(snap, tmp_path / "platform-schema.json")
    loaded = load_snapshots(tmp_path)
    assert set(loaded) == {"platform"}
    assert loaded["platform"] == json.loads((tmp_path / "platform-schema.json").read_text())
