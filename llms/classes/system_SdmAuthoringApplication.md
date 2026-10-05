# Authoring Application (system_SdmAuthoringApplication)

- Name: `system_SdmAuthoringApplication`
- IRI: `sys:SdmAuthoringApplication` (https://w3id.org/altium/cdm/system/SdmAuthoringApplication)
- Bounded context: [system-sdm](../system-sdm.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/system_SdmAuthoringApplication/](../../classes/system_SdmAuthoringApplication/)

Identifies the application used to create a system model version.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| applicationId | [plt_Application](plt_Application.md) | 1 | The platform application associated with this authoring application. |  |  |
| name | string | 0..1 | The name of the application. |  |  |
| version | string | 0..1 | The version of the application. |  |  |

## Referenced by

- [system_SdmSystemModelVersionMetadata](system_SdmSystemModelVersionMetadata.md): `authoringApplication`
