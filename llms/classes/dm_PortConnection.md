# PortConnection (dm_PortConnection)

- Name: `dm_PortConnection`
- IRI: `dm:PortConnection` (https://w3id.org/altium/cdm/deviceModel/PortConnection)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PortConnection/](../../classes/dm_PortConnection/)

A connection from this port to another component or signal.

## In the API

- Platform API type: [`DmPortConnection`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPortConnection/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | The name of the port connection. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_Port](dm_Port.md) | connections | * |  |
