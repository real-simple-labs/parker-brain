---
trace_id: 2026-07-03-strategy-first-tactical-baseline
date_captured: 2026-07-03
source: chat
source_ref: Jimmy — "make sure you're looking at the strategy first and foremost to understand the high-level overview... look through the idea bank and the evaluated ideas, and use that as the baseline for the different tactical execution of the script, the headline hook, et cetera"
trigger_type: context_rule
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - .claude/skills/scriptwriting/SKILL.md
  - .claude/skills/headlines/SKILL.md
  - .claude/skills/hooks/SKILL.md
  - .claude/skills/ai-ad-generation/SKILL.md
  - .claude/skills/iterations/SKILL.md
  - .claude/agents/context-grounding-review.md
  - .claude/skills/update-parker-skill/SKILL.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Jimmy added the execution hierarchy the creative skills were missing: before tactical work, look at the strategy first and foremost for the high-level overview, then the idea bank and the evaluated ideas, and use those as the baseline for executing the script, headline, hook, et cetera.

**Decision context:** The five creative skills' load steps named brand *identity* context — profile, ICP, personas, VoC, compliance — but never `strategy/` or `idea-bank/`. So tactical work executed against who the brand is, but not against what the brand has decided to do or the ideas it has already captured and graded. A real strategist starts from the committed plan and the pipeline, not from zero. The wiring: each skill loads `strategy/` (working thesis, roadmap calls) as the frame first, then checks `idea-bank/` including evaluated ideas; a request matching an idea-bank entry executes from that entry carrying its reasoning; a request contradicting the committed strategy is surfaced with the conflict named rather than silently executed (strategy is the baseline, the user is still the boss); a fresh brain without those surfaces says so in one line rather than faking a gate. The grounding reviewer's become-the-strategist pass reads both surfaces and flags strategy contradictions (cited to the strategy passage, same anti-taste-policing guardrail as method misapplications) and obviously-matched-but-unused idea-bank entries as missing loads.

**Why it matters:** Without this, the skills produce well-crafted, well-grounded tactical work that is strategically orphaned — a good script for a message the roadmap ruled out, a fresh concept re-invented cold when the idea bank already held the graded version with its source examples. The idea bank exists precisely so the brand's prior thinking compounds; a skill that never checks it wastes that memory.

**Inferred rule:** Tactical execution has a load order: committed strategy (the frame) → idea pipeline (the baseline) → brand identity context (the material) → method docs (the craft). Skipping a level up the hierarchy produces work that is locally good and globally wrong.

**Scope judgment:** Applies to skills that execute tactically. Promoted into the birth principles so future creative skills inherit it at creation. The conflict-surfacing behavior is deliberate: strategy misalignment is surfaced, not auto-blocked — users can knowingly run counter-strategy tests. Applies with judgment on iterations (strategy frames the strategic goal; the idea bank feeds new elements) and lightly on fresh brains where the surfaces don't exist yet.

**Routing:** Load-step edits in the five creative skills (plus the scriptwriting idea gate now starts its read from strategy and idea bank), the grounding reviewer's vault read and strategy-anchoring check, two birth-principle changes in `update-parker-skill` (strategy-first added; the reviewer leg upgraded to independent-and-equipped, closing the pending item from the peer-strategist round), system-map changelog. All edits in already-shipping files; ship lists unchanged.
