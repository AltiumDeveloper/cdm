# Bounded context: Procurement

Models bills of materials: BOMs kept in a Workspace and worked on in the BOM Portal (managed and consolidated BOMs) with their releases, global BOMs, which are not tied to a Workspace, and BOM lines with their alternate and substitute parts and the issues found when a BOM is analysed. It corresponds to the Altium 365 BOM Portal.

HTML page: [subsets/procurement/](../subsets/procurement/)

## In the product

- [BOM Portal](https://www.altium.com/documentation/altium-365/bom-portal) (primary)

## Classes

- [BOM Issue](classes/pro_BomIssue.md) (`pro_BomIssue`): A problem found when a BOM is analysed, usually against a particular BOM line: for example an unknown part number, a duplicated designator, or a part that is deprecated, low in stock or not compliant with a standard such as REACH. · Resource · API BomIssue
- [BOM Item](classes/pro_BomItem.md) (`pro_BomItem`): One line of a BOM: its designators and quantity, the primary manufacturer part used for it (identified by manufacturer and manufacturer part number), and any alternate parts recorded for that line. · Resource · API BomItem
- [BOM Item Alternate](classes/pro_BomItemAlternate.md) (`pro_BomItemAlternate`): An alternate part recorded for one BOM line: another manufacturer part that could be used instead of the line's primary part. · Resource · API BomItemAlternate
- [BOM Item Substitute](classes/pro_BomItemSubstitute.md) (`pro_BomItemSubstitute`): Substitute is a replacement of a part by another within an individual BOM. · Resource · API BomItemSubstitute
- [BOM Release](classes/pro_BomRelease.md) (`pro_BomRelease`): A static snapshot of a Managed BOM's data, saved under a release name with an incremented revision number and optional notes. · Artifact · API BomRelease · GRID `grid:workspace:{workspace-id}:procurement:bom-release/{id}`
- [Consolidated BOM](classes/pro_ConsolidatedBOM.md) (`pro_ConsolidatedBOM`): Consolidated BOM represents the aggregated bill of materials across one or more Projects or variants, combining all required Parts into a single, unified view for procurement and manufacturing. · Activity · API BomWip
- [Global BOM](classes/pro_GlobalBOM.md) (`pro_GlobalBOM`): Global BOM represents a bill of materials that resides outside of any workspace, on Octopart, where users can create, edit, collaborate on and share it with others. · Activity · GRID `grid:global::procurement:bom/{id}`
- [Managed BOM](classes/pro_ManagedBOM.md) (`pro_ManagedBOM`): A bill of materials kept in a Workspace and worked on in the BOM Portal, where its lines are enriched with manufacturer and supplier data for review and procurement. · Activity · API BomWip

## Base classes and mixins

- [BOM](classes/pro_Bom.md) (`pro_Bom`): Bill of Materials · abstract, mixin
- [BOM Item Element](classes/pro_BomItemElement.md) (`pro_BomItemElement`): An element (part) that might be used for a particular BOM item. · Resource, abstract
- [BOM WIP](classes/pro_BomWIP.md) (`pro_BomWIP`): The current, editable working state of a Workspace BOM, as opposed to a BOM release, which is a static snapshot of its data. · Activity, abstract
