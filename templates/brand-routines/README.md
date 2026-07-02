# Brand-routines template — the stampable living loop

This is the factory-canonical **routine bundle** that `prompts/onboarding-runner.md` stamps into every brand brain. It is what makes a shipped brain *self-running*: clone the brain into a Claude Code instance and the dreaming / self-improvement / idea / refresh routines are live immediately, ready to be armed on a schedule.

Author the routines **here**, once. Do not hand-edit them per brand — when a routine's method changes, change it here and re-stamp, so every brain stays in sync. (This is the "clean long-term flow" the brand-instance `.claude/README.md` points at.)

## What's in the bundle

- **`claude/`** → stamped to the brand brain's **`.claude/`**. (Named `claude/` without the dot on purpose, so Claude Code does not treat the factory's own template as active config. The runner renames it to `.claude/` on stamp.)
  - `settings.json` + `hooks/craft-context.py` — the `UserPromptSubmit` context hook (brand-agnostic; a Claude Code hook, no relation to ad hooks). The script injects the live craft catalog from `parker-system/creative-strategy-context/expertise-routing.md` into every turn, with the sources-receipt rule; settings.json wires it up with a static fallback.
  - `README.md` — explains the two layers of a routine (job travels in the repo; schedule armed per-account).
  - `skills/` — the bundled skills, self-contained (no `parker-brain/...` paths at runtime). The first four are the scheduled routines; the last two are on-demand helpers:
    - `dream` — daily planning run over the day's comms → five-bucket proposals, captured verbatim (proposes, never applies).
    - `self-improve` — weekly governing pass: curates traces, disposes dreaming and research proposals with the human in the loop.
    - `research-loops` — the weekly research cycle: rolls up the open loops, advances promoted ones into hypotheses, runs the validations and due re-validations, and aligns the standing docs with the confirmed findings.
    - `harvest-ideas` → `evaluate-ideas` — the weekly idea cycle (capture verbatim, then grade against the roadmap).
    - `refresh-context` — re-runs docs past their `refresh_by`.
    - `update-brain` — the weekly standard check: compares the brain against the current factory and its own canonical build, and offers every gap as a choice. Never overrides; the team's edits, deletions, and declines are remembered and respected.
    - `setup-routines` — one-time installer that arms the cron schedules in a fresh instance.
    - `get-started` — the first-run walkthrough: teaches a new user (or a teammate who just cloned the brain) what it knows, how to use it, and the single best first move, grounded in the brand's own data. On-demand and re-runnable; the runner invokes it live at hand-off.
- **`schedules/`** → stamped to the brand brain's **`schedules/`**. One recipe per routine (task, cron cadence, what it runs/reads/updates, deliverable, status, origin) plus the folder README. These are repo-native cron routines — **not** the Parker-MCP `workflows/` product surface (see `system/schedules.md`).

## How it's stamped

`onboarding-runner.md` copies `claude/` → `.claude/` and `schedules/` → `schedules/`, then de-genericizes: replace `[brand]` / "the brand" with the brand name where it reads naturally, and leave the brand-rule pointers (`CLAUDE.md`, `running-notes/brand-notes-from-org.md`) as-is, since those resolve inside the brain. The schedules ship as `status: not-yet-registered`; the brand owner runs `/setup-routines` once per cloud instance to arm the cron.

## The canonical method behind each routine

These skills are faithful distillations of the factory method docs — keep them in sync with:
- `self-improvement/the-living-loop.md` (the plan→execute spine + the five streams)
- `self-improvement/dreaming-system.md` (the planning arm, the day's-comms read, the verbatim rule)
- `system/schedules.md` (repo-native cron vs MCP workflows)
- `system/open-loops-system.md` (the loop lifecycle the `self-improve` roll-up runs)
- `system/refresh-cadence.md` (what `refresh-context` acts on)
- `prompts/ideas-and-briefs/` (what `harvest-ideas` / `evaluate-ideas` distill)
