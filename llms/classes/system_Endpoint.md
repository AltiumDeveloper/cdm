# Endpoint (system_Endpoint)

- Name: `system_Endpoint`
- IRI: `sys:Endpoint` (https://w3id.org/altium/cdm/system/Endpoint)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_Endpoint/](../../classes/system_Endpoint/)

One end of a connection in an ESD document, identified by the functional block and the port where the connection line starts or ends.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| functionalBlockId | [system_FunctionalBlock](system_FunctionalBlock.md) | 1 |  |  |  |
| portId | [system_Port](system_Port.md) | 1 |  |  |  |

## Referenced by

- [system_Connection](system_Connection.md): `endpoints`
