# Hardware Project (des_Project)

- Name: `des_Project`
- IRI: `des:Project` (https://w3id.org/altium/cdm/design/Project)
- Bounded context: [design](../design.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Subclasses: [des_HarnessProject](des_HarnessProject.md), [des_MultiboardProject](des_MultiboardProject.md)
- Mixins: [plt_SolutionItem](plt_SolutionItem.md)
- HTML page: [classes/des_Project/](../../classes/des_Project/)

A design project stored in a Workspace, normally under its built-in version control, such as a PCB project. It groups the design documents that together define one implementation of a product, along with its project parameters and variants; it is the source from which releases are made and from which Managed BOMs can be created.

## In the product

- [Workspace Projects](https://www.altium.com/documentation/altium-365/workspace-projects) (primary)
- [Creating Projects and Documents](https://www.altium.com/documentation/altium-designer/creating-projects-documents)
- Term: **Workspace project** (exact; altium-365, altium-designer)
- Term: **design project** (related; altium-designer, altium-365)

## In the API

- Platform API type: [`DesProject`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesProject/) (object)

## GRID

`grid:workspace:{workspace-id}:design:project/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| releases | [des_ProjectRelease](des_ProjectRelease.md) | * | The release artifacts produced by this activity. | core_releases |  |
| usesParts | [lib_Part](lib_Part.md) | * | Parts used in this Activity | core_hasInput |  |
| usesComponents | [lib_ComponentRevision](lib_ComponentRevision.md) | * | Components used in this Activity | core_hasInput |  |
| parameters | [des_ProjectParameter](des_ProjectParameter.md) | * |  |  |  |
| variants | [des_ProjectVariant](des_ProjectVariant.md) | * |  |  |  |
| partOfSolution | [plt_Solution](plt_Solution.md) | * |  | core_partOf | [plt_SolutionItem](plt_SolutionItem.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_MultiboardProject](des_MultiboardProject.md) | projects | * | core_hasPart |
| [ins_PartInsight](ins_PartInsight.md) | informedBy | * | core_informedBy |
| [lib_ComponentRevision](lib_ComponentRevision.md) | usedByProjectVariant | * | core_inputOf |
| [system_FunctionalBlock](system_FunctionalBlock.md) | implementedBy | 0..1 | core_implementedBy |
| [system_HardwareProject](system_HardwareProject.md) | implementedBy | 0..1 | core_implementedBy |
| [system_SdmHardwareModel](system_SdmHardwareModel.md) | implementedBy | 0..1 | core_implementedBy |
