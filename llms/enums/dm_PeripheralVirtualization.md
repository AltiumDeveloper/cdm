# dm_PeripheralVirtualization

- Name: `dm_PeripheralVirtualization`
- IRI: `dm:PeripheralVirtualization` (https://w3id.org/altium/cdm/deviceModel/PeripheralVirtualization)
- Kind: enumeration
- HTML page: [enums/dm_PeripheralVirtualization/](../../enums/dm_PeripheralVirtualization/)

Defines the virtualization model used by a peripheral interface, describing whether the peripheral is implemented as a single, non-virtualized instance or as multiple virtualized instances mapped to individual functional channels.

## Values

| Value | Description |
| --- | --- |
| `None` | No virtualization. All associated functions collectively implement a single peripheral interface instance (for example, SCI0 on RA devices). |
| `Channel` | Channel-based virtualization. Each individual function represents an independent channel and implements the peripheral interface type separately (for example, ADC on RA devices where each ANxxx function corresponds to an ADC channel). |

## Referenced by

- [dm_PeripheralInstance](../classes/dm_PeripheralInstance.md): `virtualization`
