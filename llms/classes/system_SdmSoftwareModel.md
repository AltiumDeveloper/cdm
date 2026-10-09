# Software Model (system_SdmSoftwareModel)

- Name: `system_SdmSoftwareModel`
- IRI: `sys:SdmSoftwareModel` (https://w3id.org/altium/cdm/system/SdmSoftwareModel)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md), [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md)
- HTML page: [classes/system_SdmSoftwareModel/](../../classes/system_SdmSoftwareModel/)

Captures the software components and their interactions within the system design.

## In the API

- Platform API type: [`SysSdmSoftwareModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmSoftwareModel/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| implementedBy | [sft_SoftwareProject](sft_SoftwareProject.md) | 0..1 | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| softwareComponents | [system_SdmSoftwareComponent](system_SdmSoftwareComponent.md) | * | The software components that make up this software model. |  |  |
| softwareStackInstances | [system_SdmSoftwareStackInstance](system_SdmSoftwareStackInstance.md) | * | The stack instances used by this software model. |  |  |
| deviceModelId | [dm_ConfiguredDeviceModel](dm_ConfiguredDeviceModel.md) | 0..1 | A device model associated with this software model. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |
| sdmReferenceDesignator | string | 1 | Reference designator |  | [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md) | softwareModels | * |  |
