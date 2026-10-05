# Bounded context: customization

Models ways to customize and automate a Workspace: process workflows, and scripts with their versions, their executions and the event raised when an execution completes. In the product, each workflow belongs to a process definition that a Workspace administrator creates and manages in the Workspace browser interface.

HTML page: [subsets/customization/](../subsets/customization/)

## In the product

- [Processes & Workflows](https://www.altium.com/documentation/altium-365/processes-workflows) (primary)
- [Altium 365 API](https://www.altium.com/documentation/altium-developer-center/altium-365/api#how_the_api_is_organized)

## Classes

- [Script](classes/cus_Script.md) (`cus_Script`): Artifact · API GloScrScript · GRID `grid:workspace:{workspace-id}:scripts:script/{id}`
- [Script Execution](classes/cus_ScriptExecution.md) (`cus_ScriptExecution`): Artifact · API GloScrScriptExecution · GRID `grid:workspace:{workspace-id}:scripts:script-execution/{id}`
- [Script Execution Completed](classes/cus_ScriptExecutionCompleted.md) (`cus_ScriptExecutionCompleted`): Event
- [Script Version](classes/cus_ScriptVersion.md) (`cus_ScriptVersion`): Artifact · API GloScrScriptVersion · GRID `grid:workspace:{workspace-id}:scripts:script-version/{id}`
- [Workflow](classes/cus_Workflow.md) (`cus_Workflow`): A process workflow of an Altium 365 Workspace: the workflow that belongs to a process definition and steps designers through an everyday design process (e.g. requesting a new part, a design review or creating a new project). · Activity · API DesWorkflowDefinition · GRID `grid:workspace:{workspace-id}:customization:workflow/{id}`
