# Bounded context: Design

Models design projects stored in a Workspace, including multi-board and harness projects, with their parameters, variants and releases, the manufacturing packages shared from releases, project templates with their revisions, and rule checks run against projects. It corresponds to Workspace projects in Altium 365 and Altium Designer, from project creation through to design release.

HTML page: [subsets/design/](../subsets/design/)

## In the product

- [Workspace Projects](https://www.altium.com/documentation/altium-365/workspace-projects) (primary)
- [Management of a Specific Project](https://www.altium.com/documentation/altium-365/management-specific-project)
- [Design Project Release](https://www.altium.com/documentation/altium-designer/preparing-for-manufacture/design-release)

## Classes

- [Board Layer](classes/des_BoardLayer.md) (`des_BoardLayer`): A physical or logical layer of a board: copper (signal or plane), dielectric, mask, overlay, paste or mechanical. · Resource · API DesLayer
- [Compiled Design](classes/des_CompiledDesign.md) (`des_CompiledDesign`): The compiled, connectivity-level view of a design project at one revision: its schematic sheets, the components placed on them, their pins and the nets that connect those pins, resolved across the sheet hierarchy. · Resource · API DesignData_Preview
- [Component Part](classes/des_ComponentPart.md) (`des_ComponentPart`): One part (section) of a placed component. · Resource · API DesignDataPart_Preview
- [Design Parameter](classes/des_DesignParameter.md) (`des_DesignParameter`): A name/value parameter of an object in the compiled design, such as a placed component. · Resource
- [Differential Pair](classes/des_DifferentialPair.md) (`des_DifferentialPair`): Two nets that carry a differential signal together, for example USB_D_P and USB_D_N. · Resource · API DesignDataDifferentialPair_Preview
- [Hardware Project](classes/des_Project.md) (`des_Project`): A design project stored in a Workspace, normally under its built-in version control, such as a PCB project. · Activity · API DesProject · GRID `grid:workspace:{workspace-id}:design:project/{id}`
- [Hardware Project Release](classes/des_ProjectRelease.md) (`des_ProjectRelease`): Project Release captures an immutable snapshot of a PCB design project at a specific point in its lifecycle, packaging all design data, outputs, and metadata required for manufacturing, assembly, and downstream processes. · Artifact · API DesRelease · GRID `grid:workspace:{workspace-id}:design:project-release/{id}`
- [Hardware Project Variant](classes/des_ProjectVariant.md) (`des_ProjectVariant`): A design variant of a project: a named variation of the same base design that is assembled with a different set of components. · Resource · API DesWipVariant
- [Harness Project](classes/des_HarnessProject.md) (`des_HarnessProject`): Harness Project defines the design of a cable and wiring harness as a standalone yet integrable artifact, capturing connectors, wires, splices, and pin-to-pin mappings required to implement electrical interconnects between boards and system elements. · Activity · API DesProject
- [Layer Stack](classes/des_LayerStack.md) (`des_LayerStack`): One stack of layers of a board, ordered from top to bottom; a rigid-flex board has one per rigid or flex region type. · Resource · API DesStack
- [Layer Stackup](classes/des_Stackup.md) (`des_Stackup`): The layer structure of a board: one or more layer stacks (more than one for rigid-flex boards). · Resource · API DesStackup
- [Manufacturing Package](classes/des_ManufacturingPackage.md) (`des_ManufacturingPackage`): A read-only package that contains a subset of Project Release artifacts that is typically shared with an external party for the purposes of manufacturing the board (e.g. Manufacturing Package may contain fabrication/assembly files required by the factories, but not the sources of the project) · Artifact · GRID `grid:workspace:{workspace-id}:design:manufacturing-package/{id}`
- [Multiboard Project](classes/des_MultiboardProject.md) (`des_MultiboardProject`): Multiboard Project represents the coordinated design of multiple interconnected PCB projects assembled into a single system, capturing both their logical interconnects and physical arrangements. · Activity · API DesProject
- [Net](classes/des_Net.md) (`des_Net`): An electrical net of the compiled design: a set of component pins that are electrically connected, resolved across the sheet hierarchy. · Resource · API DesignDataNet_Preview
- [Net Class](classes/des_NetClass.md) (`des_NetClass`): A named group of nets that share design rules, for example DDR3 or HighSpeed. · Resource
- [Net Item](classes/des_NetItem.md) (`des_NetItem`): A connection object that contributes to a net, such as a net label, a port, a sheet entry or a power object. · Resource · API DesignDataNetItem_Preview
- [Pad](classes/des_Pad.md) (`des_Pad`): A connection target on a board, usually one pin of a placed component; a free pad belongs to no component. · Resource · API DesPad
- [PCB Component](classes/des_PcbComponent.md) (`des_PcbComponent`): A component as placed on a board: its footprint instance with position, rotation, side and pads. · Resource · API DesDesignItem
- [PCB Layout](classes/des_PcbLayout.md) (`des_PcbLayout`): The physical design of one board in a design project at one revision: its outline, layer stack, placed components, pads, tracks and vias, and the copper nets they form. · Resource · API DesPcb
- [PCB Net](classes/des_PcbNet.md) (`des_PcbNet`): A net as realised in copper on a board: the pads, tracks and vias that carry it, the layers it is routed on and its routed length. · Resource · API DesNet
- [Pin Instance](classes/des_PinInstance.md) (`des_PinInstance`): A pin of a placed component in the design. · Resource · API DesignDataPin_Preview
- [Placed Component](classes/des_PlacedComponent.md) (`des_PlacedComponent`): A component instance placed in the design, identified by its designator. · Resource · API DesignDataComponent_Preview
- [Point 2D](classes/des_Point2D.md) (`des_Point2D`): A point in the coordinate system of a schematic sheet or PCB document. · Resource · API DesPosition2D
- [Project Parameter](classes/des_ProjectParameter.md) (`des_ProjectParameter`): A name/value parameter defined at the level of a design project. · Resource · API DesProjectParameter
- [Project Template](classes/des_ProjectTemplate.md) (`des_ProjectTemplate`): A reusable starting point for new design projects that bundles the documents, files and project settings a team wants to apply again and again. · Artifact · API DesProjectTemplate · GRID `grid:workspace:{workspace-id}:design:project-template/{id}`
- [Project Template Revision](classes/des_ProjectTemplateRevision.md) (`des_ProjectTemplateRevision`): An immutable revision of a project template. · Artifact · API DesProjectTemplateRevision · GRID `grid:workspace:{workspace-id}:design:project-template-revision/{id}`
- [Rectangle 2D](classes/des_Rectangle2D.md) (`des_Rectangle2D`): An axis-aligned rectangle, used for bounding boxes of drawing objects. · Resource · API DesRectangle
- [Rule Check](classes/des_RuleCheck.md) (`des_RuleCheck`): Rule check definitions that can be executed against a project to validate design integrity and compliance with specified constraints. · Artifact · API RuleCheck · GRID `grid:workspace:{workspace-id}:design:rule-check/{id}`
- [Rule Check Execution](classes/des_RuleCheckExecution.md) (`des_RuleCheckExecution`): Execution of a rule check against a project to validate design integrity and compliance with specified constraints. · Activity · API RuleCheckExecution · GRID `grid:workspace:{workspace-id}:design:rule-check-execution/{id}`
- [Schematic Sheet](classes/des_SchematicSheet.md) (`des_SchematicSheet`): A schematic document of the design. · Resource · API DesignDataSchematicDocument_Preview
- [Track](classes/des_Track.md) (`des_Track`): A straight conductor segment on a board layer, with a width. · Resource · API DesTrack
- [Variant Variation](classes/des_VariantVariation.md) (`des_VariantVariation`): How one placed component differs in a project variant: not fitted, or replaced by an alternate component. · Resource · API DesignDataVariation_Preview
- [Via](classes/des_Via.md) (`des_Via`): A plated hole that connects copper on two or more layers of a board. · Resource · API DesVia
- [Wire](classes/des_Wire.md) (`des_Wire`): A wire drawn on a schematic sheet, part of one net. · Resource · API DesignDataLine_Preview
