# Known Violations (editorial record)

Human-curated companion to the machine baseline `cdm-lint.yaml` (see AGENTS.md §5).
A violation is **Fixed** only when the YAML conforms, the baseline no longer lists it after
`poetry run cdm-lint --baseline-out cdm-lint.yaml`, and this row is updated with the PR.

| ID | File | Element | Violation | Correct form | Breaking? | Status |
|---|---|---|---|---|---|---|
| V-001 | system.yaml | `system_SdmSystemModelVersion` | `class_uri: sys:SystemModelVersion` missing `Sdm` | `sys:SdmSystemModelVersion` | Yes (IRI) | Open |
| V-002 | system.yaml | `system_SdmSystemModel` | `class_uri: sys:SystemModel` missing `Sdm` | `sys:SdmSystemModel` | Yes (IRI) | Open |
| V-003 | system.yaml | `system_SdmMappableEntity` | `class_uri: sys:SdmEntity` does not match class name | `sys:SdmMappableEntity` | Yes (IRI) | Open |
| V-004 | system.yaml | `system_HardwareProject_hardwareComponents` | `alias: functionalBlocks` does not match field name | `alias: hardwareComponents` | Yes (Python/JSON name) | Open |
| V-005 | library.yaml | `lib_ComponentRevision_partChoiceList` | `title: partChoiceList` is camelCase (AGENTS.md §4.4 title format) | `title: part choice list` | No | Open |
| V-006 | library.yaml | `lib_PartChoiceList_partChoices` | `title: partChoices` is camelCase | `title: part choices` | No | Open |
| V-007 | supply.yaml | `sup_eval_kits` | `slot_uri: sup:consists_of_eval_kits`, `title: evalKits` | `slot_uri: sup:evalKits`, `title: eval kits` | Yes (IRI) | Open |

Note: CONV-02 only rejects underscores in titles, so V-005/V-006 are not caught by `cdm-lint`.
