# dm_PortMode

- Name: `dm_PortMode`
- IRI: `dm:PortMode` (https://w3id.org/altium/cdm/deviceModel/PortMode)
- Kind: enumeration
- HTML page: [enums/dm_PortMode/](../../enums/dm_PortMode/)

Defines the primary operational mode of a physical port pin. Determines if the pin is controlled by the GPIO controller or routed to a specific peripheral function.

## Values

| Value | Description |
| --- | --- |
| `Gpio` | Pin is configured as General Purpose Input/Output. |
| `AlternateFunction` | Pin is routed to a specific peripheral internal signal (e.g., UART TX, SPI CLK). |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [dm_PortConfigurationDependency](../classes/dm_PortConfigurationDependency.md) | portMode | 0..1 |  |
