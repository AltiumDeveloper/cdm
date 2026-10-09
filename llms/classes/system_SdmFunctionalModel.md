# Functional Model (system_SdmFunctionalModel)

- Name: `system_SdmFunctionalModel`
- IRI: `sys:SdmFunctionalModel` (https://w3id.org/altium/cdm/system/SdmFunctionalModel)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md)
- HTML page: [classes/system_SdmFunctionalModel/](../../classes/system_SdmFunctionalModel/)

Captures the functional aspects of the system design, focusing on the behavior and interactions of functional blocks.

## In the API

- Platform API type: [`SysSdmFunctionalModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmFunctionalModel/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| implementedBy | [system_ESDDocument](system_ESDDocument.md) | 0..1 | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| functionalBlocks | [system_SdmFunctionalBlock](system_SdmFunctionalBlock.md) | * | Functional blocks that make up this functional model. |  |  |
| connections | [system_SdmConnection](system_SdmConnection.md) | * | Connections between functional blocks in this functional model. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md) | functionalModel | 0..1 |  |
