# BOM Item Alternate (pro_BomItemAlternate)

- Name: `pro_BomItemAlternate`
- IRI: `pro:BomItemAlternate` (https://w3id.org/altium/cdm/procurement/BomItemAlternate)
- Bounded context: [procurement](../procurement.md)
- Kind: Resource
- Is a: [pro_BomItemElement](pro_BomItemElement.md)
- HTML page: [classes/pro_BomItemAlternate/](../../classes/pro_BomItemAlternate/)

An alternate part recorded for one BOM line: another manufacturer part that could be used instead of the line's primary part. Alternates belong to the individual BOM line rather than applying across BOMs. They can come from an uploaded BOM file, be added by hand, or be filled in automatically from the linked component's Part Choices and from suggested alternates, and an alternate can be promoted to become the line's primary part.

## In the product

- [Configuration and Options](https://www.altium.com/documentation/altium-365/bom-portal/configuration-options#add_alternate) (primary)
- Term: **Alternate** (exact; altium-365)

## In the API

- Platform API type: [`BomItemAlternate`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomItemAlternate/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_BomItemElement](pro_BomItemElement.md) |
| mpn | string | 0..1 |  |  | [pro_BomItemElement](pro_BomItemElement.md) |
| manufacturer | string | 0..1 |  |  | [pro_BomItemElement](pro_BomItemElement.md) |
| part | [lib_Part](lib_Part.md) or [sup_Part](sup_Part.md) | 0..1 | The Part this element resolves to - a workspace library Part for workspace BOMs, or a supply Part for BOMs that live outside a workspace (e.g. Global BOM). |  | [pro_BomItemElement](pro_BomItemElement.md) |
| component | [lib_ComponentRevision](lib_ComponentRevision.md) | 0..1 |  |  | [pro_BomItemElement](pro_BomItemElement.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [pro_BomItem](pro_BomItem.md) | alternates | * |  |
