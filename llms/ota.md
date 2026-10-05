# Bounded context: ota

Models over-the-air (OTA) firmware and software updates: devices with their status and installed packages, fleets that group devices, and packages with their version, size, checksums and target hardware. All classes are experimental.

HTML page: [subsets/ota/](../subsets/ota/)

## In the product

No public product documentation exists for this bounded context.

## Classes

- [Device](classes/ota_Device.md) (`ota_Device`): Artifact · GRID `grid:workspace:{workspace-id}:ota:device/{id}`
- [Fleet](classes/ota_Fleet.md) (`ota_Fleet`): Artifact · GRID `grid:workspace:{workspace-id}:ota:fleet/{id}`
- [Package](classes/ota_Package.md) (`ota_Package`): Artifact · GRID `grid:workspace:{workspace-id}:ota:package/{id}`
