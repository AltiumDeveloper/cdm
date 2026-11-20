# Placed Component (des_PlacedComponent)

- Name: `des_PlacedComponent`
- IRI: `des:PlacedComponent` (https://w3id.org/altium/cdm/design/PlacedComponent)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_PlacedComponent/](../../classes/des_PlacedComponent/)

A component instance placed in the design, identified by its designator. When the design uses managed components, it is derived from a library component revision; when it uses a file-based library, there is no Workspace library item to follow and only its parameters (for example manufacturer and part number) describe it.

## Comments

- Replaces udm_DesignComponent and des_design_component from pull request 23.

## In the API

- Platform API type: [`DesignDataComponent_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataComponent_Preview/) (object)
- Altium Designer SDK type: [`EDP.IComponent`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IComponent/)
- Altium Designer SDK type: [`SCH.ISch_Component`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/sch/ISch_Component/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| uniqueId | string | 0..1 | Identifier of the placed component, unique within the design. |  |  |
| logicalDesignator | string | 1 | The designator as placed on the schematic, e.g. U3. |  |  |
| physicalDesignator | string | 0..1 | The designator after multi-channel annotation, e.g. U3_CH1. |  |  |
| sheet | [des_SchematicSheet](des_SchematicSheet.md) | 0..1 | The sheet the component is placed on. |  |  |
| parts | [des_ComponentPart](des_ComponentPart.md) | * | The parts (sections) of a multi-part component; a single-part component has one. |  |  |
| parameters | [des_DesignParameter](des_DesignParameter.md) | * | Name/value parameters of the placed component. |  |  |
| librarySource | [lib_ComponentRevision](lib_ComponentRevision.md) | 0..1 | The library component revision this placed component was taken from, when it is a managed component. |  |  |
| librarySourceKind | [des_LibrarySourceKind](../enums/des_LibrarySourceKind.md) | 0..1 | Whether the component comes from a managed Workspace library or a file-based library. |  |  |
| location | [des_Point2D](des_Point2D.md) | 0..1 | The location on its schematic sheet. |  |  |
| boundingBox | [des_Rectangle2D](des_Rectangle2D.md) | 0..1 | The bounding box on its schematic sheet. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_CompiledDesign](des_CompiledDesign.md) | components | * |  |
| [des_PcbComponent](des_PcbComponent.md) | placedComponent | 0..1 |  |
| [des_VariantVariation](des_VariantVariation.md) | component | 1 |  |
