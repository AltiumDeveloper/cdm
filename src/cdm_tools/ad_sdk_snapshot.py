"""
cdm-ad-sdk-snapshot — capture the type names of the Altium Designer SDK (AD SDK) from its published C#
declarations (`<namespace>/api.cs.txt` on the AD SDK reference site), used to check and link `adSDK` annotations.

An `adSDK` annotation names one or more AD SDK types, qualified by namespace and separated by commas, for example
`EDP.INet, PCB.IPCB_Net`. A name resolves to the reference page `<DOCS_BASE>/reference/<namespace>/<Type>/`.

Snapshot format (JSON):
  {"source", "retrieved", "generated_from", "namespaces": {Namespace: [TypeName, ...]}}
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Optional, Union

DOCS_BASE = "https://altiumdeveloper.github.io/ad-sdk-docs"
NAMESPACES = ("SCH", "PCB", "EDP", "DXP", "ComponentLib")
SNAPSHOT_FILE = "ad-sdk-types.json"
DEFAULT_API_DIR = "src/docs/api"
_TYPE_RE = re.compile(r"^    public (?:interface|enum|class|struct) ([A-Za-z_][A-Za-z0-9_]*)", re.M)
_HEADER_RE = re.compile(r"Generated from ([^\n]*?)\.\s*$", re.M)


def declarations_url(namespace: str) -> str:
    return f"{DOCS_BASE}/reference/{namespace.lower()}/api.cs.txt"


def type_url(qualified: str) -> str:
    namespace, _, name = qualified.partition(".")
    return f"{DOCS_BASE}/reference/{namespace.lower()}/{name}/"


def parse_declarations(text: str) -> tuple[list[str], Optional[str]]:
    """Type names declared in one api.cs.txt file, and the assembly versions named in its header."""
    header = _HEADER_RE.search(text.split("\n", 1)[0])
    return sorted(set(_TYPE_RE.findall(text))), (header.group(1) if header else None)


def split_annotation(value: str) -> list[str]:
    return [v.strip() for v in str(value).split(",") if v.strip()]


def load_ad_sdk(api_dir: Union[str, Path]) -> Optional[dict[str, set[str]]]:
    """Namespace -> type names from the snapshot in *api_dir*, or None when there is no snapshot."""
    path = Path(api_dir) / SNAPSHOT_FILE
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return {ns: set(types) for ns, types in data["namespaces"].items()}


def resolves(qualified: str, snapshot: Optional[dict[str, set[str]]]) -> bool:
    namespace, _, name = qualified.partition(".")
    return snapshot is None or name in snapshot.get(namespace, set())


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--api-dir", default=DEFAULT_API_DIR)
    parser.add_argument("--from-dir", help="read <namespace-lower>/api.cs.txt files from this directory instead")
    args = parser.parse_args(argv)
    namespaces: dict[str, list[str]] = {}
    generated_from = None
    for ns in NAMESPACES:
        if args.from_dir:
            text = (Path(args.from_dir) / ns.lower() / "api.cs.txt").read_text()
        else:
            with urllib.request.urlopen(declarations_url(ns), timeout=60) as resp:  # noqa: S310 (fixed host)
                text = resp.read().decode("utf-8")
        namespaces[ns], header = parse_declarations(text)
        generated_from = generated_from or header
    out = {
        "source": f"{DOCS_BASE}/reference/<namespace>/api.cs.txt",
        "retrieved": datetime.date.today().isoformat(),
        "generated_from": generated_from,
        "namespaces": namespaces,
    }
    path = Path(args.api_dir) / SNAPSHOT_FILE
    path.write_text(json.dumps(out, indent=1, sort_keys=False) + "\n")
    print(f"{path}: {sum(len(v) for v in namespaces.values())} types in {len(namespaces)} namespaces", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
