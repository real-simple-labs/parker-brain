# `.claude/` — the brand brain's routines and config

This directory makes the brand brain **self-running**. Clone this repo into a Claude Code cloud instance and everything here is live immediately — the context hook (which loads the craft catalog every turn), and the standing **routines** (the recurring jobs that keep the brain fresh without being asked each time).

## The two layers of a routine

A "routine" is really two things, and only one of them lives in this repo:

| Layer | What it is | Where it lives |
|---|---|---|
| **The job** (the *what*) | The prompt, sources, method, and deliverable for refreshing context, dreaming, harvesting ideas, self-improving. | **Here**, as skills in `.claude/skills/`. Travels with the repo — clone → ready. |
| **The schedule** (the *when*) | The cron trigger that fires the job on Anthropic's cloud infra. | **Per-account**, registered once via `/schedule`. Cannot be committed. |

So the work is fully pre-built and version-controlled; the clock gets armed **per cloud instance**. A brain built by onboarding arrives with the clock already running — the build arms the schedules at its stamp step and says so plainly at the finish. A brain cloned onto a new instance arrives un-armed (schedules are per-account), and `/setup-routines` registers them there; it's also how you change a cadence or turn a routine off. `../schedules/*.md` records the exact cadence + the prompt to schedule for each. (These are **schedules** — repo-native cron routines — not the Parker-MCP `workflows/` product surface; see `../schedules/README.md`.)

## What's here

- **`settings.json`** — committed project config. The `permissions.deny` rules keep the `parker-system/` method mount (a pinned submodule of the public factory) read-only, so updates only ever arrive through `/update-brain` moving the pin. The `SessionStart` hook runs `hooks/session-start.py`, which catches a clone whose mount was never initialized (empty `parker-system/`), says exactly how to fix it (`git submodule update --init parker-system`), and reminds the session to `git pull --recurse-submodules` before real work. The `UserPromptSubmit` hook runs `hooks/craft-context.py`, which injects the actual craft catalog (the DOC-MAP table from `parker-system/creative-strategy-context/expertise-routing.md`) into every turn, plus the standing rules: load the method docs the question touches, close substantive answers with a Sources list, and treat a creative answer whose sources name no method doc as under-retrieved. A menu in front of the planner beats a reminder to go find one. Travels with the repo; falls back to a plain pointer if the catalog file is missing.
- **`hooks/craft-context.py`** — the small script behind the prompt hook. Reads the generated DOC-MAP section live, so the injected catalog stays current as method docs are added.
- **`hooks/session-start.py`** — the small script behind the session-start check. Instruction-only: it runs no git commands itself, it tells the session what to run.
- **`skills/`** — `.claude/skills/` is where Claude Code loads skills from, so **all** of the brain's skills live here. Alongside the routines listed below sit the **craft skills** (scriptwriting, hooks, headlines, iterations, ad-account-analysis, ai-ad-generation, the open-loops pipeline, and the rest), copied in during onboarding so the brand `CLAUDE.md` can route execution through `.claude/skills/<skill>/` and they register the moment the brain is cloned. The routines, each a self-contained skill (invoke as `/refresh-context`, `/dream`, etc.):
  - `refresh-context` — re-runs stale context docs on cadence.
  - `update-brain` — weekly standard check: in the standard (connected) layout it compares the pinned factory release against the newest and offers the bump plus its migrations; on a decoupled brain it falls back to per-file compare-and-offer. Never overrides, remembers declines.
  - `disconnect-factory` — the deliberate decoupling: converts the read-only `parker-system/` mount into files the team owns (or repoints it at their own factory copy), removes the guardrails, and flips the update posture. Confirmation-gated; never runs as a side effect.
  - `dream` — daily dreaming run over the day's comms → five-bucket proposals, captured verbatim (proposes, never applies).
  - `harvest-ideas` — weekly agentic idea capture into the idea bank.
  - `evaluate-ideas` — ranks the idea bank against the strategic roadmap.
  - `research-loops` — the weekly research cycle: rolls up the loops, advances them into hypotheses, runs the validations and due re-validations, aligns the docs with what was found.
  - `self-improve` — weekly curation; governs dreaming and research proposals with the human in the loop.
  - `setup-routines` — registers the cron schedules; run automatically by the build, by hand on a fresh clone, or any time to change a cadence.
  - `get-started` — the first-run walkthrough: teaches a new user what the brain knows, how to use it (you just talk to it), and the one best first move, grounded in the brand's own data. On-demand, re-runnable, and offered proactively on a fresh brain. Not a scheduled routine.
- **`settings.local.json`** (gitignored, you create it) — instance-specific overrides: MCP server connections, model, theme. **Do not commit secrets or MCP connections** — those are per-instance.

## Portability rule (important)

These skills are **self-contained**. The brand brain is the *output* of the `parker-brain` factory, but the factory does **not** travel when this repo is cloned. So every skill embeds its own method and points only at in-repo surfaces — `CLAUDE.md`, the folder READMEs (`open-loops/`, `idea-bank/`, `dreaming/`, `schedules/`…), the `parker-system/` mount, and the brand's own docs. The mount itself travels as a pinned submodule, so a clone materializes it with `git submodule update --init` (the session-start hook catches a clone that skipped it).

## System-of-records note (for the factory maintainer)

The canonical authoring home for these methods is the factory (`parker-brain`: `self-improvement/`, `system/open-loops-system.md`, `prompts/ideas-and-briefs/`, `system/refresh-cadence.md`). These skills are faithful, self-contained distillations of those specs as of 2026-06-18. To avoid drift, the clean long-term flow is to author the routine once in the factory and have `onboarding-runner` stamp it into each brand brain — rather than hand-editing per brand. Until that's wired, treat the factory specs as source of truth and re-sync these skills when the specs change.
