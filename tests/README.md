# CDM Test Suite

## Test Fixtures

### Kame_fmu_desingdata.json

The design validation tests (`test_design_validation.py`) require a real ModelsProvider JSON export file named `Kame_fmu_desingdata.json`.

**This file is gitignored and must be placed manually.**

#### Placement

Copy the file to the **repository root** (not the `tests/` directory):

```
cdm/
├── Kame_fmu_desingdata.json   ← place here
├── src/
├── tests/
│   ├── test_design_validation.py
│   ├── udm_to_cdm_transformer.py
│   └── ...
```

#### How to Obtain

1. Request the file from the CDM team or your project lead
2. The file is a JSON export from Altium Designer's ModelsProvider (UDM design data for the "Kame FMU" project)
3. Expected size: ~2.6 MB

#### Verification

After placing the file, run:

```bash
pytest tests/test_design_validation.py -v
```

All 14 tests should pass. If you see `FileNotFoundError`, the file is not in the correct location.

#### Important

- **Do NOT commit this file** — it is listed in `.gitignore`
- The file contains real design data and should be treated as proprietary
- Tests that depend on this fixture will be skipped or fail if the file is absent
