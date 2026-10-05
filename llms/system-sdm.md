# Bounded context: System Design - System Data Model

Models the System Data Model (SDM) of a Renesas 365 solution and its versions, each combining a functional model with device, hardware and software models, plus metadata recording who created a version and with which application, and client-specific metadata (e.g. for ESD, Altium Designer or e² studio). The ESD document and e² studio push changes to and pull changes from the SDM, and Altium Designer pulls it into hardware projects.

HTML page: [subsets/system-sdm/](../subsets/system-sdm/)

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365#system_data_model) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#pushing_pulling_sdm)
- [Working with Renesas 365 Solutions](https://www.altium.com/documentation/altium-designer/working-renesas-365-solutions#pulling_sdm_into_a_hardware_project)

## Classes

- [Authoring Application](classes/system_SdmAuthoringApplication.md) (`system_SdmAuthoringApplication`): Identifies the application used to create a system model version. · Resource
- [Connection](classes/system_SdmConnection.md) (`system_SdmConnection`): Represents a connection between functional blocks. · Resource · API SysSdmConnection
- [Device Model](classes/system_SdmDeviceModel.md) (`system_SdmDeviceModel`): Represents a device model within the system design. · Resource · API SysSdmDeviceModel
- [Domain Metadata](classes/system_SdmClientMetadata.md) (`system_SdmClientMetadata`): Captures metadata specific to a particular client (e.g., ESD, AD, E2Studio). · Resource
- [Endpoint](classes/system_SdmEndpoint.md) (`system_SdmEndpoint`): Represents an endpoint of a connection. · Resource · API SysSdmEndpoint
- [Functional Block](classes/system_SdmFunctionalBlock.md) (`system_SdmFunctionalBlock`): Represents a logical block within a system functional model. · Resource · API SysSdmFunctionalBlock
- [Functional Model](classes/system_SdmFunctionalModel.md) (`system_SdmFunctionalModel`): Captures the functional aspects of the system design, focusing on the behavior and interactions of functional blocks. · Resource · API SysSdmFunctionalModel
- [Hardware Component](classes/system_SdmHardwareComponent.md) (`system_SdmHardwareComponent`): Represents a hardware component / part. · Resource · API SysSdmHardwareComponent
- [Hardware Model](classes/system_SdmHardwareModel.md) (`system_SdmHardwareModel`): Captures the hardware components and their interactions within the system design. · Resource · API SysSdmHardwareModel
- [Port](classes/system_SdmPort.md) (`system_SdmPort`): Represents a port within a system design. · Resource · API SysSdmPort
- [Software Component](classes/system_SdmSoftwareComponent.md) (`system_SdmSoftwareComponent`): Represents a software component instance and its dependencies. · Resource · API SysSdmSoftwareComponent
- [Software Model](classes/system_SdmSoftwareModel.md) (`system_SdmSoftwareModel`): Captures the software components and their interactions within the system design. · Resource · API SysSdmSoftwareModel
- [Software Specification](classes/system_SdmSoftwareSpecification.md) (`system_SdmSoftwareSpecification`): The "blueprint" for a software component. · Resource · API SysSdmSoftwareSpecification
- [Software Stack Instance](classes/system_SdmSoftwareStackInstance.md) (`system_SdmSoftwareStackInstance`): Represents a software stack instance and its dependencies. · Resource · API SysSdmSoftwareStackInstance
- [System Model](classes/system_SdmSystemModel.md) (`system_SdmSystemModel`): A high-level system model that captures the overall system architecture, crossing boundary between functional and logical domains (e.g., hardware and software). · Activity · API SysSdmSystemModel · GRID `grid:workspace:{workspace-id}:system-design:sdm/{id}`
- [System Model Version](classes/system_SdmSystemModelVersion.md) (`system_SdmSystemModelVersion`): A specific version of a system model, capturing the state of the system design at a particular point in time. · Artifact · API SysSdmSystemModelVersion · GRID `grid:workspace:{workspace-id}:system-design:sdm-version/{id}`
- [System Model Version Metadata](classes/system_SdmSystemModelVersionMetadata.md) (`system_SdmSystemModelVersionMetadata`): Metadata associated with a specific version of a system model, capturing provenance information. · Resource
