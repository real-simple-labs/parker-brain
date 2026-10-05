# v32 — a README in each folder the brain fills (2026-10-05)

A new brain now shows its shape before anything is built. Each folder the build and the team fill starts with a short `README.md`: what the folder will hold, and which `parker-system/` prompts and skills write it. Before, these folders didn't exist until their first doc was written, so a scaffolded brain showed only its method files.

## What shipped

- **Ten folder READMEs** in `templates/brand-scaffold/`, seeded by `scripts/scaffold-brain.py`: `sub-context-docs/`, `personas/`, `source-pulls/`, `competitors/`, `audits/`, `strategy/`, `idea-bank/`, `sprints/`, `briefs/`, `expert-insights/`. They join the six living-layer READMEs the scaffold already wrote.
- **A README is not a doc.** Every README says so in its first line, and the brand `CLAUDE.md` template's map says so too. The `INDEX.md` steps in `/refresh-context` and in the build's closeout leave it out. The earlier rule kept these folders empty for exactly this reason: a README among the docs is noise in a synthesis prompt's input.
- **`system/brain-scaffold.md`** and **`system/master-file-structure.md`** describe the new seeds.

## For the other Parker repos

None needed. Parker's backend scaffolds new brains from this release's `brain-scaffold.json`, which now carries the ten READMEs. The brand context sync is unaffected: it writes only `brand-context/`.

## Migration

`migrations/v32.md`: add each of the ten READMEs a brain doesn't have yet (never overwrite one), add the map line to `CLAUDE.md`, and remove a README line from `competitors/INDEX.md` or `audits/INDEX.md` if one got in.
