"""
Documentation coverage of the CDM per subset (product links, API types, product terms, standards mappings)
and the model findings recorded in MODEL-FINDINGS.md. Used by the documentation hub pages.
"""

from __future__ import annotations

import dataclasses
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from cdm_tools.api_links import ApiIndex
from cdm_tools.hub import MAPPING_FIELDS

OPEN_STATUS = "Needs SME"
PENDING_STATUS = "Fixed — pending review"
CONTEXT_ALIASES = {"requirement": "requirements"}
NO_SUBSET = "(none)"


@dataclass
class Finding:
    id: str
    element: str
    kind: str
    context: str
    status: str


@dataclass
class SubsetCoverage:
    classes: int = 0
    with_docs: int = 0
    with_api: int = 0
    with_terms: int = 0
    with_mappings: int = 0
    tbd: int = 0
    no_docs_declared: int = 0
    findings_open: int = 0
    findings_pending: int = 0

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


def is_concrete_domain_class(name: str, cls) -> bool:
    """True for a concrete domain class: not abstract, not a mixin, not core_*, not a linkml built-in."""
    if cls.abstract or cls.mixin or name.startswith("core_"):
        return False
    return not (name == "Any" or str(cls.class_uri or "").startswith("linkml:"))


def _cell(text: str) -> str:
    return text.strip().strip("`").strip()


def load_findings(path: Union[str, Path]) -> list[Finding]:
    """Parse the findings table: rows starting with '| MF-'."""
    findings = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("| MF-"):
            continue
        cells = [_cell(c) for c in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        context = CONTEXT_ALIASES.get(cells[5], cells[5])
        findings.append(Finding(id=cells[0], element=cells[1], kind=cells[4], context=context, status=cells[6]))
    return findings


def _has_api(ann, platform_index: Optional[ApiIndex], nexar_types: Optional[dict]) -> bool:
    if "platformAPI" in ann:
        if platform_index is None or platform_index.kind_of(str(ann["platformAPI"].value)) is not None:
            return True
    if "nexarAPI" in ann:
        if nexar_types is None or str(ann["nexarAPI"].value) in nexar_types:
            return True
    return False


def subset_coverage(sv, *, platform_index: Optional[ApiIndex], nexar_types: Optional[dict],
                    findings: list[Finding]) -> dict[str, SubsetCoverage]:
    """Coverage counters per subset; each class counts in its first in_subset. Finding contexts get an entry too."""
    result: dict[str, SubsetCoverage] = {str(n): SubsetCoverage() for n in sv.all_subsets()}
    for name, cls in sv.all_classes().items():
        if not is_concrete_domain_class(name, cls):
            continue
        cov = result.setdefault(str(cls.in_subset[0]) if cls.in_subset else NO_SUBSET, SubsetCoverage())
        ann = cls.annotations or {}
        cov.classes += 1
        cov.with_docs += bool(cls.see_also)
        cov.no_docs_declared += "productDocs" in ann and str(ann["productDocs"].value) == "none"
        cov.with_api += _has_api(ann, platform_index, nexar_types)
        cov.with_terms += bool(cls.structured_aliases)
        cov.with_mappings += any(getattr(cls, attr, None) for _, attr in MAPPING_FIELDS)
        cov.tbd += str(cls.description or "").strip().upper() in ("", "TBD")
    for f in findings:
        cov = result.setdefault(f.context, SubsetCoverage())
        cov.findings_open += f.status.startswith(OPEN_STATUS)
        cov.findings_pending += f.status.startswith(PENDING_STATUS)
    return result


def total_coverage(coverage: dict[str, SubsetCoverage]) -> SubsetCoverage:
    total = SubsetCoverage()
    for cov in coverage.values():
        for f in dataclasses.fields(SubsetCoverage):
            setattr(total, f.name, getattr(total, f.name) + getattr(cov, f.name))
    return total
