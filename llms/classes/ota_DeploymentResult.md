# Deployment Result (ota_DeploymentResult)

- Name: `ota_DeploymentResult`
- IRI: `ota:DeploymentResult` (https://w3id.org/altium/cdm/ota/DeploymentResult)
- Bounded context: [ota](../ota.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_DeploymentResult/](../../classes/ota_DeploymentResult/)

Deployment Result is the outcome of a deployment on one target device, from the time the device is addressed by the deployment, before its update is created. It is kept apart from the deployment, which records the request: the request is fixed when it is created, while the result is updated from the reports of the device as the update progresses. A device deployment has one result; a fleet deployment has one result per device of the fleet.

## GRID

`grid:workspace:{workspace-id}:ota:deployment-result/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| deployment | [ota_Deployment](ota_Deployment.md) | 1 | The deployment whose outcome this result records, referenced by its GRID. | core_outputOf |  |
| device | [ota_Device](ota_Device.md) | 1 | The target device the result applies to, referenced by its GRID. |  |  |
| status | [ota_DeploymentStatus](../enums/ota_DeploymentStatus.md) | 0..1 | The status of the deployment on the device. |  |  |
| completedAt | datetime | 0..1 | The date and time the deployment finished on the device, in UTC. |  |  |
| isSuccessful | boolean | 0..1 | Indicates whether the deployment on the device succeeded, once reported. |  |  |
| resultCode | string | 0..1 | The result code reported by the device. |  |  |
| resultDescription | string | 0..1 | The human-readable result reported by the device. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
