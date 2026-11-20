# Point 2D (des_Point2D)

- Name: `des_Point2D`
- IRI: `des:Point2D` (https://w3id.org/altium/cdm/design/Point2D)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Point2D/](../../classes/des_Point2D/)

A point in the coordinate system of a schematic sheet or PCB document.

## Comments

- The Platform API serves PCB positions in internal units, mils and millimetres (DesPosition2D); the AD SDK uses internal units of 10,000 per mil. The integer x/y of DesignDataLocation_Preview (schematic design data) has no unit stated in the API snapshot; this is open question Q7.

## In the API

- Platform API type: [`DesPosition2D`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesPosition2D/) (object)
- Altium Designer SDK type: [`PCB.ICoordPoint`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/ICoordPoint/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| x | decimal | 1 | The X coordinate, in millimetres. |  |  |
| y | decimal | 1 | The Y coordinate, in millimetres. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_ComponentPart](des_ComponentPart.md) | location | 0..1 |  |
| [des_NetItem](des_NetItem.md) | location | 0..1 |  |
| [des_Pad](des_Pad.md) | position | 1 |  |
| [des_PcbComponent](des_PcbComponent.md) | position | 0..1 |  |
| [des_PcbLayout](des_PcbLayout.md) | origin | 0..1 |  |
| [des_PcbLayout](des_PcbLayout.md) | outline | * |  |
| [des_PinInstance](des_PinInstance.md) | location | 0..1 |  |
| [des_PlacedComponent](des_PlacedComponent.md) | location | 0..1 |  |
| [des_Track](des_Track.md) | begin | 1 |  |
| [des_Track](des_Track.md) | end | 1 |  |
| [des_Via](des_Via.md) | position | 1 |  |
| [des_Wire](des_Wire.md) | location | 0..1 |  |
| [des_Wire](des_Wire.md) | vertices | * |  |
