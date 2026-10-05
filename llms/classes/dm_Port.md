# Port (dm_Port)

- Name: `dm_Port`
- IRI: `dm:Port` (https://w3id.org/altium/cdm/deviceModel/Port)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_Port/](../../classes/dm_Port/)

A physical port on the device, with its functions, configurations, and connections.

## In the API

- Platform API type: [`DmPort`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPort/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| description | string | 0..1 | A brief description of the entity. |  |  |
| name | string | 0..1 | The name of the port. |  |  |
| symbolicName | string | 0..1 | A symbolic name for the port used in code or configuration. |  |  |
| pin | [dm_Pin](dm_Pin.md) | 0..1 | The physical pin associated with this port. |  |  |
| functions | [dm_PortFunction](dm_PortFunction.md) | * | The list of functions that this port can perform. |  |  |
| configurations | [dm_PortConfiguration](dm_PortConfiguration.md) | * | The list of configurations available for this port. |  |  |
| connections | [dm_PortConnection](dm_PortConnection.md) | * | The list of connections associated with this port to other components or signals. |  |  |

## Referenced by

- [dm_ConfiguredDeviceModel](dm_ConfiguredDeviceModel.md): `ports`
- [dm_FullStackDeviceModel](dm_FullStackDeviceModel.md): `ports`
- [system_SdmDeviceModel](system_SdmDeviceModel.md): `ports`
