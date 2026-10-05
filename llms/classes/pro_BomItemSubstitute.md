# BOM Item Substitute (pro_BomItemSubstitute)

- Name: `pro_BomItemSubstitute`
- IRI: `pro:BomItemSubstitute` (https://w3id.org/altium/cdm/procurement/BomItemSubstitute)
- Bounded context: [procurement](../procurement.md)
- Kind: Resource
- Is a: [pro_BomItemElement](pro_BomItemElement.md)
- HTML page: [classes/pro_BomItemSubstitute/](../../classes/pro_BomItemSubstitute/)

Substitute is a replacement of a part by another within an individual BOM.

## In the API

- Platform API type: [`BomItemSubstitute`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomItemSubstitute/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  | [pro_BomItemElement](pro_BomItemElement.md) |
| mpn | string | 0..1 |  |  | [pro_BomItemElement](pro_BomItemElement.md) |
| manufacturer | string | 0..1 |  |  | [pro_BomItemElement](pro_BomItemElement.md) |
| part | [lib_Part](lib_Part.md) or [sup_Part](sup_Part.md) | 0..1 | The Part this element resolves to - a workspace library Part for workspace BOMs, or a supply Part for BOMs that live outside a workspace (e.g. Global BOM). |  | [pro_BomItemElement](pro_BomItemElement.md) |
| component | [lib_ComponentRevision](lib_ComponentRevision.md) | 0..1 |  |  | [pro_BomItemElement](pro_BomItemElement.md) |

## Referenced by

- [pro_BomItem](pro_BomItem.md): `substitutes`
