# Scriptwriting — Strategy

This document picks which scriptwriting process to run. The default path is reference-driven adaptation. Net-new from scratch is the fallback when references do not exist or the user explicitly asks for fresh-from-scratch.

## What to load before deciding

- **Brand script-voice profile.** Build or load it via build-brand-voice-profile. Pull the brand's own winning scripts, read them out loud, and extract the voice fingerprint — pacing, diction with exact recurring phrases, signature moves, direct-address habit, CTA shape, and the banned-by-absence list. This is the voice and structural fingerprint everything generated must match and sound like.
- **Brand visual vocabulary.** Load `sub-context-docs/visual-vocabulary.md` alongside the voice profile when it exists. Voice is what the brand sounds like; the vocabulary is what it looks like — the brand's filmed settings, talent situations, and product moves, classified in-play, adjacent, and out-of-play per the method at `global/knowledge/creative-strategy/visual-vocabulary-method.md`. Every beat's visual direction sources from it.
- **Brand profile, ICP, personas, voice of customer.**
- **Brand voice rules and compliance constraints.**
- **Hook strategy and hook history.** Load the hooks skill strategy, the shared hook doctrine, and the brand's latest hook audit or hook history before writing the first three seconds. The opener is where the script earns the watch, so it must be chosen from ICP, emotion, brand history, and actual first-three-second evidence.
- **The account's current format performance.** Which formats carry spend and which are winning right now. The format choice is made from this evidence and stated with its reasoning. Defaulting to any format without examining the account's evidence is the named failure.
- **The intended format** — UGC, VSL, organic-feel, polished, vertical short, longer-form.
- **The intended placement** — Meta paid, TikTok organic, YouTube, landing page video.
- **Any source material the user provided** — a competitor script to adapt, a reference style, a desired framework.

## First decision: reference-driven adaptation or net-new

This is the routing decision. Default to reference-driven adaptation.

### Default: reference-driven adaptation

Adaptation is the default because AI cannot write good net-new scripts cold. The path:

1. **build-brand-voice-profile** — build or load the brand's voice fingerprint first, from the brand's own winning scripts read out loud.
2. **find-reference-ads** — pull a handful of reference ads in source order: the brand's own account scripts first, then captured vault competitor/inspo scripts, then the niche organic library, then the global AI-tagged DB. Filter by the tags that match the request — format, angle, awareness stage, persona, hook type, brand type.
3. **adapt-existing-script** — adapt the chosen reference for the brand. Preserve the structural skeleton; rewrite every word in the brand's voice fingerprint.

Apply this default unless one of the net-new triggers fires.

### Net-new triggers

Route to a net-new process only when:

- The user explicitly asks for a script "from scratch" or says they do not want references used.
- find-reference-ads returns no genuinely relevant references for the request.
- The user is testing a deliberately untested angle that has no precedent in the database — and is explicit that they want net-new for that reason.
- The format is so unusual that no references in the database match (rare).

## Second decision (only when going net-new): which net-new approach

If the net-new path is the right call, pick the framework based on the audience and brand type.

### By user signal

| User signal | Process |
|---|---|
| "I need a VSL" or "long-form video" | write-vsl |
| "Cold audience, they don't know the problem yet" | write-awareness-stage-script (unaware focus) |
| "Our market is saturated, they're jaded" | write-awareness-stage-script (most-aware focus) |
| "Write in [humorous / testimonial / demonstration / FUD / educational] style" | write-style-based-script |
| "I need emotional depth on [identity / belonging / freedom]" | write-emotional-depth-script |
| "Write a 60-second organic-feeling script, not DR formula" | write-storytelling-script |
| "Quick problem-solution hook + CTA" | write-problem-solution-script |
| "Our market is low-sophistication (first hearing of problem)" | write-sophistication-matched-script (low) |
| "High-sophistication market (tired of failed solutions)" | write-sophistication-matched-script (high) |

### By default if user did not signal and reference path failed

- **Problem/solution brand, problem-aware or solution-aware audience** → write-problem-solution-script.
- **Lifestyle brand, identity-led purchase** → write-storytelling-script with a lifestyle framing.
- **Unaware or low-sophistication audience** → write-awareness-stage-script.
- **Long-form ad** → write-vsl.

## Cross-cutting principles that apply to every script

Non-negotiable across every process — reference-driven or net-new.

### Brand voice-fingerprint match
Every script must read and sound as belonging to this brand. The brand script-voice profile — built from the brand's own winning scripts read out loud — defines what that means. Pacing, diction, signature moves, direct-address habit, CTA shape, and the banned-by-absence words. If the generated script does not match the brand's voice fingerprint, it does not ship.

### Spoken, not written
Every script must survive being read out loud by a real person. Write for the mouth, not the page. Apply the spoken-register rules in `creative-strategy-context/spoken-script-voice.md`: short sentences with the length jumping around, contractions and elisions, fragments as emphasis, the mess left in, concrete named things over abstractions, transitions by moving not signposting, and a friend's-recommendation CTA. The AI-tells list there is the contrast set — train every line against the real corpus lines, not the AI defaults.

### Cold-audience assumption
The script must work for cold audiences. Cold-focused works for warm too; warm-focused never scales.

### Customer language sourcing
Pull from real reviews, comments, surveys, organic social, voice-of-customer data. Marketing voice fails. The casual, imperfect way customers actually talk is the language the script uses.

### Emotion first, logic second
People buy feelings and justify with logic. Every script's persuasive engine is emotional. Tap primal desires (food, sex, comfort, safety, status) and learned desires (belonging, achievement, recognition).

### Clarity over cleverness
Fifth-grade reading level. Short sentences. No marketer-for-marketers copy.

### Hook is the gate
80% of creative energy on the first 3 seconds. If the hook fails, the rest does not matter.

### Problem clarity
Name the problem early and clearly. Go deep — surface symptom → behavioral impact → identity impact. Level 2 and Level 3 emotional depth outperform Level 1.

### Pacing variety
Mix two-word fragments with long run-ons. The jumping is the rhythm. Read aloud — if the breaths come at even intervals, the variety is too flat.

### Insider language and cultural fit
Match the audience's generational and cultural register.

### Visual cues
Every beat has visual direction.

### Relatability quirks
Audience-specific universal truths land hard. The brand baseline often reveals which quirks the brand has already pulled.

### Proof fidelity
Never fabricate claims. If no verified source exists, mark `[STAT NEEDED — verify before publishing]`.

### Fluff removal
Cut every sentence that does not escalate pain, deepen desire, or move toward resolution.

## Awareness stage matching

- **Unaware.** Storytelling, education, hidden-villain reveals.
- **Problem-aware.** Problem naming, education on solutions, "I tried X and Y."
- **Solution-aware.** Investment framing, myth-busting, differentiation.
- **Product-aware.** Social proof, urgency, comparison.
- **Most-aware.** Offer, scarcity, direct CTA.

## Sophistication level matching

- **High sophistication.** Acknowledge failed past attempts. Differentiate from what has not worked. Mechanism specificity.
- **Low sophistication.** Education and clarity. Simple problem naming, metaphors.

## Format-specific decisions

- **UGC short-form (15-30 seconds).** Tight pacing. Single angle. Customer-language voiceover. Visual proof.
- **Mid-form (30-60 seconds).** Hook + 2-3 proof beats + CTA. Room for one persona shift if needed.
- **VSL (90 seconds to several minutes).** Full hook + lead + mechanism + close pipeline.
- **Vertical short (TikTok/Reels-native).** Conversational opener. Native pacing.

## Common mistakes the strategy must avoid

- Skipping reference-finding and going net-new by default. AI cannot write good net-new; references produce better scripts.
- Skipping the brand script-voice profile. Without it, scripts drift to generic ad-voice instead of the brand's fingerprint.
- Skipping hook docs and writing the first three seconds from instinct. A good script with a generic opener still fails.
- Writing scripts that sound written, not spoken. Clean grammar, em-dash cadence, smooth triplets, and signposted transitions are AI tells — they die when read aloud.
- Writing in marketing voice instead of customer voice.
- Cold scripts that only work for warm audiences.
- Scripts without visual cues.
- Fabricated stats or claims.
- Forbidden terms in dialogue or copy.
- Bloated scripts.
- Multiple competing CTAs.

## Final quality audit before output

- Does the script read and sound like the brand's voice fingerprint — pacing, diction, signature moves, CTA shape?
- Does it pass the read-aloud test? Read it out loud at performance speed — any line you stumble on, or any line that sounds like an ad, gets cut to plain speech.
- Does it pass the AI-tells check in `spoken-script-voice.md`? No em-dash cadence, no smooth triplets, no "it's not just X it's Y," no signposted transitions ("but here's the thing"), no over-clean grammar, no abstractions where a body part or named thing belongs.
- Are the brand's banned-by-absence words absent?
- Is the mess kept by default: the natural "so," "okay," "honestly," "I mean," repeated words, small false starts, placed where the thought turns and in the brand's register? A too-clean script a person could deliver perfectly on the first take fails this gate, unless the brand voice profile or the brand explicitly calls for a polished read.
- For reference-adapted scripts: is the structural fidelity to the reference preserved?
- Does the hook earn the first 3 seconds with a specific ICP and emotion?
- Does the script work for cold audiences?
- Does it match the audience's awareness stage and sophistication?
- Is the customer language sourced from real data?
- Is every claim verifiable?
- Are visual cues present for every beat?
- Does every beat's visual pass script-congruence — does the shot show what the words claim?
- Does the visual grammar match the chosen ad format — is each beat shot for the format actually being made?
- Is every beat marked in-play, adjacent, or out-of-play, with evidence carried on the adjacent and out-of-play picks?
- Is there one CTA, not multiple?

## Reasoning log

Past script picks the user has accepted, rejected, or adjusted accumulate here as the loop runs. Over time this trains Parker on the brand's specific scripting taste — which reference patterns convert, which net-new frameworks land, which voice patterns the audience responds to.

*(No entries yet — populated by the fine-tuning loop.)*
