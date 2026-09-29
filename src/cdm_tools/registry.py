"""
Link registry — the single source of titles and verification state for every external
documentation URL referenced by the CDM (see AGENTS.md §8).

Keys are URLs without a fragment. Fragments used by classes must be listed in `anchors`.
`title` must equal the page <title> text before " | " (checked by cdm-verify-links).
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Union

import yaml

DEFAULT_REGISTRY_PATH = "src/docs/links/registry.yaml"
SOURCES = frozenset({"altium-docs", "altium-dev-center", "renesas", "nexar", "standard"})

_HEADER = (
    "# CDM documentation link registry (see AGENTS.md §8)\n"
    "# Keyed by URL without fragment. `title` = page <title> text before ' | '.\n"
    "# `anchors` lists every #fragment used by the schema. Verify with: make verify-links\n"
)


class RegistryError(ValueError):
    """Raised when the registry file is malformed."""


@dataclass
class LinkEntry:
    url: str
    title: str
    source: str
    product: Optional[str] = None
    label: Optional[str] = None
    anchors: list[str] = field(default_factory=list)
    last_verified: Optional[str] = None

    @property
    def display_text(self) -> str:
        return self.label or self.title


def split_url(url: str) -> tuple[str, Optional[str]]:
    """Split 'https://x/p#frag' into ('https://x/p', 'frag')."""
    base, sep, frag = url.partition("#")
    return base, (frag if sep else None)


def load_registry(path: Union[str, Path]) -> dict[str, LinkEntry]:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise RegistryError(f"{path}: top level must be a mapping of URL -> entry")
    entries: dict[str, LinkEntry] = {}
    for url, data in raw.items():
        url = str(url)
        if "#" in url:
            raise RegistryError(f"{url}: registry keys must not contain a fragment")
        if not isinstance(data, dict) or not data.get("title"):
            raise RegistryError(f"{url}: entry must be a mapping with a 'title'")
        source = data.get("source")
        if not isinstance(source, str) or source not in SOURCES:
            raise RegistryError(f"{url}: 'source' must be one of {sorted(SOURCES)}, got {source!r}")
        anchors = data.get("anchors")
        if anchors is not None and not isinstance(anchors, list):
            raise RegistryError(f"{url}: 'anchors' must be a list")
        last = data.get("last_verified")
        if isinstance(last, datetime.date):
            last = last.isoformat()
        entries[url] = LinkEntry(
            url=url,
            title=str(data["title"]),
            source=source,
            product=data.get("product"),
            label=data.get("label"),
            anchors=[str(a) for a in (anchors or [])],
            last_verified=str(last) if last else None,
        )
    return entries


def lookup(registry: dict[str, LinkEntry], url: str) -> Optional[LinkEntry]:
    """Return the entry for *url*; None if unknown or its fragment is not a listed anchor."""
    base, frag = split_url(url)
    entry = registry.get(base)
    if entry is None or (frag is not None and frag not in entry.anchors):
        return None
    return entry


def dump_registry(registry: dict[str, LinkEntry], path: Union[str, Path]) -> None:
    data: dict[str, dict] = {}
    for url in sorted(registry):
        e = registry[url]
        d: dict = {"title": e.title}
        if e.label:
            d["label"] = e.label
        d["source"] = e.source
        if e.product:
            d["product"] = e.product
        d["anchors"] = list(e.anchors)
        if e.last_verified:
            d["last_verified"] = e.last_verified
        data[url] = d
    body = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120)
    Path(path).write_text(_HEADER + body, encoding="utf-8")
