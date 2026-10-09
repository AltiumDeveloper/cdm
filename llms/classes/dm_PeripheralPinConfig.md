# PeripheralPinConfig (dm_PeripheralPinConfig)

- Name: `dm_PeripheralPinConfig`
- IRI: `dm:PeripheralPinConfig` (https://w3id.org/altium/cdm/deviceModel/PeripheralPinConfig)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PeripheralPinConfig/](../../classes/dm_PeripheralPinConfig/)

A specific pin multiplexing configuration within peripheral configuration.

## In the API

- Platform API type `DmPeripheralPinConfig` is named by the class but is not in the API snapshot.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| pinName | string | 0..1 | The fully qualified identifier representing the channel, and pin function (e.g., sci0.txt, iic1.scl). |  |  |
| pinValue | string | 0..1 | The fully qualified identifier representing the channel, pin function, and physical pin (e.g., sci0.txd.p101, iic1.scl.p402). |  |  |
| function | string | 0..1 | The logical pin function name (e.g., TXD, RXD). |  |  |
| port | string | 0..1 | The physical port target for the pin function. |  |  |
| portName | string | 0..1 | The physical port mapping target for the pin function. |  |  |
| channel | string | 0..1 | Identifies the specific virtualized channel used by this pin configuration. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_PeripheralConfiguration](dm_PeripheralConfiguration.md) | pinConfigs | * |  |
