# Bounded context: Software

Models the embedded software of a Renesas 365 solution: software projects with their releases and build artifacts, device configurations (with revisions) and their pin assignments, and AI models. In Renesas 365 the software project is the software part of a solution, edited in the built-in Web IDE or in e² studio; a device configuration there also covers the ports, package information and peripherals of a hardware component.

HTML page: [subsets/software/](../subsets/software/)

## In the product

- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365) (primary)
- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration)

## Classes

- [AI Model](classes/sft_AIModel.md) (`sft_AIModel`): AI model artifact in context of a workspace · Artifact · GRID `grid:workspace:{workspace-id}:software:ai-model/{id}`
- [Build Artifact](classes/sft_BuildArtifact.md) (`sft_BuildArtifact`): Artifact
- [Device Configuration](classes/sft_DeviceConfiguration.md) (`sft_DeviceConfiguration`): The configuration of a device (e.g. an MCU placed as a hardware component in an ESD document), covering its ports, package information, peripherals and pin assignments. · Artifact · API SftDevCfgDeviceConfiguration · GRID `grid:workspace:{workspace-id}:software:device-configuration/{id}`
- [Device Configuration Revision](classes/sft_DeviceConfigurationRevision.md) (`sft_DeviceConfigurationRevision`): Artifact · API SftDevCfgDeviceConfigurationRevision · GRID `grid:workspace:{workspace-id}:software:device-configuration-revision/{id}`
- [Pin Assignment](classes/sft_PinAssignment.md) (`sft_PinAssignment`): The assignment of a function to one pin of a device, identified by pin number and name. · Resource
- [Pin Assignment Model](classes/sft_PinAssignmentModel.md) (`sft_PinAssignmentModel`): The set of pin assignments of a device, one part of its device configuration alongside ports, package information and peripherals. · Resource
- [Software Project](classes/sft_SoftwareProject.md) (`sft_SoftwareProject`): The software part of a Renesas 365 solution, developed in the built-in Web IDE (based on the Theia framework) or in e² studio; it can also be created with an external repository type. · Activity · API SftSoftwareProject · GRID `grid:workspace:{workspace-id}:software:software-project/{id}`
- [Software Release](classes/sft_SoftwareRelease.md) (`sft_SoftwareRelease`): Artifact · GRID `grid:workspace:{workspace-id}:software:software-release/{id}`
