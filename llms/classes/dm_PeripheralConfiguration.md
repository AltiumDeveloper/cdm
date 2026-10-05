# PeripheralConfiguration (dm_PeripheralConfiguration)

- Name: `dm_PeripheralConfiguration`
- IRI: `dm:PeripheralConfiguration` (https://w3id.org/altium/cdm/deviceModel/PeripheralConfiguration)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PeripheralConfiguration/](../../classes/dm_PeripheralConfiguration/)

A concrete configuration for a peripheral role, containing pin multiplexing details.

## In the API

- Platform API type `DmPeripheralConfiguration` is named by the class but is not in the API snapshot.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| parameters | [dm_PeripheralParameter](dm_PeripheralParameter.md) | * | The list of parameters associated with this peripheral configuration. |  |  |
| pinConfigs | [dm_PeripheralPinConfig](dm_PeripheralPinConfig.md) | * | The list of pin function to port mappings for this configuration. |  |  |
| pinDependencyConfigs | [dm_PeripheralPinDependencyConfig](dm_PeripheralPinDependencyConfig.md) | * | The list of alternative pin configurations that must be applied together with this configuration. |  |  |

## Referenced by

- [dm_PeripheralMode](dm_PeripheralMode.md): `configurations`
