# dm_HasAddressRange

- Name: `dm_HasAddressRange`
- IRI: `dm:HasAddressRange` (https://w3id.org/altium/cdm/deviceModel/HasAddressRange)
- Bounded context: none
- Kind: abstract, mixin
- Is a: [core_Meta](core_Meta.md)
- HTML page: [classes/dm_HasAddressRange/](../../classes/dm_HasAddressRange/)

A mixin for entities that occupy a specific span of the memory map. It provides the foundational properties required for addressing and size-based feasibility checks.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| startAddress | integer | 1 | The base physical address of the memory region. |  |  |
| size | integer | 0..1 | The total span of the memory region in bytes. |  |  |
