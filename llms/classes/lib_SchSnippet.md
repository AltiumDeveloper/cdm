# SCH Snippet (lib_SchSnippet)

- Name: `lib_SchSnippet`
- IRI: `lib:SchSnippet` (https://w3id.org/altium/cdm/library/SchSnippet)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_SchSnippet/](../../classes/lib_SchSnippet/)

A selection of circuitry from a single schematic sheet, including its components, saved so that it can be placed in other designs. A snippet saved to a Workspace is revised like other Workspace items; snippets can also be kept in local folders.

## In the product

- [Working with Snippets](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/snippets) (primary)
- Term: **schematic snippet** (exact; altium-designer)

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_SchSnippetRevision](lib_SchSnippetRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
