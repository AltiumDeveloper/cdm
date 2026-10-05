# Bounded context: System Design

Models the Electronic System Design (ESD) document of a Renesas 365 solution: a system-level block diagram of functional blocks with their key (hardware) and software components, ports and parameters, the connections between blocks, and entries for the hardware and software projects that implement the system. It corresponds to Electronic System Design in a Renesas 365 Workspace.

HTML page: [subsets/system/](../subsets/system/)

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd) (primary)
- [Renesas 365](https://www.altium.com/documentation/altium-365/renesas-365)

## Classes

- [Connection](classes/system_Connection.md) (`system_Connection`): A connection line in an ESD document representing an interconnection between functional blocks (e.g. signals passed between the interfaces of two devices), drawn directly between blocks or between their ports. · Resource
- [Endpoint](classes/system_Endpoint.md) (`system_Endpoint`): One end of a connection in an ESD document, identified by the functional block and the port where the connection line starts or ends. · Resource
- [ESD Document](classes/system_ESDDocument.md) (`system_ESDDocument`): A system-level block diagram document used in a Renesas 365 solution (listed there as a System Design project) to describe the architecture of the system at a functional level. · Activity · API SysEsdDocument · GRID `grid:workspace:{workspace-id}:system-design:esd/{id}`
- [Functional Block](classes/system_FunctionalBlock.md) (`system_FunctionalBlock`): Represents a logical block within an ESD document (e.g., MCU subsystem, LED driver block) that stands for a function, operation or device of the system, including parameters, key components, software components, ports, and associations. · Resource
- [Hardware Project](classes/system_HardwareProject.md) (`system_HardwareProject`): An entry of an ESD document for a PCB design project (des_Project) that implements part of the system, listing the functional blocks that project covers. · Resource
- [Key Component](classes/system_KeyComponent.md) (`system_KeyComponent`): A key component of a functional block in an ESD document, shown in the editor as a hardware component (e.g. a Renesas RA MCU chosen with the RA Explorer). · Resource
- [Parameter](classes/system_Parameter.md) (`system_Parameter`): Name–value parameter associated with functional blocks, ports, or other system design resources. · Resource
- [Port](classes/system_Port.md) (`system_Port`): An interface of a functional block in an ESD document (e.g. the I2C interface of an MPU), placed inside the block's boundaries; connection lines between blocks can start and end at ports. · Resource
- [Port Association](classes/system_PortAssociation.md) (`system_PortAssociation`): Resource
- [Software Component](classes/system_SoftwareComponent.md) (`system_SoftwareComponent`): Functional in nature, abstracted from but connected to logical implementation. · Resource
- [Software Project](classes/system_SoftwareProject.md) (`system_SoftwareProject`): An entry of an ESD document for a software project (sft_SoftwareProject) that implements part of the system, listing the software components that project covers. · Resource
