# Footprint (lib_Footprint)

- Name: `lib_Footprint`
- IRI: `lib:Footprint` (https://w3id.org/altium/cdm/library/Footprint)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_Footprint/](../../classes/lib_Footprint/)

Footprint represents the physical layout definition of a Component on a PCB, specifying pad geometry, land patterns, and mechanical clearances required for assembly and manufacturing.

## Comments

- Each Footprint has its own identity and lifecycle, and is associated with one or more Components.
- It binds the abstract logical design to its physical implementation, ensuring accurate placement, routing, and compatibility with fabrication and MCAD workflows within Altium Designer and Altium 365.

## In the product

- [Creating a PCB Footprint](https://www.altium.com/documentation/altium-designer/components-libraries/creating-pcb-footprint) (primary)
- Term: **Workspace Footprint** (exact; altium-designer)
- Term: **PCB footprint** (related; altium-designer)

## GRID

`grid:workspace:{workspace-id}:library:footprint/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_FootprintRevision](lib_FootprintRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
