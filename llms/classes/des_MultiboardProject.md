# Multiboard Project (des_MultiboardProject)

- Name: `des_MultiboardProject`
- IRI: `des:MultiboardProject` (https://w3id.org/altium/cdm/design/MultiboardProject)
- Bounded context: [design](../design.md)
- Kind: Activity
- Is a: [des_Project](des_Project.md)
- HTML page: [classes/des_MultiboardProject/](../../classes/des_MultiboardProject/)

Multiboard Project represents the coordinated design of multiple interconnected PCB projects assembled into a single system, capturing both their logical interconnects and physical arrangements.

## Comments

- Multiboard Project serves as an aggregate that composes individual board Projects into a higher-level system entity, maintaining identity and traceability across design boundaries. It enables engineers to define harnesses, connectors, and mechanical fit at the system level, while preserving the autonomy of each board design, thus supporting codesign, simulation, and integration workflows across ECAD and MCAD domains.

## In the product

- [Designing with Multiple PCBs](https://www.altium.com/documentation/altium-designer/multi-board-design#structure_multi_board_design_project) (primary)

## In the API

- Platform API type: [`DesProject`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesProject/) (object)

## GRID

None declared (nearest ancestor `des_Project`: `grid:workspace:{workspace-id}:design:project/{id}`).

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| projects | [des_Project](des_Project.md) | * | The individual PCB projects that make up this Multiboard Project. | core_hasPart |  |
| releases | [des_ProjectRelease](des_ProjectRelease.md) | * | The release artifacts produced by this activity. | core_releases | [des_Project](des_Project.md) |
| usesParts | [lib_Part](lib_Part.md) | * | Parts used in this Activity | core_hasInput | [des_Project](des_Project.md) |
| usesComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Activity | core_hasInput | [des_Project](des_Project.md) |
| parameters | [des_ProjectParameter](des_ProjectParameter.md) | * |  |  | [des_Project](des_Project.md) |
| variants | [des_ProjectVariant](des_ProjectVariant.md) | * |  |  | [des_Project](des_Project.md) |
| partOfSolution | [plt_Solution](plt_Solution.md) | * |  | core_partOf | [plt_SolutionItem](plt_SolutionItem.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
