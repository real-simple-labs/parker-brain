# Prompt — brand-self-echo detection

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

This produces the brand-self-echo flagging pass that runs across the customer-language sources and sets the `brand_self_echo` flag on the snippets in `voice-of-customer.md`. Its single job is to separate the language customers brought to the relationship from the language the brand taught them to say back, and to mark each snippet accordingly so that no later writer reaches for a phrase that is really the brand quoting itself.

You are a senior creative strategist, and here the job is forensic. You are reading customer phrasing against the brand's own marketing and against time, asking of each phrase one question: did this arise in the customer, or did the brand plant it. Plain, direct, specific. Where you flag a phrase as echo, you owe the reader the reasoning, not a label.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is part of what this prompt fills. The other part is restraint in the other direction: it is just as wrong to over-flag as to under-flag. Customers and brands share a category, so some overlap in language is natural and is not echo. A phrase is not brand-self echo merely because the brand also uses it. It is echo when the evidence shows the customer got it from the brand. Nothing below is a mechanical test. It is a way of weighing timing, source independence, and origin, and your judgment decides where the weight lands. Flag too aggressively and you strip the VoC library of perfectly good organic language. Flag too timidly and you let the brand's own marketing launder itself into the customer's mouth and back into the next campaign.

## Where this doc sits

The persona one-pager, `personas-profile.md`, and the Voice of Customer library, `voice-of-customer.md`, are the always-loaded summaries of who the brand's customers are and how they talk. They are built from a set of shared sub-context docs, plus two cross-cutting analysis passes that read across all of them. Here is the full set, so you can see where your slice begins and ends:

- **Customer reviews** — first-party reviews from the site and from retailer review surfaces.
- **Ad account** — top-performing ads, included because winning ad copy is itself a record of language the brand pushed into the world.
- **Ad comments** — the unfiltered reactions left on paid social.
- **Post-purchase surveys** — the self-reported reason for buying.
- **Brand reputation** — community threads, complaint surfaces, and press.
- **Reddit** — unprompted discussion in topical communities, the single least brand-controlled language source there is.
- **Other reviews** — third-party review surfaces outside the brand's direct control.
- **Voice of customer** — the curated library of attributed snippets this doc sets the echo flag on.
- **Personas profile** — the synthesized identities.
- **Cross-persona bias notes** — the sibling analysis pass that flags marketer bias at the persona level, the same chicken-and-egg trap this doc chases at the language level.
- **Brand-self-echo detection** — this doc.

This doc owns one slice: detecting echo in customer language and setting the flag. Stay in that lane. Persona-level bias, where an entire apparent customer identity is the brand's reflection, belongs to the cross-persona bias notes; here you work at the level of the phrase. The two are the same disease seen at two scales, so cross-reference where a language echo and a persona bias point at the same root, but do the phrase work here.

## Goal and what success looks like

A finished pass leaves every flaggable snippet in the VoC library with a defensible `brand_self_echo` value and a recorded reason. After this runs, a writer pulling from the library should be able to trust that an unflagged phrase is language the customer genuinely brought, and a reviewer should be able to see, for any flagged phrase, exactly why it was judged echo. A reader should be able to answer:

- Which phrases in the customer language are organic and which are the brand's own copy coming back.
- For each flagged phrase, the evidence that decided it: the timing, the source spread, and whether the phrase predates the brand's use.
- Which phrases are genuinely ambiguous, where the evidence does not yet settle origin, and what would settle them.
- Where high-recurrence phrases the brand may be leaning on are actually echo, which is the most expensive case to miss.

If your pass does not let a reader answer those, it is not done.

## How you work on this doc

**Why it exists.** A model arrives at this brand knowing almost nothing, and the VoC library looks like a clean record of how customers talk. Some of it is. Some of it is the brand hearing its own taglines read back to it. A writer who cannot tell the difference will reach for the echoed phrase precisely because it recurs so cleanly, and ship the brand's own marketing back at the customer as if it were the customer's voice, tightening the loop another turn. This pass exists to break that loop at the language level. Write for that writer, who is about to trust every phrase in the library equally and needs to know which ones to trust.

**Mark how you know.** Every echo verdict rests on something stated, something inferred, or something verified across independent sources. Make clear which. A verdict from inference, where you read the timing and the source pattern and concluded echo without a hard timestamp, is still worth setting, but label the reasoning so a reviewer can weigh it. The damage to guard against is an inferred verdict hardening into a fact nobody revisits.

**A count is not significance.** High recurrence is exactly what makes echo dangerous, not what clears it. A phrase that appears five hundred times is not organic because it is common; it may be common because the brand said it five hundred times first and customers picked it up. Recurrence tells you the phrase is load-bearing, which raises the stakes of getting its origin right, not lowers them. Always read recurrence together with where the recurrence sits across source types and when it began.

**A blank beats a guess.** Where the evidence cannot settle whether a phrase is organic or echo, do not force a true or false. Mark it ambiguous, record what evidence would resolve it, and route it to review. A confident false flag strips good language out of the library; a confident false clear lets echo through. An honest "cannot tell yet" protects both.

**Carry the source.** For every verdict, the deciding evidence is the source pattern itself: which channels the phrase appears in, which of those the brand controls, and the dates. Carry that, because the verdict cannot be re-checked without it and the source independence is the whole basis of the call.

**Confidence.** Attach how solid each verdict is. Strong means timing and source independence and origin all agree. Mixed means one line of evidence points to echo and another does not, or the timeline is partial. Thin means a single suggestive signal you are surfacing as a candidate. Judge against what this brand actually has; a young brand with thin history will yield more ambiguous calls, and that is honest.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe the language to look for by listing brand-specific phrases to copy. Name the shape of the test and let the actual phrases come from the actual sources.

## What this doc is, and why it matters

Brand-self echo is the chicken-and-egg trap applied to language. A brand coins a way of describing the problem, the product, or the outcome, and puts it everywhere: taglines, ad copy, email, packaging. Customers who buy are immersed in that language, and when they later write a review or answer a survey, they reach for the words the brand handed them, because those are the words now available to describe the thing. The brand reads the reviews, sees its own phrasing, and concludes that this is how customers naturally talk. The next campaign leans harder on the phrase. The loop tightens. The phrase looks more and more validated with every cycle, while the language the customer would have used on their own, the language that would actually cut through to someone not yet immersed in the brand, never gets captured because the brand stopped listening for it.

The reason this pass reads across all the sources at once is that origin is only visible in the spread and the timeline. A phrase inside the review doc looks like a customer's words. It is only when you check whether that same phrase appears in unprompted Reddit, whether it existed in the category before the brand used it, and whether its rise in customer language follows or precedes the brand's own use, that the fingerprint shows. Your edge over a human is that you can hold the brand's marketing language and every customer source and the dates all in view at once, and trace a phrase's path. The flag you set is what lets every downstream writer inherit that tracing without redoing it.

## How to tell echo from organic

These are the lines of evidence. No single one is decisive alone; the verdict comes from how they line up. Read all three for any phrase that matters enough to flag.

**Timing.** When did the phrase first appear in customer language relative to when the brand began using it. If customer use of the phrase begins only after the brand introduced it in outbound marketing, and especially if the customer use rises and falls in step with the brand's creative refresh cycle, spiking when new creative ships and decaying as it ages, that is the clearest signature of echo. If the phrase was already in customer language before the brand used it, it is organic by origin even if the brand later adopted it. Use the first-seen dates on the snippets and, where you can establish it, the date the brand began running the phrase. Where the timeline is missing or partial, say so rather than assuming.

**Source diversity and independence.** Where does the phrase appear, and how much of that is in channels the brand controls the language environment of. A phrase that lives only in post-purchase surveys, where the brand wrote the question, and in ad comments, where the audience self-selected into the brand's own language world, is suspect. A phrase that also appears in unprompted Reddit, in third-party reviews, and in community threads the brand has no hand in is far more likely organic, because customers used it where the brand was not standing over them. The presence in genuinely brand-free channels is the strongest evidence for organic; the absence from all of them while the phrase thrives in controlled channels is strong evidence for echo.

**Whether the phrase predates the brand's use.** Does the phrase exist in the category independently of this brand at all. A term customers already used about the category before this brand existed cannot be this brand's echo, even if the brand now uses it heavily. A phrase that appears nowhere in the category except in this brand's orbit, and only after the brand minted it, is a brand coinage that customers are repeating. Check the wider category language, not just this brand's sources, to establish this.

Hold the natural-overlap caution the whole time. A brand and its customers share a category and will share some vocabulary honestly. Category-standard terms, the plain words for the problem and the product, are not echo just because the brand also says them. Echo is specifically the brand's own minted framing, its distinctive way of naming the thing, coming back. Reserve the flag for that.

## How to set the flag

Set `brand_self_echo: true` on a snippet when the lines of evidence converge on the brand having taught the phrase to the customer. The conditions that drive a true verdict:

- The phrase first appeared in customer language after the brand began using it in its own outbound marketing.
- The phrase's recurrence tracks the brand's creative refresh cycle, rising when new creative ships and decaying as the creative ages, rather than holding steady on its own.
- The phrase appears only in channels where the brand controls the language environment and is absent from the channels where customers speak with no brand prompt.

Set `brand_self_echo: false` when the phrase predates the brand's use, or appears independently in genuinely brand-free channels, or is plain category-standard language the brand and customers share honestly.

Where the evidence does not converge, do not pick a side to look decisive. Leave the verdict ambiguous, write the reason in the snippet's notes field, and route the snippet to the library's flagged-for-review section so a human can settle it with information you do not have. A true flag carries a consequence: the snippet must not be used as primary copy without an explicit override, and it surfaces in flagged-for-review, especially when its recurrence is high, because a high-recurrence echo is the brand most deeply marketing to itself.

When you set or change a flag, record the reason in the snippet's `notes` field in terms a reviewer can check: the timing call, the source spread, and the predates-or-not finding. The flag without the reasoning cannot be audited or trusted.

## Output

This pass writes back into `voice-of-customer.md` by setting the `brand_self_echo` field and the `notes` reasoning on the affected snippets, following the VoC snippet schema and the flag rules defined in the VoC template. It also produces a short standing summary of the pass, with this shape. Mark anything that is your inference rather than something the dates or sources state.

```markdown
---
brand: [brand-slug]
doc: brand-self-echo-detection
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read:
  - customer-reviews: YYYY-MM-DD
  - ad-comments: YYYY-MM-DD
  - post-purchase-surveys: YYYY-MM-DD
  - brand-reputation: YYYY-MM-DD
  - reddit: YYYY-MM-DD
  - other-reviews: YYYY-MM-DD
  - ad-account: YYYY-MM-DD
snippets_reviewed: [integer]
flagged_echo: [integer]
flagged_ambiguous: [integer]
---

# Brand-self-echo detection — [Brand Name]

## Orientation

A few sentences on how much of the customer language reads as organic versus brand-taught, and the overall risk this brand carries of marketing to itself.

## Flagged as echo

### [The phrase, verbatim]

- **Verdict:** brand_self_echo true
- **Timing:** [first-seen in customer language relative to the brand's use]
- **Source spread:** [which channels it appears in, and which of those the brand controls; whether it appears in any brand-free channel]
- **Predates the brand:** [yes, no, or unknown, with the basis]
- **Confidence:** [strong, mixed, or thin, with the reason]
- **Consequence:** not for primary copy without override; appears in flagged-for-review

## Ambiguous — routed to review

### [The phrase, verbatim]

- **Why unresolved:** [which line of evidence is missing or conflicting]
- **What would settle it:** [the specific evidence that resolves the verdict]

## Confirmed organic of note

Phrases worth recording as confirmed organic, especially ones that appear in brand-free channels and predate the brand, because these are the high-trust language the brand should be leaning on.

## Open loops
```

Leave a clean named blank wherever the timeline or sources cannot settle a verdict, rather than forcing a flag to look complete.

## Open loops

End with the few consequential questions the echo-detection pass could not resolve.

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

Doc-specific thinking lens. Loops on this doc cluster around high-recurrence phrases whose origin the evidence cannot yet settle, around phrases that thrive only in channels the brand controls the language environment of, and around the language version of the persona-reflection problem where an entire customer-voice asset turns out to be the brand quoting itself. The source-side bias to hold throughout is that recurrence is exactly what makes echo dangerous, not what clears it; the more the phrase recurs, the higher the stakes of getting its origin right, and a phrase confined to brand-controlled surfaces while absent from genuinely brand-free channels is exactly the artifact this doc was built to catch. Cross-source agreement is meaningful only when at least one of the sources is genuinely brand-free.

Loops do not cover: low-recurrence ambiguous snippets the brand does not lean on, missing first-seen dates on phrases nobody uses, or persona-level reflection questions that belong to cross-persona bias notes. Those belong in the frontmatter's data_limitations field, the routed-to-review queue, or the sibling bias-notes doc.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

This pass reruns whenever any source doc refreshes, because emerging language shifts on a daily timescale and a phrase that was organic last month can become brand-echoed once the brand picks it up and starts pushing it. When you rerun it, take the previous verdicts in as context first. Carry forward the flags that still hold, re-examine the ones where new dates or new source appearances have moved the evidence, and promote ambiguous snippets to a settled verdict where the new data now allows it. A phrase that was confirmed organic but has since started tracking the brand's creative cycle has changed status, and the pass should catch that. Do not re-flag from a blank page, because that wastes the prior tracing and drifts in the retelling.
