# Track (des_Track)

- Name: `des_Track`
- IRI: `des:Track` (https://w3id.org/altium/cdm/design/Track)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Track/](../../classes/des_Track/)

A straight conductor segment on a board layer, with a width.

## In the API

- Platform API type: [`DesTrack`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesTrack/) (object)
- Altium Designer SDK type: [`PCB.IPCB_Track`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Track/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| begin | [des_Point2D](des_Point2D.md) | 1 | The first end point. |  |  |
| end | [des_Point2D](des_Point2D.md) | 1 | The second end point. |  |  |
| width | decimal | 1 | The track width, in millimetres. |  |  |
| layer | [des_BoardLayer](des_BoardLayer.md) | 0..1 | The layer of the track. |  |  |
| net | [des_PcbNet](des_PcbNet.md) | 0..1 | The net the track is on. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PcbLayout](des_PcbLayout.md) | tracks | * |  |
| [des_PcbNet](des_PcbNet.md) | tracks | * |  |
