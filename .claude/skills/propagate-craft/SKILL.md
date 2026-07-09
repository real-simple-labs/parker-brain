---
name: propagate-craft
description: Push-based re-ship of the factory methodology bundle into brand brains that carry the method as copied files — the legacy vendored-parker-system layout and decoupled brains that asked for a refresh. Brains on the standard layout (parker-system as a pinned submodule) do NOT use this; they update by moving the pin via their own /update-brain routine, and migrations/v1.md converts a legacy brain to that layout. Use for a factory-initiated sweep of the remaining copy-based brains.
triggers:
  - propagate the craft layer
  - update the brand brains
  - re-ship the methodology to the brand brains
  - the brand brains are stale
  - push factory updates to the living brains
  - sync brand brains with the factory
---

# Propagate Craft — factory → standing brand brains

## Where this now fits — legacy and decoupled brains only

The standard brand brain no longer copies the method: it mounts the factory at `parker-system/` as a submodule pinned to a release, and its weekly `/update-brain` routine offers pin bumps plus the release's `migrations/`. **That is the primary update path, and this skill must never write into a submodule-mounted brain** — the mount is read-only there, and a push-sweep would fight the pin.

What remains for this skill is the copy-based world: brains built before the submodule layout (vendored `parker-system/`, or the older flat shape), and decoupled brains that own their method copy but ask for a factory refresh. For those, this push-based re-ship is still the tool — and the better long-term fix for a legacy brain is running `migrations/v1.md` to convert it to the submodule layout, which this sweep should offer first.

## What is factory methodology vs brand-specific

A brand brain has a clean separation, and propagation depends on it:

- **`parker-system/`** is a copy of the factory methodology — `prompts/`, `skills/`, `system/`, `templates/`, and `creative-strategy-context/` (the craft layer, mapped from the factory's `creative-strategy-context/`). This is safe to mirror from the factory; brand brains are not meant to edit it.
- **Everything outside `parker-system/`** is brand data and output: `brand-profile.md`, `personas/`, `strategy/`, `audits/`, `competitors/`, `open-loops/`, `running-notes/`, `sub-context-docs/`, `prompts-run-log/`, `CLAUDE.md` (brand rules), `README.md`, `.claude/`, `schedules/`. Never touched.
- **Brand-specific files that live *inside* the copied `parker-system/creative-strategy-context/`** must be preserved: the brand lens overlay `_<brand>-lens.md`, and the brand's `expert-insights/` intake. These are excluded from the mirror. (On the current layout they live at the brain root — `brand-lens.md` and `expert-insights/` — outside any mirrored path; the excludes here protect the legacy brains that still nest them.)

## How it runs

The executable form is `scripts/propagate-to-brand-brains.sh`. It clones each brand brain, **auto-detects its layout** (nested `parker-system/` or flat standalone), and runs an **update-only** sync (`rsync --existing`, no `--delete`) of the methodology layers into the right place: every file the brain already has is refreshed to the factory version, nothing is added, nothing is deleted. It excludes the brand-specific paths, commits with the factory SHA, and pushes. Update-only is deliberate — it prevents product-internal docs (e.g. `system/product-brain-CLAUDE.md`, `repo-boundary-and-promotion-model.md`, this `propagate-craft` skill itself) from leaking into brand brains, and prevents deletion of brand-specific or intentionally-kept files. A genuinely-new methodology doc that a brain *should* gain (like `hook-psychology.md` or `emotional-delivery-and-timing.md` were) is added through the script's named **deliberate-adds list** (currently `system/growing-the-brain.md`, the `research-loops` and `update-brain` routine skills and their schedule recipes, and the creative review-gate bundle — `creative-strategy-context/ai-writing-tells.md`, the `.claude/agents/creative-voice-review.md` and `context-grounding-review.md` agents, and the `scripts/voice-lint.py` and `grounding-check.py` checkers, which ship together because the creative skills' ship gates reference all of them by name) — extend that list when the runtime ship list grows, rather than relying on the sweep. Two exceptions to update-only ship as plain copies, added if missing: the **hook bundle** — the `.claude/hooks/` directory (`craft-context.py`, which injects the craft catalog every turn, and `pull-log.py`, which logs MCP calls to the session pull record the grounding gate verifies against) and `.claude/settings.json`, from `templates/brand-routines/claude/` — because settings.json calls the scripts, so they only work together, and none of it carries brand-specific content.

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

## The release-pinned model is now the standard

What the old "better future" note here described now exists: standard brains pin a factory release through the `parker-system/` submodule, `/update-brain` offers the bump weekly, and `migrations/` carry the structural steps. This skill is the shrinking legacy path, not the roadmap. Before sweeping a brain, check its layout honestly — `git submodule status` in the brain, or a `.gitmodules` naming `parker-system` — and **skip any submodule-mounted brain** with a note that its updates come from its own pin.
