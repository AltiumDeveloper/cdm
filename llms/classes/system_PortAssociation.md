# Port Association (system_PortAssociation)

- Name: `system_PortAssociation`
- IRI: `sys:PortAssociation` (https://w3id.org/altium/cdm/system/PortAssociation)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_PortAssociation/](../../classes/system_PortAssociation/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| portId | [system_Port](system_Port.md) | 1 |  |  |  |
| softwareComponentId | [system_SoftwareComponent](system_SoftwareComponent.md) | 1 |  |  |  |
| portLibraryName | [system_PortType](../enums/system_PortType.md) | 1 |  |  |  |

## Referenced by

- [system_FunctionalBlock](system_FunctionalBlock.md): `portsAssociations`
- [system_Port](system_Port.md): `associationId`
- [system_SoftwareComponent](system_SoftwareComponent.md): `portsAssociationsIds`
