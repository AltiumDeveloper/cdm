# Device Status (ota_DeviceStatus)

- Name: `ota_DeviceStatus`
- IRI: `ota:DeviceStatus` (https://w3id.org/altium/cdm/ota/DeviceStatus)
- Kind: enumeration
- HTML page: [enums/ota_DeviceStatus/](../../enums/ota_DeviceStatus/)

The OTA update status of a device.

## Values

| Value | Description |
| --- | --- |
| `NotSeen` | The device has not connected to the platform yet. |
| `Error` | The last update reported an error. |
| `UpToDate` | The installed software matches the assigned software. |
| `UpdatePending` | An update is assigned and waits to be delivered. |
| `Outdated` | The installed software differs from the assigned software. |
| `UpdateScheduled` | An update is scheduled for a future date and time. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_Device](../classes/ota_Device.md) | status | 0..1 |  |
