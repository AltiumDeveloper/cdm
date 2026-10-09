# BOM Item (pro_BomItem)

- Name: `pro_BomItem`
- IRI: `pro:BomItem` (https://w3id.org/altium/cdm/procurement/BomItem)
- Bounded context: [procurement](../procurement.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/pro_BomItem/](../../classes/pro_BomItem/)

One line of a BOM: its designators and quantity, the primary manufacturer part used for it (identified by manufacturer and manufacturer part number), and any alternate parts recorded for that line. A line can be linked to a Workspace component that lists its part among its Part Choices, and BOM checks report issues against individual lines.

## In the product

- [Configuration and Options](https://www.altium.com/documentation/altium-365/bom-portal/configuration-options#bom-structure-features) (primary)
- Term: **BOM line** (exact; altium-365)

## In the API

- Platform API type: [`BomItem`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomItem/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| issues | [pro_BomIssue](pro_BomIssue.md) | * | Issues associated with this BOM item. |  |  |
| designators | string | * | A list of designators that specify the placements of the item within the schematic. |  |  |
| quantity | integer | 1 | The quantity of the item required to produce one unit. |  |  |
| primaryElement | [pro_BomItemElement](pro_BomItemElement.md) | 0..1 | The primary element chosen for this item. |  |  |
| alternates | [pro_BomItemAlternate](pro_BomItemAlternate.md) | * | Alternate elements that could be used for this item. |  |  |
| substitutes | [pro_BomItemSubstitute](pro_BomItemSubstitute.md) | * | Substitute elements that could be used for this item. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [pro_Bom](pro_Bom.md) | items | * |  |
