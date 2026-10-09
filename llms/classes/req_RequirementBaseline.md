# Requirement Baseline (req_RequirementBaseline)

- Name: `req_RequirementBaseline`
- IRI: `req:RequirementBaseline` (https://w3id.org/altium/cdm/requirement/RequirementBaseline)
- Bounded context: [requirements](../requirements.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_RequirementBaseline/](../../classes/req_RequirementBaseline/)

A version-managed release of a specification or subset of requirements approved for execution. In the product this corresponds to a released specification (Release Specification). It is not what the product calls a baseline: in the Requirements & Systems Portal (Legacy), a baseline is a named bookmark for a point in time (e.g. a design review) that is used to compare how requirements and values have changed.

## In the product

- [Requirement Versioning and Releasing](https://www.altium.com/documentation/altium-365/requirements-systems-portal/requirements-module/requirement-versioning-and-releasing) (primary)
- Term: **Release Specification** (related; altium-365)

## GRID

`grid:workspace:{workspace-id}:requirements:baseline/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| identifier | string | 1 | Distinguishing label for the approved baseline (e.g. BL-2025.1). |  |  |
| notes | string | 0..1 | Additional context for the approval, deviations, or applicability limits. |  |  |
| ofSpecification | [req_RequirementSpecification](req_RequirementSpecification.md) | 1 | Specification for which this baseline is approved. |  |  |
| includesRequirements | [req_Requirement](req_Requirement.md) | 1..* | Specific requirements frozen into this baseline. | core_hasPart |  |
| targetsProjectReleases | [des_ProjectRelease](des_ProjectRelease.md) | * | Project releases that must comply with this baseline. |  |  |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [req_Project](req_Project.md) | baselines | * | core_hasPart |
| [req_RequirementSpecification](req_RequirementSpecification.md) | revisions | * | core_revisions |
