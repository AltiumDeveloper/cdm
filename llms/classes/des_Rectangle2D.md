# Rectangle 2D (des_Rectangle2D)

- Name: `des_Rectangle2D`
- IRI: `des:Rectangle2D` (https://w3id.org/altium/cdm/design/Rectangle2D)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Rectangle2D/](../../classes/des_Rectangle2D/)

An axis-aligned rectangle, used for bounding boxes of drawing objects.

## Comments

- Platform API PCB items give two corners (DesRectangle pos1/pos2); schematic design data gives left/bottom/right/top (DesignDataRectangle_Preview).

## In the API

- Platform API type: [`DesRectangle`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesRectangle/) (object)
- Altium Designer SDK type: [`PCB.ICoordRect`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/ICoordRect/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| left | decimal | 1 | The left edge, in millimetres. |  |  |
| bottom | decimal | 1 | The bottom edge, in millimetres. |  |  |
| right | decimal | 1 | The right edge, in millimetres. |  |  |
| top | decimal | 1 | The top edge, in millimetres. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_ComponentPart](des_ComponentPart.md) | boundingBox | 0..1 |  |
| [des_NetItem](des_NetItem.md) | boundingBox | 0..1 |  |
| [des_PcbComponent](des_PcbComponent.md) | boundingBox | 0..1 |  |
| [des_PinInstance](des_PinInstance.md) | boundingBox | 0..1 |  |
| [des_PlacedComponent](des_PlacedComponent.md) | boundingBox | 0..1 |  |
| [des_Wire](des_Wire.md) | boundingBox | 0..1 |  |
