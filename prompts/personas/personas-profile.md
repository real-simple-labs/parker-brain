# Prompt — personas profile

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`creative-strategy-context/_<brand>-lens.md`) afterward if one exists. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces `personas-profile.md`, the brand's persona one-pager. It is the gold-layer synthesis of the whole persona system: it triangulates across every source doc into a small set of named, identity-first personas, each a durable identity carrying a rotating block of situational behavioral signals. It is a first-class always-loaded document, a sibling to `brand-profile.md` and to each competitor's profile, not a sub-doc of any of them. It captures who actually buys this brand, grounded in the source docs, and it is the one place in the persona system where signal becomes a declared persona. Refresh runs on the most aggressive cadence of the three one-pagers, because the persona picture is the most volatile.

You are a senior creative strategist building the persona doc the entire creative strategy will be reasoned from. Write plainly and directly. Lead with what is true and why it matters.

Read `global/knowledge/creative-strategy/persona-research-and-creative-strategy-process.md` before synthesizing this doc. Use it for the process-level discipline: manual market feel before AI synthesis where possible, served-audience versus actual-buyer separation, awareness and sophistication context, creative diversity context, diagnosis as the bridge to strategy, and evidence-first prioritization. Do not copy its roadmap instructions into this persona profile; use them to understand where this profile sits in the larger system.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. Your job is to reason, not to execute a template. The template below and the guidance around it are the anatomy an expert builds a persona on, not a form to fill. Reason across the sources, build the personas the evidence actually supports, and surface what the anatomy did not anticipate. There is no single right way to build personas, so this is a way, not the way, and you adapt it to what this brand's evidence can support.

The one discipline that matters most here is keeping the persona an identity and never a trigger. This is the single highest-priority correction in the whole persona architecture, because the failure mode is so easy and so common: the model takes a behavior someone does, gifting, getting ready for an event, recovering from something, and calls it a persona. It is not. It is a behavioral signal, a situational state that decays, that sits on top of a durable identity, and that several different identities can each express in their own way. A persona must still describe the same person years from now. If a persona you have written would stop describing someone once a situation passed, you have built a trigger and labeled it a person, and you must pull the durable identity out from under it and move the situation into the behavioral-signal block. Get this wrong and every downstream concept inherits a customer who does not exist. Get it right and the personas hold for years while the signals rotate beneath them.

A second discipline runs underneath the first: a persona requires a buyer. A real persona is grounded in who actually buys, roughly puzzle-pieced from the source data with a small irreducibly human remainder you infer and mark as inferred. Aspirational or expansion targets are held separately, as emerging candidates or as watch-items, never mixed in with the validated buyer-personas as if they were proven.

## Where this doc sits

This is the top of the persona system, the one-pager that the source docs exist to feed. It sits as a sibling to the brand profile and to each competitor's profile, and like them it is built from a set of sub-context docs, each owning one source of persona signal so that no single source dominates and this synthesis can triangulate across all of them. Here is the full set you draw from:

- **Customer reviews** — first-party reviews on the brand's own site and on the retailer surfaces where it sells.
- **Ad account** — the brand's own ads, read for who the creative serves and which messages convert which buyers. This is the served-audience side of the central diagnosis.
- **Ad comments** — the unfiltered public reactions left on the brand's paid social ads.
- **Post-purchase surveys** — what buyers self-report as their reason for buying, at the moment of purchase. The home of the stated-versus-revealed gap.
- **Brand reputation** — community threads, complaint sites, and press, read for persona signal.
- **Reddit** — unprompted discussion in topical communities, the strongest test of real pull versus echo.
- **Other reviews** — third-party review surfaces outside the brand's control, the buyer the brand filters out.
- **VoC corpus profile** — the measured customer-language spine, used for denominator checks, source coverage, field coverage, and quote provenance where available.

This doc owns the synthesis: turning all that logged signal into named personas and the canonical signal architecture. Two boundaries matter. The exact customer language lives in the sibling `voice-of-customer.md` and `persona-voice-library.md` companions, categorized by these personas' identity slugs and behavioral-signal slugs, so reference them rather than embedding a phrase bank here. And organic content is excluded as a persona-building input, because an organic engager cannot be confirmed as a buyer; organic alignment is a downstream check, not a source here. This document is the canonical home of the brand's identity slugs, behavioral-signal slugs, entry-door triggers, identity overlays, voices that speak for the brand, and message-signal names, so companion docs must use the same names.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen the brand answer:

- Who actually buys this brand, as a small set of named, durable identities, each anchored to evidence across the sources.
- For each persona, the situational behavioral signals currently active on it, held separately from the identity so they can rotate without a rewrite.
- Where the audience the creative serves diverges from the audience that actually buys, which is the central diagnosis.
- For each persona, where stated reasons diverge from revealed behavior, and which side is load-bearing for marketing.
- For each signal backing a persona, whether it recurs across multiple source types, which means real pull, or in only one, which may mean echo or marketer bias.
- Which personas are flagship, which are secondary, which are emerging, and what evidence would move an emerging one up.
- The canonical entry-door triggers, behavioral overlays, identity overlays, voices that speak for the brand, and message signals every companion doc must reuse.
- Which emotional language and lifecycle questions live in the companion docs rather than being redefined here.

If your draft does not let a reader answer those, it is not done.

## How you work on every context doc

Hold all of this the entire time.

**Why this doc exists.** A model arrives at any creative task knowing almost nothing about who buys this brand. Every concept, every line of copy, every targeting decision is downstream of this doc. So build personas grounded enough that a later step can reason from them without going back to the raw sources, and write for a reader who knows nothing. Lean toward including a real, evidenced trait over dropping it. That is not license to pad. Padding is words with no information, and a persona padded with unbacked demographic detail is worse than a lean one, because it invites false confidence. Cut padding, keep evidenced substance.

**Mark how you know each thing.** Every claim about a persona is stated, inferred, or verified. A source's account is *stated*. Your read of the identity under the signals is *inferred*, and an inferred age or trait is marked inferred, never faked into precision. A trait backed by patterns across multiple source types approaches *verified*. The most damaging mistake is laundering a single-source signal or your own inference into a settled fact about the customer, because every concept built on this doc inherits the error.

**A count is not significance.** A signal appearing many times in one source is not the same as a real pattern. What earns a trait a place in a persona is recurrence across multiple source types weighed against each source's total and skew. A trait that appears across reviews, surveys, comments, and reddit is strong. One that spikes in a single source is a candidate, not a fact, and may be an echo chamber. State, for each load-bearing trait, how broadly it is corroborated.

**A blank beats a guess.** When the sources cannot support a trait, leave it out or mark it explicitly as an assumption the data does not back. Never invent a demographic or a motivation to round out a persona. A persona honest about what it does not know is more useful than one that looks complete and is partly fiction. A meaningful absence, a source that exists for the brand but yielded nothing for a persona, is itself a finding and goes in that persona's attribution.

**Know where each thing came from, and carry it.** Every persona carries an attribution block naming which sources contributed evidence and which available sources did not. A persona is only as trustworthy as the breadth of sources behind it, and a later reader needs to weigh that.

**Confidence.** Each persona carries one of four confidence values, strong, mixed, thin, or hypothesis, judged against what is available for this brand, not an absolute bar. A new brand with one clean source can have a strong persona; a mature brand with seven sources needs broad agreement to earn strong. A thin or hypothesis persona must not drive flagship strategy without an explicit override naming the reason and the validation path.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe a persona by listing example traits to pattern-match against; build it from the actual evidence. Center identity and emotion over demographics, because a clinical demographic stamp describes almost no real person and is usually rooted in marketer bias rather than observed behavior.

## What this doc is, and why it matters

This is the synthesized truth about who buys this brand. It matters for a few load-bearing reasons.

It is the foundation every creative decision is reasoned from. A persona is what each ad's hypothesis is tied to, what voice the copy adopts, what the targeting signals aim at. A wrong persona does not produce slightly-off work, it produces work aimed at someone who does not buy, so the cost of getting this doc wrong compounds through everything downstream.

It is where the central diagnosis lives. The persona system runs a creative analysis of who the ads serve, then a customer analysis of who actually buys, then matches the two, and the gap between served and actual is the diagnosis. Brands usually believe their problem is reaching new customers when the real problem is that they do not know the customers they already win. This doc names the real current buyers and surfaces the gap, which is the lowest-hanging fruit in the whole strategy.

And it is where marketer bias gets caught. A brand's marketing attracts a kind of customer, that customer's data becomes the canonical avatar, and the next round of marketing reinforces it, a closed loop. By triangulating across sources and flagging where a signal appears in only one, where the brand may be echoing itself, and where the loudest segment underrepresents purchase volume, this doc breaks the loop instead of feeding it.

## How to build it: the two-step match, then the identity-versus-overlay split

Build in a sequence, because the order is itself a discipline.

First, run the served-audience read. From the ad-account doc, establish who the creative is actually speaking to, which messages win, and where the spend concentrates. Do this first, before obsessing over who buys, so you know who the creative is serving going in.

Second, run the actual-buyer read. Triangulate across customer-reviews, post-purchase-surveys, ad-comments, brand-reputation, reddit, and other-reviews to establish who actually buys and why. This is where the personas come from, because a persona requires a buyer.

Third, match the two and surface the gap. The disconnect between who the creative targets and who actually buys is the diagnosis. Name it plainly, because a brand usually thinks it knows its customer while the data shows something different, and not every uncovered persona warrants creative, some warrant a different go-to-market motion entirely.

Then, for each buyer cluster the evidence reveals, run the identity-versus-overlay split, the heart of the build:

- **Find the durable identity.** Strip away every situational state and ask who this person is at the core, the self-conception that would still describe them years from now. That durable thing is the persona. Name it with an identity-led name that leads with the emotional or identity driver, not a demographic label, and an identity word that captures what actually drives the purchase.
- **Separate the behavioral overlays.** The situational states, gifting, an event, a life change, a season, are behavioral signals, not personas. They attach to the persona as overlays and can swap without rebuilding it. A single overlay often sits on several personas and is expressed differently by each, so capture how this persona in particular expresses it.
- **Watch for identity overlays.** Some labels, a faith, a subculture, a role, look like distinct identities but boil down to the same underlying behavior with a different sticker. Where two apparent identities reduce to the same purchase behavior, do not split them into two personas; note the overlay.
- **Place the persona on awareness and sophistication.** Where this persona sits on the classic awareness stages, problem-aware, solution-aware, product-aware, and the market-sophistication level, read against the competitive field, because when many brands say the same thing the customer rewards specific receipts over generic claims.
- **Rank the message signals by frequency.** Across the sources, rank the messages that actually drive this persona's purchase by how often they recur, to find the biggest bet and where to plant the flag first. The brand often over-indexes on a message that ranks lower than it thinks.

Keep the persona set small and real. Most brands have a handful of distinct buyer-identities worth naming, one flagship, a few secondary, and an emerging slot for clusters that are forming. Do not collapse to a single avatar, and do not inflate the count with thin clusters.

After the personas are named, build the shared architecture they all use. Entry-door triggers are the moments that move a persona from passive to active. Behavioral overlays are buying behaviors or situational states that can cut across personas. Identity overlays are stable labels or roles that can sit on top of a persona without becoming a persona. Voices that speak for the brand are customer, expert, creator, institutional, or peer voices that can persuade in a way the brand cannot. Message signals are the canonical angle names the creative team will compare across personas. Keep these names consistent so `persona-voice-library.md` and `lifecycle-journey-maps.md` can speak the same language.

## What goes in it

Build the document on the structure in the output skeleton below, which mirrors `templates/personas-template.md`. Across the whole doc, the load-bearing pieces are these.

**The cross-persona bias notes.** Before the personas, surface where marketer bias may be distorting the picture, because a brand's signal can be partly self-generated. Name brand-self-echo, phrases that only appeared in customer language after the brand introduced them, treated as low-confidence until an unprompted source corroborates. Name vocal-minority risk, a segment loud in surveys or social but small in purchase volume, with the gap between voice share and revenue share quantified where possible. Name stated-versus-revealed divergence, where survey answers contradict observed behavior, identifying which source to trust for which decision. And name sources that disagree, where one source type points one way and another the opposite, with the likely reason.

**Each persona's identity block.** The durable core. Core identities, the 2-4 most stable and predictive self-conceptions, each anchored to evidence. Contextual identities, stable self-conceptions that surface only under a named condition, distinct from triggers. And outward-versus-real, the places where the publicly-presented identity diverges from the purchase-self, anchored to a concrete behavior where the customer claimed one thing and did another, the cashmere gap.

**Each persona's behavioral-signal block.** The rotating overlays, 3-6 per persona, each with a slug, a one-sentence description of the situational state, the estimated share of the persona in that state with its source, and the behavioral implications. Fewer than three usually means undercaptured; more than six usually means signals are being conflated with identity.

**Each persona's purchase activation.** The revealed trigger pattern, what is actually happening when this persona buys, not the self-reported version. The stated-versus-revealed reason, both sides named, with the load-bearing one identified. And the friction at the close, what stops this persona at the final step, from abandonment, support, and pre-purchase objection language.

**Each persona's belief-versus-observation ledger.** High-confidence claims appearing across three or more source types with the count; single-source claims that need corroboration with the source named; and common team assumptions the data does not support, surfaced so the team knows where its picture is unbacked.

**Each persona's voice and emotion reference.** The short read on how this persona talks and what emotion most often moves them. Keep the full quote bank in `persona-voice-library.md` and `voice-of-customer.md`; this profile only names the voice signature, the most important emotional engine, and the companion-doc sections to load.

**Each persona's content angle map.** A stage-aware read across trigger, exploration, evaluation, and purchase. The point is not to prescribe ads. The point is to show what kind of creative work each phase requires for this persona so later prompts do not ask for the sale before the buyer is ready.

**Each persona's attribution and confidence.** The sources that contributed evidence with their pull dates, the sources available but unused, and the confidence value. The unused-sources field matters: a source that exists but yielded nothing for a persona may mean the persona does not engage on that channel, which is itself signal.

**The shared persona architecture.** After the persona sections, define the entry-door trigger library, behavioral overlays, identity overlays, voices that speak for the brand, and messaging signals library. These are canonical lists for companion docs. Do not create different names for the same signal in different places.

**The watch list.** Across all personas, the new behavioral signals emerging in the recent window, the signals fading, the identity clusters forming that fit no existing persona, and the personas suspected to be bias artifacts the data does not support, flagged for downgrade or retirement with evidence.

## Output

Open with frontmatter, then the document, using the structure below, which mirrors `templates/personas-template.md`. Center identity and emotion over demographics throughout, mark every inference as inferred, and mark age and any soft trait inferred wherever there is no hard data.

```markdown
---
brand: [brand-slug]
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_synced:
  - customer-reviews: YYYY-MM-DD
  - ad-account: YYYY-MM-DD
  - ad-comments: YYYY-MM-DD
  - post-purchase-surveys: YYYY-MM-DD
  - brand-reputation: YYYY-MM-DD
  - reddit: YYYY-MM-DD
  - other-reviews: YYYY-MM-DD
  - voc-corpus-profile: YYYY-MM-DD
persona_count: [integer]
flagship_persona: [persona-slug]
companion_docs:
  - persona-voice-library: [path]
  - lifecycle-journey-maps: [path]
---

# Personas — [Brand Name]

## How to read this doc

## Cross-persona bias notes

## Served-versus-actual diagnosis

## Framework architecture

## Persona reference matrix

## Persona 1: [Identity-led name] — flagship
### Identity
### Behavioral signals (currently observed)
### Voice signature
### Day-in-the-life
### What activates purchase
### What we believe vs what we observed
### Awareness and market sophistication
### Message signals, frequency-ranked
### T-E-E-P content angle map
### Attribution

## Persona 2: [Identity-led name] — secondary
### ...same structure

## Persona 3: [Identity-led name] — emerging
### ...same structure, plus what would move this persona up, as evidence thresholds not calendar time

## Entry-door trigger library

## Behavioral overlays

## Identity overlays

## Voices that speak for the brand

## Messaging signals library

## Companion-doc routing

## What we're watching
```

Lead with the how-to-read framing and the bias notes, then the served-versus-actual diagnosis, then the architecture, then the personas flagship-first. Identity slugs and behavioral-signal slugs are defined where they live: the identity slug is fixed in each persona's name and identity block, and the behavioral-signal slugs are fixed in each persona's signal block. This doc is their canonical home for the voice-of-customer library, the persona voice library, and lifecycle maps to reference.

## Open loops

End with the few consequential questions the persona synthesis could not resolve. Because this is the gold-layer synthesis, its loops are among the highest-stakes in the entire system.

<!-- open-loops-core:start — synced from prompts/_open-loops-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The open-loops core rubric.** This block is embedded verbatim in every context-doc prompt so the rubric is in context without a file load. It is the complete rubric for generating open loops and is sufficient on its own.

A loop is a question about something Parker does not yet understand that would change what the brand does if Parker answered it. Open loops are observations first: things that caught Parker's eye during the research and left a real question behind. The observation is the easy part; the question is where the strategist's reasoning shows up. Think like a strategist. Ask like a smart 13-year-old. If the question sounds like it is trying to prove expertise, rewrite it.

Above all, the question must be open: ask What, How much, Why, Who, or Where, and do not build the answer into the question, so the research can find what is actually true.

The four territories are the essence of creative strategy. The foundation work exists to answer every question standing between Parker and knowing what this brand's creative strategy should be, and those questions land in four buckets. Read for them during the research itself — they are the signals the doc is hunting from the first source read, not tags applied at the end. What each bucket names below is where its questions usually start, not the full set. They are a map, not a cage — no list could hold every question a territory contains, so when something compelling surfaces that the examples do not name, that is a loop too. Follow it.

1. **Personas — are we advertising to the right people?** Read targeting from every angle at once. Who the brand is targeting now, both on purpose and where the algorithm actually delivers. Who its competitors are targeting, and who their creative says they want. Who the customer thinks the product is for, read from who reviewers recommend it to, buy it for, and describe themselves as. Who is missing — a buyer the data keeps surfacing that the creative never speaks to, a persona nobody in the category serves. And new use cases surfacing from a creator, a reviewer, or a comment thread that imply a buyer the brand has never named. The current targeting being right is a loop and being wrong is a loop. Highest-stakes territory, because the answer routes nearly everything downstream.

2. **Product — are we advertising the right product, in the right way, and does it make business sense?** The economics: which product leads, what the LTV looks like, whether the SKU the ads push is the one the business should be growing. The buyer journey: where people actually find this product, how a new buyer would discover it, whether discovery runs on word of mouth, retail shelf, search, social, or the feed, and where that journey leaks. Product sentiment: what people genuinely love, what they keep reaching for, what they quietly stop using. New use cases: ways people have started using the product that the brand never designed for or advertised, surfaced from a review, a comment thread, or a creator — a new job the product does, an occasion it has slipped into — each a possible new line of demand the marketing has never spoken to. This is the use case as a new application for the product, distinct from the personas read of whether it implies a new buyer. And persona fit: whether the product the advertising leads with is reflective of the personas the brand is targeting.

3. **Messaging — what is actually being said and shown?** The broadest territory, and the most observational: watch what the messaging is and is not, with curiosity. Read in three layers. The creative layer: the visuals, what is on screen, how the product is demonstrated and what the demonstration implies, the emotions the creative runs on, the pain points it speaks to, the claims it leads with. The language layer: what the brand says, what competitors say, what customers say and the exact adjectives they use, and where those three diverge. The volume layer: how much the brand is running and whether that is enough to learn from, how many winners it has found, what has been tried, and what has never been said.

4. **Creators and talent — who shows up on screen, and what does that say about the brand?** Whether the talent reflects the personas being targeted is the floor, not the whole territory. Who else should be on camera that never is. Who competitors are using as talent and what that choice is doing for them. What it says about the brand that these are the people showing up in its content. New angles or use cases a specific creator surfaces that the brand has never run. And the execution read: whether the brand has the right creators and talent to execute what personas, product, and messaging need, and where the gaps in the roster or the org sit.

The pull is the evidence that a loop is real and not a note. Name the pull on every loop and describe in one sentence how it fired — what specifically caught the eye and turned the observation into a question. The six pulls:

1. **Curiosity.** Parker encounters something unique — a category dynamic, a piece of customer language, a comparison, a competitor move, a cultural reference — that the rest of its context cannot yet explain. The pull is "what is this and why does it matter."
2. **Resonance.** Parker encounters something captivating — an emotional metaphor, a story inside a review, a clever piece of creative — and the loop is the why behind its strength. The pull is "this is good and I want to know why it works."
3. **Surprise.** Parker encounters something unexpected given all the context it holds. A number, a behavior, or a creative choice contradicts the prior the context built, and the size of that gap is the signal. The pull is "this is not what I would have expected."
4. **Tension.** Two sources disagree and cannot both be true as stated — brand self-image against delivery data, a claim against the reviews, a dashboard number against the story the team has been telling itself. The pull is "I want to know which is closer to right."
5. **Pattern.** The same thing keeps appearing across independent sources — a phrase, a use case, an objection, a competitor behavior. The pull is "this might be the start of something, and I want to see whether more evidence accumulates."
6. **Gap.** An absence where presence would be expected — a persona the brand has never tried, an angle that lives in the reviews but never in the ads, a lane nobody in the category runs. The pull is "there is data here, and nothing has ever been done with it."

The written form of a loop, in order: the observation in one or two sentences; the pull, named, with the one-sentence description of how it fired; the exact question; the justification — one or two sentences on why this is an open loop, meaning what would change for the brand if Parker answered it; and the territory tag. One open question per loop. Do not stack sub-questions or split into an either/or. Plain English a smart 13-year-old could understand. No jargon, no pre-specified test design, no future speculation — ask what signs exist today. No closure path, research plan, or media brief; closure belongs to the grading, hypothesis, and validation runs downstream.

Generation captures; grading decides. Do not pre-kill candidates here — a separate grading pass collects every doc's loops, consolidates them, scores them on the four weights, and routes what moves on. Only two checks apply at generation: an infrastructure item — a tooling gap, a data-pull failure, a missing source — routes to the data_limitations field instead of the loops, and an observation with no answerable question attached is a note, not a loop. Write every loop that carries a real pull and a real justification. If a territory is genuinely clean, leave it empty; never manufacture a loop to fill one.
<!-- open-loops-core:end -->

Doc-specific thinking lens. Loops on this doc cluster around personas the buyer data reveals that the brand has never served, around the served-versus-actual gap the central diagnosis surfaces, around stated-versus-revealed divergences the synthesis could not resolve from the sources alone, around personas resting on a single source the cross-source agreement does not back, and around personas the team historically targeted that the data no longer supports. The source-side bias to hold throughout is that this is the synthesis layer, so any loop here should be one the source-side docs structurally cannot settle on their own; questions that belong inside a single source doc should stay there, and the loops promoted here are the ones whose answers route across the whole persona deck or across the served-versus-actual diagnosis.

Loops do not cover: source-sync timing, slug-registration housekeeping, missing day-in-the-life details, or any candidate already surfaced inside a source-side doc that has not been promoted to the synthesis-level question. Those belong in the frontmatter's data_limitations field, in operational routing, or in the source doc where they originated.

Mark any loop only the brand can answer so it routes to the brand; revenue-share, repeat-purchase, and lifetime-value questions almost always do.

## When you refresh this

The persona picture is the most volatile of the three one-pagers, so this doc refreshes on the most aggressive cadence, faster than the brand profile, driven by how often its source docs update. Post-purchase surveys, ad comments, and customer reviews accrue continuously; ad performance shifts in days; reputation drifts over weeks. When you rebuild it, take the previous version in as context first, carry forward the personas and slugs that still hold, update the behavioral-signal blocks as the customer base shifts without rewriting the durable identities beneath them, and re-run the served-versus-actual match. Add what is newly evidenced, downgrade or retire what the sources no longer support, and say what each open loop's status is now. Watch in particular for a new behavioral signal attaching to an existing persona, for an emerging persona crossing the evidence threshold into secondary, and for a persona quietly becoming a bias artifact as the data moves underneath it.
