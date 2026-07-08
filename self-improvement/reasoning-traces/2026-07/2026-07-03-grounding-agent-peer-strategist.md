---
trace_id: 2026-07-03-grounding-agent-peer-strategist
date_captured: 2026-07-03
source: chat
source_ref: Jimmy on the grounding agent — "I don't know if it would be equipped to review outputs to determine if it actually sounds like something a creative strategist would say... step one is actually this agent going and reviewing those documents to learn itself"
trigger_type: correction
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - .claude/agents/context-grounding-review.md
  - system/parker-system-map.md
promotion_condition: already applied — explicit approval in the same session
---

**What happened:** After seeing both review agents, Jimmy flagged that the grounding reviewer wasn't equipped to judge whether an output sounds like something a creative strategist would say. His fix, stated directly: step one is the agent reviewing the method documents itself — learning first — and only then providing a quality review of the output.

**Decision context:** The agent as first built was a citation checker with a vocabulary test: it could verify a doc's named concepts appear in the output (proving the doc was opened) but never read the docs deeply itself, so it could not catch the second failure a real senior reviewer catches — the method loaded and then misapplied. The reshape: (1) the agent's first move is now reading the routed method docs end to end, under the same rule the routing map imposes on generators — you cannot judge work through a method you have not loaded; (2) the review gains the applied-not-just-opened dimension, a MISAPPLIED METHODS section where every finding must cite the doc passage the output violates; (3) `grounded` tightened to require no recommendation-changing misapplication; (4) a guardrail against taste-policing — misapplication means contradicting something a method doc states, and judgment calls the method leaves open stay the writer's, even when the reviewer would decide differently. The added token cost of full doc reads per review was accepted explicitly as the price of the review being worth anything.

**Why it matters:** A reviewer with less expertise than the writer is theater. The generating skill loads the methods; a gate that never does can only check surface compliance, so it would pass work that speaks the vocabulary and botches the reasoning — the exact failure mode of a smart model imitating expertise. Making the reviewer do the reads first is what makes it a peer rather than a spell-checker.

**Inferred rule:** Any independent review agent must first load the same canonical expertise the work it reviews was supposed to be built from — the reviewer's authority comes from the docs, never from the model's general opinions. And review findings about method are only valid when they cite the method: doc-cited or it didn't happen.

**Scope judgment:** Applies to the grounding reviewer and to any future review-shaped agent (the birth principles' "independent reviewer" leg should be read with this in mind: independent AND equipped). The voice reviewer already follows the pattern at its narrower scope — it reads its two doctrine docs before judging. The guardrail matters as much as the power: without the doc-cited requirement, a well-read reviewer drifts into second-authoring.

**Routing:** Applied as a full rewrite of `.claude/agents/context-grounding-review.md` (learn-first step, misapplication dimension, new return section, tightened verdict, guardrail) and the system-map agent entry + changelog. No skill edits — the skills spawn the agent by name and its own definition governs how it reviews. File already ships in the review-gate bundle, so ship lists unchanged.
