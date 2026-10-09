# Solution (plt_Solution)

- Name: `plt_Solution`
- IRI: `plt:Solution` (https://w3id.org/altium/cdm/platform/Solution)
- Bounded context: [platform](../platform.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/plt_Solution/](../../classes/plt_Solution/)

A Renesas 365 solution: the main, top-level object of a Renesas 365 Workspace, which brings together the system design (an ESD document), PCB projects and software projects of one system. System designs and software projects both push their changes to the solution's System Data Model (SDM) and pull from it; Altium Designer can open a solution's PCB projects and pull SDM changes into them.

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365) (primary)
- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions)
- Term: **Renesas 365 solution** (exact; altium-365, altium-designer)

## In the API

- Platform API type: [`SolSolution`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SolSolution/) (object)

## GRID

`grid:workspace:{workspace-id}:platform:solution/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [plt_SolutionRelease](plt_SolutionRelease.md) | * | The release artifacts produced by this activity. | core_releases |  |
| solutionItems | [plt_SolutionItem](plt_SolutionItem.md) | * |  | core_hasPart |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [plt_SolutionItem](plt_SolutionItem.md) | partOfSolution | * | core_partOf |
