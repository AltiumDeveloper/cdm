# Deployment Assignment (ota_DeploymentAssignment)

- Name: `ota_DeploymentAssignment`
- IRI: `ota:DeploymentAssignment` (https://w3id.org/altium/cdm/ota/DeploymentAssignment)
- Bounded context: [ota](../ota.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/ota_DeploymentAssignment/](../../classes/ota_DeploymentAssignment/)

Deployment Assignment assigns a package to the ECUs with a given hardware identifier. Deployment requests may name packages only; the provider then resolves the hardware identifier from the package and the target device's ECUs.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| hardwareId | string | 0..1 | The hardware identifier of the target ECUs. |  |  |
| package | [ota_Package](ota_Package.md) | 1 | The package to install on the target ECUs, referenced by its GRID. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_Deployment](ota_Deployment.md) | assignments | 1..* |  |
