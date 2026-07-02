# Schedule — research-loops

- **Task:** Run the open-loops research cycle end to end: roll up and grade the loops, advance promoted ones into hypotheses (honoring the approval gate), run every cleared hypothesis in the testing queue to an honest verdict, run due re-validations, deliver the research digest, and align the standing docs with the confirmed findings — applied only where the user agreed, filed as pending proposals otherwise.
- **Cadence:** Weekly, mid-week — after Monday's refresh and idea cycle feed it current docs, before Friday's self-improve curates the finished findings.
- **Sources:** `open-loops/` and every context doc's open-loops tail, dreaming's captured loop proposals, `hypotheses/` (the testing queue and awaiting-user), `re-validations/scheduled/`, plus the live Parker MCP pulls each test plan names.
- **Skill:** `.claude/skills/research-loops/` (`/research-loops`), which sequences the roll-up prompt (`parker-system/prompts/open-loops/open-loops-roll-up.md`) and the `open-loops-advance` / `open-loops-validate` skills.
- **Deliverable:** The consolidated roll-up updated, hypotheses filed (awaiting-user surfaced), validations resolved into their four states with closure docs, re-validation results filed, the research digest, and doc-alignment updates applied or proposed with validation provenance.
- **Origin:** Seeded 2026-07-02 from `system/open-loops-system.md` and the loop pipeline skills, at Jimmy's direction that the loop → hypothesis → validation system run standing, like dreaming and the idea cycle.
- **Status:** Job committed and live. Schedule **not yet registered** — run `/setup-routines` to arm it.

## Schedule recipe (register once via `/schedule`)

> **Cadence:** weekly, Wednesday 06:00 (user's timezone).
> **Prompt:** "Run the /research-loops routine for the brand brain in this repo. Follow the skill exactly: roll up and grade the loops, advance promoted ones through the approval gate, validate every cleared hypothesis honestly, run due re-validations, deliver the digest, and align the standing docs — apply nothing the gates say needs the user; file those as pending proposals."

> **Doc alignment in a scheduled run proposes, never applies — `/self-improve` disposes with the human in the loop. Strategy and brand hard rules always wait for the user.**
