# Managed Sheet Revision (lib_ManagedSheetRevision)

- Name: `lib_ManagedSheetRevision`
- IRI: `lib:ManagedSheetRevision` (https://w3id.org/altium/cdm/library/ManagedSheetRevision)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/lib_ManagedSheetRevision/](../../classes/lib_ManagedSheetRevision/)

A revision of a Managed Sheet: the schematic sheet as saved into the Workspace at one point in time. A design uses a specific revision, so when the sheet is revised, existing designs can be updated to the new revision or kept on the previous one.

## In the product

- [Working with Managed Schematic Sheets](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/workspace-managed-schematic-sheets#just_what_is_a_managed_schematic_sheet) (primary)
- [Working with Items](https://www.altium.com/documentation/altium-designer/connected-workspace/items)

## GRID

`grid:workspace:{workspace-id}:library:managed-sheet-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| consistsOfComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Artifact | core_hasPart |  |
| template | [con_SchematicTemplateRevision](con_SchematicTemplateRevision.md) | 0..1 |  | core_derivedFrom |  |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [lib_ManagedSheet](lib_ManagedSheet.md) | revisions | * | core_revisions |
