# Software Project (sft_SoftwareProject)

- Name: `sft_SoftwareProject`
- IRI: `sft:SoftwareProject` (https://w3id.org/altium/cdm/software/SoftwareProject)
- Bounded context: [software](../software.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Mixins: [plt_SolutionItem](plt_SolutionItem.md)
- HTML page: [classes/sft_SoftwareProject/](../../classes/sft_SoftwareProject/)

The software part of a Renesas 365 solution, developed in the built-in Web IDE (based on the Theia framework) or in e² studio; it can also be created with an external repository type. In the solution's ESD document it can be linked to a software blanket, and generating a board support package (BSP) from that blanket pushes the SDM and applies the changes to the linked project, creating the project first if none exists yet.

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#exploring_a_solution) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#generating_a_board_support_package)

## In the API

- Platform API type: [`SftSoftwareProject`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SftSoftwareProject/) (object)

## GRID

`grid:workspace:{workspace-id}:software:software-project/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [sft_SoftwareRelease](sft_SoftwareRelease.md) | * | The release artifacts produced by this activity. | core_releases |  |
| aiModels | [sft_AIModel](sft_AIModel.md) | 0..1 |  | core_hasInput |  |
| deviceConfiguration | [sft_DeviceConfiguration](sft_DeviceConfiguration.md) | 0..1 | Device Configuration derived from the project | core_hasOutput |  |
| latestBuildArtifacts | [sft_BuildArtifact](sft_BuildArtifact.md) | * | Latest build artifacts produced from the project | core_hasOutput |  |
| partOfSolution | [plt_Solution](plt_Solution.md) | * |  | core_partOf | [plt_SolutionItem](plt_SolutionItem.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_FunctionalBlock](system_FunctionalBlock.md) | implementedBy | 0..1 | core_implementedBy |
| [system_SdmSoftwareModel](system_SdmSoftwareModel.md) | implementedBy | 0..1 | core_implementedBy |
| [system_SoftwareProject](system_SoftwareProject.md) | implementedBy | 0..1 | core_implementedBy |
