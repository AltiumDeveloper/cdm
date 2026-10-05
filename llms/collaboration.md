# Bounded context: collaboration

Models collaboration on Workspace content: comment threads attached to a point, object or area of a document, the individual comments in each thread, and tasks that assign work to users or teams. In the product, comments are placed on documents of Workspace projects (e.g. through the Comments and Tasks panel in Altium Designer), and tasks are tracked on the Tasks page of a Workspace.

HTML page: [subsets/collaboration/](../subsets/collaboration/)

## In the product

- [Document Commenting](https://www.altium.com/documentation/altium-designer/document-commenting) (primary)
- [Working with Tasks](https://www.altium.com/documentation/altium-365/tasks)
- [Altium 365 API](https://www.altium.com/documentation/altium-developer-center/altium-365/api#how_the_api_is_organized)

## Classes

- [Comment](classes/col_Comment.md) (`col_Comment`): A single entry in a comment thread: either the initial comment, pinned to a point, an object or an area of a design document (or to a BOM line), or a reply to it. · Resource · API DesComment
- [Comment Thread](classes/col_CommentThread.md) (`col_CommentThread`): Comment Thread represents a structured discussion linked to a specific design object, document, or workspace item, capturing feedback, decisions, and context directly within the collaborative design environment. · Activity · API DesCommentThread · GRID `grid:workspace:{workspace-id}:collaboration:comment-thread/{id}`
- [Task](classes/col_Task.md) (`col_Task`): Task represents a discrete unit of work assigned to a user or team within the design workflow, used to track progress, responsibility, and completion status for design, review, or management activities. · Activity · API DesTask · GRID `grid:workspace:{workspace-id}:collaboration:task/{id}`
