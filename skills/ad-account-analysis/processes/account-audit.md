# Process — Account Audit

A broad read of the account. Surface what is taking up the spend, verify whether the top spenders are hitting the brand's KPIs, and call out any systemic issues across profitability, engagement, fatigue, placement, or demographic skew.

## Required inputs

- The brand's primary KPI (target CPA or NC CPA), and whether the brand defines "winning" by ROAS, CPA, NC CPA, or some combination.
- Last 30 days of account data — at minimum, ad-level spend, purchases, CPA, NC CPA, ROAS, CTR, CvR, hook rate, hold rate, frequency, CPM.
- Lifetime data on the top spenders if available, for comparison.
- The brand's attribution setting and whether it has changed in the period being read.

## Execution

1. **Surface the top 5 spenders.** Sort by 30-day spend. These are the ads Meta has decided are most efficient — they get the most attention in the audit.

2. **Verify KPI fit on each top spender.** For each, compare against the brand's KPI threshold. Mark each as "hitting target," "slightly elevated but profitable at scale," or "not hitting target."

3. **Run both lenses on the top 5.** Pull both profitability metrics (spend, purchases, CPA, NC CPA, ROAS) and user-behavior metrics (CTR, CvR, CPM, frequency) plus user-reaction metrics (hook rate, hold rate). Compare each ad's metrics against account averages so the user sees over- and under-performance.

4. **Name the patterns.** From the patterns list in strategy.md, identify which one(s) describe what the data is doing. "Top spender shows hook fatigue with rising frequency" is more actionable than the metric dump that produced it.

5. **Check for systemic issues:**
   - Is one placement absorbing a disproportionate share of spend, and does that match the brand's audience strategy?
   - Is one demographic absorbing more spend than expected, and does that match the ICP?
   - Are multiple top spenders all clustered on the same hook, format, or creator? That is a creative-diversity warning.
   - Is overall frequency climbing across the account? Exclusion list hygiene check.

   When the read turns into "which kind of creative acquires better" — UGC against static, one format against another, one creator against another — apply the cohort-efficiency discipline from `creative-strategy-fundamentals.md`. Classify off the account's own creative tags such as ad_format, not the audience token in the ad name, which leaves most spend unclassified. Weigh each cohort by its total spend over its total customers, never the single cheapest ad in a group and never a flat average across ads of wildly different spend. Check the median against the spend-weighted number so one big winner is not carrying the read, and state what share of spend the classification actually covers.

6. **Compare to lifetime, if available.** Lifetime ROAS, lifetime hook rate, and lifetime CPA tell whether the current snapshot is on, above, or below the historical norm for each top spender.

## Output

- **The Headline Read.** Two-to-four-sentence summary of what is true about the account right now and what the brand should do next.
- **Top Spenders Read.** A short prose profile of each top spender — never a table. Carry its spend with the window, its KPI status, the pattern it is showing, and the verdict (keep / iterate / kill) in sentences that hold the contrast between ads in the same breath.
- **Systemic Signals.** Anything happening across the account, not just one ad — placement skew, demographic skew, creative-diversity narrowness, frequency trend.
- **Recommended Next Steps.** Prioritized actions. If iteration is the right call, name the ad and route to the iterations skill. If creative diversity is the issue, name what is missing.

## What never to do

- Never recommend turning off a top spender solely because CPA is slightly above target. If the ad is still profitable at the brand's definition, it stays.
- Never call an ad a "winner" on the basis of a high ROAS at low spend. Spend volume × ROAS is the truth.
- Never compare across an attribution-setting change.
- Never produce a metrics dump as the deliverable. The deliverable is the read.
