# Changelog

All notable changes to the Common Data Model are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions are the `vX.Y.Z` git release tags
(the package version is derived from them by poetry-dynamic-versioning; the schema YAML carries no version).
Breaking changes (renames, removals, cardinality or parent-class changes) are prefixed **BREAKING:**.

## [Unreleased]

### Added
- Bounded-context titles (`title` on every subset), matching the Altium 365 API reference names where the two differ: library is Library Management, configuration is Configuration Management.
- Concept pages: Domain Model, Entity Classification and Relation Types.
- About page (introduction): the model, its bounded contexts and entities, the APIs behind it, the class-page hub panel and `hub.json`.
- Bounded Contexts page: every bounded context with its classes and their API types (the generated schema index, the site home page).
- GRIDs page (top-level): format and the catalogue of class GRID templates (class title and template) per bounded context.
- Glossary of product terms (class titles and `structured_aliases`; terms shared by several classes are noted as homonyms).
- Bounded-context overview pages with landing links and GRID templates.
- `cdm-gen-reference`: generates the relation, prefix and class-hierarchy tables for the concept pages, the GRID catalogue for the GRIDs page and the glossary (`make gendoc`); it also generates the reference pages and a documentation coverage page for internal use, which are not published on the site.
- `llms.txt` for AI tools (`cdm-gen-llms`, published by an MkDocs hook): a catalogue per bounded context, a card per class and per enumeration, the concept pages and the glossary as plain markdown, `llms-ctx.txt` and `llms-full.txt`; the About page links them.
- Glossary: the class name is shown next to the class title.
- PROV-O, RO and BFO mappings on core classes and relations (`prov:` and `obo:` prefixes).
- DOC-01/DOC-04 checks for `see_also` and mappings on slots and subsets.
- Bounded-context descriptions (rewritten) and links to their product areas.
- Hub panel on class pages (product links and terms, Platform/Nexar API type, standards). API links are emitted unfiltered without `platform-docs-pages.json`, and the type name is shown without links without the Platform snapshot.
- `cdm-hub-export`: `hub.json` export of the documentation hub; `make gendoc` publishes it with `hub.schema.json`, and the test suite checks the export against the schema (not checked at export time).
- `nexarAPI` annotation for supply-chain types served by the Nexar (Octopart) API.
- Documentation hub foundations: link registry, API snapshots, lint rules DOC-01…DOC-05, link verifier.
- `cdm-gendoc`: registry-aware documentation generation (`make gendoc`).
- `cdm-api-snapshot` with checked-in Platform API and Nexar GraphQL schema snapshots (`make refresh-api-snapshot`); it also records existing API docs pages (`platform-docs-pages.json`).
- `cdm-gendoc --api-dir` (exits 2 if missing).
- `cdm-verify-links`: online verifier for registry links (`make verify-links`).
- `see_also` replaces `extensions: documentation` for product documentation links.
- PR CI workflow (`.github/workflows/pr.yaml`) running `make lint` and `tests/cdm_tools`.
- Governance files `VIOLATIONS.md` and `MODEL-FINDINGS.md`.
- Subsets can declare `annotations: {productDocs: none}`; their page then states that no public product documentation exists (set on `core`).
- Snippet includes are checked (`pymdownx.snippets` `check_paths`).
- PR CI builds the documentation (`make gendoc` and `mkdocs build --strict`); `make gendoc` stops at the first failing step.

### Changed
- Site look aligned with the Altium 365 API reference: Altium header and favicon, self-hosted Inter and JetBrains Mono, Altium blue in light and dark schemes, a sidebar listing every bounded context with its CDM colour and icon (no top tabs), header links to the API reference and the Developer Center, bounded-context cards on the home page, bounded-context titles and chips on subset and class pages.
- Root schema description: replaces the placeholder with a summary of the model.
- Bounded-context pages: the IRI of the context (`https://w3id.org/altium/cdm/<subset>`, resolvable through w3id.org) under the title; the GRID table and the "Identifier and Mapping Information" section are dropped.
- Class pages: the GRID template under the IRI as plain text (with copy buttons on hover for both); the bounded context is named by the breadcrumbs, class titles in the inheritance tree and in the Inheritance column of the fields table; the GRID box and the "Identifier and Mapping Information" section are dropped.
- Bounded-context pages link the same bounded context in the Altium 365 API reference ("In the API").
- Bounded-context pages list Entities, Resources, Events and Mixins (base types too for Core) in separate tables instead of one Classes table; the home-page cards count entities and resources, and the CDM's terms replace LinkML's "class" in table headings.
- Field pages: titled with the field title only; Properties before Used by; titles instead of technical names in the inheritance tree and the range; no IRI (not resolvable yet), "Identifier and Mapping Information" or "LinkML Source" sections; "Applicable Classes" is now "Used by".
- llms class cards carry what the class diagram shows: subclasses, and incoming relations as a table with cardinality and core relation (like the Attributes table for outgoing ones).
- Class diagrams: the site's font and greys, nodes in their bounded-context colour with a darker border and readable text, the current class emphasised, core base types no longer drawn as parents; lines, labels and the panel follow the light/dark scheme; a diagram wider than the column has an Expand button that opens it at full size.
- Instant navigation is off (class diagrams render only on a full page load).
- Site navigation: every bounded context in the sidebar expands to its entity classes (Artifacts and Activities), subclasses indented under their parent; breadcrumbs and a "View as Markdown" link (to the page's llms file) above each page; table headings never wrap.
- Comments use the Discussions of this repository (giscus) instead of the separate cdm-comments repository.
- DOC-02 counts registry entries used by slots and subsets as used.
- `AGENTS.md`: the instance-URI rule is withdrawn (see MF-072); concept-page pointers name their sources.
- Class pages no longer show separate Documentation and Platform API boxes; API links use the canonical trailing-slash URLs.
- Class index tables link API types via the hub data (Nexar types link to the Octopart API docs).

### Fixed
- Class diagrams render again: Mermaid is pinned (the floating `mermaid@11` tag moved to a release that showed a syntax error on every diagram), diagrams are rendered by `javascript/mermaid.mjs` from their source text, and they use the class `cdm-diagram`, which Material's own Mermaid integration leaves alone.
- Module ids of collaboration, configuration, customization and supply end with `/`, and core's id no longer has a doubled `/`, so each matches the namespace of its prefix.
- `hub.json`: an empty `grid` annotation is exported as `null`, not `"None"`.
- Platform API type names corrected against production for `des_RuleCheck`, `des_RuleCheckExecution`,
  `dm_ConfiguredDeviceModel`, `dm_AddressMap`, `dm_Memory`, `dm_Register`, `dm_RegisterField`,
  `dm_FieldEnum`, `dm_PortConfigurationEnumValue`, `dm_PortConfigurationDependency`, `sup_ReferenceDesign`;
  removed from `dm_Processor`; `sup_Part` and `sup_Offer` moved from `platformAPI` to `nexarAPI`;
  `sup_Company` gained `nexarAPI: SupCompany` (it had no API annotation before).
- `required: false` added to `dm_AddressMap_segments` (LINT-06).
- `GRID` type description aligned with the official GRID definition.
- AGENTS.md corrections: GRID format, relation tables, known violations, documentation hub conventions.
- Docs link GraphQL interface types correctly and use the public GRID page.
- Four `dm_Peripheral*` platformAPI names remain unresolved (not in production); tracked in MODEL-FINDINGS.md MF-050, MF-054–MF-056 and baselined as DOC-03 warnings.

## [0.0.12]

- Baseline for this changelog (see the v0.0.12 release).
