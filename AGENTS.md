# AGENTS.md — Minimal Version

## 1. Class Naming
- `subsetName_ClassName`
- subset: camelCase  
- ClassName: PascalCase  
- `class_uri: subset:ClassName`
- Each class must appear in exactly one subset.

## 2. Slot Naming
- `subsetName_ClassName_fieldName`
- fieldName: camelCase
- `slot_uri: subset:ClassName_fieldName`
- `alias`: required, camelCase

## 3. Required Class Metadata
- class_uri  
- title  
- description  
- in_subset

## 4. Required Slot Metadata
- slot_uri  
- alias  
- title  
- description  
- range  
- multivalued  
- required

## 5. Subsets
- Classes: exactly one subset
- Slots: no subset
- Subset names: camelCase
- Nested subsets allowed (e.g., system-sdm)

## 6. URIs
Classes:
```
prefix:ClassName
```

Slots:
```
prefix:ClassName_fieldName
```

Instances:
```
https://w3id.org/altium/cdm/{subset}/{uuid}
```
- {uuid} must be UUID.

## 7. External Ontologies
- BFO: Optional  
- PROV-O: Recommended  
- SKOS: Recommended  
- Internal CDM: Required  

## 8. Agents
Agents must:
1. Avoid renaming classes unless asked  
2. Preserve ordering  
3. Preserve comments  
4. Avoid new prefixes  
5. Follow naming rules  
6. Propose diffs  
7. Run linkml-validate  
8. Regenerate JSON Schema  
9. Regenerate SHACL  
10. Create aliases  
11. Create class_uri/slot_uri  

## 9. Contributors
- PR review required  
- Example instance YAML: recommended  
- in_subset required  
- Regenerate JSON Schema, SHACL, Pydantic  
- Conventional commits  
- Changelog required  
- No folder-per-BC requirement  
- Linting required  (make lint)
- Project build required (make gen-project)
