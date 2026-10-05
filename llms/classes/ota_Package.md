# Package (ota_Package)

- Name: `ota_Package`
- IRI: `ota:Package` (https://w3id.org/altium/cdm/ota/Package)
- Bounded context: [ota](../ota.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_Package/](../../classes/ota_Package/)

## GRID

`grid:workspace:{workspace-id}:ota:package/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| version | string | 0..1 | Package version |  |  |
| size | integer | 0..1 | Package size in bytes. |  |  |
| hashes | string | 0..1 | Package checksums as a JSON string map (e.g. {"sha256":"..."}), matching Torizon Package.hashes. |  |  |
| hardwareIds | string | * | Hardware identifiers this package targets. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [ota_Device](ota_Device.md): `packages`
