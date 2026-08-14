---
summary: "The end-to-end Congruence method for one paid-social journey: infer who an ad's message and on-screen person appear built for, compare that intention with actual age-and-gender delivery and outcomes, inspect whether the exact landing page continues the same promise and audience experience, calculate a fixed-weight score from 1 to 10 without hiding missing evidence, and build a brand-faithful local page mockup when the destination is the break."
doc: congruence
status: drafted
source: approved Parker product method; initiated by Jimmy Slagle on 2026-08-14
last_updated: 2026-08-14
---

# Congruence

Congruence is the degree to which one person can move from ad impression to landing page without feeling that the message, messenger, audience, promise, or experience changed underneath them.

The goal is not visual sameness. A landing page can carry more detail than an ad, and a spokesperson can differ from the buyer. The goal is continuity of intent. The ad should attract a specific person for a specific reason. Meta should find people consistent with that signal or reveal a useful surprise. The page should then continue the reason they clicked in language, proof, imagery, and interaction that makes sense for the people arriving.

This method joins three truths:

1. **The ad's intended experience.** What the message says, who appears, what role that person plays, what the visual shows, what prior knowledge the ad assumes, and who it appears to invite.
2. **Meta's delivered experience.** Which age-and-gender groups receive the delivery and which groups produce the meaningful outcome under the campaign objective.
3. **The landing-page experience.** What the exact destination says and shows, how it behaves on mobile, and whether it continues the ad for the people actually arriving.

No one surface can answer the question alone. Creative without delivery is an intention read. Delivery without creative cannot explain what signals Meta received. A page without both cannot tell whether it is the right handoff.

## The unit is one exact path

Congruence is scored for one ad creative or identifiable variant, one delivery window, and one final destination. Never blend several ads into an account-wide score. Never use one ad's creative with another ad's demographics. Never audit the homepage when the ad routes to a product page.

Lock the brand, account, campaign, ad set, ad ID, creative or variant ID, objective, optimization event, date window, attribution setting, and final URL before scoring.

Dynamic creative and automated variants can break the join. If the data source cannot show which person saw which creative and destination, the experience cannot be scored honestly. State the collision and stop.

## Evidence before scoring

Every scored audit requires:

- the complete customer-facing creative;
- exact ad-level delivery by age and gender, with a delivery denominator and a meaningful outcome;
- the rendered mobile destination and its actual copy;
- matching IDs, dates, filters, and attribution.

Full creative means the actual static or the whole video, including the message in the picture, spoken words, on-screen words, caption, primary text, person, setting, and action. Names and tags are handles, not evidence.

Delivery concentration and performance concentration are different. Spend or impressions show where Meta delivered. Purchases, leads, landing-page views, or the campaign's real optimization event show what happened. A group can receive the most delivery without producing the best outcome, or produce an impressive rate on too little volume to guide a decision.

The page needs both content and experience evidence. A fetch can verify the words and destination. A rendered mobile view reveals the first screen, visual order, readability, tap targets, overlays, and other friction. One cannot stand in for the other.

If any required seam is unscorable, do not issue an overall score. Missing evidence is not neutral evidence.

## Read the intended audience in layers

Keep three layers separate:

- **Creative-implied audience:** who the ad appears made for based on its problem, desire, promise, language, person, role, setting, proof, format, awareness level, and action.
- **Stated audience:** who the brief, brand strategy, persona work, or user says the ad is for.
- **Delivered audience:** who Meta reaches and who produces the meaningful outcome.

The creative-implied audience is the lived ad. A brief can say one thing while the creative signals another. The gap is itself a finding.

The person on screen is evidence, but not a demographic stamp. Their role matters. An older doctor can lend authority to an ad aimed at younger buyers. A child can be the beneficiary while the parent is the buyer. A founder can speak across age groups. Read who they are *doing the work of being* in the ad before deciding whom they signal.

Describe appearance cautiously and never infer sensitive traits. Age and gender are Meta reporting categories here, not a complete model of a person.

## Read delivery as evidence, not destiny

Sort age-and-gender rows by delivery, then read outcomes with volume attached. Ask:

- Which group receives the most spend or impressions?
- Which group produces the most meaningful outcomes?
- Which group produces the most efficient outcomes at credible volume?
- Does one group lead all three, or do delivery and response split?
- Does the pattern match the creative-implied audience, the stated audience, both, or neither?

A mismatch is not automatically bad. Meta may reveal a real audience the brand did not name. Profitable off-plan delivery can be an opportunity. Unprofitable delivery outside the implied audience can indicate unclear creative, a broad offer, account structure, or auction effects.

Do not claim that messaging caused delivery merely because the two correlate. Objective, budget, placement, inventory, account structure, prior conversion signals, seasonality, and the breakdown effect can all shape the distribution.

## Read the landing page as the next beat

The page does not need to repeat the ad word for word. It needs to answer the expectation the click created.

Compare:

- problem or desire;
- promise and result;
- product or SKU;
- offer, price, and terms;
- proof and objection handling;
- person, imagery, and situation;
- tone and customer language;
- awareness level and amount of explanation;
- next action;
- mobile readability and interaction.

The first screen carries extra weight because it is the first proof that the click went to the right place. A strong ad can lose Congruence immediately when the page opens on a generic brand statement, a different product, a missing offer, unrelated imagery, or an experience the arriving audience struggles to read or use.

Do not turn this into a full CRO score. A page can be imperfect and still congruent. A beautiful page can be incongruent if it continues the wrong promise for the wrong person.

## The four scored seams

Score each seam from 1.0 to 10.0. Use one decimal only when the evidence supports that precision. Each score needs decisive evidence and one reason it is not higher.

### 1. Ad message and person shown, 20%

Does the person, role, voice, setting, and primary visual make the message more recognizable and believable for the creative-implied audience? If no person appears, score the message against the primary visual subject.

### 2. Intended audience and actual delivery, 30%

Do delivery concentration and meaningful outcomes support the audience the ad appears built for? Read profitable spillover as evidence, not disobedience to a brief.

### 3. Ad promise and landing page, 25%

Does the page continue the same problem, desire, promise, product, offer, proof, tone, awareness level, and next action?

### 4. Delivered audience and landing-page experience, 25%

Does the rendered page make sense for the demographic groups receiving meaningful delivery and outcomes? Point to actual language, imagery, proof, readability, and interaction. Do not lean on stereotypes.

## Score anchors

Use these anchors for every seam:

- **10:** The seam is exceptionally continuous. Evidence points the same way, and no meaningful break is visible.
- **8:** The seam is strong. The intended experience carries through with only a small gap that is unlikely to change the main response.
- **6:** The seam is mixed. Important parts line up, but a visible conflict, split audience, or lost expectation weakens the path.
- **4:** The seam is weak. The evidence materially favors a different person, message, promise, or experience.
- **2:** The seam is badly broken. Most of the experience points somewhere else or works against the click expectation.
- **1:** The seam is almost entirely disconnected.

Scores between anchors require evidence proportionate to the distinction. Do not reward attractive design, high ROAS, or a familiar persona label unless it improves the seam being scored.

## Weighted score

Calculate:

```text
overall =
  (ad message and person × 0.20) +
  (intended audience and actual delivery × 0.30) +
  (ad promise and landing page × 0.25) +
  (delivered audience and landing-page experience × 0.25)
```

Round the final result to one decimal. Do not add a label in place of the number.

Find the largest repair opportunity with weighted point loss:

```text
weighted loss = seam weight × (10 - seam score)
```

The largest loss usually deserves the first change. Legal, factual, accessibility, or severe usability failures can override that order.

## What a useful recommendation changes

Repair the seam, not the score in the abstract. A useful recommendation names the exact message, person, frame, URL, first-screen element, proof block, or interaction to change and ties it to evidence.

Do not recommend narrowing or excluding an age or gender group solely because it differs from the brief. First decide whether the group is profitable, whether the creative accidentally or usefully signals to it, and whether the page serves it. The better move may be a new congruent variation for that group rather than removing it.

## When the page is the break, show the repair

A written recommendation is too abstract when the destination is the main break. If either landing-page seam scores 6.0 or lower, or the page is a generic handoff that loses the ad's core audience, promotion, product, or promise, the audit produces a working local mockup as its final step.

The mockup is a narrow repair, not a rebrand. Study the company's rendered site, computed styles, current page family, brand context, and owned assets. Carry forward its real fonts, color roles, grid, spacing, radius, shadows, header, footer, product imagery, photography, and component behavior. Then change the message hierarchy and only the page elements needed to continue the ad for the people actually arriving.

Design systems and component libraries can improve accessibility and implementation quality, but they do not get to replace brand evidence. A generic purple gradient, a stack of rounded cards, a bento grid, or an off-the-shelf component theme is not an improvement when the company's own site does not look that way. Use 21st.dev, shadcn/ui, or another component source for mechanics when useful, then translate it into the company's design system.

The result stays local. It must not edit or publish the live site, connect a real checkout or lead flow, or collect customer data. It does need working interactions, mobile and desktop browser verification, screenshots, asset sources, and an explicit list of the Congruence seams it repairs.

When several ads are compared, score each independently and rank only complete audits. The rank is a comparison of whole paths, not a declaration that the highest-scoring ad is the most profitable or most scalable. Congruence and business performance answer different questions and should be read together.
