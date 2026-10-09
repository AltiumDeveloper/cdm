# Bounded context: Library Management

Models the components stored in a Workspace and their revisions, the symbols, footprints, parameters, datasheets and part choices that make them up, and the component templates they can be created from. It also covers manufacturer parts in the Workspace part catalog, part requests, and reusable design content such as reuse blocks, managed sheets, and schematic and PCB snippets. It corresponds to Workspace components and design reuse in Altium Designer and Altium 365.

HTML page: [subsets/library/](../subsets/library/)

## In the product

- [Building & Maintaining Your Components and Libraries](https://www.altium.com/documentation/altium-designer/components-libraries) (primary)
- [Workspace Components](https://www.altium.com/documentation/altium-365/workspace-components)
- [Design Reuse](https://www.altium.com/documentation/altium-designer/schematic/design-reuse)

## Classes

- [Component](classes/lib_Component.md) (`lib_Component`): Component represents a uniquely identifiable electronic part, defined by both its abstract design intent and its concrete realizations in manufacturing and supply. · Artifact · GRID `grid:workspace:{workspace-id}:library:component/{id}`
- [Component Parameter](classes/lib_ComponentParameter.md) (`lib_ComponentParameter`): A named parameter of a Workspace component, holding a value and, optionally, a data type. · Resource · API DesComponentParameter
- [Component Revision](classes/lib_ComponentRevision.md) (`lib_ComponentRevision`): Revision of a Component. · Artifact · API DesComponent · GRID `grid:workspace:{workspace-id}:library:component-revision/{id}`
- [Component Template](classes/lib_ComponentTemplate.md) (`lib_ComponentTemplate`): Component Template defines a reusable blueprint for creating and managing electronic components with consistent parameters, metadata, and lifecycle policies. · Artifact · API DesComponentTemplate · GRID `grid:workspace:{workspace-id}:library:component-template/{id}`
- [Component Template Revision](classes/lib_ComponentTemplateRevision.md) (`lib_ComponentTemplateRevision`): A revision of a Component Template: the template definition, stored as a *.CMPT document, saved into the Workspace at one point in time. · Artifact · API DesComponentTemplateRevision · GRID `grid:workspace:{workspace-id}:library:component-template-revision/{id}`
- [Datasheet](classes/lib_Datasheet.md) (`lib_Datasheet`): Datasheet represents a technical document associated with a Component or Part, providing authoritative specifications, electrical characteristics, and manufacturer information. · Artifact · API DesDatasheet · GRID `grid:workspace:{workspace-id}:library:datasheet/{id}`
- [Footprint](classes/lib_Footprint.md) (`lib_Footprint`): Footprint represents the physical layout definition of a Component on a PCB, specifying pad geometry, land patterns, and mechanical clearances required for assembly and manufacturing. · Artifact · GRID `grid:workspace:{workspace-id}:library:footprint/{id}`
- [Footprint Revision](classes/lib_FootprintRevision.md) (`lib_FootprintRevision`): A revision of a Footprint: the PCB footprint as saved into the Workspace at one point in time, with its own lifecycle state. · Artifact · API DesFootprint · GRID `grid:workspace:{workspace-id}:library:footprint-revision/{id}`
- [Managed Sheet](classes/lib_ManagedSheet.md) (`lib_ManagedSheet`): A schematic sheet, with its components and wiring, stored in a Workspace so that it can be reused in other designs. · Artifact · GRID `grid:workspace:{workspace-id}:library:managed-sheet/{id}`
- [Managed Sheet Revision](classes/lib_ManagedSheetRevision.md) (`lib_ManagedSheetRevision`): A revision of a Managed Sheet: the schematic sheet as saved into the Workspace at one point in time. · Artifact · GRID `grid:workspace:{workspace-id}:library:managed-sheet-revision/{id}`
- [Part](classes/lib_Part.md) (`lib_Part`): A manufacturer part, identified by manufacturer and part number, as held in the Workspace's Part Catalog together with the supplier parts through which it is sold. · Artifact · API DesPart · GRID `grid:workspace:{workspace-id}:library:part/{id}`
- [Part Choice](classes/lib_PartChoice.md) (`lib_PartChoice`): One entry in a component's Part Choice list: a manufacturer part, rather than a specific supplier, that may be used to implement the component, bringing with it the offers of the suppliers that sell it. · Resource
- [Part Choice List](classes/lib_PartChoiceList.md) (`lib_PartChoiceList`): The list of Part Choices for a component: the manufacturer parts that may be used to implement it on the assembled board. · Resource
- [Part Request](classes/lib_PartRequest.md) (`lib_PartRequest`): Part Request represents a formal demand from a designer to introduce a new Component or Part into the managed library, typically triggered when an item is not yet available in the workspace. · Activity · GRID `grid:workspace:{workspace-id}:library:part-request/{id}`
- [PCB Snippet](classes/lib_PcbSnippet.md) (`lib_PcbSnippet`): A selection of circuitry from a PCB design, including its components and routing, saved so that it can be placed in other PCB documents. · Artifact
- [PCB Snippet Revision](classes/lib_PcbSnippetRevision.md) (`lib_PcbSnippetRevision`): A revision of a PCB snippet as saved into the Workspace at one point in time. · Artifact
- [Reuse Block](classes/lib_ReuseBlock.md) (`lib_ReuseBlock`): A reusable section of a design stored in a Workspace, typically combining schematic circuitry with its PCB representation; a block can also be schematic-only or PCB-only. · Artifact · API DesReuseBlock · GRID `grid:workspace:{workspace-id}:library:reuse-block/{id}`
- [Reuse Block Revision](classes/lib_ReuseBlockRevision.md) (`lib_ReuseBlockRevision`): A revision of a Reuse Block: its schematic and/or PCB content as saved into the Workspace at one point in time, with its own lifecycle state. · Artifact · API DesReuseBlockRevision · GRID `grid:workspace:{workspace-id}:library:reuse-block-revision/{id}`
- [SCH Snippet](classes/lib_SchSnippet.md) (`lib_SchSnippet`): A selection of circuitry from a single schematic sheet, including its components, saved so that it can be placed in other designs. · Artifact
- [SCH Snippet Revision](classes/lib_SchSnippetRevision.md) (`lib_SchSnippetRevision`): A revision of a schematic snippet as saved into the Workspace at one point in time. · Artifact
- [Symbol](classes/lib_Symbol.md) (`lib_Symbol`): Symbol represents the logical schematic view of a Component, defining its electrical interface, pins, and attributes used to express circuit intent in design schematics. · Artifact · GRID `grid:workspace:{workspace-id}:library:symbol/{id}`
- [Symbol Revision](classes/lib_SymbolRevision.md) (`lib_SymbolRevision`): A revision of a Symbol: the schematic symbol as saved into the Workspace at one point in time, with its own lifecycle state. · Artifact · API DesSymbol · GRID `grid:workspace:{workspace-id}:library:symbol-revision/{id}`
