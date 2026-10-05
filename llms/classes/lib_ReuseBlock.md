# Reuse Block (lib_ReuseBlock)

- Name: `lib_ReuseBlock`
- IRI: `lib:ReuseBlock` (https://w3id.org/altium/cdm/library/ReuseBlock)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_ReuseBlock/](../../classes/lib_ReuseBlock/)

A reusable section of a design stored in a Workspace, typically combining schematic circuitry with its PCB representation; a block can also be schematic-only or PCB-only. Placing a reuse block on a schematic sheet brings its PCB content into the board design when changes are transferred through an ECO.

## Comments

- TBD

## In the product

- [Working with Reuse Blocks](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/reuse-blocks) (primary)

## In the API

- Platform API type: [`DesReuseBlock`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesReuseBlock/) (object)

## GRID

`grid:workspace:{workspace-id}:library:reuse-block/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_ReuseBlockRevision](lib_ReuseBlockRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
