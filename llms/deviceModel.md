# Bounded context: Device Model

Models an embedded device (e.g. an MCU), which the CDM calls a digital twin: its processors; its address map with memories, registers, bit fields and their enumerated values; its peripherals with their instances, modes and configurations; and its pins and ports with the alternative functions of each port. A configured device model filters the full model to one device configuration, which in the product is edited on a hardware component in an ESD document.

HTML page: [subsets/deviceModel/](../subsets/deviceModel/)

## In the product

- [Electronic System Design](https://www.altium.com/documentation/altium-365/esd#using_the_device_configuration) (primary)

## Classes

- [AddressBlock](classes/dm_AddressBlock.md) (`dm_AddressBlock`): Address block with start, size, and optional registers and peripherals. · Resource · API DmAddressBlock
- [AddressMap](classes/dm_AddressMap.md) (`dm_AddressMap`): Address map for the device including memory and peripheral regions. · Resource · API DmAddressMapModel
- [AddressSegment](classes/dm_AddressSegment.md) (`dm_AddressSegment`): A contiguous region of the device's memory map. · Resource · API DmAddressSegment
- [ConfiguredDeviceModel](classes/dm_ConfiguredDeviceModel.md) (`dm_ConfiguredDeviceModel`): A digital twin of an embedded hardware device as configured for a specific use-case. · Resource · API DmDeviceModelAsConfigured
- [FieldEnum](classes/dm_FieldEnum.md) (`dm_FieldEnum`): An enumerated value for a register field. · Resource · API DmAmFieldEnum
- [FullStackDeviceModel](classes/dm_FullStackDeviceModel.md) (`dm_FullStackDeviceModel`): A digital twin of an embedded hardware device. · Artifact · API DmFullStackDeviceModel · GRID `grid:global::device-model:fullstack-dm/{id}`
- [Memory](classes/dm_Memory.md) (`dm_Memory`): A memory entry within an address block. · Resource · API DmAmMemory
- [Peripheral](classes/dm_Peripheral.md) (`dm_Peripheral`): A single peripheral definition, including its instances and properties. · Resource · API DmPeripheral
- [PeripheralConfiguration](classes/dm_PeripheralConfiguration.md) (`dm_PeripheralConfiguration`): A concrete configuration for a peripheral role, containing pin multiplexing details. · Resource
- [PeripheralInstance](classes/dm_PeripheralInstance.md) (`dm_PeripheralInstance`): A concrete instance of a peripheral (e.g., SCI0), including available modes. · Resource · API DmPeripheralInstance
- [PeripheralMode](classes/dm_PeripheralMode.md) (`dm_PeripheralMode`): A specific mode that a peripheral instance can fulfill, · Resource · API DmPeripheralMode
- [PeripheralParameter](classes/dm_PeripheralParameter.md) (`dm_PeripheralParameter`): A parameter associated with peripheral instance configuration. · Resource
- [PeripheralPinConfig](classes/dm_PeripheralPinConfig.md) (`dm_PeripheralPinConfig`): A specific pin multiplexing configuration within peripheral configuration. · Resource
- [PeripheralPinDependencyConfig](classes/dm_PeripheralPinDependencyConfig.md) (`dm_PeripheralPinDependencyConfig`): A pin dependency to port mapping entry within peripheral configuration. · Resource
- [Pin](classes/dm_Pin.md) (`dm_Pin`): A physical pin on the device. · Resource · API DmPin
- [Port](classes/dm_Port.md) (`dm_Port`): A physical port on the device, with its functions, configurations, and connections. · Resource · API DmPort
- [PortConfiguration](classes/dm_PortConfiguration.md) (`dm_PortConfiguration`): A specific configuration for a port. · Resource · API DmPortConfiguration
- [PortConfigurationDependency](classes/dm_PortConfigurationDependency.md) (`dm_PortConfigurationDependency`): A dependency describing how a configuration value maps to GPIO or alternate function usage. · Resource · API DmConfigDependency
- [PortConfigurationEnumValue](classes/dm_PortConfigurationEnumValue.md) (`dm_PortConfigurationEnumValue`): An enumerated value for a port configuration. · Resource · API DmConfigEnumValue
- [PortConnection](classes/dm_PortConnection.md) (`dm_PortConnection`): A connection from this port to another component or signal. · Resource · API DmPortConnection
- [PortFunction](classes/dm_PortFunction.md) (`dm_PortFunction`): A specific function that a port can perform. · Resource · API DmPortFunction
- [Processor](classes/dm_Processor.md) (`dm_Processor`): Represents a physical processing core. · Resource
- [Register](classes/dm_Register.md) (`dm_Register`): A hardware register within an address block. · Resource · API DmAmRegister
- [RegisterField](classes/dm_RegisterField.md) (`dm_RegisterField`): A bit field within a register. · Resource · API DmAmRegisterField
