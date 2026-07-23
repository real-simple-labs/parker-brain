---
summary: "Plain-language definitions of the Meta ad metrics Parker reads — what each measures, how it's calculated, and how to read it in the account, organized by category."
doc: ad-metrics-glossary
last_updated: 2026-07-11
---

# Ad Metrics Glossary

This is the **reference glossary** for the metrics Parker reads inside a Meta ad account — what each one measures, how it's calculated, and, where it matters, how to read it. It is a lookup, not a how-to. The *how* — reading an account end to end, judging scale vs. behavior, and diagnosing a single ad — lives in [ad-account-analysis.md](ad-account-analysis.md), and the attribution mechanics that shape what these numbers appear to show live in meta-attribution.md. When a definition here and the reasoning in those docs overlap, this doc owns the definition and they own the read.

Two things to carry before you use any number below:

- **Targets are brand-specific.** Target CPA, new-customer CPA, and ROAS goals depend on the brand's margins, AOV, LTV, and stage. A supplement brand and a luxury-apparel brand can both be healthy at completely different numbers. Parker knows each brand's KPI targets from its context; read every cost-and-return metric against *that brand's* reality, not a universal bar.
- **Benchmarks are starting points, not laws.** The rule-of-thumb numbers in this doc (CTR, frequency, hook rate, hold rate) are reasonable defaults for D2C, but they move by category, price point, funnel stage, and objective. Treat them as a place to start a read, not a pass/fail line.

---

## Table of Contents

1. Account Structure
2. Campaign Objectives & Optimization
3. Budget & Bidding
4. Attribution
5. Delivery & Auction
6. Spend & Profitability Metrics
7. Click & Traffic Metrics
8. Conversion & Funnel Metrics
9. Engagement Metrics
10. Video Metrics
11. Reach & Frequency Metrics
12. Cost-Per-Action Metrics
13. Placements
14. Breakdowns & Audience Analysis
15. Creative & Ad Formats
16. Audiences
17. Pixel, Events & Tracking
18. Advantage+ & Automation

---

## 1. Account Structure

**Ad Account** — The billing and organizational container that holds campaigns, ad sets, and ads. Each account has its own pixel, payment method, and permissions.

**Business Manager / Meta Business Suite** — The top-level tool for managing multiple ad accounts, pages, pixels, and team access.

**Campaign** — The top level of an ad's structure. This is where you set the objective (what you want Meta to optimize for).

**Ad Set** — The middle level. Controls audience targeting, budget, schedule, placements, and the optimization event.

**Ad** — The bottom level. The actual creative (image, video, copy, headline, CTA) that users see.

**Campaign ID / Ad Set ID / Ad ID** — Unique numeric identifiers Meta assigns to each level for tracking.

---

## 2. Campaign Objectives & Optimization

**Objective** — What you're telling Meta to optimize for at the campaign level. The modern objectives are: Awareness, Traffic, Engagement, Leads, App Promotion, and Sales.

**Sales Objective** — The most common D2C objective. Optimizes for purchases (or another chosen conversion event).

**Optimization Event** — The specific action Meta's algorithm tries to drive at the ad set level (Purchase, Add to Cart, Lead, Landing Page View, etc.).

**Conversion Event** — The action tracked as a "result" (usually a Pixel or Conversions API event like Purchase).

**Conversion Location** — Where the conversion happens (Website, App, Messenger, Calls, etc.).

> The objective and optimization event you choose shape both delivery and how the numbers should be read. The deeper treatment of what each objective does to creative and performance reads lives in conversion-objectives.md.

---

## 3. Budget & Bidding

**Daily Budget** — The average amount you're willing to spend per day on an ad set or campaign.

**Lifetime Budget** — Total budget spent across the campaign's schedule.

**Weekly Budget** — A newer flexible budget option Meta has been rolling out.

**Advantage Campaign Budget (ACB / CBO)** — Meta distributes the campaign budget across ad sets automatically to maximize results.

**Bid Cap** — Manual bid ceiling telling Meta the maximum you'll pay per optimization event.

**Cost Cap** — You tell Meta the average cost per result you're willing to pay.

**Lowest Cost (Highest Volume)** — Default bid strategy. Meta gets you as many results as possible for your budget.

**ROAS Goal** — Bid strategy where you tell Meta the minimum return on ad spend you'll accept.

**Pacing** — How Meta spreads your budget across the schedule so you don't spend it all in an hour.

---

## 4. Attribution

**Attribution Setting** — The rules that decide which ad gets credit for a conversion and within what time window.

**Click-Through Attribution** — Counts a conversion if it happens within a set number of days after someone clicked your ad. Options: 1-day click, 7-day click.

**View-Through Attribution** — Counts a conversion if it happens within 1 day after someone saw your ad but didn't click.

**Engaged View Attribution** — Counts a conversion after someone watched at least 10 seconds of your video ad within 1 day.

**7-Day Click / 1-Day View** — The most common default attribution window for D2C.

**Incremental Attribution** — A newer setting where Meta uses machine learning to credit only conversions it predicts wouldn't have happened without the ad.

**Attribution Window** — The time period during which a click or view can be credited to your ad.

**On-Ad Actions** — Actions that happen directly on the ad itself (video views, reactions, shares).

**Off-Ad Actions** — Actions that happen after leaving the ad (website purchases, sign-ups).

**Aggregated Event Measurement (AEM)** — Meta's iOS 14+ compliant attribution framework, which limits you to 8 events per domain and uses modeled data.

> Attribution is not a side detail — the setting a brand runs changes what every conversion metric below appears to say. Two accounts with identical creative can read differently because one counts 1-day-view and the other doesn't. The full mechanics, and how to reason about them when reading an account, live in meta-attribution.md.

---

## 5. Delivery & Auction

**Auction** — Every ad impression is decided by an auction. The winner is the highest total value (bid + estimated action rate + ad quality).

**Learning Phase** — The initial period (usually the first 50 conversion events) where Meta is figuring out who to show your ad to. Performance is unstable here, so don't judge an ad mid-learning.

**Learning Limited** — Status when an ad set isn't getting 50+ optimization events per week, so Meta can't fully optimize.

**Delivery Status** — Whether an ad is Active, Paused, In Review, Rejected, or Not Delivering.

**Ad Fatigue** — When frequency climbs and performance drops because your audience has seen the ad too many times.

**Breakdown Effect** — When Meta shifts budget to what *looks* like a higher-CPA placement or ad but is actually the correct move, because Meta predicts where costs will rise and pivots ahead of them. This is why a higher-spend ad at a lower ROAS is often the real winner over a tiny-spend ad at a flashy ROAS — the small one hasn't been tested at scale. This effect is the single most misread thing in an account; the full explanation and how to evaluate at the aggregate level is in [ad-account-analysis.md](ad-account-analysis.md).

**Inflection Point** — The moment during a campaign when costs on one placement or ad start rising faster than another, triggering Meta to reallocate spend.

---

## 6. Spend & Profitability Metrics

**Amount Spent** — Total dollars spent on an ad, ad set, or campaign in the selected date range.

**Purchases** — Number of purchase events attributed to the ad.

**Purchase Value / Purchase Conversion Value** — Total revenue attributed to purchases from the ad.

**CPA (Cost Per Acquisition) / CPP (Cost Per Purchase)** — The same metric: spend ÷ purchases. The core profitability metric for D2C, read against the brand's own target.

**NC CPA (New Customer CPA)** — Cost per *new* customer purchase, excluding returning customers. Requires a custom conversion set up in the account. For many scaling brands this is the truer north-star than blended CPA, because it measures what acquisition actually costs.

**ROAS (Return on Ad Spend)** — Purchase value ÷ spend. A 3x ROAS means $3 back for every $1 spent.

**Purchase ROAS** — Same as ROAS, specifically for purchase events.

**AOV (Average Order Value)** — Purchase value ÷ number of purchases.

**MER (Media Efficiency Ratio)** — Total revenue ÷ total ad spend across all channels. A board-level blended metric, not native to Meta.

**Contribution Margin** — What's left after COGS, shipping, and ad spend. The actual profitability number, and the one that tells you whether a "good" ROAS is really good for this brand.

---

## 7. Click & Traffic Metrics

**Impressions** — Number of times your ad was displayed on screen. Includes repeats to the same person.

**Clicks (All)** — Every click on the ad — link clicks, likes, comments, profile clicks, expansions, and more. A noisy metric.

**Link Clicks** — Clicks on links that go somewhere (website, app store, Messenger).

**Outbound Clicks** — Clicks that take users off Meta's platforms to your site. More meaningful than all-clicks.

**Landing Page Views (LPV)** — The moment someone lands on your site *and* the pixel fires. Better than link clicks because it filters out drop-offs and slow-loading pages.

**CTR (Click-Through Rate)** — Clicks ÷ impressions.

**Outbound CTR** — Outbound clicks ÷ impressions. Around 1%+ is a common target. A low outbound CTR usually means the CTA or the offer isn't strong enough to move people off the platform.

**Unique Clicks** — Number of unique people who clicked (dedupes multiple clicks from the same person).

**CPC (Cost Per Click)** — Spend ÷ clicks.

**Cost Per Link Click** — Spend ÷ link clicks. More useful than raw CPC for traffic analysis.

**Cost Per Landing Page View** — Spend ÷ LPVs. The truest "cost to get someone onto your site."

---

## 8. Conversion & Funnel Metrics

**Add to Cart (ATC)** — Number of ATC events attributed to the ad.

**Cost Per Add to Cart** — Spend ÷ ATCs.

**Initiated Checkout / Checkouts Initiated** — Number of times someone started checkout.

**Cost Per Checkout** — Spend ÷ checkouts initiated.

**Conversion Rate (CR)** — Percentage of people who saw the ad and converted on the website. A low CR can point to a creative problem *or* a website/UX problem — worth checking both before blaming the ad.

**Purchase Rate** — Purchases ÷ clicks (or ÷ LPVs, depending on how it's measured).

**Funnel Ratios** — Click-to-ATC, ATC-to-Purchase, Click-to-Purchase, Checkout-to-Purchase. These reveal *where* people drop off, which tells you whether the fix is creative, offer, or site.

**Leads** — Number of lead events (form submissions, sign-ups).

**Cost Per Lead (CPL)** — Spend ÷ leads.

---

## 9. Engagement Metrics

**Post Reactions** — Likes, loves, wows, and so on, on the ad.

**Post Comments** — Comments on the ad.

**Post Shares** — Times the ad was shared by users.

**Post Saves** — Times users saved the ad.

**Page Likes** — New page follows attributed to the ad.

**Post Engagement** — Total engagement (reactions + comments + shares + saves + clicks).

**Engagement Rate** — Engagement ÷ impressions or reach.

**Cost Per Save** — Spend ÷ saves. A low cost per save means the ad resonated enough that people wanted to come back to it.

**Cost Per Share** — Spend ÷ shares. A low cost per share means free organic exposure; a very high one means almost nobody shared it.

**Cost Per Engagement** — Spend ÷ total engagement.

**Messaging Conversations Started** — For click-to-Message ads.

---

## 10. Video Metrics

**Video Plays** — Total number of times the video started playing.

**3-Second Video Views** — Number of times the video was watched for at least 3 seconds.

**ThruPlays** — Video watched to completion, or at least 15 seconds if it's longer.

**Hook Rate** — Percentage of impressions where the viewer watched the first 3 seconds. A common benchmark is 30%+ minimum, ideally 45–50%. It tells you whether your first frame is stopping the scroll.

**Hold Rate** — Percentage of impressions that watched the full video. A common benchmark is 12–15%+. It tells you whether you're keeping attention after the hook.

**Video Average Play Time** — Average duration viewers watched before dropping off.

**Video Play at 25% / 50% / 75% / 95% / 100%** — Number of viewers who reached each milestone.

**Retention Curve** — The shape of viewer drop-off across the video timeline. Reading where the curve falls off tells you which moment lost people.

**First Frame Retention** — Percentage of viewers who stayed past the very first frame.

**Cost Per ThruPlay** — Spend ÷ thruplays.

**Cost Per 3-Second View** — Spend ÷ 3-second views.

---

## 11. Reach & Frequency Metrics

**Reach** — Number of *unique* accounts that saw your ad at least once.

**Impressions** — Total times shown, including repeats.

**Frequency** — Impressions ÷ reach. The average number of times each person saw your ad. A common target is around 1.2 or lower for prospecting; high frequency (3–4+) usually means you're hitting the same people instead of reaching new ones.

**CPM (Cost Per 1,000 Impressions)** — Spend ÷ (impressions ÷ 1,000). What you pay per 1,000 ad views.

**Cost Per 1,000 Accounts Reached (CPMR)** — Spend ÷ (reach ÷ 1,000). What you pay to reach 1,000 unique accounts. If CPM is low but CPMR is high, you're showing to the same audience over and over.

**Estimated Ad Recallers** — Modeled number of people likely to remember your ad within 2 days.

---

## 12. Cost-Per-Action Metrics

**Cost Per Purchase** — Spend ÷ purchases. Same as CPA.

**Cost Per New Customer Purchase (NC CPA)** — Spend ÷ new customer purchases.

**Cost Per Add to Cart** — Spend ÷ ATCs.

**Cost Per Initiated Checkout** — Spend ÷ checkouts.

**Cost Per Landing Page View** — Spend ÷ LPVs.

**Cost Per Lead** — Spend ÷ leads.

**Cost Per Page Like** — Spend ÷ new page likes.

**Cost Per Outbound Click** — Spend ÷ outbound clicks.

**Cost Per Messaging Conversation** — Spend ÷ conversations started.

---

## 13. Placements

**Placement** — Where the ad appears within Meta's platforms.

**Advantage+ Placements (Automatic)** — Meta chooses placements for you. Usually the recommended default.

**Manual Placements** — You pick specific placements.

**Facebook Feed** — Ads in the main FB scroll. Skews older, more deliberate engagement.

**Instagram Feed** — Ads in the main IG scroll. Younger, more visual, aspirational.

**Facebook Reels** — Short-form video on FB. More casual, incidental viewing. Cheap CPMs but shallower attention.

**Instagram Reels** — Short-form vertical video on IG. High-intent entertainment consumption, young and trend-driven.

**Facebook Stories** — Ephemeral vertical content on FB. Passive viewing, older skew, upper-funnel.

**Instagram Stories** — Ephemeral vertical content on IG. Habitual viewing, higher intent, more interactive.

**Facebook Marketplace** — Ads in the Marketplace tab.

**Instagram Explore** — Ads in the discovery/Explore feed.

**Audience Network** — Ads shown on third-party apps and sites outside Meta.

**Messenger** — Ads in the Messenger inbox and stories.

**Threads** — A newer placement for Meta's Twitter-alternative.

> Placement is signal, not just a setting: where an ad delivers and how it performs there tells you something about the creative and the audience. How to read the placement breakdown as evidence lives in placement-signals.md.

---

## 14. Breakdowns & Audience Analysis

**Breakdown** — Slicing metrics by a specific dimension (age, gender, placement, device, and so on).

**Age Breakdown** — Spend/results by age bracket (18–24, 25–34, 35–44, 45–54, 55–64, 65+).

**Gender Breakdown** — Spend/results by Male, Female, Unknown.

**Placement Breakdown** — Spend/results by placement.

**Device Breakdown** — Mobile vs. desktop split.

**Platform Breakdown** — Facebook vs. Instagram vs. Messenger vs. Audience Network.

**Geo/Region Breakdown** — Spend/results by country, state, or DMA.

**Time Breakdown** — Day or hour of the week performance.

**Delivery Breakdown** — Where Meta chose to deliver based on the algorithm's predictions.

**Action Breakdown** — Breaking results down by conversion event type.

> Read breakdowns against the breakdown effect (Section 5). A slice that looks like a loser at the segment level can be the correct allocation at the aggregate level.

---

## 15. Creative & Ad Formats

**Ad Creative** — The actual media (video, image, carousel) plus copy.

**Static / Image Ad** — Single image creative.

**Video Ad** — Video creative.

**Carousel Ad** — Multiple swipeable images or videos in one ad.

**Collection Ad** — Mobile format with a hero image/video and product tiles.

**Instant Experience** — Full-screen mobile experience that opens when someone taps an ad.

**Dynamic Product Ads (DPA) / Advantage+ Catalog Ads** — Ads that pull products from your catalog and personalize per user.

**Headline** — The bolded text above or below the creative, usually short and punchy.

**Primary Text / Body Copy** — The main text above the creative.

**Description** — Optional text below the headline.

**CTA (Call to Action)** — The button on the ad ("Shop Now," "Learn More," "Sign Up," and so on).

**Ad Copy** — The written text portion of the ad.

**Hook** — The first 3 seconds of a video ad, or the first thing seen in a static. Determines whether the scroll stops.

**UTM Parameters** — Query strings appended to your ad URL for tracking in GA or other tools.

---

## 16. Audiences

**Core Audience** — Targeting based on demographics, interests, and behaviors.

**Custom Audience** — Audience built from your own data (email list, website visitors, video viewers, and so on).

**Lookalike Audience (LAL)** — People similar to a source audience. Usually sized 1–10% of a country's population.

**Value-Based Lookalike** — A lookalike weighted by customer LTV.

**Retargeting Audience** — People who've interacted with your brand before (site visitors, cart abandoners, past purchasers).

**Advantage+ Audience** — Meta's AI-driven audience suggestions where you provide loose targeting inputs.

**Broad Targeting** — Minimal or no targeting inputs, letting Meta's algorithm find your buyer.

**Exclusions** — Audiences you exclude (past purchasers, current employees, and so on). Important for keeping frequency low and finding new customers.

**Audience Overlap** — How much two audiences share the same people, which can cause you to compete against yourself in the auction.

**Estimated Audience Size** — Meta's forecast of how many people match your targeting.

---

## 17. Pixel, Events & Tracking

**Meta Pixel** — A snippet of code on your website that tracks visitor actions and sends the data to Meta.

**Conversions API (CAPI)** — Server-side event tracking that supplements the pixel. Important after the iOS 14 changes.

**Standard Events** — Pre-defined events (PageView, ViewContent, AddToCart, InitiateCheckout, Purchase, Lead, and so on).

**Custom Events** — Events you define yourself.

**Custom Conversions** — Filtered versions of standard events (for example, a Purchase where the URL contains "/thank-you-newcustomer").

**Event Match Quality (EMQ)** — A score (0–10) rating how well your events match to users. Higher means better attribution.

**Deduplication** — Preventing the pixel and CAPI from double-counting the same event.

**Domain Verification** — Proving you own the domain so you can control event prioritization under iOS 14+.

---

## 18. Advantage+ & Automation

**Advantage+ Shopping Campaigns (ASC)** — Meta's automated campaign type for e-commerce. Combines audiences, placements, and creative optimization.

**Advantage+ Creative** — Meta auto-transforms your creative (adds music, adjusts aspect ratio, tries variations).

**Advantage+ Audience** — Meta expands beyond your targeting inputs when it predicts better results.

**Advantage+ Placements** — Meta chooses all placements automatically.

**Dynamic Creative Optimization (DCO)** — Meta mixes and matches multiple headlines, images, videos, and CTAs to find the best combinations per user.

**Existing Customer Budget Cap** — In ASC, the percentage of budget you allow to go to existing customers vs. new customers.

---

## Quick Reference: Rule-of-Thumb Benchmarks

These are D2C starting points, not universal pass/fail lines. Every category, price point, and funnel stage moves them, and each brand's KPI targets override them. Use them to *start* a read, then judge against the brand's own reality.

| Metric | Starting-point benchmark |
|--------|--------------------------|
| Outbound CTR | Around 1%+ |
| Frequency | ~1.2 or lower (prospecting) |
| Hook Rate | 30%+ minimum, ideally 45–50% |
| Hold Rate | 12–15%+ |
| Learning Phase | 50 conversion events per week per ad set |

---

## Related docs

- [ad-account-analysis.md](ad-account-analysis.md) — how to actually read an account: scale vs. behavior metrics, the breakdown effect in full, and diagnosing a single ad.
