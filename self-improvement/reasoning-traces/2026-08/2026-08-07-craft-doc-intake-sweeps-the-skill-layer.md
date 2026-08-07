---
trace_id: 2026-08-07-craft-doc-intake-sweeps-the-skill-layer
date_captured: 2026-08-07
source: chat
source_ref: Alex's pre-PR review of the v15 intake — "i see a lot of the creative strategy context docs have changed but only one of the skills has changed... just trying to make sure that we're not missing something here"
trigger_type: correction
scope: system
brand: global
team: creative-strategy
confidence: strong
status: applied
target_surfaces:
  - .claude/skills/hooks/processes/trigger-event.md
  - .claude/skills/hooks/processes/INDEX.md
  - .claude/skills/hooks/strategy.md
  - .claude/skills/headlines/SKILL.md
  - .claude/skills/headlines/strategy.md
  - .claude/skills/iterations/processes/static-headline-iteration.md
promotion_condition: already applied — proposed and approved in the same session
---

**What happened:** A seventeen-doc craft intake landed in `creative-strategy-context/` and only one craft skill was touched. Alex asked, before opening the PR, whether that was correct or whether something had been missed. Two genuine gaps surfaced, plus a third file neither of us had named.

**Decision context:** The default answer was "correct, and by design" — the skills load their canonical docs at runtime and call them source of truth, so a doc getting richer propagates for free. That reasoning is right and it covered most of the intake: ugly ads, creator briefs, static design, persona and brand-size additions all reached their skills with no skill edit. But it is right only where the skill *points at* the doc. It is wrong in two specific shapes, and both were present.

**Inferred rule:** When a craft doc changes, the runtime-reference architecture handles it — except in two places, which have to be swept by hand every time:

1. **A new format or pattern needs its execution layer built.** `hooks.md` gained format #22, but the hooks skill has a per-format process file for seventeen formats and a `processes/INDEX.md` that explicitly reasons about which formats deliberately lack one. A new format that is silently absent reads as an oversight rather than a decision, and — more importantly — `strategy.md` is where format selection actually happens, so a process file that nothing routes to is the same as no process file. Adding the file is half the work; the awareness-stage line, the emotional-driver line, and the format menu are the other half.

2. **Flat restatements of a rule the doc just qualified now over-state it.** `lifestyle-headline-generator.md` qualified the no-reviews rule (praise does not scale; a verbatim carrying identity, a vivid image, or real charge is the exception and gets lifted in her register). Three skill files restated the testimonial trap flatly, in two different skills. The doc being source of truth does not help here, because these lines are the *quality gate* — they are what gets applied, and a gate that has not heard about the exception will reject the exception.

**Scope judgment:** The sweep is two greps, and it is cheap enough to run on every craft-doc intake. First, does any changed doc add a named format, pattern, or process the skill layer enumerates? Second, does any changed doc *qualify* a rule that skills restate in their own words — and does that restatement appear in sibling skills too? The third file here (`iterations/processes/static-headline-iteration.md`) was found only by the second grep; it had drifted a step further already, carrying an extra phrase the headlines version never had. Same rule, two skills, two wordings, is the drift this catches.

**What deliberately did not change:** `headlines/processes/headline-from-review-verbatim.md` already drew the distinction correctly — specific and visual, the customer's own register, carries an emotional charge, filler is not a nugget. The doc change ratified that process rather than changing it. Sweeping does not mean editing everything the grep returns; the process layer was already right and touching it would have been noise.

**Routing:** New `trigger-event.md` process built on `reaction.md`'s shape, with the zone caution carried in because #22 is a high-intensity open and the existing cold-traffic guidance in `strategy.md` and `hook-psychology.md` #11 applies to it. Added to `processes/INDEX.md`, the `strategy.md` format menu, the problem-aware awareness line, and a new shame/social-cost emotional driver — none of the five existing drivers covered a problem whose stakes are dignity rather than function. Testimonial-trap qualifier applied to `headlines/SKILL.md`, `headlines/strategy.md`, and `iterations/processes/static-headline-iteration.md` in matching language.
