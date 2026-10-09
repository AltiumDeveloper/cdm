# Requirement Artifact (req_Artifact)

- Name: `req_Artifact`
- IRI: `req:Artifact` (https://w3id.org/altium/cdm/requirement/Artifact)
- Bounded context: [requirements](../requirements.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/req_Artifact/](../../classes/req_Artifact/)

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [req_Project](req_Project.md) | artifacts | * |  |
| [req_Requirement](req_Requirement.md) | satisfiedByArtifacts | * |  |
| [req_Requirement](req_Requirement.md) | tracedFromSources | * |  |
| [req_RequirementSpecification](req_RequirementSpecification.md) | inputs | * |  |
| [req_VerificationCase](req_VerificationCase.md) | generatesEvidence | * |  |
| [req_VerificationCase](req_VerificationCase.md) | usesArtifacts | * |  |
