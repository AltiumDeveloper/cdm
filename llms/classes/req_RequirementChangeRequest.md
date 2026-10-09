# Requirement Change Request (req_RequirementChangeRequest)

- Name: `req_RequirementChangeRequest`
- IRI: `req:RequirementChangeRequest` (https://w3id.org/altium/cdm/requirement/RequirementChangeRequest)
- Bounded context: [requirements](../requirements.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_RequirementChangeRequest/](../../classes/req_RequirementChangeRequest/)

Structured workflow item proposing additions, updates, or removals of requirements.

## GRID

`grid:workspace:{workspace-id}:requirements:change-request/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| reason | string | 1 | Business, technical, or compliance driver motivating the change. |  |  |
| priority | string | 0..1 | Handling urgency for backlog triage. |  |  |
| decision | string | 0..1 | Outcome such as approved, rejected, or deferred. |  |  |
| impactsRequirements | [req_Requirement](req_Requirement.md) | 1..* | Requirements directly impacted by the change request. |  |  |
| impactsSpecifications | [req_RequirementSpecification](req_RequirementSpecification.md) | * | Specifications that must be updated when processing the change. |  |  |
| generatesRevisions | [req_RequirementRevision](req_RequirementRevision.md) | * | Requirement revisions produced as the outcome of the change request. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [req_Project](req_Project.md) | changeRequests | * |  |
| [req_RequirementRevision](req_RequirementRevision.md) | derivesFromChange | 0..1 |  |
| [req_VerificationCase](req_VerificationCase.md) | triggersChanges | * |  |
