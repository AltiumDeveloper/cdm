# system_PortType

- Name: `system_PortType`
- IRI: `sys:PortType` (https://w3id.org/altium/cdm/system/PortType)
- Kind: enumeration
- HTML page: [enums/system_PortType/](../../enums/system_PortType/)

## Values

| Value | Description |
| --- | --- |
| `UART` |  |
| `GPIO` |  |
| `I2C` |  |
| `PWM` |  |
| `ADC` |  |
| `SPI` |  |
| `CAN` |  |
| `USB` |  |
| `DAC` |  |
| `DISPLAY` |  |
| `ETHERNET` |  |
| `IRQ` |  |
| `CAMERA` |  |
| `AUDIO` |  |
| `CD/MMC` |  |
| `POWER_MCU` |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [system_PortAssociation](../classes/system_PortAssociation.md) | portLibraryName | 1 |  |
| [system_SdmPort](../classes/system_SdmPort.md) | portType | 0..1 |  |
