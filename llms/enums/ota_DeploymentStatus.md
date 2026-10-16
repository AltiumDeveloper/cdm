# ota_DeploymentStatus

- Name: `ota_DeploymentStatus`
- IRI: `ota:DeploymentStatus` (https://w3id.org/altium/cdm/ota/DeploymentStatus)
- Kind: enumeration
- HTML page: [enums/ota_DeploymentStatus/](../../enums/ota_DeploymentStatus/)

The status of a deployment on one target device, reported by its Deployment Result. Success or failure of a completed deployment is reported by the result's isSuccessful.

## Values

| Value | Description |
| --- | --- |
| `Pending` | The deployment is created and not yet received by the device. |
| `Scheduled` | The deployment is scheduled to start at a future date and time. |
| `InProgress` | The device has received the update instructions and is installing. |
| `Completed` | The deployment finished, either successfully or with a failure. A partially completed deployment, where only some ECUs installed successfully, is also Completed, with isSuccessful false. |
| `Cancelled` | The deployment was cancelled before it was received by the device. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_DeploymentResult](../classes/ota_DeploymentResult.md) | status | 0..1 |  |
