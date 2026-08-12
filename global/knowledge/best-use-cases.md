---
doc: best-use-cases
team: global
last_updated: 2026-08-07
purpose: The answer to "how can I best use Parker?" — a plain, practical menu of what Parker can do for a marketing team inside Claude Code, with real prompts to copy and what each one gives back. Parker reads from this when a user asks how to get the most out of it.
provenance: Seeded 2026-07-11 from a walkthrough of how the Parker brain gets used day to day (account analysis, static generation, recreating top ads, loops-and-judges, reporting, and putting workflows on a schedule). Extended 2026-08-07 from the 2026-08-06 monthly webinar (`global/knowledge/webinars/2026-08-06-monthly-webinar.md`) — swipe files and briefs off the discovery database, Reddit, cross-client agency analysis, fine-tuning a skill on your own back catalog, feeding the brain outside content, the hypothesis-tracker routine, and browser control. Extended again 2026-08-07 from the backfilled 2026-07-02 monthly webinar (`global/knowledge/webinars/2026-07-02-monthly-webinar.md`) — connecting your tools before the build, auditing your own working week, the review-agent pass over generated output, and natural-language routines; almost everything else in that session was already here. A coverage audit against both transcripts on the same day closed three more gaps: extending the brain past paid creative into other channels and browsing the discovery database to find formats you haven't tried (both 2026-08-06, missed on first promotion), and the routines point above. Generalized across brands; examples are illustrative, not tied to any one account.
---

# Best use cases for Parker

> **When to read this:** a user asks how to use Parker, what it can do, how to get the most out of it, where to start, or "what should I ask you?" Pull from here and give them two or three ideas that fit where they are, not the whole list at once. Lead with what's easy and pays off fast.
>
> If they're asking about something specific that was shown or announced on a webinar, the transcripts are at [`global/knowledge/webinars/`](webinars/INDEX.md) — this doc carries the durable use cases, those carry what was actually said and when.

Parker isn't a chatbot you start over with each time. It's a brain that lives in a folder on your machine, holds everything about your brand, and gets a little smarter every time you or your team use it. So the best way to use it is less about one clever prompt and more about pointing it at real work, then putting the good stuff on a schedule so it just shows up.

Here's what people actually get out of it, running roughly from quick wins to the deeper systems. Every prompt below is meant to be copied and tweaked.

## Start here: pour your real context in

The brain is only as good as what it can see. Before the fancy stuff, feed it the places your team already works. If you've connected Slack, Notion, Gmail, or your calendar as tools, Parker can read them and fold them into its running memory for good.

**If you haven't built your brain yet, connect those tools first.** It's a small ordering thing that changes the result. Building the brain is by far the heaviest pass it will ever run — hours of reading your account, your customers, and your competitors and writing it all down. Anything connected before that pass gets read *into* the build. Anything connected after has to be bolted onto a finished V0. Same tools, worse foundation. So go to your connectors and add whatever you actually do strategy in — Notion, Slack, Google Drive, your design tool, your generation tool, your deck tool — and then start the build (`stated`, 2026-07-02 webinar).

There's a second half to this, and it's the part people underdo. When the build asks whether there's anything else it should know about your brand, **dictate the answer and be long about it.** The yardstick that makes it concrete: if you're a brand, say everything you'd want an agency you just hired to know. If you're an agency, say everything you'd tell a new strategist joining the account — your process, your tools, where your ideas database lives, what the asset statuses mean, who decides what. That's the level.

**Ingest client and team feedback from Slack.**
> "Look through my client channel, read all the feedback the client has ever given, and fold it into your context going forward."

Parker reads the channel history end to end and writes what matters into the brain. From then on, every answer already knows what that client likes, hates, and keeps asking for. Do the same for Notion (every concept you've ever made), Gmail, and your calendar (every meeting and brainstorm). The more of your real context it can see, the less it runs on stale guesses.

Tip: turn on auto mode for big reads like this so you're not clicking "allow" every few seconds.

## Then point it at your own week, not just your brand

Every use case below aims Parker at the brand's data. This one aims it at *you*, and it's the fastest way to find the two or three workflows worth automating in your actual job rather than in the abstract.

Sit down and voice dictate for about ten minutes. Not a prompt — a brain dump. What you do on Mondays, what you do on Tuesdays. What eats the most hours. What you genuinely have to do yourself because it's your judgment. What you'd hand off tomorrow if you could. Then close it out:

> "That's how my week actually goes. Look at what you can reach and what tools I've got connected, and tell me what you could take off my plate or speed up. Be specific about which ones you'd automate first."

You get back a list of candidate routines shaped around your real job, not a generic feature tour — and it knows what's actually wired up, so it won't propose something it can't do. This is where a lot of the best prompts in this doc came from originally (`stated`, 2026-07-02 webinar). Pick one, build it, put it on a schedule, then come back for the next.

Don't self-edit while you're dictating. Long and messy beats short and tidy — the model takes what's relevant and drops the rest.

## Make static ads from your own customers' words

This is one of the strongest use cases, and it works because Parker isn't making the language up. It pulls real reviews, ad comments, and post-purchase surveys through the Parker connection, then can generate the image through a tool like Higgsfield.

> "Search my customer reviews and Facebook ad comments, find the most emotionally loaded phrases our customers actually use, cluster them into distinct angles, check the ad account for angles we haven't tested yet, and turn the best ones into statics."

What comes back is a handful of ready-to-run statics, each built on a real customer phrase, aimed at a persona or angle you haven't hit yet. Parker knows where your white space is because it can see what's already spending in the account. You'll usually want a light human pass on the copy, but the concept and the grounding are done.

Statics and reporting are where this shines most. You can do it for video too, it just wants more human-in-the-loop.

## Recreate the ads that are already winning

Parker can see top-performing ads from other brands (yours and external ones) through the Parker connection. So you can borrow what works and rebuild it in your own voice, with your own customers' language.

> "Look at my external brands' top static ads by impressions, find the ones that make sense for us to recreate, and draft the copy grounded in our real reviews, ad comments, and post-purchase surveys."

The point is it translates the mechanism, not the surface. It takes an ad that performed for someone else, then rebuilds it around a real thing your customers say. Same idea works for pulling from your own back catalog of what's worked before.

## Build a swipe file out of every ad Parker can see

You don't have to limit this to the brands you follow. Parker holds every ad from every brand anyone has followed, all tagged the same way your own ads are, and ranked by impressions. So you can go looking for one very specific kind of ad and get back the ones that are near the top of their account, which is a decent proxy for a winner.

> "Look in the Parker directory and find me animation ads under a minute long for problem-solution products, top by impressions. I want ad inspo I'll turn into scripts."

That's the whole move: name the format, the length, the industry, the awareness stage, the language, whatever narrows it — then let the impression ranking do the quality filtering. You get back a swipe file where most of the ads were #1 or near it in their own account.

**There's a second way to use it, and it's the one people forget.** The above assumes you already know what you want to make. You can also go the other direction — browse the top of the database with the format filter *off* and see what's winning that you'd never have thought to ask for. Same ranking doing the same work, but now it's answering "what should we be making?" instead of "find me more of this."

> "Show me what's winning across the whole database for brands like ours right now, top by impressions, and group it by format. I want to see the ad types we've never tried, not more of what we already make."

Read the gap between that list and your own account. Formats that are working everywhere and are absent from your library are the cheapest thing you'll test all quarter.

**One rule about impressions, and it's not optional.** Ranking by impressions is a stand-in for data you don't have. It works for other brands' ads because nobody can see their spend, and a brand that keeps paying to deliver an ad is telling you something. It is the wrong tool the second real numbers are available. For your own account, or any client account you have access to, use the actual spend, ROAS, and fatigue data — that says what an ad *did*, where impressions only say it kept getting served. Never rank your own creative by impressions when the real read is sitting right there.

Say where you want it to land. An HTML doc you can scroll is good for a training or a team share. Saving it into a folder in the Parker app is better if you want it to live somewhere permanent.

> "Now save these down to a new swipe file folder in Parker so I can share it with the team."

One thing worth being clear about: tell it whether you want your followed brands only or the whole database. Both work, and the default isn't obvious. On the 2026-08-06 webinar a run of this against top-of-funnel statics searched 120,000 ads to build one file (`stated` — said live on the call).

## Turn the swipe file into finished briefs

The swipe file isn't the deliverable. The brief is. And the same session can carry straight through.

> "Now turn each of these into a brief for us. Rewrite the script knowing everything you know about our brand and using the adapting-script method, and include a reference to the original ad in every brief."

You get ten real briefs with adapted scripts off ten proven ads, in a few minutes of actual work. Two rules for using them well. **Include the reference to the source ad** — a brief that doesn't name what it was adapted from can't be checked, and whoever produces it loses the thing that made the original work. And **read them before they go anywhere.** The honest expectation is that maybe half to two-thirds come back usable on the first pass; the rest want a human edit. Tell Parker what was wrong with the weak ones and the next batch is better.

If your briefs live in Notion or another connected tool, ask for them there rather than in a file.

## Mine the brands sitting right next to yours

Your direct competitors aren't the only place good angles live. There's a whole set of brands that sell to your exact audience but aren't competitors at all, and their winners are full of angles you could borrow. Parker scores these on three things — audience, positioning, and tone — and rules out anyone selling your product.

> "Find brands that sell to our audience but aren't our competitors. Look at their best-performing ads and pull out the angles that would translate to us."

You get a set of fresh angles from outside your own category, which is often where the ideas that don't feel done-to-death come from. The reason to prefer this over mining competitors: when you adapt an affinity brand's script you still get a strong script, without copying what your competitor is doing and living one step behind them permanently.

When you find brands worth watching, tell Parker to follow them and they'll be in your ad library from then on.

> "Follow those brands in Parker so their ads keep coming into my library."

## Let it watch you research

Research is visual. You scroll an ad library, something stops you, and then you're stuck describing it or pasting links. On the Claude Code desktop app you don't have to — open a browser inside the session and **Parker can see the page you're on.**

So the ask becomes as simple as pointing:

> "I like this ad on screen. Tell me how we'd recreate it for us, then build it through Higgsfield."

You get the breakdown and the recreation without leaving what you were doing. It works in the other direction too — say "use the browser control" and Parker drives the browser itself, going and finding the ads rather than handing you a list to go look at.

This is the fastest way to work through Parker's own views. Scroll the top ads, react to what you see, and let the analysis and the build happen in the same motion.

## Turn winning TikToks into scripts for you

Parker can go find what's working organically in your niche and draft the rewrite so it's yours, not a copy.

> "Search TikTok for winning content in our niche, find the videos that would work for us, and draft script rewrites we can film."

You get scripts built off proven organic content, already pointed at your brand and your customer. Same human-in-the-loop rule as any video: read it, tweak it, then shoot it.

## Hear how people actually talk about it on Reddit

Reviews tell you what customers say to a brand. Reddit tells you what they say to each other, which is a different and often blunter thing — the objections they won't put in a review, the workarounds, the comparisons, the way they name the problem before they know your category exists.

Pulling Reddit directly through Claude Code is unreliable; Reddit's API doesn't make it easy, which is why almost nothing has it. Parker scrapes the subreddits you pick on a schedule into a directory you can query cleanly, with links back to the original posts.

> "Find what people are saying about [the problem we solve] on Reddit using Parker. Pull the exact phrases, the objections, and anything that reads like a trigger event."

**Check whether it's turned on for this brand before promising it.** It shipped — it was in limited testing on the 2026-08-06 webinar and is live now — but it's still switched on per brand, and nothing works until that brand finishes Reddit onboarding (picking subreddits, the relevance pass). So the check is per brand, not "is the feature out yet." If it isn't set up for them, say so plainly and point them at onboarding rather than returning an empty answer.

Two things make it much better. First, follow as many relevant subreddits as you can — a thin directory gives thin answers. To find them, **Reddit Answers** (free, from Reddit) works well: tell it what you sell and what problem you solve, give it one example subreddit, and add what it returns. Second, when a query surfaces a subreddit you weren't watching, follow it:

> "Follow those subreddits in Parker too, so we're pulling from them going forward."

## Keep your creative test tracker honest

Most teams keep a hypothesis or creative tracker in a spreadsheet or Notion, and most of them go stale because nobody goes back to score the calls. Parker can do the going-back part.

Spend three minutes describing your tracker — where it lives, what's in each field, what a row means, what you're actually testing. Then hand it the loop:

> "Every day, look at our ad account and any newly launched ads, go back to our hypothesis tracker, and decide whether each hypothesis was right or wrong and why. Update the tracker and show me the changes."

You get a running record of what you predicted versus what happened, kept current without anyone remembering to do it. Pick the trigger that fits how you work — every new ad, or seven days after launch when there's enough data to judge. Ask for the output as an artifact or a page you can share if the team needs to see it.

## Keep watch on what competitors just launched

Instead of checking manually, have Parker watch the competitive set and tell you what changed.

> "Look at what our competitors have launched in the last 30 days, run a gap analysis against us, and deliver it to Slack."

You get a running read on what they're testing, where the gap is, and what you could run to close it. Put it on a weekly cadence and it just shows up.

## Get the customer voice flagged to you every week

Your reviews and ad comments are moving all the time, and the good stuff gets buried. Parker can surface it.

> "Every week, flag the most notable new customer reviews and ad comments to Slack — the ones that reveal a new objection, a new angle, or a phrase worth putting in an ad."

You get the signal without digging for it. A single highly-liked comment or a repeated phrase is often the seed of your next winning static.

## Run ideas through judges before you ever see them

This is the quality gate. Instead of handing you 20 raw ideas, Parker can spin up several independent judge agents that each score an idea from a different angle, then only surface the ones that clear all of them. Five judges works well.

> "Come up with 20 concepts. Score each one with five independent judges: how close is it to our proven winners, to what's spending in the ad account, to what our customers say in reviews, to our ad comments, and to what's working in our organic feed. Only give me the ones that score high across the board."

You get a short list where every idea is backed by your winners, the account, the customer voice, and the organic feed at once, plus the reason it made the cut. It's the difference between volume and volume you'd actually launch.

## Add a reviewer after the work, not just before it

Judges filter ideas *before* anything gets made. This is the other half — a second pass over what actually came out. It's the single cheapest fix when a one-shot generation lands at "close, but the copy's weak," which is where most first runs land.

> "Now add a review pass. Have a separate reviewer read every ad you just generated, critique the copy specifically — what's vague, what's not in our customers' words, what a person wouldn't say out loud — then regenerate each one against that feedback."

You get a second, better version of the same batch without writing a new prompt. The reason it works is that the reviewer isn't the writer: an agent that didn't produce the draft catches things the one that did will defend. Ask for the critique alongside the rewrite so you can see what it changed and why — that's also how you learn what to put in the original prompt next time.

Worth doing on anything generated in volume. Statics, headline sets, script batches. And it stacks with the approval gate: review, regenerate, then show you the copy before spending anything on generation.

## Get your reports written for you

Parker can build the monthly or weekly report you already have to make, grounded in real numbers and real customer evidence, and drop it into Gamma or Google Slides.

> "Build my monthly creative report. Tell the performance story over time, what's working and what's not, ground it in customer evidence, and add a gap analysis against our top competitor with a few ad ideas that close the gap."

You get a V1 report in one prompt: the numbers, the story, the competitor read, the customer voice. Treat it as a first draft to approve or edit, not a finished deck. And you can teach it what you care about:

> "When you do reporting, don't over-index on ROAS. I care most about the ads pulling the most spend. From now on, prioritize that in every report."

It writes that preference into its memory and honors it next time. That's the whole game: correct it once, and it stays corrected.

## If you run an agency, ask across every account at once

The work that used to mean opening twelve ad accounts and scrolling is now one prompt.

> "Look at every client account's statics from the last 365 days. Pull the top spenders and top performers for each, split by what we made in-house versus what we didn't, and put it all in one doc."

You get the cross-account read in a single pass — for a quarterly review, a team training, a new-hire onboarding deck, or just to see which of your own patterns are actually carrying. On the 2026-08-06 webinar the comparison drawn was two hours of manual scrolling eighteen months ago versus about twenty minutes now, mostly spent assembling the deck rather than finding the examples (`stated`).

Same shape works for any cross-account question: which angles are working across the whole roster, which clients are running thin on a format, where one client's winner should obviously be tested on another.

## Put the good stuff on a schedule

Anything above that's worth having every week, you can hand off entirely. Parker delivers it to Slack on a cadence so it shows up in the place you already work.

> "Turn this into a routine and send it to me on Slack every Monday morning."

**Say it in the chat — don't go hunting for a settings screen.** That sentence, typed right after the thing you liked, is the whole setup. There's no form to fill in and no cron syntax to learn, and the most common reason people never automate anything is that they assume there must be a proper place to go and do it. The best moment to ask is immediately after Parker produces something good: "I love this, do it every Monday at 8 and send it to Slack."

Imagine 25 fresh statics in your Slack every Monday, or a report waiting the first of every month that says "here's the V1, approve it and I'll send it on." If you're running the full Parker brain, a set of these are already wired up for you: it refreshes its own context, dreams up new angles, hunts for ad ideas, and runs research loops on a cadence, all on its own. You can add your own routines any time.

## Teach it to write like you, not like Parker

This is the deepest one, and it's the difference between a good general strategist and one who's read everything your team has ever written.

Parker ships with its own method for scripts, hooks, headlines, iterations. That method is strong, and it's generic on purpose. But you have a back catalog — every script, every brief, every concept your team has produced for this brand — and that catalog is the actual answer to "how do we write?" Point Parker at it.

> "Look through every script we've ever made for this brand in Notion. Take the scriptwriting method and tailor it to us — exactly how we write for this brand."

What comes back is a **fine-tuned version of the skill**, usually alongside a script voice profile and a visual vocabulary doc. From then on it isn't writing from Parker's general method, it's writing from three hundred of your own scripts.

**How the override works.** The Parker method lives in `parker-system/` inside your brain, and that's read-only — you can't edit it and you shouldn't want to, because it's how you keep getting updates. So the fine-tuned skill gets built in your own part of the brain, and you tell the brain to prefer it:

> "Build this as a fine-tuned skill in my own skills folder, and update my CLAUDE.md so the brain always defaults to my fine-tuned skills over the Parker system ones. Where there's no fine-tuned version, fall back to Parker's."

Now everything routes to your version, and Parker's stays underneath as the fallback and keeps updating.

**Keep it current.** The catalog grows every month, so put the refresh on a schedule:

> "Every month, read the scripts we made in the last 30 days and update the fine-tuned scriptwriting skill."

**And it isn't only scripts.** Anything you have a body of work in can be fine-tuned the same way — the iterations you've made, the statics you've designed, the feedback you've given. Source it from wherever it lives: Notion, your PM tool, Slack, or Parker itself, which already holds every script from every ad you've run.

> "Read every message in my client channel and every piece of feedback my creative team has given, and fold it into the fine-tuned scriptwriting skill."

## Feed it what you read

The brain gets sharper from your work automatically. It gets sharper from the rest of the industry only if you hand it over.

> "Pull the transcript of this video, take the relevant learnings on static ads, and add them to my brain wherever they belong."

Works for a YouTube video, a podcast, a thread, a tweet, a newsletter, a conference talk. If a transcript won't pull directly, a tool like the vidIQ connection handles YouTube, and Glasp (a free Chrome extension) will grab one to paste in.

> "Here's another piece of content — good principles on writing static ads. Take it and put it into my brain too."

The reason this compounds harder than it looks: you don't read what your colleague reads. If everyone on the team drops what they consume into one shared brain, it ends up holding a version of the field that no single person on the team has. Pair it with a tool that shares context across the org and the whole team is working from it.

If you want the version with a review gate on it — where Parker shows you the exact change it would make before writing anything — that's what `/expert-signal-intake` is for.

## Give it the rest of your marketing, not just the ads

Worth knowing early, because most people assume the opposite: **the brain isn't limited to creative strategy.** That's just what the build knows how to construct cold, because it's what your ad account, reviews and competitors can be read into. It's the floor, not the ceiling.

Structurally, everything the build produced sits under one parent — creative strategy. You add siblings for whatever else you actually run: growth marketing, organic social, CRO and landing pages, email and SMS, retention, retail. Each new one learns the same way the first did, from whatever you connect and whatever you tell it.

You don't have to design the folders. Describe what you want and let it propose the shape:

> "Right now this brain only covers paid creative. We also run email, SMS, and organic. Look at how the brain is structured today, tell me how you'd extend it to cover those, and what you'd need from me for each."

You get a proposed structure and an honest list of what it's missing to fill it — usually a connector or two and some context only you have. Approve, then let it build.

Two things make this safe to do. Your brain is version-controlled, so nothing is a one-way door — if a structure stops fitting in three months, describe the new one and it reorganizes. And a new domain gets the same treatment as the original build: it reads real sources, marks what it inferred, and names what it couldn't reach. It doesn't guess a channel into existence because you asked for the folder.

The method behind this is `system/growing-the-brain.md`, which also covers growing a skill *downward* — the fine-tuning move in the section above — rather than only adding surfaces sideways.

## The pattern underneath all of it

The trick isn't any single prompt. It's this: connect your real tools, point Parker at real work, correct it when it's off, teach it from what you've already made, and schedule what pays off. Every one of those makes the brain sharper for the next run. That compounding is the reason people stop opening the regular chat.

If you're brand new, start with two things: pour your Slack or Notion history in, and ask for a batch of statics from your customer reviews. Those two alone tend to be the moment it clicks.

## Three habits that make all of it go better

**Yap.** Voice dictate, and say more than feels necessary. Think about everything a person would need to know to do this task, then say all of it — the context, the constraints, the history, the thing you're worried about. Don't edit yourself for relevance; the model takes what matters and drops the rest. Long, messy, detailed input beats a short tidy prompt almost every time.

**Use plan mode for the "how should we do this" work.** When you're thinking through a change rather than making one, plan mode keeps it from starting to edit, and you get a clean read on what it intends and why before anything happens. Approve, then let it run.

**Nothing is permanent.** The structure of your brain, the way your folders are organized, where things live — all of it can be reorganized later by describing what you want instead. So don't stall trying to get the shape right up front. Build it, use it, restructure when it stops fitting.

## A prompt library to steal from

These are real prompts that have worked well, grouped by the job. Copy one, swap in your specifics, and go. Notice the habit running through the good ones: when a prompt ends in something you'll spend money on or launch, it hands you an approval gate first. Ask for the copy, approve it, then let it generate. That one move keeps you in control and saves the credits.

**Generate static ads**

> "Find my external brand's top static by impressions, break down why it works, mine reviews for language that supports the same angle, draft 3 recreation concepts with copy, wait for my approval, then generate the approved ones in Higgsfield."

> "Look at my external brands' top static ads by impressions, find ones it would make sense for us to recreate, then draft copy for us to recreate them through the Higgsfield MCP. Don't generate them yet, I want to approve the copy first."

> "Search my customer reviews and Facebook ad comments for the most emotionally loaded verbatim phrases about the problem we solve. Cluster them into 3 to 4 distinct angles. Then check my Facebook ads data to see which of those angles we're not currently running. For the uncovered angles, draft static ad copy using the exact customer phrases as headlines. I'll approve the copy, then we'll generate the statics through Higgsfield."

**Review and regenerate what was just made**

> "Add a review pass over the ads you just generated. Have a separate reviewer critique each one's copy — what's vague, what isn't in our customers' actual words, what a person wouldn't say out loud — then regenerate each against that feedback. Show me the critique next to the rewrite."

**Audit your own week and find what to automate**

> "Here's how my week actually runs, in detail. [dictate it — what you do each day, what eats the most time, what only you can do, what you'd hand off tomorrow.] Look at what you can reach and what tools I've got connected, and tell me what you could take off my plate or speed up. Be specific about which you'd automate first, and don't propose anything you can't actually do today."

**Find your underserved persona**

> "Look at my customer reviews and my ad account, and cross-reference the personas that show up in the reviews against the personas our ads actually speak to. Show me the share of reviews versus the share of ads for each one, and flag the biggest gap."

This is the prompt behind one of the best real finds on record: a brand discovered one persona was in roughly half their reviews but only about a tenth of their ads — they made creative for that persona and it performed (`stated`, March 2026). Reviews aren't a perfect census of who buys, so treat the shares as a strong indicator rather than gospel — but a gap that wide is nearly always worth creative.

**Search TikTok**

> "Search TikTok for top-performing videos in my brand's category from the last 90 days. Pull transcripts of the top 5 and break down the mechanism of each — hook structure, pacing, why it worked. Then translate the two strongest mechanisms, not the surface content, into scripts for my brand using our persona and customer language. Once I approve a script, generate the voiceover and video."

**Research competitors**

> "Give me a visual breakdown of my competitors' ads by ad format."

> "Check my main competitors' Facebook ad libraries for ads launched in the last 14 days. Diff against what you saw last week. If they've launched a new angle, offer, or format, describe it narratively and send a digest to Slack. If nothing's new, say so in one line."

> "Pull my top competitor's Facebook ads that are top by impressions. Group them by angle and format, describe each ad narratively, and infer their creative strategy. Then contrast it with our own ad mix and identify what they're exploiting that we aren't. Package the whole thing as a slide deck I can present to the team Thursday."

**Generate reports**

> "Build my monthly creative report: the performance story over time read through the brand's business reality (seasonality, launches), top and bottom creatives with the why behind each, and next month's testing recommendations grounded in customer evidence. Output it as a deck."

**Build swipe files and briefs from the ad database**

> "Look in the Parker directory and find me animation ads under a minute long for problem-solution products, top by impressions. Build it as an HTML swipe file I can scroll, and note where each ad ranks in its own account."

> "Search the whole discovery database, not just brands we follow, for top-of-funnel statics that are top by impressions. Group them by mechanic, describe each one narratively, and save the set to a new swipe file folder in Parker so I can share it."

> "Show me what's winning across the whole database for brands like ours right now, top by impressions, grouped by format. Then diff it against our own library and tell me which formats are working everywhere and missing from our account."

> "Take these ten and turn each into a brief for us. Rewrite the script knowing everything you know about our brand and using the adapting-script method, and include a reference to the original ad in every brief. I'll review before anything gets produced."

> "From that swipe file of 50, pick the 10 most applicable to us, draft the copy for each, wait for my approval, then generate the approved ones through Higgsfield."

**Research with browser control**

> "I like this ad on screen. Break down why it works, tell me how we'd recreate it for us, then build it through Higgsfield."

> "Use the browser control — go through the top ads in my Parker library and pull out every animation ad that opens on a trigger event."

**Mine customer language for emotional triggers**

> "Read our customer reviews and pull out the specific trigger events our customers face — the concrete moments that carry real emotional pain, not general complaints. Quote them verbatim with the source, and tell me which ones we've never built an ad around."

**Query Reddit**

> "Find what people are saying about [the problem we solve] on Reddit using Parker. Pull exact phrases, the objections they raise to each other, and anything that reads like a trigger event. Link back to the original posts."

> "Follow those subreddits in Parker too, so we're pulling from them going forward."

**Work across every client account (agency)**

> "Look at every client account's statics from the last 365 days. Pull the top spenders and top performers for each, split by what we made in-house versus what we didn't, and put it all in one doc."

**Fine-tune the brain to your own work**

> "Look through every script we've ever made for this brand in Notion. Take the scriptwriting method and tailor it to us — exactly how we write for this brand. Build it as a fine-tuned skill in my own skills folder, and update my CLAUDE.md so the brain always defaults to my fine-tuned skills over the Parker system ones, falling back to Parker's where no fine-tuned version exists."

> "Every month, read the scripts we made in the last 30 days and update the fine-tuned scriptwriting skill."

> "Pull the transcript of this video, take the relevant learnings on static ads, and add them to my brain wherever they belong."

**Extend the brain past paid creative**

> "Right now this brain only covers paid creative. We also run email, SMS, and organic. Look at how the brain is structured today, tell me how you'd extend it to cover those, and what you'd need from me for each. Don't build anything yet — show me the shape first."

**Close the loop on creative tests**

> "Every day, look at our ad account and any newly launched ads, go back to our hypothesis tracker in Notion, and decide whether each hypothesis was right or wrong and why. Update the tracker and show me what changed."

**Manage ideas**

> "Add all of the recent ad ideas from the idea bank to my Ideas Library in Notion."
