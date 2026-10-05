# Bounded context: supply

Models the supply catalog: manufacturer parts with their aggregated sourcing data and distributor offers, the companies acting as their manufacturers or distributors, and the vendor-specific part family hierarchy, along with catalog content such as reference designs, evaluation kits, solution templates and software projects. Part, offer and company data correspond to the supply chain data that Octopart aggregates and serves through the Octopart API.

HTML page: [subsets/supply/](../subsets/supply/)

## In the product

- [Octopart](https://www.altium.com/documentation/altium-developer-center/octopart) (primary)
- [Octopart API](https://www.altium.com/documentation/altium-developer-center/octopart/api)
- [Adding Supply Chain Information to a Component](https://www.altium.com/documentation/altium-designer/components-libraries/adding-supply-chain-information-component)

## Classes

- [Company](classes/sup_Company.md) (`sup_Company`): Supply Company represents an organization in the electronics supply chain. · Artifact · Nexar SupCompany · GRID `grid:supply::platform:company/{id}`
- [Evaluation Kit](classes/sup_EvalKit.md) (`sup_EvalKit`): A vendor evaluation kit in the supply catalog, described by its associated devices, its reference designs (including a main one) and the software projects compatible with it. · Artifact · API SupEvalKit · GRID `grid:supply::platform:eval-kit/{id}`
- [Offer](classes/sup_Offer.md) (`sup_Offer`): Supply Offer represents a specific commercial listing of a Part from a supplier, detailing price breaks, stock availability, lead times, and ordering conditions at a given point in time. · Artifact · Nexar SupOffer · GRID `grid:supply::platform:part/{id}/offer/{offerID}`
- [Part](classes/sup_Part.md) (`sup_Part`): Supply Part represents a market-available instance of a manufactured Part, providing aggregated sourcing data such as pricing, stock levels, and supplier offers. · Artifact · Nexar SupPart · GRID `grid:supply::platform:part/{id}`
- [Part Family](classes/sup_PartFamily.md) (`sup_PartFamily`): A manufacturer's grouping of parts in the supply data, where the kind of family is vendor-specific (e.g. Series or Family). · Artifact · API SupPartFamily · GRID `grid:supply::platform:part-family/{id}`
- [Part Group](classes/sup_PartGroup.md) (`sup_PartGroup`): A leaf of the part family hierarchy in the supply data, holding the parts that belong to it together with group-level information such as its manufacturer, overview, key features and documents. · Artifact · API SupPartGroup · GRID `grid:supply::platform:part-group/{id}`
- [Reference Design](classes/sup_ReferenceDesign.md) (`sup_ReferenceDesign`): An example design published in the supply catalog, bringing together its design files (e.g. schematics and layouts), documentation and the parts it uses. · Artifact · API SupRefDesign · GRID `grid:supply::platform:ref-design/{id}`
- [Software Project](classes/sup_SoftwareProject.md) (`sup_SoftwareProject`): A software project published in the supply catalog, together with the evaluation kits it is compatible with. · Artifact · API SupSoftwareProject · GRID `grid:supply::platform:software-project/{id}`
- [Solution Template](classes/sup_SolutionTemplate.md) (`sup_SolutionTemplate`): A publisher's template for a solution, held in the supply catalog. · Artifact · API SupSolutionTemplate · GRID `grid:supply::platform:solution-template/{id}`
