# Script Version (cus_ScriptVersion)

- Name: `cus_ScriptVersion`
- IRI: `cus:ScriptVersion` (https://w3id.org/altium/cdm/customization/ScriptVersion)
- Bounded context: [customization](../customization.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/cus_ScriptVersion/](../../classes/cus_ScriptVersion/)

## In the API

- Platform API type: [`GloScrScriptVersion`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloScrScriptVersion/) (object)

## GRID

`grid:workspace:{workspace-id}:scripts:script-version/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| executions | [cus_ScriptExecution](cus_ScriptExecution.md) | * | Script executions produced by this script version. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [cus_Script](cus_Script.md): `revisions`
