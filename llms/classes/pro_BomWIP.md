# BOM WIP (pro_BomWIP)

- Name: `pro_BomWIP`
- IRI: `pro:BomWIP` (https://w3id.org/altium/cdm/procurement/BomWIP)
- Bounded context: [procurement](../procurement.md)
- Kind: Activity, abstract
- Is a: [core_Activity](core_Activity.md)
- Subclasses: [pro_ConsolidatedBOM](pro_ConsolidatedBOM.md), [pro_ManagedBOM](pro_ManagedBOM.md)
- Mixins: [pro_Bom](pro_Bom.md)
- HTML page: [classes/pro_BomWIP/](../../classes/pro_BomWIP/)

The current, editable working state of a Workspace BOM, as opposed to a BOM release, which is a static snapshot of its data. It is the common base of Managed BOM and Consolidated BOM; in the BOM Portal, BOM releases are made from a Managed BOM's working state.

## In the product

- Term: **WIP BOM** (related; altium-365)

## GRID

`grid:workspace:{workspace-id}:procurement:bom/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [pro_BomRelease](pro_BomRelease.md) | * | The release artifacts produced by this activity. | core_releases |  |
| usesParts | [lib_Part](lib_Part.md) | * | Parts used in this Activity | core_hasInput |  |
| usesComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Activity | core_hasInput |  |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| items | [pro_BomItem](pro_BomItem.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ins_PartInsight](ins_PartInsight.md) | informedBy | * | core_informedBy |
