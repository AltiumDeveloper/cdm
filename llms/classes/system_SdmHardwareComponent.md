# Hardware Component (system_SdmHardwareComponent)

- Name: `system_SdmHardwareComponent`
- IRI: `sys:SdmHardwareComponent` (https://w3id.org/altium/cdm/system/SdmHardwareComponent)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md), [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md)
- HTML page: [classes/system_SdmHardwareComponent/](../../classes/system_SdmHardwareComponent/)

Represents a hardware component / part.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#hardware_component) (primary)
- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions#pulling_sdm_into_a_hardware_project)

## In the API

- Platform API type: [`SysSdmHardwareComponent`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmHardwareComponent/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| deviceModelId | [dm_ConfiguredDeviceModel](dm_ConfiguredDeviceModel.md) | 0..1 | A device model associated with this hardware component. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |
| sdmReferenceDesignator | string | 1 | Reference designator |  | [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md) |

## Referenced by

- [system_SdmFunctionalBlock](system_SdmFunctionalBlock.md): `hardwareComponentIds`
- [system_SdmHardwareModel](system_SdmHardwareModel.md): `hardwareComponents`
- [system_SdmPort](system_SdmPort.md): `hardwareComponentId`
