# v31 — the brand context file is brand-one-pager.md (2026-10-02)

The brand context file in a brand's brain is renamed from `brand-context/brand-context.md` to `brand-context/brand-one-pager.md`. Parker moves the file in each brain on its next sync of that brand; the context docs and the rest of the folder stay as they are. The map also names the other files in `brand-context/`, so the brain treats them as brand context too.

## What shipped

- **Brand `CLAUDE.md` template:** the map line names `brand-context/brand-one-pager.md`. A new line covers the other files in the folder (Parker's `README.md`, files Parker adds later, files the team puts there): they are important too, the brain reads the ones a task needs, and it doesn't rename, move or delete them.
- **`system/master-file-structure.md`:** the `brand-context/` entry names the new file and the other files.

## For the other Parker repos

- simple-ai#1747: the sync writes the new name, moves the file in brains synced under the old name, and removes the old name if a client brings it back.
- simple-ai#1746: Parker writes a `brand-context/README.md` into each brain that has none, and never overwrites one that is there.
- parker-desktop#498: Parker Desktop shows its read-only copy under the new name and removes an old copy left by an earlier version.

## Migration

`migrations/v31.md`: rename the file in the map line of `CLAUDE.md` (or add the line if there is none; if the team already added a line with the new name, remove the old one), and add the line for the other files in the folder. Nothing else; the file itself is moved by Parker. While a brain still has only the old file, the migration stops before it changes anything and does not record `v31`; the next `/update-brain` finishes it once Parker has moved the file.

Tag v31 only after simple-ai#1747 is deployed: from then on Parker writes only the new name, so a brain that gets its first sync after v31 never gets the old one. simple-ai#1747 went to production on 2026-10-02.
