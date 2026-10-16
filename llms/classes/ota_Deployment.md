# Deployment (ota_Deployment)

- Name: `ota_Deployment`
- IRI: `ota:Deployment` (https://w3id.org/altium/cdm/ota/Deployment)
- Bounded context: [ota](../ota.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/ota_Deployment/](../../classes/ota_Deployment/)

Deployment represents the request for an OTA update that assigns packages to the ECUs of its target, either a single device or all devices of a single fleet. It records what was requested, not how it was carried out: the outcome on each targeted device is a separate Deployment Result, which refers to the deployment. Provider-specific scheduling and cancellation restrictions are defined by the corresponding API profile.

## GRID

`grid:workspace:{workspace-id}:ota:deployment/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| targetDevice | [ota_Device](ota_Device.md) | 0..1 | The single device targeted by the deployment. | core_occursIn |  |
| targetFleet | [ota_Fleet](ota_Fleet.md) | 0..1 | The fleet targeted by the deployment; all devices of the fleet are addressed. | core_occursIn |  |
| createdAt | datetime | 0..1 | The date and time the deployment was requested, in UTC, when reported by the provider. |  |  |
| scheduledFor | datetime | 0..1 | The date and time the deployment is scheduled to start, in UTC. |  |  |
| assignments | [ota_DeploymentAssignment](ota_DeploymentAssignment.md) | 1..* | The packages assigned per hardware identifier, at least one. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_DeploymentResult](ota_DeploymentResult.md) | deployment | 1 | core_outputOf |
