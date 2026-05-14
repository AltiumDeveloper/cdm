"""
CDM convention rules — single source of truth for both cdm-lint and cdm-wizard.

All naming regexes and required-field sets are derived from AGENTS.md §4.
"""

from __future__ import annotations
import re
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Naming regexes (LINT-03, LINT-04)
# ---------------------------------------------------------------------------

# Class: {subsetName}_{ClassName}
#   subsetName: starts with lowercase letter, followed by alphanumeric (camelCase OK)
#   ClassName:  starts with uppercase letter, followed by alphanumeric (PascalCase)
CLASS_NAME_RE = re.compile(r"^[a-z][a-zA-Z0-9]*_[A-Z][a-zA-Z0-9]*$")

# Class-specific slot (defined under `attributes:` in a class, used by exactly one class):
#   {subsetName}_{ClassName}_{fieldName}
#   ClassName:  starts with uppercase (PascalCase)
#   fieldName:  starts with lowercase (camelCase)
SLOT_NAME_RE = re.compile(r"^[a-z][a-zA-Z0-9]*_[A-Z][a-zA-Z0-9]*_[a-z][a-zA-Z0-9]*$")

# Shared slot (defined in top-level `slots:` section, intended for reuse across classes):
#   {subsetName}_{slotName}
#   slotName may be camelCase or contain underscores (e.g. core_id, pro_bom_items, dm_boardName)
#   Distinguished from class-specific slots by absence of a PascalCase middle component.
SHARED_SLOT_NAME_RE = re.compile(r"^[a-z][a-zA-Z0-9]*_[a-z][a-zA-Z0-9_]*$")

# ---------------------------------------------------------------------------
# CONV-01: slot_uri format for class-specific attributes
# ---------------------------------------------------------------------------

# CONV-01: slot_uri for class-specific attributes must be {prefix}:{ClassName}_{field}
# prefix = lowercase letters only; ClassName = PascalCase; field = lowerCamelCase
SLOT_URI_CLASS_RE = re.compile(r"^[a-z]+:[A-Z][a-zA-Z0-9]*_[a-z][a-zA-Z0-9]*$")

# ---------------------------------------------------------------------------
# CONV-02: alias and title format constraints
# ---------------------------------------------------------------------------

# CONV-02: alias must be lowerCamelCase (starts lowercase, no underscores)
ALIAS_RE = re.compile(r"^[a-z][a-zA-Z0-9]*$")

# CONV-02: title must not contain underscores (must be human-readable spaced string)
TITLE_UNDERSCORE_RE = re.compile(r"_")  # presence = violation

# ---------------------------------------------------------------------------
# GRID annotation regex (LINT-07, D-04)
# ---------------------------------------------------------------------------
# Format: grid:{area}:{tenant-id}:{context}:{resource-type}[/{resource-id}]
# - area:          e.g. workspace, supply, global
# - tenant-id:     may be empty (global resources use "::")
# - context:       e.g. library, design, system-design
# - resource-type: e.g. component, bom
# - resource-id:   optional path; may contain {placeholder} tokens in template annotations
#
# Examples:
#   grid:workspace:{workspace-id}:library:component/{id}
#   grid:supply::platform:part/{id}
#   grid:global::device-model:fullstack-dm/{id}
# ---------------------------------------------------------------------------
# core.yaml naming exception
# ---------------------------------------------------------------------------

# Classes defined in core.yaml use plain PascalCase — NO subset prefix.
# They are the shared abstract foundation (Entity, Artifact, Activity, Resource,
# Event, Meta, and all With* mixins) that every bounded context derives from.
# LINT-03 is intentionally skipped for these classes.
CORE_SCHEMA_BASENAME = "core.yaml"

# ---------------------------------------------------------------------------
# URL convention — IRI local names must be URL-safe (IRI-CONV-01, IRI-CONV-02)
# ---------------------------------------------------------------------------

# Pattern for a valid IRI local name segment: PascalCase, no special chars
# Matches the last path segment of a w3id IRI (e.g. "Comment", "HasAddressRange")
IRI_LOCAL_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")


def is_url_safe_iri_local_name(local_name: str) -> bool:
    """Return True if the IRI local name segment is URL-safe (no encoding needed)."""
    return bool(IRI_LOCAL_NAME_RE.match(local_name))


GRID_RE = re.compile(
    r"^grid:"
    r"[a-z][a-z0-9-]*:"  # area
    r"[^:]*:"  # tenant-id (can be empty)
    r"[a-z][a-z0-9-]*:"  # context
    r"[a-z][a-z0-9-]*"  # resource-type
    r"(?:/[^ \t\n]*)?$"  # optional /resource-id path
)

# ---------------------------------------------------------------------------
# Required metadata fields (LINT-05, LINT-06)
# ---------------------------------------------------------------------------

# Every domain class must have all four (AGENTS.md §4.3)
CLASS_REQUIRED_FIELDS: frozenset[str] = frozenset(
    {
        "class_uri",
        "title",
        "description",
        "in_subset",
    }
)

# Every named domain slot must have all seven (AGENTS.md §4.4)
SLOT_REQUIRED_FIELDS: frozenset[str] = frozenset(
    {
        "slot_uri",
        "alias",
        "title",
        "description",
        "range",
        "multivalued",
        "required",
    }
)

# ---------------------------------------------------------------------------
# Diagnostic type
# ---------------------------------------------------------------------------


@dataclass
class LintIssue:
    """A single lint diagnostic."""

    file: str
    line: int
    severity: str  # "error" or "warning"
    rule_id: str  # e.g. "LINT-03"
    message: str
    element: str = ""  # optional element name for quick lookup (e.g. class/slot name)

    def __str__(self) -> str:
        return (
            f"{self.file}:{self.line}: {self.severity}: [{self.rule_id}] {self.message}"
        )
