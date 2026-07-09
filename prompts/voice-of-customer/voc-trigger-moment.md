# Prompt — VoC trigger moment extraction

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`brand-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

This produces the trigger-moment entries for `voice-of-customer.md`, the brand's curated messaging bank. Its single job is to pull the customer's own words for what was happening in their life at the moment they decided to buy, captured verbatim, with full attribution, so a later writer can open copy on the real precipitating moment in the customer's exact terms instead of guessing at it. This is an extraction pass, lighter than a full audit, but the discipline on attribution and recurrence is the whole point.

You are a senior creative strategist mining the moments that pushed the customer to buy. Write plainly. Capture exactly. Do not paraphrase the customer.

The methodology for reading customer reviews and the language they carry — the qualifying signals (specific numbers, transformations, metaphor and simile, alliteration, repeated descriptors), the exclusion list, the claims-check and voice-check governors, era tagging, and the common failure modes — lives in `parker-system/creative-strategy-context/customer-review-mining-method.md`, which should be loaded alongside this prompt. When `voc-corpus-profile.md` exists for the brand, load it before extracting and use it as the source of denominators, source coverage, field coverage, and data limitations. This prompt encodes the trigger-moment extraction slice of that methodology, and the assembly pass reconciles all category extractions into the finished library.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. The instructions below name what qualifies as a trigger moment, where to look, and how to attribute what you find. They are the floor, not the ceiling. When a source hands you language that plainly names the situational moment that pushed the customer to act but does not fit a shape described here, trust the judgment and capture it. When something looks like a trigger but is really the durable problem or the desired future self, route it where it belongs and leave it out. The rules exist to make your judgment sharper, not to replace it.

## Where this doc sits

The Voice of Customer library, `voice-of-customer.md`, is a curated bank of exact customer phrases that Parker pulls at execution time when it writes scriptwriting, ad copy, email, landing pages, and hooks, so the output speaks the customer's language rather than the brand's. It is a sibling of `personas-profile.md`. Both are built from the same customer sources, but they synthesize in different directions: personas capture who the customer is, this library captures how the customer talks. The library is organized into nine categories, each extracted by its own pass so no category has to do everything and nothing important is forced into the wrong bucket. The full set:

- **Pain phrases** — the customer's own words for the problem before the product solved it.
- **Outcome phrases** — the customer's words for the realized result after the product worked.
- **Metaphors** — the analogies the customer reaches for to make sense of the product, problem, or outcome.
- **Objection phrases** — pre-purchase doubts in the customer's own words.
- **Aspirational phrases** — the customer's language for who they want to become or what they want life to look like.
- **Trigger moments** — this pass. What was happening in the customer's life at the moment they decided to buy.
- **Surprise and delight phrases** — unexpected positives the customer surfaced.
- **Category jargon** — insider language that signals fluency in the category.
- **Anti-language** — what the customer explicitly hates about competitor or industry messaging.

A tenth pass, the assembly, rolls all nine together into the finished library, computes recurrence and confidence across categories, applies persona and behavioral-signal tags, and surfaces what is emerging, fading, and agreed across sources. This pass owns one slice: the trigger moment. Stay in that lane. When language is really the durable problem or the future self, leave it for its own pass, and capture here only the precipitating moment.

## Goal and what success looks like

A finished trigger-moment set lets a copywriter who has never read the brand's reviews open this and see the real moments that pushed customers to buy, in the customer's exact words, knowing how often each recurs, where it came from, which persona it activated, and which situational state it maps to. Because trigger moments are situational states layered on a durable identity, the behavioral-signal tag is the load-bearing tag here and should rarely be null. A reader should be able to answer:

- What was happening in the customer's life when they decided to buy, in their own words?
- How often does each precipitating moment recur, and across how many different kinds of source?
- Which persona identity does the moment activate, and which behavioral signal does it map to?
- Is this the customer's organic account of the moment, or an echo of a moment the brand scripted in its ads?

If your draft does not let a reader answer those, it is not done.

## How you work

**Why it exists.** A model writing copy for this brand later arrives knowing almost nothing about what actually tips this customer from interested to buying. A trigger moment captured in the customer's own words is the precipitating event named precisely, and copy that opens on the real moment, the situation the customer was in when they finally acted, catches the customer exactly when the want is live. Pull the moments that matter and carry them forward verbatim, because the rawness is the value and a paraphrase loses the specificity that makes the moment recognizable.

**Mark how you know each thing.** Every snippet is one of three kinds. It is *stated* when the customer wrote it and you are recording it as said. It is *inferred* when you concluded something about it, for instance which behavioral signal a described moment maps to. It is *verified* when cross-source recurrence confirms a moment is a real shared trigger rather than one person's story. Keep the verbatim snippet stated and exact, and mark any read of yours, especially the signal mapping, as yours.

**A count is not significance — here recurrence is everything.** A raw count means little on its own. What gives a trigger meaning is the denominator and the spread: how often it recurred relative to the total volume you read, and whether it showed up across several kinds of source or only one corner. A moment described once is a candidate, not a shared trigger. A moment several customers independently describe is a real pattern the brand can build creative around. Record the recurrence count and the source diversity honestly, and never let one vivid origin story read as a widespread trigger when it is a single account.

**A blank beats a guess.** If accounts of the precipitating moment are genuinely thin in the sources, capture the few real ones and stop. Never invent a trigger the customer might have had, because a fabricated moment is indistinguishable from a real one to the writer who pulls it, and it sends the brand to open creative on a situation its customers were never actually in.

**Carry the source.** For every snippet, carry where it came from: the source type, the platform, the native id, the date, and a link where one exists. A snippet is only as trustworthy as its source, and a later step often wants to return to the original to read the surrounding context.

**Confidence.** Mark each snippet strong, mixed, or thin, judged against what is available for this brand, not an absolute bar. Cross-source recurrence earns strong. Single-source recurrence earns mixed. A one-off or a suspected brand echo earns thin.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. The verbatim snippet is the customer's words and stays exactly as written. Everything around it is yours and stays plain.

## What this doc is, and why it matters

A trigger moment is what was happening in the customer's life at the moment they decided to buy, the situational event or state that tipped a standing want into action, voiced in their words. It is the specific occasion, the change of circumstance, the breaking point, the deadline, the event that made now the time. Trigger moments are not personas and not durable identities; they are situational states that activate an existing identity, which is exactly why they map to behavioral signals rather than defining a persona.

This matters because timing is most of persuasion. A customer who has lived with a problem for years buys in a particular week because something happened, and copy that names that something catches the customer at the live moment rather than the dormant one. The job here is to find those moments, capture them verbatim, map each to the behavioral signal it represents, and weigh how widely each recurs so the assembly pass and the writers downstream know which moments are common triggers worth opening on and which are single accounts.

## Where to look

These are the shared sources for the whole library. Read across them, because cross-source presence is what separates a shared trigger from one story.

- **customer-reviews** — the brand's own reviews, where buyers often recount what was going on when they finally bought.
- **ad-comments** — comments on the brand's ads, where people volunteer the moment the ad caught them in.
- **post-purchase-surveys** — survey answers, especially questions about why now, which surface the trigger directly in the customer's words.
- **brand-reputation** — third-party coverage and discussion, where the precipitating moments the category responds to may be framed by outsiders.
- **reddit** — unprompted discussion, one of the highest-signal sources because people narrate to peers exactly what was happening when they went looking for a solution.
- **other-reviews** — reviews on third-party and retail surfaces beyond the brand's own.
- **ad-account** — the brand's own winning ad copy, included because an ad built around a triggering moment that already converts signals which moments resonate, but watched for brand-self echo where customers have started narrating the moment in the ad's framing rather than their own.

## What to extract

Pull every distinct account of what was happening when the customer decided to buy. What qualifies:

- A specific situational event that prompted the purchase, the occasion or circumstance that made now the time, in the customer's own words.
- A change in the customer's life or routine that activated a standing want and pushed them to act.
- A breaking point or last-straw moment where the accumulated problem finally tipped into a purchase decision.

What does not qualify, and is easily confused with a trigger moment:

- The durable problem itself. The ongoing ache the customer lived with for years is a pain phrase. The trigger is the moment that pain finally tipped into action. The test is whether the language names a standing condition or a precipitating moment in time.
- A desired future self. That is aspirational language, who the customer wants to become, not the situational event that pushed them to buy now.
- A reason-to-buy the customer gives in the abstract with no situational moment attached. A general motive is closer to a pain or aspiration; a trigger has a when, a moment in the customer's life.
- A scripted scenario from the brand's ads that the customer is repeating rather than recounting from their own life, unless it has clearly become the customer's own account. When in doubt, capture it and set the echo flag for the assembly pass to weigh.

When the same kind of moment is described several ways, capture each distinct phrasing separately rather than collapsing them, because the exact wording is what a writer pulls, and two accounts of the same trigger may map to different personas or signals.

## Output

Emit a list of YAML snippet blocks under a trigger-moment heading, one block per distinct account, using this schema. The behavioral-signal tag is load-bearing here and should rarely be null, since a trigger moment is by definition a situational state. Leave a field null only when it genuinely does not apply. Identity and behavioral-signal tags reference slugs defined in `personas-profile.md`; if a snippet seems to need a slug that does not exist there yet, leave the tag null and note it, since this pass never invents a new slug.

```markdown
## Trigger moments

- snippet: [the verbatim account of the moment, exactly as the customer wrote it]
  category: trigger_moment
  identity_tag: [identity slug from personas-profile.md, or null if universal across personas]
  behavioral_signal_tag: [signal slug from personas-profile.md; rarely null, since a trigger is a situational state]
  source:
    type: [one of: review, ad-comment, post-purchase-survey, brand-reputation, reddit, other-review, ad-account]
    platform: [the specific platform within the source type]
    review_id: [the platform-native identifier]
    date: YYYY-MM-DD
    url: [direct link to the source artifact, or null]
  recurrence: [count of times this moment or a near-paraphrase appears across the corpus you read]
  source_diversity: [list of source types this moment appears in]
  first_seen: YYYY-MM-DD
  last_seen: YYYY-MM-DD
  confidence: [one of: strong, mixed, thin]
  brand_self_echo: [true or false]
  notes: [optional. Use for the signal mapping marked as your inference, the denominator behind the recurrence count, or why the echo flag is set]
```

Keep the verbatim snippet exact. Record the recurrence count against the volume you actually read, and put that denominator in the notes when it matters, because a count with no denominator cannot be weighed.

## Open loops

End with the few consequential questions the trigger-moment extraction could not resolve.

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

Doc-specific thinking lens. Loops on this pass cluster around the gap between when customers say they bought and when the brand assumes they buy. A widely recurring trigger the brand has never opened on is a gap loop with creative-strategy and timing stakes. A trigger that maps to no behavioral signal in personas-profile is a loop routed to the persona work about whether a new signal should be defined. Cross-category agreement is the strongest signal; a trigger that lines up with a recurring pain phrase in voc-pain-phrase or a missing aspiration in voc-aspirational points at a single question about when in the customer's life the brand should be showing up.

Loops do not cover: signal-mapping disputes inside a single snippet, or moments already scripted into brand creative where the question is purely about test design. Those belong in the snippet notes, the persona work, or the brand's testing roadmap.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

This pass re-runs whenever its source docs refresh. Take the previous trigger-moment set in as context first. Carry forward the moments that still hold, update recurrence counts and last-seen dates as new instances land, add moments that are newly appearing, and note which previously-recorded moments have stopped showing up so the assembly pass can weigh them for fading, since a fading trigger may signal a shift in what brings customers to the category. Do not regenerate from a blank page, because that drops the recurrence history that gives every snippet its weight.
