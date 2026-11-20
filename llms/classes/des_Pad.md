# Pad (des_Pad)

- Name: `des_Pad`
- IRI: `des:Pad` (https://w3id.org/altium/cdm/design/Pad)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Pad/](../../classes/des_Pad/)

A connection target on a board, usually one pin of a placed component; a free pad belongs to no component.

## Comments

- Neither API states the pad-to-pin join explicitly; the AD SDK exposes IPCB_Pad.PinDescriptorString and OwnerPart_ID. This is part of open question Q8.

## In the API

- Platform API type: [`DesPad`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesPad/) (object)
- Altium Designer SDK type: [`PCB.IPCB_Pad`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Pad/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| designator | string | 0..1 | The pad designator within its component (for example 1, A3). |  |  |
| globalDesignator | string | 0..1 | The pad designator qualified by its component designator. |  |  |
| padType | [des_PadType](../enums/des_PadType.md) | 1 | Whether the pad is surface-mount or free. |  |  |
| shape | [des_PrimitiveShape](../enums/des_PrimitiveShape.md) | 0..1 | The pad shape. |  |  |
| sizeX | decimal | 0..1 | The pad size along X, in millimetres. |  |  |
| sizeY | decimal | 0..1 | The pad size along Y, in millimetres. |  |  |
| holeSize | decimal | 0..1 | The hole size, in millimetres; zero for surface-mount pads. |  |  |
| isPlated | boolean | 0..1 | Whether the hole is plated. |  |  |
| position | [des_Point2D](des_Point2D.md) | 1 | The pad location. |  |  |
| rotation | decimal | 0..1 | The rotation, in degrees. |  |  |
| layer | [des_BoardLayer](des_BoardLayer.md) | 0..1 | The layer of the pad; multi-layer for through-hole pads. |  |  |
| net | [des_PcbNet](des_PcbNet.md) | 0..1 | The net the pad is on. |  |  |
| pin | [des_PinInstance](des_PinInstance.md) | 0..1 | The pin of the compiled schematic design that this pad realises. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PcbComponent](des_PcbComponent.md) | pads | * |  |
| [des_PcbLayout](des_PcbLayout.md) | pads | * |  |
| [des_PcbNet](des_PcbNet.md) | pads | * |  |
