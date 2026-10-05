# Offer (sup_Offer)

- Name: `sup_Offer`
- IRI: `sup:Offer` (https://w3id.org/altium/cdm/supply/Offer)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_Offer/](../../classes/sup_Offer/)

Supply Offer represents a specific commercial listing of a Part from a supplier, detailing price breaks, stock availability, lead times, and ordering conditions at a given point in time.

## Comments

- Each Supply Offer has its own identity and is associated with a Supply Part, reflecting one supplier’s current market position.
- It enables designers and procurement teams to evaluate sourcing options dynamically, supporting cost optimization, risk mitigation, and automated supply validation within the Altium 365 and Octopart ecosystems.

## In the product

- [Sourced Manufacturer and Supplier Data](https://www.altium.com/documentation/altium-365/bom-portal/sourced-manufacturer-supplier-data#order_list) (primary)
- [Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api)
- Term: **Supplier Part** (related; altium-designer)

## In the API

- Nexar type: `SupOffer` ([Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api))

## GRID

`grid:supply::platform:part/{id}/offer/{offerID}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
