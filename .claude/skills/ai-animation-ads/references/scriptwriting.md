# Scriptwriting — AI Animation Ads

The script is the highest-leverage stage of the whole pipeline. The scaffolding (formats, styles, prompts) gets any ad to "good"; the script and visual direction are what separate a great AI ad from the okay ones flooding the feed. Spend the iteration budget here — regenerating a script costs nothing; regenerating 15 video clips costs real credits.

## Stage 0 — Research brief (before any writing)

Never script from memory. Build a 1–2 page brief, in this priority order of sources:
1. **Brand vault** — if this brand has a brain/vault, pull the existing research: creative strategy context, personas, competitor docs, claims guardrails. Don't re-research what the vault already holds.
2. **Parker MCP** — customer reviews (`search_customer_reviews_semantic`), post-purchase surveys, winning ad angles from the account, competitor animation ads (`search_competitor_facebook_ads` with keywords like "Pixar/claymation/animated character") for swipe context.
3. **Web** — product page, Amazon/Trustpilot/Reddit, for brands with no vault.

**The brief must contain (keep each section tight):**
1. **The product** — what it is/does in 2–3 sentences; what it physically looks like (packaging, color, shape, labeling — specific enough for an image model to recreate); ingredients/tech that could be VISUALIZED (probiotics populating a gut, caffeine firing neurons).
2. **Castable characters** — objects that could talk: the product, ingredients, body parts, competing products, tools the customer uses now. A personality for each ("the magnesium capsule — calm, zen, the peacekeeper"; "the gut lining — overworked, begging for help"). 3–5 natural settings.
3. **The customer** — one specific person, not a demographic; the ONE core pain in the customer's own words; the trigger event that leads to purchase.
4. **The language** — 5–10 vivid review quotes (flag any that work as first-person product lines: "it gave me my mornings back" → "I gave her her mornings back"); 5–8 pain words (humiliated, defeated, exhausted); 5–8 desire words (alive, unstoppable, myself again).
5. **The proof** — 2–3 strongest proof points (review count, rating, clinical study, guarantee); one killer social-proof one-liner from a real review.
6. **Visualisable moments** — 8–12 standalone scene ideas mixing problem/mechanism/payoff ("a tired cracked battery inside her chest flickering," "ingredient workers rappelling down hair follicles with repair tools").
7. **What NOT to say** — claims the brand cannot make; off-brand tones. (See Compliance below.)

## Stage 1 — Angle + awareness (one recommendation, not a menu)

**Angle** = the customer-focused reason to buy — an outcome or transformation, never a feature or brand brag. Formats that work: "Stops [pain]" · "[Desired state] without [objection]" · "[Product] does what [alternative] can't." **Awareness stage** (pick one): unaware / problem-aware / solution-aware / product-aware / most-aware — it sets how much education the script carries and where the product enters. Present as: `RECOMMENDED ANGLE: "…" / AWARENESS: [stage] — [one line why]`, with one line of reasoning so the user learns the logic. Offer alternates only if asked.

## Stage 2 — The script

### The five-part frame (all spoken formats)
**Hook → Agitation → The Turn (solution) → Proof → CTA.** ~110–160 words for 60s of VO; one idea per beat; each beat is one concrete visual moment. Deliver as two columns — VO text left, visual scene direction right — plus a numbered **VO line list** (one sentence per line; each line becomes one clip and one audio take).

### Hook rules
- **Declarative statements, not questions** — with two deliberate exceptions: (1) the skeleton progression format runs on curiosity-gap QUESTIONS ("What happens if you take creatine every day for a year?"); (2) the READER-IMPLICATING question when the brand's evidence validates it (an owner-graded exemplar or a tracked field winner running on the mechanic) — a question that makes the viewer audit THEMSELVES is a pattern interrupt, not a curiosity gap, and owner-graded evidence outranks this default. Everything else: state the hidden truth. "This is why your weight doesn't reflect your health." "You don't have dry scalp. You have fungus on your face."
- Specific numbers beat adjectives ("98% DEXA accuracy," "3 million units," "$1.50 a day").
- Write **5 hook variations** at the top of every script draft; the hook is also the text overlay + thumbnail frame, so it must work visually.
- The verbal hook, visual hook, and text hook land together in seconds 0–3 (Parker's ad library tracks all three separately — design all three deliberately).

### Voice structure by format (who speaks — this drives all downstream prompting)
- **Talking-character cast:** multiple speakers; label every line with its character. Lip-sync YES (3D style only).
- **Narrator-led / character-follow:** one narrator; characters silent. Lip-sync NO.
- **Claymation (all variants):** VO or song only; mouths NEVER move.
- **Sung VO:** the script IS the lyrics — verses/chorus/bridge structure; write the song before storyboarding (see audio.md).
- **Multi-narrator:** mark which voice carries which section; handoff = tonal shift at a visual transition.

### Beat-writing craft
- **Second person, present tense** for progression/journey formats: "You wake up. Day one. Your inbox is a war zone."
- **Translate every abstract benefit into a physical image** — this is the core craft:

| Abstract claim | Visceral beat |
|---|---|
| Saves time | "You blink and the work's already done. You stare at an empty to-do list, twitching." |
| Reduces churn | "Customers used to vanish like smoke. Now they're chained to you, grinning." |
| More energy | "The battery in her chest stops flickering. It burns steady, all afternoon." |
| Cuts costs | "Your burn rate was a bonfire. Now it's a birthday candle." |
| Better absorption | "The cheap pill sails through untouched. This one docks like it has a key." |

- **Escalate** — each beat bigger/worse/better than the last; raise stakes, not just the clock.
- **Open loops and keep them open.** The hook plants a question; beats tease ("…but that's nothing compared to Day 30."); the payoff snaps it shut. Never answer early.
- **Earn the product — the turn is one clean beat.** Build pain fully first, then hinge: "That's why you need me." / "Then you find [product]." The product must feel like the answer to the loop, not an ad break.
- **The villain speaks with zero remorse.** In confession formats, failed solutions are smug or sheepishly matter-of-fact ("I also only last about 20 minutes. My bad."), never apologetic marketing-speak. Villains taunt; heroes stay calm.
- **Simplicity test:** if a 5-year-old can't follow the VO, rewrite it.
- **Banned words:** revolutionary, seamless, leverage, solution (as a noun of praise), game-changer, cinematic, stunning, breathtaking, "professional voiceover," and any generic hype. Say what physically happens.
- **VO lines are plain human speech.** No em-dashes, no semicolons, no parentheticals or stage directions inside the spoken text. Short sentences. Ellipses only as deliberate TTS pause marks, added at the audio stage. If a line reads like written ad copy instead of something a person would say out loud, rewrite it.
- **CTA rides momentum** — end on the transformation, then a soft confident close tied to the offer (guarantee, trial, "Look up [product]"). Never a hard "buy now."

### Format-specific frameworks
- **Villain confession:** cast list first (villain + symptoms + hero), then beats: confession hook → symptom escalation (one character per beat) → turn → mechanism in hero's voice → proof → knowing final line.
- **Skeleton progression:** hit the four mechanics (curiosity hook, escalating spine, visceral specifics, payoff) + the creative layer (loops, turn) — full doctrine in formats.md §4. 5–7 beats.
- **Song lyrics:** hook in first 5s; 4–8 syllables/line; genre-authentic vocabulary; angle not brand-chant; mechanism in a verse; structure by duration (see audio.md for the Suno brief format).

## Compliance gate (runs on every script before production)

- **No medical/cure claims** for supplements/wellness; no condition-specific promises; realistic timelines stated where results are implied. For supplements, keep "not intended to diagnose, treat, cure, or prevent" available for the ad copy layer.
- **No personal-attribute callouts** — "Do you suffer from [condition]?" is a Meta policy violation; reframe third-person/aspirational.
- **No weight-loss before/after side-by-sides** (2026 enforcement extends to *implied* transformations); non-body outcomes (energy, focus) are the safe lane.
- **Defer to the brand vault's claims doc** where one exists — it wins over anything generated here.
- **IP:** no franchise characters/looks in scripts or prompts (see styles.md universal rule 5).

## Script gate (all must pass before Stage 3)

1. Hook is declarative (or a skeleton-format curiosity question, or an evidence-backed reader-implicating question), specific, and works as a silent text overlay.
2. Read it aloud: 60s script lands 110–160 words; every line survives the 5-year-old test.
3. One idea per beat; every beat has a concrete visual; escalation is real.
4. The turn is one clean beat and the product answers the opened loop.
5. Proof beat uses the brief's strongest proof; CTA is soft and offer-tied.
6. Zero banned words; compliance gate passed.
7. The user has confirmed the script — **explicitly, on the script itself.** Present the full script (speaker + line + visual per beat) with the shot plan and estimated generation cost, and wait for the yes before any paid generation. Added credits or an approved brief are not script approval. Iterate freely here — it's the cheap stage. (Sole exception: the user says in their own words to run this batch without checking.)

Study swipe-file.md before writing — pattern inspiration, never copied: the structural moves (multi-character casts, narrator pacing, sung-VO hybrid structure) are what transfer.
