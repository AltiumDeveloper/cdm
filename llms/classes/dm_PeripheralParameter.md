# PeripheralParameter (dm_PeripheralParameter)

- Name: `dm_PeripheralParameter`
- IRI: `dm:PeripheralParameter` (https://w3id.org/altium/cdm/deviceModel/PeripheralParameter)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PeripheralParameter/](../../classes/dm_PeripheralParameter/)

A parameter associated with peripheral instance configuration.

## In the API

- Platform API type `DmPeripheralParameters` is named by the class but is not in the API snapshot.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The name of the peripheral parameter. |  |  |
| value | string | 1 | The value of the peripheral parameter. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_PeripheralConfiguration](dm_PeripheralConfiguration.md) | parameters | * |  |
