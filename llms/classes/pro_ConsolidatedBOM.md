# Consolidated BOM (pro_ConsolidatedBOM)

- Name: `pro_ConsolidatedBOM`
- IRI: `pro:ConsolidatedBOM` (https://w3id.org/altium/cdm/procurement/ConsolidatedBOM)
- Bounded context: [procurement](../procurement.md)
- Kind: Activity
- Is a: [pro_BomWIP](pro_BomWIP.md)
- HTML page: [classes/pro_ConsolidatedBOM/](../../classes/pro_ConsolidatedBOM/)

Consolidated BOM represents the aggregated bill of materials across one or more Projects or variants, combining all required Parts into a single, unified view for procurement and manufacturing.

## Comments

- Consolidated BOM provides a supply-chain–ready artifact with its own identity and lifecycle, ensuring traceability back to the originating designs while normalizing duplicates, alternates, and quantity rollups. It acts as the bridge between engineering output and enterprise procurement systems, enabling efficient sourcing, cost analysis, and lifecycle validation across multiple boards or product configurations within the Altium 365 ecosystem.

## In the product

- [Consolidated BOM](https://www.altium.com/documentation/altium-365/bom-portal/consolidated-bom) (primary)

## In the API

- Platform API type: [`BomWip`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomWip/) (object)

## GRID

None declared (nearest ancestor `pro_BomWIP`: `grid:workspace:{workspace-id}:procurement:bom/{id}`).

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [pro_BomRelease](pro_BomRelease.md) | * | The release artifacts produced by this activity. | core_releases | [pro_BomWIP](pro_BomWIP.md) |
| usesParts | [lib_Part](lib_Part.md) | * | Parts used in this Activity | core_hasInput | [pro_BomWIP](pro_BomWIP.md) |
| usesComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Activity | core_hasInput | [pro_BomWIP](pro_BomWIP.md) |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| items | [pro_BomItem](pro_BomItem.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
