# Board Layer (des_BoardLayer)

- Name: `des_BoardLayer`
- IRI: `des:BoardLayer` (https://w3id.org/altium/cdm/design/BoardLayer)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_BoardLayer/](../../classes/des_BoardLayer/)

A physical or logical layer of a board: copper (signal or plane), dielectric, mask, overlay, paste or mechanical.

## In the API

- Platform API type: [`DesLayer`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesLayer/) (object)
- Altium Designer SDK type: [`PCB.IPCB_LayerObject`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_LayerObject/)
- Altium Designer SDK type: [`PCB.IPCB_ElectricalLayer`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_ElectricalLayer/)
- Altium Designer SDK type: [`PCB.IPCB_DielectricLayer`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_DielectricLayer/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The layer name. |  |  |
| layerType | [des_LayerType](../enums/des_LayerType.md) | 1 | The kind of layer. |  |  |
| material | string | 0..1 | The layer material. |  |  |
| thickness | decimal | 0..1 | The layer thickness, in millimetres. |  |  |
| copperWeight | decimal | 0..1 | The copper weight of a copper layer, in ounces. |  |  |
| dielectricConstant | decimal | 0..1 | The dielectric constant of a dielectric layer. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_LayerStack](des_LayerStack.md) | layers | * |  |
| [des_Pad](des_Pad.md) | layer | 0..1 |  |
| [des_PcbComponent](des_PcbComponent.md) | layer | 0..1 |  |
| [des_PcbNet](des_PcbNet.md) | layers | * |  |
| [des_Track](des_Track.md) | layer | 0..1 |  |
| [des_Via](des_Via.md) | endLayer | 0..1 |  |
| [des_Via](des_Via.md) | startLayer | 0..1 |  |
