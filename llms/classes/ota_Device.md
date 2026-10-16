# Device (ota_Device)

- Name: `ota_Device`
- IRI: `ota:Device` (https://w3id.org/altium/cdm/ota/Device)
- Bounded context: [ota](../ota.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_Device/](../../classes/ota_Device/)

Device represents a physical unit registered for OTA updates. A device consists of one primary ECU and optional secondary ECUs, and may belong to fleets.

## GRID

`grid:workspace:{workspace-id}:ota:device/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| description | string | 0..1 | Free-form notes associated with the device. |  |  |
| deviceId | string | 0..1 | The device-side identifier provided at provisioning. |  |  |
| hardwareId | string | 0..1 | The hardware type of the device as a whole (for example the product or board type), as reported by the provider, when provided. |  |  |
| status | [ota_DeviceStatus](../enums/ota_DeviceStatus.md) | 0..1 | The current status of the device, set by the provider. |  |  |
| lastSeenAt | datetime | 0..1 | The date and time the device last connected, in UTC, set by the provider. |  |  |
| createdAt | datetime | 0..1 | The date and time the device was registered, in UTC, set by the provider. |  |  |
| activatedAt | datetime | 0..1 | The date and time the device first connected, in UTC, set by the provider. |  |  |
| lastUpdatedAt | datetime | 0..1 | The date and time the device was last updated, in UTC, set by the provider. |  |  |
| hibernated | boolean | 0..1 | Indicates whether the device is hibernated and excluded from updates. |  |  |
| packages | [ota_Package](ota_Package.md) | * | The registered packages installed on the device, when known, referenced by their GRID. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_Deployment](ota_Deployment.md) | targetDevice | 0..1 | core_occursIn |
| [ota_DeploymentResult](ota_DeploymentResult.md) | device | 1 |  |
| [ota_Fleet](ota_Fleet.md) | devices | * |  |
