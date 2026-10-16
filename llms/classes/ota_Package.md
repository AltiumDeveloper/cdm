# Package (ota_Package)

- Name: `ota_Package`
- IRI: `ota:Package` (https://w3id.org/altium/cdm/ota/Package)
- Bounded context: [ota](../ota.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_Package/](../../classes/ota_Package/)

Package represents one version of a software package registered for OTA deployment. A package is identified by its name and version; the version list of a package is the set of packages sharing the same name.

## GRID

`grid:workspace:{workspace-id}:ota:package/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The package name. |  |  |
| description | string | 0..1 | A brief description of the entity. |  |  |
| version | string | 1 | The version identifier assigned to this package. |  |  |
| size | integer | 0..1 | The size of the package binary in bytes. |  |  |
| hashes | [ota_PackageHash](ota_PackageHash.md) | * | The checksums of the package binary. |  |  |
| hardwareIds | string | * | The hardware identifiers of the ECU types compatible with the package, matched against the hardware identifiers reported by the ECUs of the target devices. |  |  |
| createdAt | datetime | 0..1 | The date and time the package was registered, in UTC. |  |  |
| packageType | string | 0..1 | The package format reported by the provider, for example ostree or binary. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_DeploymentAssignment](ota_DeploymentAssignment.md) | package | 1 |  |
| [ota_Device](ota_Device.md) | packages | * |  |
