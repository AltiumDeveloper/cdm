# Pin Electrical Type (lib_PinElectricalType)

- Name: `lib_PinElectricalType`
- IRI: `lib:PinElectricalType` (https://w3id.org/altium/cdm/library/PinElectricalType)
- Kind: enumeration
- HTML page: [enums/lib_PinElectricalType/](../../enums/lib_PinElectricalType/)

The electrical type of a pin, used by electrical rule checks.

## Values

| Value | Description |
| --- | --- |
| `Input` | Input pin. |
| `Output` | Output pin. |
| `InputOutput` | Bidirectional pin. |
| `OpenCollector` | Open collector output. |
| `OpenEmitter` | Open emitter output. |
| `HiZ` | High-impedance (tri-state) pin. |
| `Passive` | Passive pin, e.g. on a resistor. |
| `Power` | Power or ground pin. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PinInstance](../classes/des_PinInstance.md) | electricalType | 0..1 |  |
| [lib_Pin](../classes/lib_Pin.md) | electricalType | 0..1 |  |
