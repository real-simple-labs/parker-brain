# Format Library — AI Animation Ads

The format is the ad's delivery mechanism: who talks, how the story escalates, where the product enters. Pick format BEFORE style (any format can wear most styles). Never default — diagnose the product with the selection table, recommend one format + one backup, and say why in one line.

## Format selection

| Diagnose the product/script | Format |
|---|---|
| The problem is invisible/internal, has distinct symptoms or failed alternatives worth personifying; brand has playful permission | **1. Talking-character cast / villain confession** |
| Message needs a step-by-step mechanism walk-through with authority | **2. Narrator-led explainer** |
| The story happens TO a person (their body, their day, their journey); talking objects would feel forced | **3. Character-follow** |
| Benefit compounds or consequences escalate over time/quantity ("what happens if…") | **4. Skeleton progression** |
| Simple message + brand with entertainment permission; feed fatigue on spoken ads | **5. Song ad (sung VO)** |
| Product needs a "this is real" grounding beat (usage demo, texture, unboxing) | **6. Hybrid animation + live action** |
| Script needs an emotional voice AND an authority voice | **7. Multi-narrator layers** |
| Fast, cheap, always-on companion to every video concept | **8. Statics** (see static-ads.md) |

In-library proof (Parker ad library, July 2026): Organifi's parasite mechanism explainer ranked **#2 by impressions** among tracked competitor ads · Grüns runs personified-confession at scale ("I used to live in your head... until the GLP-1 era" — a hair follicle; "Dad, why aren't you taking care of your nutrition?" — the future child) · Olipop's sung jingle ("Olipop, Olipop") · Bravo Sierra scent-story animations. The formats below are working in-market right now.

---

## 1. Talking-character cast / villain confession

Personified problems, symptoms, failed solutions, ingredients, and the product itself speak directly to camera. 2–5 characters. The strongest opening move in the format: **the villain confession** — the failed solution or the problem itself confesses why it wins/sucks, in first person, with zero remorse.

**Why it works:** pattern interrupt (objects talking = scroll stop) + education (why the old way fails) + positioning (your product enters as the obvious upgrade) — three triggers in one format.

**Cast archetypes:** Villain/problem (smug, taunting — "Your toothbrush has never even met me, bro") · Failed solution (sheepish confession — "I dried out your mouth and made it worse. I also only last about 20 minutes. My bad.") · Symptom characters (each with a distinct personality, one scene each) · Hero product (calm, confident, slightly authoritative — arrives AFTER the pain is fully built).

**Script skeleton (30–60s):** villain hook (0–5s, the confession/taunt) → symptom cast escalates (1 character per beat, one idea per beat) → the turn (product character enters: "That's why you need me.") → mechanism in product's voice → proof beat (reviews/stat/guarantee) → CTA with a knowing final line.

**Rules:** one speaker per shot — specify which character speaks and that the others' mouths are closed and reacting silently, or the model animates every mouth · give each character its own scene rather than crowding a 9:16 frame · exact dialogue lines go INTO the video prompts (drives lip-sync) — Pixar-style/3D only; in claymation/paper/crochet nobody's mouth ever moves (see styles.md) · castable characters come from the research brief (ingredients, body parts, competing products, tools).

**Angle generator:** list what the customer tried before this product; each failed solution is a castable villain. "I'm your drugstore moisturizer. I'm packed with cheap seed oils to keep my price low… but those oils clog pores." Works for any category: supermarket coffee (stale), cheap mattress (sinks), generic multivitamin (low absorption), bathroom scale (only knows your weight).

## 2. Narrator-led explainer

One narrator carries the whole script; characters and mechanisms react silently on screen. The Organifi #2 ad and the Viasox varicose-vein ad are this format: calm authority walking through what's happening inside your body, then the product's mechanism fixing it.

**Script skeleton:** declarative hook stating the hidden truth ("This is why your weight doesn't reflect your health") → problem mechanism visualized (cross-sections, internal views — the format's superpower) → agitation (daily-life consequences, escalating specificity) → the turn ("Now imagine instead…") → product mechanism → proof → soft CTA ("Look up [product]").

**Rules:** NO lip-sync anywhere — every video prompt describes VO as context and prohibits speaking (`as a [TONE] narrator says "[LINE]" — no character lip-sync, no characters speaking on screen`) · vary shot types like a documentary: wide establishing → medium character → cross-section mechanism → daily-life vignette → product hero · this format carries the most educational payload; keep each beat ONE idea.

## 3. Character-follow

One character (human or animal) is the subject of the entire ad — the script narrates what happens to them, around them, or inside them. No talking objects, no reactive cast. Best when personification would distract from a body/journey story (sleep, posture, gut, weight, energy).

**Visual treatments:** full-body in scenes · anatomical cross-section / x-ray view · before/after states · surrounded by visual metaphors of the narration. Prompt like narrator-led (VO as context, no lip-sync); the character is "a body in motion or a body being observed."

## 4. Skeleton progression ("What happens if you…?")

A recurring cartoon skeleton lives out an escalating second-person journey ("Day 1… Day 30… Day 365…"), narrated by one voice. Borrowed from viral YouTube/Shorts science-hypothetical content — the curiosity gap does the retention work. Works for B2B and unsexy products precisely because the skeleton makes abstract benefits visceral.

**Four mechanics every skeleton script must hit:**
- **A. Curiosity-gap hook** — "What would happen if you ___?" / "How long can you ___ before ___?" / "What happens if you NEVER ___?"
- **B. Escalating spine** — Time (Day 1 → 30 → 365), Quantity (1 → 5 → 42), or Stage (1 → 5).
- **C. Visceral concrete specifics** — every beat is one physical, sensory image, not a claim. "Saves time" → "You blink and the work's already done. You stare at an empty to-do list, twitching."
- **D. Payoff** — triumph (crowned, unstoppable) or catastrophe (system failure). Use-the-product → triumph; never-fix-it → catastrophe.

**Angle diagnosis:** benefit compounds over time → *Transformation* (time spine, triumph) · painful worsening status quo → *Cost-of-inaction* (time, catastrophe) · people overdo a broken old way → *Limit/overload* (quantity, catastrophe) · product is vivid in an unexpected era/world → *Origin/scenario* (time/stage, triumph). Fusing two is common (fragrance ad: skeleton + 1800s world + transformation → crowned king).

**Creative-strategy layer (what separates good from on-format):** open the loop in the hook and never answer early · stack mini-loops between beats ("…but that's nothing compared to Day 30.") · **earn the product with one clean turn beat** ("Then you find [product].") — the product must feel like the answer to the loop, not an ad break · escalate stakes, not just the timeline · CTA rides the momentum (guarantee/trial, never "buy now").

**Character consistency is the whole production game.** Pick ONE of the four locked skeleton looks and paste its Character Bible verbatim into every image prompt:
1. **Bare-Bones Cinematic** (default): `A full anatomical skeleton with natural adult human proportions, tall and lanky, smooth ivory-cream bones with realistic bone detail (NOT toy-smooth, NOT chibi, NOT scary), and large expressive cartoon eyes with white sclera and dark pupils set in the eye sockets, giving an emotive, surprised, lovable face. No clothing. Same character in every shot.` + `cinematic 3D animated render, photoreal [THEME] environment, warm [palette] grade, soft volumetric light, shallow depth of field. 9:16.`
2. **Dressed Skeleton** (wearable/lifestyle/identity products): same skeleton + complete themed wardrobe, skull and hands still visible.
3. **X-Ray with Organs** (health/body/"what happens inside you"): translucent glowing body, white skeleton + organs glowing red-orange through blue-tinted translucent outline, large cartoon eyes; clean sci-fi medical render.
4. **Cute Cartoon Mascot** (only for intentionally cute brands): chibi, oversized round skull, toy-like; playful 3D render, pastel background.

Theme the world to dramatize the angle (modern office, 1940s, Wild West, the product's own industry); reaction characters (townsfolk, coworkers) amplify the arc. Full 4-stage production flow (script → concept board → image prompts → video prompts) follows the standard pipeline in SKILL.md; the beats map 1:1 to VO lines.

## 5. Song ads (sung VO)

The script IS the lyrics; the whole ad is a micro music video. Rare enough in feed to earn attention, and "so visually and audibly stimulating" that completion rates run high. Claymation and 3D-feature styles carry it best; characters bob/sway on the beat but never lip-sync words.

**Workflow inversion — the song comes FIRST:** write lyrics → generate the song (Suno) → pick the take → map the 15–19 frames to the song's actual beat structure → then images/video. The song dictates visual pacing, not the script. (Every other format: script first.)

**Lyric rules:** hook in the first 5 seconds · lyrics sell the ANGLE, not the brand name chant · real song structure (verse/chorus, real rhyme), not a jingle · 4–8 syllables per line · genre-authentic vocabulary · 15s = hook + one chorus pass, 30s = verse-chorus-verse-chorus, 60s = full structure with bridge · include the unique mechanism in a verse (peroxide powder, heme iron — the differentiator is what makes it an ad, not a song).
**Genre by demo (abridged):** moms → pop/indie pop (Gen X moms → country/soft pop) · Gen Z women → pop/hyperpop/R&B · Gen Z men → hip-hop/trap/EDM · fitness → hip-hop/EDM/hard rock · luxury → ambient/modern jazz/cinematic pop · boomers → country/classic rock/soft pop · wellness → ambient/indie folk. (Full map in audio.md.)
**Hybrid pattern:** sung verses for emotion + one spoken authoritative voice for proof/CTA (the claymation Flakes ad does exactly this — see swipe-file.md).

## 6. Hybrid animation + live action

Animated scenes intercut with real filmed footage of the product in use. Animation personifies and explains; live action grounds ("this is real") near the proof/CTA. Requires real footage from the brand vault. The +COOL ad cuts from animated bacteria villains to a real man using the device at 0:23 — right at the turn.

## 7. Multi-narrator layers

Two+ VO voices share the script — intimate first-person emotional setup, then a grounded authority voice for proof/CTA (often opposite gender for separation). Time the handoff to a visual transition (product entrance or proof start). Also the container for sung-intro + spoken-close hybrids.

---

## Format × style quick pairings

- Villain confession → 3D feature animation (lip-sync needed) — the only format that REQUIRES a lip-sync-capable style.
- Narrator-led / character-follow → any style; claymation and paper add trust/warmth.
- Skeleton → its own character library (above), photoreal-environment 3D render.
- Song ads → claymation (proven), 3D feature, crochet.
- Statics → every video concept should also ship 2–4 statics from its hero frames (see static-ads.md).

## Length & pacing defaults

**Benchmark against Parker's top-impression ads before locking length — the market is FASTER than instinct.** Production-verified July 2026: the top animated/character ads in supplements ran 5–29s with the product on screen at 0:00–0:03; the rare 60s+ winner earned it with a shock hook in second one. Defaults:
- Primary cut 30–45s; ship a 60s director's cut and a 15s cutdown as variants, not the lead.
- Hook lands by second 2–3 (verbal + visual + text designed together). **Problem/education fully in motion by second 6–8** — one villain beat max before someone explains what it means for the viewer.
- The turn (product entry) by second 15–18 absolute — not "40% of runtime."
- One idea per beat, 2–5s per beat, zero dead air: trim every clip to its line + a breath, no held tails. Late-ad joke beats (the villain's last word) are the first cut when pace is at stake — save them for the director's cut.
- Music bed under everything from frame one; silence reads as broken on paid social.
