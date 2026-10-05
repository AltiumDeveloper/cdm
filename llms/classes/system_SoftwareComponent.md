# Software Component (system_SoftwareComponent)

- Name: `system_SoftwareComponent`
- IRI: `sys:SoftwareComponent` (https://w3id.org/altium/cdm/system/SoftwareComponent)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SoftwareComponent/](../../classes/system_SoftwareComponent/)

Functional in nature, abstracted from but connected to logical implementation.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#software_component) (primary)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| parentKeyComponentId | [system_KeyComponent](system_KeyComponent.md) | 1 |  |  |  |
| portsAssociationsIds | [system_PortAssociation](system_PortAssociation.md) | * |  |  |  |

## Referenced by

- [system_FunctionalBlock](system_FunctionalBlock.md): `softwareComponents`
- [system_KeyComponent](system_KeyComponent.md): `childSoftwareComponentsIds`
- [system_PortAssociation](system_PortAssociation.md): `softwareComponentId`
- [system_SoftwareProject](system_SoftwareProject.md): `softwareComponents`
