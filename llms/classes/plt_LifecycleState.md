# Lifecycle State (plt_LifecycleState)

- Name: `plt_LifecycleState`
- IRI: `plt:LifecycleState` (https://w3id.org/altium/cdm/platform/LifecycleState)
- Bounded context: [platform](../platform.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/plt_LifecycleState/](../../classes/plt_LifecycleState/)

A named point in an Item Revision's lifecycle (e.g. Planned, New From Design, In Production, Obsolete) that shows its status from a business perspective. Each state's properties include whether revisions in that state are shown in the Explorer panel and whether they may be used in designs; a revision moves to another state only through a transition defined in its lifecycle definition.

## In the product

- [Defining Lifecycle Definitions for a Workspace](https://www.altium.com/documentation/altium-designer/connected-workspace/defining-lifecycle-definitions#options_and_controls_of_the_state_properties_dialog) (primary)
- [Managing Item Revision Lifecycle](https://www.altium.com/documentation/altium-designer/connected-workspace/items/managing-revision-lifecycle)
- [Lifecycle Management](https://www.altium.com/documentation/altium-365/lifecycle-management)

## In the API

- Platform API type: [`DesLifeCycleState`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesLifeCycleState/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 |  |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [plt_HasLifecycle](plt_HasLifecycle.md) | lifecycleState | 1 |  |
| [plt_LifecycleStage](plt_LifecycleStage.md) | states | 1..* |  |
