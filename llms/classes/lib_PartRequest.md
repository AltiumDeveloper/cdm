# Part Request (lib_PartRequest)

- Name: `lib_PartRequest`
- IRI: `lib:PartRequest` (https://w3id.org/altium/cdm/library/PartRequest)
- Bounded context: [library](../library.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/lib_PartRequest/](../../classes/lib_PartRequest/)

Part Request represents a formal demand from a designer to introduce a new Component or Part into the managed library, typically triggered when an item is not yet available in the workspace.

## Comments

- Part Request has its own identity and lifecycle, capturing intent, justification, and required attributes, and serving as the entry point for librarian or librarian-like roles to validate, enrich, and release the requested item. It connects design needs with library governance, ensuring that sourcing, compliance, and lifecycle rules are applied consistently before the Part becomes available for use in projects.

## In the product

- [Part Requests](https://www.altium.com/documentation/altium-365/workflow-part-requests) (primary)
- [Process-based Part Requests](https://www.altium.com/documentation/altium-designer/interactive-process-workflows/part-requests)

## GRID

`grid:workspace:{workspace-id}:library:part-request/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
