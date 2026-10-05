# RegisterField (dm_RegisterField)

- Name: `dm_RegisterField`
- IRI: `dm:RegisterField` (https://w3id.org/altium/cdm/deviceModel/RegisterField)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_RegisterField/](../../classes/dm_RegisterField/)

A bit field within a register.

## In the API

- Platform API type: [`DmAmRegisterField`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAmRegisterField/) (object)

## In standards

- exact: [CMSIS-SVD field element](https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html#elem_field)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| description | string | 0..1 | A brief description of the entity. |  |  |
| name | string | 0..1 | The name of the register field. |  |  |
| lsb | integer | 0..1 | The least significant bit position of the field. |  |  |
| msb | integer | 0..1 | The most significant bit position of the field. |  |  |
| access | [dm_AccessType](../enums/dm_AccessType.md) | 0..1 | The access type of the register field. |  |  |
| enums | [dm_FieldEnum](dm_FieldEnum.md) | * | Enumerated values for the register field. |  |  |

## Referenced by

- [dm_Register](dm_Register.md): `fields`
