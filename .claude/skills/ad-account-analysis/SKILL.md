---
name: ad-account-analysis
description: Analyze Meta ad account data — read what's spending, what's converting, what's fatiguing, and where the audience is being reached. Use when the user wants an account audit, a single-ad diagnosis, a placement read, a demographic breakdown, or a fatigue check.
triggers:
  - analyze my ad account
  - what's working in the account
  - what's the top spender
  - is this ad fatiguing
  - is this ad ready to scale
  - what does the data tell me
  - read my Meta account
  - audit this ad
  - which ads should I turn off
  - where is my spend going
---

# Ad Account Analysis

## Goal

Read what the Meta data is actually saying about the account, an ad, or a slice of the audience. Account data tells two intertwined stories — whether ads are scaling profitably, and how the ads are behaving in the Meta ecosystem in terms of attention and audience reach. The skill reads both stories, decides which one the user needs, and delivers a diagnosis with specific actions.

This skill does not write ads, generate iterations, or build briefs. If the user wants iteration recommendations off the analysis, route to the iterations skill. If they want a script or static built from a diagnosis, route to the scriptwriting or static-ads skill.

## What you are working from

This skill reads the account through the canonical methods, not from general knowledge. Before analyzing, load what `parker-system/creative-strategy-context/expertise-routing.md` names for an own-account read: `ad-account-analysis.md`, the canonical reading method; `killer-performance-ads.md`, the bar a winner is graded against; and `andromeda-v2.md`, so delivery patterns read as Meta auction mechanics rather than mysteries. The tools that pull the data, and what each returns, are inventoried in `parker-system/system/parker-tools.md`. When the read compares how cohorts of ads acquire, the cohort-efficiency discipline in `creative-strategy-fundamentals.md` applies: spend-weight the comparison and classify off the account's own creative tags, never best-ad-vs-best-ad. The diagnosis is performed through these methods, in their vocabulary — a read that never speaks their named concepts skipped them.

## Background that loads up front

Two pieces of background context every account analysis depends on. Both are defined in full in `ad-account-analysis.md` — that doc is the source of truth, including the worked breakdown-effect example and the full attribution-window list. What follows is only the must-surface summary so the read never forgets them. Parker assumes both, but if the user's question hinges on either, surface them explicitly.

### The breakdown effect

Meta's delivery system shifts budget toward whichever ad set, placement, or ad is predicted to drive the most efficient outcomes over the campaign duration, not over the moment Parker happens to look at the data. That means a placement or ad that currently shows a higher CPA may be the right place for budget because Meta predicted its costs would rise more slowly than the alternative. Reporting in Ads Manager can therefore look like Meta made the wrong call when it actually did not. Always evaluate at the level appropriate to the campaign structure — at the campaign level for Advantage+ campaign budget, at the ad set level for automatic placements, at the ad set level when multiple ads sit in one ad set.

### Attribution

Different attribution settings count conversions differently. Click-through credits actions within one or seven days of a click. View-through credits actions within one day of an impression. Engaged view credits actions after ten seconds of video play. Standard attribution combines a window with a behavior. Incremental attribution optimizes for conversions the model predicts the ad caused. The brand's chosen attribution setting changes which numbers tell the truth. If the user has changed attribution settings between two periods, account-level comparisons mean different things.

## How this skill runs

1. **Identify what the user is actually asking.** Run the strategy doc. Are they asking for a full account audit, a single-ad diagnosis, a placement read, a demographic breakdown, or a fatigue check? Different questions trigger different processes.

2. **Pull the data needed for the chosen process.** Each process has its own required-input list. Pull only what is needed.

3. **Apply both lenses — profitability and user behavior.** Every analysis must consider both whether the ad is making money (profitability metrics) and how the ad is being received in the ecosystem (engagement metrics). Single-lens analysis misses the picture.

4. **Diagnose, do not just report.** The output is not a metrics dump. The output is the read — what is true about the account or ad, what is the explanation, what should the team do next.

5. **Format the output per the structure below.**

## Output structure

### 1. The Headline Read

Two to four sentences. Plain language. State what the data is saying and what the user should do about it. No jargon. If the answer is "this ad is fatiguing and should be iterated within two weeks," say that.

### 2. The Diagnosis

The supporting evidence. Specific numbers compared against account benchmarks. Both lenses present — profitability and user behavior. Tied to the actual question the user asked.

### 3. Recommended Next Steps

Action items, prioritized. Each item names what to do and why, tied to the diagnosis. If the next step is running a different skill (iterations, scriptwriting), name the skill.

### Brand Context Applied

What brand-specific KPIs were used to define "winning," what compliance or operational constraints shaped the read, and why the diagnosis fits the brand's current situation.

## Hard rules

- **Do not interpret a single metric in isolation.** Profitability without engagement signal is half the story. Engagement signal without profitability is the other half. Pair them.
- **Never recommend turning off an ad on the basis of slightly elevated CPA alone.** If the ad is still profitable at the brand's KPI definition, it stays on. Slight variance on top spenders is normal.
- **Do not be deceived by high ROAS on low spend.** A small ad with ROAS 5 on $30 is not winning the same way a top spender at ROAS 1.5 on $300 is winning. Spend volume × ROAS is the truth, not ROAS in isolation.
- **Account for the breakdown effect before flagging "Meta is misallocating budget."** The system is optimizing over the campaign duration. Apparent missteps in the current snapshot often correct over time.
- **Account for attribution settings before comparing periods.** If the brand changed attribution settings, period-over-period comparisons are not apples to apples.
- **Frequency benchmark is 1.2 or lower.** Higher frequency means the same eyeballs are being repeatedly hit, which is a saturation signal, not a reach signal. Account exclusions matter too — flag exclusion list hygiene if frequency is climbing.
- **Hook rate benchmark is 30% minimum.** Hold rate benchmark is 12% minimum. Below those, the ad is fundamentally not earning attention or not holding it.
- **The placement breakdown tells you who the audience is, not just where the ad is shown.** Heavy Facebook delivery signals older. Heavy Instagram Reels signals younger and trend-driven. Use placement as a proxy for audience read when demographics breakdowns are unavailable.
