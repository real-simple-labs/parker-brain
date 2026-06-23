---
summary: "The method behind a brand's visual vocabulary — in-play / adjacent / out-of-play shot classification, the script-congruence and format-dependence rules."
status: pending Jimmy's review [~]
purpose: The doctrine of grounded visual direction for ads. AI invents generic visuals because it has no record of what a brand has actually filmed. The fix mirrors the spoken-script-voice fix. Learn the brand's visual vocabulary from what already exists on film, then map the expansion frontier from its orbit. Every method below is drawn from real visual data the Parker MCP exposes: the visual_hook, creator_demographic, storyboard, and TikTok video-report fields studied across own-account ads, captured competitors, affinity brands, and top organic TikTok in the niche. No invented visuals. Every shot described below was pulled from that data and is attributed.
layer: creative-strategy-context, an expertise method, not a brand doc
twin_of: spoken-script-voice.md. That doc governs the words, this one governs what is on screen.
---

# Visual-Vocabulary Method

## Why this document exists

Our scripts can sound human and still die on screen, because the words are only half of an ad. The other half is what the viewer sees, and that is where AI is weakest. Ask a model for visual ideas and it returns the same generic stock. A smiling person holding the product in soft window light. A slow product spin on a white table. A lifestyle montage of attractive people laughing. None of it is wrong. All of it is nowhere. It is the visual equivalent of "but here's the thing," the default the model reaches for when it has no record of what this specific brand has actually put on film.

Real accounts do not run on generic visuals. They run on a filmed vocabulary. One apparel account may open in silence on a bored-looking person in the problem product, cut to a narrator answering a text question, personify the product as an animated character, and use a pointer-style fit demo. Those are not generic. They are that brand's moves, proven on that brand's budget, and a model that has studied them can direct an ad that looks like the brand instead of looking like an ad.

This document is the method for building that filmed vocabulary, per brand, the same way the voice profile is built from a brand's own winning scripts. It does two jobs. First, it gives the extraction taxonomy: what to catalog from every ad the brand has actually run, so the brand's visual vocabulary is recorded, not guessed. Second, it gives the classification that turns that record into a usable map. What is in play, what is adjacent, and what is out of play, so a later scriptwriter or a static generator knows which visuals are grounded and which are an invention that needs flagging.

The brand's own filmed library is the authority. Nothing below is invented. The expansion frontier is mapped from real things seen in the brand's orbit, never from a model's imagination.

This is not a restriction. A brand's vocabulary is a baseline plus a mapped frontier, not a fence. The point is to know which ground is solid before stepping on it.

---

## Part 1: What a visual vocabulary is, and where it comes from

A brand's visual vocabulary is the full set of visual choices its ads are built from. The kinds of shots it films, the places it films them, the people it puts on camera, the way it handles the product, the demos it stages, the visual hooks it opens on, the b-roll it cuts to, the graphics it lays over the footage, and the way it paces and transitions. Read across a brand's library, those choices repeat. The repetition is the vocabulary. A brand that has filmed forty ads has a vocabulary whether anyone has written it down or not, and the job here is to write it down.

It comes from four sources, read in a strict order, because the order is what keeps the vocabulary grounded.

**Own account first, as the foundation.** What the brand has filmed and run is the bedrock. It is production-proven. The brand had the talent, the location, the budget, and the capability to make it, and Meta has data on how it performed. Everything the own account shows is in play by definition. This is always the first and largest source. A single own-account library might yield a silent text-question opener, an AI-animation personification character, a pointer demo, a flat-lay outfit slideshow, a fitting-room walk, a styled narrator run, and a split-screen sticky-note demo. That is a vocabulary, pulled entirely from ads the brand already paid to make.

**Organic TikTok next, as the proven-producible expansion.** The brand's own organic and the niche's top organic show what the audience makes and rewards on a phone, with no production budget. These are visuals the brand could shoot with a creator and a tripod tomorrow. In an apparel niche, that might include an expectation-versus-reality two-frame fit cut, a mirror-selfie try-on haul, a back-to-camera fit reveal with spoken body stats, a synchronized split-screen comparison, or a fitting-room verdict with discarded alternatives on the floor. Organic is the purest read of what the format actually rewards, because no agency sanded it down.

**Competitors next, as the contested frontier.** What direct rivals film shows visuals the brand could plausibly produce, same category, same rough budget tier, same kind of talent, that the brand has not run. A competitor might open on a customer photo while narrating a mistaken-identity story, or on a backyard body-fit demo with the product packaging in hand. Those are category-adjacent visuals the brand may have the capability to shoot but has not.

**Inspo and affinity last, as the reach frontier.** Brands the strategist admires or that share the audience but sit in another category show visuals worth aspiring to, some producible and some not. Examples might include a warehouse fulfillment-center shot, a high-production physical stunt, or a body-symptom demonstration shot with an expert-coded narrator. These map the outer edge of what is possible and sort into adjacent or out of play by whether the brand could realistically stage them.

The order matters because grounding decays as you move down it. Own-account visuals are certain. Organic is near-certain producible. Competitor is plausible. Inspo is aspirational. A vocabulary that treats all four as equally available has lost the plot. The whole value is knowing which ground is solid.

---

## Part 2: The extraction taxonomy, what to catalog from every studied ad

For every ad studied, walk these categories and record what is actually on screen. This is the visual equivalent of the five fingerprint dimensions in the voice profile. The data is there to support it. The own-account `visual_hook` and `creator_demographic` fields, the external `storyboard` array with its per-beat `visual` descriptions, and the TikTok video-report's named visual sections all describe these directly.

**Shot types.** The camera grammar. Close-up on the product or a body part, full-body mirror shot, walking sidewalk shot, overhead flat-lay, back-to-camera fit reveal, split-screen, macro on a single detail, talking-head to camera, POV looking down. Note the recurring ones. One account might lean on full-body fit shots, extreme close-ups on a product detail, and silent walking shots. A strong organic unit might hold a static eye-level mirror selfie for the whole video.

**Settings and locations.** Where the ad is shot. A bright domestic room, a city sidewalk, an office, a fitting room, a barn-door rustic backdrop, a backyard, a clothing store, a walk-in closet, a warehouse with metal shelving and a branded neon sign. Settings are a capability signal. A brand that only ever films in one room has a narrower production reach than one that shoots on location.

**Talent situations.** Who is on camera and how they are framed. A single creator to camera, a two-hander with a narrator and a model, a mashup of many testifiers, a partner pair, hands-only with no face, a personified animated object. Record the demographic the `creator_demographic` field gives. An account may repeatedly use a refined older narrator, an everyman demonstrator, or a creator who states exact body measurements. The talent situation is half of what makes an ad look like the brand.

**Product-interaction moves.** How the product is handled on screen. Cinching a belt, pointing at the fit with a rod, a 360-degree rotation to show the silhouette, squeezing the applicator so cream emerges from the holes, packing the product into a branded box, pulling a sock off to show the mark it left. These are the small physical actions that make a product feel real, and brands reuse them.

**Demo mechanics.** The staged demonstration that proves a claim. The one-pair-five-looks styling run, the side-by-side fit comparison, the stretch-and-move test, the before-and-after swap. A demo is a product-interaction move scaled up into the spine of the ad. Note whether the brand stages real demos or only asserts.

**Visual hooks as their own class.** The first-frame visual that stops the scroll, held separate from every other category because it carries the most weight and is the most replayable. This is what the `visual_hook` field captures directly. A man walking a sidewalk looking bored under a text question. A macro close-up of an unusual overlapping waistband. Gloved hands holding a product in front of a warehouse shelf. A split-body silhouette, one denim leg and one legging leg. The visual hook gets its own first-class section in the output, mirroring how the voice profile treats the verbal hook.

**B-roll families.** The cutaway footage the ad drops in between the main shots. Quick cuts of baggy denim gathering at the ankles, a montage of salt-and-pepper men in the product, a flat-lay of coordinated outfits, discarded pairs pooled on a fitting-room floor. B-roll is the connective tissue and brands have recurring families of it.

**Text-overlay and graphic style.** How words and graphics sit on the footage. Auto-generated bottom-center captions running word-for-word with the voiceover, a burned-in text hook at the top, a handwritten sticky note, a price-drop graphic with benefit icons, an Instagram-screenshot frame, an "Ask Me Anything" sticker. The overlay style is a strong brand fingerprint and is cheap to match once recorded.

**Transitions and pacing.** How the ad moves between beats and how fast. Hard cuts every three to five seconds, a rhythmic snap-transition matched to audio, a slow even hold on one mirror shot, a montage escalation. The `andromeda` delivery read matters here. An ad delivered to a 55-plus, two-thirds-Facebook audience has room for slower three-to-five-second cuts, while a young TikTok-native unit cuts faster. Pacing is read against where the ad actually delivers.

Catalog these per ad, then read across the library for what recurs. The recurring choices are the brand's vocabulary. A one-off is noted but not treated as signature until it repeats.

---

## Part 3: In play, adjacent, out of play

Once the vocabulary is cataloged, every visual gets sorted into one of three states. This classification is the whole point of the doc, because it is what a downstream scriptwriter or generator reads to know which ground is solid.

**In play.** The brand has filmed it and run it. It appears in the brand's own ad library. It is production-proven: the brand had the talent, the location, and the capability, and there is performance data on it. If the account has run the silent text-question opener, the personification character, the pointer demo, and the flat-lay slideshow, those visuals are in play. In-play visuals need no flag downstream. They are the grounded baseline a generation prompt builds from.

**Adjacent.** The brand has not filmed it, but it has been seen in the brand's orbit, its own organic, a competitor, an inspo or affinity brand, and the brand's apparent production capacity could plausibly make it. The honest criterion is capability, read from what the own account already proves the brand can do. If the account films real people in real locations, runs AI-animation characters, stages multi-person mashups, and produces high-production explainers, then a back-to-camera fit reveal with spoken body stats may be adjacent when seen in the niche. Every adjacent entry carries its evidence: the specific orbit unit where it was seen, described richly enough to replay, plus the one-line reason the brand's apparent capacity covers it. Adjacent is the expansion frontier, and it is the most valuable part of the doc, because it is where new production asks come from with proof already attached.

**Out of play.** The visual requires production muscle, talent, or capability the brand has never shown. A physical-stunt production is out of play for an account with no evidence of being able to stage stunts. A celebrity hook depends on access to a celebrity. If the account proves celebrity access once, that specific lane moves from out of play to in play; for a brand with no celebrity access it stays out. Out of play is not a permanent verdict and not a scold. It is an honest read of current capability, and the line moves the moment the brand proves the capability. Mark out-of-play visuals so a generator does not casually invent them as if they were free.

The criterion that separates adjacent from out of play is always read from the own account, never asserted. If the brand has filmed real people in real locations, location shoots with real talent are adjacent. If the brand has only ever filmed product on a white table, a location shoot is out of play until proven. The classification is grounded in demonstrated capability, the same way an in-play visual is grounded in a filmed unit.

---

## Part 4: The script-congruence rule

A visual must say what the words are saying. This is the first of two binding rules, and it is the one AI breaks most often, because a model will happily pair a line about thigh comfort with a generic shot of a smiling face that proves nothing.

Every script beat carries a claim or a feeling, and the visual direction for that beat must show the thing the words assert. When the line says the waistband does not dig in, the visual shows the waistband not digging in: a hand running along a flat waistband, not a man smiling in a field. When the line names a pinching fit problem, the visual shows the pinch. When the creator names an exact rise measurement, she gestures to the waist to indicate the rise as she says it. The visual and the verbal are congruent: the eye sees the claim the ear hears.

Incongruence is a tell as loud as any AI-script tell. A beat where the words make a specific claim and the visual shows a generic mood is a beat the viewer does not believe, because nothing on screen proved the words. The discipline: for every beat, name the visual that demonstrates that beat's specific claim, sourced from the brand's vocabulary. If no in-play or adjacent visual proves the claim, that is a signal the beat needs a new shot. Flag it as an adjacent or out-of-play ask rather than papering over it with stock mood footage.

The strongest brand visuals are pure congruence. If the line names a mark left by clothing, the shot should show the mark being revealed. The words name the symptom. The shot shows the symptom. That is the bar.

---

## Part 5: The format-dependence rule

The same script beat is shot differently depending on the ad format. This is the second binding rule, and it is why a visual vocabulary cannot be a flat list of shots divorced from format. The format is the container, and the container changes the grammar.

The format taxonomy lives in `creative-strategy-context/ad-formats/`, the video, static, and both folders that name every format Parker classifies. Read the brand's vocabulary against it. The same "this waistband does not dig in" beat translates differently across formats. In a UGC single, it is a creator filming their own waist on a phone, handheld, talking to camera, auto-captions running. In a b-roll mashup with voiceover, it is a clean cutaway of a hand on a flat waistband with no face, narration over the top. In an AI-animation unit, it is the personified jean character describing its own non-digging waist. In a static, it is a single designed frame: a close-up of the waistband with a headline and a benefit callout laid over it, no motion at all. Same claim, four visual grammars.

So the vocabulary records per-format grammar where the brand shows it. When a brand has run the same kind of beat across multiple formats, note how each format shot it, because that is what tells a downstream generator how to translate a beat into the format being produced. A static generator cannot use a UGC walking-shot direction. It needs the single-frame version. A UGC script cannot use a flat-lay direction. It needs the handheld version. The format-dependence note is what makes the vocabulary usable across the formats a brand actually runs, rather than only the format it was cataloged from.

Pacing rides on format too, and pacing is read against delivery. A format delivered to an older, lean-back, Facebook-heavy audience has room for slower cuts and a longer hold. A TikTok-native format aimed at a younger feed cuts faster. The format-dependence read and the delivery read are taken together.

---

## Part 6: How the vocabulary is used downstream

The visual vocabulary is a brand sub-context doc, `sub-context-docs/visual-vocabulary.md`, and it is the visual twin of the brand voice profile. It feeds three surfaces, and knowing how it is consumed is what keeps the doc honest about what it must contain.

**Scriptwriting visual cues source from it.** When a script is written or adapted, every beat's visual direction is pulled from the brand's vocabulary, and every beat is marked in play, adjacent, or out of play. A beat directed with an in-play shot is grounded and needs no flag. A beat directed with an adjacent shot is a new production ask, flagged with the orbit evidence that proves it producible. A beat that can only be served by an out-of-play shot is flagged loudly so the strategist decides whether to build the capability or rewrite the beat. This is the visual half of what `spoken-script-voice.md` does for the words.

**AI ad-generation prompts source from it.** When Parker generates a static or a video-ad concept, the visual vocabulary is the grounding that stops the model inventing generic stock. In-play shots ground the generation prompt. The model is directed toward visuals the brand has proven, in the brand's real settings, with the brand's real talent type and overlay style. Out-of-play visual inventions get caught and flagged rather than shipped as if they were free. The vocabulary is what makes a generated ad look like the brand instead of looking like a model's default.

**New-production asks get flagged as adjacent, with their evidence.** The adjacent tier is the doc's engine for growth. When the strategy calls for a visual the brand has not filmed, the vocabulary already holds the candidate, sorted as adjacent, with the competitor or organic or inspo unit that proves it producible described richly enough to hand to a creator as a reference. A new-production ask sourced from the adjacent tier arrives with its proof attached, which is the difference between "let's try something new" and "here is the exact shot, here is who already runs it, here is why we can make it."

---

## Part 7: How to mark every entry

Every entry in a brand's visual vocabulary carries two marks, the same discipline the rest of the context system runs on.

**The classification:** in play, adjacent, or out of play, with the criterion that put it there. In play points at the brand's own filmed unit. Adjacent points at the orbit unit plus the capability read. Out of play points at the missing capability.

**The evidence mark:** stated, inferred, or verified. A visual is *verified* when it was pulled directly from the data, a `visual_hook` field, a `storyboard` beat, a TikTok report section, and described from that source. A visual is *inferred* when the classification is a judgment call, such as reading whether a competitor's shot is within the brand's capacity. A visual is *stated* when a source asserts it but it was not confirmed in the data. The most damaging error is laundering an inferred capability into a verified fact, because a downstream generator will treat an "adjacent, verified producible" entry as safe ground and build on it.

And every entry carries its source ad described richly enough to replay. A later reader, often a model with only the words, must be able to picture the shot clearly. Move through what is on screen in order: the frame, who or what is in it, the setting, the action, the on-screen text, the product's role, the cut. A description too thin to replay has not done its job. The data supports this directly. The storyboard and TikTok-report fields are already this granular, so the vocabulary preserves that granularity rather than collapsing it into a content-type label.

---

## The one-line test for everything above

Picture the shot from the description alone. If a model could direct or generate that exact visual from the words on the page, and could tell whether the brand has filmed it, could film it, or could not, the entry has done its job. If it reads as a generic content type, it has not.


## No invented direction

Visual direction is quotation, not imagination. Every gesture, glance, camera move, and staging beat in a script's visual column must trace to a shot somebody actually filmed: this brand's ad, a competitor's, an organic video, an inspo unit. Any micro-behavior written into the direction, however small, must name the ad where that behavior was observed, and the entry cites it. A shot the brand has never filmed is allowed only when the source ad is named and its staging is described as it actually appeared, so the production team is copying something real rather than acting out a model's imagination. Micro-direction with no source is fabrication and gets cut in the audit, the same as an invented statistic.
