# Software Stack Instance (system_SdmSoftwareStackInstance)

- Name: `system_SdmSoftwareStackInstance`
- IRI: `sys:SdmSoftwareStackInstance` (https://w3id.org/altium/cdm/system/SdmSoftwareStackInstance)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SdmSoftwareStackInstance/](../../classes/system_SdmSoftwareStackInstance/)

Represents a software stack instance and its dependencies.

## In the API

- Platform API type: [`SysSdmSoftwareStackInstance`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmSoftwareStackInstance/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| specification | [system_SdmSoftwareSpecification](system_SdmSoftwareSpecification.md) | 1 | The specification of this software stack instance. |  |  |
| dependencyIds | [system_SdmSoftwareStackInstance](system_SdmSoftwareStackInstance.md) | 1..* | The software stacks that this instance depends on. |  |  |
| peripheralInstanceId | [dm_PeripheralInstance](dm_PeripheralInstance.md) | 0..1 | The peripheral associated with this software stack. |  |  |

## Referenced by

- [system_SdmSoftwareComponent](system_SdmSoftwareComponent.md): `implementedBy`
- [system_SdmSoftwareModel](system_SdmSoftwareModel.md): `softwareStackInstances`
