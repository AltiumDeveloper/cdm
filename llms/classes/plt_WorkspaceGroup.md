# Workspace Group (plt_WorkspaceGroup)

- Name: `plt_WorkspaceGroup`
- IRI: `plt:WorkspaceGroup` (https://w3id.org/altium/cdm/platform/WorkspaceGroup)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_WorkspaceGroup/](../../classes/plt_WorkspaceGroup/)

Workspace Group represents a logical collection of users within a workspace, used to manage access control, permissions, and collaboration roles across projects and data assets.

## Comments

- Each Workspace Group has its own identity and membership, defining collective rights and responsibilities for its members.
- It simplifies administration and governance by enabling consistent permission management and role-based access across Altium 365 projects, libraries, and shared resources.

## In the product

- [Managing Workspace Membership](https://www.altium.com/documentation/altium-365/managing-workspace-membership#admin_groups) (primary)

## In the API

- Platform API type: [`DesWorkspaceGroup`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWorkspaceGroup/) (object)

## GRID

`grid:workspace:{workspace-id}:team:group/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
