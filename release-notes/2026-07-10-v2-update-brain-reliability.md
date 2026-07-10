# 2026-07-10 — v2: more reliable `/update-brain` updates and migrations

## What shipped

`/update-brain` (the brand-routine skill at `templates/brand-routines/claude/skills/update-brain/`) got two reliability fixes for connected brains:

- **Read migrations before framing the mode.** Before choosing connected vs decoupled comparison shape, the routine reads `parker-system/migrations/README.md` and any `vN.md` newer than the brain's last-applied migration, so a release that changed filesystem shape or mode behavior is in context before the offer is written.
- **Skipped releases still carry their migrations.** If a team declined an earlier pin bump and later accepts a newer one, every `migrations/vN.md` between the old pin and the new one still runs in order. Declining a release offer does not skip the structural work those releases carried.

`migrations/v2.md` ships with this release. It is a no-op for brand layout — nothing to move or create; the pin bump's normal executable-layer re-sync picks up the clearer skill.

## Why

Connected-mode updates were easy to under-specify: an agent could frame the offer without reading what migrations said about the current shape, and a multi-release jump after a declined bump could look like "only apply the newest migration." Both made pin bumps less reliable than the contract in `migrations/README.md` already required.

## Follow-ups

- Cut the `v2` tag once this merges — nothing reaches a standing brain until the tag exists.
- No brand-side migration pass beyond the usual `/update-brain` pin bump.
