# Build Artifact (sft_BuildArtifact)

- Name: `sft_BuildArtifact`
- IRI: `sft:BuildArtifact` (https://w3id.org/altium/cdm/software/BuildArtifact)
- Bounded context: [software](../software.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/sft_BuildArtifact/](../../classes/sft_BuildArtifact/)

## In the product

- No public product documentation exists for this concept.

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

- [sft_SoftwareProject](sft_SoftwareProject.md): `latestBuildArtifacts`
- [sft_SoftwareRelease](sft_SoftwareRelease.md): `buildArtifacts`
