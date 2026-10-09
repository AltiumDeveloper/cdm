# FieldEnum (dm_FieldEnum)

- Name: `dm_FieldEnum`
- IRI: `dm:FieldEnum` (https://w3id.org/altium/cdm/deviceModel/FieldEnum)
- Bounded context: [deviceModel](../deviceModel.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/dm_FieldEnum/](../../classes/dm_FieldEnum/)

An enumerated value for a register field.

## In the API

- Platform API type: [`DmAmFieldEnum`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DmAmFieldEnum/) (object)

## In standards

- exact: [CMSIS-SVD enumeratedValue element](https://open-cmsis-pack.github.io/svd-spec/main/elem_registers.html#elem_enumeratedValue)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| description | string | 0..1 | A brief description of the entity. |  |  |
| name | string | 0..1 | The name of the enumerated value. |  |  |
| value | string | 0..1 | The actual value of the enumeration. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_RegisterField](dm_RegisterField.md) | enums | * |  |
