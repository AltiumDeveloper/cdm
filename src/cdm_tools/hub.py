"""
Hub view of a CDM class: the product layer (documentation links, product terms), the API layer
(Platform API type, or Nexar type) and the standards layer (mappings).
Used by the class page template and by the hub.json export.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Union

from cdm_tools.api_links import ApiIndex
from cdm_tools.api_snapshot import load_docs_pages, load_snapshots
from cdm_tools.registry import LinkEntry, split_url

OCTOPART_API_DOC = "https://www.altium.com/documentation/altium-developer-center/octopart/api"
DEFAULT_NAMESPACES = {"prov": "http://www.w3.org/ns/prov#", "obo": "http://purl.obolibrary.org/obo/"}
PREDICATES = {"EXACT_SYNONYM": "exact", "NARROW_SYNONYM": "narrower",
              "BROAD_SYNONYM": "broader", "RELATED_SYNONYM": "related"}
MAPPING_FIELDS = [("exact", "exact_mappings"), ("close", "close_mappings"), ("related", "related_mappings"),
                  ("narrower", "narrow_mappings"), ("broader", "broad_mappings")]


@dataclass
class DocLink:
    text: str
    url: str
    primary: bool


@dataclass
class Term:
    text: str
    predicate: Optional[str]
    contexts: list[str]
    source: Optional[str]


@dataclass
class ApiView:
    type_name: str
    kind: str
    url: Optional[str]


@dataclass
class NexarView:
    type_name: str
    url: str


@dataclass
class Mapping:
    relation: str
    text: str
    url: Optional[str]


@dataclass
class HubView:
    links: list[DocLink] = field(default_factory=list)
    terms: list[Term] = field(default_factory=list)
    product_docs_none: bool = False
    api: Optional[ApiView] = None
    api_missing: Optional[str] = None
    nexar: Optional[NexarView] = None
    nexar_missing: Optional[str] = None
    mappings: list[Mapping] = field(default_factory=list)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


def load_api_layers(api_dir: Union[str, Path]) -> tuple[Optional[ApiIndex], Optional[dict]]:
    """Return (Platform ApiIndex with docs pages, Nexar types) from the snapshots in *api_dir*; None for absent ones."""
    snapshots = load_snapshots(api_dir)
    platform = ApiIndex(snapshots["platform"], load_docs_pages(api_dir)) if "platform" in snapshots else None
    nexar_types = snapshots["nexar"]["types"] if "nexar" in snapshots else None
    return platform, nexar_types


def _doc_link(url: str, registry: dict[str, LinkEntry], primary: bool) -> DocLink:
    entry = registry.get(split_url(url)[0])
    return DocLink(text=entry.display_text if entry else url, url=url, primary=primary)


def _terms(cls) -> list[Term]:
    aliases = cls.structured_aliases or {}
    values = aliases.values() if isinstance(aliases, dict) else aliases
    return [Term(text=str(a.literal_form),
                 predicate=PREDICATES.get(str(a.predicate)) if a.predicate else None,
                 contexts=[str(c) for c in (a.contexts or [])],
                 source=str(a.source) if a.source else None) for a in values]


def _mapping(relation: str, value: str, registry: dict[str, LinkEntry], namespaces: dict[str, str]) -> Mapping:
    if value.startswith(("http://", "https://")):
        entry = registry.get(split_url(value)[0])
        return Mapping(relation=relation, text=entry.display_text if entry else value, url=value)
    prefix, _, local = value.partition(":")
    base = namespaces.get(prefix)
    return Mapping(relation=relation, text=value, url=f"{base}{local}" if base else None)


def schema_namespaces(sv) -> dict[str, str]:
    """Prefix -> IRI map merged over every loaded schema, plus defaults for prov: and obo:."""
    ns: dict[str, str] = {}
    for schema in sv.all_schema(imports=True):
        for prefix in (schema.prefixes or {}).values():
            ns.setdefault(str(prefix.prefix_prefix), str(prefix.prefix_reference))
    for prefix, iri in DEFAULT_NAMESPACES.items():
        ns.setdefault(prefix, iri)
    return ns


def build_hub(cls, *, registry: dict[str, LinkEntry], platform: Optional[ApiIndex],
              nexar_types: Optional[dict], namespaces: dict[str, str]) -> HubView:
    ann = cls.annotations or {}
    hub = HubView(
        links=[_doc_link(str(u), registry, i == 0) for i, u in enumerate(cls.see_also or [])],
        terms=_terms(cls),
        product_docs_none="productDocs" in ann and str(ann["productDocs"].value) == "none",
        mappings=[_mapping(rel, str(v), registry, namespaces)
                  for rel, attr in MAPPING_FIELDS for v in (getattr(cls, attr, None) or [])],
    )
    if "platformAPI" in ann:
        name = str(ann["platformAPI"].value)
        kind = platform.kind_of(name) if platform else None
        if platform is None:
            hub.api = ApiView(type_name=name, kind="", url=None)
        elif kind is None:
            hub.api_missing = name
        else:
            hub.api = ApiView(type_name=name, kind=kind, url=platform.type_url(name))
    if "nexarAPI" in ann:
        name = str(ann["nexarAPI"].value)
        if nexar_types is None or name in nexar_types:
            hub.nexar = NexarView(type_name=name, url=OCTOPART_API_DOC)
        else:
            hub.nexar_missing = name
    return hub
