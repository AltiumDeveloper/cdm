# Software Project (sup_SoftwareProject)

- Name: `sup_SoftwareProject`
- IRI: `sup:SoftwareProject` (https://w3id.org/altium/cdm/supply/SoftwareProject)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_SoftwareProject/](../../classes/sup_SoftwareProject/)

A software project published in the supply catalog, together with the evaluation kits it is compatible with. In Renesas 365 it can be imported into a solution with a compatible eval kit; the import places the project in the Workspace and links it to the solution (see sft_SoftwareProject).

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#import_project) (primary)

## In the API

- Platform API type: [`SupSoftwareProject`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SupSoftwareProject/) (object)

## GRID

`grid:supply::platform:software-project/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| evalKits | [sup_EvalKit](sup_EvalKit.md) | * | Evaluation Kits included in this Artifact | core_hasPart |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [sup_SolutionTemplate](sup_SolutionTemplate.md): `softwareProjects`
