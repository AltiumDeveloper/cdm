# Bounded context: core

Holds the abstract foundations shared by every bounded context: the base classes Entity (specialised as Artifact and Activity), Resource and Event; the mixins that add annotations such as GRID, maturity and API type; shared slots such as id and name; and the abstract relations (e.g. part of, input of, derived from) that domain relations specialise. It is not a product area and has no product documentation of its own.

HTML page: [subsets/core/](../subsets/core/)

## In the product

No public product documentation exists for this bounded context.

## Base classes and mixins

- [Activity](classes/core_Activity.md) (`core_Activity`): Abstract base for process and work objects — things that happen, use inputs, and produce outputs. · Activity, abstract
- [Artifact](classes/core_Artifact.md) (`core_Artifact`): Abstract base for persistent data objects that are created, stored, versioned, and consumed. · Artifact, abstract
- [Entity](classes/core_Entity.md) (`core_Entity`): Abstract base for all identifiable, versioned, platform-accessible domain objects. · Entity, abstract
- [Event](classes/core_Event.md) (`core_Event`): Abstract base for domain events. · Event, abstract
- [Meta](classes/core_Meta.md) (`core_Meta`): Abstract base for all CDM mixin classes. · abstract
- [Resource](classes/core_Resource.md) (`core_Resource`): Abstract base for lightweight platform-accessible objects that have API access but are not Entities; they carry no GRID and no versioning lifecycle. · Resource, abstract
- [With GRID](classes/core_WithGRID.md) (`core_WithGRID`): Mixin that adds a GRID annotation slot to a class. · mixin
- [With Maturity](classes/core_WithMaturity.md) (`core_WithMaturity`): Mixin that adds a maturity annotation slot indicating the lifecycle readiness level. · mixin
- [With Platform API](classes/core_WithPlatformAPI.md) (`core_WithPlatformAPI`): Mixin that adds API type annotations: platformAPI names the Altium 365 Platform API GraphQL type; nexarAPI names the Nexar (Octopart) GraphQL type for supply-chain entities served by Nexar rather than the Platform API. · mixin
- [With Vault](classes/core_WithVault.md) (`core_WithVault`): Mixin that adds a vault content type annotation to a class, indicating how its content is stored in the platform vault. · mixin
- [With Vault Link](classes/core_WithVaultLink.md) (`core_WithVaultLink`): Mixin that adds vault link parent, child, and type annotation slots for tracking hierarchical vault relationships. · mixin

## Classes without a bounded context

- [Any](classes/Any.md)
- [dm_HasAddressRange](classes/dm_HasAddressRange.md): A mixin for entities that occupy a specific span of the memory map. · abstract, mixin
- [system_HasSdmReferenceDesignator](classes/system_HasSdmReferenceDesignator.md): A mixin for entities within the System Data Model (SDM) that are identifiable by reference designators · abstract, mixin
- [system_SdmMappableEntity](classes/system_SdmMappableEntity.md): A mixin for entities within the System Data Model (SDM) that are mappable to domain-specific concepts · abstract, mixin
