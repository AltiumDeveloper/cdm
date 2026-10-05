# Symbol (lib_Symbol)

- Name: `lib_Symbol`
- IRI: `lib:Symbol` (https://w3id.org/altium/cdm/library/Symbol)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_Symbol/](../../classes/lib_Symbol/)

Symbol represents the logical schematic view of a Component, defining its electrical interface, pins, and attributes used to express circuit intent in design schematics.

## Comments

- Each Symbol has its own identity and structure, and may be reused across multiple Components or designs.
- It provides the abstract representation of a Component within the schematic domain, ensuring clarity, consistency, and accurate electrical connectivity throughout the design process.

## In the product

- [Creating a Schematic Symbol](https://www.altium.com/documentation/altium-designer/components-libraries/creating-schematic-symbol) (primary)
- Term: **Workspace Symbol** (exact; altium-designer)
- Term: **schematic symbol** (related; altium-designer)

## GRID

`grid:workspace:{workspace-id}:library:symbol/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_SymbolRevision](lib_SymbolRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
