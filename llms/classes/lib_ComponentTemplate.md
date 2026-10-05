# Component Template (lib_ComponentTemplate)

- Name: `lib_ComponentTemplate`
- IRI: `lib:ComponentTemplate` (https://w3id.org/altium/cdm/library/ComponentTemplate)
- Bounded context: [library](../library.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/lib_ComponentTemplate/](../../classes/lib_ComponentTemplate/)

Component Template defines a reusable blueprint for creating and managing electronic components with consistent parameters, metadata, and lifecycle policies.

## Comments

- Component Template establishes the structural and semantic boundaries for Components of a given class (e.g., resistors, ICs, connectors), ensuring uniformity in attributes such as electrical ratings, supplier links, simulation models, or documentation references. Its identity is independent of any individual Component but directly governs how Components are instantiated and validated, making it a key mechanism for enforcing standards, reducing errors, and enabling scalable library management across teams and projects.

## In the product

- [Component Templates](https://www.altium.com/documentation/altium-designer/components-libraries/workspace-component-templates) (primary)

## In the API

- Platform API type: [`DesComponentTemplate`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesComponentTemplate/) (object)

## GRID

`grid:workspace:{workspace-id}:library:component-template/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [lib_ComponentTemplateRevision](lib_ComponentTemplateRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
