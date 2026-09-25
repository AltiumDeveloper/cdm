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

### Deprecated

- `deviceModel`: `dm_FullStackDeviceModel_family` (alias `family`), superseded by the
  shared `dm_deviceFamily` slot. The field stays required, so populate both until
  consumers have migrated.

### Fixed

- Tests: `tests/clients/esd_client.py` and `tests/test_flows.py` referenced datamodel
  classes under their pre-rename `SystemSm*` and `SystemSystemModel` names, which broke
  pytest at collection. Updated to the current `SystemSdm*` names.

### Known issues

- `tests/test_flows.py::test_esd_basic_flow` still fails. `ESDClient` builds a
  `SystemSdmSystemModel` with `version`, `functionalModel`, `deviceModels`,
  `softwareModels` and `hardwareModels`, but those fields now belong to
  `SystemSdmSystemModelVersion`. The client needs restructuring for the model/version
  split, and the `tests/data/esd_basic_flow.json` fixture needs regenerating.
- 16 `platformAPI` annotations still name types the platform gateway does not expose,
  across `device_model.yaml`, `design.yaml` and `supply.yaml`.
