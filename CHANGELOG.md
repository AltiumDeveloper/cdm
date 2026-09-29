# Changelog

All notable changes to the Common Data Model are documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow the `vX.Y.Z` release tags
and `version:` in `src/common_data_model/schema/common_data_model.yaml`.
Breaking changes (renames, removals, cardinality or parent-class changes) are prefixed **BREAKING:**.

## [Unreleased]

### Added
- `nexarAPI` annotation for supply-chain types served by the Nexar (Octopart) API.
- Documentation hub foundations: link registry, API snapshots, lint rules DOC-01…DOC-05, link verifier.
- `cdm-gendoc`: registry-aware documentation generation (`make gendoc`).
- `cdm-api-snapshot` with checked-in Platform API and Nexar GraphQL schema snapshots (`make refresh-api-snapshot`).
- `cdm-verify-links`: online verifier for registry links (`make verify-links`).
- `see_also` replaces `extensions: documentation` for product documentation links.
- PR CI workflow (`.github/workflows/pr.yaml`) running `make lint` and `tests/cdm_tools`.
- Governance files `VIOLATIONS.md` and `MODEL-FINDINGS.md`.
- Schema `version: 0.10.0`.

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

## [0.10.0]

- Baseline for this changelog (see the v0.10.0 release tag).
