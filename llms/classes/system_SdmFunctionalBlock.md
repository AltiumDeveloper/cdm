# Functional Block (system_SdmFunctionalBlock)

- Name: `system_SdmFunctionalBlock`
- IRI: `sys:SdmFunctionalBlock` (https://w3id.org/altium/cdm/system/SdmFunctionalBlock)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md), [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md)
- HTML page: [classes/system_SdmFunctionalBlock/](../../classes/system_SdmFunctionalBlock/)

Represents a logical block within a system functional model.

## In the API

- Platform API type: [`SysSdmFunctionalBlock`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmFunctionalBlock/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| hardwareComponentIds | [system_SdmHardwareComponent](system_SdmHardwareComponent.md) | * | Hardware components associated with this functional block. |  |  |
| ports | [system_SdmPort](system_SdmPort.md) | * | Ports associated with this functional block. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |
| sdmReferenceDesignator | string | 1 | Reference designator |  | [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md) |

## Referenced by

- [system_SdmEndpoint](system_SdmEndpoint.md): `functionalBlockId`
- [system_SdmFunctionalModel](system_SdmFunctionalModel.md): `functionalBlocks`
- [system_SdmHardwareModel](system_SdmHardwareModel.md): `functionalBlockIds`
