# v20 — the mount is a check first (2026-09-15)

Parker Desktop attaches the method mount itself when it creates a brand new brain (real-simple-labs/parker-desktop#362): `parker-system` as a submodule of the public factory at the newest release, staged and committed by the app's first sync. The build that follows needs no git.

## What shipped

- **Runner, Phase 0 step 5:** checks for an existing mount before adding one. If `git submodule status` lists `parker-system` at a release, the mount is done; an older app, or a self-managed repo, still runs the add with the user's approval, per v19.
- **`system/brain-sync.md`:** the cross-team duties from v19 are done app-side; the app's guide files name the one remaining exception, the library's pin.
- **`system/codex-support.md`:** the Codex sandbox limit now applies only to app versions that don't attach the mount.

## Migration

`migrations/v20.md` is a no-op.
