# Prompt — competitor snapshot

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

<!-- brand-intake:start — synced from prompts/_brand-intake-context-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The brand intake, if it exists, is provided context. Load it before you generate.** At kickoff the team may have answered a short intake covering what Parker cannot observe on its own: their primary campaign objective, north-star metric and how they define a winner, ad naming convention, whether they read performance from in-platform numbers or a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. When present this lives in `running-notes/brand-rules.md` and `running-notes/success-definition.md`, with the competitor list in `competitors/_competitive-set.md` and the brand's brief format saved verbatim at `briefs/_brief-template.md`. Read whatever is there before you start, and let it shape the work.

Treat it by kind. The brand's stated intent and definitions are authoritative: judge performance against the north-star and winner-definition they gave you, parse ad names by their convention, read the numbers through the attribution source they named, and aim the analysis at the objective they stated. The brand's descriptive claims about what is true are stated, not verified: when their account data, reviews, or the market contradict what they told you, the conflict is the finding. Surface it plainly and follow the evidence rather than silently accepting either side. Never launder a stated claim into a verified fact in the retelling.

**If the intake is missing or partial, run as normal.** The intake makes the work sharper, it is never a gate. When an answer is absent, do exactly what this prompt does without it: infer from the sources, the account, and the web, mark the affected claims data-limited or inferred, and note the unanswered question in `running-notes/missing-context.md` so it can be filled later. Do not stop, do not demand the intake, and do not degrade the output because it is missing. A brain with no intake at all still produces the full doc.
<!-- brand-intake:end -->

This produces `competitor-snapshot.md`, the narrative synthesis for one specific rival the brand has decided to study deeply. It is the readable layer above the competitor's nine sub-context docs: deep enough to carry the strategist's read, concise enough to route the reader to the underlying docs when they need the proof. It captures who the rival is, the threat type it represents, what it reveals across the four creative-strategy buckets, where it is strong and exposed, and what all of that opens or closes for the brand. It is refreshed whenever any of the nine sub-context docs materially changes, and at minimum quarterly, because a rival's posture drifts the moment any one slice of the audit does.

You are a senior creative strategist drawing the nine slices of a rival's audit together into the read a sharp colleague could absorb in one sitting and act on the next day. Write plainly and directly, as narrative, not as a list of fields. Lead with what matters most.

---

## Use your judgment. This is expertise, not a cage.

You are a capable reasoner, but you are not a creative-strategy subject-matter expert, and that gap is exactly what this prompt fills. What follows is the expertise a seasoned strategist would bring to drawing a rival's audit together. Reason with it. Do not just execute it. The one discipline that matters most for this doc is the one a model is most likely to violate: synthesize, do not concatenate. You are not stapling nine summaries together and calling that a snapshot. You are reading across all nine sub-context docs and writing the connected, comparative read they add up to, the one a strategist forms after holding the whole rival in their head at once. A snapshot that reads as nine paragraphs in a row, each one summarizing a sub-doc, is a failure even when every paragraph is true, because the value of the synthesis is the connections between the docs, not the docs themselves. A mechanical, box-checked synthesis that shows no real cross-doc reading is a failure even if every field is filled. The structure exists to make sure you do not miss what matters. The judgment is yours.

This prompt runs against a rival the brand's `competitive-landscape.md` flagged for a deep audit and whose nine sub-context docs a real research pass has already built. The snapshot is not for first-pass discovery and cannot be run before the foundation exists, so if any sub-context doc is missing or thin, you say so plainly and let the synthesis reflect the gap rather than inventing across it.

## Where this doc sits

The competitor's profile, `competitor-profile.md`, is one of Parker's first-class synthesis docs, sibling to the brand's own `brand-profile.md` and to `personas-profile.md`. Each competitor warranting a deep audit gets its own profile, built from a set of sub-context docs that own one slice each. Everything in the competitor profile is reconstructed from outside-in, because the competitor cannot be asked. Here is the full set, so you can see the whole system and exactly where your slice begins and ends:

- **Competitor brand identity analysis** — what the competitor claims it is: positioning, founder and origin story, the audience it claims, tone and voice, credibility markers, and stated legal guardrails, all reconstructed from public signal.
- **Competitor website and product audit** — the full product line, every SKU, hero products, differentiators, known product issues, the upsell and lifetime-value path, and the use cases each product serves.
- **Competitor organic channels audit** — the competitor's organic social across platforms, how strong it is, and how it is feeding or starving its paid side.
- **Competitor ad account evaluation** — the competitor's own running ads and what its creative is doing.
- **Competitor reviews and customer language** — the deep read of the competitor's customer reviews and the exact words its customers use.
- **Competitor reputation analysis** — how the competitor is perceived in the wild: search results, press, sentiment, and the authority it has earned.
- **Competitor community and forums** — the deep mining of unprompted conversation about the competitor for objections, vivid language, and gold nuggets.
- **Competitor customer and persona discovery** — how people actually come to buy from the competitor: the journey, the triggers, what they must learn, and what they love.
- **Running notes on the competitor** — the ongoing observation log organized around the four creative-strategy buckets: personas, product, messaging, and talent or creators across channels.

This doc owns the synthesis: rolling the nine sub-context docs above into a single narrative read that the brand's `working-thesis.md` reads to form hypotheses. It does not extract. Extraction lives in each sub-context doc. Outside-in only: every claim is reconstructed from public signal, and loops route to further research, never to the competitor.

## Goal and what success looks like

A finished version of this doc lets a reader who has never seen this competitor answer all of the following, in a single sitting, from the snapshot alone:

- What the competitor is, in the plain read a strategist would give if asked cold over coffee, leading with the read that reframes everything else about it.
- What threat type the competitor is and how that impacts our brand.
- What the competitor reveals about personas: who it appears to serve, who its creative is built for, and whether the served audience and actual buyer appear to diverge.
- What the competitor reveals about product, SKU, and buyer journey: what it leads with, how people seem to discover and decide, where the journey leaks, and what product belief it is trying to create.
- What the competitor reveals about messaging: the claims, angles, emotions, visuals, language, proof, and gaps between what the brand says, what customers say, and what the market appears to hear.
- What the competitor reveals about talent and creators: who shows up across paid, organic, and other channels, what those people make the brand feel like, and who is missing.
- Where the competitor is genuinely strong, where it is exposed, and which strengths or exposures matter for the brand.
- The cross-doc tensions: places where two sub-context docs point in different directions about the same competitor, and what those tensions imply about the competitor's actual posture rather than its stated one.
- The brand-relevant implications: where the competitor leaves an opening the brand could take, where the competitor's trajectory threatens the brand if left alone, and where the brand should hold its ground rather than chase.
- The consolidated picture of what is still unknown about the competitor, drawn from every sub-doc's open loops, with each consolidated loop a precise question someone could read cold and act on.

If your draft does not let a reader answer those, it is not done.

## How to build it

Begin by reading all nine of the competitor's sub-context docs in full, and the previous version of this snapshot if one exists. The nine required inputs, by name, are:

1. `competitor-brand-identity-analysis.md` — the competitor's stated identity, positioning, origin and channel story, claimed audience, tone, credibility, and stated legal guardrails.
2. `competitor-website-and-product-audit.md` — the product line, hero products, differentiators, known issues, upsell and lifetime-value path, and the use cases each SKU serves.
3. `competitor-organic-channels-audit.md` — the competitor's organic social across platforms, its strength scored against the rubric, and whether it is feeding or starving the paid side.
4. `competitor-ad-account-evaluation.md` — the competitor's running ads, the creative-intelligence matrix where it could be built, the format and angle mix, and what the creative is actually doing.
5. `competitor-reviews-and-customer-language.md` — the deep review read for weak points to position against, category objections to reverse, borrowable language, and gold nuggets.
6. `competitor-reputation-analysis.md` — the competitor seen in the wild as a researching customer would see it: search surface, press, sentiment, authority, endorsements.
7. `competitor-community-and-forums.md` — the unprompted-conversation mining for objections, vivid language, defenders, and detractors.
8. `competitor-customer-and-persona-discovery.md` — who appears to buy from the competitor and how, the journey, the triggers, what they must learn and unlearn, inferred from public signal.
9. `running-notes-on-competitor.md` — the ongoing observation log of moves the competitor has made since the last refresh, organized around personas, product, messaging, and talent or creators across channels.

Take all nine in before you write a word, because synthesis is impossible until you hold the whole competitor at once. Read the running notes especially carefully for what the competitor has done since the last snapshot was built, because the trajectory is what keeps the snapshot current and is the most likely place for a stale read to become a wrong one.

If any of the nine sub-context docs is not yet built, do not synthesize across it from inference. Name the missing doc as a foundation gap, write the snapshot honestly across the sub-docs that do exist, and add an open loop pointing at the missing doc so the next round of competitor research closes it. A snapshot that quietly papers over a missing sub-doc is exactly the failure mode the build instruction guards against, because the burden of synthesis cannot rest on a foundation the model never read.

Then write the connected narrative. Lead with the read that reframes everything else about the rival: the threat type and the one thing the brand most needs to understand about this competitor. Organize the body around the four creative-strategy buckets, then route depth back to the specific sub-context docs rather than reproducing them. A reader should come away holding the shape of what this competitor means for the brand, with clear paths to the proof when they need it.

Every major observation needs a teammate-ready evidence layer. Write as if a new strategist just joined the account and has no idea what you mean yet. If you say the rival is solution-aware, name the ads, formats, claims, visuals, and value props that prove it. If you say a SKU is becoming more important, name the specific ads, product pages, launch notes, review language, or running-notes entries that show the shift. If you say a persona is missing or emerging, name who appears on screen, who does not, which ad or post surfaced the signal, and what the visible pattern is across the body. The reader should never have to ask, "What made you think that?"

## Output

Open with frontmatter carrying at least the competitor slug, the brand slug, the date, a note of which sub-context docs this synthesis was built from and their dates, and the threat-type classification. Then the narrative, leading with the headline read of the competitor and weaving the four creative-strategy buckets into a connected story. Then the consolidated open-loops roll-up. Keep the whole thing readable in a single sitting, but do not force it into an artificial one-page ceiling when the strategic read needs more room.

```markdown
---
competitor: [competitor-slug]
brand: [brand-slug]
doc: competitor-snapshot
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
built_from: [the nine sub-context docs and their dates, with any missing ones named as foundation gaps]
threat_type: [classification]
---

# Competitor snapshot — [Competitor Name]

## The headline read

## Threat type and brand impact

## Personas

## Product, SKU, and buyer journey

## Messaging

## Talent and creators

## Strengths, exposures, and tensions

## Brand-relevant implications

## Open-loops roll-up
```

Lead with the headline read, because that is the answer everything else supports. Carry every sub-doc's mark forward, mark your own cross-doc inferences as inferences, hold brand-relevant implications as provisional rather than as recommendations, and name the foundation gaps where any sub-doc was missing or thin rather than synthesizing across them.

## Open loops

End with the open-loops roll-up — the few consequential questions the snapshot is uniquely positioned to raise from cross-doc reading.

Do not write open-loop questions as forced binaries. The question should not assume the answer space by asking whether one explanation or another is true. Ask the cleaner open question that lets the evidence answer on its own. Use "what," "how much," "why," "where," or "when" when those words create a less leading question. A good snapshot loop asks what the competitor has actually done, how much it has done it, why a visible shift happened, or where the evidence points. It does not pre-fill the answer with two strategist guesses.

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

Doc-specific thinking lens. Loops on the snapshot cluster at the synthesis layer where individual sub-docs cannot reach — cross-doc tensions where two slices point in different directions about the same rival, threat-type uncertainties where the classification is not yet stable, trajectory questions where running-notes signal a shift the body of the snapshot has not yet absorbed, and persona-signal questions the audit cannot yet settle. The audit stays observational on the competitor; the loops route the implication to the commissioning brand. Sort the consolidated loops by strategic importance and evidence strength, and route anything narrower back to the sub-doc that owns it.

Loops do not cover: foundation gaps where a sub-doc was missing or thin. Those are named in the frontmatter's built_from field as foundation gaps, and the next round of competitor research closes them.

Mark any loop only the brand can answer so it routes to the brand.

## When you refresh this

The snapshot is regenerated whenever any of the nine sub-context docs beneath it materially changes — a fresh quarterly pass on identity, a new running-notes entry that shifts the trajectory, a new ad-account read that changes the creative-intelligence matrix — and at minimum quarterly, because identity and posture drift, and a snapshot that ages quietly becomes a confident misread of where the rival actually stands.

When you rebuild it, take the previous version of this snapshot in as context first, alongside the updated sub-context docs and the running notes. Carry forward the through-line of the read, update what the refreshed sub-docs and the new moves changed, and re-classify the threat type if the trajectory warrants. Pay close attention to the open-loops roll-up: note which consolidated loops have since been closed by new research, by the brand's own work, or by a move the rival made, and which remain open, because the movement of the loops over time is the clearest record of how the read on this rival is maturing. Do not rewrite the narrative from scratch each time, because that drifts and loses the story, and a synthesis that keeps restarting never deepens.
