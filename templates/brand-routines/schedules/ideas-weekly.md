# Schedule — ideas-weekly (harvest → evaluate)

- **Task:** The weekly idea cycle. First harvest: hunt inspo wide and capture verbatim, ungraded, into `idea-bank/entries/`. Then evaluate: rank the whole pile against the Phase-2 roadmap into `idea-bank/evaluation-[date].md`. Capture and grading are deliberately separate passes.
- **Cadence:** Weekly, every brand. A full centered harvest paired each week with the evaluator re-rank (taking the prior week's evaluation as context).
- **Sources:** Customer language (reviews/surveys/community) first, then old ads, organic TikTok, affinity ads, competitor ads, audits, source pulls, Parker MCP creative reads, web. Evaluation also reads `strategy/strategic-roadmap.md`, `personas/personas-profile.md`, the voice library, and `audits/`.
- **Skills:** `.claude/skills/harvest-ideas/` (`/harvest-ideas`) then `.claude/skills/evaluate-ideas/` (`/evaluate-ideas`).
- **Deliverable:** New verbatim entries + updated `idea-bank/index.md`, then a ranked `evaluation-[date].md` that opens with the ranked call the sprint plan sizes into a round and ends with what the bank is starving for.
- **Origin:** Seeded 2026-06-18 from the factory's `prompts/ideas-and-briefs/brand-idea-bank.md` + `idea-evaluation.md`. Matches the cadence already stated in `idea-bank/README.md`.
- **Status:** Jobs committed and live. Schedule **not yet registered** — run `/setup-routines` to arm it. Note: evaluation ranks **provisionally** until the strategic roadmap is approved (see `strategy/strategic-roadmap.md`).

## Schedule recipe (register once via `/schedule`)

> **Cadence:** weekly, Monday 07:00 (user's timezone) — one agent runs both passes in sequence.
> **Prompt:** "Run the weekly idea cycle for the brand brain in this repo: first /harvest-ideas (capture verbatim, ungraded, with provenance and a viewable link — capture only), then /evaluate-ideas (rank the whole pile against the roadmap, confidence-first, lead with the call). Mark the rank provisional if the roadmap is still awaiting approval."
