# Script Execution (cus_ScriptExecution)

- Name: `cus_ScriptExecution`
- IRI: `cus:ScriptExecution` (https://w3id.org/altium/cdm/customization/ScriptExecution)
- Bounded context: [customization](../customization.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/cus_ScriptExecution/](../../classes/cus_ScriptExecution/)

## In the API

- Platform API type: [`GloScrScriptExecution`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloScrScriptExecution/) (object)

## GRID

`grid:workspace:{workspace-id}:scripts:script-execution/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| emits | [cus_ScriptExecutionCompleted](cus_ScriptExecutionCompleted.md) | 0..1 |  |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [cus_ScriptVersion](cus_ScriptVersion.md): `executions`
