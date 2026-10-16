# Bounded context: Insights

Models insights: findings, detected asynchronously, that give the user insight within one domain area and can be followed up by tasks. There are two concrete kinds. A part insight concerns one Workspace part, may be informed by BOMs or design projects, and occurs in BOM releases, project releases or component revisions. A design insight concerns a design and is part of a design review.

HTML page: [subsets/insights/](../subsets/insights/)

## In the product

No public product documentation exists for this bounded context.

## Classes

- [Design Insight](classes/ins_DesignInsight.md) (`ins_DesignInsight`): An insight within the design domain: a finding, detected asynchronously, about the design under review in a design review. · Activity · API DesWorkspaceInsInsight
- [Part Insight](classes/ins_PartInsight.md) (`ins_PartInsight`): Activity · API DesWorkspaceInsInsight

## Base classes and mixins

- [Insight](classes/ins_Insight.md) (`ins_Insight`): A finding, detected asynchronously, that gives the user insight within one domain area: the library (part insights) or design (design insights). · Activity, abstract
