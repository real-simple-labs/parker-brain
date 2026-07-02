# `.claude/` — the brand brain's routines and config

This directory makes the brand brain **self-running**. Clone this repo into a Claude Code cloud instance and everything here is live immediately — the context hook (which loads the craft catalog every turn), and the standing **routines** (the recurring jobs that keep the brain fresh without being asked each time).

## The two layers of a routine

A "routine" is really two things, and only one of them lives in this repo:

| Layer | What it is | Where it lives |
|---|---|---|
| **The job** (the *what*) | The prompt, sources, method, and deliverable for refreshing context, dreaming, harvesting ideas, self-improving. | **Here**, as skills in `.claude/skills/`. Travels with the repo — clone → ready. |
| **The schedule** (the *when*) | The cron trigger that fires the job on Anthropic's cloud infra. | **Per-account**, registered once via `/schedule`. Cannot be committed. |

So the work is fully pre-built and version-controlled; the clock gets armed **once per cloud instance**. The `/setup-routines` skill walks you through that one-time registration, and `../schedules/*.md` records the exact cadence + the prompt to schedule for each. (These are **schedules** — repo-native cron routines — not the Parker-MCP `workflows/` product surface; see `../schedules/README.md`.)

## What's here

- **`settings.json`** — committed project config. The `UserPromptSubmit` hook runs `hooks/craft-context.py`, which injects the actual craft catalog (the DOC-MAP table from `parker-system/creative-strategy-context/expertise-routing.md`) into every turn, plus the standing rules: load the method docs the question touches, close substantive answers with a Sources list, and treat a creative answer whose sources name no method doc as under-retrieved. A menu in front of the planner beats a reminder to go find one. Travels with the repo; falls back to a plain pointer if the catalog file is missing.
- **`hooks/craft-context.py`** — the small script behind that hook. Reads the generated DOC-MAP section live, so the injected catalog stays current as method docs are added.
- **`skills/`** — `.claude/skills/` is where Claude Code loads skills from, so **all** of the brain's skills live here. Alongside the routines listed below sit the **craft skills** (scriptwriting, hooks, headlines, iterations, ad-account-analysis, ai-ad-generation, the open-loops pipeline, and the rest), copied in during onboarding so the brand `CLAUDE.md` can route execution through `.claude/skills/<skill>/` and they register the moment the brain is cloned. The routines, each a self-contained skill (invoke as `/refresh-context`, `/dream`, etc.):
  - `refresh-context` — re-runs stale context docs on cadence.
  - `dream` — daily dreaming run over the day's comms → five-bucket proposals, captured verbatim (proposes, never applies).
  - `harvest-ideas` — weekly agentic idea capture into the idea bank.
  - `evaluate-ideas` — ranks the idea bank against the strategic roadmap.
  - `research-loops` — the weekly research cycle: rolls up the loops, advances them into hypotheses, runs the validations and due re-validations, aligns the docs with what was found.
  - `self-improve` — weekly curation; governs dreaming and research proposals with the human in the loop.
  - `setup-routines` — one-time helper to register the cron schedules in a fresh instance.
  - `get-started` — the first-run walkthrough: teaches a new user what the brain knows, how to use it (you just talk to it), and the one best first move, grounded in the brand's own data. On-demand, re-runnable, and offered proactively on a fresh brain. Not a scheduled routine.
- **`settings.local.json`** (gitignored, you create it) — instance-specific overrides: MCP server connections, model, theme. **Do not commit secrets or MCP connections** — those are per-instance.

## Portability rule (important)

These skills are **self-contained**. The brand brain is the *output* of the `parker-brain` factory, but the factory does **not** travel when this repo is cloned. So every skill embeds its own method and points only at in-repo surfaces — `CLAUDE.md`, the folder READMEs (`open-loops/`, `idea-bank/`, `dreaming/`, `schedules/`…), `parker-system/creative-strategy-context/`, and the brand's own docs. No skill reads a `parker-brain/...` path at runtime, because in a cloned instance that path won't exist.

## System-of-records note (for the factory maintainer)

The canonical authoring home for these methods is the factory (`parker-brain`: `self-improvement/`, `system/open-loops-system.md`, `prompts/ideas-and-briefs/`, `system/refresh-cadence.md`). These skills are faithful, self-contained distillations of those specs as of 2026-06-18. To avoid drift, the clean long-term flow is to author the routine once in the factory and have `onboarding-runner` stamp it into each brand brain — rather than hand-editing per brand. Until that's wired, treat the factory specs as source of truth and re-sync these skills when the specs change.
