# Solution Template (sup_SolutionTemplate)

- Name: `sup_SolutionTemplate`
- IRI: `sup:SolutionTemplate` (https://w3id.org/altium/cdm/supply/SolutionTemplate)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_SolutionTemplate/](../../classes/sup_SolutionTemplate/)

A publisher's template for a solution, held in the supply catalog. It brings together catalog software projects, evaluation kits and a system design (ESD) source, and users can clone it.

## In the API

- Platform API type: [`SupSolutionTemplate`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SupSolutionTemplate/) (object)

## GRID

`grid:supply::platform:solution-template/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| evalKits | [sup_EvalKit](sup_EvalKit.md) | * | Evaluation Kits included in this Artifact | core_hasPart |  |
| softwareProjects | [sup_SoftwareProject](sup_SoftwareProject.md) | * | Software Projects included in this Artifact | core_hasPart |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
