# Pin (dm_Pin)

- Name: `dm_Pin`
- IRI: `dm:Pin` (https://w3id.org/altium/cdm/deviceModel/Pin)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_Pin/](../../classes/dm_Pin/)

A physical pin on the device.

## In the API

- Platform API type: [`DmPin`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPin/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The name of the pin. |  |  |

## Referenced by

- [dm_Port](dm_Port.md): `pin`
