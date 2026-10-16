# Design Review (des_DesignReview)

- Name: `des_DesignReview`
- IRI: `des:DesignReview` (https://w3id.org/altium/cdm/design/DesignReview)
- Bounded context: [design](../design.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/des_DesignReview/](../../classes/des_DesignReview/)

A structured assessment of a design project, carried out by assigned Reviewers on a fixed snapshot of its design and concluded by the Initiator's decision, which leaves a traceable record of the review.

## In the product

- [Design Reviews](https://www.altium.com/documentation/altium-365/project-design-reviews) (primary)

## GRID

`grid:workspace:{workspace-id}:design:design-review/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| project | [des_Project](des_Project.md) | 1 | The design project under review. | core_partOf |  |
| reviewContext | [des_ProjectRelease](des_ProjectRelease.md) | 0..1 | The project release under review, when the review context is a release. | core_occursIn |  |
| initiator | [plt_WorkspaceUser](plt_WorkspaceUser.md) | 1 | The Workspace member who created the review. |  |  |
| reviewers | [plt_WorkspaceUser](plt_WorkspaceUser.md) | * | The Workspace members asked to review the design. |  |  |
| workflow | [cus_Workflow](cus_Workflow.md) | 0..1 | The process workflow that the review follows: the built-in Design Review process or a custom design review process. | core_informedBy |  |
| tasks | [col_Task](col_Task.md) | * | Tasks of the review: the process tasks created for the Initiator and the Reviewers, and tasks raised from comments placed on the design snapshot. | core_informs |  |
| commentThreads | [col_CommentThread](col_CommentThread.md) | * | Comment threads placed on the design snapshot of the review, including those about checklist items. | core_hasPart |  |
| status | [des_DesignReviewStatus](../enums/des_DesignReviewStatus.md) | 1 | The state of the review, from In Progress to its closed state. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ins_DesignInsight](ins_DesignInsight.md) | designReview | 1 | core_partOf |
