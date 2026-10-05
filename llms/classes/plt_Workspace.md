# Workspace (plt_Workspace)

- Name: `plt_Workspace`
- IRI: `plt:Workspace` (https://w3id.org/altium/cdm/platform/Workspace)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_Workspace/](../../classes/plt_Workspace/)

The top-level entity that plays a role of a closed environment for other entities (members, projects, components, etc.).

## Comments

- A Workspace belongs to exactly one realm (e.g. a commercial region such as Europe or US West, GovCloud, or a Single-Tenant Environment), and all of its data is stored and processed in that realm. This is a major data governance function of the workspaces.
- Typically an organization has a single workspace but large entirprises may have multiple.

## In the product

- [Altium 365 Workspace](https://www.altium.com/documentation/altium-365/workspace) (primary)
- [Activation & Management](https://www.altium.com/documentation/altium-365/workspace-activation-management)
- [Realms](https://www.altium.com/documentation/altium-developer-center/altium-365/key-concepts/realms)
- Term: **Altium 365 Workspace** (exact; altium-365)

## In the API

- Platform API type: [`DesWorkspace`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWorkspace/) (object)

## GRID

`grid:global::platform:workspace/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| environmentConfigurations | [con_EnvironmentConfiguration](con_EnvironmentConfiguration.md) | * |  | core_hasPart |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
