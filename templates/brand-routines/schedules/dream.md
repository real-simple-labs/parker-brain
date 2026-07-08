# Schedule — dream

- **Task:** Read **the day's comms** for the brand and the person — first the conversations the user had with Parker, then any comms connected via MCP — and read them against the vault to return proposals across **six buckets** (context updates, skill improvements, schedules to create, new ideas to research, new open loops, and the person — what Parker now understands about them and what to tee up for them) into `dreaming/proposals/pending/`. **Captures verbatim; proposes, never applies.**
- **Cadence:** Daily (runs on the day's comms; the daily rhythm is what makes the morning suggestion possible).
- **Sources:** The day's conversations first, then connected team comms (iMessage/Slack/email via MCP, as added), read against `sub-context-docs/`, `personas/`, `competitors/`, `running-notes/`, `open-loops/`, `hypotheses/`, `validations/`, `audits/`, `source-pulls/`, `idea-bank/`, and fresh Parker MCP / web data.
- **Skill:** `.claude/skills/dream/` (`/dream`).
- **Deliverable:** A dated run folder in `dreaming/runs/`, proposal files in `dreaming/proposals/pending/` (schedule proposals also surface at `schedules/proposed/`, open-loop proposals feed `open-loops/`), and a morning-suggestion summary.
- **Origin:** Seeded 2026-06-18 from the factory's `self-improvement/dreaming-system.md` + `self-improvement/the-living-loop.md` (brand dreaming only; global product-signals stays in the factory).
- **Status:** Job committed and live. Schedule **not yet registered** — run `/setup-routines` to arm it.

## Schedule recipe (register once via `/schedule`)

> **Cadence:** daily, 05:00 (user's timezone) — earliest so proposals are ready for the morning.
> **Prompt:** "Run the /dream routine for the brand brain in this repo. Follow the skill exactly: read the day's comms, capture verbatim, write six-bucket proposals into dreaming/proposals/pending/, propose — never apply. Surface a morning-suggestion summary."

> **Promotion of proposals happens in `/self-improve`, with the human in the loop — dreaming never applies its own proposals.**
