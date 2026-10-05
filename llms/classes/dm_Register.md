# Register (dm_Register)

- Name: `dm_Register`
- IRI: `dm:Register` (https://w3id.org/altium/cdm/deviceModel/Register)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [dm_HasAddressRange](dm_HasAddressRange.md)
- HTML page: [classes/dm_Register/](../../classes/dm_Register/)

A hardware register within an address block.

## In the API

- Platform API type: [`DmAmRegister`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAmRegister/) (object)

## In standards

- close: [CMSIS-SVD register element](https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html#elem_register)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| description | string | 0..1 | A brief description of the entity. |  |  |
| name | string | 0..1 | The name of the register. |  |  |
| access | [dm_AccessType](../enums/dm_AccessType.md) | 0..1 | The access type of the register. |  |  |
| resetValue | string | 0..1 | The value to reset the register. |  |  |
| resetMask | string | 0..1 | The mask applied during register reset. |  |  |
| fields | [dm_RegisterField](dm_RegisterField.md) | * | Bit fields within this register. |  |  |
| startAddress | integer | 1 | The base physical address of the memory region. |  | [dm_HasAddressRange](dm_HasAddressRange.md) |
| size | integer | 0..1 | The total span of the memory region in bytes. |  | [dm_HasAddressRange](dm_HasAddressRange.md) |

## Referenced by

- [dm_AddressBlock](dm_AddressBlock.md): `registers`
