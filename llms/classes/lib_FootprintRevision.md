# Footprint Revision (lib_FootprintRevision)

- Name: `lib_FootprintRevision`
- IRI: `lib:FootprintRevision` (https://w3id.org/altium/cdm/library/FootprintRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_FootprintRevision/](../../classes/lib_FootprintRevision/)

A revision of a Footprint: the PCB footprint as saved into the Workspace at one point in time, with its own lifecycle state. Editing a Workspace Footprint saves it into the next revision; components that still link to an earlier revision become out of date until they are updated.

## In the product

- [Creating a PCB Footprint](https://www.altium.com/documentation/altium-designer/components-libraries/creating-pcb-footprint) (primary)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## In the API

- Platform API type: [`DesFootprint`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesFootprint/) (object)

## GRID

`grid:workspace:{workspace-id}:library:footprint-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [lib_ComponentRevision](lib_ComponentRevision.md) | footprints | * | core_hasPart |
| [lib_Footprint](lib_Footprint.md) | revisions | * | core_revisions |
