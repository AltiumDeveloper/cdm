# Peripheral (dm_Peripheral)

- Name: `dm_Peripheral`
- IRI: `dm:Peripheral` (https://w3id.org/altium/cdm/deviceModel/Peripheral)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_Peripheral/](../../classes/dm_Peripheral/)

A single peripheral definition, including its instances and properties.

## In the API

- Platform API type: [`DmPeripheral`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPeripheral/) (object)

## In standards

- related: [CMSIS-SVD peripheral element](https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html#elem_peripheral)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | The name of the peripheral. |  |  |
| instances | [dm_PeripheralInstance](dm_PeripheralInstance.md) | * | The list of instances of this peripheral present on the device. |  |  |

## Referenced by

- [dm_AddressSegment](dm_AddressSegment.md): `peripherals`
- [dm_ConfiguredDeviceModel](dm_ConfiguredDeviceModel.md): `peripherals`
- [dm_FullStackDeviceModel](dm_FullStackDeviceModel.md): `peripherals`
- [system_SdmDeviceModel](system_SdmDeviceModel.md): `peripherals`
