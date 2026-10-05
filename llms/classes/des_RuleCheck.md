# Rule Check (des_RuleCheck)

- Name: `des_RuleCheck`
- IRI: `des:RuleCheck` (https://w3id.org/altium/cdm/design/RuleCheck)
- Bounded context: [design](../design.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_RuleCheck/](../../classes/des_RuleCheck/)

Rule check definitions that can be executed against a project to validate design integrity and compliance with specified constraints.

## In the API

- Platform API type: [`RuleCheck`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/RuleCheck/) (object)

## GRID

`grid:workspace:{workspace-id}:design:rule-check/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
