# Requirement Specification (req_RequirementSpecification)

- Name: `req_RequirementSpecification`
- IRI: `req:RequirementSpecification` (https://w3id.org/altium/cdm/requirement/RequirementSpecification)
- Bounded context: [requirements](../requirements.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_RequirementSpecification/](../../classes/req_RequirementSpecification/)

A curated collection of requirements scoped to a program, domain, or release horizon.

## In the product

- [Create Specifications](https://www.altium.com/documentation/altium-365/requirements-portal/requirements-module/create-specifications) (primary)
- Term: **Specification** (exact; altium-365)

## GRID

`grid:workspace:{workspace-id}:requirements:specification/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [req_RequirementBaseline](req_RequirementBaseline.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| name | string | 1 | Human-readable name for the specification (e.g. "System Requirements"). |  |  |
| description | string | 0..1 | Narrative describing the boundaries and context of the specification. |  |  |
| owner | string | 0..1 | Role or organization managing this specification. |  |  |
| includesRequirements | [req_Requirement](req_Requirement.md) | 1..* | Requirements curated under this specification. | core_hasPart |  |
| targetsProjects | [req_Project](req_Project.md) | * | Requirements projects that receive scope from this specification. |  |  |
| inputs | [req_Artifact](req_Artifact.md) | * | Artifacts or agreements that feed this specification. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [req_Project](req_Project.md): `specifications`
- [req_RequirementBaseline](req_RequirementBaseline.md): `ofSpecification`
- [req_RequirementChangeRequest](req_RequirementChangeRequest.md): `impactsSpecifications`
