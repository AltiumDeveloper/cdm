# Layer Stackup (des_Stackup)

- Name: `des_Stackup`
- IRI: `des:Stackup` (https://w3id.org/altium/cdm/design/Stackup)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Stackup/](../../classes/des_Stackup/)

The layer structure of a board: one or more layer stacks (more than one for rigid-flex boards).

## In the API

- Platform API type: [`DesStackup`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesStackup/) (object)
- Altium Designer SDK type: [`PCB.IPCB_MasterLayerStack`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_MasterLayerStack/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| stackupType | string | 0..1 | The stackup type as reported by the Platform API. |  |  |
| stacks | [des_LayerStack](des_LayerStack.md) | * | The layer stacks (substacks) of the board. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PcbLayout](des_PcbLayout.md) | stackup | 0..1 |  |
