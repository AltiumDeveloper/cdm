# AI Model (sft_AIModel)

- Name: `sft_AIModel`
- IRI: `sft:AIModel` (https://w3id.org/altium/cdm/software/AIModel)
- Bounded context: [software](../software.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Mixins: [plt_SolutionItem](plt_SolutionItem.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/sft_AIModel/](../../classes/sft_AIModel/)

AI model artifact in context of a workspace

## Comments

- We start with a simple Artifact-like entity without explicit revisions support. The assumption is that if we need revisions going forward, we'll add explicit revision entity, define GRID for it, relations, etc.

## GRID

`grid:workspace:{workspace-id}:software:ai-model/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| partOfSolution | [plt_Solution](plt_Solution.md) | * |  | core_partOf | [plt_SolutionItem](plt_SolutionItem.md) |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [sft_SoftwareProject](sft_SoftwareProject.md) | aiModels | 0..1 | core_hasInput |
| [sft_SoftwareRelease](sft_SoftwareRelease.md) | aiModels | 0..1 | core_hasPart |
