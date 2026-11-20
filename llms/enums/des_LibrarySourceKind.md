# Library Source Kind (des_LibrarySourceKind)

- Name: `des_LibrarySourceKind`
- IRI: `des:LibrarySourceKind` (https://w3id.org/altium/cdm/design/LibrarySourceKind)
- Kind: enumeration
- HTML page: [enums/des_LibrarySourceKind/](../../enums/des_LibrarySourceKind/)

Where a placed component was taken from.

## Values

| Value | Description |
| --- | --- |
| `Managed` | A managed component from the Workspace library, traceable to a component revision. |
| `FileLibrary` | A component from a file-based library (for example a SchLib), with no Workspace library item. |
| `Unknown` | The source could not be determined. |

## Referenced by

| From | Field | Cardinality | Relation |
| --- | --- | --- | --- |
| [des_PlacedComponent](../classes/des_PlacedComponent.md) | librarySourceKind | 0..1 |  |
