# PortFunction (dm_PortFunction)

- Name: `dm_PortFunction`
- IRI: `dm:PortFunction` (https://w3id.org/altium/cdm/deviceModel/PortFunction)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_PortFunction/](../../classes/dm_PortFunction/)

A specific function that a port can perform.

## In the product

- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions#pulling_sdm_into_a_hardware_project) (primary)

## In the API

- Platform API type: [`DmPortFunction`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmPortFunction/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | The name of the port function. |  |  |
| peripheralInstance | [dm_PeripheralInstance](dm_PeripheralInstance.md) | 0..1 | The peripheral instance associated with this port function. |  |  |

## Referenced by

- [dm_Port](dm_Port.md): `functions`
