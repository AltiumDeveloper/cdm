# Application (plt_Application)

- Name: `plt_Application`
- IRI: `plt:Application` (https://w3id.org/altium/cdm/platform/Application)
- Bounded context: [platform](../platform.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/plt_Application/](../../classes/plt_Application/)

## In the API

- Platform API type: [`GloApp`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/GloApp/) (object)

## GRID

`grid:global::platform:application/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [system_SdmAuthoringApplication](system_SdmAuthoringApplication.md): `applicationId`
