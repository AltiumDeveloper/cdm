# Rule Check Execution (des_RuleCheckExecution)

- Name: `des_RuleCheckExecution`
- IRI: `des:RuleCheckExecution` (https://w3id.org/altium/cdm/design/RuleCheckExecution)
- Bounded context: [design](../design.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_RuleCheckExecution/](../../classes/des_RuleCheckExecution/)

Execution of a rule check against a project to validate design integrity and compliance with specified constraints.

## In the API

- Platform API type: [`RuleCheckExecution`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/RuleCheckExecution/) (object)

## GRID

`grid:workspace:{workspace-id}:design:rule-check-execution/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
