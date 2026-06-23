---
candidate_id: 2026-06-03-creative-forecasting-volume-hit-rate-churn-context-updates
source_signal: 2026-06-03-youtube-creative-forecasting-volume-hit-rate-churn
source_path: global/knowledge/creative-strategy/expert-insights/inbox/2026-06-03-creative-forecasting-volume-hit-rate-churn.md
status: candidate
created: 2026-06-03
owner_team: creative-strategy
---

# Context update candidates - Creative forecasting volume, hit rate, churn, and half-life

## Candidate summary

This source introduces a distinct framework Parker should preserve: creative volume can be forecast from spend target, average spend per winning asset, current winners, churn, hit rate, and buffer. It also gives Parker a cleaner way to diagnose whether a brand has a creative volume problem or a creative quality problem.

This should not become a rigid formula everywhere yet. It should become a candidate method for ad-account evaluation, performance planning, quarterly audits, and performance reports.

## Proposed context updates

### 1. Ad-account evaluation - add creative inventory mechanics

**Target path:** `prompts/brand-profile/ad-account-evaluation.md`  
**Proposed change:** Add a creative-inventory read that checks current winners, winner half-life, churn rate, hit rate, test tax, and whether creative volume is sufficient for the spend target.  
**Evidence:** The source frames creative as a portfolio of winners, decaying assets, and tests.  
**Confidence:** mixed  
**Promotion condition:** Apply after Jimmy approves or Parker validates the metrics in a live account.

### 2. Performance targets and metrics - connect spend targets to creative requirements

**Target path:** `prompts/brand-profile/performance-targets-and-metrics.md`  
**Proposed change:** Add a watch item that spend forecasts should have a matching creative forecast when Meta is a major growth channel.  
**Evidence:** The source argues that brands often forecast revenue and spend but not the creative volume required to support that spend.  
**Confidence:** mixed  
**Promotion condition:** Apply when performance-targets doc gets its next update, because this is aligned with the doc's scoreboard role.

### 3. Quarterly creative strategy audit - distinguish under-volume from low-quality

**Target path:** `prompts/audits-quarterly/90-day-creative-strategy-audit.md`  
**Proposed change:** Add a diagnostic distinction between a brand that needs more creative volume and a brand that needs higher hit rate before scaling volume.  
**Evidence:** The source describes one account with strong win rate but insufficient volume, and one with high volume but poor hit rate.  
**Confidence:** mixed  
**Promotion condition:** Apply after another account or expert source corroborates the distinction, or Jimmy approves.

### 4. Monthly performance report - add creative test tax and winner replacement watch

**Target path:** `prompts/audits-monthly/monthly-performance-report.md`  
**Proposed change:** Add watch-only language for test tax, winner churn, and whether new launches are replacing lost winning inventory.  
**Evidence:** The source uses test tax and churn to explain wasted creative spend and asset replacement needs.  
**Confidence:** mixed  
**Promotion condition:** Keep as candidate until the monthly performance report scope is reviewed.

### 5. Ad-account-analysis skill - candidate creative forecast process

**Target path:** `skills/ad-account-analysis/processes/account-audit.md`  
**Proposed change:** Add a candidate process for creative forecasting when the user asks about scaling, resourcing, creative volume, or why spend cannot grow. Inputs: target spend, average spend per winning asset, current winners, churn, hit rate, buffer. Output: required launches per period.  
**Evidence:** The source gives a worked example for calculating required launch volume.  
**Confidence:** mixed  
**Promotion condition:** Apply if Jimmy wants Parker to operationalize the forecasting method.

### 6. Persona docs - reinforce persona as the bridge from forecast to strategy

**Target paths:** `prompts/personas/personas-profile.md`; `prompts/brand-profile/customer-and-persona-discovery.md`  
**Proposed change:** Add this source as corroborating evidence for the earlier macro/micro persona candidate. Personas should inform not only messaging, but creative volume allocation, format mix, and diversity planning.  
**Evidence:** The source describes personas, micro-personas, angles, messages, and vehicles as the way a volume target becomes an execution plan.  
**Confidence:** mixed; same source-family corroboration, not independent proof  
**Promotion condition:** Update the existing persona candidate rather than creating a separate persona candidate.

### 7. Iterations strategy - connect launch volume to diversity

**Target path:** `skills/iterations/strategy.md`  
**Proposed change:** Add a candidate principle: increasing launch volume only helps if the iterations create real diversity across persona, message, format, angle, and awareness stage.  
**Evidence:** The source warns that many brands are not running 100 different ads but the same ad 100 times.  
**Confidence:** mixed  
**Promotion condition:** Apply with the next iterations skill refresh.

## Existing context surfaces updated

- Updated `2026-06-03-meta-2026-creative-scaling-persona-remix.md` to note this source as same-source-family reinforcement for macro/micro persona and persona-led creative diversity.
- Updated `patterns-to-monitor/INDEX.md` with creative forecasting, hit-rate vs volume diagnosis, test tax, and winner churn.

## Status

Candidate created. No canonical prompt or brand context doc has been rewritten from this source alone.
