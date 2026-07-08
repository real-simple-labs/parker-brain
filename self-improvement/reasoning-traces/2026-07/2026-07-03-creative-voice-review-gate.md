---
trace_id: 2026-07-03-creative-voice-review-gate
date_captured: 2026-07-03
source: chat
source_ref: Jimmy's directive to incorporate Wikipedia's "Signs of AI writing" into the creative skills as a review agent on creative output
trigger_type: product_rule
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - global/knowledge/creative-strategy/ai-writing-tells.md
  - scripts/voice-lint.py
  - .claude/agents/creative-voice-review.md
  - .claude/skills/scriptwriting/SKILL.md
  - .claude/skills/headlines/SKILL.md
  - .claude/skills/hooks/SKILL.md
  - .claude/skills/ai-ad-generation/SKILL.md
  - .claude/skills/iterations/SKILL.md
promotion_condition: already applied — explicit approval on the revised proposal in the same session
---

**What happened:** Jimmy directed that every creative-work skill get an AI-sounding review on its output, grounded in Wikipedia's "Signs of AI writing," so that when a team clones parker-brain and builds a brand brain, the scripts, headlines, hooks, and iterations it produces read human. His framing of the goal: the strategy layer already makes the ideas sound — the creative-strategy knowledge plus the brand stack — so the remaining problem is purely executional, and the execution must not read as AI slop.

**Decision context:** The first proposal put the review in a separate subagent but left the trigger as instruction text in each skill. Jimmy pushed back — "I'm just not sold that if someone were to copy our PARKERBRAIN... this would be the solution" — consistent with his standing rule that enforcement must be structural, not instructional. The revision that won approval added a deterministic bottom layer: a regex linter (`scripts/voice-lint.py`) the model cannot argue with, demonstrated live discriminating a slop sample (17 flags, density 2.12) from a human-register sample (0 flags) before he approved. The final gate is three layers: deterministic lint, an independent reviewer agent that did not write the draft, and a required Voice Review block in each skill's output contract so a skipped gate is visible in the output itself.

**Why it matters:** The failure mode this closes is real and specific to the cloned-brain scenario — no Jimmy in the loop, a thin-context turn, a model happy to grade its own homework. Instructional self-review does not survive that scenario; deterministic tooling plus a separate reviewer context plus a visible output contract does. The residual limit was named and accepted: the gate strips AI surface, it cannot invent a voice — clean-but-generic output means the brand voice profile upstream is thin, and the fix is more corpus.

**Inferred rule:** When Parker needs a behavior to survive in cloned brains operated by strangers, the enforcement stack is: (1) a deterministic check where one is possible, (2) an independent context for judgment, (3) an output contract that makes skipping visible. Instruction text alone is never the answer, and demonstrating the mechanism on real samples beats asserting it.

**Scope judgment:** The AI-tells doctrine applies to creative deliverables only — the words a customer reads or hears. It is never applied to context docs, prompts, or system docs (Jimmy's standing tactical-only rule; the warn-only global hook that fires on non-creative files is a known over-application). Customer verbatims are exempt from flagging entirely.

**Routing:** Applied across the canonical doc, the linter, the agent, the five creative skills, the routing map and DOC-MAP, the ship lists (onboarding-runner step 5, propagate deliberate-adds), and the index docs (master-file-structure, parker-system-map changelog, README). Flakes brain propagation deliberately deferred — Jimmy will trigger it later.
