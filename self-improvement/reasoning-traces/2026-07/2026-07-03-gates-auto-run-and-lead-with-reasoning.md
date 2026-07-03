---
trace_id: 2026-07-03-gates-auto-run-and-lead-with-reasoning
date_captured: 2026-07-03
source: brand_output_review
source_ref: Jimmy reviewed a real skill-driven script run in the TPJ brain — the model offered the review agents as an optional "second opinion" and buried the reasoning in a label list
trigger_type: correction
scope: skill
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
promotion_condition: already applied — explicit correction and approval in the same session
---

**What happened:** Reviewing a real skill-driven script run, Jimmy hit two problems. (1) The model ran the mechanical linter itself, self-audited, and then *offered* the independent review agents as an optional "second opinion" at the end — "Want me to run it through the full grounding + voice reviewer agents?" The whole point of the gates is that they review before the user ever sees the output, not that the model asks permission. (2) The output led with the script and buried the strategic justification in a bottom label-list (framework, awareness stage, sophistication, dominant emotion, ICP). Jimmy: that "just doesn't tell me anything" — he wants the reasoning for why this script is worth writing up front, not word-vomit at the end. Notably the earlier freelanced script led with exactly that good reasoning; the skill made it worse.

**Decision context:** Both are defects in the skill wording I authored. On the gates: the skill had a self-quality-audit step (step 6) plus the two agent steps (7-8), and the model conflated "I ran voice-lint and read it over" with the gate, treating the independent agents as extra credit. Fix: the gate steps now state the agents run automatically, before presenting, never offered, never a "second opinion"; running the linter yourself is explicitly not the gate (that is the writer grading the writer); and the output's Grounding Review / Voice Review blocks are the agents' returned verdicts, which the model cannot write itself — no verdict block means the gate never ran and the output is not done. Applied across all five creative skills via a shared gate-step preamble and a matching hard rule. On the output: scriptwriting now leads with a "Why this script" prose section (the idea gate said out loud — who it's for, the opening it fills, why now, the bet), folds awareness/emotion/sophistication into that reasoning only where they explain the call, and replaces the label-list "Script Brief" with a lean "What it's built from" (reference adapted + why, customer verbatims with attribution, only the new shots to film). The label-list is explicitly banned as a hard rule.

**Why it matters:** A gate the model can offer instead of run is not a gate — it degrades to exactly the freelanced, ungrounded, self-graded output the whole system was built to stop, which is what happened. And an output that leads with a form instead of the reasoning fails the actual job: the user reads the justification first to decide if the idea is worth filming. The freelanced version proved the reasoning-first shape is better; the skill should encode it, not fight it.

**Inferred rule:** A required verification step must be framed as automatic and pre-presentation, never as an offer — the moment a skill lets the model ask "want me to check it," the model will skip the check and offer it. And an output contract leads with the reasoning a decision-maker needs, never a label list; labels are paperwork, prose is a strategist talking. Enforce both structurally: the receipt block carries the agent's returned verdict (unwritable by the model), and the lead section is the justification.

**Scope judgment:** The automatic-gate fix applies to all five creative skills (all shared the offerable-gate flaw). The lead-with-reasoning restructure was applied to scriptwriting, where Jimmy saw it; the same principle should reach the other four output structures as they are next touched, but they were not restructured in this pass.

**Routing:** All five creative skills got the automatic-gate preamble + hard rule; scriptwriting additionally got the "Why this script" lead, the leaner "What it's built from," the label-list ban, and the receipt-blocks-are-agent-verdicts wording. Re-shipped into the TPJ brain the same session so the fix is testable. Factory canon on the creative-review-gates branch (PR #17).
