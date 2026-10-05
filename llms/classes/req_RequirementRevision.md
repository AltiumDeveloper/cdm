# Requirement Revision (req_RequirementRevision)

- Name: `req_RequirementRevision`
- IRI: `req:RequirementRevision` (https://w3id.org/altium/cdm/requirement/RequirementRevision)
- Bounded context: [requirements](../requirements.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_HasLifecycle](plt_HasLifecycle.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_RequirementRevision/](../../classes/req_RequirementRevision/)

An immutable snapshot of a requirement statement at a specific revision.

## In the product

- [Requirement Versioning and Releasing](https://www.altium.com/documentation/altium-365/requirements-systems-portal/requirements-module/requirement-versioning-and-releasing) (primary)

## GRID

`grid:workspace:{workspace-id}:requirements:requirement-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisionOf | [req_Requirement](req_Requirement.md) | 1 | A versioned snapshot derived from a prior artifact version. | core_revisionOf |  |
| number | string | 1 | Ordinal or semver-like revision number. |  |  |
| changeSummary | string | 0..1 | Concise description of what changed in this revision. |  |  |
| derivesFromChange | [req_RequirementChangeRequest](req_RequirementChangeRequest.md) | 0..1 | Change request that authorized this requirement revision. |  |  |
| lifecycleState | [plt_LifecycleState](plt_LifecycleState.md) | 1 | The current lifecycle state assigned to this entity. |  | [plt_HasLifecycle](plt_HasLifecycle.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [req_Requirement](req_Requirement.md): `revisions`
- [req_RequirementChangeRequest](req_RequirementChangeRequest.md): `generatesRevisions`
