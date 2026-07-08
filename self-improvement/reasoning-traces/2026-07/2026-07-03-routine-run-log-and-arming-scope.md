---
trace_id: 2026-07-03-routine-run-log-and-arming-scope
date_captured: 2026-07-03
source: chat
source_ref: Jimmy wanted the refresh routine to actually fire weekly and keep a running log; asked whether an open-loops routine exists
trigger_type: strategic_decision
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - templates/routine-log-template.md
  - templates/brand-routines/claude/skills/refresh-context/SKILL.md
  - .claude/skills/refresh-context/SKILL.md
  - templates/brand-routines/claude/skills/research-loops/SKILL.md
  - templates/brand-routines/schedules/README.md
  - system/refresh-cadence.md
  - prompts/onboarding-runner.md
  - scripts/propagate-to-brand-brains.sh
promotion_condition: already applied — Jimmy delegated the design and picked the arming scope
---

**What happened:** Jimmy wanted the weekly refresh to be an actual routine that fires and keeps a running log, "instead of it just being a document," and asked whether an open-loops routine exists to run the full process.

**Decision context:** Two things were already built and just needed to be surfaced. (1) The open-loops routine exists: `research-loops` (weekly, Wed) runs the full pipeline — roll-up → advance → validate → re-validate → digest → doc-alignment. Nothing to build. (2) refresh-context is already a real routine with a schedule recipe; what makes it "fire" is registering the cron via `/setup-routines`, which is per-account and deliberately not committable — so it is a live routine whose arming is a one-time per-instance step, not "just a document." The genuine gap in Jimmy's ask was the *running log*: the brain had a live due-date view (`refresh-schedule.md`) but no durable, append-only history of what actually ran each week. Built `running-notes/routine-log.md` (template `templates/routine-log-template.md`, stamped empty at build, shipped via `parker-system/templates/` and added to the propagate deliberate-adds since `--existing` never adds new files), a shared ledger every standing routine prepends one entry to — wired into refresh-context and research-loops, documented in the schedules README and the refresh-cadence doctrine. On arming: Jimmy chose to arm through `/setup-routines` in the brand-brain instance rather than here, which is correct — the factory has no brand loop or doc data, so a live agent armed against it would no-op weekly. Registering it here was surfaced as wrong-for-context and declined.

**Why it matters:** The log is the difference between "the brain is supposed to run weekly" and "here is proof it ran, and what it did." It answers a question the due-date view structurally cannot. And keeping arming in the brand-brain instance holds the schedules architecture: routines arm where their data lives, never in the factory.

**Inferred rule:** A live view of what is *due* is not a record of what was *done* — a self-running system needs an append-only run history, separate from its state view, or "did it actually fire" is unanswerable. And before arming a durable recurring agent, check that the target instance has the data the routine acts on; arming against an empty factory is a no-op worth declining even when asked.

**Scope judgment:** The run log is a shared routine ledger, wired into the two routines in play now (refresh-context, research-loops); the other four should adopt the same one-line append as they are next touched. Arming stays a per-instance `/setup-routines` step. No new routine was created — both the refresh and open-loops routines already existed; the work was completing the log and surfacing the arming path.

**Routing:** New template + both refresh-context copies (kept in sync) + research-loops + schedules README + refresh-cadence doctrine + onboarding stamp step and verification check + propagate deliberate-adds. Committed on the creative-review-gates branch (PR #17).
