# Schematic Template (con_SchematicTemplate)

- Name: `con_SchematicTemplate`
- IRI: `con:SchematicTemplate` (https://w3id.org/altium/cdm/configuration/SchematicTemplate)
- Bounded context: [configuration](../configuration.md)
- Kind: Artifact
- Is a: [core_Artifact](core_Artifact.md)
- HTML page: [classes/con_SchematicTemplate/](../../classes/con_SchematicTemplate/)

A schematic template stored as a Workspace Item. When applied to a schematic sheet, the template sets the sheet's size, its graphics such as a title block, and its sheet-level parameters, so that a team's schematics look consistent. The template content is kept in successive revisions of the Item, and environment configurations can reference those revisions to control which templates designers may use.

## Comments

- TBD

## In the product

- [Creating a Schematic Template](https://www.altium.com/documentation/altium-designer/schematic/creating-templates) (primary)

## GRID

None declared.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| revisions | [con_SchematicTemplateRevision](con_SchematicTemplateRevision.md) | * | The set of versioned snapshots derived from this artifact. | core_revisions |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |
