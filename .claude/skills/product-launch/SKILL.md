---
name: product-launch
description: Write launch creative for an established brand's new product or SKU — scripts, concepts, hooks, copy, headlines, shot lists, founder videos, multi-video themes, or a full launch content plan. Classifies the launch into one of three scenarios first, because a new color, a new format, and a new audience are three different briefs. Use when the brief is a product or SKU that has not had ads run on it yet.
triggers:
  - launch ad for our new product
  - launch concept for this SKU
  - we're launching a new product
  - we're dropping a new flavor
  - we're dropping a new scent
  - ad for our new colorway
  - new collection launch
  - new product drop ad
  - meet the new / introducing ad
  - bundle launch ad
  - spinoff product script
  - founder launch video
  - launch shot list
  - pre-launch audit
  - launch content plan
  - through-line across our launch videos
---

# Product Launch

## Goal

Produce launch creative for an established brand putting a new product or SKU into market — creative for something that has not had ads run on it yet. The skill classifies the launch before writing anything, because a new color, a new format, and a new audience are three genuinely different briefs that get confused constantly, and the wrong classification produces the wrong script no matter how well written it is.

This skill handles the launch brief end to end. It does not replace the craft skills it calls — when the deliverable is a script it runs through `scriptwriting`, hooks through `hooks`, headlines through `headlines`. What this skill owns is the launch-specific reasoning those skills do not carry: which scenario, which phase, which proof is honest, and what makes the newness visible.

## Scope gate — run this first

This skill is for **established brands with prior ad history and at least one proven SKU**. Before anything else, confirm the brief is actually in scope. Three routes out:

- **A brand launching its first product, running its first ads.** Different playbook, no account data to lean on. No doc exists in the brain for this yet — say that plainly rather than improvising.
- **Geographic expansion with existing products.** Its own brief. No doc exists in the brain for this yet either.
- **A restock, back-in-stock moment, or "limited edition" framing on an unchanged SKU.** Nothing is new, so this is not a launch. It is routine performance creative with an urgency mechanic — route to `scriptwriting` or `iterations`.

A limited or seasonal drop that introduces a genuinely new colorway, flavor, or scent **is** in scope, as Scenario A. The test is whether something new exists, not whether the brand is making an announcement. The full scope reasoning is in `parker-system/creative-strategy-context/new-product-launch-creative.md`.

## What you are working from

The launch method is `parker-system/creative-strategy-context/new-product-launch-creative.md` — the scenarios, the newness taxonomy, the authority-transfer and proof-substitution doctrine. Load it before classifying; this skill is the execution layer on top of it and assumes it.

Alongside it, routed by `parker-system/creative-strategy-context/expertise-routing.md`: `killer-performance-ads.md` for the canonical awareness-stage definitions (the launch-specific mapping is in the launch doc; the definitions are not restated anywhere), `hooks.md` and `hook-psychology.md` for openers, `adapting-scripts.md` when the brief carries competitor benchmark refs or inspiration to adapt, `spoken-script-voice.md` and `ai-writing-tells.md` for anything spoken or written, and the format libraries for what the account's tags actually call things. Brand and account data pull through the Parker tools inventoried in `parker-system/system/parker-tools.md`.

Division of labor: the launch doc is the reasoning (what the scenarios are, why launches differ), `strategy.md` here is the classifier and the routing (which scenario, which mode, which deliverable), and `processes/` are the execution playbooks. If a process and the launch doc disagree on what a scenario is, the launch doc wins.

## How this skill runs

1. **Load the strategy first, then brand context.** The brand's committed strategy — `strategy/`, the working thesis, the roadmap's persona and product calls — is the frame the launch sits inside; a launch that cuts against the committed roadmap gets surfaced with the conflict named, not silently executed. Then the idea bank (`idea-bank/`, including evaluated entries) for an entry this launch should execute from, carrying its reasoning and source examples. Then brand profile, ICP, personas, voice of customer, compliance, and what has been tested. If the brain has no `strategy/` or idea bank yet, say so in one line and proceed from brand context.

2. **Run the scope gate.** Above. Route out if the brief is not a launch.

3. **Classify the launch.** Run `strategy.md`. Four questions in order — scope, audience fit, type of newness, deliverable type — producing a scenario (A, B, or C) and a deliverable spec. **If any answer is unknown, ask the user. Do not guess.** Guessing here is how a Scenario A script gets written for a Scenario C launch, and it is the most expensive error in the whole flow because everything downstream inherits it.

4. **Diagnose the account before writing anything.** Run `processes/diagnose-the-account.md`. Existing top performers, the closest existing SKU, the equity language worth reusing, past winners *and* past failures, the product page, and any competitor refs in the brief. This step is not optional and it is what most weak launch creative skips.

5. **Scenario C stops here for persona work.** If the classification is Scenario C, do not proceed to writing. The new audience's persona is a required input, not a nice-to-have. Load the brand's persona vault (`personas/`, `sub-context-docs/`) for the new audience; if nothing exists, run the persona prompt tree at `parker-system/prompts/personas/` (gold layer `personas-profile.md`). If neither is available, ask the user the three-question persona mini-brief in `processes/scenario-c-audience-expansion.md` and flag that a full persona pass is recommended before scaling spend. Scenarios A and B get a light persona refresh — encouraged, not blocking.

6. **Run the scenario playbook.** `processes/scenario-a-depth-play.md`, `processes/scenario-b-bridge-and-expand.md`, or `processes/scenario-c-audience-expansion.md`. Each carries the launch frame, the angle set, and the script moves for that scenario.

7. **Map the proof.** Run `processes/proof-substitution.md`. A new SKU usually has no reviews, no UGC, and no best-seller status. Substitute honestly; never manufacture.

8. **Check special contexts and phase.** `processes/special-launch-contexts.md` for gifting, giveaway mechanics, and multi-video through-lines. `processes/launch-phase-sequencing.md` for warm-versus-cold and where this deliverable sits in the arc.

9. **Hand off to the craft skill for the actual writing.** Scripts run through `scriptwriting`, hooks through `hooks`, headlines through `headlines`, AI assets through `ai-ad-generation`. Carry the classification into the handoff — the scenario, phase, awareness stage, persona, and newness lever are context those skills need and cannot derive. Adapting a competitor ref runs through `scriptwriting`'s `adapt-existing-script` process.

10. **Run the persona-fit check and the launch audit.** Both in `processes/edge-cases-and-routing.md`. The persona-fit check is the one that catches the most common failure in this whole category — writing the new-SKU ad in the existing persona's voice when the SKU is for a new audience.

11. **The two gates run automatically, before you show the user anything.** They are not optional, not a second opinion, and never offered as a choice. Grounding first, because it changes content; voice second, because it changes lines. **If you catch yourself writing "want me to run this through the reviewer," you have already failed the gate — go run it.**

    **11a. Grounding gate.** Spawn the `context-grounding-review` agent (`.claude/agents/context-grounding-review.md`) with the user's task, the draft, the brain root, and the tool pulls made this session. It independently reads the routed method docs, runs `scripts/grounding-check.py`, and verifies the draft was built from the right context, nothing fabricated, the methods applied and not just cited. For a launch brief it should specifically be able to see that the account diagnostic actually happened. A `bounced` verdict means re-pull and regenerate the affected parts — never annotate around it — then re-run. Every bounce is captured through `self-improvement-intake` as a one-line trace so the routing layer learns.

    **11b. Voice gate.** Spawn the `creative-voice-review` agent (`.claude/agents/creative-voice-review.md`) on the grounded draft with the brand voice profile and deliverable type. Apply its rewrites and re-run until the verdict is `ships`. A flag that conflicts with sourced customer language keeps the source, with the reason carried into the Voice Review block.

    The Grounding Review and Voice Review blocks are the agents' **returned verdicts**, verbatim. You cannot write them yourself. Output with no verdict blocks did not pass the gates and is not done.

12. **Format output per the structure below.**

## Output structure

Steps 1 through 10 are the process, not the output. The user does not see the classification reasoning, the diagnostic notes, the persona check, or the audit. What surfaces is the deliverable plus a short Launch Context Summary that lets a strategist confirm the brief was read correctly.

### The deliverable

Whatever Step Zero Question 4 classified. The full spec for each type — hooks only, ad copy and headlines, founder video, shot list, pre-launch audit, multi-video theme, format recommendations — is in `processes/deliverable-specs.md`. The default when unspecified is full script plus storyboard.

**Match the deliverable to what was actually asked for.** A hooks-only brief does not get a script and storyboard. A shot-list audit does not get a script at all. Padding with sections the user did not ask for wastes their time and is a named failure of this skill.

### Launch Context Summary

Brief and high-level, after the deliverable. This is the receipt that makes a skipped classification visible, so it is not optional trim:

- **Scenario** — A, B, or C, plus one sentence on why.
- **Launch phase** — warm-audience recapture or cold-audience scaling.
- **Awareness stage** — and the persona, named specifically, not "existing."
- **Angle category and newness lever** — attribute, format, use case, audience entry, or category.
- **Brand language reused** — the slogans, campaign names, line names, and recurring visuals pulled from existing equity.
- **Proof strategy** — especially what was substituted for missing UGC or reviews.
- **What to test next** if this concept performs.

### Grounding Review

The grounding gate's returned verdict, verbatim from the agent. No block means the gate never ran, which means the work is not done.

### Voice Review

The voice gate's returned verdict, verbatim from the agent. Lint density before and after, what was flagged and fixed, any flag kept with its reason.

## Output contract precedence

When the deliverable is a script, **`scriptwriting`'s output contract governs the script itself** — "Why this script" leading in plain sentences, the beat-by-beat script, "What it's built from," and its visual-vocabulary markings. The Launch Context Summary is added on top of that structure, not in place of it. Same pattern for hooks and headlines: the host skill's output contract governs its own deliverable, and this skill adds the summary block.

Where the two would conflict, the host skill wins on the shape of the creative and this skill wins on the launch reasoning. Do not produce a form-shaped list of labels where `scriptwriting` asks for plain sentences — fold the scenario and awareness stage into the reasoning where they explain the call, and let the Launch Context Summary carry the tags.

## Hard rules

- **Classify before writing a word.** Scenario, phase, awareness stage, and deliverable type are decided first. A launch script written before classification is a guess wearing a script's clothes.
- **Ask, do not guess, on the audience question.** Whether the SKU targets an existing persona or a new one is the single most important strategic question in a launch brief. Everything downstream — voice, proof types, hook angle, which existing ads to study — hinges on it. If it is not clear from the brief and the brand context, ask.
- **Diagnose the account before writing.** Existing top performers, the closest SKU, the equity language, past winners and past failures. Most weak launch creative skips this and it shows.
- **Inherit winners and diagnose losers.** Past performance data does both jobs. A stated failure mode — low hold rates, weak second beats — is a constraint on the new creative, not just a reference. Write the launch to fix the specific failure.
- **Scenario C does not start without persona work.** The new audience's language, objections, and trusted proof types are required inputs. A Scenario C launch written from the existing persona's voice is the most common failure in this category.
- **Never reuse existing-persona hooks for a new-audience SKU.** Not as a starting point, not "adapted." Fresh angles in the new audience's voice.
- **Make the newness visible in the hook itself.** Even attribute-only launches. A launch ad where the new thing is not apparent in the first three seconds has not done its job.
- **Do not fabricate proof.** No best-selling, loved by thousands, or review counts for a product that has none. Inherited proof is honest only when it is attributed to the hero product it actually came from.
- **Authority transfers only where it actually transfers.** A brand's credibility with one audience or category says nothing to another. Re-pitch the mechanism where that is true; do not borrow the badge where it is not.
- **Reuse the brand's equity language.** Line names, campaign names, slogans, recurring visuals. Cheapest win in launch creative and the most-skipped.
- **Warm and cold are distinct deliverables.** The warm ad assumes the buyer knows the brand; the cold ad assumes they do not. Never blur them, and never confuse phase with awareness stage — they correlate but they are different variables.
- **Produce the deliverable that was asked for.** Not a full script by default. Not padded with extra sections.
- **Keep the process internal.** The classification reasoning, diagnostic notes, persona check, and audit do not surface. The Launch Context Summary is the deliberate exception, and it stays brief.
- **Source customer language from real reviews, comments, and surveys** — and match the register. A written verbatim ships as-is in a text overlay; a spoken line voiced from a review keeps the customer's vocabulary and gets re-cadenced for the mouth, per the written-versus-spoken rule in `spoken-script-voice.md`.
- **The gates run automatically, before you present — never offered.** Both review agents run every time, on their own. Running `scripts/voice-lint.py` yourself is not the gate; the gate is the independent agent, whose returned verdict fills the receipt blocks you cannot write for it.
- **Compliance is a wall.** Forbidden terms remain forbidden. Claims whitelists and blacklists from the brief are constraints, not suggestions.
- **No predicted metric improvements.** Never claim a launch concept will lift a number by some percentage.
