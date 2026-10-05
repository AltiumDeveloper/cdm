# Software Component (system_SdmSoftwareComponent)

- Name: `system_SdmSoftwareComponent`
- IRI: `sys:SdmSoftwareComponent` (https://w3id.org/altium/cdm/system/SdmSoftwareComponent)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Mixins: [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md)
- HTML page: [classes/system_SdmSoftwareComponent/](../../classes/system_SdmSoftwareComponent/)

Represents a software component instance and its dependencies.

## In the API

- Platform API type: [`SysSdmSoftwareComponent`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmSoftwareComponent/) (object)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| implementedBy | [system_SdmSoftwareStackInstance](system_SdmSoftwareStackInstance.md) | * | This activity is implemented by another activity (e.g. a requirement implemented by a design). | core_implementedBy |  |
| id | string | 1 | Local unique identifier within a given context. |  |  |
| name | string | 0..1 | A short name of the entity. |  |  |
| parameters | [system_Parameter](system_Parameter.md) | * |  |  |  |
| libraryComponentId | string | 0..1 | The id of the library software component |  |  |
| sdmReferenceDesignator | string | 1 | Reference designator |  | [system_HasSdmReferenceDesignator](system_HasSdmReferenceDesignator.md) |

## Referenced by

- [system_SdmPort](system_SdmPort.md): `softwareComponentId`
- [system_SdmSoftwareModel](system_SdmSoftwareModel.md): `softwareComponents`
