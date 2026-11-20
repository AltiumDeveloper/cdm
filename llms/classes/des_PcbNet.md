# PCB Net (des_PcbNet)

- Name: `des_PcbNet`
- IRI: `des:PcbNet` (https://w3id.org/altium/cdm/design/PcbNet)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_PcbNet/](../../classes/des_PcbNet/)

A net as realised in copper on a board: the pads, tracks and vias that carry it, the layers it is routed on and its routed length.

## Comments

- The AD SDK links a PCB net to its logical net (IPCB_Net.GetLogicalNet); the Platform API has no such link, so a consumer can only join on the net name.

## In the API

- Platform API type: [`DesNet`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesNet/) (object)
- Altium Designer SDK type: [`PCB.IPCB_Net`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Net/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The net name. |  |  |
| routedLength | decimal | 0..1 | The cumulative routed length, in millimetres. |  |  |
| layers | [des_BoardLayer](des_BoardLayer.md) | * | The layers the net is routed on. |  |  |
| pads | [des_Pad](des_Pad.md) | * | The pads on the net. |  |  |
| tracks | [des_Track](des_Track.md) | * | The tracks on the net. |  |  |
| vias | [des_Via](des_Via.md) | * | The vias on the net. |  |  |
| logicalNet | [des_Net](des_Net.md) | 0..1 | The net of the compiled schematic design that this copper net implements. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Pad](des_Pad.md) | net | 0..1 |  |
| [des_PcbLayout](des_PcbLayout.md) | nets | * |  |
| [des_Track](des_Track.md) | net | 0..1 |  |
| [des_Via](des_Via.md) | net | 0..1 |  |
