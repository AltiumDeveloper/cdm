# Net Class (des_NetClass)

- Name: `des_NetClass`
- IRI: `des:NetClass` (https://w3id.org/altium/cdm/design/NetClass)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_NetClass/](../../classes/des_NetClass/)

A named group of nets that share design rules, for example DDR3 or HighSpeed.

## In the API

- Altium Designer SDK type: [`EDP.INetClass`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/INetClass/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | Net class name. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_CompiledDesign](des_CompiledDesign.md) | netClasses | * |  |
| [des_Net](des_Net.md) | netClasses | * |  |
