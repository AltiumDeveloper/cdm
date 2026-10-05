# Lifecycle Stage (plt_LifecycleStage)

- Name: `plt_LifecycleStage`
- IRI: `plt:LifecycleStage` (https://w3id.org/altium/cdm/platform/LifecycleStage)
- Bounded context: [platform](../platform.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/plt_LifecycleStage/](../../classes/plt_LifecycleStage/)

A named stage that groups lifecycle states in a lifecycle definition using the Advanced management style (e.g. Design, Prototype, Production), indicating how far a revision has progressed in its development. Stages can be linked to the levels of the revision naming scheme. Definitions using the Simple style have states and transitions but no stages.

## In the product

- [Defining Lifecycle Definitions for a Workspace](https://www.altium.com/documentation/altium-designer/connected-workspace/defining-lifecycle-definitions) (primary)
- [Lifecycle Management](https://www.altium.com/documentation/altium-365/lifecycle-management)

## In the API

- Platform API type: [`DesLifeCycleStage`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesLifeCycleStage/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 |  |  |  |
| states | [plt_LifecycleState](plt_LifecycleState.md) | 1..* |  |  |  |

## Referenced by

- [plt_LifecycleDefinition](plt_LifecycleDefinition.md): `stages`
