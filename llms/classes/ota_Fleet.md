# Fleet (ota_Fleet)

- Name: `ota_Fleet`
- IRI: `ota:Fleet` (https://w3id.org/altium/cdm/ota/Fleet)
- Bounded context: [ota](../ota.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_Fleet/](../../classes/ota_Fleet/)

## GRID

`grid:workspace:{workspace-id}:ota:fleet/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| devices | [ota_Device](ota_Device.md) | * | Devices in this fleet |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_Device](ota_Device.md) | fleets | * |  |
