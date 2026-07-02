# Ad Account Analysis — Strategy

This document is how Parker routes an analysis request to the right process. Different questions about a Meta ad account need different data pulls and different interpretive frames — the strategy doc picks which.

## What to load before deciding

- The brand's primary KPI definition. For most DTC/ecommerce, this is CPA (cost per purchase) or NC CPA (new customer CPA). Without the KPI threshold, "is this hitting the target" is unanswerable.
- The brand's current attribution setting. If it has changed recently, comparisons across the change point are unreliable.
- Any operational context that frames the question — new launch, promotional moment, recent attribution change, recent budget shift, audience expansion or contraction.

If the brand's KPI definition is not available, ask the user before running the analysis. Do not assume a generic CPA target.

## What the user is actually asking

Map the user's question to one of the analysis types. The same data lives behind all of these, but the lens differs.

### account-audit

User asks "what's working in my account," "audit my account," "what should I be doing differently," "where is my spend going." Goal: surface top spenders, verify they are hitting KPIs, identify which are profitable winners and which are warning signs, and call out anything systemic — a placement skew, a demographic skew, a fatigue pattern.

Pick when the user wants a broad read of the account, not a single-ad diagnosis.

### single-ad-diagnosis

User asks "how is this ad doing," "should I keep running this," "is this ad scaling," "what is wrong with this ad." Goal: deep read on one specific ad through both lenses, with a clear should-keep / should-iterate / should-kill verdict.

Pick when the user names a specific ad or pastes its data.

### placement-breakdown

User asks "where is my spend going," "should I be on more reels," "is Instagram outperforming Facebook," "why is my CPM so high on X placement." Goal: read what the placement distribution implies about the audience being reached, where spend is concentrating and why, and whether the placement mix matches the strategic goal.

Pick when the user is asking about platform or placement performance specifically.

### demographic-breakdown

User asks "who is my audience," "what age group is converting," "is my product reaching the right people," "should I be targeting differently." Goal: read what age, gender, or combined breakdowns reveal about who the algorithm is reaching, whether that matches the intended ICP, and whether a mismatch is hurting performance.

Pick when the user wants to understand who is being reached, not just whether the ads are working.

### fatigue-diagnosis

User asks "is this ad fatiguing," "is this ad ready to scale further," "why is performance declining," "should I refresh this ad." Goal: read the fatigue signals (rising frequency, declining ROAS over time, declining hook rate, declining hold rate, rising CPM with stable reach) to determine where the ad is in its lifecycle.

Pick when the question is about an ad's trajectory, not its current state.

## How to choose when the user's question is ambiguous

Some questions touch multiple processes. Apply these tiebreakers in order:

1. **Is the user pointing at a specific ad?** Run single-ad-diagnosis as the primary process. Layer in placement or fatigue reads if the diagnosis surfaces them.
2. **Is the user asking about trajectory ("is this fatiguing," "ready to scale")?** Run fatigue-diagnosis. Single-ad-diagnosis is a snapshot read; fatigue-diagnosis is a trajectory read.
3. **Is the user asking who is being reached?** Run demographic-breakdown. Placement-breakdown reveals who as a side effect, but if the user is asking about audience, demographic is the more direct lens.
4. **Default to account-audit** for broad, undirected questions.

Multiple processes can run in sequence on a single user request. If the account-audit surfaces a fatigue signal on a top spender, follow it with a fatigue-diagnosis on that ad.

## The two lenses every process applies

Both lenses are always present. The processes vary in how much weight each lens gets.

### Profitability lens — the "is this making money" read

The metrics that say whether spend is producing returns:

- **Amount spent.** Sustainable spend, daily and week over week, is the foundation of "this ad is a real winner." Big spend on a healthy CPA matters far more than small spend on a flashy CPA.
- **Number of purchases.** Conversions actually flowing.
- **Cost per purchase (CPA).** Hitting the brand's KPI threshold or close enough to be tolerated at scale.
- **Number of new customer purchases (NC).** Custom conversion in most accounts. The growth signal.
- **Cost per new customer purchase (NC CPA).** The new-customer growth health.
- **Purchase ROAS.** Total return on ad spend. Read in context of spend volume, never in isolation.

A high ROAS on $30 of spend is a low-hanging-fruit pattern — the ad converted people who were already going to convert and took credit. It will dry out quickly. A lower ROAS on $300 of spend is the real winner.

### User-behavior lens — the "how is the ecosystem reacting" read

The metrics that say whether the ad is earning attention, holding it, and reaching new people:

- **Outbound CTR.** Target above 1%. Low CTR means the ad is not earning the click — either the hook is weak or the CTA is not landing.
- **Conversion rate.** Percent of people who saw the ad and converted on the website. Low CR with healthy CTR can be a website or offer problem, not just a creative problem.
- **Cost per link click.** What it costs to send one person to the site.
- **CPM (cost per 1,000 impressions) and Cost per 1,000 Accounts Reached.** CPM divided by 1,000 unique accounts gives the reach efficiency. High CPM with low reach efficiency means the ad is repeatedly hitting the same eyeballs.
- **Frequency.** 1.2 or lower is healthy. Climbing into the 3-4 range is a saturation signal — the same audience is being repeatedly served the same creative, which is when fatigue sets in. Also check exclusion-list hygiene at the account level if frequency is climbing.

### User-reaction lens — the "what are people doing with the ad" read

The metrics that say whether the ad earned engagement specifically:

- **Hook rate.** Percent who watched the first 3 seconds. Target 30% minimum, ideally 45-50% on top performers.
- **Hold rate.** Percent who watched the ad completely. Target 12-15% minimum.
- **Video average play time.** How long viewers stayed.
- **Cost per save.** Low cost per save means people are bookmarking the ad — strong signal.
- **Cost per share.** Low cost per share means the ad is being passed around — strong signal. High (over a thousand dollars) means it is essentially not being shared.

## Common patterns the diagnosis should name

These are the recurring stories the data tells. Naming the pattern is half the diagnosis.

- **Low CTR, high CvR.** Message converts once engaged but is not earning attention. Hook is the bottleneck.
- **Strong CTR, low hold rate.** Hook lands, body loses viewers. Pacing or transition is the bottleneck.
- **CPA rising over time, frequency rising, ROAS declining.** Audience fatigue. The same audience is saturated. Needs creative refresh — iteration, format swap, audience expansion.
- **Good metrics but not scaling further.** Audience-format combo is tapped. Needs new segments — format change, archetype change, awareness shift.
- **High video completion, low CTR.** Content engages but does not convert clicks. Offer or CTA is weak.
- **Low spend, high ROAS, low CPA.** Low-hanging-fruit pattern. Will dry up quickly. Do not over-celebrate.
- **High CPM but low Cost per 1,000 Accounts Reached.** Reaching new people efficiently despite high CPM. Good growth signal.
- **Low CPM but high Cost per 1,000 Accounts Reached.** Spending cheaply but repeatedly hitting the same eyeballs. Saturation signal even if CPM looks fine.

## Placement signals at a glance

When placement breakdown is the lens, these are the implications:

- **Heavy Facebook Feed delivery.** Audience skews older, values community, often in consideration or research phase.
- **Heavy Instagram Feed delivery.** Audience skews younger, aspirational, often top or mid funnel, responds to visual cues.
- **Heavy Facebook Reels delivery.** Audience reachable in casual viewing moments. Top-of-funnel reach, lower cost, weaker intent.
- **Heavy Instagram Reels delivery.** Trend-following, younger demographic, early funnel but high virality potential.
- **Heavy Facebook Stories delivery.** Older audience, passive tapping-through, upper funnel exposure.
- **Heavy Instagram Stories delivery.** Younger, more interactive, mid-to-lower funnel if conversion CTAs perform well.

## Common mistakes to avoid

- Reading profitability without engagement, or engagement without profitability.
- Recommending an ad be turned off because CPA is slightly above target at scale.
- Comparing periods that span an attribution-setting change.
- Calling a low-spend high-ROAS ad a winner before checking its spend volume.
- Confusing the breakdown effect with Meta misallocating budget.
- Reporting metrics instead of diagnosing what the metrics mean.
- Forgetting to check exclusion-list hygiene when flagging frequency issues.
- Calling fatigue without confirming the trajectory — current frequency alone is a snapshot, not a trend.

## Final quality audit before output

- Did I name the actual pattern, not just dump the metrics?
- Did I apply both profitability and user-behavior lenses?
- Did I tie the read to the brand's actual KPI definition, not a generic one?
- Did I account for the breakdown effect and attribution setting?
- Did I give specific next actions, not just "this ad needs attention"?
- Did I avoid recommending shutoffs on profitable ads with slightly elevated CPA?

---

## Reasoning log

This section accumulates past diagnoses and the reasoning behind them as the loop runs. Each entry captures the question asked, the read delivered, the actions taken, and any feedback that adjusted future reads for this brand. The log is the strongest signal for Parker on how this specific brand defines "winning" and what reads it has historically agreed or disagreed with.

*(No entries yet — populated by the fine-tuning loop.)*
