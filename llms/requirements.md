# Bounded context: requirements

Models requirements and their revisions, the specifications that group them, baselines approved for execution, change requests, the requirements projects that scope this work, and verification cases that provide evidence against requirements; most of its classes are experimental. It corresponds to requirements management and verification & validation in the Altium 365 Requirements Portal.

HTML page: [subsets/requirements/](../subsets/requirements/)

## In the product

- [Requirements Portal](https://www.altium.com/documentation/altium-365/requirements-portal) (primary)
- [Features Explained](https://www.altium.com/documentation/altium-365/requirements-portal/features-explained)
- [Working with Requirements](https://www.altium.com/documentation/altium-365/requirements-integration)

## Classes

- [Requirement](classes/req_Requirement.md) (`req_Requirement`): A single, testable statement of intent or constraint that governs a solution or process outcome. · Artifact · GRID `grid:workspace:{workspace-id}:requirements:requirement/{id}`
- [Requirement Artifact](classes/req_Artifact.md) (`req_Artifact`): Resource
- [Requirement Baseline](classes/req_RequirementBaseline.md) (`req_RequirementBaseline`): A version-managed release of a specification or subset of requirements approved for execution. · Artifact · GRID `grid:workspace:{workspace-id}:requirements:baseline/{id}`
- [Requirement Change Request](classes/req_RequirementChangeRequest.md) (`req_RequirementChangeRequest`): Structured workflow item proposing additions, updates, or removals of requirements. · Activity · GRID `grid:workspace:{workspace-id}:requirements:change-request/{id}`
- [Requirement Revision](classes/req_RequirementRevision.md) (`req_RequirementRevision`): An immutable snapshot of a requirement statement at a specific revision. · Artifact · GRID `grid:workspace:{workspace-id}:requirements:requirement-revision/{id}`
- [Requirement Specification](classes/req_RequirementSpecification.md) (`req_RequirementSpecification`): A curated collection of requirements scoped to a program, domain, or release horizon. · Artifact · GRID `grid:workspace:{workspace-id}:requirements:specification/{id}`
- [Requirements Project](classes/req_Project.md) (`req_Project`): The orchestration space for capturing, evolving, and validating requirements scoped to a product, program increment, or regulatory engagement. · Activity · GRID `grid:workspace:{workspace-id}:requirements:project/{id}`
- [Verification Case](classes/req_VerificationCase.md) (`req_VerificationCase`): A planned verification procedure or test that produces objective evidence against requirements. · Activity · GRID `grid:workspace:{workspace-id}:requirements:verification-case/{id}`
