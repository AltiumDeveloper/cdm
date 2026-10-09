# Task (col_Task)

- Name: `col_Task`
- IRI: `col:Task` (https://w3id.org/altium/cdm/collaboration/Task)
- Bounded context: [collaboration](../collaboration.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/col_Task/](../../classes/col_Task/)

Task represents a discrete unit of work assigned to a user or team within the design workflow, used to track progress, responsibility, and completion status for design, review, or management activities.

## Comments

- Each Task has its own identity, state, and assignees, and may be linked to specific design objects, projects, or comments.
- It provides structure and accountability in collaborative design processes, supporting review cycles, issue resolution, and workflow coordination across teams within Altium 365.

## In the product

- [Working with Tasks](https://www.altium.com/documentation/altium-365/tasks) (primary)

## In the API

- Platform API type: [`DesTask`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesTask/) (object)

## GRID

`grid:workspace:{workspace-id}:collaboration:task/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ins_Insight](ins_Insight.md) | tasks | * | core_informs |
