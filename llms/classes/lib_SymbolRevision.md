# Symbol Revision (lib_SymbolRevision)

- Name: `lib_SymbolRevision`
- IRI: `lib:SymbolRevision` (https://w3id.org/altium/cdm/library/SymbolRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_SymbolRevision/](../../classes/lib_SymbolRevision/)

A revision of a Symbol: the schematic symbol as saved into the Workspace at one point in time, with its own lifecycle state. Editing a Workspace Symbol saves it into the next revision; components that still link to an earlier revision become out of date until they are updated.

## In the product

- [Creating a Schematic Symbol](https://www.altium.com/documentation/altium-designer/components-libraries/creating-schematic-symbol) (primary)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## In the API

- Platform API type: [`DesSymbol`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesSymbol/) (object)

## GRID

`grid:workspace:{workspace-id}:library:symbol-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [lib_ComponentRevision](lib_ComponentRevision.md): `symbols`
- [lib_Symbol](lib_Symbol.md): `revisions`
