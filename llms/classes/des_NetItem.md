# Net Item (des_NetItem)

- Name: `des_NetItem`
- IRI: `des:NetItem` (https://w3id.org/altium/cdm/design/NetItem)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_NetItem/](../../classes/des_NetItem/)

A connection object that contributes to a net, such as a net label, a port, a sheet entry or a power object.

## In the API

- Platform API type: [`DesignDataNetItem_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataNetItem_Preview/) (object)
- Altium Designer SDK type: [`EDP.INetItem`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/INetItem/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| kind | [des_NetItemKind](../enums/des_NetItemKind.md) | 1 | The kind of connection object. |  |  |
| name | string | 0..1 | The name carried by the object, e.g. a port name. |  |  |
| location | [des_Point2D](des_Point2D.md) | 0..1 | The location on its schematic sheet. |  |  |
| boundingBox | [des_Rectangle2D](des_Rectangle2D.md) | 0..1 | The bounding box on its schematic sheet. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Net](des_Net.md) | netItems | * |  |
