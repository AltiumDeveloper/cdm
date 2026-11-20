# Pin (lib_Pin)

- Name: `lib_Pin`
- IRI: `lib:Pin` (https://w3id.org/altium/cdm/library/Pin)
- Bounded context: [library](../library.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/lib_Pin/](../../classes/lib_Pin/)

A pin definition on a schematic symbol: one electrical connection point with its designator, name and electrical type, and optionally alternate functions. Pins placed in a design take their definition from here.

## Comments

- From udm_Pin in pull request 23 (UDM modelling).

## In the API

- Platform API type: [`DesPin`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesPin/) (object)
- Altium Designer SDK type: [`SCH.ISch_Pin`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/sch/ISch_Pin/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| designator | string | 1 | Pin designator, unique within the symbol, e.g. 1 or A3. |  |  |
| name | string | 0..1 | Pin name, e.g. VCC or PA5. |  |  |
| electricalType | [lib_PinElectricalType](../enums/lib_PinElectricalType.md) | 0..1 | Electrical type of the pin, used by electrical rule checks. |  |  |
| functions | string | * | Alternate functions the pin can serve, e.g. SPI1_CLK or UART2_TX. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PinInstance](des_PinInstance.md) | definedBy | 0..1 |  |
| [lib_SymbolRevision](lib_SymbolRevision.md) | pins | * | core_hasPart |
