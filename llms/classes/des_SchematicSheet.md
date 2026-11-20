# Schematic Sheet (des_SchematicSheet)

- Name: `des_SchematicSheet`
- IRI: `des:SchematicSheet` (https://w3id.org/altium/cdm/design/SchematicSheet)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_SchematicSheet/](../../classes/des_SchematicSheet/)

A schematic document of the design. Sheets form a hierarchy: a sheet can reference sub-sheets, and a repeated (multi-channel) sub-sheet appears under each parent that references it.

## In the API

- Platform API type: [`DesignDataSchematicDocument_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataSchematicDocument_Preview/) (object)
- Altium Designer SDK type: [`EDP.IDocument`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IDocument/)
- Altium Designer SDK type: [`SCH.ISch_Sheet`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/sch/ISch_Sheet/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| documentId | string | 1 | Stable identifier of the sheet within the project. |  |  |
| fileName | string | 0..1 | File name of the sheet, e.g. MCU.SchDoc. |  |  |
| children | [des_SchematicSheet](des_SchematicSheet.md) | * | Sub-sheets referenced from this sheet. |  |  |
| width | decimal | 0..1 | The sheet width, in millimetres. |  |  |
| height | decimal | 0..1 | The sheet height, in millimetres. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_CompiledDesign](des_CompiledDesign.md) | sheets | * |  |
| [des_ComponentPart](des_ComponentPart.md) | sheet | 0..1 |  |
| [des_PlacedComponent](des_PlacedComponent.md) | sheet | 0..1 |  |
| [des_Wire](des_Wire.md) | sheet | 0..1 |  |
