# Design Review Status (des_DesignReviewStatus)

- Name: `des_DesignReviewStatus`
- IRI: `des:DesignReviewStatus` (https://w3id.org/altium/cdm/design/DesignReviewStatus)
- Kind: enumeration
- HTML page: [enums/des_DesignReviewStatus/](../../enums/des_DesignReviewStatus/)

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
| [des_DesignReview](../classes/des_DesignReview.md) | status | 1 |  |
