# Component (lib_Component)

- Name: `lib_Component`
- IRI: `lib:Component` (https://w3id.org/altium/cdm/library/Component)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_Component/](../../classes/lib_Component/)

Component represents a uniquely identifiable electronic part, defined by both its abstract design intent and its concrete realizations in manufacturing and supply.

## Comments

- Component encapsulates schematic symbols, PCB footprints, simulation models, parameters, and lifecycle states, serving as the single source of truth that links design, procurement, and manufacturing. Its identity persists across revisions, even as attributes such as supplier availability, footprint variants, or parameter values evolve, making it a cornerstone of consistency and traceability across Altium Designer, Altium 365, and the broader ECAD–MCAD co-design workflow.

## In the product

- [Building & Maintaining Your Components and Libraries](https://www.altium.com/documentation/altium-designer/components-libraries#WSL) (primary)
- [Workspace Components](https://www.altium.com/documentation/altium-365/workspace-components)
- [Single Component Editing](https://www.altium.com/documentation/altium-designer/components-libraries/single-component-editing)
- Term: **Workspace component** (exact; altium-designer, altium-365)
- Term: **managed component** (exact; altium-365)
- Term: **library component** (exact; altium-365)

## GRID

`grid:workspace:{workspace-id}:library:component/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_ComponentRevision](lib_ComponentRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| parameters | [lib_ComponentParameter](lib_ComponentParameter.md) | * | Component parameters |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
