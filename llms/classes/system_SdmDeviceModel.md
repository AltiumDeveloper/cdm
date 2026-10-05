# Device Model (system_SdmDeviceModel)

- Name: `system_SdmDeviceModel`
- IRI: `sys:SdmDeviceModel` (https://w3id.org/altium/cdm/system/SdmDeviceModel)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md)
- HTML page: [classes/system_SdmDeviceModel/](../../classes/system_SdmDeviceModel/)

Represents a device model within the system design.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#generating_a_board_support_package)

## In the API

- Platform API type: [`SysSdmDeviceModel`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmDeviceModel/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| boardName | string | 0..1 | Board name for the device |  |  |
| mpn | string | 1 | Manufacturer Part Number (MPN) for the device. |  |  |
| peripherals | [dm_Peripheral](dm_Peripheral.md) | * | List of all peripherals available on the device. |  |  |
| ports | [dm_Port](dm_Port.md) | * | List of physical ports on the device. |  |  |

## Referenced by

- [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md): `deviceModels`
