# Connection (system_SdmConnection)

- Name: `system_SdmConnection`
- IRI: `sys:SdmConnection` (https://w3id.org/altium/cdm/system/SdmConnection)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_SdmMappableEntity](system_SdmMappableEntity.md)
- HTML page: [classes/system_SdmConnection/](../../classes/system_SdmConnection/)

Represents a connection between functional blocks.

## In the API

- Platform API type: [`SysSdmConnection`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmConnection/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| endpoints | [system_SdmEndpoint](system_SdmEndpoint.md) | * | Endpoints of the connection. |  |  |
| id | string | 1 | Local unique identifier within a given context. |  | [system_SdmMappableEntity](system_SdmMappableEntity.md) |

## Referenced by

- [system_SdmFunctionalModel](system_SdmFunctionalModel.md): `connections`
