# Company (sup_Company)

- Name: `sup_Company`
- IRI: `sup:Company` (https://w3id.org/altium/cdm/supply/Company)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_Company/](../../classes/sup_Company/)

Supply Company represents an organization in the electronics supply chain. Depending on context it is the manufacturer of a Part or a distributor (or broker) that sells it.

## Comments

- Each Supply Company has its own identity and metadata, including contact, regional, and certification details.
- It serves as the authoritative entity behind Supply Offers, enabling traceability, supplier qualification, and integration of trusted sourcing data across Octopart and Altium 365 workflows.

## In the API

- Nexar type: `SupCompany` ([Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api))

## GRID

`grid:supply::platform:company/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [sup_Part](sup_Part.md) | manufacturer | 1 |  |
