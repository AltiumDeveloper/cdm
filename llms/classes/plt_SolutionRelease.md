# Solution Release (plt_SolutionRelease)

- Name: `plt_SolutionRelease`
- IRI: `plt:SolutionRelease` (https://w3id.org/altium/cdm/platform/SolutionRelease)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_SolutionRelease/](../../classes/plt_SolutionRelease/)

Release of the Solution. This is a formal immutable artifact, representing a specific state of the Solution at the time of release.

## In the product

- No public product documentation exists for this concept.

## GRID

`grid:workspace:{workspace-id}:platform:solution-release/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [plt_Solution](plt_Solution.md): `releases`
