# Zotero Integration Map

Use the installed Zotero helper instead of rediscovering profiles, ports, or routes manually.

## Read-only operations

- `status`, `probe`
- `inventory`, `collections`, `tags`, `groups`
- `search`
- `export-bibtex`, `sync-bib`, `citations`
- `children`
- `fulltext`, `file-url` when the user requests attachment/full-text access

`cite` edits a local draft and bibliography, so keep it within the user's requested file scope.

## Writes requiring explicit authorization

- `import-bibtex`
- `import-ris`
- connector save/import actions
- deletion, metadata correction, collection changes, or attachment changes

## Source ownership

- Zotero parent item key and citation key are different identifiers; preserve both when available.
- Zotero owns bibliography and attachment management.
- Research Vault owns derived notes, evidence traces, comparisons, and synthesis.
- Do not duplicate PDFs into the vault by default.

## Failure behavior

- If Zotero Desktop is not running, report the exact readiness state.
- Do not enable, restart, or modify Zotero unless operating Zotero is part of the task.
- If a local item is missing, search authoritative external sources rather than inventing metadata.
- If a write is not authorized, complete all possible read-only work and stop at the write boundary.
