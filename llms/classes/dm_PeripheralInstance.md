# PeripheralInstance (dm_PeripheralInstance)

- Name: `dm_PeripheralInstance`
- IRI: `dm:PeripheralInstance` (https://w3id.org/altium/cdm/deviceModel/PeripheralInstance)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PeripheralInstance/](../../classes/dm_PeripheralInstance/)

A concrete instance of a peripheral (e.g., SCI0), including available modes.

## In the API

- Platform API type: [`DmPeripheralInstance`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPeripheralInstance/) (object)

## In standards

- close: [CMSIS-SVD peripheral element](https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html#elem_peripheral)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | The name of the peripheral instance. |  |  |
| unit | string | 0..1 | The specific hardware unit index for the peripheral instance. |  |  |
| modes | [dm_PeripheralMode](dm_PeripheralMode.md) | * | The list of modes this peripheral instance can fulfill (e.g., Asynchronous UART). |  |  |
| interfaceType | string | 0..1 | The generic interface this peripheral instance is configured as. |  |  |
| virtualization | [dm_PeripheralVirtualization](../enums/dm_PeripheralVirtualization.md) | 0..1 | Specifies how this peripheral instance is virtualized, indicating whether the instance represents a single, non-virtualized peripheral or a channel-virtualized peripheral where individual functions act as separate interface instances. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_AddressBlock](dm_AddressBlock.md) | peripheralInstance | 0..1 |  |
| [dm_Peripheral](dm_Peripheral.md) | instances | * |  |
| [dm_PortFunction](dm_PortFunction.md) | peripheralInstance | 0..1 |  |
| [system_SdmPort](system_SdmPort.md) | peripheralInstanceId | 0..1 |  |
| [system_SdmSoftwareStackInstance](system_SdmSoftwareStackInstance.md) | peripheralInstanceId | 0..1 |  |
