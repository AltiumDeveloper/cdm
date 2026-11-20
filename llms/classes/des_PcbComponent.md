# PCB Component (des_PcbComponent)

- Name: `des_PcbComponent`
- IRI: `des:PcbComponent` (https://w3id.org/altium/cdm/design/PcbComponent)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_PcbComponent/](../../classes/des_PcbComponent/)

A component as placed on a board: its footprint instance with position, rotation, side and pads.

## Comments

- The Platform API gives the schematic and PCB identifiers of a design item (DesDesignItem.schId, pcbId) but does not state how they join to DesignDataComponent_Preview; the AD SDK gives IPCB_Component.SourceUniqueId and SourceDesignator. The join is open question Q8.
- The Platform API gives the footprint by name only (DesDesignItem.footprintName); the AD SDK gives IPCB_Component.ItemGUID / ItemRevisionGUID / VaultGUID, which can resolve a managed footprint.

## In the API

- Platform API type: [`DesDesignItem`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesDesignItem/) (object)
- Altium Designer SDK type: [`PCB.IPCB_Component`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/pcb/IPCB_Component/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| designator | string | 1 | The component designator on the board. |  |  |
| footprintName | string | 0..1 | The name of the footprint used. |  |  |
| position | [des_Point2D](des_Point2D.md) | 0..1 | The placement location. |  |  |
| rotation | decimal | 0..1 | The rotation, in degrees. |  |  |
| layer | [des_BoardLayer](des_BoardLayer.md) | 0..1 | The layer the component is placed on (top or bottom side). |  |  |
| boundingBox | [des_Rectangle2D](des_Rectangle2D.md) | 0..1 | The bounding box of the component on the board. |  |  |
| pads | [des_Pad](des_Pad.md) | * | The pads of the footprint instance. |  |  |
| placedComponent | [des_PlacedComponent](des_PlacedComponent.md) | 0..1 | The component in the compiled schematic design that this board component implements. |  |  |
| footprint | [lib_FootprintRevision](lib_FootprintRevision.md) | 0..1 | The Workspace footprint revision used, when the footprint is managed. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PcbLayout](des_PcbLayout.md) | components | * |  |
