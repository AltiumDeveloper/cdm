# Device (ota_Device)

- Name: `ota_Device`
- IRI: `ota:Device` (https://w3id.org/altium/cdm/ota/Device)
- Bounded context: [ota](../ota.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_Device/](../../classes/ota_Device/)

## GRID

`grid:workspace:{workspace-id}:ota:device/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 0..1 | A short name of the entity. |  |  |
| fleets | [ota_Fleet](ota_Fleet.md) | * | Fleets this device belongs to |  |  |
| deviceId | string | 0..1 | External device identifier (e.g. Torizon deviceId) |  |  |
| hardwareId | string | 0..1 | Hardware identifier indicating device type/model |  |  |
| hibernated | boolean | 0..1 | Whether the device is in hibernation (from Torizon DeviceInfoBasic.hibernated) |  |  |
| status | [ota_DeviceStatus](../enums/ota_DeviceStatus.md) | 0..1 | Current device status |  |  |
| packages | [ota_Package](ota_Package.md) | * | Installed packages, if known |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_Fleet](ota_Fleet.md) | devices | * |  |
