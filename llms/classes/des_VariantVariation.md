# Variant Variation (des_VariantVariation)

- Name: `des_VariantVariation`
- IRI: `des:VariantVariation` (https://w3id.org/altium/cdm/design/VariantVariation)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_VariantVariation/](../../classes/des_VariantVariation/)

How one placed component differs in a project variant: not fitted, or replaced by an alternate component.

## Comments

- Replaces udm_DesignVariant and des_design_variant_variation from pull request 23.

## In the API

- Platform API type: [`DesignDataVariation_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignDataVariation_Preview/) (object)
- Altium Designer SDK type: [`EDP.IComponentVariation`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IComponentVariation/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| variant | [des_ProjectVariant](des_ProjectVariant.md) | 1 | The project variant that defines the variation. |  |  |
| component | [des_PlacedComponent](des_PlacedComponent.md) | 1 | The placed component that varies. |  |  |
| kind | [des_ComponentVariationKind](../enums/des_ComponentVariationKind.md) | 1 | How the component varies. |  |  |
| alternate | [lib_ComponentRevision](lib_ComponentRevision.md) | 0..1 | The component revision used instead, for an alternate variation. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_CompiledDesign](des_CompiledDesign.md) | variations | * |  |
