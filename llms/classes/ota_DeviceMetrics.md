# Device Metrics (ota_DeviceMetrics)

- Name: `ota_DeviceMetrics`
- IRI: `ota:DeviceMetrics` (https://w3id.org/altium/cdm/ota/DeviceMetrics)
- Bounded context: [ota](../ota.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/ota_DeviceMetrics/](../../classes/ota_DeviceMetrics/)

The metric series reported by one device.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| device | [ota_Device](ota_Device.md) | 1 | The device associated with the metrics. |  |  |
| series | [ota_MetricSeries](ota_MetricSeries.md) | * | The metric series reported by the device. |  |  |
