# Metric Data Point (ota_MetricDataPoint)

- Name: `ota_MetricDataPoint`
- IRI: `ota:MetricDataPoint` (https://w3id.org/altium/cdm/ota/MetricDataPoint)
- Bounded context: [ota](../ota.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/ota_MetricDataPoint/](../../classes/ota_MetricDataPoint/)

Metric Data Point is the value of a metric at a point in time.

## Attributes

| Field | Range | Cardinality | Description | Relation | Inherited from |
| --- | --- | --- | --- | --- | --- |
| timestamp | datetime | 1 | The timestamp of the data point, in UTC. |  |  |
| value | float | 0..1 | The metric value. |  |  |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [ota_MetricSeries](ota_MetricSeries.md) | dataPoints | * |  |
