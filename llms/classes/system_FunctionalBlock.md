# Functional Block (system_FunctionalBlock)

- Name: `system_FunctionalBlock`
- IRI: `sys:FunctionalBlock` (https://w3id.org/altium/cdm/system/FunctionalBlock)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_FunctionalBlock/](../../classes/system_FunctionalBlock/)

Represents a logical block within an ESD document (e.g., MCU subsystem, LED driver block) that stands for a function, operation or device of the system, including parameters, key components, software components, ports, and associations. In the ESD editor a functional block can also contain other blocks; this nesting is not modelled here.

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#defining_an_esd_document) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#placing_and_configuring_functional_blocks)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| implementedBy | [des_Project](des_Project.md) or [sft_SoftwareProject](sft_SoftwareProject.md) | 0..1 | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| ports | [system_Port](system_Port.md) | * |  |  |  |
| keyComponents | [system_KeyComponent](system_KeyComponent.md) | * |  |  |  |
| softwareComponents | [system_SoftwareComponent](system_SoftwareComponent.md) | * |  |  |  |
| portsAssociations | [system_PortAssociation](system_PortAssociation.md) | * |  |  |  |

## Referenced by

- [system_ESDDocument](system_ESDDocument.md): `functionalBlocks`
- [system_Endpoint](system_Endpoint.md): `functionalBlockId`
- [system_HardwareProject](system_HardwareProject.md): `functionalBlocks`
