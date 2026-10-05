# PeripheralMode (dm_PeripheralMode)

- Name: `dm_PeripheralMode`
- IRI: `dm:PeripheralMode` (https://w3id.org/altium/cdm/deviceModel/PeripheralMode)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PeripheralMode/](../../classes/dm_PeripheralMode/)

A specific mode that a peripheral instance can fulfill,

## In the API

- Platform API type: [`DmPeripheralMode`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPeripheralMode/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | Name of the peripheral mode (e.g., Asynchronous UART). |  |  |
| configurations | [dm_PeripheralConfiguration](dm_PeripheralConfiguration.md) | * | The configurations available within this peripheral modes. |  |  |

## Referenced by

- [dm_PeripheralInstance](dm_PeripheralInstance.md): `modes`
