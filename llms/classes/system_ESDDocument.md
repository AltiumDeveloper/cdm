# ESD Document (system_ESDDocument)

- Name: `system_ESDDocument`
- IRI: `sys:ESDDocument` (https://w3id.org/altium/cdm/system/ESDDocument)
- Bounded context: [system](../system.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Mixins: [plt_SolutionItem](plt_SolutionItem.md)
- HTML page: [classes/system_ESDDocument/](../../classes/system_ESDDocument/)

A system-level block diagram document used in a Renesas 365 solution (listed there as a System Design project) to describe the architecture of the system at a functional level. It holds functional blocks with their hardware components, software components and ports, the connections between blocks, and blankets through which parts of the design can be linked to PCB or software projects. Pushing to and pulling from the solution's System Data Model (SDM) for the system design is done from the ESD document. Blankets are not modelled as a separate entity here (see MF-068).

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd) (primary)
- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#exploring_a_solution)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#pushing_pulling_sdm)
- Term: **System Design** (related; altium-365)

## In the API

- Platform API type: [`SysEsdDocument`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysEsdDocument/) (object)

## GRID

`grid:workspace:{workspace-id}:system-design:esd/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| functionalBlocks | [system_FunctionalBlock](system_FunctionalBlock.md) | * |  |  |  |
| connections | [system_Connection](system_Connection.md) | * |  |  |  |
| hardwareProjects | [system_HardwareProject](system_HardwareProject.md) | * | Hardware projects associated with this ESD document. |  |  |
| softwareProjects | [system_SoftwareProject](system_SoftwareProject.md) | * | Software projects associated with this ESD document. |  |  |
| partOfSolution | [plt_Solution](plt_Solution.md) | * |  | core_partOf | [plt_SolutionItem](plt_SolutionItem.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmFunctionalModel](system_SdmFunctionalModel.md) | implementedBy | 0..1 | core_implementedBy |
