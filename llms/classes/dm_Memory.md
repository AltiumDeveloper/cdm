# Memory (dm_Memory)

- Name: `dm_Memory`
- IRI: `dm:Memory` (https://w3id.org/altium/cdm/deviceModel/Memory)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_Memory/](../../classes/dm_Memory/)

A memory entry within an address block.

## In the API

- Platform API type: [`DmAmMemory`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAmMemory/) (object)

## In standards

- close: [CMSIS-Pack PDSC memory element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | The name of the memory entry. |  |  |
| type | string | 0..1 | The type of memory entry. |  |  |
| size | integer | 0..1 | The total span of the memory region in bytes. |  |  |

## Referenced by

- [dm_AddressBlock](dm_AddressBlock.md): `memories`
