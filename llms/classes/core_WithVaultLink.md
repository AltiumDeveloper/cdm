# With Vault Link (core_WithVaultLink)

- Name: `core_WithVaultLink`
- IRI: `core:WithVaultLink` (https://w3id.org/altium/cdm/core/WithVaultLink)
- Bounded context: [core](../core.md)
- Kind: mixin
- Is a: [core_Meta](core_Meta.md)
- HTML page: [classes/core_WithVaultLink/](../../classes/core_WithVaultLink/)

Mixin that adds vault link parent, child, and type annotation slots for tracking hierarchical vault relationships.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| vaultLinkParent | uriorcurie | 0..1 | Vault Link Parent |  |  |
| vaultLinkChild | uriorcurie | 0..1 | Vault Link Parent |  |  |
| vaultLinkType | string | 0..1 | Vault Link Parent |  |  |
