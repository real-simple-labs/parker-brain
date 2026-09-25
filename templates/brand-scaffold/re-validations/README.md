# Re-validations

Findings go stale. A validated answer about this brand's buyers or its account can quietly stop being true, so the ones that can decay get a re-check date.

## What lives here

- `scheduled/`: one file per finding due for a re-check, with the date it's due and what to re-run.
- `results/[YYYY-MM]/[loop-slug].md`: what the re-check found. A finding that moved is treated as a fresh finding and flows back into the docs it touches.

The weekly `/research-loops` routine checks `scheduled/` for anything past due. The method is in `parker-system/system/open-loops-system.md`.

A new brain starts with this folder empty.
