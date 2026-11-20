# Pin Instance (des_PinInstance)

- Name: `des_PinInstance`
- IRI: `des:PinInstance` (https://w3id.org/altium/cdm/design/PinInstance)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_PinInstance/](../../classes/des_PinInstance/)

A pin of a placed component in the design. It takes its number, name and electrical type from the library pin definition and is connected to at most one net.

## Comments

- Replaces udm_DesignPin and des_design_pin from pull request 23.

## In the API

- Platform API type: [`DesignDataPin_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataPin_Preview/) (object)
- Altium Designer SDK type: [`EDP.INetItem`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/INetItem/)
- Altium Designer SDK type: [`SCH.ISch_Pin`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/sch/ISch_Pin/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| number | string | 1 | Pin number, e.g. 14 or A3. |  |  |
| name | string | 0..1 | Pin name, e.g. PA5. |  |  |
| electricalType | [lib_PinElectricalType](../enums/lib_PinElectricalType.md) | 0..1 | Electrical type of the pin, used by electrical rule checks. |  |  |
| functions | string | * | Alternate functions the pin can serve. |  |  |
| definedBy | [lib_Pin](lib_Pin.md) | 0..1 | The library pin definition this pin instance comes from, when the component is managed. |  |  |
| location | [des_Point2D](des_Point2D.md) | 0..1 | The location on its schematic sheet. |  |  |
| boundingBox | [des_Rectangle2D](des_Rectangle2D.md) | 0..1 | The bounding box on its schematic sheet. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_ComponentPart](des_ComponentPart.md) | pins | * |  |
| [des_Net](des_Net.md) | connects | * |  |
| [des_Pad](des_Pad.md) | pin | 0..1 |  |
