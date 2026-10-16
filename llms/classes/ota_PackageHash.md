# Package Hash (ota_PackageHash)

- Name: `ota_PackageHash`
- IRI: `ota:PackageHash` (https://w3id.org/altium/cdm/ota/PackageHash)
- Bounded context: [ota](../ota.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/ota_PackageHash/](../../classes/ota_PackageHash/)

Package Hash is a checksum of a package binary, used for Uptane target metadata.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| algorithm | string | 1 | The lowercase hash algorithm identifier, for example sha256 or sha512. |  |  |
| value | string | 1 | The hash value encoded as hexadecimal characters. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_Package](ota_Package.md) | hashes | * |  |
