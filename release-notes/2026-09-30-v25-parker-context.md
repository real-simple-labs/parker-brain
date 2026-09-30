# v25 — `parker-context/` stays out of the repo (2026-09-30)

Some of what a brain knows about its brand lives in Parker's database, not in the repo: first the brand context (the document every Parker chat starts from), later more. It changes often, from the web app, the chat and the MCP, so reading it through GitHub on every chat would use up GitHub's rate limits. The plan is a folder, `parker-context/`, that Parker Desktop keeps in sync with the database in both directions, and that Parker's own tools show as part of the brain. The team and their agents read and edit it like any other folder; Parker Desktop saves their edits back to Parker.

This release only gets brains ready for it: git ignores the folder. Nothing writes into `parker-context/` yet.

## What shipped

- **`.gitignore` seed.** The scaffold (`scripts/scaffold-brain.py`) writes a `.gitignore` with `parker-context/` into every new brain (template: `templates/brand-scaffold/gitignore`, with no leading dot so it doesn't act on the factory itself), so Parker Desktop's git sync never commits the folder. The release manifest carries it; a fresh repo's starter `.gitignore` is replaced, like its `README.md`.
- **Docs.** `system/brain-scaffold.md`, `system/master-file-structure.md`.
- **Tests.** `tests/test_scaffold_brain.py` checks the `.gitignore` in the manifest.

## For the other Parker repos

- **Backend (mevin) and web app:** serve `parker-context/` from the database in `read_parker_brain` and the brain file viewer.
- **Parker Desktop:** keep the folder in sync with the database in both directions: download changes, upload local edits with a version check, and show a clash when both sides changed. Keep the folder out of the git sync even where `.gitignore` lacks the line.

## Migration

`migrations/v25.md`: move away any files the team already keeps under `parker-context/` (a file move, never `git rm --cached`, which would delete them from teammates' copies), then add `parker-context/` to the brain's `.gitignore`. The re-sync can't do it, since the file is the brain's own.
