# Requirements Project (req_Project)

- Name: `req_Project`
- IRI: `req:Project` (https://w3id.org/altium/cdm/requirement/Project)
- Bounded context: [requirements](../requirements.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_Project/](../../classes/req_Project/)

The orchestration space for capturing, evolving, and validating requirements scoped to a product, program increment, or regulatory engagement.

## Comments

- Provides planning scaffolding comparable to Hardware Projects, enabling traceable alignment between requirement deliverables and downstream design artifacts.
- The product already links requirements projects to design projects, through blocks of the Electronics type that are linked to PCB projects (e.g. choosing PCB projects when creating a requirements project creates a linked block and a specification for each); cross-domain slots for this link are not modelled yet. Future idea: synchronize milestone states via baselines vs. releases.

## In the product

- [Project Module](https://www.altium.com/documentation/altium-365/requirements-portal/project-module#creating_a_new_requirements_project) (primary)
- [Working with Requirements](https://www.altium.com/documentation/altium-365/requirements-integration#basic_requirements_portal_setup)
- [Working with Requirements](https://www.altium.com/documentation/altium-365/requirements-integration#linking_requirements_to_a_design_project)

## GRID

`grid:workspace:{workspace-id}:requirements:project/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | Compact display name for the requirement effort. |  |  |
| description | string | 0..1 | Longer narrative describing objectives, scope, and constraints. |  |  |
| owner | string | 0..1 | Responsible program, platform team, or external stakeholder. |  |  |
| specifications | [req_RequirementSpecification](req_RequirementSpecification.md) | 1..* | Specifications authored or curated within this requirements project. | core_hasPart |  |
| baselines | [req_RequirementBaseline](req_RequirementBaseline.md) | * | Baselines approved under this project to govern execution. | core_hasPart |  |
| changeRequests | [req_RequirementChangeRequest](req_RequirementChangeRequest.md) | * | Change requests logged against this requirements project. |  |  |
| verificationCases | [req_VerificationCase](req_VerificationCase.md) | * | Verification cases scoped to this project for coverage planning. |  |  |
| artifacts | [req_Artifact](req_Artifact.md) | * | Supporting artifacts (models, audits, customer inputs) managed by the project. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [req_RequirementSpecification](req_RequirementSpecification.md) | targetsProjects | * |  |
