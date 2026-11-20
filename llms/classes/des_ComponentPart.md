# Component Part (des_ComponentPart)

- Name: `des_ComponentPart`
- IRI: `des:ComponentPart` (https://w3id.org/altium/cdm/design/ComponentPart)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_ComponentPart/](../../classes/des_ComponentPart/)

One part (section) of a placed component. Multi-part components, such as a quad op-amp, are drawn as several parts that may sit on different sheets; each part carries a subset of the component's pins.

## In the API

- Platform API type: [`DesignDataPart_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataPart_Preview/) (object)
- Altium Designer SDK type: [`EDP.IPart`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IPart/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| uniqueId | string | 0..1 | Identifier of the part, unique within the design. |  |  |
| sheet | [des_SchematicSheet](des_SchematicSheet.md) | 0..1 | The sheet the part is drawn on. |  |  |
| pins | [des_PinInstance](des_PinInstance.md) | * | The pins of this part. |  |  |
| location | [des_Point2D](des_Point2D.md) | 0..1 | The location on its schematic sheet. |  |  |
| boundingBox | [des_Rectangle2D](des_Rectangle2D.md) | 0..1 | The bounding box on its schematic sheet. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PlacedComponent](des_PlacedComponent.md) | parts | * |  |
