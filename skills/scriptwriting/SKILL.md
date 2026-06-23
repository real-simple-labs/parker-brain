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

Scriptwriting runs on the canonical methods, routed by `global/knowledge/creative-strategy/expertise-routing.md`: `spoken-script-voice.md`, the human-voice doctrine and AI-tells audit, mandatory before writing any words; `scriptwriting.md` and `adapting-scripts.md` for the craft and the 1:1 adaptation method; `visual-vocabulary-method.md` for per-beat visual direction; and `hooks.md` for the opener. Reference ads and customer language pull through the Parker tools inventoried in `system/parker-tools.md`.

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

3. **For reference-driven adaptation:** find-reference-ads → adapt-existing-script. find-reference-ads pulls in source order — brand's own account, then captured vault competitor/inspo, then niche organic, then global DB.

4. **For net-new:** pick the right framework process — problem/solution, story-arc, VSL, awareness-staged, style-based, sophistication-matched, emotional-depth.

5. **Source customer language.** Every script — adapted or net-new — pulls language from real reviews, comments, surveys, voice of customer data. Marketing voice fails.

6. **Run the script quality audit** before output, including the spoken-script-voice check — every script passes the AI-tells check in `creative-strategy-context/spoken-script-voice.md` and the read-aloud test.

7. **Format output per the structure below.**

## Output structure

### The Script

The full script, beat by beat, with timing. Includes:

- The hook (first 3 seconds) with the four hook elements specified — text overlay, sound, visual, vibe.
- The body, with each beat's dialogue and visual direction.
- The CTA.
- Visual cues throughout — cuts, b-roll, product reveals, on-screen text.
- Total runtime.

Every beat's visual direction sources from the brand's visual vocabulary doc at `sub-context-docs/visual-vocabulary.md` when it exists, and carries three markings, per the method at `global/knowledge/creative-strategy/visual-vocabulary-method.md`:

- **In-play, adjacent, or out-of-play.** Mark each beat's visual against the brand's vocabulary. In-play is a shot the brand already films. Adjacent is a near-neighbor the brand has not filmed but the vocabulary supports. Out-of-play is a visual invention outside the brand's current language.
- **Evidence on every adjacent and out-of-play pick.** Name where the shot was seen — the brand's own organic, a competitor, or an inspo source — so the production ask is grounded, not invented. In-play shots need no evidence; the vocabulary doc already holds them.
- **Script-congruence per beat.** The shot shows what the words claim. If the line says the texture is thick, the frame shows thick texture. A beat whose visual and dialogue diverge fails congruence.
- **Format-dependence.** The visual grammar follows the chosen ad format. The same beat shoots differently across formats — a UGC selfie beat and a polished studio beat are different shooting calls for the same words. Direct the visual to the format actually chosen.

### Script Brief

- The framework or approach used.
- For reference-adapted scripts: the chosen reference ad with its source and the rationale for picking it over the other candidates.
- The awareness stage and sophistication level the script targets.
- The dominant emotion the script activates.
- The ICP and persona being addressed.
- Key VoC phrases that anchor the customer language.
- The brand's structural signature reflected — pacing, hook pattern, CTA style pulled from the brand baseline.
- **Visual Sourcing.** Which visual vocabulary entries the script's beats drew from, and what is new production — the adjacent and out-of-play beats that ask the brand to film something it has not filmed before, each with its evidence.

### Brand Context Applied

- **What I used:** brand baseline, ICP, persona, voice of customer, brand voice, compliance, reference ads if applicable.
- **What I avoided:** compliance walls, forbidden terms, marketing voice.
- **Why this fits:** two-to-four sentences on the brand's current creative moment.

## Output contract precedence

The output structure above governs every path in this skill. `creative-strategy-context/adapting-scripts.md` carries its own four-part output format; that format governs only the reference-adaptation path where a source script is being traced 1:1. On the idea paths and net-new frameworks, load adapting-scripts.md for its craft, but deliver in this skill's output structure.

## Two gates before any script gets written

**The idea gate.** Nobody just writes a script. A script request starts with the read: what is working in the account right now, what competitors are running, what the customer keeps saying. The idea comes out of that read, and the first thing the output says, in plain language, is why this script and why now. If the reasoning cannot be stated in two sentences a brand founder would follow, the idea is not ready.

**The format gate.** The format is a decision, not a default. Before choosing, pull the account's current format performance: which formats carry spend, which are winning right now, which the brand has proven it can produce. The chosen format carries its reasoning from that evidence. Choosing a format because it is the easiest one to write is banned. Choosing it because the account's current winners prove the lane, and the script's talent and tone fit it, is a decision, and the output states that reasoning in plain terms.

## Hard rules

- **Adaptation by default.** Scripts are adaptations by default because AI cannot write good net-new — left to invent cold, it produces clean, written-sounding, AI-tell-ridden copy that dies when read aloud. Reference-driven adaptation is the path; net-new is the rare fallback.
- **Voice audit before output.** Every script passes the spoken-script-voice.md AI-tells check and the read-aloud test before it ships. No em-dash cadence, no smooth triplets, no "it's not just X it's Y," no signposted transitions, no over-clean grammar, no abstractions where a body part or named thing belongs. Read it out loud — if it sounds like an ad, it has a tell; cut it to plain speech.
- **Brand voice profile loaded.** Always. Build or load the brand script-voice profile. The brand's own winning scripts are the voice fingerprint Parker matches to — pacing, diction, signature moves, CTA shape, and the banned-by-absence list.
- **Cold-audience first.** Assume no one knows or cares about the brand. Cold-focused scripts work for both cold and warm; warm-focused never scale.
- **Customer language only.** Source from real reviews, comments, surveys. No dictionary words. Read it out loud — would the audience actually say this?
- **Clarity over cleverness.** Fifth-grade reading level. Short sentences. Remove filler.
- **Emotion first, logic second.** Persuasion is emotional. Logic justifies.
- **Hook is the gate.** 80% of energy on the first 3 seconds.
- **Hook docs are loaded before the hook is written.** The hooks skill strategy, shared hook doctrine, and brand hook history are required script context. A script that skips them will sound plausible but miss the actual creative strategy.
- **Pacing variety.** Mix two-word fragments with long run-ons. The jumping is the rhythm. Test by reading aloud — even-spaced breaths mean the variety is too flat.
- **Keep the mess. This is the default writing voice for every script.** Every script ships with placed, in-register disfluencies: the natural "so," "okay," "honestly," "I mean," "you know," a repeated word, a small false start, each one voiced where the thought genuinely turns and never sprinkled as decoration. Pull the fillers from how the brand actually sounds (the brand voice profile and the brand's own transcripts), not generic "um, like." A too-clean script that a person could deliver perfectly on the first take is a fail, the same class of miss as an em-dash or a fake question. The one exception: a brand whose voice profile or explicit instruction calls for a clean, polished read. When you take that exception, say so in one line.
- **Match awareness stage and sophistication.** Different audiences need different lead approaches and proof depths.
- **Visual cues throughout.** Every beat has visual direction — what is shown, what cut happens, what product moment lands.
- **Source visuals from the brand's vocabulary.** When `sub-context-docs/visual-vocabulary.md` exists, every beat's visual direction sources from it. Mark each beat in-play, adjacent, or out-of-play per the method at `global/knowledge/creative-strategy/visual-vocabulary-method.md`. Adjacent and out-of-play picks carry their evidence — where the shot was seen, organic or competitor or inspo — so the production ask is grounded.
- **Script-congruence.** The shot shows what the words claim. A beat whose visual contradicts its dialogue fails. If the line names a thing, the frame shows that thing.
- **Format-dependence.** The visual grammar follows the chosen ad format. The same beat shoots differently across formats. Direct each beat's visual to the format actually being made, not a generic shot.
- **No fabricated stats or claims.** Every factual element traces to verified sources.
- **Compliance is a wall.** Forbidden terms are forbidden even when characters say them.
- **One CTA per script.** Multiple CTAs split attention.
- **Brand voice consistency.** If the brand would never say something a certain way, the script does not either. The brand script-voice profile tells you what the brand sounds like — including the banned-by-absence words it never uses, which are as much the voice as the words it does.
- **Plain speech to the user.** The script brief and rationale are written the way a strategist talks in a meeting: the ad, the number, the quote, the competitor move. No internal system vocabulary reaches the user.
- **Formats are named by the account's AI tag taxonomy, exactly as tagged.** The tags are shared vocabulary the user sees in their own dashboard. Inventing blended format names is banned.
- **The opener is justified against the hook taxonomy in hooks.md by name.** Any opener that delays voice, motion, or sound needs explicit support from that doctrine, and paid social almost never gives it.
