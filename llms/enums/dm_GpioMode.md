# dm_GpioMode

- Name: `dm_GpioMode`
- IRI: `dm:GpioMode` (https://w3id.org/altium/cdm/deviceModel/GpioMode)
- Kind: enumeration
- HTML page: [enums/dm_GpioMode/](../../enums/dm_GpioMode/)

Defines the specific electrical and logical configuration of a pin when PortMode is set to Gpio.

## Values

| Value | Description |
| --- | --- |
| `None` | No specific GPIO mode assigned (often used for high-impedance or initial state). |
| `Input` | Pin is configured as a digital input. |
| `OutputLow` | Pin is configured as a digital output with a default logic low (0) state. |
| `OutputHigh` | Pin is configured as a digital output with a default logic high (1) state. |

## Referenced by

- [dm_PortConfigurationDependency](../classes/dm_PortConfigurationDependency.md): `gpioMode`
