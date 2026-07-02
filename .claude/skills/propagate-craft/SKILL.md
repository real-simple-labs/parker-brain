---
name: propagate-craft
description: Re-ship the factory methodology bundle (prompts, skills, system, templates, and the creative-strategy craft layer) into standing brand brains, so factory improvements reach brains that were stood up earlier. Use when the factory has changed and the live brand brains are stale. This is the update-time counterpart to the onboarding-runner's build-time "ship the craft" step.
triggers:
  - propagate the craft layer
  - update the brand brains
  - re-ship the methodology to the brand brains
  - the brand brains are stale
  - push factory updates to the living brains
  - sync brand brains with the factory
---

# Propagate Craft — factory → standing brand brains

## The gap this closes

The onboarding-runner ships the craft layer into a brand brain **once, at standup** (Phase 0, "Ship the craft"). There is no build-time-only mechanism to re-ship when the factory changes — so every brand brain drifts stale the moment the factory is improved, and there is no automatic sync. This skill is the missing update-time re-ship.

## What is factory methodology vs brand-specific

A brand brain has a clean separation, and propagation depends on it:

- **`parker-system/`** is a copy of the factory methodology — `prompts/`, `skills/`, `system/`, `templates/`, and `creative-strategy-context/` (the craft layer, mapped from the factory's `global/knowledge/creative-strategy/`). This is safe to mirror from the factory; brand brains are not meant to edit it.
- **Everything outside `parker-system/`** is brand data and output: `brand-profile.md`, `personas/`, `strategy/`, `audits/`, `competitors/`, `open-loops/`, `running-notes/`, `sub-context-docs/`, `prompts-run-log/`, `CLAUDE.md` (brand rules), `README.md`, `.claude/`, `schedules/`. Never touched.
- **Brand-specific files that live *inside* `parker-system/creative-strategy-context/`** must be preserved: the brand lens overlay `_<brand>-lens.md`, and the brand's `expert-insights/` intake. These are excluded from the mirror.

## How it runs

The executable form is `scripts/propagate-to-brand-brains.sh`. It clones each brand brain, **auto-detects its layout** (nested `parker-system/` or flat standalone), and runs an **update-only** sync (`rsync --existing`, no `--delete`) of the methodology layers into the right place: every file the brain already has is refreshed to the factory version, nothing is added, nothing is deleted. It excludes the brand-specific paths, commits with the factory SHA, and pushes. Update-only is deliberate — it prevents product-internal docs (e.g. `system/product-brain-CLAUDE.md`, `repo-boundary-and-promotion-model.md`, this `propagate-craft` skill itself) from leaking into brand brains, and prevents deletion of brand-specific or intentionally-kept files. A genuinely-new methodology doc that a brain *should* gain (like `hook-psychology.md` or `emotional-delivery-and-timing.md` were) is added through the script's named **deliberate-adds list** (currently `system/growing-the-brain.md`, the `research-loops` routine skill, and its schedule recipe) — extend that list when the runtime ship list grows, rather than relying on the sweep. Two exceptions to update-only ship as plain copies, added if missing: the **context hook pair** — `.claude/hooks/craft-context.py` and `.claude/settings.json`, from `templates/brand-routines/claude/` — because settings.json calls the script, so they only work together, and neither carries brand-specific content.

```
scripts/propagate-to-brand-brains.sh [brand-repo ...]
```

Pass repo names as arguments, or set `PARKER_BRAND_BRAIN_REPOS` to a space-separated list for local defaults. Requires `gh` authenticated, `rsync`, `git`.

## Hard rules

- **This pushes to production brand repos.** It is outward-facing and must be run deliberately, with the user's go — never on auto-approval. Brand brains are git repos, so a mistake is recoverable from history, but treat it as a real deploy.
- **Mirror only the methodology layers.** On nested brains that means `parker-system/`; on flat brains it means the craft layer (`creative-strategy-context/`), the runtime system subset (`system/`), and the routine skills (`.claude/skills/`). Never write outside those. All brand data and output is off-limits.
- **Preserve brand-specific files inside the craft layer:** `_*-lens.md` and `expert-insights/` are excluded from both copy and delete.
- **Verify before trusting.** After a run, confirm the new craft docs are present in each brain (e.g. `hook-psychology.md`, `emotional-delivery-and-timing.md`) and the lens overlay still exists.
- **Layout is auto-detected.** The script handles both the nested `parker-system/` layout and the flat standalone layout (craft + system at repo root, runtime skills under `.claude/`). It only `SKIP`s a brain that has neither `parker-system/` nor `creative-strategy-context/`. For flat brains it ships the runtime system subset (update-only, so factory-internal docs are never added) and rewrites the shipped system docs' craft-path references to `creative-strategy-context/`.
- **Scope note:** the factory `global/knowledge/performance/` tree is not part of the brand-brain bundle today; only the creative-strategy craft layer maps in. Revisit if performance becomes a brand-brain surface.

## Better future: a pull-based or release-pinned model

This script is push-based and run from the factory. A more robust model would have each brand brain pin a factory release/SHA and pull the methodology bundle on a schedule (or on `/refresh-context`), so propagation is auditable per brain and a brain can stay on a known-good methodology version. Treat this script as the v1 that closes the immediate gap.
