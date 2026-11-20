# Wire (des_Wire)

- Name: `des_Wire`
- IRI: `des:Wire` (https://w3id.org/altium/cdm/design/Wire)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_Wire/](../../classes/des_Wire/)

A wire drawn on a schematic sheet, part of one net.

## Comments

- [interpretation] DesignDataNet_Preview.lines is read as the wires of the net: the AD SDK equivalent, INet.DM_Lines, returns ILine, described as a line object on a schematic document.
- The Platform API serves only location and bounding rectangle; vertices are available from the AD SDK (ISch_Wire inherits Vertex / VerticesCount from ISch_Polygon).

## In the API

- Platform API type: [`DesignDataLine_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataLine_Preview/) (object)
- Altium Designer SDK type: [`EDP.ILine`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/ILine/)
- Altium Designer SDK type: [`SCH.ISch_Wire`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/sch/ISch_Wire/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| uniqueId | string | 0..1 | The unique identifier of the wire. |  |  |
| sheet | [des_SchematicSheet](des_SchematicSheet.md) | 0..1 | The sheet the wire is drawn on. |  |  |
| location | [des_Point2D](des_Point2D.md) | 0..1 | The reference location of the wire. |  |  |
| boundingBox | [des_Rectangle2D](des_Rectangle2D.md) | 0..1 | The bounding box of the wire. |  |  |
| vertices | [des_Point2D](des_Point2D.md) | * | The vertices of the wire, in order. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_Net](des_Net.md) | wires | * |  |
