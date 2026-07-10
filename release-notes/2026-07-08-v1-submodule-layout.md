# 2026-07-08 — The v1 submodule layout: mount the method, stop copying it

## What shipped

The brand brain's relationship to the factory changed shape. A brain no longer carries a copied `parker-system/` snapshot of the method; it **mounts the factory as a git submodule at `parker-system/`, pinned to a release tag** (`v1`, `v2`, … — plain, manual, no semver). The brand repo holds its data flat at the root, the executable `.claude/` layer copied out of the mount, and one pointer to the exact method version it runs.

The pieces, end to end:

- **`creative-strategy-context/` moved to the factory root** (from `global/knowledge/creative-strategy/`), so the factory's own tree matches the brain's view of it minus the `parker-system/` prefix. That one rename is why ~330 existing `parker-system/…` references in prompts, skills, and system docs now resolve in both worlds with **zero ship-time copying, renaming, or path rewriting** — the onboarding-runner's whole "ship the craft" copy step collapsed into `git submodule add` + checkout of the latest tag.
- **Brand property left the method tree.** The brand lens is now `brand-lens.md` at the brain root (one fixed name, no per-brand templating); the brand's expert-insights intake is `expert-insights/` at the root. Both were previously nested inside the copied craft layer — brand-owned files inside a mirrored tree was the standing footgun.
- **The mount is read-only, structurally.** The routine bundle's `settings.json` now carries permission deny rules for `Edit`/`Write` under `parker-system/**`, and a new `SessionStart` hook (`hooks/session-start.py`) catches a clone made without `--recurse-submodules` (empty mount), says exactly how to fix it, and reminds every session to pull before working. Instruction-only: the hook runs no git itself.
- **Releases and migrations are the delivery mechanism.** New `migrations/` directory: one plain-markdown `vN.md` per release whose changes reshape standing brains, applied in order by `/update-brain` on a pin bump. `migrations/v1.md` is the first — it converts a legacy copy-based brain to the submodule layout. CLAUDE.md gained the maintainer rule (structural change ⇒ migration in the same PR) and `update-parker-skill` gained the matching proposal checklist item.
- **`/update-brain` grew two modes.** Connected (the standard): compare the pinned release to the newest tag, offer the bump, apply migrations, re-sync the copied executable layer with the team's edits still winning. Decoupled: the old per-file compare-and-offer, for teams on their own method.
- **`/disconnect-factory` is new.** The deliberate decoupling for teams that want to develop their own version of the method: repoint the submodule at their own private factory copy (keeps upstream merges possible), or fully absorb the files into the brain. Confirmation-gated, one revertable commit, flips the posture in `running-notes/standard-sync.md` (new template).
- **`propagate-craft` reframed as the legacy path** — push sweeps for copy-based and decoupled brains only; it must never write into a submodule-mounted brain.
- **Onboarding re-imports the `setup_parker_brain` provisioning flow** (from the reverted #24, adapted): connect Parker MCP and lock the brand first, then the tool provisions the private repo and short-lived credentials — no hand-created repos, no `gh auth`, and no wrapper working folder: the brand repo is the workspace.
- **Routine hygiene:** schedule names are brand-prefixed (two brains on one account stay distinguishable), and `/setup-routines` now says plainly what the standing routines cost in usage, with downshifting offered as a first-class answer.

## Why

Three folder-structure models had accumulated in the docs (copied `parker-system/`, a two-sibling-folder working layout, and fragments of both). The submodule model replaces all of them with one shape that is versioned (every brain's history shows exactly which method release it ran), self-contained (a cloud routine cloning only the brand repo materializes the method with one git command), and honest about ownership (method is Parker's until the team deliberately decouples; brand property never lives inside the mirrored tree). Updates stay offer-based — the pin only moves when the team says yes — which is the same "offer, never override" doctrine the routines already carried, now enforced by git itself.

## Follow-ups

- Cut the `v1` tag once this merges — nothing reaches a standing brain until the tag exists.
- Run `migrations/v1.md` against the existing test brains (via `/update-brain` or a supervised pass).
- The lab-vault snapshots in `system-of-records.md` still use the copy model by design; revisit if the lab moves to submodules too.
