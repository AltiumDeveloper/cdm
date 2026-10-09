# System Model Version (system_SdmSystemModelVersion)

- Name: `system_SdmSystemModelVersion`
- IRI: `sys:SystemModelVersion` (https://w3id.org/altium/cdm/system/SystemModelVersion)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/system_SdmSystemModelVersion/](../../classes/system_SdmSystemModelVersion/)

A specific version of a system model, capturing the state of the system design at a particular point in time.

## In the API

- Platform API type: [`SysSdmSystemModelVersion`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SysSdmSystemModelVersion/) (object)

## GRID

`grid:workspace:{workspace-id}:system-design:sdm-version/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| version | integer | 1 | Version of the system model, used for tracking changes over time. |  |  |
| schemaVersion | string | 0..1 | The semantic version of the SDM schema this model version conforms to, used for compatibility checks. |  |  |
| functionalModel | [system_SdmFunctionalModel](system_SdmFunctionalModel.md) | 0..1 | A functional model associated with the system model. |  |  |
| deviceModels | [system_SdmDeviceModel](system_SdmDeviceModel.md) | * | A device models associated with this system model. |  |  |
| softwareModels | [system_SdmSoftwareModel](system_SdmSoftwareModel.md) | * | A software models associated with this system model. |  |  |
| hardwareModels | [system_SdmHardwareModel](system_SdmHardwareModel.md) | * | A hardware models associated with this system model. |  |  |
| metadata | [system_SdmSystemModelVersionMetadata](system_SdmSystemModelVersionMetadata.md) | 0..1 | Metadata associated with this system model version. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmSystemModel](system_SdmSystemModel.md) | latestVersion | 1 |  |
| [system_SdmSystemModel](system_SdmSystemModel.md) | versions | * |  |
