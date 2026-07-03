---
summary: "How to analyze public ad accounts — impression-rank as a proxy, volume/recency/variant reading, and the library-vs-live-spend distinction."
---

# Analyzing public ad accounts

Updated 2026-06-08.

This doc is the canonical methodology for analyzing an ad account from the outside, using only what a public ad library exposes. It is the reasoning Parker applies whenever it reads paid creative it does not have backend access to — a competitor, an inspo brand, an affinity brand, or the brand's own public library before any logged-in performance work. It is referenced by `prompts/brand-profile/ad-account-evaluation.md`, `prompts/competitor-profile/competitor-ad-account-evaluation.md`, and any other prompt that walks a public library.

This is a public-library doc. It covers what anyone can see in the Meta Ad Library without logging in: the active creative, the launch dates, and where exposed, an impressions ranking. It does not cover spend, attribution, audience breakdowns, CPA, ROAS, or any metric that lives behind a brand's logged-in account. That work uses the separate internal-account method in `ad-account-analysis.md`.

The point of this doc is to teach Parker to run the read a human creative strategist would run, without a human in the loop. Every observation a strategist makes by eye is written here as something Parker does directly: identify the format, name the hook, read the body, name the absence. Parker is the analyst, not a note-taker waiting for one.

---

## The principle

A public ad library is a strategic statement. The active ads, the volume, the format mix, the angles repeated, the angles never run, the messaging tone, and the visible cast are all decisions an account has made with real money. Reading them as a body, not as a gallery, is what turns a library walk into a strategic read.

Two governing rules sit underneath everything below.

**Grade every account objectively in its own lane.** A brand's presence in a library is the start of an evaluation, not the conclusion. A big or pretty or category-established brand earns nothing automatically. Score each account on the strength of the creative itself, independent of brand size, retail footprint, or reputation. Presence is not endorsement.

**A single ad tells you almost nothing.** The value is the pattern across many. Read each creative open-endedly, build a picture across the body, and treat conclusions as patterns the library supports rather than reads of any one ad.

## What this method is and is not for

This is the research-phase methodology for public-library work. It applies to:

- Reading a competitor's ads to find the brand's creative opening.
- Reading inspo and affinity brands to learn from creative that is working in adjacent lanes.
- Reading the brand's own public library, before any logged-in performance pass, to spot patterns the analytics-led view will smooth over.
- Refreshing any of the above on a cadence as the libraries turn over.

It is not for:

- Logged-in performance audits behind the brand's own access. That work reads spend distribution, attribution, and audience breakdowns the public library does not expose, and it uses `ad-account-analysis.md`.
- Iterating on a single performing ad. That work uses the iterations skill.
- Concepting new ads. That work uses the scriptwriting and static-ads skills.

## The three-tag taxonomy

Every brand worth tracking is one of three things, and each tag implies a different read.

**Competitor.** A direct rival for the same problem and the same purchase. Tracked for what it advertises, what it conspicuously does not advertise, and what its creative is doing strategically. A competitor can be a major market rival and a creative non-entity at the same time, which is its own finding.

**Inspo.** A brand whose creative is worth learning from, not necessarily a rival. The bar for inspo is creative strength, not market overlap.

**Affinity.** A brand one step away from the core problem, living inside the customer's ecosystem, where the target buyer already shops. Not a direct competitor and not direct creative inspiration, but a source of new creative opportunity because it reaches the same person in an adjacent context. Affinity is the emotional connection and shared values the customer feels toward a brand beyond the product. Affinity brands are discovered during customer analysis, not during competitor analysis, so the affinity set is populated after persona work has landed.

A brand can be a competitor and an inspo at once. A brand is rarely a competitor and an affinity at once, because the lanes are defined by different relationships to the customer. Hold the tags as separate fields, not a single label, since the action each implies is different.

## Market competitor versus creative competitor

The most important conceptual cut in account analysis. A brand can be a giant market competitor and a creative non-entity, coasting on retail distribution and past wins while running few or no ads. It is unquestionably a rival for the purchase but there is nothing to learn from its pipeline. The reverse also exists: a brand barely competing for the same purchase can be a strong creative competitor worth watching.

What you do with each is different. A major market competitor running no ads still gets tagged and checked in on periodically, because the moment it starts running creative, it matters. You do not mine it for creative inspiration while it runs nothing. You rank the accounts you actually want to beat creatively, and you weight your attention by creative-competitor strength, not market size.

## The methodology

### Step one — Volume read

The first read is whether there is anything to analyze at all. Count the active ads in the library. Read the count against the brand's footprint, retail presence, online visibility, and category density. Roughly a hundred or more active ads reads as a real testing operation. A handful reads as too little to analyze on its own. Numbers in between get interpreted through the category caveat — a category where the product is the variable, or where seasonal cycles concentrate spend, can look thinner than the brand's actual operation.

If the brand runs few or no ads, that absence is the finding. Do not fabricate a creative mix for an empty library. The absence is what the brand can exploit.

### Step two — Fresh-eyes pass

Parker's first job is to spot patterns from creative alone, before reaching for any ranking or external signal. Read the body open-endedly and let the creative speak first. In a public library there is no spend or outcome data to anchor the read anyway, so the creative read is the analysis, not a warm-up to it. When this is the brand's own library, a later logged-in performance pass can overlay outcomes, but that is a different doc and a different step; the value of this pass is precisely that it is uncontaminated by the numbers.

### Step three — The top-of-library bet, read through its filter

Before reading the top of a library as a strategic statement, determine what the top is sorted by. The Meta library can be filtered, and the two sorts mean completely different things:

- **Sorted by top impressions.** Here the first placements are the closest public proxy for what the brand thinks is currently winning, what it is leaning on, or what is filling delivery in the absence of a better answer. The top one to three are a real hypothesis about the account's current bets. Read them as a strategic statement.
- **Sorted by date launched.** Here the top placements are simply the newest ads, which says what the account is testing right now, not what is winning. Do not read the newest one to three as winners. Read the top twenty most recent, or for a large library the top twenty percent of recent launches so the sample scales to the size of the brand, and read the testing pattern across that set: what angles, formats, and personas the account is putting into market this cycle.

Naming the filter first is what keeps Parker from mistaking newest for best or best for newest. The mistake is silent and it poisons everything downstream.

### Step four — Hook-first read of a single creative

The first thing Parker reads about any creative is the hook, because the hook is what is actually pulling the audience. Read it the way the hooks context doc in `hooks.md` teaches, using that doc's vocabulary rather than vague description.

Read the hook across its four elements: the text overlay on screen, the sound or spoken line, the visual of the first frame, and the vibe set by lighting, font, color grade, and aesthetic. Note whether there is movement in the first frame and whether the hook shows or merely tells, since the strongest hooks show.

Then name the hook format. `hooks.md` defines the working set the field actually uses: Comment Response, Investment, Scam, Give Me Time, POV, Demographic, How Do I Know If, Speed & Transformation, Conversational, Viral Product, Reaction, Controversy, Trigger Word, Myth-Busting, Educational, Comparison, Storytelling, Authority, Question, and hook stacking. Identifying that an account opens with Demographic and Comment Response hooks while never touching Authority or Storytelling is a real read; "the hooks are varied" is not. Speaking in these named formats is how Parker proves it understands hooks rather than describing them from the outside.

After the hook, read what the ad is about and what it communicates, who the talent is trying to mirror or represent, the length, and the storytelling structure. Do not hunt for a preset checklist of findings; the finding might not be in your checklist. Some signals register only on the recap — a recurring setting, a recurring time of day, a recurring framing. Analyze what is given, follow what catches the eye, and let the pattern across many ads do the work the single creative cannot.

### Step five — The lenses the public library actually gives you

A public library walk runs the reads the data supports, and no more. Be precise about what is and is not available.

**Top by impressions.** Where the library exposes this ranking, it is the closest available signal to what is working, because more impressions usually means more delivery and more delivery usually means more spend. Treat that as a correlation, not a fact: the library does not show spend, so a high-impression ad is a strong hypothesis about a winner, not proof of one. A top product-release ad can carry forced launch delivery rather than creative strength, and a top partnership ad can carry an inflated impression count from the partner's audience without converting.

**Most recent by launch date.** This shows what the account is currently testing, where its head is at, and its cadence. Recent volume and variation tells you whether the account is in test mode or in milking-a-winner mode.

**Days active.** The library exposes each ad's launch date, so Parker can read how long an ad has been running. Before impressions were ever visible, longevity was the classic public proxy for a winner: an account does not keep paying to run an ad that is failing, so an ad that has been live for a long stretch is likely performing. An ad that has run for months reads as a probable winner; a cluster of ads all launched in the last week reads as a fresh test, not a proven set.

What Parker does not have is spend. There is no public spend data. Do not infer, estimate, or guess spend amounts, and do not let a spend-weighted read sneak in through impressions. The honest public read is top-by-impressions and days-active as winner proxies, most-recent as the testing signal.

Across all of these, the ads are already classified with Parker's AI format tags. Pull the existing tags from the MCP rather than re-deriving them by eye, and use the ad-formats context only to interpret what a tag means. Reading the format mix is a tag-level read, not a guess.

### Step six — Pattern across the body

This is the core of the method. Across the body of the active library:

- Format mix and the balance across the AI format tags — the split between static and video, and within those the lean toward UGC, founder, authority, demo, listicle, offer-based, and the rest.
- Angles and hooks that recur, and how much they vary, read in the hook vocabulary from step four.
- Clusters of near-duplicate variations, which are either a test in progress or a winner being milked.
- Previously-organic creative reappearing as a partnership or whitelisted ad, which is a likely winner getting more delivery.
- Funnel distribution by destination — lead form, best-seller page, product page, collection page — which reveals different funnel objectives.

The comparative read is the lever. The angle a rival overuses is an angle the brand should avoid to not saturate the field further. The angle a rival never runs is either a failed angle or an opening, which only testing resolves.

### Step seven — Read the body across five dimensions

Several of the most important reads come from holding the whole library against a small set of diagnostic questions. These are questions, not verdicts: Parker answers them from the library and names what the answer implies about how the brand sees itself and its customer.

- **Brand posture, and whether the creative matches it.** Is this a problem-solution brand, a lifestyle brand, or a hybrid — and do the current ads match that? A problem-solution brand running predominantly aesthetic, sustainability, or brand-pride creative is positioned as a lifestyle brand by default even though its product solves a problem. That is a posture mismatch, not a style choice, and it cannot be fixed by improving execution on the aesthetic ads. Read the dominant messaging angles against what the category demands and name the mismatch when it is there.
- **Creator diversity.** Do they use a variety of creators, and what does that variety, or the lack of it, tell us? This one question absorbs several older ones. Count the distinct on-brand humans across the recent body and ask whether the range matches the breadth of audience the brand claims to serve. Whether the brand uses real people at all, whether it leans on its founder, and whether it runs partnership or whitelisted creators are all reads inside this question: a brand with no real-people content believes its own taste is the buyer's taste, a brand with an authoritative founder absent from the creative is sitting on an unused trust asset, and a brand running no partnership creative in a category where it is obvious is either taking a deliberate stance or leaving a lever untapped.
- **Product spread.** Which products or SKUs get creative weight, and which get none? The spread shows where the brand is putting its creative bet and which parts of the catalog it treats as the growth engine versus the long tail.
- **Format spread.** Using the AI format tags, what is the format mix, and which formats are absent? A narrow format spread is a testing ceiling; a format the category runs heavily and this account never touches is an opening or a deliberate avoid.
- **Stage of awareness.** What awareness stages do the ads target — unaware, problem-aware, solution-aware, product-aware, most-aware — and is the spread lopsided? An account that only ever speaks to the most-aware buyer is not building new demand, and that gap is a finding.

Read each dimension through recency and through the category caveat, the same way step five and the failure modes below demand.

### Step eight — Specific account-health signals

A few targeted reads to run across the library, each independent of the dimensions above.

- **Avatar callouts.** When the creative leans on aesthetic-tag avatars — a hobby, a vibe, a mood label — it is a window into who the brand thinks its personas are. Aesthetic-tag avatars usually mean the brand is guessing at its personas through aesthetics rather than building them from buyer data, so treat them as a diagnostic of how well the brand actually knows its customer.
- **Founder usage.** Where a founder appears, compare the format diversity of their appearances against their demonstrated pull and named credibility. Founder content is the highest-trust creative most brands already have, and it is almost always under-formatted in the accounts that have it working.
- **Branded technical language.** Flag any branded technical term — patented this, proprietary that, category-internal jargon — that an unaware buyer would not understand without category context. The customer pays a cognitive cost before any selling happens, and most customers will not spend it.
- **Offer-led creative frequency.** Read how much of the active library leads with an offer or discount. Offer-led creative as a meaningful share of the library is either inventory clearing, near-term revenue pressure, or a substitute for a missing demand-generation engine. None of those reads recommends more offer creative.
- **Organic-versus-paid disconnect.** A brand can be strong organically and have no discernible paid testing strategy, or the reverse, and that gap is a hypothesis about where the operational problem lives. This read is only real when the organic picture is actually in hand, so it requires pulling in the organic social audit for the same brand. Without that audit loaded, do not assert an organic-versus-paid disconnect from the ad library alone; flag it as a read that needs the organic audit and move on.

### Step nine — What can we learn from them

The read is not only defensive. For inspo, affinity, and strong creative competitors especially, run the body a second way and ask what is worth borrowing. What new or unusual angles is this account running? What format is it using in a way the brand has not tried? What hook structure keeps recurring that the brand could adapt? Where is it clearly ahead — a fresh organic format brought into paid before it saturates, a creator archetype the brand has not cast, a posture the brand could test?

When a learnable idea surfaces here, first verify it is new to Parker — check the iterations and other skills, the creative-strategy context docs, the hooks doc, and the existing idea-bank entries. If Parker already has it, it is not an idea-bank idea; route it to the surface that owns it instead. Only a genuinely new idea routes to the idea bank: a reusable cross-brand pattern to Parker taste, a brand-specific idea to that brand's idea bank, with the novelty check, the reasoning, the why-now, and the source example attached so it can be taught later. Route it as a `[~]` proposed entry in the pending set — Parker proposes idea-bank ideas, Jimmy approves them before they become trusted taste. The point is to leave a library walk having learned from the account, not only having graded it.

## What does not qualify

A few patterns to refuse.

A single ad's hook is not an account read. Single-ad findings are tactical and do not earn a place in the strategic synthesis.

There is no public spend data. Do not infer or guess spend amounts, and do not dress an impressions read up as a spend read.

## Common failure modes

Walking a public library, the model will by default do several things that produce wrong reads.

**Treat presence as endorsement.** A brand with a hundred active ads gets read as having a strategy worth borrowing from, even when the body is repetitive, untested, or off-strategy. Hold the grade-in-own-lane discipline. On the other side, be cautious about a brand running well under fifty to a hundred ads; that thinness is often a sign it has not truly cracked Meta.

**Mistake the sort for the signal.** Reading the newest ads as winners, or reading the top-impression ads as the testing frontier, inverts the whole analysis. Name the filter first, every time.

**Average across product eras.** A pattern from three years ago and a pattern from last month can describe two operationally different brands. Weight the read toward recency, and where the brand can supply a timeline of operational changes — leadership, agency, product line — overlay it.

**Score format mix without the category caveat.** A category where the product is the variable, like apparel, shows formal sameness by design, not by weak strategy. Read format mix through the category lens.

**Read partnership ads as top performers.** A large-network creator inflates impressions without necessarily converting. Log partnership and whitelisted ads separately rather than counting them in top-performer reads.

**The Meta active-versus-running UI quirk.** The public library can show an ad as active when only its ad set is paused, or the reverse. Treat the public library as a partially-noisy mirror of what is really running.

## How this method gets used downstream

The output of a library walk is not a list of ads. It is a strategic read of the account: what it advertises, what it does not, the angles it runs, the posture it occupies, the absences worth noting, the comparative opening for the brand, and what is worth learning from it.

That read feeds three downstream artifacts:

- For competitors, the `competitor-ad-account-evaluation.md` sub-context doc, one per rival, rolled into the competitor profile.
- For the brand's own public library, the `ad-account-evaluation.md` sub-context doc, which later combines this public read with the logged-in performance pass and resolves to a two-sentence diagnosis.
- For inspo and affinity brands, a lighter capture sufficient to inform concepting later, plus any idea-bank or taste routing from step nine.

In all cases, the discipline is the same: grade in own lane, name the filter, read patterns across the body, name absences as findings, learn what is worth learning, and refuse the failure modes above.

## When to refresh

A library turns over quickly. Refresh on a quarterly cadence at minimum, more often when the category is moving or when a tracked rival is testing fast. Take the previous read in as context first, carry forward what still holds, and re-read what moved. Watch for new angles entering the account, a previously-organic creative scaled into paid, a shift in the funnel distribution, and any active-rival library that has gone quiet — each is a strategic move worth catching.
