# Reuse Block Revision (lib_ReuseBlockRevision)

- Name: `lib_ReuseBlockRevision`
- IRI: `lib:ReuseBlockRevision` (https://w3id.org/altium/cdm/library/ReuseBlockRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_ReuseBlockRevision/](../../classes/lib_ReuseBlockRevision/)

A revision of a Reuse Block: its schematic and/or PCB content as saved into the Workspace at one point in time, with its own lifecycle state. Editing a reuse block saves it into the next revision.

## In the product

- [Working with Reuse Blocks](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/reuse-blocks) (primary)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## In the API

- Platform API type: [`DesReuseBlockRevision`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesReuseBlockRevision/) (object)

## GRID

`grid:workspace:{workspace-id}:library:reuse-block-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| consistsOfComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Artifact | core_hasPart |  |
| schSnippet | [lib_SchSnippetRevision](lib_SchSnippetRevision.md) | 0..1 |  | core_hasPart |  |
| pcbSnippet | [lib_PcbSnippetRevision](lib_PcbSnippetRevision.md) | 0..1 |  | core_hasPart |  |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [lib_ReuseBlock](lib_ReuseBlock.md): `revisions`
