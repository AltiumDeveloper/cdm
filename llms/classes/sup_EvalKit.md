# Evaluation Kit (sup_EvalKit)

- Name: `sup_EvalKit`
- IRI: `sup:EvalKit` (https://w3id.org/altium/cdm/supply/EvalKit)
- Bounded context: [supply](../supply.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sup_EvalKit/](../../classes/sup_EvalKit/)

A vendor evaluation kit in the supply catalog, described by its associated devices, its reference designs (including a main one) and the software projects compatible with it. In Renesas 365 an eval kit can be linked to a solution, and the browser can connect to the kit over J-Link.

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#linking_an_evaluation_kit) (primary)
- Term: **Eval Kit** (exact; altium-365)

## In the API

- Platform API type: [`SupEvalKit`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SupEvalKit/) (object)

## GRID

`grid:supply::platform:eval-kit/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [sup_SoftwareProject](sup_SoftwareProject.md): `evalKits`
- [sup_SolutionTemplate](sup_SolutionTemplate.md): `evalKits`
