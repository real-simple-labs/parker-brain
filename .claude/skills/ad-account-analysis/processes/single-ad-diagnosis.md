# Process — Single-Ad Diagnosis

Deep read on one specific ad. Profitability lens, engagement lens, and a verdict.

## Required inputs

- The ad name and ID, the format, and the launch date.
- 30-day metrics: spend, purchases, CPA, NC CPA (if tracked), ROAS, CTR, CvR, CPM, frequency, hook rate, hold rate, video average play time.
- Lifetime metrics if the ad has been running long enough to have meaningful history.
- Account benchmark for each metric — same period, account-wide — so the diagnosis is comparative, not absolute.
- The brand's KPI definition.
- Any prior iteration history on this ad.

## Execution

1. **Frame the ad.** State its launch date, current spend level, lifetime spend, and whether it has been iterated on before. Context matters — a six-month-old ad with $200K lifetime spend is a different story than a two-week-old ad with $20K.

2. **Profitability read.** Is the ad hitting CPA, NC CPA, ROAS targets? Compare 30-day to lifetime to detect drift. State "this ad is profitable" or "this ad is borderline" or "this ad is losing money."

3. **Engagement read.** Walk through CTR, CvR, hook rate, hold rate, frequency. Compare each to account benchmark and to scaling thresholds (30% hook rate, 12% hold rate, 1% CTR, 1.2 frequency). Identify where the ad is over- or under-performing the benchmark.

4. **Identify the bottleneck.** If profitability is the issue, the engagement read tells you why. If engagement is the issue, the profitability read tells you whether the issue matters yet. Specific patterns to name (from strategy.md): low CTR with high CvR is a hook problem, strong CTR with low hold rate is a body problem, high frequency with declining ROAS is fatigue, low spend with high ROAS is a low-hanging-fruit pattern.

5. **Trajectory check.** If 30-day metrics meaningfully differ from lifetime, name the direction — improving, plateauing, or declining. Trajectory determines whether the recommendation is "keep scaling," "iterate now," or "let it run and watch."

6. **Verdict.** One of: keep scaling, scale carefully, iterate now, let it run and watch, or kill. Verdict must follow from the diagnosis, not lead it.

## Output

- **The Headline Read.** Verdict in one sentence with the primary reason.
- **The Diagnosis.** Profitability and engagement reads with specific numbers vs. benchmarks.
- **The Bottleneck.** One sentence naming the constraint.
- **Recommended Next Steps.** What to do next. If iterating, name the iteration type(s) worth testing and route to the iterations skill. If killing, explain why and what to learn from the kill.

## What never to do

- Never deliver a profitability read without an engagement read or vice versa.
- Never recommend a kill on a profitable ad over slight CPA elevation.
- Never name a pattern that the data does not support.
- Never call fatigue from a single snapshot — fatigue requires a trajectory.
