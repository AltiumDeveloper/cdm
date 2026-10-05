# Endpoint (system_SdmEndpoint)

- Name: `system_SdmEndpoint`
- IRI: `sys:SdmEndpoint` (https://w3id.org/altium/cdm/system/SdmEndpoint)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SdmEndpoint/](../../classes/system_SdmEndpoint/)

Represents an endpoint of a connection.

## In the API

- Platform API type: [`SysSdmEndpoint`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmEndpoint/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| functionalBlockId | [system_SdmFunctionalBlock](system_SdmFunctionalBlock.md) | 1 | Functional block associated with this endpoint. |  |  |
| portId | [system_SdmPort](system_SdmPort.md) | 1 | Port associated with this endpoint. |  |  |

## Referenced by

- [system_SdmConnection](system_SdmConnection.md): `endpoints`
