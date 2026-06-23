# Schedule — refresh-context

- **Task:** Re-run stale standing context docs so the brain never trusts a doc past its shelf life. Check `running-notes/refresh-schedule.md` + each doc's `refresh_by`, surface what's overdue, re-run the generating prompt for each.
- **Cadence:** Weekly (the check is cheap; it only re-runs docs actually due — 90/180/365-day cadences by doc type).
- **Sources:** `running-notes/refresh-schedule.md`, each standing doc's frontmatter, the live sources each doc rests on (Parker MCP reads, brand surfaces, web), `creative-strategy-context/` per the `CLAUDE.md` routing table.
- **Skill:** `.claude/skills/refresh-context/` (`/refresh-context`).
- **Deliverable:** Due docs re-run and re-stamped, `refresh-schedule.md` updated, a short report of what was refreshed / left / surfaced.
- **Origin:** Seeded 2026-06-18 from the factory's `system/refresh-cadence.md`.
- **Status:** Job committed and live. Schedule **not yet registered** in this instance — run `/setup-routines` to arm it.

## Schedule recipe (register once via `/schedule`)

> **Cadence:** weekly, Monday 06:00 (user's timezone).
> **Prompt:** "Run the /refresh-context routine for the brand brain in this repo. Follow the skill exactly: surface what's overdue, re-run each due doc's generating prompt carrying prior context forward, re-stamp dates, update the refresh schedule. Report what was refreshed."
