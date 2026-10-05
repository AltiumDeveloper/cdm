# AddressSegment (dm_AddressSegment)

- Name: `dm_AddressSegment`
- IRI: `dm:AddressSegment` (https://w3id.org/altium/cdm/deviceModel/AddressSegment)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [dm_HasAddressRange](dm_HasAddressRange.md)
- HTML page: [classes/dm_AddressSegment/](../../classes/dm_AddressSegment/)

A contiguous region of the device's memory map. Each segment can represent either a memory or a peripheral region.

## In the API

- Platform API type: [`DmAddressSegment`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAddressSegment/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| description | string | 0..1 | A brief description of the entity. |  |  |
| name | string | 0..1 | The name of the address segment. |  |  |
| aliases | string | * | Alternative names for the segment. |  |  |
| blocks | [dm_AddressBlock](dm_AddressBlock.md) | * | The nested address blocks within the segment |  |  |
| peripherals | [dm_Peripheral](dm_Peripheral.md) | * | The peripherals associated with this segment. |  |  |
| startAddress | integer | 1 | The base physical address of the memory region. |  | [dm_HasAddressRange](dm_HasAddressRange.md) |
| size | integer | 0..1 | The total span of the memory region in bytes. |  | [dm_HasAddressRange](dm_HasAddressRange.md) |

## Referenced by

- [dm_AddressMap](dm_AddressMap.md): `segments`
