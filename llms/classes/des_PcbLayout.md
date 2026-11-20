# PCB Layout (des_PcbLayout)

- Name: `des_PcbLayout`
- IRI: `des:PcbLayout` (https://w3id.org/altium/cdm/design/PcbLayout)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_PcbLayout/](../../classes/des_PcbLayout/)

The physical design of one board in a design project at one revision: its outline, layer stack, placed components, pads, tracks and vias, and the copper nets they form.

## Comments

- The Platform API serves it per variant (DesWipVariant.pcb, DesReleaseVariant.pcb), not under DesignData_Preview; it is attached to Compiled Design here so that one traversal reaches both the logical and the physical design (see G7, two schematic paths).
- Arcs, polygons (copper pours), regions, fills, text, dimensions, rooms and design rules are available in the AD SDK (IPCB_Arc, IPCB_Polygon, IPCB_Region, ...) but not in the Platform API, and are out of scope of this draft.
- DesPcb.mesh3D is marked PROTOTYPE in the Platform API and is out of scope.

## In the API

- Platform API type: [`DesPcb`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesPcb/) (object)
- Altium Designer SDK type: [`PCB.IPCB_Board`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Board/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| documentId | string | 1 | The identifier of the PCB document. |  |  |
| documentName | string | 0..1 | The PCB document file name. |  |  |
| origin | [des_Point2D](des_Point2D.md) | 0..1 | The location of the coordinate system origin. |  |  |
| outline | [des_Point2D](des_Point2D.md) | * | The vertices of the board outline, in order. |  |  |
| area | decimal | 0..1 | The area enclosed by the board outline, in square millimetres. |  |  |
| stackup | [des_Stackup](des_Stackup.md) | 0..1 | The layer structure of the board. |  |  |
| components | [des_PcbComponent](des_PcbComponent.md) | * | The components placed on the board. |  |  |
| nets | [des_PcbNet](des_PcbNet.md) | * | The electrically connected copper regions of the board. |  |  |
| pads | [des_Pad](des_Pad.md) | * | All pads on the board, including free pads. |  |  |
| tracks | [des_Track](des_Track.md) | * | All conductor segments on the board. |  |  |
| vias | [des_Via](des_Via.md) | * | All vias on the board. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_CompiledDesign](des_CompiledDesign.md) | boards | * |  |
