---
trace_id: 2026-07-03-rsl-is-doctrine-canon-script-coach-refit
date_captured: 2026-07-03
source: chat
source_ref: Jimmy's request to review the script-coach skill for Fable-era quality, and his three calls on the refit
trigger_type: strategic_decision
scope: product_architecture
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - ~/.claude/skills/script-coach/SKILL.md (user-level skill, outside this repo)
promotion_condition: explicit approval — Jimmy picked all three options directly
---

**What happened:** Jimmy asked for a review of the script-coach skill ("done with opus, want to make sure it's fable quality"). The review found the problems were drift, not writing: the skill routed extracted canon rules to the lab tree (`~/Parker-skills/parker-v2/creative-strategy-context/`) and hand-copied to old vaults plus `~/parker-brain` — with `rsl-parker-brain`, where all current doctrine lives, absent from its write and copy lists entirely — plus a stale opus model pin and no awareness of the review gates, `ai-writing-tells.md`, or `voice-lint.py`.

**Decision context:** Three calls, all Jimmy's: (1) **`rsl-parker-brain` is the single canonical home for creative-strategy doctrine.** Script-coach rules land here; the lab `parker-v2` doctrine copies become read-only history (the training log stays in the lab, since round history with verbatim feedback is lab material per the repo boundary); propagation to brand brains runs through propagate-craft, never hand-copies. (2) **Generation pins to fable**, with the model recorded per training-log round and the opus→fable comparability break noted. (3) **The gate-comparison step is added:** after Jimmy's critique — never before, his read must stay uncontaminated — both reviewer agents run on the identical raw draft, and the three-way diff routes into canon: Jimmy-caught-gates-missed is a doctrine gap fixed like any feedback; gates-flagged-Jimmy-shrugged is a false-positive candidate softened if it recurs. Each round now evals the canon and the reviewers at once.

**Why it matters:** Two live canons drift in opposite directions — the next coaching round would have written rules into a lab copy missing Tell 11, the register rule, and the gates, while the open-source factory never received them. And the coaching loop was the natural home for gate evaluation: Jimmy's eye is the ground truth the reviewers should be graded against, and the raw-generation step already produces the perfect test artifact.

**Inferred rule:** One doctrine, one home: any skill that writes rules must write them to `rsl-parker-brain` and propagate outward; a skill that hand-copies canon into individual trees is a drift engine. And human-first ordering in eval loops: the human read always precedes the machine read it grades.

**Scope judgment:** Applies to script-coach and to any future coaching/training-loop skill. The training log staying in the lab is deliberate (raw feedback and brand-specific history do not belong in the product repo). The gate step's ordering rule (Jimmy before gates) is load-bearing, not stylistic.

**Routing:** Full rewrite of `~/.claude/skills/script-coach/SKILL.md` (canon-home note, fable pin with logged model, gate-comparison step 4, routing table updated to the current surfaces including the agents and the linter, propagation through update-parker-skill + propagate-craft). This trace is the in-repo record, since the skill itself lives at user level outside version control here.
