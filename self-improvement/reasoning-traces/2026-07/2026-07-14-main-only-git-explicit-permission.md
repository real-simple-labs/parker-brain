---
trace_id: 2026-07-14-main-only-git-explicit-permission
date_captured: 2026-07-14
source: chat
source_ref: Anton reported hosted Claude Code sessions obeying the harness's "develop on branch claude/…, NEVER push elsewhere without explicit permission" and stranding brain work on side branches
trigger_type: correction
scope: system
brand: global
team: product
confidence: strong
status: applied
target_surfaces:
  - templates/brand-routines/claude/skills/save-brain/SKILL.md
  - templates/brand-brain-CLAUDE-template.md
  - prompts/onboarding-runner.md
  - templates/brand-routines/README.md
  - templates/brand-routines/claude/README.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** A hosted Claude Code session working in a brand brain followed its harness instruction ("develop on the designated branch `claude/parker-brain-setup-…`; NEVER push to a different branch without explicit permission") instead of the brain's standing "no branches, no pull requests" rule, leaving work on a side branch. Nobody on a brand team reviews or merges PRs — most members are non-technical — so branch-parked work is effectively lost.

**Decision context:** The harness instruction is conditional: it forbids pushing elsewhere *without explicit permission*. The docs forbade branches but never granted that permission, so the two rules never actually met — the agent had no sanctioned path to `main`. The fix grants the permission in so many words, in the surfaces that are in context when the harness instruction is: the `/save-brain` canonical paragraph and hard rule, and the always-loaded brand `CLAUDE.md` (via its template), with the delivery mechanics spelled out (`git push origin HEAD:main` after the usual rebase — work on the assigned branch if the harness insists, but deliver to `main`). Short reference clauses went to the onboarding runner's save step and the two routine-bundle README summaries. A `git-guard.py` structural block on non-main pushes was proposed and skipped per Anton's simplicity-over-hardening preference; a migration step editing standing brains' `CLAUDE.md` was proposed and rejected — template only, so the grant reaches standing brains through the bundle-synced `/save-brain` and new builds through the template.

**Why it matters:** A brain whose updates sit on unreviewed branches silently stops being shared: routines and teammates read `main`, so the work might as well not exist.

**Inferred rule:** When a harness or platform instruction conflicts with a repo's operating contract on a conditional ("without explicit permission"), don't fight the instruction — satisfy its condition explicitly in an always-loaded doc, and pair the grant with the reason branch-parking fails here.

**Scope judgment:** Bundle- and template-only; `migrations/v13.md` is a no-op. Shipped in the v13 release alongside the onboarding existence triage.
