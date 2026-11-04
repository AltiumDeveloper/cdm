# Metric Series (ota_MetricSeries)

- Name: `ota_MetricSeries`
- IRI: `ota:MetricSeries` (https://w3id.org/altium/cdm/ota/MetricSeries)
- Bounded context: [ota](../ota.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/ota_MetricSeries/](../../classes/ota_MetricSeries/)

Metric Series is the time series of one metric reported by a device, with the values in each time bucket aggregated by one method.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | The metric name, for example mem_free. |  |  |
| aggregationMethod | [ota_MetricAggregationMethod](../enums/ota_MetricAggregationMethod.md) | 0..1 | The method used to aggregate values within each time bucket. |  |  |
| aggregationBucket | string | 0..1 | The length of each aggregation bucket as reported by the provider. |  |  |
| dataPoints | [ota_MetricDataPoint](ota_MetricDataPoint.md) | * | The data points of the metric series. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_DeviceMetrics](ota_DeviceMetrics.md) | series | * |  |
