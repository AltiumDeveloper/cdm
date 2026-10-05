# Part (sup_Part)

- Name: `sup_Part`
- IRI: `sup:Part` (https://w3id.org/altium/cdm/supply/Part)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_Part/](../../classes/sup_Part/)

Supply Part represents a market-available instance of a manufactured Part, providing aggregated sourcing data such as pricing, stock levels, and supplier offers.

## Comments

- Each Supply Part has its own identity derived from manufacturer and supplier metadata, and may correspond to multiple suppliers’ listings.
- It bridges the design and supply chain domains by enriching managed Parts with real-time market intelligence, enabling informed sourcing, alternates evaluation, and procurement optimization within Altium 365.

## In the product

- [Searching for Manufacturer Parts](https://www.altium.com/documentation/altium-designer/components-libraries/searching-manufacturer-parts#manufacturer_and_supplier_data) (primary)
- [Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api)
- Term: **Manufacturer Part** (related; altium-designer)

## In the API

- Nexar type: `SupPart` ([Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api))

## GRID

`grid:supply::platform:part/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| mpn | string | 1 |  |  |  |
| manufacturer | [sup_Company](sup_Company.md) | 1 | The company that manufactures this part. |  |  |
| referenceDesigns | [sup_ReferenceDesign](sup_ReferenceDesign.md) | * | Reference designs that use this part. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [pro_BomItemElement](pro_BomItemElement.md): `part`
- [pro_GlobalBOM](pro_GlobalBOM.md): `usesParts`
- [sup_PartGroup](sup_PartGroup.md): `parts`
