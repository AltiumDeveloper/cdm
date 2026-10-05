# Comment (col_Comment)

- Name: `col_Comment`
- IRI: `col:Comment` (https://w3id.org/altium/cdm/collaboration/Comment)
- Bounded context: [collaboration](../collaboration.md)
- Kind: Resource
- Is a: [core_Resource](core_Resource.md)
- HTML page: [classes/col_Comment/](../../classes/col_Comment/)

A single entry in a comment thread: either the initial comment, pinned to a point, an object or an area of a design document (or to a BOM line), or a reply to it. A comment can mention people or groups using @, and it can be assigned to a Workspace member as a task, either when it is posted or later by converting it. Only the author can edit or delete a comment, and deleting the initial comment also deletes its replies.

## In the product

- [Web Viewer](https://www.altium.com/documentation/altium-365/viewers/web-viewer#comment_placement) (primary)

## In the API

- Platform API type: [`DesComment`](https://altiumdeveloper.github.io/platform-api-docs/types/objects/DesComment/) (object)

## Referenced by

- [col_CommentThread](col_CommentThread.md): `comments`
