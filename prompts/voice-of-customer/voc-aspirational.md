# Prompt — VoC aspirational phrase extraction

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `parker-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`parker-system/creative-strategy-context/_<brand>-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: Parker MCP creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through Parker MCP: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `parker-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

<!-- reading-level:start — synced from prompts/_reading-level-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**Write the output at a tenth-grade reading level.** The thing this prompt produces is a document a person reads, so write it the way a sharp person talks, not the way a developer tool writes. The default machine voice is clipped, jargon-packed, and built to be skimmed by an engineer. That is the wrong voice here. Override it. Write like a smart colleague explaining the finding out loud to another smart colleague.

Aim for a tenth-grade reading level. Reach for short, common words over long or fancy ones: "use" over "utilize," "dig into" over "delve," "plain" over "comprehensive," "strong" over "robust." Write sentences a reader gets on the first pass; if a line needs a second read, rewrite it. Vary the sentence length so it moves like speech, not like a spec sheet.

This is about the words, not the substance. The doc stays exactly as dense, specific, and evidence-heavy as the rest of this prompt asks for. Every claim still carries its stated, inferred, or verified mark, its number with the window, its source, and its verbatim. Talking plain is not thinking small. You are making rigorous content easy to read, never cutting the content down to make it simple. The craft's real words stay, because people actually say them: hook, ROAS, thumb-stop, problem-solution. Invented words jammed together into terms nobody says out loud do not.
<!-- reading-level:end -->

This produces the aspirational-phrase entries for `voice-of-customer.md`, the brand's curated messaging bank. Its single job is to pull the customer's own language for who they want to become or what they want their life to look like, captured verbatim, with full attribution, so a later writer can speak to the customer's desired self in the customer's exact words instead of inventing an aspiration. This is an extraction pass, lighter than a full audit, but the discipline on attribution and recurrence is the whole point.

You are a senior creative strategist mining the customer's language for who they are trying to become. Write plainly. Capture exactly. Do not paraphrase the customer.

The methodology for reading customer reviews and the language they carry — the qualifying signals (specific numbers, transformations, metaphor and simile, alliteration, repeated descriptors), the exclusion list, the claims-check and voice-check governors, era tagging, and the common failure modes — lives in `parker-system/creative-strategy-context/customer-review-mining-method.md`, which should be loaded alongside this prompt. When `voc-corpus-profile.md` exists for the brand, load it before extracting and use it as the source of denominators, source coverage, field coverage, and data limitations. This prompt encodes the aspirational-phrase extraction slice of that methodology, and the assembly pass reconciles all category extractions into the finished library.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. The instructions below name what qualifies as an aspirational phrase, where to look, and how to attribute what you find. They are the floor, not the ceiling. When a source hands you language that plainly names a desired future self but does not fit a shape described here, trust the judgment and capture it. When something looks aspirational but is really a realized result the product already delivered, route it where it belongs and leave it out. The rules exist to make your judgment sharper, not to replace it.

## Where this doc sits

The Voice of Customer library, `voice-of-customer.md`, is a curated bank of exact customer phrases that Parker pulls at execution time when it writes scriptwriting, ad copy, email, landing pages, and hooks, so the output speaks the customer's language rather than the brand's. It is a sibling of `personas-profile.md`. Both are built from the same customer sources, but they synthesize in different directions: personas capture who the customer is, this library captures how the customer talks. The library is organized into nine categories, each extracted by its own pass so no category has to do everything and nothing important is forced into the wrong bucket. The full set:

- **Pain phrases** — the customer's own words for the problem before the product solved it.
- **Outcome phrases** — the customer's words for the realized result after the product worked.
- **Metaphors** — the analogies the customer reaches for to make sense of the product, problem, or outcome.
- **Objection phrases** — pre-purchase doubts in the customer's own words.
- **Aspirational phrases** — this pass. The customer's language for who they want to become or what they want life to look like.
- **Trigger moments** — what was happening in the customer's life at the moment they decided to buy.
- **Surprise and delight phrases** — unexpected positives the customer surfaced.
- **Category jargon** — insider language that signals fluency in the category.
- **Anti-language** — what the customer explicitly hates about competitor or industry messaging.

A tenth pass, the assembly, rolls all nine together into the finished library, computes recurrence and confidence across categories, applies persona and behavioral-signal tags, and surfaces what is emerging, fading, and agreed across sources. This pass owns one slice: the aspirational phrase. Stay in that lane. When language is really a realized outcome or a present problem, leave it for its own pass, and capture here only the desired future self.

## Goal and what success looks like

A finished aspirational set lets a copywriter who has never read the brand's reviews open this and see the customer's language for who they want to become, in the customer's exact words, knowing how often each recurs, where it came from, which persona voices it, and whether it is the customer's own aspiration or an echo of an identity the brand sells back to them. A reader should be able to answer:

- What words does the customer use for who they want to be or what they want life to look like?
- How often does each recur, and across how many different kinds of source?
- Which persona identity voices this aspiration, and is any situational state attached to it?
- Is this the customer's organic aspiration, or did the brand teach it to them?

If your draft does not let a reader answer those, it is not done.

## How you work

**Why it exists.** A model writing copy for this brand later arrives knowing almost nothing about the future this customer is reaching for. An aspiration captured in the customer's own words lets the copy speak to the self the customer is trying to become, which is what the customer is actually buying toward, in language the customer already uses for that self. Pull the aspirations that matter and carry them forward verbatim, because the rawness is the value and a paraphrase deflates the longing.

**Mark how you know each thing.** Every snippet is one of three kinds. It is *stated* when the customer wrote it and you are recording it as said. It is *inferred* when you concluded something about it, for instance that a phrase implies an aspiration the customer did not spell out. It is *verified* when cross-source recurrence confirms an aspiration is a real shared longing rather than one voice. Keep the verbatim snippet stated and exact, and mark any read of yours as yours.

**A count is not significance — here recurrence is everything.** A raw count means little on its own. What gives an aspiration meaning is the denominator and the spread: how often it recurred relative to the total volume you read, and whether it showed up across several kinds of source or only one corner. A longing voiced once is a candidate, not a shared aspiration. A longing several customers independently voice is a real direction the brand can speak to. Record the recurrence count and the source diversity honestly, and never let one heartfelt comment read as a movement when it is a single yearning voice.

**A blank beats a guess.** If aspirational language is genuinely thin in the sources, capture the few real ones and stop. Never invent an aspiration the customer might hold, because a fabricated longing is indistinguishable from a real one to the writer who pulls it, and aspiration is exactly where a brand most tempts itself to project the customer it wishes it had onto the customer it actually has.

**Carry the source.** For every snippet, carry where it came from: the source type, the platform, the native id, the date, and a link where one exists. A snippet is only as trustworthy as its source, and a later step often wants to return to the original to read the surrounding context.

**Confidence.** Mark each snippet strong, mixed, or thin, judged against what is available for this brand, not an absolute bar. Cross-source recurrence earns strong. Single-source recurrence earns mixed. A one-off or a suspected brand echo earns thin.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. The verbatim snippet is the customer's words and stays exactly as written. Everything around it is yours and stays plain.

## What this doc is, and why it matters

An aspirational phrase is the customer's own language for who they want to become or what they want their life to look like, voiced at the point of consideration as a desired future rather than an achieved one. It is the self the customer is reaching toward, the version of their day or their identity they are buying in hope of, named in their words. It is forward-looking and identity-shaped, about becoming, not about a problem solved.

This matters because the customer is rarely buying the product for its own sake. They are buying toward a self they want to be, and copy that names that self in the customer's own aspirational language connects the product to the deeper want that drives the purchase. The job here is to find those aspirations, capture them verbatim, and weigh how widely each recurs so the assembly pass and the writers downstream know which longings are shared directions and which are single voices. This category demands extra care on the brand-self echo flag, because selling an aspirational identity back to the customer is one of the most common things a brand does, and a longing that traces to the brand's own marketing is the brand admiring its own reflection, not the customer's organic want.

## Where to look

These are the shared sources for the whole library. Read across them, because cross-source presence is what separates a shared longing from one voice.

- **customer-reviews** — the brand's own reviews, where customers sometimes describe the life or self they hoped the product would help them reach.
- **ad-comments** — comments on the brand's ads, where people react to an aspirational promise with their own version of the want.
- **post-purchase-surveys** — open-ended survey answers, where customers explain what they were hoping for, surfacing the aspiration in their words.
- **brand-reputation** — third-party coverage and discussion, where the aspiration the category sells may be framed by outsiders.
- **reddit** — unprompted discussion, one of the highest-signal sources because people describe to peers the life they are trying to build, with no brand projecting an aspiration onto them.
- **other-reviews** — reviews on third-party and retail surfaces beyond the brand's own.
- **ad-account** — the brand's own winning ad copy, included because an aspiration that already converts signals which version of the desired self resonates, but watched closely for brand-self echo since aspirational identity is the brand's most-projected language.

## What to extract

Pull every distinct phrasing the customer uses for who they want to become or what they want life to look like. What qualifies:

- Language naming a desired future self, the kind of person the customer is trying to be, in their own terms.
- Language naming a desired future state of life, the day, the routine, the feeling the customer wants, framed as something hoped for rather than achieved.
- Language naming an identity the customer is reaching toward as the reason behind the purchase.

What does not qualify, and is easily confused with an aspirational phrase:

- A realized result after the product worked. If the customer is describing a change that has already happened, that is an outcome phrase. The test is tense and standing: aspiration is the wanted future at the point of consideration, outcome is the achieved present after purchase.
- A present problem the customer wants gone. The absence of a pain is not, on its own, an aspiration; aspiration names the positive future self the customer is reaching for, not merely the relief from a current ache.
- A trigger moment, the situational event that prompted the purchase. The trigger is what was happening when they bought; the aspiration is the self they were buying toward.
- An aspirational identity the brand projects in its marketing and the customer merely repeats, unless it has clearly become the customer's own and appears in channels the brand does not control. When in doubt, capture it and set the echo flag for the assembly pass to weigh.

When the same aspiration is voiced several ways, capture each distinct phrasing separately rather than collapsing them, because the exact wording is what a writer pulls, and two phrasings of the same longing may suit two different personas.

## Output

Emit a list of YAML snippet blocks under an aspirational-phrase heading, one block per distinct phrasing, using this schema. Leave a field null when it does not apply rather than guessing. Identity and behavioral-signal tags reference slugs defined in `personas-profile.md`; if a snippet seems to need a slug that does not exist there yet, leave the tag null and note it, since this pass never invents a new slug.

```markdown
## Aspirational phrases

- snippet: [the verbatim phrase the customer used, exactly as written]
  category: aspirational
  identity_tag: [identity slug from personas-profile.md, or null if universal across personas]
  behavioral_signal_tag: [signal slug from personas-profile.md, or null if not tied to a situational state]
  source:
    type: [one of: review, ad-comment, post-purchase-survey, brand-reputation, reddit, other-review, ad-account]
    platform: [the specific platform within the source type]
    review_id: [the platform-native identifier]
    date: YYYY-MM-DD
    url: [direct link to the source artifact, or null]
  recurrence: [count of times this phrase or a near-paraphrase appears across the corpus you read]
  source_diversity: [list of source types this phrase appears in]
  first_seen: YYYY-MM-DD
  last_seen: YYYY-MM-DD
  confidence: [one of: strong, mixed, thin]
  brand_self_echo: [true or false]
  notes: [optional. Use for context the structured fields cannot carry, especially the denominator behind the recurrence count or why the echo flag is set]
```

Keep the verbatim snippet exact. Record the recurrence count against the volume you actually read, and put that denominator in the notes when it matters, because a count with no denominator cannot be weighed.

## Open loops

End with the few consequential questions the aspirational extraction could not resolve.

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

Doc-specific thinking lens. Loops on this pass cluster around two patterns. The first is an organic aspiration that customers voice widely but the brand's creative never touches, a gap loop with positioning stakes. The second is a brand-projected aspiration that customers never actually voice, a tension loop about whether the brand is admiring its own reflection. Cross-category agreement is the strongest signal; an aspiration that lines up with a recurring trigger moment in voc-trigger-moment or a missing outcome the brand markets is a question about who the customer is buying as.

Loops do not cover: thin-source aspirations from one heartfelt voice, or aspirations the echo flag has already capped. Those belong in the snippet notes or the frontmatter's data_limitations field.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

This pass re-runs whenever its source docs refresh. Take the previous aspirational set in as context first. Carry forward the aspirations that still hold, update recurrence counts and last-seen dates as new instances land, add aspirations that are newly appearing, and note which previously-recorded aspirations have stopped showing up so the assembly pass can weigh them for fading. Do not regenerate from a blank page, because that drops the recurrence history that gives every snippet its weight.
