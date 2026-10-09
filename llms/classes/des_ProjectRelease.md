# Hardware Project Release (des_ProjectRelease)

- Name: `des_ProjectRelease`
- IRI: `des:ProjectRelease` (https://w3id.org/altium/cdm/design/ProjectRelease)
- Bounded context: [design](../design.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- HTML page: [classes/des_ProjectRelease/](../../classes/des_ProjectRelease/)

Project Release captures an immutable snapshot of a PCB design project at a specific point in its lifecycle, packaging all design data, outputs, and metadata required for manufacturing, assembly, and downstream processes.

## Comments

- Project Release serves as the authoritative artifact that bridges design and production, ensuring repeatability, traceability, and regulatory compliance. Its identity is tied to the originating Project but remains stable as a versioned deliverable, enabling teams to collaborate confidently, audit changes, and integrate with supply chain and PLM systems through Altium 365 and related workflows.

## In the product

- [Design Project Release](https://www.altium.com/documentation/altium-designer/preparing-for-manufacture/design-release) (primary)
- [Releasing to a Workspace](https://www.altium.com/documentation/altium-designer/preparing-for-manufacture/design-release/workspace)
- Term: **design project release** (related; altium-designer)

## In the API

- Platform API type: [`DesRelease`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesRelease/) (object)

## GRID

`grid:workspace:{workspace-id}:design:project-release/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| consistsOfComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Artifact | core_hasPart |  |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_ManufacturingPackage](des_ManufacturingPackage.md) | projectRelease | 1 | core_derivedFrom |
| [des_Project](des_Project.md) | releases | * | core_releases |
| [ins_PartInsight](ins_PartInsight.md) | occursIn | * | core_occursIn |
| [req_RequirementBaseline](req_RequirementBaseline.md) | targetsProjectReleases | * |  |
