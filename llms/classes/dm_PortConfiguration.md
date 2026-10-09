# PortConfiguration (dm_PortConfiguration)

- Name: `dm_PortConfiguration`
- IRI: `dm:PortConfiguration` (https://w3id.org/altium/cdm/deviceModel/PortConfiguration)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PortConfiguration/](../../classes/dm_PortConfiguration/)

A specific configuration for a port.

## In the API

- Platform API type: [`DmPortConfiguration`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPortConfiguration/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | The name of the port configuration. |  |  |
| enumValues | [dm_PortConfigurationEnumValue](dm_PortConfigurationEnumValue.md) | * | The possible values that can be associated with this port configuration. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_Port](dm_Port.md) | configurations | * |  |
