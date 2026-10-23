# Design Review Status (col_DesignReviewStatus)

- Name: `col_DesignReviewStatus`
- IRI: `col:DesignReviewStatus` (https://w3id.org/altium/cdm/collaboration/DesignReviewStatus)
- Kind: enumeration
- HTML page: [enums/col_DesignReviewStatus/](../../enums/col_DesignReviewStatus/)

The state of a design review.

## Values

| Value | Description |
| --- | --- |
| `InProgress` | The review is open; Reviewers can complete their tasks. |
| `Completed` | The Initiator closed the review as completed; it can no longer be changed. |
| `Rejected` | The Initiator closed the review as rejected; it can no longer be changed. |
| `Cancelled` | The Initiator or a Reviewer cancelled the review; its tasks are resolved and it can no longer be changed. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [col_DesignReview](../classes/col_DesignReview.md) | status | 1 |  |
