# Device Configuration Revision (sft_DeviceConfigurationRevision)

- Name: `sft_DeviceConfigurationRevision`
- IRI: `sft:DeviceConfigurationRevision` (https://w3id.org/altium/cdm/software/DeviceConfigurationRevision)
- Bounded context: [software](../software.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sft_DeviceConfigurationRevision/](../../classes/sft_DeviceConfigurationRevision/)

## In the API

- Platform API type: [`SftDevCfgDeviceConfigurationRevision`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/SftDevCfgDeviceConfigurationRevision/) (object)

## GRID

`grid:workspace:{workspace-id}:software:device-configuration-revision/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| pinModel | [sft_PinAssignmentModel](sft_PinAssignmentModel.md) | 1 |  |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [sft_DeviceConfiguration](sft_DeviceConfiguration.md) | revisions | * | core_revisions |
