# Domain Metadata (system_SdmClientMetadata)

- Name: `system_SdmClientMetadata`
- IRI: `sys:SdmClientMetadata` (https://w3id.org/altium/cdm/system/SdmClientMetadata)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SdmClientMetadata/](../../classes/system_SdmClientMetadata/)

Captures metadata specific to a particular client (e.g., ESD, AD, E2Studio).

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| clientId | string | 1 | The client identifier (e.g., "ESD", "AD", "E2Studio") this metadata are associated with. |  |  |
