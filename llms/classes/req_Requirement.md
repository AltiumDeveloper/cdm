# Requirement (req_Requirement)

- Name: `req_Requirement`
- IRI: `req:Requirement` (https://w3id.org/altium/cdm/requirement/Requirement)
- Bounded context: [requirements](../requirements.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_Requirement/](../../classes/req_Requirement/)

A single, testable statement of intent or constraint that governs a solution or process outcome.

## Comments

- Requirements aggregate rationales, acceptance criteria, and trace links needed to drive downstream design and verification.

## In the product

- [Requirement Fields](https://www.altium.com/documentation/altium-365/requirements-portal/requirements-module/requirement-fields) (primary)
- [Creating Requirements](https://www.altium.com/documentation/altium-365/requirements-portal/requirements-module/creating-requirements)
- [Requirements Breakdown Process](https://www.altium.com/documentation/altium-365/requirements-portal/requirements-module/requirements-breakdown-process)

## GRID

`grid:workspace:{workspace-id}:requirements:requirement/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [req_RequirementRevision](req_RequirementRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| identifier | string | 1 | Human-friendly identifier that is unique within a specification context (e.g. SYS-001). |  |  |
| title | string | 1 | Concise human-readable title of the requirement. |  |  |
| text | string | 1 | Canonical textual form of the requirement. |  |  |
| rationale | string | 0..1 | Justification or reasoning that motivates the requirement intent. |  |  |
| category | string | 0..1 | Classification such as functional, safety, regulatory, or usability. |  |  |
| priority | string | 0..1 | Relative importance or sequencing hint for planning. |  |  |
| acceptanceCriteria | string | * | Objective criteria or measurements that prove the requirement is met. |  |  |
| owner | string | 0..1 | Responsible role or team accountable for the requirement. |  |  |
| sourceReference | uriorcurie | * | Link or citation to originating contract, regulation, or customer input. |  |  |
| children | [req_Requirement](req_Requirement.md) | * | Requirements that refine or decompose this requirement. | core_hasPart |  |
| parent | [req_Requirement](req_Requirement.md) | 0..1 | Higher-level requirement that allocates scope to this requirement. | core_partOf |  |
| satisfiedByArtifacts | [req_Artifact](req_Artifact.md) | * | Artifacts, designs, or solutions that implement this requirement. |  |  |
| verifiedByActivities | [core_Activity](core_Activity.md) | * | Verification activities that produce evidence for this requirement. |  |  |
| tracedFromSources | [req_Artifact](req_Artifact.md) | * | Upstream sources such as contracts, standards, or customer requests. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [req_RequirementBaseline](req_RequirementBaseline.md): `includesRequirements`
- [req_RequirementChangeRequest](req_RequirementChangeRequest.md): `impactsRequirements`
- [req_RequirementRevision](req_RequirementRevision.md): `revisionOf`
- [req_RequirementSpecification](req_RequirementSpecification.md): `includesRequirements`
- [req_VerificationCase](req_VerificationCase.md): `validatesRequirements`
