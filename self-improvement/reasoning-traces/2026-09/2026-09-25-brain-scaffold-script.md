---
trace_id: 2026-09-25-brain-scaffold-script
date_captured: 2026-09-25
source: chat
source_ref: Anton asked for a one-click, no-AI script for the build's setup phase, reusable by a backend process that creates an empty brain when a brand signs up
trigger_type: product-direction
scope: system
brand: global
team: product
confidence: strong
status: applied
target_surfaces:
  - scripts/scaffold-brain.py
  - scripts/sync-executable-layer.py
  - prompts/onboarding-runner.md
  - .claude/skills/set-up-brain/SKILL.md
  - templates/brand-routines/claude/hooks/session-start.py
  - templates/brand-routines/claude/hooks/pull-log.py
  - templates/brand-routines/claude/skills/get-started/SKILL.md
  - system/brain-scaffold.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Anton pointed out that the build's setup phase spends model time on work with no judgment in it: creating folders and copying method and skill files. They wanted a plain script for it, and wanted the same thing reusable by Parker's backend so a brand gets an empty brain the moment it signs up. Their bet is that a scaffolded but unbuilt brain is already useful: the agent can start filling it in from conversation before the full build ever runs.

**Decision context:** The copy list already existed as code (the bundle map `/update-brain` uses), so the script reuses it rather than keeping a third copy. For the backend, running git in a serverless function is the hard part, so the scaffold ships as a release asset in GitHub tree-entry form and the backend needs three write calls, plus preflight reads. Anton chose a marker file (`.scaffolded`) over a flag inside `parker_config.json` as the "not built" signal, because the web app already lists the repo root, so a file's presence costs no extra GitHub API call while reading the config would. They also agreed the brand name should not be swapped into copied method files unless it served a real purpose; checking the files showed it didn't (they find the brand through `CLAUDE.md`), and the swap was freezing those copies against updates. The organic-fill contract (building single standing docs on demand from their own prompts) was split off as a second step, since it's more product call than plumbing.

**Why it matters:** Token cost and reliability at setup, a brain that exists before anyone builds it, and a cheap, unambiguous built-or-not signal for the apps.

**Inferred rule:** Deterministic work belongs in a script the model calls, not in instructions the model follows by hand. When the same list drives two jobs (setting up a brain and updating one), keep one list and have both jobs read it.

**Scope judgment:** Method and bundle only; standing brains need nothing but the pin bump, so `migrations/v23.md` is a no-op. The web app's built check and the backend's scaffold call live in other repos and are flagged in the release note and `system/brain-sync.md`.

**Follow-up, same session:** Anton asked how reliably the marker would come off, since the web app will never show a marked brain as built. Leaving it to the model at the end of a multi-hour build was the weak point, so the marker now comes off in code: the existing `pull-log` PostToolUse hook, which already runs after every Parker MCP call, deletes it when the build reports its first finished phase after Phase 0 to `update_parker_brain_setup_status` (or the whole run as completed). Anton's call was that a brain with real docs isn't "just scaffolded" anymore, so the marker should come off at the first real phase, not at the end. Reusing that hook meant no new hook registration and no Codex re-approval. The closeout still deletes the marker if it's there, which covers a build whose status calls never went through. `BUILD-STATUS.md` at the root now carries the "build under way or stopped partway" signal on its own, for the session-start hook, `/get-started`, `/update-brain`, and optionally the web app.
