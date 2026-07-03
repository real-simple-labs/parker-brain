---
trace_id: 2026-07-03-refresh-context-phase-dependency-spine
date_captured: 2026-07-03
source: chat
source_ref: Jimmy asked for a weekly Context refresh routine that looks across all phase 1/2/3 docs to determine if anything needs re-running; on the fork he said to rely on my judgment
trigger_type: strategic_decision
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - system/refresh-cadence.md
  - .claude/skills/refresh-context/SKILL.md
  - templates/brand-routines/claude/skills/refresh-context/SKILL.md
  - templates/brand-routines/schedules/refresh-context.md
promotion_condition: already applied — Jimmy delegated the design call after the duplication check
---

**What happened:** Jimmy asked to add a weekly "Context refresh" routine that looks across the Phase 1/2/3 docs to determine if anything needs re-running to stay current. The duplication check found the routine largely already exists: the `refresh-context` skill (shipped via PR #13) runs weekly, reads every standing doc's `refresh_by` and the `refresh-schedule.md` ledger, surfaces overdue docs, and re-runs their generating prompts. Rather than build a parallel routine (drift), the move was to find and close the real gap. Jimmy delegated the design call.

**Decision context:** The existing routine is calendar-driven: a doc re-runs when its own clock expires. What it did not do is reason about dependency staleness across the phase chain — a Phase-2 roadmap built on a Phase-1 performance read is out of date the moment that read is refreshed and the picture changes, even though the roadmap's own `refresh_by` is months away. The cadence doctrine already carried two narrow event-driven rules of exactly this shape (`brand-profile-narrative` re-runs after its sub-context inputs change; `idea-evaluation` re-runs when the roadmap is re-approved), so the enhancement generalizes those two special cases into one phase-spine principle rather than inventing a new mechanism. Doctrine went to `system/refresh-cadence.md` (the canonical cadence home): the spine Phase 1 → Phase 2 (four strategy inputs → strategic-roadmap) → Phase 3 (idea-evaluation), the edges that carry staleness downstream, and the materiality gate — a downstream doc is stale-by-dependency only when an upstream input's `generated_on` is newer than the downstream's AND the upstream re-run materially changed the read, so a carry-forward-unchanged refresh does not thrash the whole chain every cycle. Execution went into the `refresh-context` skill (both the factory `.claude/skills/` copy and the `templates/brand-routines/` source, kept identical): a new phase-spine process step, a materiality note on the re-run and schedule-update steps, a hard rule against auto-cascading on a touch, and the deliverable now separates date-overdue from stale-by-dependency. The schedule recipe was updated to match.

**Why it matters:** "Is anything out of date" as a strategist means it, is not a calendar question — it is whether something underneath a doc moved. Without the spine, the brain would keep trusting a roadmap whose evidentiary base had already shifted, which is the exact silent-staleness failure the whole refresh mechanism exists to prevent, one level up.

**Inferred rule:** Before building a routine, check whether one already owns that job; if it does, complete it rather than duplicating it. And freshness is a graph property, not only a per-doc date: a synthesis is stale when a material input changed since it was built, and that cascade should be surfaced with a materiality gate so it does not thrash.

**Scope judgment:** The cascade runs only downstream along the phase spine and only on material change; briefs stay exempt (per-campaign). Surfaced as recommendations, never auto-cascaded, consistent with the routine's existing surface-before-acting discipline. Ships to brand brains through the existing routine bundle — no ship-list change, since refresh-context already travels.

**Routing:** Doctrine in `system/refresh-cadence.md`; execution mirrored into both refresh-context SKILL.md copies (description, mechanism subsection, process step 3, materiality on steps 5–6, hard rule, deliverable) and the schedule recipe. Both skill copies verified identical; process steps renumbered 1–8 with no gap.
