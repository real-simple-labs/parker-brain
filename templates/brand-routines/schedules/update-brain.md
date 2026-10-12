# Schedule — update-brain

- **Task:** Compare this brain against the current `parker-brain` factory — on the standard layout, the pinned `parker-system/` release against the newest factory tag; on a decoupled brain, per-file compare — and against its own canonical build (standing docs never generated — an existence check that lands as one digest line, never questions). On the standard layout, **install the newest release that `update-brain.py plan` says is safe to take unattended** (`auto_target`: every migration on the way is a no-op or marked `**Auto-apply:** yes`, automatic updates are on, nothing earlier is unfinished): move the pin, run and record the migrations in order, let `sync-executable-layer.py` refresh the untouched copies, record the pin, and save the cloud-run way. Anything past that (a migration that needs a person, a decoupled brain, automatic updates turned off) is written to the ledger and the digest as an offer; the script's `--dry-run` report (with `--to` the newest tag, no checkout) is how it sees what the rest would touch. Team edits always stay theirs; declined items stay declined until the factory version moves.
- **Cadence:** Weekly, early Monday, so the week opens with the offer list ready before the refresh sweep runs.
- **Sources:** The posture, pin, and factory remote recorded in `running-notes/standard-sync.md`, the factory's tags and `migrations/` (fetched through the mount), the brain's own `parker-system/prompts/` and their path map, the standing docs on disk, and the ledger's history of prior answers.
- **Skill:** `.claude/skills/update-brain/` (`/update-brain`).
- **Deliverable:** `running-notes/standard-sync.md` updated with the week's comparison, what installed, and what's still offered, and a plain digest — what installed on its own, what's still waiting on the team and why, what's missing from this brain, what stayed declined. One line when nothing changed.
- **Origin:** Seeded 2026-07-02 from Jimmy's direction: standing brains drift below the improving standard and below their own canonical build (older brains missing persona source pulls), and the fix must never override — the team's deletions and edits are theirs. Changed in v40 (team decision, 2026-10-09): safe releases install on their own, because asking about every one kept brains behind; only what needs a person is still offered.
- **Status:** Job committed and live. Schedule **not yet registered** — run `/setup-routines` to arm it.

## Schedule recipe (register once via `/schedule`)

> **Cadence:** weekly, Monday 05:30 (user's timezone).
> **Prompt:** "Run the /update-brain routine for this brand brain. Follow the skill exactly: compare against the factory and against the brain's own canonical build, install the release the skill's plan says is safe to take unattended, then write what installed and what's still offered to the ledger and the digest. Apply nothing past that — offers wait for the user."

> **Only the safe part of a release installs on its own. The team's edits stay theirs, a migration that needs a person waits for one, and declined offers stay quiet until the factory moves again.**
