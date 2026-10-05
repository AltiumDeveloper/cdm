# Has Lifecycle (plt_HasLifecycle)

- Name: `plt_HasLifecycle`
- IRI: `plt:HasLifecycle` (https://w3id.org/altium/cdm/platform/HasLifecycle)
- Bounded context: [platform](../platform.md)
- Kind: abstract, mixin
- Is a: [core_Meta](core_Meta.md)
- HTML page: [classes/plt_HasLifecycle/](../../classes/plt_HasLifecycle/)

Mixin that adds a lifecycle state reference to an entity.

## In the product

- [Managing Item Revision Lifecycle](https://www.altium.com/documentation/altium-designer/connected-workspace/items/managing-revision-lifecycle) (primary)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  |  |
