# Software Project (system_SoftwareProject)

- Name: `system_SoftwareProject`
- IRI: `sys:SoftwareProject` (https://w3id.org/altium/cdm/system/SoftwareProject)
- Bounded context: [system](../system.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SoftwareProject/](../../classes/system_SoftwareProject/)

An entry of an ESD document for a software project (sft_SoftwareProject) that implements part of the system, listing the software components that project covers. In the ESD editor a software project can be linked to a software blanket, and each project can be linked to at most one blanket in a document.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| implementedBy | [sft_SoftwareProject](sft_SoftwareProject.md) | 0..1 | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| softwareComponents | [system_SoftwareComponent](system_SoftwareComponent.md) | * | Software components associated with this software project. |  |  |

## Referenced by

- [system_ESDDocument](system_ESDDocument.md): `softwareProjects`
