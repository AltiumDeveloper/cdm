# Project Template (des_ProjectTemplate)

- Name: `des_ProjectTemplate`
- IRI: `des:ProjectTemplate` (https://w3id.org/altium/cdm/design/ProjectTemplate)
- Bounded context: [design](../design.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/des_ProjectTemplate/](../../classes/des_ProjectTemplate/)

A reusable starting point for new design projects that bundles the documents, files and project settings a team wants to apply again and again. A project created from a template receives the template's documents and its project options.

## Comments

- Besides the usual project documents, a template may carry reference documentation, configuration files and Output Jobs, together with agreed project and document settings such as design rules, parameters, title blocks and release options.
- Templates are available for PCB, multi-board and harness projects. A Workspace project template is kept as a series of revisions; saving an edited template creates its next revision, and new projects are based on the latest revisions shared with the user.

## In the product

- [Creating a Project Template](https://www.altium.com/documentation/altium-designer/creating-project-template) (primary)

## In the API

- Platform API type: [`DesProjectTemplate`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesProjectTemplate/) (object)

## GRID

`grid:workspace:{workspace-id}:design:project-template/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [des_ProjectTemplateRevision](des_ProjectTemplateRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
