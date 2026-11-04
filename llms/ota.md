# Bounded context: Over-the-Air Updates

Models over-the-air (OTA) firmware and software updates: devices with the packages installed on them, fleets that group devices, packages with their version, size, checksums and target hardware, deployments that request packages to be rolled out to a device or fleet, the deployment results that record the outcome on each targeted device, and the metrics reported by devices. All classes are experimental.

HTML page: [subsets/ota/](../subsets/ota/)

## In the product

No public product documentation exists for this bounded context.

## Classes

- [Deployment](classes/ota_Deployment.md) (`ota_Deployment`): Deployment represents the request for an OTA update that assigns packages to the ECUs of its target, either a single device or all devices of a single fleet. · Activity · GRID `grid:workspace:{workspace-id}:ota:deployment/{id}`
- [Deployment Assignment](classes/ota_DeploymentAssignment.md) (`ota_DeploymentAssignment`): Deployment Assignment assigns a package to the ECUs with a given hardware identifier. · Resource
- [Deployment Result](classes/ota_DeploymentResult.md) (`ota_DeploymentResult`): Deployment Result is the outcome of a deployment on one target device, from the time the device is addressed by the deployment, before its update is created. · Artifact · GRID `grid:workspace:{workspace-id}:ota:deployment-result/{id}`
- [Device](classes/ota_Device.md) (`ota_Device`): Device represents a physical unit registered for OTA updates. · Artifact · GRID `grid:workspace:{workspace-id}:ota:device/{id}`
- [Device Metrics](classes/ota_DeviceMetrics.md) (`ota_DeviceMetrics`): The metric series reported by one device. · Resource
- [Fleet](classes/ota_Fleet.md) (`ota_Fleet`): Fleet represents a named group of devices managed and updated together. · Artifact · GRID `grid:workspace:{workspace-id}:ota:fleet/{id}`
- [Metric Data Point](classes/ota_MetricDataPoint.md) (`ota_MetricDataPoint`): Metric Data Point is the value of a metric at a point in time. · Resource
- [Metric Series](classes/ota_MetricSeries.md) (`ota_MetricSeries`): Metric Series is the time series of one metric reported by a device, with the values in each time bucket aggregated by one method. · Resource
- [Package](classes/ota_Package.md) (`ota_Package`): Package represents one version of a software package registered for OTA deployment. · Artifact · GRID `grid:workspace:{workspace-id}:ota:package/{id}`
- [Package Hash](classes/ota_PackageHash.md) (`ota_PackageHash`): Package Hash is a checksum of a package binary, used for Uptane target metadata. · Resource
