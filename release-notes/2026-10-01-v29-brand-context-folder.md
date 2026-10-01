# v29 — the brand context is a file of the brain (2026-10-01)

Parker's brand context (the document Parker's chat reads for a brand in every conversation, `brand_personas.persona_full`) is now also `brand-context/brand-context.md` in the brand's brain, an ordinary tracked file. The team edits it like any other file (Parker Desktop, an agent); Parker's chat keeps reading its database copy, so chat costs no GitHub calls.

## What shipped

- **Brand `CLAUDE.md` template:** "## The map" names `brand-context/brand-context.md`: when it is there, it is the brand context and Parker syncs it both ways; when it isn't, Parker hasn't synced the brain yet and the file isn't to be made by hand. The folder never says whether the brain is built.
- **`system/master-file-structure.md`:** the `brand-context/` entry; `parker-context/` is marked unused (its `.gitignore` line from v25 stays, harmless).
- **`system/brain-scaffold.md`:** the `.gitignore` seed's note follows. The scaffold itself is unchanged: Parker writes `brand-context/` on its first sync, not at scaffold time.

## For the other Parker repos

- simple-ai#1732: the sync. A cron writes a changed brand context into each set-up brain; the GitHub App's push webhook brings edits back. Off until `BRAND_CONTEXT_BRAIN_SYNC=on` (the backfill).
- simple-ai#1733: the web brain view shows the file; the old brand context page goes.
- parker-desktop#496 / #497: the Desktop shows the file in every brain (read-only until the brain has it in git, then editable).

## Migration

`migrations/v29.md`: add the `brand-context/brand-context.md` line to "## The map" in `CLAUDE.md`. Nothing else; the file arrives from Parker.
