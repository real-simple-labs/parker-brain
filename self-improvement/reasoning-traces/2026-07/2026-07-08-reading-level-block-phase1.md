---
trace_id: 2026-07-08-reading-level-block-phase1
date_captured: 2026-07-08
source: chat
source_ref: Jimmy asked that every prompt's output be written at a tenth-grade reading level; clarified scope to Phase 1 docs, voice-not-depth
trigger_type: product_rule
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - prompts/_reading-level-block.md
  - prompts/{audits-*, brand-profile, competitor-profile, personas, voice-of-customer, market-synthesis, open-loops} (67 embeds)
  - scripts/sync-open-loops-core.py
  - scripts/propagate-to-brand-brains.sh
  - system/system-of-records.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Jimmy asked that the output of "any prompt that we have within here" be written at a tenth-grade reading level. Two clarifications narrowed it: (1) the point is *voice, not depth* — override Claude Code's terse, built-for-developers default so the docs read like a human talking, while keeping full rigor; (2) scope is the **Phase 1 docs only**, not Phase 2 strategy and not Phase 3 creative.

**Decision context:** A blanket "tenth-grade output" rule collides with two standing doctrines. The `CLAUDE.md` Output Standards keep written deliverables dense and specific, and the voice block's tenth-grade rule was scoped to *how Parker talks to a person* (chat), not deliverables. The fix threads both: change the *words* (plain, human, readable) without touching the *substance* (density, claim marks, numbers, verbatims, sources all stay). Implemented as a new marker-synced block `_reading-level-block.md` rather than hand-pasted prose, because a behavior rule that must survive a cloned brain has to be structural and drift-checkable, not instruction text sprayed across 67 files. Folding it into an existing block (expertise-core / open-loops-core) was rejected: those blocks also ride Phase 2 and Phase 3 prompts, so folding would leak the rule past the approved scope. A dedicated block embedded only in the 67 Phase 1 doc prompts is the scoping tool.

Deliberately excluded from the block: the em-dash / AI-writing-tells doctrine. Per `system-of-records.md`, that doctrine governs creative outputs only and never context/system/prompt docs, so the reading-level block says nothing about em dashes.

**Why it matters:** The runtime's native register is the wrong voice for a doc a marketing strategist reads. Left unstated, the model defaults to clipped, jargon-packed, engineer-skim prose. Naming the override once, in a synced block, resets every Phase 1 doc's voice at once and keeps it from drifting.

**Inferred rule:** Reading level and rigor are independent axes. A doc can be dense, specific, and evidence-heavy *and* read at a tenth-grade level; plain words are a property of the prose, not a discount on the content. When a voice rule needs to apply to a subset of prompts, a dedicated synced block embedded only in that subset is the right tool — reusing a wider block over-applies.

**Scope judgment:** Phase 1 only, by Jimmy's explicit call. Phase 2 strategy docs are human-read prose too and could take the same block as a trivial follow-on if he wants it; flagged, not done. Creative stays on brand voice. Standing brands' already-built Phase 1 docs were written under the old standard and are flagged for re-run on their next refresh, not re-run now.

**Routing:** New source block + 67 marker embeds (after `expertise-core:end`, else after H1); `reading-level` registered in the sync script's BLOCKS map and docstring; `system-of-records.md` Synced-blocks registry and audit-checks note updated; propagate deliberate-adds gains the new source file so standing brains' `prompts/` stays a mirror (the 67 embeds refresh via rsync `--existing`; onboarding copies the whole tree so new brains are covered). Sync run, `--check` clean.
