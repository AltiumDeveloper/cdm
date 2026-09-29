"""
Derive documentation links for GraphQL API types from a checked-in API snapshot
(see cdm_tools.api_snapshot): the type page, query operations that return the type (Read),
mutations whose payload contains it or whose name targets it (Write), and — for types no query
returns — the parent fields that reach it.

Known limitation: reads nested inside non-connection result wrappers (e.g. a ``results`` field of a
``*ResultSet``) are not followed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

DOCS_BASE = "https://altiumdeveloper.github.io/platform-api-docs"
KIND_PATHS = {"OBJECT": "objects", "INTERFACE": "interfaces", "UNION": "unions"}
NAMESPACE_SUFFIX = "Queries"
MAX_NAMESPACE_DEPTH = 2
MAX_REACHED_VIA = 5
_WRAPPER_FIELDS = ("nodes", "edges", "pageInfo")
_WRAPPER_SUFFIXES = ("Payload", NAMESPACE_SUFFIX)
_WORD_RE = re.compile(r"[A-Z][a-z0-9]*")


def base_type(ref: str) -> str:
    return re.sub(r"[\[\]!]", "", ref)


@dataclass(frozen=True)
class Operation:
    path: str            # e.g. "desProjects" or "design.ruleCheck.byId"
    root: str            # top-level Query/Mutation field, used for the docs URL
    kind: str            # "query" | "mutation"
    via: Optional[str] = None   # connection, union or interface the result goes through


@dataclass
class ApiLinks:
    type_name: str
    kind: str
    reads: list[Operation] = field(default_factory=list)
    writes: list[Operation] = field(default_factory=list)
    write_candidates: list[Operation] = field(default_factory=list)
    reached_via: list[str] = field(default_factory=list)
    refetchable: bool = False


class ApiIndex:
    def __init__(self, snapshot: dict, doc_pages: Optional[set[str]] = None) -> None:
        self.types: dict[str, dict] = snapshot["types"]
        self.query_type: str = snapshot.get("query_type") or "Query"
        self.mutation_type: str = snapshot.get("mutation_type") or "Mutation"
        self.doc_pages = doc_pages

    # --- URLs -----------------------------------------------------------------
    def _page(self, path: str) -> Optional[str]:
        if self.doc_pages is not None and path not in self.doc_pages:
            return None
        return f"{DOCS_BASE}/{path}/"

    def type_url(self, name: str) -> Optional[str]:
        kind = self.types.get(name, {}).get("kind")
        return self._page(f"types/{KIND_PATHS[kind]}/{name}") if kind in KIND_PATHS else None

    def operation_url(self, op: Operation) -> Optional[str]:
        return self._page(f"operations/{'queries' if op.kind == 'query' else 'mutations'}/{op.root}")

    # --- Matching -------------------------------------------------------------
    def _resolves(self, name: str, target: str, through_connection: bool = True) -> Optional[str]:
        """'' if *name* is *target*; the wrapper's name if it yields *target*; None otherwise."""
        if name == target:
            return ""
        info = self.types.get(name, {})
        kind = info.get("kind")
        if kind == "UNION" and target in info.get("possible_types", []):
            return name
        if kind == "INTERFACE" and name != "Node" and name in self.types.get(target, {}).get("interfaces", []):
            return name
        if kind == "OBJECT" and through_connection and "nodes" in info.get("fields", {}):
            if self._resolves(base_type(info["fields"]["nodes"]), target, through_connection=False) is not None:
                return name
        return None

    def _reads(self, target: str) -> list[Operation]:
        ops: list[Operation] = []

        def walk(type_name: str, prefix: str, root: Optional[str], depth: int) -> None:
            for fname, ref in sorted(self.types.get(type_name, {}).get("fields", {}).items()):
                if type_name == self.query_type and fname == "node":
                    continue
                bt = base_type(ref)
                via = self._resolves(bt, target)
                if via is not None:
                    ops.append(Operation(path=prefix + fname, root=root or fname, kind="query", via=via or None))
                elif bt.endswith(NAMESPACE_SUFFIX) and depth < MAX_NAMESPACE_DEPTH:
                    walk(bt, f"{prefix}{fname}.", root or fname, depth + 1)

        walk(self.query_type, "", None, 0)
        return sorted(ops, key=lambda o: (".preview." in o.path, o.path))

    def _is_wrapper(self, name: str) -> bool:
        fields = self.types.get(name, {}).get("fields", {})
        return name.endswith(_WRAPPER_SUFFIXES) or any(f in fields for f in _WRAPPER_FIELDS)

    def _is_entity(self, name: str) -> bool:
        info = self.types.get(name, {})
        return info.get("kind") == "OBJECT" and "Node" in info.get("interfaces", [])

    def _writes(self, target: str) -> list[Operation]:
        ops: list[Operation] = []
        for mname, ref in sorted(self.types.get(self.mutation_type, {}).get("fields", {}).items()):
            payload = base_type(ref)
            fields = self.types.get(payload, {}).get("fields", {})
            if self._resolves(payload, target) is not None or any(
                self._resolves(base_type(r), target) is not None for r in fields.values()
            ):
                ops.append(Operation(path=mname, root=mname, kind="mutation"))
        return ops

    def _write_candidates(self, target: str, exclude: set[str]) -> list[Operation]:
        words = _WORD_RE.findall(target)
        if len(words) < 2:
            return []
        prefix, stem = words[0], target[len(words[0]):]
        longer = [n[len(prefix):] for n in self.types
                  if n.startswith(prefix + stem) and len(n) > len(prefix + stem)]
        ops: list[Operation] = []
        mutations = self.types.get(self.mutation_type, {}).get("fields", {})
        for mname in sorted(mutations):
            if mname in exclude or not mname.startswith(prefix.lower()):
                continue
            payload_fields = self.types.get(base_type(mutations[mname]), {}).get("fields", {})
            if any(self._is_entity(base_type(r)) and base_type(r) != target for r in payload_fields.values()):
                continue
            rest = mname[len(prefix):]
            verb = _WORD_RE.match(rest)
            if not verb:
                continue
            remainder = rest[verb.end():]
            if remainder.startswith(prefix):
                remainder = remainder[len(prefix):]
            if not _starts_with_word(remainder, stem):
                continue
            if any(_starts_with_word(remainder, other) for other in longer):
                continue
            ops.append(Operation(path=mname, root=mname, kind="mutation"))
        return ops

    def _reached_via(self, target: str) -> list[str]:
        found: list[tuple[bool, str]] = []
        for tname, info in self.types.items():
            if tname in (self.query_type, self.mutation_type, target) or self._is_wrapper(tname):
                continue
            if info.get("kind") not in ("OBJECT", "INTERFACE"):
                continue
            for fname, ref in info.get("fields", {}).items():
                if self._resolves(base_type(ref), target) is not None:
                    found.append((not self._is_entity(tname), f"{tname}.{fname}"))
        return [path for _, path in sorted(found)][:MAX_REACHED_VIA]

    def links_for(self, type_name: str) -> Optional[ApiLinks]:
        info = self.types.get(type_name)
        if info is None:
            return None
        reads = self._reads(type_name)
        writes = self._writes(type_name)
        return ApiLinks(
            type_name=type_name,
            kind=info["kind"],
            reads=reads,
            writes=writes,
            write_candidates=self._write_candidates(type_name, {o.path for o in writes}),
            reached_via=[] if reads else self._reached_via(type_name),
            refetchable="Node" in info.get("interfaces", []),
        )


def _starts_with_word(text: str, word: str) -> bool:
    return text.startswith(word) and (len(text) == len(word) or text[len(word)].isupper())
