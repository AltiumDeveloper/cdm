# Changelog

All notable changes to the Common Data Model are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions are the `vX.Y.Z` git release tags
(the package version is derived from them by poetry-dynamic-versioning; the schema YAML carries no version).
Breaking changes (renames, removals, cardinality or parent-class changes) are prefixed **BREAKING:**.

## [Unreleased]

### Added
- Concept pages: Domain Model, Entity Classification and Relation Types.
- GRIDs page (top-level): GRIDs by bounded context (summary), format, and the catalogue of class GRID templates per bounded context.
- Glossary of product terms (class titles and `structured_aliases`; terms shared by several classes are noted as homonyms).
- Coverage dashboard: documentation coverage per bounded context.
- Bounded-context overview pages with landing links, coverage line and GRID templates.
- `cdm-gen-reference`: generates the relation, prefix and class-hierarchy reference tables, the GRID summary and catalogue for the GRIDs page, the glossary and the coverage page (`make gendoc`).
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
- `cdm-gendoc --findings` (exits 2 when `MODEL-FINDINGS.md` is missing).
- Subsets can declare `annotations: {productDocs: none}`; their page then states that no public product documentation exists (set on `core`).
- Reference pages (relations, prefixes, class hierarchy) in the site navigation.
- Snippet includes are checked (`pymdownx.snippets` `check_paths`).
- PR CI builds the documentation (`make gendoc` and `mkdocs build --strict`); `make gendoc` stops at the first failing step.

### Changed
- DOC-02 counts registry entries used by slots and subsets as used.
- `AGENTS.md`: the instance-URI rule is withdrawn (see MF-072); concept-page pointers name their sources.
- Class pages no longer show separate Documentation and Platform API boxes; API links use the canonical trailing-slash URLs.
- Class index tables link API types via the hub data (Nexar types link to the Octopart API docs).

### Fixed
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
