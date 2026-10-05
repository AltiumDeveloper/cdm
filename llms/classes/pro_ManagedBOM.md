# Managed BOM (pro_ManagedBOM)

- Name: `pro_ManagedBOM`
- IRI: `pro:ManagedBOM` (https://w3id.org/altium/cdm/procurement/ManagedBOM)
- Bounded context: [procurement](../procurement.md)
- Kind: Activity
- Is a: [pro_BomWIP](pro_BomWIP.md)
- HTML page: [classes/pro_ManagedBOM/](../../classes/pro_ManagedBOM/)

A bill of materials kept in a Workspace and worked on in the BOM Portal, where its lines are enriched with manufacturer and supplier data for review and procurement. It can be created from a design project (one of its variants or releases) or uploaded as a CSV/XLS file from any source. A Managed BOM made from a project keeps a link to that project, so it can be updated when the project changes, either in place or as a new revision; snapshots of its data at a point in time are kept as BOM releases.

## Comments

- Managed BOM has its own identity and lifecycle, separate from any design project it is created from (though linked to it), and serves as the authoritative reference for procurement, manufacturing, and compliance processes. It supports traceability, repeatability, and governance by recording sourcing decisions and alternates and capturing them in BOM releases, while enabling collaboration between engineering, supply chain, and manufacturing teams within the Altium 365 environment.

## In the product

- [BOM Portal](https://www.altium.com/documentation/altium-365/bom-portal) (primary)
- [Workspace Projects](https://www.altium.com/documentation/altium-365/workspace-projects#uploading_or_creating_a_managed_bom)

## In the API

- Platform API type: [`BomWip`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomWip/) (object)

## GRID

`grid:workspace:{workspace-id}:procurement:bom/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [pro_BomRelease](pro_BomRelease.md) | * | The release artifacts produced by this activity. | core_releases | [pro_BomWIP](pro_BomWIP.md) |
| usesParts | [lib_Part](lib_Part.md) | * | Parts used in this Activity | core_hasInput | [pro_BomWIP](pro_BomWIP.md) |
| usesComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Activity | core_hasInput | [pro_BomWIP](pro_BomWIP.md) |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| items | [pro_BomItem](pro_BomItem.md) | * |  |  | [pro_Bom](pro_Bom.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
