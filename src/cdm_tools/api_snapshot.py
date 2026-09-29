"""
cdm-api-snapshot — capture compact GraphQL schema snapshots of the Altium 365 Platform API
and the Nexar API, used by lint rule DOC-03 to check platformAPI / nexarAPI annotations.

Snapshot format (JSON):
  {"endpoint", "retrieved", "query_type", "mutation_type",
   "types": {Name: {"kind", "fields"?: {field: "TypeRef"}, "interfaces"?: [...], "possible_types"?: [...]}}}
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable, Optional, Union

DEFAULT_API_DIR = "src/docs/api"
ENDPOINTS = {
    "platform": "https://usw.365.altium.com/api/graphql",
    "nexar": "https://api.nexar.com/graphql",
}
SNAPSHOT_FILES = {"platform": "platform-schema.json", "nexar": "nexar-schema.json"}

INTROSPECTION_QUERY = """
query CdmIntrospection {
  __schema {
    queryType { name }
    mutationType { name }
    types {
      name
      kind
      interfaces { name }
      possibleTypes { name }
      fields(includeDeprecated: true) { name type { ...TypeRef } }
    }
  }
}
fragment TypeRef on __Type {
  kind name
  ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } }
}
"""

PostFn = Callable[[str, dict], dict]


def _post_json(endpoint: str, payload: dict) -> dict:
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "cdm-api-snapshot"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp)


def fetch_introspection(endpoint: str, post: PostFn = _post_json) -> dict:
    try:
        data = post(endpoint, {"query": INTROSPECTION_QUERY})
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"introspection request to {endpoint} failed: {exc}") from exc
    if data.get("errors"):
        raise RuntimeError(f"introspection for {endpoint} returned errors: {data['errors']}")
    schema = (data.get("data") or {}).get("__schema")
    if not schema:
        raise RuntimeError(f"introspection failed for {endpoint}: {data.get('errors')}")
    return schema


def type_ref_str(ref: dict) -> str:
    kind = ref["kind"]
    if kind == "NON_NULL":
        return type_ref_str(ref["ofType"]) + "!"
    if kind == "LIST":
        return "[" + type_ref_str(ref["ofType"]) + "]"
    return ref["name"]


def to_snapshot(schema: dict, endpoint: str, retrieved: str) -> dict:
    types: dict[str, dict] = {}
    for t in schema["types"]:
        name = t["name"]
        if name.startswith("__"):
            continue
        entry: dict = {"kind": t["kind"]}
        if t.get("fields"):
            entry["fields"] = {f["name"]: type_ref_str(f["type"]) for f in t["fields"]}
        if t.get("interfaces"):
            entry["interfaces"] = sorted(i["name"] for i in t["interfaces"])
        if t.get("possibleTypes"):
            entry["possible_types"] = sorted(p["name"] for p in t["possibleTypes"])
        types[name] = entry
    return {
        "endpoint": endpoint,
        "retrieved": retrieved,
        "query_type": (schema.get("queryType") or {}).get("name"),
        "mutation_type": (schema.get("mutationType") or {}).get("name"),
        "types": dict(sorted(types.items())),
    }


def write_snapshot(snapshot: dict, path: Union[str, Path]) -> None:
    Path(path).write_text(json.dumps(snapshot, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def load_snapshot(path: Union[str, Path]) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_snapshots(api_dir: Union[str, Path]) -> dict[str, dict]:
    """Return {"platform": snapshot, "nexar": snapshot} for the files present in *api_dir*."""
    result: dict[str, dict] = {}
    for target, filename in SNAPSHOT_FILES.items():
        p = Path(api_dir) / filename
        if p.is_file():
            result[target] = load_snapshot(p)
    return result


def diff_snapshots(old: dict, new: dict) -> dict[str, list[str]]:
    o, n = old.get("types", {}), new.get("types", {})
    return {
        "added": sorted(set(n) - set(o)),
        "removed": sorted(set(o) - set(n)),
        "kind_changed": sorted(k for k in set(o) & set(n) if o[k]["kind"] != n[k]["kind"]),
    }


def format_diff(label: str, diff: dict[str, list[str]]) -> str:
    lines = [f"[{label}] +{len(diff['added'])} -{len(diff['removed'])} ~{len(diff['kind_changed'])}"]
    lines += [f"  removed: {n}" for n in diff["removed"]]
    lines += [f"  kind changed: {n}" for n in diff["kind_changed"]]
    lines += [f"  added: {n}" for n in diff["added"]]
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="cdm-api-snapshot", description=__doc__)
    parser.add_argument("--out-dir", default=DEFAULT_API_DIR)
    parser.add_argument("--target", choices=[*ENDPOINTS, "all"], default="all")
    args = parser.parse_args(argv)
    targets = list(ENDPOINTS) if args.target == "all" else [args.target]
    Path(args.out_dir).mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    results = []
    try:
        for target in targets:
            new = to_snapshot(fetch_introspection(ENDPOINTS[target]), ENDPOINTS[target], today)
            results.append((target, new))
    except RuntimeError as exc:
        print(f"cdm-api-snapshot: {exc}", file=sys.stderr)
        return 1
    for target, new in results:
        path = Path(args.out_dir) / SNAPSHOT_FILES[target]
        old = load_snapshot(path) if path.is_file() else {"types": {}}
        write_snapshot(new, path)
        print(format_diff(target, diff_snapshots(old, new)))
    return 0
