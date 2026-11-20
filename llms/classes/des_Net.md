# Net (des_Net)

- Name: `des_Net`
- IRI: `des:Net` (https://w3id.org/altium/cdm/design/Net)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Net/](../../classes/des_Net/)

An electrical net of the compiled design: a set of component pins that are electrically connected, resolved across the sheet hierarchy. Its scope says whether it is local to one sheet, part of a sheet interface or global. Net names are not necessarily unique.

## Comments

- Replaces udm_DesignNet and des_design_net from pull request 23; nets are design-wide rather than per sheet.
- Open question Q2 is which relation from the relation dictionary (if any) expresses that a net connects pins.

## In the API

- Platform API type: [`DesignDataNet_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataNet_Preview/) (object)
- Altium Designer SDK type: [`EDP.INet`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/INet/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | Net name, e.g. GND or SPI1_CLK. |  |  |
| scope | [des_NetScope](../enums/des_NetScope.md) | 0..1 | Whether the net is local to a sheet, a sheet interface, or global. |  |  |
| isPower | boolean | 0..1 | True when the net carries power, including ground. |  |  |
| connects | [des_PinInstance](des_PinInstance.md) | * | The component pins connected by this net. |  |  |
| netItems | [des_NetItem](des_NetItem.md) | * | The connection objects that make up the net, such as net labels, ports, sheet entries and power objects. |  |  |
| netClasses | [des_NetClass](des_NetClass.md) | * | The net classes this net belongs to. |  |  |
| differentialPair | [des_DifferentialPair](des_DifferentialPair.md) | 0..1 | The differential pair this net is one side of, if any. |  |  |
| wires | [des_Wire](des_Wire.md) | * | The wires drawn for this net on schematic sheets. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_CompiledDesign](des_CompiledDesign.md) | nets | * |  |
| [des_DifferentialPair](des_DifferentialPair.md) | negative | 0..1 |  |
| [des_DifferentialPair](des_DifferentialPair.md) | positive | 0..1 |  |
| [des_PcbNet](des_PcbNet.md) | logicalNet | 0..1 |  |
