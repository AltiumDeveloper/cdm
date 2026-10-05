# BOM Release (pro_BomRelease)

- Name: `pro_BomRelease`
- IRI: `pro:BomRelease` (https://w3id.org/altium/cdm/procurement/BomRelease)
- Bounded context: [procurement](../procurement.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [pro_Bom](pro_Bom.md), [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/pro_BomRelease/](../../classes/pro_BomRelease/)

A static snapshot of a Managed BOM's data, saved under a release name with an incremented revision number and optional notes. The BOM Portal makes a release automatically when a Managed BOM is first created and again once its data has been mapped, and further releases can be made whenever needed. Each release moves through its own lifecycle states (by default Draft, Approved and Obsolete), and a Workspace can be configured to block releasing while the BOM has Error or Fatal Error issues.

## In the product

- [BOM Portal](https://www.altium.com/documentation/altium-365/bom-portal#release_naming) (primary)

## In the API

- Platform API type: [`BomRelease`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomRelease/) (object)

## GRID

`grid:workspace:{workspace-id}:procurement:bom-release/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| consistsOfParts | [lib_Part](lib_Part.md) | * | Parts used in this Artifact | core_hasPart |  |
| consistsOfComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Artifact | core_hasPart |  |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| items | [pro_BomItem](pro_BomItem.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [ins_PartInsight](ins_PartInsight.md): `occursIn`
- [pro_BomWIP](pro_BomWIP.md): `releases`
