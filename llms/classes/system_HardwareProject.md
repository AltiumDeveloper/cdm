# Hardware Project (system_HardwareProject)

- Name: `system_HardwareProject`
- IRI: `sys:HardwareProject` (https://w3id.org/altium/cdm/system/HardwareProject)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_HardwareProject/](../../classes/system_HardwareProject/)

An entry of an ESD document for a PCB design project (des_Project) that implements part of the system, listing the functional blocks that project covers. In the ESD editor a PCB project can be linked to a hardware blanket (which can be placed around functional blocks), and each project can be linked to at most one blanket in a document.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| implementedBy | [des_Project](des_Project.md) | 0..1 | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| functionalBlocks | [system_FunctionalBlock](system_FunctionalBlock.md) | * | Functional blocks associated with this hardware project. |  |  |

## Referenced by

- [system_ESDDocument](system_ESDDocument.md): `hardwareProjects`
