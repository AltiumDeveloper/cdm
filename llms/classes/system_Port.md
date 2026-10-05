# Port (system_Port)

- Name: `system_Port`
- IRI: `sys:Port` (https://w3id.org/altium/cdm/system/Port)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_Port/](../../classes/system_Port/)

An interface of a functional block in an ESD document (e.g. the I2C interface of an MPU), placed inside the block's boundaries; connection lines between blocks can start and end at ports. It is a logical interface, distinct from dm_Port, which is a physical port of a device.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#defining_an_esd_document) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#port)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| associationId | [system_PortAssociation](system_PortAssociation.md) | 0..1 |  |  |  |

## Referenced by

- [system_Endpoint](system_Endpoint.md): `portId`
- [system_FunctionalBlock](system_FunctionalBlock.md): `ports`
- [system_PortAssociation](system_PortAssociation.md): `portId`
