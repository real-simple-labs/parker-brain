---
name: headlines
description: Write headlines for ads — static, video text overlays, paid social, landing page hero. Picks the right structural pattern for the brand type (lifestyle vs problem/solution), the awareness stage, and the customer language available.
triggers:
  - write me headlines
  - write a headline
  - headline ideas
  - new headline variations
  - headline for this static
  - headline for this ad
  - landing page headline
  - hero headline
  - headline rewrites
  - the headline isn't working
  - bold headline for this concept
  - text overlay for this video
---

# Headlines

## Goal

Write headlines that earn attention and convert it. A headline carries the weight of the entire argument in one line — it has to land instantly for cold scrollers, sound like the brand's actual customers, and follow a structural pattern that fits the brand type.

This skill writes headlines for static ads, video text overlays, landing page heroes, and paid social. It does not write full scripts (route to scriptwriting), full statics with layouts (route to ai-ad-generation), or iterate on existing winning headlines (route to iterations).

## What you are working from

Headlines run on the canonical methods. Before writing, load what `global/knowledge/creative-strategy/expertise-routing.md` names for headline generation: `lifestyle-headline-generator.md` or `problem-solution-headline-writer.md` by the brand's positioning; `spoken-script-voice.md`, whose AI-tells list applies to headlines too; and `visual-vocabulary-method.md` where the headline sits on a static. The running corpus and customer language pull through the Parker tools inventoried in `system/parker-tools.md`.

`lifestyle-headline-generator.md` and `problem-solution-headline-writer.md` are the source of truth for the structural patterns, their named structures, and the proven-example library. The structural-pattern process files under `processes/` carry the execution playbook for each pattern — when to pick it, how to run it, what never to do — and point back to the canonical doc for the structures and examples rather than re-listing them. When the canonical library changes, the patterns inherit it. The AI-tells the candidates are read against are the canonical list in `spoken-script-voice.md`, not a copy held here.

## How this skill runs

1. **Load brand context.** Brand voice, ICP, voice of customer, compliance, customer language pulled from reviews.

2. **Build the headline baseline first.** Before writing anything, pull the brand's RUNNING headline corpus — the ad_title, headline, and text_hook fields from the account's top spenders and top performers. What already wins in this account is the baseline. Adaptation of a proven structure beats invention. Run `processes/build-headline-baseline.md` to group the running headlines into families and read performance against them. Then pull the rival headlines captured in the vault — the claim a competitor cannot make is an angle. This study step is mandatory. Generated headlines that were never measured against what actually runs sound AI-written.

3. **Run the voice audit.** From the baseline, extract the brand's headline fingerprint: length distribution, casing and punctuation habits, how it uses numbers and specifics, which registers it runs. Then name the AI-tells to avoid — the patterns that show up in generated headlines and never in the winning corpus. Read every candidate out loud against the corpus. If it sounds like marketing and the corpus sounds like a person, the candidate is wrong.

4. **Determine brand type.** Lifestyle or problem/solution. This decision shapes everything that follows — different patterns, different emotional engines, different goals.

5. **Run strategy.md to pick the approach.** Strategy routes first to the adaptation paths — adapt a winning headline, lift a review verbatim, answer a comment, counter a competitor, build on a stat receipt — and then to the structural pattern library when a fresh structure is needed.

6. **Load and execute the picked process file(s).** Each process is a distinct method with its own playbook.

7. **Source customer language from real data.** Every headline pulls from reviews, comments, surveys, the running corpus. Never invented marketing voice.

8. **Ground the visual where the headline sits on a static.** When the headline lands on a static or a video frame and the recommendation suggests what runs alongside it, work through `visual-vocabulary-method.md` and the brand's `sub-context-docs/visual-vocabulary.md`. Source the paired visual from the brand's in-play shots; mark any adjacent or out-of-play visual invention as a flag, not a grounded direction. A headline that only works over an invented stock visual is not grounded.

9. **Run the headline quality checklist** before output.

10. **Format output per the structure below.**

## Output structure

### The Headline Recommendations

2-5 headlines. Each one includes:

- A name that signals the move. Format pattern: "[Structure type] — [Specific ICP + emotion angle]."
- The headline itself, under 10 words.
- The process used — which adaptation path or structural pattern.
- The ICP and emotion the headline activates.
- The emotional depth level (Level 1 surface / Level 2 behavioral / Level 3 identity) for problem/solution brands.
- The source — the running headline it adapts, the review or comment it lifts, the competitor claim it counters, or the verified stat it carries. Name it. Every headline traces to something real in this account.
- Two-to-four-sentence rationale on the structure choice and the brand fit.

### Baseline Studied

Two-to-four sentences naming the winning headlines this set was built against — the running corpus you pulled, the family each new headline extends, and the AI-tells you avoided after the read-aloud.

### Brand Context Applied

- **What I used:** ICP, persona, customer language, voice of customer, brand voice, compliance.
- **What I avoided:** compliance walls, forbidden terms, marketing voice, testimonial-trap phrasing.
- **Why this fits:** two-to-four sentences on the brand's current creative moment.

## Hard rules

- **Study the running corpus first.** Never write a headline before pulling what the account already runs. The winning headlines are the baseline. Adapting a proven structure to a new angle beats inventing a structure that has never been measured here.
- **Read every candidate against the corpus, out loud.** If the corpus sounds like a person talking and the candidate sounds like a brand talking, the candidate loses. The corpus is the bar, not a generic notion of good copy.
- **No AI-tells.** Read every candidate against the canonical AI-tells list in `spoken-script-voice.md` — it applies to headlines, not just scripts. The winning corpus is blunt, short, and specific; whatever the corpus never does is forbidden too. The tells that surface most in generated headlines are the colon-summary cadence where an abstract noun is restated, the "Discover/Unlock/Elevate/Transform" verb openers when the brand never uses them, balanced rule-of-three triads invented for rhythm, hedge phrases like "say goodbye to" or "the secret to," dictionary words where the brand uses slang, and the marketing abstraction standing in for the named thing. Match the brand's actual register, not a polished version of it.
- **Under 10 words.** Always. If it can be shorter, make it shorter.
- **Specific ICP + specific emotion.** Every headline targets a specific person feeling a specific emotion. Generic headlines fail.
- **Customer language only.** No marketing voice, no dictionary words. Read it out loud — would the actual customer say this to a friend?
- **Cold-audience first.** Headlines must work for cold audiences. Cold-focused headlines work for both cold and warm; warm-focused headlines never scale.
- **Clear beats clever.** Simple language, no jargon. State the transformation, benefit, or identity signal directly.
- **Fifth-grade reading level or below.** No words over 3 syllables unless absolutely necessary.
- **Different structure from the current ad if iterating.** The whole point of an iteration is testing a new approach.
- **Pass the testimonial trap test.** "Best ever," "so good," "worth it," "love it," "can't believe how X" — these are reviews, not headlines.
- **No fabricated stats or claims.** Every factual element traces to verified sources. If no verified source exists, mark `[STAT NEEDED — verify before publishing]`.
- **Compliance is a wall.** Forbidden terms are forbidden in headlines, even when the user asks. Push back, explain, offer a compliant alternative.
- **Match brand voice.** If the brand would never use a curse word, do not force one. If the brand is playful, do not write austere headlines.
