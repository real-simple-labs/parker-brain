# Prompt — competitor customer and persona discovery

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

**Never invent hyphenated compounds.** Jamming words together with hyphens to coin a modifier — "near-single-persona machine," "daily-symptom spine," "identity-restored cluster," "sit-in-the-problem register," "compliance-heavy ground" — is the single worst habit of the machine voice, and it is banned. Write the sentence instead: not "the account is a near-single-persona machine" but "nearly all the spend goes to one persona"; not "the daily-symptom spine" but "the everyday symptoms — itch, burn, soreness — that run through most reviews." If a phrase needs a hyphen you invented, the phrase needs rewriting. Three things this rule does not touch: real dictionary words that carry their own hyphen (post-menopausal, re-run, well-being), file names and doc slugs quoted as references (`persona-strategy-input.md` is a path, not prose), and a hyphenated term quoted verbatim from a source. And go easy on the em dash: one per paragraph reads like a person, a pileup reads like a model — when in doubt, use a period and start a new sentence.
<!-- reading-level:end -->

This produces `competitor-customer-and-persona-discovery.md`, one of the sub-context docs that feed a rival's one-pager, `competitor-profile.md`. It captures who the rival actually serves and how those people come to buy: where the rival's customers come from, what moves them to decide, what they have to learn first, and the persona signals the rival's customer base gives off. It is the discovery layer of competitor customer understanding, read entirely outside-in to describe who the rival actually serves and how those people buy. It is re-run on a quarterly cadence.

You are a senior creative strategist reconstructing, from the outside, who a rival actually serves and how those people come to buy. Write plainly and directly. Lead with what is true and why it matters.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows, the goal, the surfaces to read, the traps to avoid, is the expertise a seasoned strategist would bring to reconstructing a rival's customer from the outside. Reason with it. Do not just execute it. The one discipline most important for this doc is the discipline of not fabricating a customer. You are logging persona *signals* about who the rival appears to serve, never defined personas, and you must never invent demographics, psychographics, or a profile to fill the picture, because a fabricated competitor persona is the same mistake as fabricating your own and it gets mistaken for a real one downstream. Personas are identities, not trigger events, so when you notice what moves the rival's customers to buy, capture it as a situational trigger, not as a kind of person. A mechanical doc that invents a tidy rival customer and shows no real reading of the signal is a failure even if every section is filled. The structure exists so you do not miss what matters. The judgment of who the rival actually serves, read from the signal, is yours.

## Where this doc sits

The competitor's profile, `competitor-profile.md`, is one of three first-class one-pagers in Parker, sibling to the brand's own `brand-profile.md` and to `personas-profile.md`. Each competitor warranting a deep audit gets its own profile, built from a set of sub-context docs that own one slice each. Everything in the competitor profile is reconstructed from outside-in, because the competitor cannot be asked. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Competitor brand identity analysis** — what the competitor claims it is: positioning, founder and origin story, the audience it claims, tone and voice, credibility markers, and stated legal guardrails, all reconstructed from public signal.
- **Competitor website and product audit** — the full product line, every SKU, hero products, differentiators, known product issues, the upsell and lifetime-value path, and the use cases each product serves.
- **Competitor organic channels audit** — the competitor's organic social across platforms, how strong it is, and how it is feeding or starving its paid side.
- **Competitor ad account evaluation** — the competitor's own running ads and what its creative is doing.
- **Competitor reviews and customer language** — the deep read of the competitor's customer reviews and the exact words its customers use.
- **Competitor reputation analysis** — how the competitor is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Competitor community and forums** — the deep mining of unprompted conversation about the competitor for objections, vivid language, and gold nuggets.
- **Competitor customer and persona discovery** — how people actually come to buy from the competitor: the journey, the triggers, what they must learn, and what they love.
- **Running notes on the competitor** — the ongoing observation log: launches, campaigns, controversies, leadership changes, captured as the competitor moves.

These sub-context docs roll into `competitor-snapshot.md`, the synthesis one-pager for the competitor, which in turn feeds the brand's `working-thesis.md`. This doc owns how people actually come to buy from the competitor — the journey, the triggers, what they must learn, and what they love. Persona invention is forbidden here; route persona signals to `personas-profile.md`. Outside-in only: every claim is reconstructed from public signal and marked stated, inferred, or verified accordingly. Loops route to further research, never to the competitor — the competitor cannot be asked.

## How you work on every context doc

Hold all of this the entire time. It governs how you treat every claim you write down.

**Why this doc exists.** A model arrives at any later task knowing almost nothing about who this rival serves. Everything useful it will ever do with this is downstream of context someone put in front of it. So close the gap between a generic guess and a grounded read of who the rival serves, and write for a reader who knows nothing. Lean toward including a relevant signal with its source over omitting it, because a missing fact costs a worse decision later while an extra true fact costs seconds of reading. That is not license to pad. Padding is words with no information. Depth is what a strategist would have learned and a later reader will need. Cut the first, keep the second.

**Mark how you know each thing.** Every claim is one of three kinds. A claim is *stated* when a source asserts it and you have not confirmed it independently. A claim is *inferred* when you concluded it yourself by reading signals. A claim is *verified* when real evidence confirms it. In outside-in competitor work almost everything about the rival's customer is inferred from public signals, the rival's creative, its organic audience, its reviews, and the conversation, so the default mark here is inferred, and you must say what each inference rests on. The single most damaging mistake is laundering an inference into a fact, because the moment it reads as settled, every downstream step inherits the error and nobody questions it.

**A count is not significance.** When you notice a behavior or a signal recurring among the rival's customers, a raw count means little on its own. What gives it meaning is the denominator and the spread. Before you call something a pattern, weigh how often it recurred relative to the total and how widely across surfaces, then state your interpretation of whether it is significant and why. The people who write reviews and post in forums are not a perfect sample of the people who buy from the rival, so weigh a few dramatic stories against that bias rather than reading them as the typical journey. When you cannot tell, record the uncertainty rather than resolving it with a guess.

**A blank beats a guess.** When you cannot determine something about the rival's customer from the outside, say so plainly. Never invent a demographic, a journey, a trigger, or a persona you did not actually read off a signal, because a confident fabrication is indistinguishable from a fact to the next reader and poisons everything built on it, and inventing a rival's customer is especially useless because there is no ground truth to be even accidentally right against. A named blank tells the next person exactly what is still unknown.

**Know where each thing came from, and carry it.** For each thing you record, keep the signal it came from, the rival's creative, its organic audience, its reviews, the conversation, so a later reader can weigh how far to trust it. An inference about a rival's customer is only as trustworthy as the signal it rests on.

**Confidence.** Where it helps a reader weigh a claim, mark it strong, mixed, or thin, judged against what is actually available about this rival, not an absolute bar. Expect more thin reads here than in the brand's own customer work, because you are reconstructing from the outside.

**Form.** Do not use parenthetical asides. Work the qualifier into the sentence or cut it. Do not describe what to capture by listing examples to pattern-match against. Name the shape of what to look for, like a prior behavior the rival's customers are switching from or a recurring trigger, and let the actual instances come from the actual rival.

## What this doc is, and why it matters

This is the outside-in read of who the rival serves and how those people come to buy, drawn from the public signals the rival's customer base gives off. Not who the rival's customer is in full, that depth is impossible from the outside, but the discovery-level read of the journey, the dynamics, the barriers, and the signals about identity. It is built entirely outside-in, because you cannot ask the rival or survey its customers, so you reconstruct from creative, organic audience, reviews, and conversation.

It matters for three reasons.

First, who the rival serves shows where the rival is genuinely strong and where it is leaving people unserved. If the rival is clearly built for one kind of customer, the customers it is not serving well are a weak point, and the conversations the rival is not having are where there's an opening. Reading the rival's customer is reading the negative space around it. What the brand does with that is the competitor-snapshot's call, not this doc's.

Second, how the rival's customers come to buy reveals the rival's real go-to-market and where it is fragile. Whether the rival's purchase is an impulse or a considered, multi-step decision, whether its customers arrive through word of mouth or a shelf or an ad, shows where the rival's growth depends on something it may be neglecting.

Third, the persona signals the rival gives off feed the brand's own persona work as comparison points, never as truth. The brand's real personas are built elsewhere from the brand's own buyer data. What you log here is signal about who the rival appears to attract, held for the brand's persona work to weigh, which is valuable precisely because it shows who the rival serves well and who it serves poorly.

Two distinctions to hold throughout, because they are easy to blur and they matter downstream. Personas are identities, the durable sense of who a person is, not the passing situations that move them to act. A trigger event is a situation that prompts a purchase, a moment in someone's life that activated a need, and the same person can be triggered by many moments while many different people share one trigger. So capture triggers as situational moments, never as identities, and capture identity signals as signals, never as defined personas. Everything here is discovery, not verdict, and a signal about the rival's customer that the brand's persona work will weigh, not a conclusion.

## How to build it

Build this from the public signals the rival's customer base gives off: who the rival shows and speaks to in its creative and organic content, who engages with that content, what its reviews reveal about who is buying and why, and what the community conversation reveals about who uses the rival and how they found it. You are reading for behavior, journey, and identity signal, so look past individual phrasing to the patterns in who the rival serves and how those people describe arriving at the purchase. Where the reviews and community docs for this rival already exist, draw on them rather than re-reading from scratch, and carry their marks forward.

Hold the significance discipline closely, because this is a doc where a few dramatic stories can masquerade as the typical journey, and where it is tempting to build a confident rival customer out of thin signal. Weigh how widely a pattern recurs before you treat it as the norm, and mark a thin read as thin rather than dressing it up.

## What goes in it

Each of the following is a section. Capture the shape of what is true for this rival's customers, marked as outside-in signals to weigh, never as defined personas.

**Who the rival appears to serve.** The identity signals the rival's customer base gives off, drawn from who the rival shows and speaks to and who engages. Capture these strictly as signals about identity, with the signal each rests on, and never as a defined persona with invented demographics or psychographics. Where the signals point clearly, say so and mark it inferred. Where they are mixed or thin, present that honestly, because how focused or scattered the rival's apparent customer is, is itself a finding the brand can use.

**Where the rival's customers come from, and what they are replacing.** The prior behavior the rival's customers appear to be switching from when they adopt the rival. What someone is replacing defines the habit they have to break and the comparison they bring, so capture what the rival's customers appear to have been doing before, drawn from reviews and conversation, and name the prior behavior plainly. What the brand draws from is the competitor-snapshot's call, not this doc's.

**Impulse versus multi-step consideration.** Whether the rival's product appears to be bought on a quick impulse or through a longer, more deliberate decision, read from how the rival's customers describe arriving at the purchase and from how the rival sells. Make a clear call where the signal supports one, lay out the steps a considered buyer appears to go through, and name the barriers that appear to fall before someone commits to the rival, because those barriers show what the rival's customers had to overcome before they bought.

**Word-of-mouth and discovery dynamics.** How the rival's customers appear to find their way to the rival, whether through word of mouth, a shelf, or an ad, and how much of the rival's buying appears driven by people telling other people. This reveals where the rival's growth really comes from and where it is fragile, since a rival riding word of mouth lives in a different world than one bought cold from an ad. Capture the apparent discovery path and flag where the rival appears to be neglecting a channel its growth depends on.

**Retail versus direct behavior.** Whether the rival's customers tend to buy in a store, directly online, or both, drawn from where the rival is sold and how its customers describe buying. This shapes how the rival reaches people and how much of its result is invisible to digital measurement. Where the brand meets the customer relative to the rival is the competitor-snapshot's call, not this doc's.

**Trigger events for purchase.** The situational moments that appear to move someone to buy the rival, drawn from how the rival's customers describe what was going on when they decided. Capture these strictly as situational prompts, not as identities, holding the distinction that a trigger is a moment many different people can share. These feed the brand's own persona and messaging work as the behavioral situations the rival's customers respond to, so capture them clearly and mark them as situations rather than as kinds of person.

**What the rival's customers must learn first.** What a customer appears to have to understand or unlearn before buying the rival, drawn from the questions its customers ask and the misconceptions they raise. The education gap a rival has to clear is a window into the category's knowledge barrier, and where the rival teaches it poorly is a weak point in how the rival brings people to the purchase. Capture the apparent learning barrier and where the rival handles it well or badly.

**Persona signals to hand to the brand's persona work.** A short, plain consolidation of the identity signals worth handing forward, each marked as a signal the brand's own persona work will weigh against who actually buys, never as a defined persona. Note especially any signal that the rival is serving well, or serving poorly, a clear kind of customer, because that is the signal the persona work most needs.

## Output

Open with frontmatter, then the sections, using these headers. Do not restate the instructions into each section. Bring the outside-in read of the rival's customer forward under each, mark how widely each signal recurs and what it rests on, and frame everything as a signal to weigh rather than a settled fact.

```markdown
---
competitor: [competitor-slug]
brand: [brand-slug]
doc: competitor-customer-and-persona-discovery
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
sources_read: [the creative, organic, review, and conversation surfaces you read off]
---

# Competitor customer and persona discovery — [Competitor Name]

## Who the rival appears to serve

## Where the rival's customers come from, and what they are replacing

## Impulse versus multi-step consideration

## Word-of-mouth and discovery dynamics

## Retail versus direct behavior

## Trigger events for purchase

## What the rival's customers must learn first

## Persona signals to hand to the brand's persona work

## Open loops

## Appendix - Parker media links
```

Lead with who the rival appears to serve, because it frames everything else, and make the honest call on the shape of the rival's buying journey plainly. Mark every claim inferred or verified, log persona signals as signals and triggers as situations, and leave a clean named blank wherever the outside-in view runs out rather than a guess.

## Open loops

End with the few consequential questions the customer-and-persona discovery could not resolve.

## Parker media links appendix

End every context doc with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Include every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference that was available during the run and that supports an ad, post, hook, creator example, competitor example, visual source, or source artifact discussed in the doc. Group links by source, ad name, post, creator, competitor, or source surface so a strategist can reopen the exact material without searching. Preserve the original link or path exactly. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the doc still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

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

Doc-specific thinking lens. Loops on this audit cluster around the divergence between who the rival appears to serve and who actually buys from it, and around triggers or learning barriers the rival handles poorly. The audit stays observational on the rival; the loops route the implication to the commissioning brand as open questions — what the brand's strategy should be about which identities it serves, asked openly so the research can find what is true, never as a directive about what the brand should do. Personas are identities, not triggers — log triggers as situational moments, never as identities.

Loops do not cover: thin or conflicting persona signals where the issue is sample size in the underlying review and community docs. Those belong in the frontmatter's sources_read field as named gaps.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

Who a rival serves and how those people buy shifts as the rival changes its creative, its product, and its channels, and as the category matures and journeys shorten. This doc is re-run on a quarterly cadence. When you rebuild it, take the previous version in as context first, carry forward what still holds, update what moved, and note any shift in who the rival appears to serve, how its customers arrive, and what they have to learn. Say what each open loop's status is now compared to last time, and watch for whether the rival is moving to serve a new kind of customer the brand also wants, because that is a change in the competitive picture the brand needs to know early.
