# System Model Version Metadata (system_SdmSystemModelVersionMetadata)

- Name: `system_SdmSystemModelVersionMetadata`
- IRI: `sys:SdmSystemModelVersionMetadata` (https://w3id.org/altium/cdm/system/SdmSystemModelVersionMetadata)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SdmSystemModelVersionMetadata/](../../classes/system_SdmSystemModelVersionMetadata/)

Metadata associated with a specific version of a system model, capturing provenance information.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| createdAt | datetime | 1 | The date and time when the SDM version was created. |  |  |
| createdBy | [plt_WorkspaceUser](plt_WorkspaceUser.md) | 1 | The user that created this SDM version. |  |  |
| authoringApplication | [system_SdmAuthoringApplication](system_SdmAuthoringApplication.md) | 1 | The application used to create this SDM version. |  |  |
| tags | string | 1..* | The tags associated with this SDM version. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md) | metadata | 0..1 |  |
