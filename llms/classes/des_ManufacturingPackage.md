# Manufacturing Package (des_ManufacturingPackage)

- Name: `des_ManufacturingPackage`
- IRI: `des:ManufacturingPackage` (https://w3id.org/altium/cdm/design/ManufacturingPackage)
- Bounded context: [design](../design.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/des_ManufacturingPackage/](../../classes/des_ManufacturingPackage/)

A read-only package that contains a subset of Project Release artifacts that is typically shared with an external party for the purposes of manufacturing the board (e.g. Manufacturing Package may contain fabrication/assembly files required by the factories, but not the sources of the project)

## In the product

- [Viewing Manufacturing Packages](https://www.altium.com/documentation/altium-365/viewers/manufacturing-package-viewer) (primary)
- [Management of a Specific Project](https://www.altium.com/documentation/altium-365/management-specific-project#SAMPYM)
- Term: **Build Package** (related; altium-365)

## GRID

`grid:workspace:{workspace-id}:design:manufacturing-package/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| projectRelease | [des_ProjectRelease](des_ProjectRelease.md) | 1 | Manufacturing Packages are created based on a specific Project Release. | core_derivedFrom |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
