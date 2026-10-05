# Managed Sheet (lib_ManagedSheet)

- Name: `lib_ManagedSheet`
- IRI: `lib:ManagedSheet` (https://w3id.org/altium/cdm/library/ManagedSheet)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_ManagedSheet/](../../classes/lib_ManagedSheet/)

A schematic sheet, with its components and wiring, stored in a Workspace so that it can be reused in other designs. A managed sheet may itself contain further managed sheets beneath it in a hierarchy, and the Workspace lets you trace which components it contains and which designs use it.

## Comments

- TBD

## In the product

- [Working with Managed Schematic Sheets](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/workspace-managed-schematic-sheets#just_what_is_a_managed_schematic_sheet) (primary)
- Term: **managed schematic sheet** (exact; altium-designer)

## GRID

`grid:workspace:{workspace-id}:library:managed-sheet/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_ManagedSheetRevision](lib_ManagedSheetRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
