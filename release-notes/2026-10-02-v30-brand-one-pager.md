# v30 — the brand context file is brand-one-pager.md (2026-10-02)

The brand context file in a brand's brain is renamed from `brand-context/brand-context.md` to `brand-context/brand-one-pager.md`. Parker moves the file in each brain on its next sync of that brand; the context docs and the rest of the folder stay as they are.

## What shipped

- **Brand `CLAUDE.md` template:** the map line names `brand-context/brand-one-pager.md`.
- **`system/master-file-structure.md`:** the `brand-context/` entry names the new file.

## For the other Parker repos

- simple-ai#1747: the sync writes the new name, moves the file in brains synced under the old name, and removes the old name if a client brings it back.
- parker-desktop#498: Parker Desktop shows its read-only copy under the new name and removes an old copy left by an earlier version.

## Migration

`migrations/v30.md`: rename the file in the map line of `CLAUDE.md` (or add the line if there is none). Nothing else; the file itself is moved by Parker. While a brain still has only the old file, the migration stops before it changes anything and does not record `v30`; the next `/update-brain` finishes it once Parker has moved the file.

Tag v30 only after simple-ai#1747 is deployed: from then on Parker writes only the new name, so a brain that gets its first sync after v30 never gets the old one.
