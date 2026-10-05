# SCH Snippet Revision (lib_SchSnippetRevision)

- Name: `lib_SchSnippetRevision`
- IRI: `lib:SchSnippetRevision` (https://w3id.org/altium/cdm/library/SchSnippetRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_SchSnippetRevision/](../../classes/lib_SchSnippetRevision/)

A revision of a schematic snippet as saved into the Workspace at one point in time. Editing a Workspace snippet saves it into the next revision.

## In the product

- [Working with Snippets](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/snippets) (primary)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [lib_ReuseBlockRevision](lib_ReuseBlockRevision.md): `schSnippet`
- [lib_SchSnippet](lib_SchSnippet.md): `revisions`
