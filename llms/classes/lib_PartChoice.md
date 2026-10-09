# Part Choice (lib_PartChoice)

- Name: `lib_PartChoice`
- IRI: `lib:PartChoice` (https://w3id.org/altium/cdm/library/PartChoice)
- Bounded context: [library](../library.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/lib_PartChoice/](../../classes/lib_PartChoice/)

One entry in a component's Part Choice list: a manufacturer part, rather than a specific supplier, that may be used to implement the component, bringing with it the offers of the suppliers that sell it. Entries are ranked automatically by availability, price and lifecycle, and users can override the order with their own rank; the top preferred entry is used as the component's part choice in a BOM.

## In the product

- [Adding Supply Chain Information to a Component](https://www.altium.com/documentation/altium-designer/components-libraries/adding-supply-chain-information-component#anatomy_of_a_part_choice) (primary)
- [Workspace Components](https://www.altium.com/documentation/altium-365/workspace-components#view_edit_part_choices)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| rank | integer | 1 | Rank of the part choice in the list |  |  |
| part | [lib_Part](lib_Part.md) | 1 | The part associated with this choice |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [lib_PartChoiceList](lib_PartChoiceList.md) | partChoices | * |  |
