# AddressBlock (dm_AddressBlock)

- Name: `dm_AddressBlock`
- IRI: `dm:AddressBlock` (https://w3id.org/altium/cdm/deviceModel/AddressBlock)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [dm_HasAddressRange](dm_HasAddressRange.md)
- HTML page: [classes/dm_AddressBlock/](../../classes/dm_AddressBlock/)

Address block with start, size, and optional registers and peripherals.

## In the API

- Platform API type: [`DmAddressBlock`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAddressBlock/) (object)

## In standards

- related: [CMSIS-SVD addressBlock element](https://open-cmsis-pack.github.io/svd-spec/main/elem_peripherals.html#elem_addressBlock)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| description | string | 0..1 | A brief description of the entity. |  |  |
| name | string | 0..1 | The name of the address block. |  |  |
| type | [dm_AddressBlockType](../enums/dm_AddressBlockType.md) | 0..1 | The type of the address block. |  |  |
| memories | [dm_Memory](dm_Memory.md) | * | List of memory entries associated with this block. |  |  |
| registers | [dm_Register](dm_Register.md) | * | List of registers contained within this address block. |  |  |
| peripheralInstance | [dm_PeripheralInstance](dm_PeripheralInstance.md) | 0..1 | A peripheral instance associated with this address block. |  |  |
| startAddress | integer | 1 | The base physical address of the memory region. |  | [dm_HasAddressRange](dm_HasAddressRange.md) |
| size | integer | 0..1 | The total span of the memory region in bytes. |  | [dm_HasAddressRange](dm_HasAddressRange.md) |

## Referenced by

- [dm_AddressSegment](dm_AddressSegment.md): `blocks`
