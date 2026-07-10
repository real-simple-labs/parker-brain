# Schedule — update-brain

- **Task:** Compare this brain against the current `parker-brain` factory — on the standard layout, the pinned `parker-system/` release against the newest factory tag (the offer is the release bump plus its migrations, one short line; on an accepted bump `sync-executable-layer.py` re-syncs the copied skills deterministically, no per-file offers); on a decoupled brain, per-file compare — and against its own canonical build (standing docs never generated — an existence check that lands as one digest line, never questions), then write the offer to the ledger and the digest. **Offers only; a scheduled run applies nothing** — the script's `--dry-run` report (with `--to` the newest tag, no checkout) is how it sees what a bump would touch. Declined items stay declined until the factory version moves.
- **Cadence:** Weekly, early Monday, so the week opens with the offer list ready before the refresh sweep runs.
- **Sources:** The posture, pin, and factory remote recorded in `running-notes/standard-sync.md`, the factory's tags and `migrations/` (fetched through the mount), the brain's own `parker-system/prompts/` and their path map, the standing docs on disk, and the ledger's history of prior answers.
- **Skill:** `.claude/skills/update-brain/` (`/update-brain`).
- **Deliverable:** `running-notes/standard-sync.md` updated with the week's comparison and offers, and a plain digest — what's new in the standard, what's missing from this brain, what stayed declined. One line when nothing changed.
- **Origin:** Seeded 2026-07-02 from Jimmy's direction: standing brains drift below the improving standard and below their own canonical build (older brains missing persona source pulls), and the fix must offer, never override — the team's deletions and edits are theirs.
- **Status:** Job committed and live. Schedule **not yet registered** — run `/setup-routines` to arm it.

## Schedule recipe (register once via `/schedule`)

> **Cadence:** weekly, Monday 05:30 (user's timezone).
> **Prompt:** "Run the /update-brain routine for the brand brain in this repo. Follow the skill exactly: compare against the factory and against the brain's own canonical build, write the offer list to the ledger and the digest, and apply nothing — offers wait for the user."

> **Nothing is copied, regenerated, or edited without the user's yes. Declined offers stay quiet until the factory moves again.**
