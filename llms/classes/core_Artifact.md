# Artifact (core_Artifact)

- Name: `core_Artifact`
- IRI: `core:Artifact` (https://w3id.org/altium/cdm/core/Artifact)
- Bounded context: [core](../core.md)
- Kind: Artifact, abstract
- Is a: [core_Entity](core_Entity.md)
- Subclasses: [con_EnvironmentConfiguration](con_EnvironmentConfiguration.md), [con_SchematicTemplate](con_SchematicTemplate.md), [con_SchematicTemplateRevision](con_SchematicTemplateRevision.md), [cus_Script](cus_Script.md), [cus_ScriptExecution](cus_ScriptExecution.md), [cus_ScriptVersion](cus_ScriptVersion.md), [des_ManufacturingPackage](des_ManufacturingPackage.md), [des_ProjectTemplate](des_ProjectTemplate.md), [des_ProjectTemplateRevision](des_ProjectTemplateRevision.md), [des_RuleCheck](des_RuleCheck.md), [dm_FullStackDeviceModel](dm_FullStackDeviceModel.md), [lib_Component](lib_Component.md), [lib_ComponentRevision](lib_ComponentRevision.md), [lib_ComponentTemplate](lib_ComponentTemplate.md), [lib_ComponentTemplateRevision](lib_ComponentTemplateRevision.md), [lib_Datasheet](lib_Datasheet.md), [lib_Footprint](lib_Footprint.md), [lib_FootprintRevision](lib_FootprintRevision.md), [lib_ManagedSheet](lib_ManagedSheet.md), [lib_ManagedSheetRevision](lib_ManagedSheetRevision.md), [lib_Part](lib_Part.md), [lib_PcbSnippet](lib_PcbSnippet.md), [lib_PcbSnippetRevision](lib_PcbSnippetRevision.md), [lib_ReuseBlock](lib_ReuseBlock.md), [lib_ReuseBlockRevision](lib_ReuseBlockRevision.md), [lib_SchSnippet](lib_SchSnippet.md), [lib_SchSnippetRevision](lib_SchSnippetRevision.md), [lib_Symbol](lib_Symbol.md), [lib_SymbolRevision](lib_SymbolRevision.md), [ota_Device](ota_Device.md), [ota_Fleet](ota_Fleet.md), [ota_Package](ota_Package.md), [plt_Application](plt_Application.md), [plt_EventSubscription](plt_EventSubscription.md), [plt_LifecycleDefinition](plt_LifecycleDefinition.md), [plt_NamingScheme](plt_NamingScheme.md), [plt_Organization](plt_Organization.md), [plt_SolutionRelease](plt_SolutionRelease.md), [plt_User](plt_User.md), [plt_UserGroup](plt_UserGroup.md), [plt_Workspace](plt_Workspace.md), [plt_WorkspaceGroup](plt_WorkspaceGroup.md), [plt_WorkspaceUser](plt_WorkspaceUser.md), [pro_BomRelease](pro_BomRelease.md), [req_Requirement](req_Requirement.md), [req_RequirementBaseline](req_RequirementBaseline.md), [req_RequirementRevision](req_RequirementRevision.md), [req_RequirementSpecification](req_RequirementSpecification.md), [sft_AIModel](sft_AIModel.md), [sft_BuildArtifact](sft_BuildArtifact.md), [sft_DeviceConfiguration](sft_DeviceConfiguration.md), [sft_DeviceConfigurationRevision](sft_DeviceConfigurationRevision.md), [sft_SoftwareRelease](sft_SoftwareRelease.md), [sup_Company](sup_Company.md), [sup_EvalKit](sup_EvalKit.md), [sup_Offer](sup_Offer.md), [sup_Part](sup_Part.md), [sup_PartFamily](sup_PartFamily.md), [sup_PartGroup](sup_PartGroup.md), [sup_ReferenceDesign](sup_ReferenceDesign.md), [sup_SoftwareProject](sup_SoftwareProject.md), [sup_SolutionTemplate](sup_SolutionTemplate.md), [system_SdmSystemModelVersion](system_SdmSystemModelVersion.md)
- HTML page: [classes/core_Artifact/](../../classes/core_Artifact/)

Abstract base for persistent data objects that are created, stored, versioned, and consumed. Examples: components, documents, system models.

## In standards

- close: [prov:Entity](http://www.w3.org/ns/prov#Entity)
- related: [obo:BFO_0000031](http://purl.obolibrary.org/obo/BFO_0000031)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
