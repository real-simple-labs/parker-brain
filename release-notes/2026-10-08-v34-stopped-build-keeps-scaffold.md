# v34 — a cancelled build goes back to the scaffold (2026-10-08)

A customer started a build in Parker Desktop on a brand the backend had not scaffolded, so the build's Phase 0 laid the scaffold down itself (191 files). An hour later, in Phase 1, the build was stopped. The runner had no rule for a stop, so the model reset the folder to how it was before the build: it deleted all 213 files the build had added, the scaffold and the `.scaffolded` marker included. Only `brand-context/` was left, which Parker's own sync had written during the build. Parker Desktop showed a brain with one folder and no "not built yet" banner (the banner needs the marker), so the team saw an empty brain for about a day and had no sign that a build could start again.

## What shipped

- **`prompts/onboarding-runner.md`, "When the user stops the build".** A stop is a pause unless the user clearly asks to undo the build, and Parker never offers the undo itself, so a person who only wanted the build to stop never loses finished work. A pause keeps everything, and the next session resumes it. A cancel goes back to the scaffolded state, never to an empty folder: the scaffold is setup, not build, so it stays even when the build's own Phase 0 laid it down. A build whose status file is marked complete is closed out, never undone. The steps: report the run `failed` while `parker_config.json` still has its `run_id`, delete only the docs the build wrote (every ledger output on disk, whatever its mark; if the stamp step ran, also the stamped `CLAUDE.md`, `README.md` and `running-notes/refresh-schedule.md`, and turn off the routines it armed), and keep the scaffold's other files, the intake answers, `brand-context/` and the team's files. Then run the script below.
- **`scripts/scaffold-brain.py init --undo-build`.** It removes `BUILD-STATUS.md`, `prompts-run-log/`, and the `run_id` in `parker_config.json`, then runs the normal init: the marker first, then every scaffold file that is missing, never overwriting one. So even a stop that deleted the whole scaffold gets it back. Without the `run_id`, the next build starts a new run; with it, the status tool would resume the old run and skip phases whose docs are gone. It refuses a brain with `prompts-run-log/BUILD-STATUS.md`, the record a finished build's closeout archives. `--dry-run` shows what it would remove.
- **`set-up-brain`** has the same rule in its hard rules, and **`system/brain-scaffold.md`** documents the option.
- **Tests.** `tests/test_scaffold_brain.py`: a stopped build with the marker already off gets the marker, a deleted method file and Parker Desktop's "not built yet" state (marker, no status file) back, and keeps the intake answers, `brand-context/` and the other config keys. A cancel that deleted the status file but left the build log is still undone. A folder wiped down to `brand-context/` and the mount gets the whole scaffold back. A finished build (its status file archived in `prompts-run-log/`) is refused.

## For the other Parker repos

None needed. Parker Desktop already shows its "not built yet" banner and offers a build for a brain with the marker and no `BUILD-STATUS.md`, which is the state a cancelled build now ends in.

## Migration

`migrations/v34.md`: nothing to do. The runner and the script are read from the mount, and the pin bump's re-sync delivers `set-up-brain`.
