# Net Item Kind (des_NetItemKind)

- Name: `des_NetItemKind`
- IRI: `des:NetItemKind` (https://w3id.org/altium/cdm/design/NetItemKind)
- Kind: enumeration
- HTML page: [enums/des_NetItemKind/](../../enums/des_NetItemKind/)

The kind of connection object that contributes to a net.

## Values

| Value | Description |
| --- | --- |
| `Pin` | A component pin. |
| `SheetEntry` | A sheet entry on a sheet symbol. |
| `NetLabel` | A net label. |
| `Port` | A sheet port. |
| `PowerObject` | A power port object, such as GND or VCC. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_NetItem](../classes/des_NetItem.md) | kind | 1 |  |
