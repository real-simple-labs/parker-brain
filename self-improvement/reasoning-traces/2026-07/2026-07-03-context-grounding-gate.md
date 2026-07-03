---
trace_id: 2026-07-03-context-grounding-gate
date_captured: 2026-07-03
source: chat
source_ref: Jimmy's follow-up on the voice gate — "do you believe this is going to solve it, not looking at the expert context docs as well... we need a system that is extremely good at knowing exactly what context docs are needed"
trigger_type: product_rule
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - .claude/agents/context-grounding-review.md
  - scripts/grounding-check.py
  - global/knowledge/creative-strategy/expertise-routing.md
  - .claude/skills/scriptwriting/SKILL.md
  - .claude/skills/headlines/SKILL.md
  - .claude/skills/hooks/SKILL.md
  - .claude/skills/ai-ad-generation/SKILL.md
  - .claude/skills/iterations/SKILL.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** Right after approving the voice gate, Jimmy asked whether it would actually solve the cloned-brain problem without also verifying the output came from the expert context docs and the right context generally — domain expertise, brand expertise, and the tool calls a real strategist would make. His framing: a creative strategist doesn't deliberate over which documents to read; the right context is baked into their mind. The goal is a system extremely good at knowing exactly what context each response needs.

**Decision context:** The honest read he approved: the voice gate covers surface only, and everything defending grounding — the sign-off stamps, expertise-routing's self-graded closing test, the MUST-load lists — was the instructional pattern he rejects. The approved design applies the same three-layer structural shape that had just worked for voice: (1) a deterministic checker, `grounding-check.py`, that traces quoted verbatims against the vault (fabrication detection by grep), resolves cited source paths on disk, and reports receipt presence; (2) an independent `context-grounding-review` agent that derives the right loads and pulls for the task from the routing catalog, brand vault, and tool inventory, then diffs against the output's *vocabulary evidence* rather than its claimed sources; (3) a required Grounding Review receipt block in each creative skill's output contract. Gate order is grounding then voice, because grounding changes content and voice changes lines. The checker was demonstrated on a fake mini-vault before wiring: real verbatim traced, invented quote flagged, real source resolved, fake citation caught.

**Why it matters:** The "baked into their mind" instinct cannot be instructed into existence; it forms under consequence. The injected catalog is the memory and the generous-planner posture is the instinct, but nothing ever punished under-pulling — so it persisted. The bounce is the consequence: work built from general knowledge instead of the brand's actual context goes back for re-pulls and regeneration, and each bounce is a reasoning trace about how the planner should have routed that task shape, which `/improve-system` folds back into the routing layer. That loop, not more instruction text, is how the retrieval instinct gets baked in.

**Inferred rule:** Verification of *inputs* is a separate gate from verification of *surface*, and it runs first. When checking whether a model used its sources, never trust the citation — check the evidence: does the output speak the source's vocabulary, do its verbatims trace, do its cited paths resolve. Claimed sources are claims; fingerprints are proof.

**Scope judgment:** Wired into the five creative skills where the voice gate lives. The mechanism generalizes to audits and syntheses (the routing map covers them and the same checker works), but Jimmy chose the narrower scope this session; widening it is a natural follow-up, not an assumption to act on.

**Routing:** Applied across the agent, the checker, the five skills (gate step, Grounding Review receipt, hard rule), expertise-routing's test section, the ship lists (onboarding-runner, propagate deliberate-adds, propagate-craft), and the index docs. Flakes propagation still deferred to Jimmy's trigger.
