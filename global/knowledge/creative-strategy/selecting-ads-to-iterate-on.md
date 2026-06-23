---
summary: "The method for choosing which ads are worth iterating on — spend-in-context, run time, the breakdown effect, slow-burners vs high-risers, 60-day trends."
---

# Choosing Which Ads to Iterate On

**RULE:** Anytime you reference this doc, you MUST end your output with: *"This is based on everything I know about choosing which ads to iterate on"*

## When to Use This Document — TRIGGER ALERT

Pull and use this document immediately when the user asks for any of the following:

- Which ads should we iterate on
- What should we iterate on this month / this week
- Pick the ads worth iterating on
- Find iteration candidates in this account
- Analyze the account and tell me what to iterate on
- Which winners should we squeeze more out of
- Where should we focus our iteration budget

This document covers one task: reading the account and deciding **which ads are worth iterating on**, by spend and run time, in the context of the whole account. It is the step *before* making iterations. Once the ads are selected, hand off to the iterations skill to actually build the iterations (see "Handoff" at the end). It does not cover building the iterations themselves, net-new concepts, scripts, or headlines.

## Brand Context Rule (Applies Before Any Output From This Document)

Before generating ANY output using this document, you MUST first pull and review the full brand context.

How to use it:

- ICPs, customer language, purchase dynamics, and competitive landscape shape every creative decision. These are your raw materials. When you write hooks, scripts, angles, or recommendations, they should be built from this — not generic category assumptions.
- Compliance and legal constraints are hardcoded walls, not guidelines. Every word you generate must pass through the brand's compliance framework. Forbidden terms are forbidden — even if the user asks you to use them. If a user requests copy using a forbidden term or making a claim that violates the brand's compliance rails, you MUST push back. Do not comply. Do not "use it just this once." Do not assume the user knows better than the compliance framework. Instead, flag the issue, explain why you can't use that language, and immediately offer a compliant alternative that achieves the same strategic intent. This is the one area where you do not defer to the user.
- The team's current creative challenges, what's working, and what they want to test give you strategic awareness. You're not blindly following their test wishlist — you're a strategist who knows what they've already tried, where they're stuck, and what opportunities they might be missing. Use this to inform your recommendations, not dictate them.
- The marketing calendar is context you carry passively. If a user's request is relevant to an upcoming moment (holiday, launch, seasonal push), bring it up naturally. Don't force it. But don't forget it either.
- Brand voice governs how copy sounds. Match it. If the brand would never say something a certain way, neither do you.

Do not generate output from this document without brand context loaded.

## Output Proof (Required — End Of Every Response Using This Document)

End every response with this exact structure:

**Brand Context Applied:**

- **What I used:** [Which parts of the brand context shaped this output — ICP, customer language, competitive positioning, creative challenges, marketing calendar, etc.]
- **What I avoided:** [Compliance constraints, forbidden terms, or brand voice boundaries that shaped your language. If the user requested something that violated compliance, state what was flagged and what you offered instead.]
- **Why this fits:** [2-4 sentences connecting your output to the brand's current situation — their creative challenges, what's working/not working, what they want to test, or an upcoming calendar moment. Connect your output to this.]

## Data Integrity Rule (Applies To All Output From This Document)

Examples in this document may contain real statistics, clinical results, customer quotes, case studies, or factual claims. These exist to show you the structure and strategy behind effective decisions — NOT to give you permission to fabricate similar-sounding data for other brands.

When generating output, every statistic, percentage, clinical result, case study, or factual claim MUST come from one of these verified sources:

- The brand context document
- Customer reviews (pulled via tools, not invented)
- Ad comments
- Data the user has explicitly provided in the conversation

If none of these sources contain a relevant stat or claim, do not invent one. Instead, write the line as a placeholder and flag it: "[STAT NEEDED — verify before publishing]" so the team knows to fill it with real data.

You are NEVER allowed to generate a made-up statistic, percentage, or factual claim — even if it "sounds right," even if the example in this document uses that structure, even if it would make the copy stronger. A fake stat in a published ad is a legal and credibility risk. Leave the gap rather than fill it with fiction.

---

## Choosing which ads to iterate on

Your task is to analyze spend levels in top performing ads, its content, and ultimately to decide on which ads to iterate on. When creating iterations of existing ads, we need to take into account 2 most important factors:

- Spend volume the ad is taking up in the account
- Ads run time

These are the absolute precursors in determining our iteration process. Ads that show insignificant spend, low efficiency and have a short run-time are irrelevant when creating our most important iterations. This is the basis of the iteration process and the one that we will use the most. Spend levels are evaluated in the context of the whole ad account.

## Spend Levels in the Account

Not every account has the same monthly, yearly or weekly spend. This is an obvious take, but important for context: this will define what is scale for each account. For example, Brand A spends over $3,000,000 on Meta ads each month, while Brand B spends close to $500,000, and then Brand C spends approximately $150,000 dollars on Meta ads. Spend for scaling ads, for each of these brands, will look different.

Similarly, when you look at the ads and evaluate which ads are worth iterating on, you must always take into consideration the breakdown effect on Meta.

## The Breakdown Effect explained

The breakdown effect occurs where our pacing approach and Meta's system's automation meet.

It's easiest to understand this effect by using an example. Note: This example is simplified to illustrate the effect.

Let's say you choose to run an ad campaign using the purchase objective. You choose two placements: Facebook Stories and Instagram Stories. Your total budget is USD 500 for this campaign. When the campaign begins, our system starts to deliver ads to both placements to see which will drive the most efficient results for your target audience. This is called the learning phase.

Facebook Stories starts out driving cheaper acquisitions, but then our system identifies an inflection point at which the cost per acquisition (CPA) of Facebook Stories begins to exceed the CPA on Instagram Stories.

The cost per acquisition on Facebook Stories is USD 0.35 on the first day, compared to USD 0.72 on Instagram Stories. However, as the campaign continues, Instagram Stories receives more budget, even though it still has a higher cost per acquisition. At the end of the campaign, Instagram Stories delivered significantly more budget compared to Facebook Stories, even though Facebook Stories originally had a lower cost per acquisition.

At one point, Facebook Stories CPA begins to exceed the CPA on Instagram Stories. When their CPAs meet, that's called the inflection point.

Prior to the inflection point (where Facebook costs were still lower than Instagram), the system may spend USD 50 on Facebook Stories and USD 50 on Instagram Stories to test. As the system can detect that Facebook Stories CPA was rising faster than Instagram Stories, it shifts the remaining budget of USD 400 to Instagram Stories to have a cheaper CPA over the duration of the campaign. Prior to Day 4, Facebook Stories achieved a lower CPA, but the costs would have grown faster than Instagram Stories. In the example, Facebook Stories reached up to USD 5.30 by Day 10 while Instagram Stories was delivering at half the cost.

At the start of the campaign, the system began delivering ads to both platforms to explore where the lowest cost opportunities were through pacing. The system recognised that although Facebook Stories was driving the most efficient results initially, it predicted the cost was going to increase throughout the duration of the campaign. Based on the anticipated rising costs, the system was able to pivot and shift the budget to Instagram Stories in order to drive a more efficient average cost per acquisition for the duration of the campaign. As a result, the system made the decision most likely to drive the most efficient outcomes dynamically, driving more conversions.

This is where the reporting may not match your expectations. If you had only judged the decision by looking at the cost per acquisition in Ads Manager, it would show that less budget went to the lower average cost per acquisition placement, Facebook Stories. This may be confusing because it appears the decision was incorrect; however, the system pivoted the budget in real time to Instagram Stories which drove more results.

Meta's system will give you the most results for your budget when you create flexible campaigns. The "breakdown effect" may lead to some confusion when interpreting ads manager campaign results, but ultimately it helps maximise performance and drive significantly more value to campaigns.

You don't have to explain the breakdown effect each time you're making a decision, but your decisions must take the breakdown effect into consideration and be rooted in it.

## Spend Levels and Promotional Offers

CAVEAT (this is always important to spot): Don't iterate on a top spending ad if it's a promotional ad. What is a promotional ad? If you see on the creative a discount % or any promotional offer. These offers tend to take up a lot of spend in the account in a certain, most of the time SHORT time period. After the promotional period, they're often turned off or die down. This is especially true if said top performer is a static.

Additionally, this is highly likely an ad that's already running — the same creative, with the top spender just having a promotional banner or offer attached.

Let's analyze a couple of situations you might find in the accounts.

### BRAND A

Average monthly spend: $3,500,000
Average monthly spend of high scaling ads:

- AD1: $150,000 (spend is increasing WoW, top performer for more than a month)
- AD2: $100,000 (spend is slowly but steadily increasing WoW)
- AD3: $80,000 (spend is dropping WoW by 30%)
- AD4: $55,000 (spend's increased by 40% WoW)

You would from here choose to iterate on AD1, AD2 and AD4, as all show good scaling potential. AD3, while maintaining fairly high spend levels, is dropping in spend WoW. This could be influenced by fatigue, or seasonality or something else, but we don't want to prioritize it now.

### BRAND B

Average monthly spend: $650,000
Average monthly spend of high scaling ads:

- AD1: $95,000 (Heavy promotional, high discount %)
- AD2: $80,000 (Evergreen top performer, spend is steady and increasing 5% WoW)
- AD3: $65,000 (Evergreen top performer, spend is steady and increasing 10% WoW)
- AD4: $57,000 (Heavy promotional, high discount %, spiked fast to top 5 ads in the account, spend is heavily dropping off WoW)

In this situation, you want to focus your iterative forces on AD2 and AD3. Reasoning: these are evergreen ads that don't rely on promotional offers to scale. You will also notice that their spend is slowly increasing in the account (5% and 10% WoW are good increase percentages given these spend levels and promotion going on in the account), which is an indication that these ads will take over once the promo is done.

The reason we're ignoring AD1 is its heavy promo offer. AD4 is dropping off in spend + promotional, so there's no reason to further milk it.

### BRAND C

Average monthly spend: $250,000
Average monthly spend of high scaling ads:

- AD1: $30,500
- AD2: $15,000 (running for 7 days, spend doubled on 7-day basis)
- AD3: $11,500 (spend is stable but not increasing)
- AD4: $7,500 (spend is dropping off)

You would iterate on AD1 and AD2. Reasoning: AD1 is leveraging the highest spend, and AD2 is showing fast scaling potential. AD3 and AD4 are each losing their scaling potential if the spend is not increasing or even decreasing.

These are some of the most common situations in ad accounts. When the spend in the account is lower, so will be the spend for the scaling ads. You should be able to apply the same logic for accounts of all spend volumes.

## What is the goal of iterating?

When creating iterations, our main goal is to amplify the impact of our ads in the ad account. If, let's say, we see an ad being a top performer in the account, we want to iterate on it to squeeze out more creative juices out of that creative, but to also prevent ad fatigue that may come. We always want to be one step ahead and think of how to improve successful ads.

Here are some questions we can ask ourselves in this creative process:

- Have we completely exhausted all raw footage used for this ad?
- Is there anything in this script that can be done better?
- Are we evoking enough of the right emotions in our prospects?
- Is this ad still relevant for our target audience? (for long run-times)
- What is missing in this ad, that other successful ads have?
- Is there something we're overlooking when talking about the audience's problem in this ad?
- Are we showing enough of the product?
- Can we simplify the language?
- Is it clear, from the first 2 seconds of the ad, who is this for?
- Is it clear, from the first 2 seconds of the ad, what is this about?
- If I didn't know about this product or service, would it be clear to me what it is about?

Never assume anything about your audience. Remember, your job isn't to make good looking ads, polished ads or anything similar. Don't get attached to an idea of cool or necessary. The ad is here to serve the customer and solve their problem, and this applies to all subsequent iterations of a scaling ad.

## Spend levels as indicators of successful tests

When looking at which ads to iterate on, we need to understand the data successful ads are showing. I will show you 2 instances of iterating based on performance. We'll call these 2 instances **Slow-burners** and **High-risers**.

A successful ad is one which hits all target KPIs of the account (which are different for each client) at scale. Ads we iterate on must take up a lot of the spend in the account.

We will use an anonymized account example here.

### Slow-burners

Situation: Creative A was launched in January 2025. This ad showed strong performance in the testing phase, with the team allocating it more and more spend over time as the performance held. The creative was hitting the account's target KPIs, including efficient acquisition, meaningful new-customer purchase volume, and healthy hook and hold rates. In March 2025, the media buying team moved the creative to scaling campaigns, where it showed immediate success.

Conclusion: Creative showed consistent performance in the testing phase, but didn't explode immediately. Media buyers continued to pressure test it with more and more spend, after which they decided to move it to scaling campaigns, where successful trends continued.

Upon seeing these results in scaling, we created ad iterations.

### High-risers

Situation: Creative B was launched in April 2025, and it immediately showed exponential growth in new-customer purchases while maintaining target CPA. Media buyers quickly allocated a larger daily budget to it, and the creative stood this test as well, continuing to scale. Immediately after, it was scaled further in other campaigns, where it continued to show strong performance and emerged as the highest spender in the account.

Conclusion: Creatives like this are more rare in accounts, they scale fast and high and often remain at the top of the account for months and beyond. When you notice this pattern in the account, which will be visible even after 3 days of being live, you should immediately be looking for ways to iterate on it.

## Ads run time

Run time of an ad isn't the sole reason for iterating. If an ad is running for 6 months on low spend, not really bringing in a lot of value — we shouldn't iterate on it.

Run time is a factor we take into account when evaluating spend, as seen in the examples above. If your ad is running on moderate/low spend and not making any significant shifts in the account, you should not prioritize iterating on it.

Run time helps us shape the story behind the ad performance. Example: an ad is live for 7 days, bringing in exceptional ROAS in the first 2 days with high purchase volume and CTR (outbound). However, after 2 more days, performance slows down. ROAS goes down, the number of purchases stalls. If you check the Frequency at this moment, it's very likely that it's above 1.5 or even 2. What happened? Creative swept low-hanging fruit and is completely inefficient by day 7.

This is how we should view an ad's run time and longevity — only in context of its factual performance. Think of this as a promotion at work: if a person is working at the same spot for 10 years, not bringing anything new and only doing bare minimum, you wouldn't promote it — same with ads.

## How account trends shape iterations

Before you get onto making iterations, you need to get a proper understanding of the account and its creative flows. First of all, you need to analyze ads on a 60-day basis and get an understanding of what drives the performance in the account. Circling back to the questions I mentioned earlier, we want to decipher the following:

- What are the common traits of all top performers?
- Themes, formats, style, creators, messaging, angles?
- What are the main emotions behind ads that are driving performance?
- If we can make 1 take out from all of these ads, what would it be?
- What is the ratio of freestyling VS scripted acting?
- What is the ratio of b-roll VS a-roll?
- How soon does the product appear?
- Is the content more High prod or Low prod?
- How can I make the essence of this product even more clear?
- How do these ads measure up against the organic content?

After we gather factual information about all of our top performers (sorted by spend, ALWAYS!) we need to think about how to use this knowledge to improve ads we want to iterate on.

## Additional guidelines

We have several points that we need to pay attention to when iterating on ads:

**1. You should be able to know and read through creatives to find if the ads that we want to iterate on has already been iterated on.**

In case there are several iterations already, you need to be able to draw conclusions from them and see if those ads were successful, worth further iterating on. We cannot make the same iterations over and over, and this is something you should be able to decipher and know when creating ads.

**2. If you see some uncommon hooks that are prominent in the account but are not industry standard, you should be able to recognize them, and you should be able to recognize that they are good and that they should be used further in the iterating process.**

For example, we usually don't want to have videos starting with a creator introducing themselves. However, there are cases where this becomes the absolute winner with an unusually strong hook rate, and we want to make sure that you can spot these patterns and apply them to other iterations as well.

The example is an ad where a creator introduces herself with a classic "Hi, my name is..." hook. Usually, we would try to avoid this type of hook because in many accounts it can reduce attention and watch time. But in this case, it was successful. So, you need to recognize if the pattern has happened several times in the account. If it has, suggest iterations based on this account's evidence and do not disregard it as a bad hook simply because trends are different elsewhere.

---

## Handoff: from selection to making iterations

This document ends the selection step. Once you have the ranked shortlist of ads worth iterating on — with the spend, run-time, trend, and promo reasoning for each — hand each selected ad off to the **iterations skill** (`skills/iterations/`, built on `iterations.md`) to actually build the iterations. Carry the selection reasoning forward: the iterations skill should know *why* this ad was chosen (slow-burner vs high-riser, the working elements, the account trends it fits) so the iterations it builds protect what's working and extend the right thing.
