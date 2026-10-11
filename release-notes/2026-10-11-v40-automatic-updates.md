# v40 — safe releases install on their own (2026-10-11)

Until now, `/update-brain` asked before every release. Most releases are no-ops that only refresh the method, and the sync already keeps every file the team changed, so the question mostly kept brains behind. The team decided on 2026-10-09 that updates should happen automatically. From v40 on, they do, wherever that's safe.

## What shipped

- **Safe releases install themselves.** On the standard layout, `/update-brain` moves the pin to the newest release it may take with nobody asked, runs and records the migrations in order, re-syncs the copied skills, and records the pin. It does this in an interactive session and in the Monday scheduled run, then says in one line what changed. Nothing is put to the team first.
- **What counts as safe.** Every migration on the way must be safe to run unattended: the one-line no-op ("Nothing to do; ..."), or a migration with real steps that says `**Auto-apply:** yes` near the top. A migration with real steps and no marker needs a person. Automatic updates stop at the release before it, and the rest comes as the one short question it always was. `migrations/README.md` has the rule for maintainers: mark a migration safe only when every step is idempotent, touches no brand-authored content, and asks nothing.
- **What never installs on its own:** anything on a decoupled brain (`own-factory` or `independent`), anything while a build is underway, anything after a migration an earlier update didn't finish, and anything when the team turned automatic updates off. The ledger has a new **Auto-update:** line (`on` by default), and "turn off automatic updates" flips it.
- **The team's work stays theirs.** Unchanged from before: `sync-executable-layer.py` refreshes only copies the team never touched, keeps their edits, and never deletes. Migrations that change the brain's own content still show the team first, which is exactly why they need a person.
- **A deterministic helper, `scripts/update-brain.py`.** Brains run it through the mount. `plan` decides what may install on its own and says why not when it can't. `record-migration` refuses to skip a migration, and `record-pin` refuses a release the mount isn't on, so the ledger can't drift from what really happened.
- **Failure handling.** A dry run of the sync goes before anything moves; if it fails, nothing changes. A migration that stops partway isn't recorded, and nothing newer installs until it's finished. A sync that fails twice leaves the pin unrecorded, and the next run sees the moved pin and finishes the job.
- **Tests:** `tests/test_update_brain.py` covers a full automatic update (team edits kept), a stop before a migration that needs a person, an interrupted migration that blocks the next update until it's finished, a pin moved but never recorded, and the decoupled, opted-out and mid-build cases. It also checks that every shipped migration classifies the way its text reads.

## Migration

`migrations/v40.md`, real steps, and marked `**Auto-apply:** no`: this release is the team's yes to automatic updates, so every brain takes it on a yes. It adds the **Auto-update:** line to the ledger, updates one sentence about updates in the brain's `CLAUDE.md` (shown first), and offers to re-arm the update routine, since a routine armed before v40 tells each run to apply nothing.
