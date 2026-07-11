---
summary: "How to read own ad-account data — the two kinds of metrics and what the numbers actually mean for creative decisions."
---

# Analyzing Ad Account Data

When analyzing ad account data, we are looking at two different types of metrics:

First and foremost, when creating ads, we want to be creating ads that are able to scale and hit relevant KPIs. Relevant KPIs will be different for each brand and even industry. So a brand that's selling make-up will have a very different target CPA compared to a very high-end enterprise SaaS product. Keep that in mind. You will know key performance metrics for each of the brands you're analyzing with, so this shouldn't be an issue for you to decipher when looking at the ad account.

The second thing that you need to know besides scale are metrics that tell us how the ad is behaving in the ad ecosystem on Meta. This essentially means that certain metrics tell us a story of how people are perceiving the ad. Is it engaging? Is it scroll-stopping? Does it reach new audiences? Does it reach warmer or colder audiences?

As a caveat, you need to know that not all performance marketers will only look at ad account data. This is because Facebook has one system of attribution. However, if there is another tool involved, then software that does the attribution for each marketing channel might have different data than Facebook. This shouldn't concern you because you will be only tasked to analyze ad account data, meaning numbers that are pulled directly from Meta's platform.

Before we dive into metric-specific things, you will need to understand two things:

1. You need to understand the breakdown effect
2. You need to understand attribution on Meta

I will provide you with documentation from Meta on both of these things. Always keep them in mind when looking at the ad because sometimes clients will use different attribution models, different attribution settings, and they will optimize for different things. So you need to keep that in mind.

## Breakdown Effect

The "breakdown effect" refers to the misinterpretation that our system shifts impressions and spending into underperforming ad sets, placements or ads.

In reality, the system is designed to maximise the number of results for your campaign dependent on the ad set optimisation you choose.

### How to evaluate ads results across Meta technologies

When using multiple ad sets, placements and ads, the best way to measure the efficiency of your campaign is by evaluating your results at the aggregate level. For example, when using Advantage+ campaign budget (also known as campaign budget, or budget with Advantage+ on), the system will optimise to deliver the highest number of results between the ad sets. This means that to properly evaluate success, you should evaluate results at the campaign level.

How to evaluate results with each automated solution in Meta Ads Manager:

- When using Advantage+ campaign budget, make sure that you evaluate your results at the campaign level.
- When using automatic placements (without Advantage+ campaign budget), evaluate your results at the ad set level.
- When running multiple ads in one ad set, evaluate your results at the ad set level.

### How the ads delivery system on Meta technologies works

It's important to understand how our delivery system works in order to properly judge the performance of your campaigns when using automation between ad sets, placements and ads.

There are two main components to consider:

- **Pacing:** Pacing is how we help ensure that we spend your budget evenly over the schedule of your ad set. There are only so many optimisation events that you can get for your budget over the duration of your campaign.
- **Automation:** Meta's delivery system uses machine learning to automate the delivery and management of impressions between ads, ad sets and placements to help maximise your results based on your inputs (such as creative, budget, audience and objective).

### The breakdown effect explained

The breakdown effect occurs where our pacing approach and our system's automation meet.

It's easiest to understand this effect by using an example. (Note: This example is simplified to illustrate the effect.)

Let's say you choose to run an ad campaign using the engagement objective. You choose two placements: Facebook Stories and Instagram Stories. Your total budget is USD 500 for this campaign.

When the campaign begins, our system starts to deliver ads to both placements to see which will drive the most efficient results for your target audience. This is called the learning phase.

Facebook Stories starts out driving cheaper acquisitions, but then our system identifies an inflection point at which the cost per acquisition (CPA) of Facebook Stories begins to exceed the CPA on Instagram Stories.

The cost per acquisition on Facebook Stories is USD 0.35 on the first day, compared to USD 0.72 on Instagram Stories. However, as the campaign continues, Instagram Stories receives more budget, even though it still has a higher cost per acquisition. At the end of the campaign, Instagram Stories delivered significantly more budget compared to Facebook Stories, even though Facebook Stories originally had a lower cost per acquisition.

Inflection point happens when costs for two of these placements meet, and then Facebook Stories costs begin to rise compared to Instagram Stories.

Prior to the inflection point (where Facebook costs were still lower than Instagram), the system may spend USD 50 on Facebook Stories and USD 50 on Instagram Stories to test. As the system can detect that Facebook Stories CPA was rising faster than Instagram Stories, it shifts the remaining budget of USD 400 to Instagram Stories to have a cheaper CPA over the duration of the campaign. In the table, you'll see that prior to Day 4, Facebook Stories achieved a lower CPA, but the costs would have grown faster than Instagram Stories. In the example above, Facebook Stories reached up to USD 5.30 by Day 10 while Instagram Stories was delivering at half the cost.

**Why?**

At the start of the campaign, the system began delivering ads to both platforms to explore where the lowest cost opportunities were through pacing. In the example, the system recognised that although Facebook Stories was driving the most efficient results initially, it predicted the cost was going to increase throughout the duration of the campaign. Based on the anticipated rising costs, the system was able to pivot and shift the budget to Instagram Stories in order to drive a more efficient average cost per acquisition for the duration of the campaign. As a result, the system made the decision most likely to drive the most efficient outcomes dynamically, driving more conversions.

This is where the reporting may not match your expectations. If you had only judged the decision by looking at the cost per acquisition in Ads Manager, it would show that less budget went to the lower average cost per acquisition placement, Facebook Stories. This may be confusing because it appears the decision was incorrect; however, the system pivoted the budget in real time to Instagram Stories which drove more results.

Our system will give you the most results for your budget when you create flexible campaigns through lowest-cost bidding, automatic placements and campaign budget optimisation features. The "breakdown effect" may lead to some confusion when interpreting ads manager campaign results, but ultimately it helps maximise performance and drive significantly more value to your campaigns.

## Attribution

When a person sees your ad on Facebook, Instagram or Meta Audience Network, there are several actions that they can take, such as watching a video in the ad or visiting your website or shop and buying a product.

To see the actions taken directly on your ad, such as a video view or link click, you can navigate to Meta Ads Manager and view the respective metric columns. For actions taken off your ad, such as a purchase on your website or shop, Meta attributes these actions to your ad if they happened within a specified number of days.

### Types of actions

- **Actions that occur on your ad:** Some actions can only happen directly on your ad and we show these actions in their respective columns in the reporting table in Ads Manager. For example, when someone views your ad and clicks on the ad, we will report one impression and one link click in the Impressions and Link clicks columns. Other examples of actions that only occur on your ad are: video views, post reactions and post shares.
- **Actions taken off your ad:** Actions taken off your ad, such as a purchase on your website or shop, are attributed back to your ad if they happened within a certain number of days after someone viewed or clicked on your ad. By default, we show these actions based on the attribution setting on the ad set level.
- **Actions that can happen on and off your ad:** Some actions can be taken both on and off your ads. For example, if you're running an ad to promote an event, people can select Going/interested directly on the ad or they can click on the ad, visit the event page and then select Going/interested on the event page.

If you change your attribution windows to show view-through and click-through, you will see a column for "on ad" actions in addition to the columns for view-through and click-through attribution. The "on ad" metric column will show all the actions that happened directly on your ad, while the columns broken down by attribution windows will show "off ad" actions.

### Standard attribution settings

The standard attribution setting allows advertisers to choose whether to credit a conversion based on ad impressions, clicks (all) or video plays. Advertisers can also select in what time period to credit these conversions and results.

You can choose your attribution setting at the ad set level when you create a campaign in Meta Ads Manager. The standard attribution settings that we support currently are:

- **Click-through:** Counts results after any click occurs on your ad within one day or seven days of an optimised conversion. Clicks may include interactions such as likes, shares and saves.
- **View-through:** Counts results after an ad impression was counted within one day of an optimised conversion.
- **Engaged view:** Counts results after a video is played for at least ten seconds within one day of an optimised conversion.
- **Standard attribution:** Optimise delivery for a selected time window and either click or view behaviour, such as 7-day click or 1-day view.
- **Incremental attribution:** Optimise delivery for incremental conversions using models that predict whether a conversion is caused by an ad.

For certain types of campaigns, not all attribution settings will be available. These include:

- iOS 14 and above app re-engagement campaigns using Meta's attribution, also known as Aggregated Event Measurement, which reports using 1-day or 7-day click attribution, depending on the attribution setting you chose in Ads Manager.
- iOS 14 and above app install campaigns using Meta's attribution, which reports using 1-day or 7-day click, depending on the attribution setting you chose in Ads Manager. For iOS 14 and above app install campaigns using SKAdNetwork, the attribution setting for these campaigns will be reporting using "From Apple's SKAdNetwork".

Incremental attribution is an attribution setting that optimises ad delivery for incremental conversions using machine learning models that predict whether a conversion is caused by an ad. Understanding how many conversions are incremental can help you better understand the outcomes of your advertising.

With incremental attribution, you can: focus campaigns on outcomes that are more likely to be directly driven by an ad and potentially drive more incremental conversions compared to your existing campaigns.

---

## Ad Account Analysis

Now that you understand attribution and breakdown effect, we are going to focus on ad account analysis. Our roadmap looks like this:

### 1. Determine which creative is taking up most of the spend in the account

You are looking for a TOP SPENDING AD. It's easily detectable. We focus on spend because Meta's own system predicted the highest spending ad is the most potent ad in the account at any given time — this is also easily explained in the breakdown effect section.

### 2. Determine if the creative with the highest spend is optimizing for and hitting our KPIs

In practice, this means that our highest spender (or spenders — at any given time you can be instructed to pull up top 5 spenders in the account) is hitting our primary KPIs.

KPIs (key performance indicators) are different for each client. In B2C / D2C / ecommerce space, this is in 99% of the cases CPA (Cost per Action — in which action is purchase). Most of the businesses have a certain threshold when it comes to their optimal CPA.

Because these businesses expect their business to grow with us, most of them are also optimizing for NC CPA — which is CPA for NEW CUSTOMERS. Most of the ad accounts which optimize for this already have this metric in the ad account, and you can see it.

Even if you can't see this in the ad account as a custom metric, you'll be provided with primary KPIs you can use for ad account analysis or top spenders.

Next up, you'll determine if the top spending ad or top spenders are hitting those KPIs. So if our target KPI is NC CPA of $45, you want to see if this creative is hitting that goal. Another example here would be that creative may be the top spender. It can have a CPA of $50, $40, $35, or even $55. If this creative is taking up a lot of the spend, we can still count it into a winning ad. It's different for each of the businesses how much variance we can have here. For example, if we are talking about a skincare brand and the CPA is slightly higher than what we want to see, it can be tolerated on high spend levels. So you shouldn't disregard an ad just because the CPA is slightly higher as in the example I provided.

You shouldn't recommend turning off an ad simply because the CPA is slightly higher. If we are still profitable, the ad should keep running and the ad should be counted as a winner.

So, after you've determined which creatives are top spenders, now I'm going to tell you which other metrics you should be looking at. I will be sharing a table of metrics with you that you should be looking at at all times in the account.

I will show you two tables. One will represent the profitability of an ad, and you will use these metrics to analyze if the ad is bringing in money and new customers.

### Profitability metrics table

- Amount spent
- Number of purchases
- Cost per purchase
- Number of new customer purchases (this is a custom conversion in Ads Manager)
- Cost per new customer purchase
- Purchase ROAS (the total return on ad spend from purchases)

This is the most standard way that you will be looking at ad profitability:

- We want to have a sustainable amount spent, which means that the ad is taking up a lot of spend not only daily, but week over week (since as of recently Meta is introducing more and more weekly budgets, allowing more flexibility with weekly budgets).
- We need to have a sustainable number of purchases, which means that the ad is getting people to convert from our ad.
- Those purchases need to be in a profitable range.
- All of this will result in ROAS hitting the KPI goal.

You shouldn't be deceived by high ROAS in the account. For example:

One ad can have $30 in spend and ROAS 5, another ad can have $300 and be the top spender in the account with ROAS 1.5. You need to understand that the ad that spent more ($300) and had a lower ROAS is the winner here for the obvious reasons of $300 x 1.5 being higher than $30 x 5. Just because you see a high ROAS number, that doesn't mean that the ad is doing well.

Here's a little bit of more context for this. Let's say an ad has spent $30 for 5 days and is generating a ROAS of 5, it generated a lot of purchases as well. However, what is going to happen with this ad in the very foreseeable future is that it's going to dry out really quickly.

These ads that have low spend and sudden high number of purchases or higher ROAS and even low CPA usually tend to dry out very quickly. That is because these ads pick up the low hanging fruit. They convert people that would most likely convert anyway, and then they just took all the credit for it. A lot of times you will find high frequency in these ads which indicates that they did not reach a new audience. However, you shouldn't be concerned with that just yet. We will get to the frequency.

### User-behavior metrics table

Now we will talk about metrics that show how your ad relates to user behavior:

- **Outbound CTR (click-through rate)** — tells us how many people clicked through to our website upon seeing the ad.
- **Conversion rate** — measured in percentages and it tells us what is the percentage of people who, upon seeing the ad, converted into purchases.
- **Cost per link click** — tells us how much we're paying for one link click. This can be a link clicked in our description or outside of Meta Technologies, which means to the website.
- **CPM (cost per 1,000 impressions)** — tells us how much we're paying for 1,000 impressions.
- **Cost per 1,000 Accounts Reached** — very similar to CPM but tells us how much it costs to reach 1,000 unique accounts on Meta Technologies. Not impressions which can be repeated to the same people, but unique accounts.
- **Frequency** — tells us if we are reaching new people or not. This metric tells us how many times, on average, a prospect sees the ad. But the higher this number is, the more it indicates that we are repeatedly reaching the same people over and over, which means that we are not reaching a new audience. We want this number to be 1.2 or lower.

There are no magic numbers for each of these metrics, however we want to look at the account averages and there are some general directions in which we want those to move.

**Outbound CTR (Click-through Rate)** — we want this to be above 1% and more because the higher the Outbound CTR, the higher chance of people converting fully to purchasers and not just clicking on to the website. If the CTR is low for the creative, that means that our CTA is not potent enough. We haven't managed to get our prospect to believe what we're saying and how we're saying it, and therefore the prospect doesn't feel the urge or need to own the product. So, in a way, our ad appears less relevant to them (and Meta), it appears less trustworthy and will not be rewarded by Facebook.

We want to get as many people to the website as possible. CTA is of course an integral part of an ad, but our whole ad needs to be persuasive in a non-obvious way so that the prospect will want to convert by nature. We will use a CTA to get people to the website, we will use it in every ad, however we want the whole ad to entice the feeling that the prospect needs to go and buy our product NOW, because we can't rely on people watching the ad throughout, especially when it comes to video creatives.

**Conversion rate** is very similar to CTR. However, CR measures what is the percentage of people who saw our ad that actually converted on the website. This can come down to several factors. If our conversion rate is low, that can indicate problems on the creative, but it can also indicate problems on the website. This is not fully in our hands. Upon assessing the averages of the conversion rate on the ad account and for giving creative, you should always at least question if there have been any changes made to the website. Is everything working properly on the website? What is the customer journey like — so that we can reassess this number and get the full picture.

**CPM and Cost per 1000 Accounts Reached** are two very similar metrics, but they differ in a very specific way. CPM tells us how much we're paying for 1000 impressions, while Cost per 1000 Accounts Reached tells us how much we're paying to reach 1000 unique accounts on Meta.

These two metrics are not as important in determining the success of an ad, but it does tell us a lot about what our visibility is to newer audiences. If our CPM is low and our Cost per 1000 Accounts Reached is high, that means that we have difficulties reaching new audiences and we're kind of staying in front of the eyes that have already seen us.

So in our messaging we should strive for newer audiences because that is how businesses grow mostly. So these two metrics you should keep in mind and you should track their progress into the account. If you notice that CPM is getting higher, it's getting more expensive to reach new fresh accounts, you should flag it!

**Frequency** tells us the average number of times that a prospect is seeing our ad. We want this number to be 1, 1.2, or lower because we don't want to spam people with our ads. We don't want this to be 3 or 4 because that essentially means that we are not reaching new people, which is again something that we should strive for. Of course, this will also depend on exclusions in our ad account. Exclusions are something that is done on account level settings, and we should be excluding all possible purchasers that we have (updated email lists, long exclusions like 180 days and more if possible). These should be constantly updating, and you should check it or whoever works on the account should check it. This will help lower the frequency as well, so it's a matter of account settings and not only ad itself.

### User-reaction / engagement metrics

Now we'll take a look at metrics that actually tell us how people are reacting to our ad:

- **Hook Rate** — measures the percentage of users who watch the first 3 seconds of the ad.
- **Hold Rate** — tells us the percentage of users who watched our ad completely.
- **Video Average Play Time** — tells us how long, on average, did users play our video.
- **Cost Per Save** — measures how much it costs for a prospect to save our ad.
- **Cost Per Share** — measures the cost of a prospect sharing our ad with a friend or somewhere else.

Now, these metrics tell us how users interact with our ad. Sometimes there are KPIs and set expectations on Hook and Hold rates, and that is something that will also be provided to you most likely with other KPIs.

**Hook rates** are a very important metric in determining the perception of our ads. If a hook rate is high, that doesn't necessarily mean that the ad is successful and is bringing in a lot of money, but it tells us that the ad is generating interest. Essentially, it tells us how this ad stops people in their tracks and how successful we are in capturing the attention of our prospects.

Good hook rates are usually above 30%, but lately, this can even go higher to 50%, 45%. And at minimum you want it to be at 30%.

So that obviously will not be maintained throughout the whole video and after the first 3 seconds you can see a sharp drop in viewer attention, but that's fine. However, it is ideal if this attention is garnered throughout the video and results in purchases. It's a long journey that we can't fully track but we can connect some of the dots.

Most likely, successful ads will have high hook rates. This doesn't directly correlate that high hook rate is going to result in top-performing ads. However, if you think about it, when we have high hook rates, that means our ad is interesting to people. Meta values interesting content on its platform and it values user attention, so if we are interesting to the user, Meta will reward us by more exposure. Therefore, when we have more exposure, this will bring the right eyeballs to our ad, which means that we will get relevant prospects that have a high chance of converting. This is, as you see, a long string of factors that determine the success of an ad but they are connected.

**Hold rate** tells us how well we are maintaining the attention of the prospect. You can always use a controversial hook or any gimmick to get the prospect's interest to stop scrolling. However, how will we maintain that interest? Lately, what we are seeing in the accounts is hold rates 12–15% and above. These are lower thresholds. I wouldn't want to see it under 12% because we want that deep interest. We want people to engage with our ad by watching it, and the longer they watch, they are more prone to remember us and buy our product in the end. Maybe they will buy in 7 days, maybe they will buy in 15 days, or maybe they will remember our ad in 3 months, and this still counts as an impact of our ad.

So, it's important that the prospects are thoroughly watching our ads. We should be optimizing our scripts to garner that high level of interest (whether it's sitting longer in a problem or using engagement editing style or showing more of the product). We need to determine what it is in the ad that keeps the viewer's attention. You will do this by watching the ads, by determining what are some common styles, practices, and themes in ads that have high hold rates because this is the content that works and that will bring more purchases, more profit, and more scale to the business.

**Cost per save and Cost per share** tell us a lot about how our prospects feel about our ads.

When you think about it, you share memes with your friends. You share positive stories, you share something horrific, but it's always something that captures your interest so much that you want to share it with others.

We can't see the number of saves in our ads. However, we can see cost per save and if that cost per save is low that means 90% that a lot of people felt the need to come back to our ad by saving it. The same can be said about shares — if the cost per share is low, that means that our ad was shared repeatedly. Usually, when the ad isn't being shared, this will be a very high number (over $1k). But the more shares you have, the lower this will be.

This is basically free exposure of our ads. Maybe somebody sent it to a friend, maybe somebody shared it with their family member, and that all counts as an impact of our ads.

---

## Funnel Stage — Don't Compare Ads on a Level Playing Field

There's one caveat that has to sit on top of all the top-spender and metric reading above: **not all ads are competing for the same thing, so you can't compare them apples-to-apples.**

Here's the situation that makes this concrete. You open an account and the top spender is a buy-one-get-one offer ad. On spend alone it looks like the account's most potent creative. But that ad is scooping up people who already knew the brand and were likely to buy anyway — it's just closing them with a discount. That is not the same job as reaching a cold audience who has never heard of the product, and it shouldn't be weighed equally against an ad that does.

The distinction is the funnel stage the ad is built for:

- **TOF (top of funnel)** ads are made for cold traffic — people who have never seen the brand, sitting in the first three stages of awareness. This is the harder, growth-driving job.
- **MOF / BOF (middle and bottom of funnel)** ads target people in the final two stages of awareness — warm audiences already close to buying. Typical BOF creative: BOGO offers, discounts, heavy social proof, review statics.

A few practical reads that follow from this:

- **Statics skew BOF.** Not exclusively, but generally — so an account that's heavy on statics is often heavy on bottom-of-funnel demand capture, and should be read that way. This matters a lot when an account is static-dominant.
- **Don't compare a TOF video to a BOF static as if they're the same.** They're playing different games. When you rank or judge creative, make that caveat explicit rather than letting a BOF offer ad's spend crown it the "best" ad outright.
- **The hook and intro reveal the stage.** The first 15–30% of an ad usually tells you whether it's built for TOF, MOF, or BOF — a cold-audience opener does different work than one that leans on an offer or existing familiarity. Use the opener to classify the ad before you compare it to anything.

None of this means BOF ads are bad — demand capture is real and profitable. It means a fair read groups ads by the job they're doing before it judges them against each other.

## Understanding Breakdowns

We use breakdowns to further get information about our prospects and our audience who is seeing the ads. You can use several types of breakdowns, such as:

- Placements
- Age
- Gender
- Age and gender combined
- Platform

You can also look at the geo (location) and audience segments.

Often when looking at top performers and top spenders, you will be asked to deliver data based on breakdowns. Each time you look at the breakdowns for certain ads, you will want to sort them by spend. This way we will know on which variable Meta spends the most money.

For us, the most important are:

- Placement
- Age
- Gender

These breakdowns tell us three most important things:

- Where our ads are being shown
- Who is our audience in terms of gender
- Who is our audience in terms of age demographics

This paints a picture of their user behavior, of their scrolling habits, of their social media habits, and of course of their shopping habits, which is all very important to factor in when you're creating creative strategy.

### Placements

Your account will usually spend most on the following placements:

- Facebook feed
- Instagram feed
- Facebook stories
- Instagram stories
- Facebook reels
- Instagram reels

Here's an example: If we have high spend on Facebook feeds, Facebook Reels, or Facebook Stories, we are more likely to see higher age groups (older age groups) engaging with our ad. That is because most of them are still using only Facebook and this is where they spend most of their time.

When it comes to younger audiences, they are more likely to see our ads on Instagram, either stories, reels, or feeds, and this is for age groups that are 18+ over to 40s or even mid-50s.

## What It Means When Spend Is Heavier on One Placement

### FEEDS — FB vs IG

**User Intent & Behavior**

- **Facebook Feeds:** Users tend to be in a lean-back browsing mode, scanning for updates from friends, groups, news outlets and similar. Engagement here is slower and more deliberate — likes, comments, shares. Content discovery is secondary to staying connected.
- **Instagram Feeds:** Users are in a visual-first, aspirational mindset. They expect curated, aesthetic content, and engage heavily with visual storytelling (carousels, high-quality images). Discovery is core to the experience, so users are more open to branded or influencer-like content.

**Algorithmic Distribution**

Meta delivers more to Facebook Feeds when signals show that the audience engages with text, long captions, and discussion-driven content. By contrast, delivery skews to Instagram Feeds when signals favor short attention visual scroll behavior (image saves, quick likes, double-taps).

**Demographic & Psychographic Implications**

- **Heavy Facebook Feed delivery:** Suggests your audience is older, values community, and is more likely in a consideration or research phase of the funnel.
- **Heavy Instagram Feed delivery:** Suggests a younger, aspirational audience, often at top or mid-funnel, who responds to visual cues more than detailed explanations.

### REELS — FB vs IG

**User Intent & Behavior**

- **Facebook Reels:** Consumption is more casual and accidental. Many users land on Reels because of algorithmic nudges, and sessions are shorter. They may swipe a few videos while on Facebook, but aren't in "infinite scroll mode."
- **Instagram Reels:** Users enter Reels with high intent for entertainment and discovery. They actively seek content in an infinite-scroll, TikTok-like environment. They are primed for new creators, trends, and products.

**Algorithmic Distribution**

If Meta sends most impressions to Facebook Reels, it signals that your audience is reachable in incidental, casual viewing moments — the algorithm is exploiting cheap CPMs with lower attention depth.

If impressions concentrate on Instagram Reels, it indicates your audience is habitual short-form content consumers — high discoverability, fast trend adoption, and younger skew.

**Demographic & Psychographic Implications**

- **Heavy Facebook Reels delivery:** Suggests your audience might be broader, older, or less trend-driven. They engage when interrupted but aren't seeking trends. Often top-of-funnel reach, lower cost, but weaker intent.
- **Heavy Instagram Reels delivery:** Suggests trend-following, younger demographics, likely early in the funnel but with higher virality potential. Great for UGC-style hooks.

### STORIES — FB vs IG

**User Intent & Behavior**

- **Facebook Stories:** Viewed more passively, often while checking in on friends. Users click through faster, with low tolerance for interruptions. Attention span is shortest here.
- **Instagram Stories:** Intentional, habitual viewing. Users are primed for ephemeral, daily check-ins with influencers, brands, and friends. They interact more with polls, stickers, and swipe-ups.

**Algorithmic Distribution**

When delivery leans toward Facebook Stories, it means your audience is glancing passively and responding to low-effort visuals. CPMs are cheap, but engagement depth is shallow.

When it prioritizes Instagram Stories, it suggests your audience is actively consuming ephemeral content and comfortable with fast-moving, vertical creatives.

**Demographic & Psychographic Implications**

- **Heavy Facebook Story delivery:** Signals an older audience who engages in habitual tapping-through, less likely to convert on direct CTAs. Often upper-funnel exposure.
- **Heavy Instagram Story delivery:** Signals younger, more interactive users, accustomed to swiping up for offers. They're likely mid-to-lower funnel, especially if conversion CTAs (polls, quiz stickers, links) perform well.
