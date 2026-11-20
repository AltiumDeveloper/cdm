# Via (des_Via)

- Name: `des_Via`
- IRI: `des:Via` (https://w3id.org/altium/cdm/design/Via)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Via/](../../classes/des_Via/)

A plated hole that connects copper on two or more layers of a board.

## In the API

- Platform API type: [`DesVia`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesVia/) (object)
- Altium Designer SDK type: [`PCB.IPCB_Via`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Via/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | The via name, if any. |  |  |
| position | [des_Point2D](des_Point2D.md) | 1 | The via location. |  |  |
| holeDiameter | decimal | 1 | The hole diameter, in millimetres. |  |  |
| padDiameter | decimal | 1 | The pad diameter, in millimetres. |  |  |
| shape | [des_PrimitiveShape](../enums/des_PrimitiveShape.md) | 0..1 | The via pad shape. |  |  |
| startLayer | [des_BoardLayer](des_BoardLayer.md) | 0..1 | The first layer the via connects. |  |  |
| endLayer | [des_BoardLayer](des_BoardLayer.md) | 0..1 | The last layer the via connects. |  |  |
| net | [des_PcbNet](des_PcbNet.md) | 0..1 | The net the via is on. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PcbLayout](des_PcbLayout.md) | vias | * |  |
| [des_PcbNet](des_PcbNet.md) | vias | * |  |
