# PortConfigurationEnumValue (dm_PortConfigurationEnumValue)

- Name: `dm_PortConfigurationEnumValue`
- IRI: `dm:PortConfigurationEnumValue` (https://w3id.org/altium/cdm/deviceModel/PortConfigurationEnumValue)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PortConfigurationEnumValue/](../../classes/dm_PortConfigurationEnumValue/)

An enumerated value for a port configuration.

## In the API

- Platform API type: [`DmConfigEnumValue`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmConfigEnumValue/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | The name of the enumerated value. |  |  |
| dependencies | [dm_PortConfigurationDependency](dm_PortConfigurationDependency.md) | * | The list of dependencies associated with this enumerated value. |  |  |

## Referenced by

- [dm_PortConfiguration](dm_PortConfiguration.md): `enumValues`
