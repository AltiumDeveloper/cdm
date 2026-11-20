# Compiled Design (des_CompiledDesign)

- Name: `des_CompiledDesign`
- IRI: `des:CompiledDesign` (https://w3id.org/altium/cdm/design/CompiledDesign)
- Bounded context: [design](../design.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/des_CompiledDesign/](../../classes/des_CompiledDesign/)

The compiled, connectivity-level view of a design project at one revision: its schematic sheets, the components placed on them, their pins and the nets that connect those pins, resolved across the sheet hierarchy. It is what is read when the logical design is analysed, as opposed to the drawing objects that are edited in the schematic editor. It is identified by its project and revision.

## Comments

- Refresh of pull request 23 (UDM modelling). Open question Q1 is whether this should be a Resource of the project (as here), an Artifact, or part of a new project revision class.
- Design data is only available for revisions where design data generation has run.

## In the API

- Platform API type: [`DesignData_Preview`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesignData_Preview/) (object)
- Altium Designer SDK type: [`EDP.IProject`](https://altiumdeveloper.github.io/ad-sdk-docs/reference/edp/IProject/)

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| project | [des_Project](des_Project.md) | 1 | The design project this compiled design belongs to. |  |  |
| revisionId | string | 1 | The version-control revision of the project that was compiled. |  |  |
| sheets | [des_SchematicSheet](des_SchematicSheet.md) | * | The root schematic sheets of the design; sub-sheets are reached through their parents. |  |  |
| components | [des_PlacedComponent](des_PlacedComponent.md) | * | All components placed in the design. |  |  |
| nets | [des_Net](des_Net.md) | * | All nets of the design, power and signal, resolved across sheets. |  |  |
| netClasses | [des_NetClass](des_NetClass.md) | * | The net classes defined in the design. |  |  |
| variations | [des_VariantVariation](des_VariantVariation.md) | * | Per-component variations defined by the project variants. |  |  |
| boards | [des_PcbLayout](des_PcbLayout.md) | * | The PCB layouts of the project at this revision. |  |  |
