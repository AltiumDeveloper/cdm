# Layer Stack (des_LayerStack)

- Name: `des_LayerStack`
- IRI: `des:LayerStack` (https://w3id.org/altium/cdm/design/LayerStack)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_LayerStack/](../../classes/des_LayerStack/)

One stack of layers of a board, ordered from top to bottom; a rigid-flex board has one per rigid or flex region type.

## In the API

- Platform API type: [`DesStack`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesStack/) (object)
- Altium Designer SDK type: [`PCB.IPCB_LayerStack`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_LayerStack/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The stack name. |  |  |
| layers | [des_BoardLayer](des_BoardLayer.md) | * | The layers of the stack, ordered from top to bottom. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Stackup](des_Stackup.md) | stacks | * |  |
