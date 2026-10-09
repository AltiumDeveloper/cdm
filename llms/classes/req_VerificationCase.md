# Verification Case (req_VerificationCase)

- Name: `req_VerificationCase`
- IRI: `req:VerificationCase` (https://w3id.org/altium/cdm/requirement/VerificationCase)
- Bounded context: [requirements](../requirements.md)
- Kind: Activity
- Is a: [core_Activity](core_Activity.md)
- Maturity: EXPERIMENTAL
- HTML page: [classes/req_VerificationCase/](../../classes/req_VerificationCase/)

A planned verification procedure or test that produces objective evidence against requirements.

## In the product

- [Verification & Validation Module](https://www.altium.com/documentation/altium-365/requirements-portal/verification-validation-module) (primary)
- [Flow 1: Plan Verification Activities](https://www.altium.com/documentation/altium-365/requirements-portal/verification-validation-module/flow-1-plan-verification-activities)
- Term: **V&V Activity** (related; altium-365)

## GRID

`grid:workspace:{workspace-id}:requirements:verification-case/{id}`

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| identifier | string | 1 | External-facing identifier or document number for the verification case. |  |  |
| method | string | 1 | Verification technique such as analysis, inspection, demonstration, or test. |  |  |
| environment | string | 0..1 | Description of lab, simulation, or operational context for execution. |  |  |
| result | string | 0..1 | Pass/fail or summary of latest execution outcome. |  |  |
| validatesRequirements | [req_Requirement](req_Requirement.md) | 1..* | Requirements validated by executing this verification case. |  |  |
| usesArtifacts | [req_Artifact](req_Artifact.md) | * | Test articles, prototypes, or simulations consumed during verification. |  |  |
| generatesEvidence | [req_Artifact](req_Artifact.md) | * | Reports, datasets, or other artifacts captured as verification evidence. |  |  |
| triggersChanges | [req_RequirementChangeRequest](req_RequirementChangeRequest.md) | * | Change requests created due to verification findings. |  |  |
| id | GRID | 1 | Globally unique identifier across the whole platform. |  | [core_Entity](core_Entity.md) |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [req_Project](req_Project.md) | verificationCases | * |  |
