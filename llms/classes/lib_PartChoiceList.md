# Part Choice List (lib_PartChoiceList)

- Name: `lib_PartChoiceList`
- IRI: `lib:PartChoiceList` (https://w3id.org/altium/cdm/library/PartChoiceList)
- Bounded context: [library](../library.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/lib_PartChoiceList/](../../classes/lib_PartChoiceList/)

The list of Part Choices for a component: the manufacturer parts that may be used to implement it on the assembled board. In the product the list is associated with the component and seen by all of its revisions; when part choice revision control is enabled, changing the list saves a new component revision.

## In the product

- [Adding Supply Chain Information to a Component](https://www.altium.com/documentation/altium-designer/components-libraries/adding-supply-chain-information-component#part_choices) (primary)
- [Workspace Components](https://www.altium.com/documentation/altium-365/workspace-components#view_edit_part_choices)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| partChoices | [lib_PartChoice](lib_PartChoice.md) | * | List of part choices |  |  |

## Referenced by

- [lib_ComponentRevision](lib_ComponentRevision.md): `partChoiceList`
