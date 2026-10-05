# BOM Issue (pro_BomIssue)

- Name: `pro_BomIssue`
- IRI: `pro:BomIssue` (https://w3id.org/altium/cdm/procurement/BomIssue)
- Bounded context: [procurement](../procurement.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/pro_BomIssue/](../../classes/pro_BomIssue/)

A problem found when a BOM is analysed, usually against a particular BOM line: for example an unknown part number, a duplicated designator, or a part that is deprecated, low in stock or not compliant with a standard such as REACH. The level at which each kind of check reports (Fatal Error, Error or Warning, or No Report to ignore it) is configurable, and an individual issue can be waived.

## In the product

- [BOM Error Detection and Correction](https://www.altium.com/documentation/altium-365/bom-portal/error-detection-correction) (primary)

## In the API

- Platform API type: [`BomIssue`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/BomIssue/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| description | string | 0..1 |  |  |  |
| howToFix | string | 0..1 |  |  |  |
| severity | string | 0..1 |  |  |  |

## Referenced by

- [pro_Bom](pro_Bom.md): `issues`
- [pro_BomItem](pro_BomItem.md): `issues`
- [pro_BomItemElement](pro_BomItemElement.md): `issues`
