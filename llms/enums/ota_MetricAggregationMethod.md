# Metric Aggregation Method (ota_MetricAggregationMethod)

- Name: `ota_MetricAggregationMethod`
- IRI: `ota:MetricAggregationMethod` (https://w3id.org/altium/cdm/ota/MetricAggregationMethod)
- Kind: enumeration
- HTML page: [enums/ota_MetricAggregationMethod/](../../enums/ota_MetricAggregationMethod/)

The method used to aggregate the values a device reported within one time bucket.

## Values

| Value | Description |
| --- | --- |
| `Last` | The last value reported in the bucket. |
| `Average` | The average of the values reported in the bucket. |
| `Max` | The highest value reported in the bucket. |
| `Min` | The lowest value reported in the bucket. |
| `Count` | The number of values reported in the bucket. |
| `Raw` | The values are not aggregated; each data point is a reported value. Corresponds to none in provider APIs. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_MetricSeries](../classes/ota_MetricSeries.md) | aggregationMethod | 0..1 |  |
