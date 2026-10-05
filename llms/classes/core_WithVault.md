# With Vault (core_WithVault)

- Name: `core_WithVault`
- IRI: `core:WithVault` (https://w3id.org/altium/cdm/core/WithVault)
- Bounded context: [core](../core.md)
- Kind: mixin
- Is a: [core_Meta](core_Meta.md)
- HTML page: [classes/core_WithVault/](../../classes/core_WithVault/)

Mixin that adds a vault content type annotation to a class, indicating how its content is stored in the platform vault.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| contentType | [VaultContentType](../enums/VaultContentType.md) | 0..1 | Vault Content Type |  |  |
