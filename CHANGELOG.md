# Changelog

All notable changes to the Common Data Model are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `deviceModel`: shared slots `dm_deviceFamily` (alias `deviceFamily`) and
  `dm_deviceFramework` (alias `deviceFramework`), both optional strings, applied to
  `dm_ConfiguredDeviceModel`, `dm_FullStackDeviceModel` and `system_SdmDeviceModel`.
  Both names match the platform GraphQL API: `deviceFamily` is the stable family key
  (`RA`, `RAFW`, `RX`) exposed as `DmDeviceFamily.key`, and `deviceFramework` is the
  driver framework (`FSP`, `FIT`) that the software side calls `ecosystem`.

### Changed

- BREAKING: `system`: added the missing `Sdm` segment to two class URIs.
  `system_SdmSystemModel` moves from `sys:SystemModel` to `sys:SdmSystemModel`, and
  `system_SdmSystemModelVersion` from `sys:SystemModelVersion` to
  `sys:SdmSystemModelVersion`. This changes the OWL, RDF and SHACL IRIs of both classes,
  so external ontology consumers must be updated. Clears the violation recorded in
  AGENTS.md section 5.
- `deviceModel`: `dm_ConfiguredDeviceModel` now annotates
  `platformAPI: DmDeviceModelAsConfigured`. The previous value,
  `DmConfiguredDeviceModel`, names no type in the platform gateway.
- `system`: `sdmReferenceDesignator` on the `system_HasSdmReferenceDesignator` mixin is
  now optional. A reference designator is assigned by the hardware design tool once
  parts are placed, so a producer compiling an SDM earlier in the flow has no value to
  supply. The mixin also applies to `system_SdmSoftwareModel` and
  `system_SdmSoftwareComponent`, which have no reference designator at all.
- `system`: `dependencyIds` on `system_SdmSoftwareStackInstance` is now optional. The
  slot is self-referential, so requiring a non-empty list meant the dependency graph
  could never terminate at a leaf.

Both relaxations keep previously valid data valid, but consumers must now handle the
fields being absent.

### Deprecated

- `deviceModel`: `dm_FullStackDeviceModel_family` (alias `family`), superseded by the
  shared `dm_deviceFamily` slot. The field stays required, so populate both until
  consumers have migrated.

### Fixed

- Tests: `tests/clients/esd_client.py` and `tests/test_flows.py` referenced datamodel
  classes under their pre-rename `SystemSm*` and `SystemSystemModel` names, which broke
  pytest at collection. Updated to the current `SystemSdm*` names.
- Tests: `test_esd_basic_flow` passes again. It had been failing since 2026-02-25, when
  commit 26591d1 landed three schema changes the test was never updated for:
  `compile_sdm` returns a version snapshot, so `ESDClient.latest_sdm` is now a
  `SystemSdmSystemModelVersion` rather than a `SystemSdmSystemModel`; a software library
  item now becomes a `SystemSdmSoftwareStackInstance` that carries the specification,
  with the component referencing it through `implementedBy`; and
  `tests/data/esd_basic_flow.json` was regenerated to match.

### Known issues

- 16 `platformAPI` annotations still name types the platform gateway does not expose,
  across `device_model.yaml`, `design.yaml` and `supply.yaml`.
