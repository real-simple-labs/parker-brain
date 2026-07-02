# Process — Fatigue Diagnosis

Trajectory read on an ad — is it scaling, plateauing, or fatiguing? Fatigue requires a trend, not a snapshot. The job is to identify where in its lifecycle the ad is so the team knows whether to scale, refresh, or iterate.

## Required inputs

- The ad and its 30-day metrics: CPA, ROAS, CTR, CvR, hook rate, hold rate, frequency, CPM.
- Lifetime metrics for the same ad — minimum 4 weeks of history is needed for a real trajectory read.
- Week-over-week breakdown of the key metrics if available.
- The brand's KPI definition.
- Prior iteration history on this ad.

## Fatigue signals to check

Fatigue rarely shows on one metric. It is a pattern across several. Check all of these:

- **Frequency climbing past 1.5–2.0.** The same audience is being repeatedly served the same creative. Classic saturation signal.
- **ROAS declining vs. lifetime average.** The conversion rate from impressions is degrading even if the creative still engages.
- **Hook rate declining.** The opening is losing its stopping power — viewers who have seen it before are scrolling past.
- **Hold rate declining.** Even when the hook still earns the first three seconds, viewers are dropping off because they have seen the rest before.
- **CPM rising with stable or declining reach.** Meta is paying more to reach the same eyeballs.
- **CPA rising vs. lifetime, even if still under target.** A directional change matters even before the threshold breaks.

A single signal is a hint. Two signals is a pattern. Three or more is fatigue.

## Execution

1. **Compare 30-day to lifetime.** Across each fatigue signal, name where the 30-day is worse than lifetime. If it is, the ad is in the declining phase. If 30-day matches or exceeds lifetime, the ad is still scaling or plateauing.

2. **Check week-over-week if available.** Fatigue accelerates in the late phase. If the weekly trend is sharply declining over the last 2-4 weeks, the timeline for action is shorter than the 30-vs-lifetime read alone suggests.

3. **Check exclusion list hygiene.** Climbing frequency can be a function of stale exclusions — repeat customers still seeing acquisition creative. Worth flagging as an account hygiene check before declaring creative fatigue.

4. **Identify lifecycle stage:**
   - **Scaling.** Performance improving or flat, frequency under 1.5, engagement signals strong. Push more spend.
   - **Mature plateau.** Performance flat at or near KPI target, frequency 1.5-2.0, engagement signals stable but not improving. Continue running, queue iteration for when fatigue begins.
   - **Early fatigue.** One or two signals declining, others still healthy. Iterate within 2-3 weeks before decline accelerates.
   - **Late fatigue.** Three or more signals declining, frequency over 2.0, ROAS meaningfully below lifetime. Iterate immediately or kill.

5. **Recommend the right action by stage.** Scaling → more budget, monitor. Mature plateau → hold and prepare iteration. Early fatigue → iterate now while the ad is still profitable enough to learn from. Late fatigue → iterate or kill, and audit what the ad's death taught the brand.

## Output

- **The Headline Read.** Lifecycle stage and the action implied.
- **The Fatigue Signal Audit.** Each signal checked, with the 30-day vs. lifetime comparison and whether it is firing.
- **The Trajectory.** Where the ad has been, where it is now, where it is heading if nothing changes.
- **Recommended Next Steps.** Specific action by lifecycle stage. If iterating, route to the iterations skill and name the iteration types most likely to refresh the signal.

## What never to do

- Never declare fatigue from a snapshot. Fatigue requires a trend.
- Never kill an ad over a single declining signal if profitability is still healthy.
- Never recommend "just spend more" on a late-fatigue ad. The signals are saying the audience is saturated; more spend on the same creative makes it worse.
- Never skip the exclusion-list hygiene check when frequency is the lead signal.
