# User Group (plt_UserGroup)

- Name: `plt_UserGroup`
- IRI: `plt:UserGroup` (https://w3id.org/altium/cdm/platform/UserGroup)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_UserGroup/](../../classes/plt_UserGroup/)

A named group of users within an organization's Company Account, managed in the Company Dashboard. Licenses can be allocated to a group so that its members can use them, and the Group Administrators system group gives its members Dashboard administration rights. A user can belong to any number of groups, groups can be provisioned from an identity provider via SCIM, and they are distinct from the groups defined inside a Workspace.

## In the product

- [Managing Groups](https://www.altium.com/documentation/altium-dashboard/managing-groups) (primary)

## In the API

- Platform API type: [`GloUserGroup`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloUserGroup/) (object)

## GRID

`grid:global::platform:group/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
