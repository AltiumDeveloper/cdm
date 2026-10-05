# Revision Naming Scheme (plt_NamingScheme)

- Name: `plt_NamingScheme`
- IRI: `plt:NamingScheme` (https://w3id.org/altium/cdm/platform/NamingScheme)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_NamingScheme/](../../classes/plt_NamingScheme/)

Defines the format of Revision IDs for the Items that use it: one to three levels (e.g. Model, Prototype and Revision), each with its own format, separator and minimum width. The scheme is chosen per Item when the Item is created and cannot be changed after its first release. It is distinct from the Item Naming Scheme, which determines the Item ID rather than the revision's ID.

## In the product

- [Defining Revision Naming Schemes for a Workspace](https://www.altium.com/documentation/altium-designer/connected-workspace/defining-naming-schemes) (primary)

## In the API

- Platform API type: [`DesRevisionNamingScheme`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesRevisionNamingScheme/) (object)

## GRID

`grid:workspace:{workspace-id}:platform:revision-naming-scheme/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
