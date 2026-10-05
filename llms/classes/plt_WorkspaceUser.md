# Workspace User (plt_WorkspaceUser)

- Name: `plt_WorkspaceUser`
- IRI: `plt:WorkspaceUser` (https://w3id.org/altium/cdm/platform/WorkspaceUser)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_WorkspaceUser/](../../classes/plt_WorkspaceUser/)

A person's membership in a particular Workspace, connecting their Altium Account to that Workspace and to the Workspace groups they are assigned to. Members can come from the organization that owns the Workspace or from other organizations, and inviting an outside user does not add them to the owning organization. People who only have a project shared with them (External Share guests) are not members.

## In the product

- [Managing Workspace Membership](https://www.altium.com/documentation/altium-365/managing-workspace-membership#workspace_members) (primary)
- [Inviting other Users to Your Workspace](https://www.altium.com/documentation/altium-365/inviting-users)
- Term: **Workspace member** (exact; altium-365)

## In the API

- Platform API type: [`DesWorkspaceUser`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWorkspaceUser/) (object)

## GRID

`grid:workspace:{workspace-id}:team:user/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [system_SdmSystemModelVersionMetadata](system_SdmSystemModelVersionMetadata.md): `createdBy`
