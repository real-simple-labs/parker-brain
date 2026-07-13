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

Headlines run on the canonical methods. Before writing, load what `parker-system/creative-strategy-context/expertise-routing.md` names for headline generation: `lifestyle-headline-generator.md` or `problem-solution-headline-writer.md` by the brand's positioning; `spoken-script-voice.md`, whose AI-tells list applies to headlines too; `ai-writing-tells.md`, the written-slop signs that are the primary check for headline copy; and `visual-vocabulary-method.md` where the headline sits on a static. The running corpus and customer language pull through the Parker tools inventoried in `parker-system/system/parker-tools.md`.

`lifestyle-headline-generator.md` and `problem-solution-headline-writer.md` are the source of truth for the structural patterns, their named structures, and the proven-example library. The structural-pattern process files under `processes/` carry the execution playbook for each pattern — when to pick it, how to run it, what never to do — and point back to the canonical doc for the structures and examples rather than re-listing them. When the canonical library changes, the patterns inherit it. The AI-tells the candidates are read against are the canonical list in `spoken-script-voice.md`, not a copy held here.

## How this skill runs

1. **Load brand context — strategy first.** The brand's committed strategy (`strategy/` — the working thesis, the roadmap's messaging and persona calls) is the frame the headlines execute inside; read it before writing, and check the idea bank (`idea-bank/`, including evaluated ideas) for an entry this request should execute from. Then brand voice, ICP, voice of customer, compliance, customer language pulled from reviews. A request that cuts against the committed strategy is surfaced with the conflict named, not silently executed; a brain without `strategy/` or an idea bank yet gets one line saying so.

2. **Build the headline baseline first.** Before writing anything, pull the brand's RUNNING headline corpus — the ad_title, headline, and text_hook fields from the account's top spenders and top performers. What already wins in this account is the baseline. Adaptation of a proven structure beats invention. Run `processes/build-headline-baseline.md` to group the running headlines into families and read performance against them. Then pull the rival headlines captured in the vault — the claim a competitor cannot make is an angle. This study step is mandatory. Generated headlines that were never measured against what actually runs sound AI-written.

3. **Run the voice audit.** From the baseline, extract the brand's headline fingerprint: length distribution, casing and punctuation habits, how it uses numbers and specifics, which registers it runs. Then name the AI-tells to avoid — the patterns that show up in generated headlines and never in the winning corpus. Read every candidate out loud against the corpus. If it sounds like marketing and the corpus sounds like a person, the candidate is wrong.

4. **Determine brand type.** Lifestyle or problem/solution. This decision shapes everything that follows — different patterns, different emotional engines, different goals.

5. **Run strategy.md to pick the approach.** Strategy routes first to the adaptation paths — adapt a winning headline, lift a review verbatim, answer a comment, counter a competitor, build on a stat receipt — and then to the structural pattern library when a fresh structure is needed.

6. **Load and execute the picked process file(s).** Each process is a distinct method with its own playbook.

7. **Source customer language from real data.** Every headline pulls from reviews, comments, surveys, the running corpus. Never invented marketing voice.

8. **Ground the visual where the headline sits on a static.** When the headline lands on a static or a video frame and the recommendation suggests what runs alongside it, work through `visual-vocabulary-method.md` and the brand's `sub-context-docs/visual-vocabulary.md`. Source the paired visual from the brand's in-play shots; mark any adjacent or out-of-play visual invention as a flag, not a grounded direction. A headline that only works over an invented stock visual is not grounded.

9. **Run the headline quality checklist** before output.

10. **You run the two review gates yourself, now, before you present anything — this is a step you execute, not a thing that happens for you.** Read "automatically" as *without being asked*, never as *without you doing it*: nothing else spawns these agents, so if you don't spawn them they never run. They are not optional, not a "second opinion," and never offered to the user as a choice — asking "want me to review this" is itself the failure. Running `scripts/voice-lint.py` yourself is not the gate; the gate is the independent agent, and its returned verdict fills the receipt block below, which you cannot write yourself. Grounding gate first (it changes content), voice gate second (it changes lines). Spawn the `context-grounding-review` agent (defined at `.claude/agents/context-grounding-review.md`) with the user's task, the candidate set, the brain root, and the list of tool pulls made this session. It runs `scripts/grounding-check.py` and independently derives what should have been loaded and pulled — the running-corpus pull behind the baseline is the one it will always check — then diffs that against the evidence. A `bounced` verdict means re-pull and regenerate the affected candidates. This gate runs before the voice gate because its verdict changes content, not lines. And every bounce gets captured through `self-improvement-intake` as a one-line reasoning trace — the task shape plus the loads or pulls that were missed — so the routing layer learns from the catch instead of re-making the same mistake for the gate to re-catch.

11. **Run the voice review gate.** Spawn the `creative-voice-review` agent (defined at `.claude/agents/creative-voice-review.md`) on the finished candidate set, handing it the headlines, the headline fingerprint from the baseline, and the deliverable type. The agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass per `ai-writing-tells.md` — independently, in a context that did not write the candidates. Apply its rewrites and re-run until the verdict is `ships`. A flag that conflicts with a review verbatim or the running corpus keeps the source, with the reason carried into the Voice Review block.

12. **Format output per the structure below.**

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

### Grounding Review

The grounding gate's receipt, required on every set: the `context-grounding-review` verdict, one or two plain sentences on what it checked (the corpus pull behind the baseline, verbatims traced, sources resolved), and — if it bounced — what was re-pulled and regenerated before re-shipping. A set missing this block did not pass the gate.

### Voice Review

The gate's receipt, required on every set: the `creative-voice-review` verdict, the lint density before and after, one or two plain sentences on what was flagged and fixed, and any flag kept with its reason — a review verbatim, or a pattern the running corpus genuinely uses. A set missing this block did not pass the gate.

## Hard rules

- **Study the running corpus first.** Never write a headline before pulling what the account already runs. The winning headlines are the baseline. Adapting a proven structure to a new angle beats inventing a structure that has never been measured here.
- **Read every candidate against the corpus, out loud.** If the corpus sounds like a person talking and the candidate sounds like a brand talking, the candidate loses. The corpus is the bar, not a generic notion of good copy.
- **No AI-tells.** Read every candidate against the canonical AI-tells list in `spoken-script-voice.md` — it applies to headlines, not just scripts. The winning corpus is blunt, short, and specific; whatever the corpus never does is forbidden too. The tells that surface most in generated headlines are the colon-summary cadence where an abstract noun is restated, the "Discover/Unlock/Elevate/Transform" verb openers when the brand never uses them, balanced rule-of-three triads invented for rhythm, hedge phrases like "say goodbye to" or "the secret to," dictionary words where the brand uses slang, and the marketing abstraction standing in for the named thing. Match the brand's actual register, not a polished version of it.
- **No headline set ships bounced.** The independent `context-grounding-review` agent verifies the set was built from the right method docs, the real running corpus, and traced customer language — a headline whose source traces to nothing is fabrication, not a candidate. A bounce means re-pull and regenerate; its verdict appears in the Grounding Review block.
- **Check facts, not flavor.** The grounding gate verifies facts — numbers, sizes, specs, prices, claims must be real and trace. It does not hunt the exact source of every customer-voice line; a review-, comment-, or thread-sounding line that reads authentic and fits the brand register is fine unpulled, labeled illustrative in one line so no made-up quote runs as a real testimonial. Bounce for a wrong fact, never for an untraceable voice line.
- **You spawn both gates yourself before you present — never offered, never delegated.** You run both review agents on every set, as your own step, before it reaches the user; nothing runs them for you, so a set presented without them is unfinished, not merely unreviewed. "Runs every time" means *you* run it every time. Never ask "want me to review this," never call it a "second opinion," never present and hold the review for later. Running the linter yourself is not the gate — the gate is the independent agent, whose returned verdict fills the receipt blocks you cannot write yourself.
- **No headline set ships without a clean `creative-voice-review` pass.** The independent agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass against `ai-writing-tells.md`; its verdict and the before/after lint density appear in the Voice Review block. Self-review does not substitute — the reviewer must not be the writer.
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
