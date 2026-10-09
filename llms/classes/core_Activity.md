# Activity (core_Activity)

- Name: `core_Activity`
- IRI: `core:Activity` (https://w3id.org/altium/cdm/core/Activity)
- Bounded context: [core](../core.md)
- Kind: Activity, abstract
- Is a: [core_Entity](core_Entity.md)
- Subclasses: [col_CommentThread](col_CommentThread.md), [col_Task](col_Task.md), [cus_Workflow](cus_Workflow.md), [des_Project](des_Project.md), [des_ProjectRelease](des_ProjectRelease.md), [des_RuleCheckExecution](des_RuleCheckExecution.md), [ins_Insight](ins_Insight.md), [lib_PartRequest](lib_PartRequest.md), [plt_Solution](plt_Solution.md), [pro_BomWIP](pro_BomWIP.md), [pro_GlobalBOM](pro_GlobalBOM.md), [req_Project](req_Project.md), [req_RequirementChangeRequest](req_RequirementChangeRequest.md), [req_VerificationCase](req_VerificationCase.md), [sft_SoftwareProject](sft_SoftwareProject.md), [system_ESDDocument](system_ESDDocument.md), [system_SdmSystemModel](system_SdmSystemModel.md)
- HTML page: [classes/core_Activity/](../../classes/core_Activity/)

Abstract base for process and work objects — things that happen, use inputs, and produce outputs. Examples: projects, releases, design workflows.

## In standards

- close: [prov:Activity](http://www.w3.org/ns/prov#Activity)
- related: [obo:BFO_0000015](http://purl.obolibrary.org/obo/BFO_0000015)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [req_Requirement](req_Requirement.md) | verifiedByActivities | * |  |
