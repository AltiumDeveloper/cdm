# BOM Item Element (pro_BomItemElement)

- Name: `pro_BomItemElement`
- IRI: `pro:BomItemElement` (https://w3id.org/altium/cdm/procurement/BomItemElement)
- Bounded context: [procurement](../procurement.md)
- Kind: Resource, abstract
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/pro_BomItemElement/](../../classes/pro_BomItemElement/)

An element (part) that might be used for a particular BOM item.

## In the product

- [Workspace Components Integration](https://www.altium.com/documentation/altium-365/bom-portal/workspace-components-integration) (primary)

## In the API

- Platform API type: [`BomItemElement`](https://altiumdeveloper.github.io/platform-api-docs/types/interfaces/BomItemElement/) (interface)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| issues | [pro_BomIssue](pro_BomIssue.md) | * |  |  |  |
| mpn | string | 0..1 |  |  |  |
| manufacturer | string | 0..1 |  |  |  |
| part | [lib_Part](lib_Part.md) or [sup_Part](sup_Part.md) | 0..1 | The Part this element resolves to - a workspace library Part for workspace BOMs, or a supply Part for BOMs that live outside a workspace (e.g. Global BOM). |  |  |
| component | [lib_ComponentRevision](lib_ComponentRevision.md) | 0..1 |  |  |  |

## Referenced by

- [pro_BomItem](pro_BomItem.md): `primaryElement`
