# User (plt_User)

- Name: `plt_User`
- IRI: `plt:User` (https://w3id.org/altium/cdm/platform/User)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_User/](../../classes/plt_User/)

A person identified by a global Altium Account, the identity used for signing in to Altium services. A user can be registered in an organization's Company Account, either added by an administrator or admitted through an approved join request, and can then be given access to licenses through the Company Account's user groups. Access to a Workspace is granted separately, by making the user a member of that Workspace.

## In the product

- [Managing Users](https://www.altium.com/documentation/altium-dashboard/managing-users) (primary)
- Term: **Altium Account** (related; altium-dashboard, altium-365)

## In the API

- Platform API type: [`GloUser`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloUser/) (object)

## GRID

`grid:global::platform:user/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
