# ConfiguredDeviceModel (dm_ConfiguredDeviceModel)

- Name: `dm_ConfiguredDeviceModel`
- IRI: `dm:ConfiguredDeviceModel` (https://w3id.org/altium/cdm/deviceModel/ConfiguredDeviceModel)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_ConfiguredDeviceModel/](../../classes/dm_ConfiguredDeviceModel/)

A digital twin of an embedded hardware device as configured for a specific use-case. It exposes the device model filtered to specific device configuration.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration) (primary)

## In the API

- Platform API type: [`DmDeviceModelAsConfigured`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmDeviceModelAsConfigured/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| boardName | string | 0..1 | Board name for the device |  |  |
| mpn | string | 1 | Manufacturer Part Number (MPN) for the device. |  |  |
| peripherals | [dm_Peripheral](dm_Peripheral.md) | * | List of all peripherals available on the device. |  |  |
| ports | [dm_Port](dm_Port.md) | * | List of physical ports on the device. |  |  |

## Referenced by

- [system_SdmHardwareComponent](system_SdmHardwareComponent.md): `deviceModelId`
- [system_SdmSoftwareModel](system_SdmSoftwareModel.md): `deviceModelId`
