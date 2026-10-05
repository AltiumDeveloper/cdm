# Workflow (cus_Workflow)

- Name: `cus_Workflow`
- IRI: `cus:Workflow` (https://w3id.org/altium/cdm/customization/Workflow)
- Bounded context: [customization](../customization.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- HTML page: [classes/cus_Workflow/](../../classes/cus_Workflow/)

A process workflow of an Altium 365 Workspace: the workflow that belongs to a process definition and steps designers through an everyday design process (e.g. requesting a new part, a design review or creating a new project). Workspace administrators build process definitions in the Process Workflow Editor, grouped by process theme (Part Requests, Project Activities, Project Creations), and activate them; each started instance of a process follows the workflow and creates tasks for the users whose action is needed to move it on.

## In the product

- [Processes & Workflows](https://www.altium.com/documentation/altium-365/processes-workflows) (primary)
- [Create & Manage Electronics Design Processes](https://www.altium.com/documentation/altium-365/creating-managing-processes)
- [Defining a Process Workflow](https://www.altium.com/documentation/altium-365/defining-process-workflow)
- Term: **Process Workflow** (exact; altium-365)
- Term: **Process Definition** (related; altium-365)

## In the API

- Platform API type: [`DesWorkflowDefinition`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesWorkflowDefinition/) (object)

## GRID

`grid:workspace:{workspace-id}:customization:workflow/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
