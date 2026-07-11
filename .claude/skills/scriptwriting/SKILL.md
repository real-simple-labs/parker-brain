---
name: scriptwriting
description: Write ad scripts that sound spoken, not written, by adapting proven reference ads into the brand's own voice fingerprint. AI cannot write good scripts cold — references are the default input and the brand script-voice profile is the sound. Every script passes the spoken-script-voice AI-tells check and read-aloud test. Net-new from scratch is the rare fallback.
triggers:
  - write me a script
  - write a script for this ad
  - new script ideas
  - script for this brand
  - adapt this script
  - adapt this ad
  - recreate this script
  - VSL script
  - long-form script
  - 30-second script
  - 60-second script
  - story-arc script
  - problem-solution script
  - rewrite this for our brand
---

# Scriptwriting

## Goal

Write ad scripts that match the brand, the audience, the awareness stage, and the format — grounded in proven reference ads from the global database. The default flow is reference-finding plus adaptation. AI cannot reliably produce good scripts from cold context; proven references provide the structural skeleton that adaptation then dresses in the brand's voice and product.

This skill writes scripts. It does not write hooks in isolation (route to hooks skill — though scripts contain hooks), write headlines (route to headlines skill), generate AI video prompts (route to ai-ad-generation), or iterate on existing winning scripts (route to iterations).

## What you are working from

Scriptwriting runs on the canonical methods, routed by `parker-system/creative-strategy-context/expertise-routing.md`: `spoken-script-voice.md`, the human-voice doctrine and AI-tells audit, mandatory before writing any words; `scriptwriting.md` and `adapting-scripts.md` for the craft and the 1:1 adaptation method; `visual-vocabulary-method.md` for per-beat visual direction, with `visuals.md` as its why-layer; and `hooks.md` for the opener. When the script casts a persona or hands off to a creator, `creative-consumption-analysis.md` reads the native content she already watches so casting and setting blend in, and `creator-briefs.md` carries the terminology and story-structure the brief needs. Reference ads and customer language pull through the Parker tools inventoried in `parker-system/system/parker-tools.md`.

## The default flow is reference-driven adaptation

Adaptation is the default because AI cannot write good net-new scripts cold. Left to invent from scratch, AI produces clean, written-sounding, AI-tell-ridden copy that dies when read aloud. Proven references supply the structural skeleton; the brand's own voice fingerprint supplies the sound. Net-new is the rare fallback, not a co-equal path. The full flow:

1. **Build or load the brand script-voice profile.** Run build-brand-voice-profile. Pull the brand's own winning scripts, read them out loud, and extract the voice fingerprint — pacing, diction, signature moves, direct-address habit, CTA shape, and the banned-by-absence list. This profile is the brand baseline; everything generated must read and sound as belonging to it. If a current profile exists, load and refresh it.

2. **Load brand context.** Brand profile, ICP, personas, voice of customer, compliance, what has been tested.

3. **Load hook context before writing the first three seconds.** If the script contains a hook, load the hooks skill strategy, the shared hook doctrine, and the brand's latest hook audit or hook history. The opener is not a decorative line at the top of a script; it is the creative gate. Do not write the hook from memory or justify it after the fact.

4. **Find reference ads.** Pull a handful of relevant reference ads via Parker MCP, in source order: the brand's own account scripts first, then the competitor and inspo scripts already captured in the brand's vault, then the niche's top organic library, then the global AI-tagged DB. Filter by the AI tags that match the user's request — format, angle, awareness stage, persona, hook type, brand type. Pick the single strongest candidate. The find-reference-ads process handles this.

5. **Adapt the reference.** Use adapt-existing-script against the chosen reference. Preserve the structural skeleton — beat count, pacing, emotional arc, proof type. Rewrite every word in the brand's voice fingerprint. Adaptation is 1:1 against the one reference, not blended across multiple.

6. **Net-new only when references fail.** If no good references exist for the request, route to one of the net-new processes. This is the exception, not the rule — AI cannot write good net-new, so even net-new scripts are held to the spoken-script-voice doctrine.

## How this skill runs

1. **Determine the path.** Run strategy.md. Reference-driven adaptation is the default. Net-new is the fallback when references are not available or the user explicitly requests fresh-from-scratch.

2. **Build or load the brand script-voice profile, load brand context, and load hook context.** Always. Run build-brand-voice-profile for the voice fingerprint; load the brand profile, ICP, personas, voice of customer, compliance, hook strategy, shared hook doctrine, and the brand's latest hook audit or hook history. These are foundational.

   **And load the strategy first, above all of it.** The brand's committed strategy — `strategy/`, the working thesis, the strategic roadmap, the who/what/say/show calls — is the high-level frame every tactical choice sits inside; read it before deciding what to write. Then the idea bank (`idea-bank/`, including its evaluated ideas) as the baseline of what's worth executing: a script request that matches an idea-bank entry executes from that entry, carrying its source examples and reasoning, instead of re-inventing the concept cold. A request that cuts against the committed strategy is surfaced to the user with the conflict named, not silently executed. If the brain has no `strategy/` or idea bank yet, say so in one line and proceed from brand context.

3. **For reference-driven adaptation:** find-reference-ads → adapt-existing-script. find-reference-ads pulls in source order — brand's own account, then captured vault competitor/inspo, then niche organic, then global DB.

4. **For net-new:** pick the right framework process — problem/solution, story-arc, VSL, awareness-staged, style-based, sophistication-matched, emotional-depth.

5. **Source customer language.** Every script — adapted or net-new — pulls language from real reviews, comments, surveys, voice of customer data. Marketing voice fails.

6. **Self-check as you draft** — read every line aloud, watch for AI-tells per `parker-system/creative-strategy-context/spoken-script-voice.md`. This is your own pre-pass while writing. It is **not** the gate, and it does not replace the two review agents below. Running `scripts/voice-lint.py` yourself is not the gate either — the linter is a tool the gate agents run inside their own context. Your own lint plus your own read is the writer grading the writer's paper, which is exactly what the gates exist to stop.

7. **The two gates run automatically, before you show the user anything.** They are not optional, not a "second opinion," and never offered as a choice. You do not ask the user whether to review — you run both, apply what they return, and only then present. **If you catch yourself writing "want me to run it through the reviewer," you have already failed the gate: go run it.** Run them in order, because grounding can change the content and voice only changes the lines:

   **7a. Grounding gate.** Spawn the `context-grounding-review` agent (`.claude/agents/context-grounding-review.md`) with the user's task, the draft, the brain root, and the tool pulls made this session. It independently reads the routed method docs, runs `scripts/grounding-check.py`, and checks the draft was built from the right context, nothing fabricated, the methods applied not just cited. A `bounced` verdict means re-pull and regenerate the affected parts — never annotate around it — then re-run. Every bounce is captured through `self-improvement-intake` as a one-line trace (task shape + what was missed) so the routing layer learns.

   **7b. Voice gate.** Spawn the `creative-voice-review` agent (`.claude/agents/creative-voice-review.md`) on the grounded draft with the brand voice profile and deliverable type. It runs the mechanical lint and the judgment pass independently, in a context that did not write the draft. Apply its rewrites and re-run until the verdict is `ships`. A flag that conflicts with sourced customer language or the reference structure keeps the source, with the reason carried into the Voice Review block.

   The Grounding Review and Voice Review blocks in the output are the agents' **returned verdicts**, verbatim — you cannot write them yourself. A script with no verdict blocks did not pass the gates and is not done.

8. **Format output per the structure below.**

## Output structure

The output leads with the reasoning, then the script, then only what earns its place. No label lists — a strategist briefing a founder talks in plain sentences, not a form.

### Why this script

Two to five sentences, up front, before the script. This is the idea gate, said out loud: who it's for, the opening it fills that the account or the market is leaving on the table, why now, and the bet the script is making. Fold in the awareness stage, the emotion, and the sophistication read **only where they explain the choice** — as reasoning a founder would nod at, never as standalone labels. If a reader can't tell from this paragraph why this script is worth filming over any other, it isn't done. This is the part the user actually reads first, so it carries the weight.

### The Script

The full script, beat by beat, with timing. Includes:

- The hook (first 3 seconds) with the four hook elements specified — text overlay, sound, visual, vibe.
- The body, with each beat's dialogue and visual direction.
- The CTA.
- Visual cues throughout — cuts, b-roll, product reveals, on-screen text.
- Total runtime.

Every beat's visual direction sources from the brand's visual vocabulary doc at `sub-context-docs/visual-vocabulary.md` when it exists, and carries three markings, per the method at `parker-system/creative-strategy-context/visual-vocabulary-method.md`:

- **In-play, adjacent, or out-of-play.** Mark each beat's visual against the brand's vocabulary. In-play is a shot the brand already films. Adjacent is a near-neighbor the brand has not filmed but the vocabulary supports. Out-of-play is a visual invention outside the brand's current language.
- **Evidence on every adjacent and out-of-play pick.** Name where the shot was seen — the brand's own organic, a competitor, or an inspo source — so the production ask is grounded, not invented. In-play shots need no evidence; the vocabulary doc already holds them.
- **Script-congruence per beat.** The shot shows what the words claim. If the line says the texture is thick, the frame shows thick texture. A beat whose visual and dialogue diverge fails congruence.
- **Format-dependence.** The visual grammar follows the chosen ad format. The same beat shoots differently across formats — a UGC selfie beat and a polished studio beat are different shooting calls for the same words. Direct the visual to the format actually chosen.

### What it's built from

Short and only what informs — three plain lines, not a form:
- **The reference adapted** — the ad you rebuilt from, its source, and one line on why it over the others (for a net-new script, say so and why no reference fit).
- **The customer language** — the verbatims you voiced. A line pulled from a real source carries its attribution (reviewer/date or source). A line written to *sound* like a real review, comment, or thread but not pulled from a verified source is fine — just label it in one plain line: "illustrative — written to sound like real customer voice, not a verified quote; check before running any as a real testimonial." Don't hunt down the exact source of a review-flavored line; sounding real and being labeled is enough. (Facts are different — numbers, sizes, specs, and claims must be real; those don't get the illustrative pass.)
- **New shots to film** — only the adjacent and out-of-play beats that ask the brand to shoot something it hasn't, each with the evidence for where it was seen. The in-play beats need no mention; skip them.

Compliance flags, if any, go here in one line. Don't restate the brand context you used — the "Why this script" section already carried the reasoning.

### Grounding Review

The grounding gate's returned verdict, verbatim from the `context-grounding-review` agent — you do not write this, the agent does. Its verdict, one or two lines on what it checked, and if it bounced, what was re-pulled and regenerated. No block here means the gate never ran, which means the script is not done.

### Voice Review

The voice gate's returned verdict, verbatim from the `creative-voice-review` agent. Its verdict, the lint density before and after, what was flagged and fixed, and any flag kept with its reason. No block here means the gate never ran.

## Output contract precedence

The output structure above governs every path in this skill. `parker-system/creative-strategy-context/adapting-scripts.md` carries its own four-part output format; that format governs only the reference-adaptation path where a source script is being traced 1:1. On the idea paths and net-new frameworks, load adapting-scripts.md for its craft, but deliver in this skill's output structure.

## Two gates before any script gets written

**The idea gate.** Nobody just writes a script. A script request starts with the read: the brand's committed strategy and idea bank first, then what is working in the account right now, what competitors are running, what the customer keeps saying. The idea comes out of that read, and the first thing the output says, in plain language, is why this script and why now — naming the idea-bank entry it executes when there is one. If the reasoning cannot be stated in two sentences a brand founder would follow, the idea is not ready.

**The format gate.** The format is a decision, not a default. Before choosing, pull the account's current format performance: which formats carry spend, which are winning right now, which the brand has proven it can produce. The chosen format carries its reasoning from that evidence. Choosing a format because it is the easiest one to write is banned. Choosing it because the account's current winners prove the lane, and the script's talent and tone fit it, is a decision, and the output states that reasoning in plain terms.

## Hard rules

- **Adaptation by default.** Scripts are adaptations by default because AI cannot write good net-new — left to invent cold, it produces clean, written-sounding, AI-tell-ridden copy that dies when read aloud. Reference-driven adaptation is the path; net-new is the rare fallback.
- **Voice audit before output.** Every script passes the spoken-script-voice.md AI-tells check and the read-aloud test before it ships. No em-dash cadence, no smooth triplets, no "it's not just X it's Y," no signposted transitions, no over-clean grammar, no abstractions where a body part or named thing belongs. Read it out loud — if it sounds like an ad, it has a tell; cut it to plain speech.
- **The gates run automatically, before you present — never offered.** Both review agents run every time, on their own, before the script reaches the user. You never ask "want me to run the review," never call it a "second opinion," never present a script and hold the review for later. Asking is itself the failure. Running `scripts/voice-lint.py` yourself and reading it over is not the gate — that is the writer grading the writer; the gate is the independent agent, which runs the linter inside its own context and returns a verdict you cannot write for it.
- **No script ships bounced.** The independent `context-grounding-review` agent verifies the script was built from the right method docs, brand context, and data pulls — verbatims trace, cited sources exist, the loaded docs' vocabulary shows in the work. A bounce means re-pull and regenerate; its returned verdict appears in the Grounding Review block. Claimed sources are not proof — evidence is.
- **No script ships without a clean `creative-voice-review` pass.** The independent agent runs the mechanical lint and the judgment pass against `ai-writing-tells.md`; its returned verdict appears in the Voice Review block. Self-review does not substitute — the reviewer must not be the writer.
- **Check facts, not flavor.** The grounding gate verifies facts — numbers, sizes, specs, prices, named results, product and health claims must be real and trace. It does not hunt the exact source of every customer-voice line; a review-, comment-, or thread-sounding line that reads authentic and fits the brand's register is fine unpulled, labeled illustrative in one line so no one runs a made-up quote as a real testimonial. A script does not bounce for an untraceable voice line; it bounces for a wrong fact.
- **Lead with the why, not a label list.** The output opens with "Why this script" in plain sentences — the justification a founder reads first. The awareness stage, emotion, and sophistication live inside that reasoning only where they explain the call, never as a standalone checklist at the bottom. A form-shaped brief of labels is banned; it reads like paperwork and tells the reader nothing.
- **Brand voice profile loaded.** Always. Build or load the brand script-voice profile. The brand's own winning scripts are the voice fingerprint Parker matches to — pacing, diction, signature moves, CTA shape, and the banned-by-absence list.
- **Cold-audience first.** Assume no one knows or cares about the brand. Cold-focused scripts work for both cold and warm; warm-focused never scale.
- **Customer language only — voiced, not pasted.** Source from real reviews, comments, surveys. No dictionary words. Written sources arrive in written register: keep the customer's exact vocabulary but re-cadence the line for the mouth with in-register disfluencies, per the written-vs-spoken rule in `spoken-script-voice.md` — nobody says their own review. The exact written verbatim lands in the output's "What it's built from" customer-language line with its attribution so provenance holds; the script line is its voiced adaptation. Read it out loud — would the audience actually say this?
- **Clarity over cleverness.** Fifth-grade reading level. Short sentences. Remove filler.
- **Emotion first, logic second.** Persuasion is emotional. Logic justifies.
- **Hook is the gate.** 80% of energy on the first 3 seconds.
- **Hook docs are loaded before the hook is written.** The hooks skill strategy, shared hook doctrine, and brand hook history are required script context. A script that skips them will sound plausible but miss the actual creative strategy.
- **Pacing variety.** Mix two-word fragments with long run-ons. The jumping is the rhythm. Test by reading aloud — even-spaced breaths mean the variety is too flat.
- **Keep the mess. This is the default writing voice for every script.** Every script ships with placed, in-register disfluencies: the natural "so," "okay," "honestly," "I mean," "you know," a repeated word, a small false start, each one voiced where the thought genuinely turns and never sprinkled as decoration. Pull the fillers from how the brand actually sounds (the brand voice profile and the brand's own transcripts), not generic "um, like." A too-clean script that a person could deliver perfectly on the first take is a fail, the same class of miss as an em-dash or a fake question. The one exception: a brand whose voice profile or explicit instruction calls for a clean, polished read. When you take that exception, say so in one line.
- **Match awareness stage and sophistication.** Different audiences need different lead approaches and proof depths.
- **Visual cues throughout.** Every beat has visual direction — what is shown, what cut happens, what product moment lands.
- **Source visuals from the brand's vocabulary.** When `sub-context-docs/visual-vocabulary.md` exists, every beat's visual direction sources from it. Mark each beat in-play, adjacent, or out-of-play per the method at `parker-system/creative-strategy-context/visual-vocabulary-method.md`. Adjacent and out-of-play picks carry their evidence — where the shot was seen, organic or competitor or inspo — so the production ask is grounded.
- **Script-congruence.** The shot shows what the words claim. A beat whose visual contradicts its dialogue fails. If the line names a thing, the frame shows that thing.
- **Format-dependence.** The visual grammar follows the chosen ad format. The same beat shoots differently across formats. Direct each beat's visual to the format actually being made, not a generic shot.
- **No fabricated stats or claims.** Every factual element traces to verified sources.
- **Compliance is a wall.** Forbidden terms are forbidden even when characters say them.
- **One CTA per script.** Multiple CTAs split attention.
- **Brand voice consistency.** If the brand would never say something a certain way, the script does not either. The brand script-voice profile tells you what the brand sounds like — including the banned-by-absence words it never uses, which are as much the voice as the words it does.
- **Plain speech to the user.** The script brief and rationale are written the way a strategist talks in a meeting: the ad, the number, the quote, the competitor move. No internal system vocabulary reaches the user.
- **Formats are named by the account's AI tag taxonomy, exactly as tagged.** The tags are shared vocabulary the user sees in their own dashboard. Inventing blended format names is banned.
- **The opener is justified against the hook taxonomy in hooks.md by name.** Any opener that delays voice, motion, or sound needs explicit support from that doctrine, and paid social almost never gives it.
