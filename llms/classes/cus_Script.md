# Script (cus_Script)

- Name: `cus_Script`
- IRI: `cus:Script` (https://w3id.org/altium/cdm/customization/Script)
- Bounded context: [customization](../customization.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/cus_Script/](../../classes/cus_Script/)

## In the API

- Platform API type: [`GloScrScript`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloScrScript/) (object)

## GRID

`grid:workspace:{workspace-id}:scripts:script/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [cus_ScriptVersion](cus_ScriptVersion.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
