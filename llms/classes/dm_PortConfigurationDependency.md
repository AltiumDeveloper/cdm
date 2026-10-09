# PortConfigurationDependency (dm_PortConfigurationDependency)

- Name: `dm_PortConfigurationDependency`
- IRI: `dm:PortConfigurationDependency` (https://w3id.org/altium/cdm/deviceModel/PortConfigurationDependency)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PortConfigurationDependency/](../../classes/dm_PortConfigurationDependency/)

A dependency describing how a configuration value maps to GPIO or alternate function usage.

## In the API

- Platform API type: [`DmConfigDependency`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmConfigDependency/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| configRef | string | 1 | Root configuration reference token (e.g., P408). |  |  |
| altRef | string | 0..1 | Full alternative reference string used to derive mode/function tokens. |  |  |
| port | string | 0..1 | Port identifier extracted from the configuration reference (e.g., P000). |  |  |
| portMode | [dm_PortMode](../enums/dm_PortMode.md) | 0..1 | Port mode. |  |  |
| gpioMode | [dm_GpioMode](../enums/dm_GpioMode.md) | 0..1 | GPIO mode. |  |  |
| peripheralInstanceName | string | 0..1 | Peripheral instance name for alternate function mode (e.g., SCI0). |  |  |
| functionName | string | 0..1 | Peripheral function name for alternate mode (e.g., TXD, RXD). |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_PortConfigurationEnumValue](dm_PortConfigurationEnumValue.md) | dependencies | * |  |
