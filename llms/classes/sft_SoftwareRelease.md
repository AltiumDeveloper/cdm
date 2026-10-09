# Software Release (sft_SoftwareRelease)

- Name: `sft_SoftwareRelease`
- IRI: `sft:SoftwareRelease` (https://w3id.org/altium/cdm/software/SoftwareRelease)
- Bounded context: [software](../software.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sft_SoftwareRelease/](../../classes/sft_SoftwareRelease/)

## In the product

- No public product documentation exists for this concept.

## GRID

`grid:workspace:{workspace-id}:software:software-release/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| title | string | 0..1 | Title of the release |  |  |
| description | string | 0..1 | Free form text with additional details about the release. |  |  |
| attachments | BLOB | 0..1 | Additional files associated with the release (reports, documents, etc.) |  |  |
| aiModels | [sft_AIModel](sft_AIModel.md) | 0..1 | AI model artifacts included into the release. | core_hasPart |  |
| buildArtifacts | [sft_BuildArtifact](sft_BuildArtifact.md) | * | Firmware build artifacts, deployable to the device. | core_hasPart |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [sft_SoftwareProject](sft_SoftwareProject.md) | releases | * | core_releases |
