# PCB Snippet (lib_PcbSnippet)

- Name: `lib_PcbSnippet`
- IRI: `lib:PcbSnippet` (https://w3id.org/altium/cdm/library/PcbSnippet)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_PcbSnippet/](../../classes/lib_PcbSnippet/)

A selection of circuitry from a PCB design, including its components and routing, saved so that it can be placed in other PCB documents. A snippet saved to a Workspace is revised like other Workspace items; snippets can also be kept in local folders.

## In the product

- [Working with Snippets](https://www.altium.com/documentation/altium-designer/schematic/design-reuse/snippets) (primary)

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_PcbSnippetRevision](lib_PcbSnippetRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
