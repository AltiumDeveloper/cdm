"""
Bounded contexts (LinkML subsets) as the site shows them: their order and their titles.

The order is the one the Altium 365 API reference uses for the same contexts; the site navigation (mkdocs.yml), the
home-page cards and the GRIDs page follow it. Subsets not listed here come after the listed ones, by name.
"""

from __future__ import annotations

BC_ORDER = [
    "platform", "design", "insights", "library", "collaboration", "configuration", "procurement", "supply",
    "customization", "system", "system-sdm", "requirements", "deviceModel", "software", "ota", "core",
]


def subset_sort_key(name: str) -> tuple[int, str]:
    """Sort key putting subsets in BC_ORDER, then the others by name."""
    return (BC_ORDER.index(name) if name in BC_ORDER else len(BC_ORDER), name.casefold())


def subset_title(sv, name: str) -> str:
    """The subset's `title`, or its name when it has none (or is not a subset)."""
    subset = sv.all_subsets().get(name)
    return str(subset.title) if subset is not None and subset.title else name


# The Altium 365 API reference groups its operations and types by the same bounded contexts. Subset -> (API context
# slug, title), mirroring the `cdm:` lists of AltiumDeveloper/platform-api-docs config/context-map.yaml; several subsets
# can share one API context. core has none (the API's Common context holds shared scalars and paging, not CDM classes).
API_REFERENCE = "https://altiumdeveloper.github.io/platform-api-docs/reference"
API_CONTEXTS = {
    "platform": ("platform", "Platform"),
    "design": ("design", "Design"),
    "insights": ("insights", "Insights"),
    "library": ("library-management", "Library Management"),
    "collaboration": ("collaboration", "Collaboration"),
    "configuration": ("configuration-management", "Configuration Management"),
    "procurement": ("procurement", "Procurement"),
    "supply": ("supply", "Supply"),
    "customization": ("customization", "Customization"),
    "system": ("system-design", "System Design"),
    "system-sdm": ("system-design", "System Design"),
    "requirements": ("requirements", "Requirements"),
    "deviceModel": ("renesas-preview", "Renesas (preview)"),
    "software": ("renesas-preview", "Renesas (preview)"),
    "ota": ("renesas-preview", "Renesas (preview)"),
}


def api_context(name: str):
    """(title, overview URL) of the API reference's bounded context for a subset, or None."""
    entry = API_CONTEXTS.get(name)
    return (entry[1], f"{API_REFERENCE}/{entry[0]}/overview") if entry else None
