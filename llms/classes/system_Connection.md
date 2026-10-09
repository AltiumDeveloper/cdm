# Connection (system_Connection)

- Name: `system_Connection`
- IRI: `sys:Connection` (https://w3id.org/altium/cdm/system/Connection)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_Connection/](../../classes/system_Connection/)

A connection line in an ESD document representing an interconnection between functional blocks (e.g. signals passed between the interfaces of two devices), drawn directly between blocks or between their ports. In the editor a line can also start or end on other objects or in free space; this model records each end as a functional block and port (see system_Endpoint).

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#connecting_functional_blocks) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#defining_an_esd_document)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| endpoints | [system_Endpoint](system_Endpoint.md) | 1..* |  |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_ESDDocument](system_ESDDocument.md) | connections | * |  |
