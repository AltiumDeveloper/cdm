# Lifecycle Definition (plt_LifecycleDefinition)

- Name: `plt_LifecycleDefinition`
- IRI: `plt:LifecycleDefinition` (https://w3id.org/altium/cdm/platform/LifecycleDefinition)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_LifecycleDefinition/](../../classes/plt_LifecycleDefinition/)

Defines the set of states that an entity can transition through in its lifecycle. This definition clarifies what stage a revision of an entity has reached in its 'life' and what it can be safely used for. Different entities can have different lifecycle definitions assigned to them.

## In the product

- [Defining Lifecycle Definitions for a Workspace](https://www.altium.com/documentation/altium-designer/connected-workspace/defining-lifecycle-definitions) (primary)
- [Lifecycle Management](https://www.altium.com/documentation/altium-365/lifecycle-management)

## In the API

- Platform API type: [`DesLifeCycleDefinition`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesLifeCycleDefinition/) (object)

## GRID

`grid:workspace:{workspace-id}:platform:lifecycle-definition/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| stages | [plt_LifecycleStage](plt_LifecycleStage.md) | * |  |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
