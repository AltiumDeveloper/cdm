# Organization (plt_Organization)

- Name: `plt_Organization`
- IRI: `plt:Organization` (https://w3id.org/altium/cdm/platform/Organization)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_Organization/](../../classes/plt_Organization/)

An Altium customer organization, represented by its Company Account. The Company Account brings together the organization's users and groups of users, its purchased licenses and the Altium 365 Workspaces created for it, along with a company profile (e.g. name, logo and website). Administrators manage it through the Company Dashboard.

## In the product

- [Company Dashboard](https://www.altium.com/documentation/altium-dashboard) (primary)
- [Configuring Your Company Profile](https://www.altium.com/documentation/altium-dashboard/profile)
- Term: **Company Account** (exact; altium-dashboard)

## In the API

- Platform API type: [`GloOrganization`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloOrganization/) (object)

## GRID

`grid:global::platform:organization/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
