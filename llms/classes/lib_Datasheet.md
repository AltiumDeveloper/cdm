# Datasheet (lib_Datasheet)

- Name: `lib_Datasheet`
- IRI: `lib:Datasheet` (https://w3id.org/altium/cdm/library/Datasheet)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_Datasheet/](../../classes/lib_Datasheet/)

Datasheet represents a technical document associated with a Component or Part, providing authoritative specifications, electrical characteristics, and manufacturer information.

## Comments

- Each Datasheet has its own identity and version reference, ensuring consistent access to verified technical details.
- It supports informed design decisions, validation, and compliance by linking engineering data with official manufacturer documentation across Components and managed libraries within Altium 365.

## In the product

- [Adding Datasheets to a Component](https://www.altium.com/documentation/altium-designer/components-libraries/adding-datasheets-component) (primary)

## In the API

- Platform API type: [`DesDatasheet`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesDatasheet/) (object)

## GRID

`grid:workspace:{workspace-id}:library:datasheet/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
