# With Platform API (core_WithPlatformAPI)

- Name: `core_WithPlatformAPI`
- IRI: `core:WithPlatformAPI` (https://w3id.org/altium/cdm/core/WithPlatformAPI)
- Bounded context: [core](../core.md)
- Kind: mixin
- Is a: [core_Meta](core_Meta.md)
- HTML page: [classes/core_WithPlatformAPI/](../../classes/core_WithPlatformAPI/)

Mixin that adds API type annotations: platformAPI names the Altium 365 Platform API GraphQL type; nexarAPI names the Nexar (Octopart) GraphQL type for supply-chain entities served by Nexar rather than the Platform API; adSDK names the Altium Designer SDK types (namespace-qualified, comma-separated, e.g. "EDP.INet, PCB.IPCB_Net") that expose the same concept inside Altium Designer.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| platformAPI | string | 0..1 | Altium 365 Platform API type name. |  |  |
| nexarAPI | string | 0..1 | Nexar (Octopart) API type name. |  |  |
| adSDK | string | 0..1 | Altium Designer SDK type names, namespace-qualified and comma-separated (reference https://altiumdeveloper.github.io/ad-sdk-docs/reference/). |  |  |
