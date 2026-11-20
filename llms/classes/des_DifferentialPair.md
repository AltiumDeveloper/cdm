# Differential Pair (des_DifferentialPair)

- Name: `des_DifferentialPair`
- IRI: `des:DifferentialPair` (https://w3id.org/altium/cdm/design/DifferentialPair)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_DifferentialPair/](../../classes/des_DifferentialPair/)

Two nets that carry a differential signal together, for example USB_D_P and USB_D_N.

## In the API

- Platform API type: [`DesignDataDifferentialPair_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataDifferentialPair_Preview/) (object)
- Altium Designer SDK type: [`EDP.IDifferentialPair`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IDifferentialPair/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | Differential pair name, e.g. USB_D. |  |  |
| positive | [des_Net](des_Net.md) | 0..1 | The positive net of the pair. |  |  |
| negative | [des_Net](des_Net.md) | 0..1 | The negative net of the pair. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Net](des_Net.md) | differentialPair | 0..1 |  |
