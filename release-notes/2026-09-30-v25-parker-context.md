# v25 — `parker-context/` is read-only and stays out of the repo (2026-09-30)

Some of what a brain needs lives in Parker's database, not in the repo: first the brand context (the document every Parker chat starts from), later other documents Parker writes on a schedule. They change often, from the web app, the chat and the MCP, so reading them through GitHub on every chat would use up GitHub's rate limits. The plan is a folder, `parker-context/`, that Parker Desktop writes into each brain from the database, and that Parker's own tools show as part of the brain.

This release only gets brains ready for it. Nothing writes into `parker-context/` yet.

## What shipped

- **`.gitignore` seed.** The scaffold (`scripts/scaffold-brain.py`) writes a `.gitignore` with `parker-context/` into every new brain, so Parker Desktop's sync never commits the folder. The release manifest carries it; a fresh repo's starter `.gitignore` is replaced, like its `README.md`.
- **Read-only in both runtimes.** Claude Code: four `permissions.deny` rules in `.claude/settings.json`, the same shapes as the `parker-system/` ones. Codex: `"parker-context" = "read"` in the `parker-brain` filesystem profile. `mount-guard.py` is unchanged: it explains denials inside the method mount only, and `/disconnect-factory` still removes only the mount's rules.
- **Docs.** `system/brain-scaffold.md`, `system/codex-support.md`, `system/master-file-structure.md`, the bundle READMEs.
- **Tests.** `tests/test_runtime_hooks.py` checks both runtimes' rules; `tests/test_scaffold_brain.py` checks the `.gitignore` in the manifest. The offline Codex probe (`tests/probe_codex_runtime.py`) gained a `context-write` case: a script's write into an existing `parker-context/` is denied by the profile. Its other cases run with no `parker-context/` folder at all, which shows Codex (0.159.0, `--strict-config`) accepts the profile entry before the folder exists. Without the profile line, `context-write` fails.

## For the other Parker repos

- **Backend (mevin) and web app:** serve `parker-context/` from the database in `read_parker_brain` and the brain file viewer.
- **Parker Desktop:** write the folder from the database, read-only, and keep it out of the sync even where `.gitignore` lacks the line.

## Migration

`migrations/v25.md`: add `parker-context/` to the brain's `.gitignore` (the re-sync can't, since the file is the brain's own), and add the rules by hand only where the team edited `.claude/settings.json` or `.codex/config.toml`.
