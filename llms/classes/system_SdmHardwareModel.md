# Hardware Model (system_SdmHardwareModel)

- Name: `system_SdmHardwareModel`
- IRI: `sys:SdmHardwareModel` (https://w3id.org/altium/cdm/system/SdmHardwareModel)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md), [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md)
- HTML page: [classes/system_SdmHardwareModel/](../../classes/system_SdmHardwareModel/)

Captures the hardware components and their interactions within the system design.

## In the API

- Platform API type: [`SysSdmHardwareModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmHardwareModel/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| implementedBy | [des_Project](des_Project.md) | 0..1 | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| hardwareComponents | [system_SdmHardwareComponent](system_SdmHardwareComponent.md) | * | The hardware components that make up this hardware model. |  |  |
| functionalBlockIds | [system_SdmFunctionalBlock](system_SdmFunctionalBlock.md) | * | A functional blocks associated with this hardware model. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |
| sdmReferenceDesignator | string | 1 | Reference designator |  | [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md) |

## Referenced by

- [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md): `hardwareModels`
