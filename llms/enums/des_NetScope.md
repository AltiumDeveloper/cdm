# Net Scope (des_NetScope)

- Name: `des_NetScope`
- IRI: `des:NetScope` (https://w3id.org/altium/cdm/design/NetScope)
- Kind: enumeration
- HTML page: [enums/des_NetScope/](../../enums/des_NetScope/)

How far a net reaches in the sheet hierarchy.

## Values

| Value | Description |
| --- | --- |
| `Local` | The net exists on one sheet only. |
| `SheetInterface` | The net connects a sheet to its parent through ports or sheet entries. |
| `Global` | The net is global to the design, e.g. a power net. |
| `Unknown` | The scope could not be determined. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Net](../classes/des_Net.md) | scope | 0..1 |  |
