# PeripheralPinDependencyConfig (dm_PeripheralPinDependencyConfig)

- Name: `dm_PeripheralPinDependencyConfig`
- IRI: `dm:PeripheralPinDependencyConfig` (https://w3id.org/altium/cdm/deviceModel/PeripheralPinDependencyConfig)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PeripheralPinDependencyConfig/](../../classes/dm_PeripheralPinDependencyConfig/)

A pin dependency to port mapping entry within peripheral configuration.

## In the API

- Platform API type `DmPeripheralPinDependencyConfig` is named by the class but is not in the API snapshot.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | The name of the pin dependency configuration. |  |  |
| value | string | 0..1 | The value of the pin dependency configuration. |  |  |

## Referenced by

- [dm_PeripheralConfiguration](dm_PeripheralConfiguration.md): `pinDependencyConfigs`
