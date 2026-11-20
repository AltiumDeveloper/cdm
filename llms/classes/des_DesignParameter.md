# Design Parameter (des_DesignParameter)

- Name: `des_DesignParameter`
- IRI: `des:DesignParameter` (https://w3id.org/altium/cdm/design/DesignParameter)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_DesignParameter/](../../classes/des_DesignParameter/)

A name/value parameter of an object in the compiled design, such as a placed component.

## In the API

- Altium Designer SDK type: [`EDP.IParameter`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IParameter/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | Parameter name. |  |  |
| value | string | 0..1 | Parameter value. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PlacedComponent](des_PlacedComponent.md) | parameters | * |  |
