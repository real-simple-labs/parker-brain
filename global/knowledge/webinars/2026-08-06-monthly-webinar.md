---
doc: webinar-2026-08-06
team: global
date: 2026-08-06
last_updated: 2026-08-07
purpose: Verbatim transcript and digest of Parker's monthly customer webinar on Thursday 6 August 2026. Covers new Parker app features (Discovery tab, affinity-brand discovery, Reddit), a run of MCP and brand-brain use cases, how to fine-tune the brain's skills to your own brand, and the announcement of a free six-week Claude Code course.
provenance: Transcript supplied by Alex on 2026-08-07, the day after the live session, in two parts — the opening arrived first and the closing stretch was appended the same day. Auto-transcribed, lightly punctuated, speaker labels not marked in the source — attribution below is inferred from context. Stored verbatim and complete through the sign-off.
summary: The first webinar logged in the brain. Alex demos the Discovery tab and affinity-brand finder, walks through Parker's new Reddit ingestion, then shows real Claude Code sessions building swipe files, ad briefs, and cross-client analysis off the Parker database. Second half is about making the brain your own — fine-tuning a scriptwriting skill on 300+ of your own scripts and overriding the Parker system defaults. Jimmy covers hypothesis-tracker routines, extending the brain past creative strategy, and plan mode. Ends with a free six-week course announcement.
source_type: first-party Parker customer webinar
speakers: Alex (host), Jimmy (guest segment), live attendees in chat
transcript_status: complete — runs from the open through the closing sign-off
---

# Monthly webinar — Thursday 6 August 2026

> **Read this first.** The digest below is dense on purpose. Most questions about this session get answered here without loading the transcript. Go to the verbatim transcript when you need exact wording, a specific answer to a specific person, or a detail the digest compressed.
>
> **Two cautions.** Product state is as of 6 August 2026 — "coming very shortly" meant that day, not today. And every figure the hosts say live (impression counts, database sizes, time saved) is `stated`, not verified.

---

## What this session covered

### The framing: use cases are the unlock

Alex opened by saying the thing that makes people good at agentic tools isn't a clever prompt, it's absorbing as many use cases as possible — seeing how someone else uses it, then recognizing the version of that for your own business. That's the whole shape of the session: expose people to workflows they haven't seen, so they go build their own.

He also named a product priority. He rarely uses the Parker web chat himself; he does everything through the MCP inside Claude Code or Codex. So every new Parker feature is now scoped around **how it improves the experience for someone using Parker agentically.** The web app keeps improving, but the agentic path is the main priority.

### What's new in the Parker app

**The Discovery tab** — shipped, and not publicly announced yet beyond a couple of YouTube videos. Every ad from every brand followed anywhere in Parker is pooled into one database, tagged with the same AI tags a brand gets on its own ads. You filter down to exactly the ad you want — ad type, format, industry, language, ad length, runtime — and, the part Alex called the differentiator, **it's sorted by impressions.** Other tools have the filters; he doesn't think many, if any, have the impression sort.

Why that matters: you're not just finding "comparison statics," you're finding comparison statics that are near the top of their account by impressions, which is a decent proxy for a winner.

> **Reading note, added on capture.** The impression-rank proxy applies to brands whose ad account you can't see. On your own or a client's account you have the real spend and performance data, and that always takes priority — never rank your own creative by impressions. The canonical rule is at the top of `creative-strategy-context/analyzing-public-ad-accounts.md`. His demo pulled comparison statics in an industry and returned ads ranked #2 and #7 in their accounts; he cross-checked one and it had been in the top 10 for the last month. Another example he'd run recently: animation ads longer than 10 minutes, sorted by impressions.

Use it two ways — when you know what you want to make, or to discover ad types you hadn't considered.

**Brands discovery / affinity brands** — this came directly from a customer request in an earlier webinar. Attendees had asked for help finding brands worth recreating ads from that *aren't* competitors. So Parker built it: it scores every brand in Parker against yours on **three variables — audience, positioning, and tone** — producing a match score, filtered to exclude direct competitors and same-product sellers. Filters let you make the matches more adventurous or safer.

Alex's reasoning for why he prefers this over mining competitors: he's a bigger fan of recreating from the organic feed than from ad libraries at all, but when he does use an ad library, he takes angles from brands selling to the same audience rather than competitors — because adapting those scripts still lands well without copying what your competitor is doing and permanently being one step behind them.

All of it is queryable through the MCP. You can ask Claude Code to find affinity brands, and then tell it to **follow them inside Parker from the chat** — they land in your ad libraries section.

There are also new analytics on brand pages: breakdowns by tag, what a brand is running, and so on. Alex called these unremarkable relative to other platforms.

**Known gap, raised live by David:** filters are not consistent across tabs. Runtime filtering exists in Discovery but not at the single-brand level. Alex confirmed this is a known internal issue he's already raised — Parker needs a pass to make filters consistent everywhere — and committed to raising it again with the team. Also noted: the ad library currently covers **Meta ads only**, and they're open to suggestions on what else to cover.

**Reddit** — the big one, long requested, and **not yet in customers' hands as of this call.** Limited testing spots were opened live; attendees were told to ping Tanner on Slack.

The reason it exists: Reddit's API is unforgiving and Reddit doesn't like being scraped, so anyone who's tried pulling Reddit through Claude Code directly knows it's unreliable. Alex said that's why no other tool has Reddit. Parker's approach is to scrape curated subreddits **on a schedule into a directory**, which you then query reliably from the app or from Claude Code, Codex, or whatever harness you use.

Setup takes about two minutes: Parker suggests subreddits, you add your own, you can add specific search queries, and you do a quick relevance pass on roughly 15 sample posts to teach it what's on target. His demo brand pulled in ~800 posts on setup and keeps growing on the schedule.

**A genuinely useful tip from this section:** to find which subreddits to follow, use **Reddit Answers** — a free tool Reddit provides. Ask it something like "I run the ads for [product]; find me all the relevant subreddits where people talk about my product or the problem it solves," give it one example subreddit to anchor on, and add what comes back. Also: after querying, ask Parker to go follow the new subreddits it surfaced, so the directory keeps deepening.

Advice throughout: follow as many relevant subreddits as you can, because more subreddits means more posts in the directory, which means better answers when you query from Claude Code.

**Feature request from the chat (Avielle):** a select-all button inside the ad library and analysis tab, to save multiple ads to a swipe file at once. Alex asked for the use case and said they'd discuss it.

### MCP and brain use cases

**Emotional storytelling / trigger-event animation ads.** Alex flagged a format he's seeing win across accounts and strongly recommended brands consider it: animation ads (often song ads) that lead with a **specific trigger event** rather than a conventional animated pitch. The trigger is a small, concrete, emotionally loaded moment — a kid noticing, a comment from a mother-in-law at dinner, a partner not looking at you the same. He named Brazilia as a good library to study, and said "quasi" is also very good at it. He personally wouldn't go as far as the aggressive DR versions ("my wife left me"), but the mechanism works.

The prompt that follows from it: ask Parker to read your customer reviews and pull the **specific trigger events your customers actually face that carry deep emotional pain**, then build ads on those.

**Building a swipe file from the whole Parker database.** He wanted trigger-event animation ads for a client (Open Farm), so he asked Claude Code to look inside the Parker directory and find animation ads no longer than one minute for problem-solution products, framed as ad inspo he'd turn into scripts. Claude Code came back with an HTML swipe document — and because they were ranked by impressions, several were #1 in their accounts. Same move at scale for a training he was preparing: **top-of-funnel statics, top by impressions, across the whole database — it looked through 120,000 statics** to build the file. One of the results had been #1 in its account for 12 days straight.

You can then tell it to save the results down to a swipe file inside Parker, create a new folder there, and share it with your team.

**Turning the swipe file into briefs.** The follow-up prompt: take each one and turn it into a brief for the client, rewriting the script using everything you know about us and the adapting-script context in the brain, and **include a reference to the original ad in each brief.** Output: 10 full ad briefs from 10 winning animation problem-solution ads, with adapted scripts. Alex estimated roughly three minutes of real work.

Honest caveat he gave live: he hadn't reviewed the output yet, so he'd want to do a quality pass and give feedback. He guessed five or six of the ten would be usable.

**Chaining to generation.** A natural next prompt he named: take the 10 most applicable of the 50 ads in the swipe file and recreate them for my brand through the Higgsfield MCP.

**Cross-client analysis for agencies, in one prompt.** He asked Claude Code to look at every client account's statics for the last 365 days and prepare a single document on top spenders and top performers, split by AdCrate-made versus not. One prompt, one doc, across all clients. The comparison he drew: he ran the same training 18 months ago and spent **two hours** scrolling accounts and pulling references by hand; this time the deck took him about **20 minutes**, because Claude Code pulled every example.

**Question from Karim — does it only pull brands you follow?** No. You can point it at either. Ask for only your followed brands and it does that; ask for the entire discovery database and it queries every ad in Parker (Alex said hundreds of thousands, possibly into the millions). You can scope it any way the Discovery tab filters allow — problem-solution ads only, unaware-stage ads only, one industry, animation only.

**Where recordings live:** circulated in Slack after the call, and uploaded to a University section in the Parker web app.

### Making the brain your own — the core of the session

Alex's framing of what the Parker brain is: **a top creative strategist's brain you can plug into your brand or your clients' brands.** All the method docs — how to write headlines, how to write scripts, how to do iterations, the whole creative strategy process — baked in, and adapted to the specific client on build, with routines and audits set up from the data in Parker.

Then the point he wanted to land: **you can make it your own, and that's where it gets really powerful.**

**Fine-tuning a skill on your own work.** With the Notion MCP connected, he pointed Claude Code at AdCrate's master Notion database for a client — where every brief and script lives, now past **300 concepts** for that one brand. First he verified it could actually see the scripts inside each concept. Then the real prompt: *look through every script we've ever made for this brand and tailor the scriptwriting skill to my brand.*

What it produced: a **script voice profile**, a **visual vocabulary** doc, and a brand-specific **fine-tuned scriptwriting skill** in the brain's own skills folder. From then on, writing a script for that brand isn't just running Parker's general method — it's running a method trained on every script that team has ever written for that brand.

**The override pattern — this is the mechanically important bit.** You can't edit `parker-system/`; it's read-only, you have read access but not write. So you don't overwrite the Parker scriptwriting skill. You build a fine-tuned version in your own part of the brain, then **update CLAUDE.md to always default to your fine-tuned skills over the Parker system ones**, falling back to Parker's when no fine-tuned version exists. Everything in the brain then routes to your version.

**Keeping it current.** Set a routine: every month, look at all the scripts from the last month and update the fine-tuned scriptwriting skill. Same move works for any context you want kept fresh.

**Other places to fine-tune from.** Slack — every message a client has ever sent you, every piece of feedback your creative team has shared, every piece of feedback you've given. Your project management system. The iterations you've made. The images you've created. Or Parker itself, since Parker holds every script from every ad you've ever made.

**Feeding the brain content you consume.** Two demos. First, a YouTube video — his own guide to static ads — pulled in through the **vidIQ MCP** with a prompt along the lines of *look at the transcript of this video, extract the relevant learnings, and add them to my brain where necessary.* He noted he hasn't tested whether Fable can extract transcripts without vidIQ, and that **Glasp**, a free Chrome extension, is the fallback for grabbing a transcript to paste in. Second, a tweet with good principles on writing static ads — dropped straight into the chat with "here's another piece of content, take it and put it into my brain as well."

The compounding argument underneath: the brain gets stronger as you write more scripts and make more ads and it dreams on its own, **and** as everyone on the team feeds in the content they personally consume. You read different things than your colleague does; all of it lands in one shared brain that knows you better over time.

**Question from David — what tool for managing client context across a team, when several people want to contribute?** Alex's answer, in order: **HQ** is his pick today and works on the free plan. **GitHub** is what the Parker brain uses now, and is fine if your team is AI-literate. The **Parker Desktop app** is coming very soon and solves exactly this problem. **Dropbox** works too if you're mounting the file system and opening Claude Code there. He passed along a customer line he liked: using Parker and HQ together is AGI.

**Antigravity.** Alex was demoing inside an IDE called Antigravity rather than the Claude Code desktop app. His honest read: **there's no capability difference** — it's the same Claude Code, just displayed differently. What you get is easier visualization of the folder structure and colored diffs showing what changed and what's been committed. His actual reason for using it that day: he's traveling without a monitor, and the desktop app runs out of room past about four parallel chats, so Antigravity gives him somewhere to put more.

### Jimmy's segment

**Question from Gabrielle — can Parker keep an ongoing feedback loop of tests, learnings, and win rate? We use a spreadsheet today.**

Jimmy's answer, and the general method he wanted people to take from it: the point of the brain is that **you just describe what you want.** Concretely — with the Notion MCP connected, spend three minutes describing your creative or hypothesis tracker: where it lives, what's in each field, what you're testing, how you keep track of hypotheses. Then build a **routine** (his plain definition for the room: a way to make Claude do a task automatically on a cadence) that every day goes and looks at the ad account, looks at the new ads, goes back to the hypothesis tracker, and determines whether each hypothesis was right or wrong and why. Trigger it however fits — every ad, or seven days after an ad goes live. Have it present the result as an artifact, or even build its own landing page showing all your creative testing.

His broader point: describe it the way you'd describe it to a teammate who has to do it manually. That's the skill.

**Question — any tips on building on top of this at a macro architectural level, merging systems?**

Jimmy: ask the AI that exact question. Structurally, everything currently in the Parker brain condenses under one parent folder — creative strategy — and then you add siblings for growth marketing, organic, CRO and landing pages, email and SMS, whatever you run. Describe the structure you want and let Claude Code recommend the changes. He named the reason it's safe: **Claude Code is built on top of Git, and Git is what lets you edit and modify files freely, which is what lets you just describe what you want and let AI figure out how.**

**Plan mode — his pro tip.** For "how should we do this" work, switch to plan mode. It won't start making changes, and you avoid the pop-ups asking you to pick between three options before you have any visibility into the reasoning. You get a clean *here's what I think we should do and why*, then you flip to auto and let it rip.

**Alex's addition — everything is reversible.** He showed his own Alex OS folder structure (businesses, content, context, call transcripts) and made the point that if he wanted to merge the businesses together or resplit his calls by week, Claude Code would just reorganize it. So don't over-engineer the structure up front. If it needs restructuring later, explain what you want.

**And: yap.** Alex cited Andrej Karpathy's recent tweet encouraging people to voice dictate everything in as much detail as possible, because AI does very well with long dictation. Think about every piece of information someone would need to know about the task, then say all of it. Don't self-edit for relevance — the model takes what's relevant and ignores the rest.

### Browser control — Claude watching you research

Jimmy's other pro tip, and the one with the most immediate leverage in it. On the Claude Code desktop app you can open a browser inside the session, and **Claude can see the page you're looking at.** Say "use the browser control" and it can also drive that side itself.

Why it matters for this work specifically: research is visual. You're scrolling an ad library or Parker's own top-ads view, you hit something good, and instead of describing it or copying a link you just say *"I like this ad — tell me how we'd recreate it,"* then chain straight into the Higgsfield MCP to build it. You work out of Parker with Claude's power sitting right next to it, in the same motion.

It also removes a step from the discovery workflows earlier in the session. Rather than Parker querying the database and handing back a list, Claude can take the browser and go find the animation ads itself.

Roadmap note from the same breath: Parker's web app is being **revamped to be more agentic**, so a "recreate this ad" action pushes into Claude Code or Codex rather than opening in Parker's own chat.

### The static workflow skill Alex is building

Teased, not shared — the workflow wasn't ready and is still tailored to one brand. Alex built it with a friend for that brand, on top of a swipe file assembled with Parker and held locally. The output he showed: **230 image ads** in one run, most of them, in his words, good to go. His framing was blunt — "you don't need a graphic designer anymore."

It isn't brand-agnostic yet. He committed to having it ready by the next webinar or in the course, where the process for building your own will be taught. Worth reading as a direction of travel rather than an available capability: the fine-tuned-skill pattern from earlier in the session, pointed at statics and pushed to volume.

### How the brain actually processes a brand — Jimmy on the architecture

Someone asked whether Parker has a real process behind big data dumps — research, analysis, agents running on judgment — since the repo is large enough that they hadn't been able to read it yet. Jimmy's answer is the clearest public statement of the brain's architecture in this session, and it matches the factory's own three-phase model exactly:

1. **Audit first.** The brand, the ad account, the competitors, the competitors' ad accounts, the market, and community forums.
2. **That dictates the creative strategy layer**, which looks at four buckets — opportunities or gaps in **personas**, **messaging / angles / value props**, **product and SKU** (including how the product is being introduced), and **creator talent** within the ad account.
3. **Then ideation, concepting, and briefing** as the final phase.

So a fresh build runs the audit, produces a creative strategy, and finds ideas, in that order. After that the team builds on top: more context, their creative operations, their creative trackers, and the brain self-improves from what it's told.

Those four buckets are the same four territories the open-loops system uses (`system/three-phase-operating-model.md`). Useful as corroboration that the shipped architecture and the way it gets explained to customers are the same thing — nothing new to promote from it.

### Make it your own — the closing argument

Alex closed on the same point the middle of the session made, stated more plainly: the Parker brain on its own is powerful, and it becomes much more powerful when you bring in everything else. Two kinds of context, both worth having:

- **Where your work lives** — wherever briefs get written (Notion, Docs), Slack messages, brand guidelines, PDFs.
- **What you come across** — any ad content or writing you see online, dropped in with "now include this."

The line he landed on, which is the whole idea in four words: *brain dump your brain.*

### Announcement: free six-week course

Alex announced it to this room first, ahead of the public announcement.

- A **six-week live course on Claude Code and Codex for creative strategy.**
- **Free** this time. They ran a paid version last year on being an AI creative strategist.
- Starts **27 August 2026**; public announcement Tuesday **11 August 2026**, via a tweet, the Slack channels, and email.
- **Jimmy teaches the first couple of weeks** — Claude Code / Codex fundamentals, aimed at people newer to this.
- **Alex does roughly four live sessions** of use cases for brands and agencies, on becoming an agentic creative strategist.
- Guest sessions included.
- Explicitly pitched at upskilling team members who are still timid with the tooling — AdCrate has people at both ends of that range.

Reason given for making it free: they want the information as accessible to as many people as possible, and they think this arbitrage window — where some people know how to use these tools and most don't — is an unusually good time to build.

Two logistics from the close:

- **The course runs Thursdays at 12 Eastern — the monthly webinar slot.** So the next one, possibly two, monthly webinars are expected to be skipped, resuming once the course ends.
- **A caveat for advanced users:** the first session, possibly the first two, are fundamentals and may not be worth their time. Three or four whole sessions are advanced use cases, and Alex wants to reach those as fast as the room allows.

The team also offered themselves directly — Slack, and calls on request. Their stated reason: every call so far has gotten someone to the moment where it clicks.

---

## Use cases demonstrated here

These were pulled into [`global/knowledge/best-use-cases.md`](../best-use-cases.md) on 2026-08-07:

1. Build a swipe file off the whole Parker ad database, filtered and ranked by impressions.
2. Turn that swipe file into full ad briefs with scripts adapted to your brand, each referencing its original.
3. Run one prompt across every client account (agency cross-account analysis).
4. Mine Reddit for how people actually talk about the problem you solve.
5. Fine-tune a skill on your own back catalog of scripts, and override the Parker default with it.
6. Feed the brain the content you consume — YouTube transcripts, tweets, Slack history.
7. Keep a creative hypothesis tracker honest with a daily routine.
8. Find affinity brands and follow them into Parker from the chat.
9. Use browser control so Claude can see the ad you're looking at and recreate it from there.

Two more were promoted on 2026-08-07 in a coverage audit, after being missed on the first pass:

10. Extend the brain past paid creative into the other channels you run — growth, organic, CRO, email and SMS — by describing the structure rather than designing the folders (Jimmy's segment).
11. Browse the discovery database with the format filter *off*, to find ad types you'd never have thought to ask for, then diff that against your own library.

---

## Full transcript (verbatim)

> Auto-transcribed from the live session. Speaker labels are not marked in the source; Alex hosts throughout and Jimmy joins for the segment noted in the digest. **This transcript is incomplete — the source ends mid-sentence.**

What's up everyone? How we doing? Let me make the chat accessible. Oh no, I've seen him change the settings again. Okay, you should be able to chat to everyone now.

Just say hello if you're in the chat. Let me know we're here. Let me know someone's listening.

What's up? What's up? Welcome in. Welcome in guys. I hope you've been well.

A lot's been happening. It's busy. It's busy.

And I don't know, I've just been spending all day, every day inside of Codecode over the last few weeks. It's been a pretty crazy time. So today I want to share with you a couple of the things that I've been doing.

I found with this stuff, you know, even myself internally with Parker and Adcrete, so much of, you know, using agentic tools or like getting comfortable and proficient with them is just learning, like absorbing as many different use cases as possible. Like seeing how other people use it and then going, oh, that's how I can actually use it to me. And I can build this workflow.

I can build this skill. So that's what I want to try and do. I want to like expose you to use cases that you may or may not have seen before.

And then hopefully that will inspire you to go and either build something similar to what I've built or go and build something yourself for your business and the way that you guys work. So, I mean, I think we're just good to get straight into it. I want to start by showing a couple of things that are new to Parker.

Basically, the way that we're thinking about this now, guys, is we are trying to scope out new features to improve the quality of the MCP. I don't know about you guys, but I think we have people from different levels of AI competence inside of here. I actually don't or very, very rarely use the web chat in the web app for Parker.

Now, I do everything through the MCP instead of core code or codec. So every feature that we're thinking about implementing is how we improve the experience for someone who is using Parker agentically. There are also a lot of improvements we're making in the web app, but the main priority is how can we enable you guys to better use it inside of core code, inside of codecs when you're building things agentically.

So we only get straight into it. With that being said, let's pull up Parker and show you a couple of things that are new inside the web app. And everything that I show inside the web app is going to flow through into core code.

As you guys know, everything's going to be queryable inside of there. So without further ado, let's get into Parker and share. Now, I think I shared this in the in the last call briefly, but it's since been shipped and there's been a couple of modifications to it.

Something that I'm really excited about. We haven't actually publicly announced that this has been launched. Besides me showcasing it in a couple of YouTube videos, which you guys may have seen, is the discovery tab.

Now, the idea of this is we have exposed every single ad inside of the Parker database. Every brand that's been followed, all of their ads have been combined into one overall database that has been tagged by all of the different AI tags that you have for your own brand inside of Parker. So I can see for every brand that I want to query what is working for them by impressions and I can filter down to the specific ad that I want.

So, for example, I find this really useful when I want to create like if I say I want to make a certain type of ad, let's just say that I want to make a comparison ad. I can filter down to comparison ads that are statics in X industry. And what that's going to go and do is it's going to find me all of these.

But as we have everything sorted by impressions, you're going to find what are good proxies for winning examples of these ads. So as you can see here, these ads are ranked number two and number seven for $14.40. They're near the top of the ad account. I can verify that by looking inside of here.

So this one has actually been in the top 10 for the last month. So we've got a pretty good idea that's probably doing pretty well for them. And again, you can scroll down here and actually this is comparison statics, quite a more niche search.

But usually you'll get a lot of number ones here and like some ads are in the top three and probably performing pretty well. So any type of ad that you're trying to create, you can go and find what are probably good ideas for winning examples of that type of ad. You can filter down to the length of the ad.

So, for example, the other day I was looking at animation ads that are longer than 10 minutes. You can look at runtime if that's important to you, language, industry, you can query down to exactly what you want. And this is available in other tools, but I don't think there are many others, if any others, that have got the sort by impressions feature.

So it's really cool to see not just like animation ads are above 10 minutes, but animation ads that are above 10 minutes, that are top by impressions or near the top by impressions in the ad library. Discovery tab, very good if you know what you want to make or you just want to discover new ads that you want to make. You also have the brands discovery here.

Now, this actually came from you guys. I remember in a webinar that we did a few months ago, we had a number of you guys asking us to help you find new brands that are not necessarily competitors, but are like brands that you can recreate ads from. So they're like what we would call affinity brands or whatever you guys want to call it, not indirect competitors.

So we did that. So we've built like how to look at every brand inside of Parker and allows you to find brands that are not competitors of yours, but like still sell to the same audience. So this is the competitors house that will serve as competitors.

But then you can also look at affinity brands that are like selling to the same audience as you, but are not like a direct competitor. So we've done that by looking at three different variables, your audience, your position, your tone. And we just basically can like found a match score for your brand to their brand, given that they are not selling the same product or like a not direct competitor of yours.

You can play with the filters here if you want to make this more adventurous or safer. But I found this to be really interesting because when I recreate like, as you guys know, or many of you know, we're big fans of recreating things from the organic feed and get inspiration from the organic feed versus competitors or other ad libraries. But if I do recreate ads from other ad libraries, I don't like to do competitors.

I like to try and take angles and ideas from from brands that are like selling to a similar audience, but not competitors of ours. Because we found that when you adapt those scripts, you can still get really good scripts without like just copying what your competitors are doing and always being one step behind them. So a lot of our customers have found this to be a very useful tab so far.

Again, all of this is curable inside the MCP. So inside of Cloud Code, you could say, go and find me brands that are like affinity brands or brands that are selling that are not direct competitors, but are selling to a similar audience than us. And it will go and find you some of these.

And you can literally say from inside the MCP now go and follow these inside of inside of Parker. If I did go and follow them, they would go straight into my ad libraries section of the brands I follow. We've also added a few other analytics inside of here.

Nothing crazy. You know, I think you guys would have seen these in other platforms as well. Just looking at different metrics on breakdowns by tags, the breakdowns of what they're running, et cetera, et cetera.

So anything that you follow inside the discovery tab will show up inside of ad libraries. If you have any questions, by the way, as I'm going through this, feel free to put in the chat. I've got the chat open so I can see and hit any questions that we've got as they come through.

Would be nice if you have the full feature of your ad discovery tab. But when I look at a single brand currently, I haven't seen a way to use runtime built on the brand level. OK, thank you, David, for raising this.

Candidly, that is something that I have raised internally as well. I am aware that right now we have filters that are that applicable on some pages, but not others. We need to do a run on all of our filters and make sure that they are consistent across all tabs because right now they're not.

So thank you for raising that. I will make sure that's raised to the team after. Because, yeah, there are some tabs right now that it's really easy to add these filters.

We just haven't done a pass at making them all consistent. The ad library does currently only cover meta ads. If you have suggestions for where else you would like it to cover, then we are more than open to see what we can do inside of here as well.

OK. The other thing that is not yet in your hands, but will be very shortly, is something that you guys have been asking for for a very long time. And we are super excited to finally have something for you ready.

And that is Reddit. Now, anyone here who's used Cloud Code to try and pull from Reddit knows they can be a little unreliable because Reddit does not like you crashing on the API or on their site to try and extract things. So we have built it into Parker in a way that you can easily, reliably and sustainably pull from Reddit into the Parker app or into Cloud Code, Codex or whatever you're using as your as your harness.

So what I want to do super quickly is walk you through the process of setting it up. And then once you set it up, you can go and query whatever you want to query. I'll show you some examples of things I've been creating over the last few days.

So this one's already set up for this brand. I'm actually going to go into a new brand where it's not been set up. It'll take two minutes to go and do this.

So basically what we're going to do is when you access this, you will see this. We're going to go through the process. And the way that we've done this is we are going to scrape different subreddits that we found.

And you can add your own inside of here as well. We're going to primarily scrape these. We will also be able to scrape outside of these.

But these are the ones that we're primarily going to bring and post into on a schedule. Now, I would advise adding your own subreddits inside of here to a tip that you can do to find what subreddits to use, because you might not know what subreddits to use inside of here. You can literally just come into Reddit Answers, which is a free tool that Reddit provides and say, I'm running the ads for Flakes, which is an anti dandruff shampoo brand.

I want you to find me all of the relevant subreddits for Flakes that I might want to follow to listen to people talking about my product or just dandruff as a problem in general. And you could even say an example is r slash male grooming. And then I'm just going to go and add in some of these.

And maybe one of the team will be able to fill in in the chat on the specific reasoning for us setting up like this. To my understanding, it's so that we can better learn what are the best subreddits to pull from, and that we can service the most relevant things, because there is a lot on Reddit that is not relevant to you or your brand. So we just want to make sure that we're putting the right things in here.

Dermatology questions. I could go and add all of these. And you can also add these in after you've gone through the setup.

So I wouldn't worry about making it perfect. But, you know, just adding as many of you as you can here that you think are relevant to your brand. You're going to continue.

And then you can go through a few of these to see like if you are like if they are on par or not with what you're expecting. So I'm just going to go through this super quickly. It's going to be about 15 in here.

That's not relevant. That's a woman. And then it's just going to go and use this to curate your Reddit feed.

You can use Reddit like the Reddit feed on here if you want. It's just basically going to be a curation of all the different feeds that you that you have. I'm more so just been using it through the MTP to query.

Again, if you want to add specific search queries here, you can. But just for the sake of time, I'm not going to. And there you go.

You have Reddit pulled into here. As you can see, now I have 800 posts that have been pulled into here. It's also running on a schedule to bring in more.

And over time, more posts are going to come in from all of these different subreddits and threads. And you can literally now start querying Reddit from the chat or querying it from Cloud Code. I would love for one of the team to jump in with an update, even in the chat, of just like what the timeline is like on when this is going to be in people's hands.

But I mean, it's working perfectly fine to me. So I would imagine it's not that far away. And then I'm going to go into Cloud Code.

Sorry, it's going to be very messy because I have a lot of chats open right now. Let's get rid of that. And let's bring in this.

OK. So as you can see here, I said find what now I said find what people are saying about Laura Geller, which is another ad hoc client on Reddit using Parker. And then it went and got and pulled like everything from our directory.

And you can query this however you want to. And if you want to find links back to the original post, it will take you to Parker from here. But yeah, you can query Reddit without any issues, because I was using it without Parker before we launched this.

And I just kept getting like it was it was unreliable. It was able to pull it sometimes, but just it didn't like it. It was not the best experience.

So this is reliable because it's pulling from a directory. And if you do find anything on here, because I actually tried to do it without. I tried to do it without Parker.

As you can see, it's still pulled things, but it was like I mean, it's it's not as reliable. But what I actually said was just now going to without Parker, I found a bunch of like other subreddits. And I said now go and follow these inside of Parker.

And now I have even more subreddits followed. So I would recommend trying to follow as many relevant subreddits as possible, because then you're going to pull in more posts. And then you've got more of a directory to work from when you are when you are querying inside of forward code.

And that like the reason we built this again is because the Reddit API is not very forgiving. That's the reason why no other tool has Reddit. So we built in a way where you can curate your kind of Reddit experience and then you can pull it through in a reliable way.

So I am super excited about getting to do this more often. Ready for base users to start testing Reddit. Perfect.

So open up to a limited number of spots. So if you just if you want to start using Reddit, just ping Tanner on Slack or you've got his email in the chat there. Thank you very much, Tanner.

Avielle says something that would be helpful is a select all button when inside the ad library and analysis tab. Did we expand on the use case there? I'm just curious, like what select or would it be to to add multiple ads at once? Would it be to. I'd imagine save multiple ads down to swipe all at once.

OK. Yeah, we can talk about that. Alrighty.

That's what's in Parker. I now want to go into some MCP and brain use cases for you guys. If I open up my core code again, I've just got a lot of chats inside of here right now.

So I want to make sure that I am pulling up the right ones. One thing that I've been using the Parker MCP and the brain for a lot over the last couple of weeks is building like using the discovery tab. I just showed you guys to build either swipe files or actually build ad briefs myself.

So something that I have been very interested in recently, I'm actually got a short YouTube video coming out next week about this is these like emotional storytelling ads. Let's see if I can find one. I can just put up here.

I'm seeing a lot of these work in accounts. And if you are a if you're a brand here, I would strongly recommend considering how you can do this yourself. So it is.

I think. Yeah. You may have seen these before, like these are like these animation as obviously everyone's seen.

But like animation ads that are very specific to certain trigger events. It's probably it is this one. Let's go for this.

You may or may not. Is that your dad? Yeah. Damn.

Perfect. It's the beers. It's been the beers for years.

How did I let it get this bad? I'm not going to play the whole ad for Brazilia, actually. Really good library to study on this. But like I have seen multiple examples of these animation ads, oftentimes song ads, quasi also very, very good at it.

Like instead of like just trying to sell it with the traditional animation ads actually leading with a trigger event, like leading the trigger event here. I was like, does my like why is my wife like not look at me the same? I mean, I'm sure you've all seen the aggressive, you know, D.R. ones are like my wife left me. And, you know, and it goes on to eventually sell the products.

I wouldn't go that far myself personally. But like there are so many examples in this white bar in ad accounts that I've seen of them working. Well, just a trigger event like this, like it could be my wife doesn't look the same anymore.

Or like I was at I was at dinner and, you know, my my mother in law made a comment about my about my pause or something like that. You can literally go into cold code or Parker and say, like, what are these specific trigger events that my customers are facing from our customer reviews? That is like deep emotional pain for them and going out to service some of those. Anyway, the reason that I am saying this is because inside of cold code, I was trying to find a bunch of these because I knew I wanted to create one for my client Open Farm.

So I literally just said, I want you to look inside the Parker directory and find me animation ads that are no longer than one minute long for problem solution based products. I'm looking for ad inspo that I will then turn to scripts. I'm basically using the discovery tab, but in the in cold code here.

And as you can see, it went and put together a little HTML document of a bunch of these. And, you know, that's something else that you can use the MCP for, like building your own swipe file. I can easily say like after this, now go and say this all down to a swipe file in Parker.

And because these are like all occurring here in the Parker MCP, these are all ads. And if it's going to say this, yeah, this is this is number one by impressions in this ad library. This is number one climbing.

I mean, it's top by impressions. This is number one already. This one is number one.

So you're seeing ads that are, you know, we can estimate are working and that we can recreate for our brand. So I do that. It went through and produced this HTML document for me.

I actually haven't seen the answers to this chat yet, but then I went and said, you know, now I want you to turn each one of these into a brief for Open Farm, which is the client. By rewriting the script, knowing everything you know about us and using the adapting script context that you have, which is inside the brain, include reference to the original ad in each brief. I haven't seen the outcome of this because I was on a call before this, but it has gone and produced a full brief.

I could have asked this in Notion if I had the Notion MTP connected. It's produced 10 full ad briefs based on 10 winning animation problem solution based ads with adapted scripts for me, for my brand. Again, so I haven't checked the quality of these yet, so I would probably want to do a pass on that and give any feedback that's relevant.

But I bet you've got at least five or six full animation ad scripts built for my brand in literally probably, you know, three minutes worth of actual work by using the Parker MCP inside of Cloud Code, which I thought was a pretty nice use case. And just for building briefs or just for building swipe files in general, this has been really useful. I mean, another use case they had for it here was saying that I'm preparing a training with the AdCrete team, which is what I just came off of, about their static ads.

And I literally asked it to go and make a swipe file of static ads that are topped by impressions across the whole Parker database. And then it went and did that. I can't see.

I don't think it's going to open. I'm going to say, yeah, I'm going to actually find the actual file, which I'll find in a second. But then I made another version of it here.

Yeah. So this literally went onto the Parker database and produced me a whole swipe file of static ads that are winning by impressions, as you can see here. Number one for 12 days straight.

And it's like I actually asked for top of funnel statics in this one. So if you're looking to build a swipe file around statics or around emotional storytelling or around whatever, you can literally just ask Parker to go and find it in the database, recreate the briefs for my brand or like turn it into a swipe file, save this to my own swipe file, create a new folder inside of the Parker web app and just save these down so I can share it with my team. Like anything you want to do here, you can do by pulling from this entire database of, you know, hundreds of thousands of ads that we have stored and tagged and ranked by impressions.

So it's really, really, really powerful. You could go and say as a follow up prompt to this, now go and take the one, now go and take the 10 from the swipe file of 50 that are most applicable for my brand and recreate them with the Hicksfield MCP. But you can go and do that inside of it.

It would go and remake them for your brand. Yeah. So it looked through 120,000 statics here, which is crazy.

And to create this swipe file. So building HTML documents like this for swipe files, actually building the swipe file inside of Parker and even, you know, actually creating ad briefs and or even like real statics for the Hicksfield MCP. That's something that I've been using this discovery tab a lot for.

If you are an agency in this call, you can also do this for cross, cross account, you know, analysis or work. So in this prompt, I was actually saying, you know, look up all of our statics for the last 365 days on every client account. And look at all of the client statics and basically prepare me a document on.

What's like, what's the top spenders for the client? What's the top things for me? All in one doc. Again, one prompt. And then I think I. Yeah, one prompt and then it was there.

I had an issue opening it, but that was that's my fault, not the not the chat. And it produced me a doc like this. I can't show that doc has got client spend on it.

But it was a doc like this, basically, where it was like ad great statics, non-ad great statics across all of my clients done in one pass. And I was I did that exact same training 18 months ago for the for the ad strategy team. And it took me two hours to scroll through all the accounts and.

And pull out the individual references, this one, I put the deck together in like 20 minutes because it just went and pulled all the examples out for me. So super cool use case of the discovery tab that you see one of your ads. That's funny.

That's funny, Gabriel. Sick. Is any point in brands that you follow in Parker? Good question, Karim.

So it depends what you ask it to do. If you ask it to only pull the brands that you follow, it will only do that. But like this is actually looking at the entire database.

Anyone here can query the entire discovery database of every ad from the hundreds of thousands, possibly into the millions of ads that we have inside of Parker. And if you wanted to query the whole database, you could just ask it to as I did. Yeah.

Look at the whole discovery database as I did here. If you only want to look at your brands, too, you can do that and it will do that. But like I'm imagining a lot of queries.

You want to look at every every ad inside of Parker. Or you could say every only look at problem solution based ads or only look at unaware ads or only look at ads in this industry or only look at ads that are animation ads. Like literally whatever you want to query from that discovery tab that I showed you earlier on.

You can ask it inside of here, either on brands that you follow or the entire discovery database. Yes. A recording of this call will be shared.

I think Tanner, one of the team will circulate in Slack either later today or tomorrow. And also it gets uploaded. If you go on to the Parker web app, there's like a university section.

We upload all of our webinars there, too. If any of the team want to watch it back. What else? What else have we got in here? Oh, I want to show up at the end.

I want to talk a little bit about making the brain your own. So a lot of you in here have got the Parker brain set up. That's going to reach a different chat this time.

A lot of you have already got the Parker brain set up. If you have not got the Parker brain set up, let me give you a quick introduction on what it is. So the Parker brain, if this is a little intimidating, ignore everything in the middle here.

Just look at the stuff on the left. The Parker brain is basically our pass at giving you a version of a top creative strategist brain that you can plug right into your brand or your clients brands. You will see all of our documents here on how to write headlines, how to write scripts, how to do iterations, like everything that you could think of from a creative strategy process.

We have baked into this brain and we've built in a way that you can adjust it to your clients. When you go and run it, you can run the brain for flakes in this case, which is the ad client. And it's gone like adapted all of the documents to flakes and set up routines and audits and done everything on the flakes account based on all the data that you have inside of Parker.

Now we have our own context that that we've baked into the brain. What I also want to encourage you guys to do is you can make it your own, too. Once you have the brain for your client or your brand, you can make it your own and customise.

And this is where it gets really, really powerful because you can make something super tailored to your brand. Let me show you what I mean by that. I'm actually going to for the sake of simplicity.

I'm going to get rid of this chap now. And by the way, if this looks different to like normal code, I'm actually using it inside of what's called an IDE called anti gravity. A lot of you are familiar with.

But if you're not, it's just basically another way. I'm still using code code the exact same way. It's just visually displayed slightly differently.

And you can see the actual folder structure like this is what is in my my local on my local laptop. This is the folder structure here. And I can click and you can see all the different skills, all of the different audits and the whole system with the Parker brain.

Here's what I did and what I have been doing for a bunch of ad clients that we have brains set up for. We have like a master, you know, brain folder that's got all the client brains in. This is just one of those client brains.

I. I might have to share my entire screen for this rather than just this. Rather than just this. OK, let's do this again.

We're going to go with entire screen. Cool. So this is the ad create notion database for flakes.

This is where we store all of our scripts. Everything is done inside of here. As you can see here, like this is just the way that we do it.

Like, you know, some people do it inside a spreadsheet. Some of those are notions. We've been set up wherever we hold hold all of our scripts and all of our briefs inside this master notion database.

If you see my YouTube videos, you might see me go through this process. We still use it. It still works.

And it's been very reliable for us. And as you can see, like every every concept we ever made. We're now we're now at over 300 concepts of this brand has been stored in this one central database.

Now, I have the notion MCP hooked up to to cloud code. And what I basically did was I said, look inside of this database because inside of it, you have the brief. This is the brief.

Some of the scripts, some of them are just general briefs. What I said was. Oops, that's not it.

But what I what I said was I said, firstly, can you see this because I was testing out and then I said, can you pull it? And then let me find the right can use. Yeah. So I basically said, can you look through all the scripts and can you see all the scripts inside of my notion database as an ad brief inside of each concept? And then I think it's the next prompt where I basically said, yeah.

So I said to it, now look through every script we've ever made for this brand. And I want you to tailor the script writing skill to my brand. So basically, the way that this works is inside of the like we have the brain here and then inside of the brain, we have the Parker system.

This is all of our context inside of your brain. All of this stuff is like your brain. And then we've got like our context that we update over time.

We add new skills. We add new context inside of here. You can't change the Parker system because you've got you've not got right access.

You've only got access, but you can obviously change the rest of this because it's your brain. So what you can do is you can't like overwrite the scripting skill inside of here. You can build like a fine tune scripting skill inside of the rest of the brain.

So I basically said, look up every script I've ever wrote inside of notion. And I want you to take the script writing doc and tailor it to my brand for exactly how I write flicks. And it wouldn't did that.

I went and looked through every single script that I wrote in notion, all 300 or so of them. And it created a bunch of different documents off the back of it. It created a script, voice profile, visual vocabulary.

It created in the cloud. There's a skill that's called flake script writing, kind of fine script writing. And I just basically said that go and tell this exactly to my brand.

And like now, next time, write a script for flakes. It's not just going to be going off of the Parker. Here's how you write a script.

I think content is also going to be trained on every script I've ever wrote for flakes inside of here, which is super powerful, because then you can just say every month, go and look at all the scripts in the last month and. And update the the fine tune script writing flake skill so that it's up to date or even set up a routine for that. And you can do that for any context that you want to update.

And if you want to update, you know, based on the the images that you've created, if you want updated based on iterations you've made, you can get to look into your project management system or just inside of Parker itself, because Park has every single script from every ad that you've ever made and get it to create like a tailored, fine tuned skill for you. Now, you might be wondering what happens then if you've got a fine tune skill on the local and you've got a a set of skills, like default skills inside of the Parker system. What I basically did is I said here, what I want you to do is instead of creating subcontext docs, which is what I was doing firstly, create a fine tune, a fine tune script writing skill on my local and then update the Claude MD, which is just basically the kind of overall instruction file to always default to my fine tune skills rather than the Parker skills.

So there's not a fine tune skill, don't default to it. But now I've got this fine tuned script writing skill that knows everything I've ever wrote on scripts. It knows my visual vocabulary.

It knows my voice profile. It knows exactly how I write. And everything in this brain is going to default to my fine tune script writing skill versus the Parker system one.

If you don't create this, obviously, you're still going to have all of our context on the Parker script writing skill. But this is how you can really make it your own. And it's just one thing you can do, by the way.

You can also get it to go into Slack. I could send a follow up here and say, now look at every Slack message the client has ever sent me or every Slack message that my creative team has ever shared or every Slack message from every piece of feedback I've ever given. And ingest all of that context to into the script writing skill or into the brain.

And you can really make it tailored to you and your brand. So it becomes this system that has all of the relevant context that it needs about your business. And it's not just context from the like your project management that you can pull in here.

If I go back to the other chat that I had open, this one, you can see that I basically said I went to my YouTube channel because I put out a YouTube video last week about the ultimate guide to static ads. If you wanted to include that in your brain, you could literally just say, look at the transcript of this video, extract the relevant learnings and add to my brain where necessary. I don't know if Fable can extract transcripts.

I have the vidIQ MCP, which is how it did it here. I haven't tried it like outside of the vidIQ MCP. Otherwise, you can use Glasp, which is a Chrome extension to extract the transcripts and just paste the transcripts in here.

But because I've got the vidIQ MCP, it was able to just take the link and turn it into a transcript. But anyway, point being, you can say, look at the transcript from this video and just take the relevant points about static ads in this case and just absorb that and put it into my brain where you think is necessary and create something that improves the context. And again, you can just keep adding more and more things.

If you see tweets, you know, I saw a tweet the other day I thought was good. Here's some just good headlines, good principles on writing static ads. I just took that and it's somewhere down, down the chat here and said, hey, here's another piece of content.

Take that and put it into my brain as well. And the brain is going to get stronger and stronger over time as not only as you write more scripts and you make more ads and it learns more with the dreaming that it already does, but also as you add more content yourself. Like, you know, you may consume different content to me.

You may consume different content to Jimmy. You may consume different content to your creative strategist. And everyone can just feed in the content they want into this shared brain.

And it gets stronger and stronger. It knows you more and more over time. And if you're using a tool like HQ, you can have this thing cross your entire organisation, which I know a lot of you guys do.

So it makes it really easy to share this context and build this brain that just gets stronger and stronger, stronger the more that you use it. Anything in the chat? I appreciate I was talking for a while there. I know that I'm going pretty, pretty fast on this.

I'm just trying to expose you guys to a lot of use cases, as I was saying. But if this stuff doesn't, here's a good time to talk about this actually. If this stuff, it does sound a little bit overwhelming to you and you're still a little bit hesitant and, you know, you're playing around with code, you're playing with the brain.

You don't know exactly how to get the most out of it currently. I actually have something very timely that I'm like super excited, super excited to share with you guys. A lot of people here or some of you here may have been in Jimmy and my paid course last year around being an AI creative strategist.

We are actually going to be running that back and making a version this year that starts at the end of August. And this time is going to be free. So we're going to do a six week course all on code and codecs for creative strategy.

So if this is interesting to you or if this is like, oh, I want to learn more about this. I've got, you know, so much more content, so many more use cases that I could share on this. Jimmy's also going to come in and do a great job on, like, helping people understand that they're newer.

If they're newer to code, if they're newer to codecs or if you've got team members, if you've got team members, like we have ad create. We have some people who are like super advanced and like pushing agentic workflows to the limit. We have some people are still a little bit timid and don't know how to use the stuff.

If you have team members that you want to upscale into code and and codecs and just working agentically as a creative strategist, enrol them into this course. I don't have a working landing page for you yet because we're announcing on Tuesday. But like you guys, the first people that I've told outside of like the internal parking team and the ad create team, free six week live course.

We have some guest sessions in there as well. That's going to be super exciting. So if you want to learn more about this stuff, look at the announcement on Tuesday.

And we'll also post it in your Slack channels. Make sure you get yourself signed up. Make sure you get your team signed up because it's going to be a lot of fun.

And I mean, I think it's just the most incredible time to build, whether you're building an AI tool like we are, whether you're building a brand, like the amount of leverage that you can have and this this period that we have of arbitrage where some of like some people know how to use it, but most don't. I think it's such an incredible opportunity right now. So, you know, we decided to do it and we and we're like, we don't want to charge for it this time.

We just want to make it free because we want to make this information as accessible to as many people as possible. So that is something that we are super excited to announce. I believe it starts on the 27th of August, but the announcement is going up on Tuesday.

So you'll probably see some stuff about it on socials if you are in the Twittersphere. OK, David asks, what tool do you suggest for managing client context across all your team members in the example of various team members wanting to contribute to it? You can use GitHub. We currently use GitHub for the Parker brain.

HQ is probably the best option on the market today. And I think Jake is very smart and it's a very good business. Or the Parker Desktop app is coming very soon and it's solving this exact problem.

So you can wait on that. But right now, you can literally do that on the HQ free plan, share context across the team. So that's probably the best option today.

If your team are more AI literate than GitHub. But yeah. Dropbox works too if you're mounting the file system and opening code.

Yeah. Yes. There are different options.

I would personally choose HQ today. Yeah. A lot of people have said that.

A lot of people have said we're using Parker and HQ alongside each other. I can't remember who it was that said this, but someone said that using Parker and HQ together is AGI, which is pretty cool. I agree.

It's insane the stuff that you can do. Will you share with us the sign up? Yes. On Tuesday, we will share.

I might even, if the line of pages are ready before then, I'll share it before Tuesday. There will be a tweet that goes out on Tuesday and we'll make sure that everyone here gets an email or a Slack message with a link to sign up. So you can share it with your team.

Completely free. Six weeks live. If you were in the course last year, you know the format.

So we're going to teach live and Jimmy's going to cover the first couple of weeks. It's going to be called Code Codex Fundamentals. And then I'm just going to spend literally four sessions live like this, like showing use cases for brands, for agencies.

And exactly how you can become like an agentic creative strategist. So it's gonna be a lot of fun. Yes.

Jimmy, would you like to come on, Jimmy, and talk about it? If you can't come on camera as well, you're more than welcome. Sorry. So Gabrielle asked anyway that you would use Parker to keep an ongoing feedback loop of tests, learning and win rate.

We currently have a spreadsheet to keep track of that. I want to see if I can make Jimmy a host. Yeah.

Jimmy, if you leave and rejoin so you can come up. Jimmy is the mastermind who's built a lot of this stuff. So he's a great person to ask this question.

Yo. Yo. There we go.

Dude, I'm doing well. Good work. OK, so the coolest thing about the Parker brain, kind of what Alex was talking about, is you really just get to explain what you're looking for.

And as long as you have the brain or some sort of like folder system set up for it to go and build. I mean, you could even use this as the foundational one. What I would do if I were you is.

And let me share my screen. So. So let's just say that I am I'm this is our demo account.

So I'm I'm 81 and I'm looking to to build this out, this sort of like creative tracker. What you would do is you would go into your notion, however you have it set up. And as long as the notion MCP is there, I would just essentially spend three minutes describing to Parker like, hey, this is essentially how we keep track of our creative hypotheses.

Here is either the notion of the Google sheet. Here's what's in each file. And you can really just go in and say this is what we're looking at.

This is what we're testing. And you would be able to create either like a routine, which which if you are familiar with cloud code is really just the way to make a quad do automatic tasks for you. So you could say, I want to create a routine where every day you're going and looking at our ad account, you're looking at our ads, you're then going back to the creative tracker or the hypothesis tracker and determining if we are right or wrong.

And I want you to do this on every ad. Now, you could get this to be pretty robust to the point at which you could have Parker go and update this like your tracker every day based on any new ads that are launched. So as long as you have it within the creative tracker, so he would know really what you're looking for, you would be able to have it so Parker could kind of keep a running node system inside of this brain.

So, yeah, again, if I were you, I would just sort of come in here and it'd be easier if I could see like exactly how you have set it up. But you could just use whisper flow, say this is what we want to build. We want you to go in.

We want you to look at our ad account, describe the exact process that you do. So every time the ad is live or after seven days or whatever it is, since it went live, I want you to go and look at our our hypothesis tracker, determine if our hypotheses were correct or incorrect, why you believe that to be the case. And I want you to present that information to me in some sort of artefact or like you could even create like your own landing page for this that's just looking at all the creative testing that you're doing.

So that's like what I hope you guys really learn more than anything is the way that the brain is set up, the way that cloud code works, especially when you have the underlying. So like the reason why we like cloud code is because it's built on top of Git. Git is really just the technology that allows you to edit and modify files, which enables you to just describe what you want and let AI go and figure out how it should be done.

So yeah, Gabriel, what I would say is if you just went in and like pretended as if you had to describe to a teammate how they would go in to keep track of this. And as long as that's all connected inside of your cloud code or codex, it's going to do a really good job of doing that automatically. And if you start to add in those routines to just do it without even you needing to like prompt it, the better.

Any tips on building on top of things macro level architecturally was going to merge systems. Yeah, totally. I mean, like, again, it's my answer to everything, but AI is going to be the best person to even just ask that exact question.

Like if you went into the Parker brain that you had created and said, you know, this is very much so our creative strategy arm. We want to add in organic. We want to add in, you know, conversion rate optimisation.

We want to add an email and SMS, just creating multiple different folders. Everything that's in the Parker brain could just be condensed into one extra parent level folder, which could be creative strategy. And then you could have growth marketing, you could have organic, you could have, you know, CRO landing pages, whatever you wanted and start to make this your own.

And again, the deal, what I would say is just describe the changes to, especially if you use a model like Fable 5, describe the changes and kind of the build structure that you're looking for. And because of Git and just what Cloud Code and Codex can do, it's going to be able to go and recommend those changes for you. One pro tip, if you guys are familiar, so there's different modes that you can choose here.

When you're doing something like that, that's more like, OK, I want to think through how we could do this. Always just use the plan mode. That way it's not going to go and just start like making changes.

Plus, then you're not going to like sometimes if you use Cloud Code, there'll be pop ups of like, oh, do you want me to, you know, here's three options that we could do. Which one do you want? But you don't really have the context into how it's been thinking beforehand. So when it's in plan mode, then you just get a nice, clean, easy, hey, here's what I'm thinking we should do and why.

And then you can switch it back to auto to kind of rip through it. The only other thing that I add to that is already a comprehensive answer on that is that just remember that everything's reversible. Like this is this is my like Alex OS full of structure.

I have everything about like different businesses, content, context of everything, all my calls, transcripts, everything. But if I wanted to say if I built this out and I wanted to say to Cloud Code, hey, now go and reorganise this such that like all the businesses merge together. And I want I want you to split up my call by I don't know, by week or whatever.

Like it could very easily go and reorganise your structure. So I wouldn't place too much emphasis on having it perfect, because if you need to restructure after, you can very easily do that by just explaining what you want to to Cloud Code, as Jimmy said. And the other thing I'd say on that is I'm sure you guys are probably using it already.

But like Andrej Karpathy put out a tweet somewhat recently, basically just encouraging people to yap like voice dictate, voice dictate everything in as much detail as possible, because AI does really, really well with just long yap sessions. And if you just explain, just think, what is every piece of possible information that I would need to know about this migration? Just yap it down and don't worry if you if you think that you're agreeing with things that are relevant, because it will just take the things that are relevant and use that to do whatever the task is. So, yeah, that is that's anti-gravity, Maggie.

So inside of here is anti-gravity. It's an IDE, which is just a free, like, harness that you can use Cloud Code in. The reason that you would use this versus doing it in Cloud Code, like yourself, like there's not nothing you can't do inside of anti-gravity that you can't do inside of Cloud Code.

It just does make it easier to visualise the file structure. You can do this in Cloud now and Jimmy, maybe it was correctly, but I don't think you get the different like it shows you changes in terms of the yellow and the green colours inside of Cloud. If you do it like this, so this is actually a really good way to visualise like what's changed, what's been committed to GitHub if you do use that.

But yeah, just another like this is using the Cloud Code API. So you use it the exact same way you do inside of Cloud Code. It's just a different way to display it visually.

There's no difference in actually like what it can do versus doing inside of Cloud Code. Actually, another reason I will use it is I'm travelling right now. I don't have a I don't have a monitor with me.

So when I'm on Cloud Code and I have like four chats going at the same time, there's no space for more chats on the on the desktop app. I also have chats going anti-gravity as well, so I can have more chats and without having to hook up the screen. So, you know, that's another reason I use it, but there's no real difference.

I still do most of my chats in in the Cloud Code or Codex, but it's just another way to use it. One one other thing, too, that we love to show people as well. One of the cooler things that you can do now with Cloud Code is at least if you're on the desktop version is you can essentially be using the browser.

So, you know, normally this is kind of what it looks like, but you can actually open the browser. And what's cool is that Cloud now has access to see what I'm doing over here. So especially when you're going in research and if you're looking at, you know, different ad libraries or or anything along those lines, like, you know, you can just you can just go through like top ads, for example.

And, you know, if you saw this, you could be like. I really like this ad. Can you just tell us how we could recreate it here and then use the Higgs field MCP and actually go and recreate it.

And that way, like, you can kind of work out of Parker while also still having, like, the cloud experience and the cloud power right next to it. So this is something that we've loved. We're going to be revamping the web app to be more agentic as well to be able to instead of just being recreate ad in this open inside of our chat.

We'll have this actually go into, you know, Cloud Code or Codex or wherever you work out of. But that's just one like other pro tip that we have really enjoyed. And yeah, you can say, like, use the browser control.

So, yeah, just something that we found that's that's really, really powerful. And it makes the whole experience more visual because that way to even, you know, when Alex was saying, like, hey, go and find me animation ads like this or whatever it is. It can actually just go and use the browser like it can take control of that right hand side and just like go and do everything for you.

So, yeah, it's it's pretty sweet. It's it's it's really powerful. And I think it's just a glimpse of what's to come in this whole world.

Yeah, absolutely. One more thing I want to share. I'm not going to have time to share the actual workflow behind this.

And it's also not ready for me to share with you guys. But by the next webinar or by the course, it will be. I've been refining my static workflow skills.

This is something that I built with a friend of mine for his brand. And I mean, it's getting ridiculously good now. This is based on a swipe file that I built with Parker.

That's just on my local. And it's a skill that, as you can see, I put out two hundred and thirty image ads. And they're like, they're good to go.

Like a lot of them are. It's it's scary how how good these again, you don't need a graphic designer anymore. So I don't have anything to share with you guys yet because this is this is still tailored to this brand.

It's not brand agnostic yet, but. I will have that done very soon. And if you're in the course, I'm going to be teaching you the we're going to be teaching you the process to go making one of these yourself.

So you can actually pump out hundreds of statics, high quality statics as well. They're ready to go inside your account using Parker MCP. So that's going to be super exciting.

But, yeah, things are things are moving right now. It's a fun time to be building. We are almost at time.

If you've got any other questions, feel free to drop them in the chat. This recording will be going out as well with the transcript. So you guys will be able to put this straight into your code and just say, go and do all of this for me.

Is there a way that Parker approaches big data dumps? Like, is there a process built in that follows research processes, analysis, agents running on judgement, etc.? The repo is quite extensive, so I haven't been able to look into it yet. Jimmy? Yeah, I mean, we built it out and it starts with an audit, looks at your brand, your ad account, your competitors, your competitor ad accounts, the market, community forums, all of that. That's what dictates the creative strategy layer, which is looking at four buckets, which is opportunities or gaps in personas, messaging slash angles or value props.

The product SKU and how you're introducing the product and then the creator talent within your ad account. That is then going to go into the final phase of like this ideation, concepting, briefing. I can dive into that much deeper if you want.

That's a very high level, but that's how we've structured the brain to work. So when you set up the brain, it will go through the audit, it will come up with a creative strategy and then it will find ideas for you in the simplest way. I don't know if that answers the question, but yeah, that's at least like how we have built it.

So then you can go and build on top of it, add more context to it, add your creative operations, your creative trackers, like truly just make it your own and it will self improve based on everything that you're telling it. Yeah, and that's what I really want you guys to get from today, as we were saying earlier, like the Parker brain on its own is very powerful, but it becomes even more powerful. So much more powerful when you really go in and make it your own by bringing in all different contexts from your connectors, like wherever you do briefs, whether that be Notion or whether that be docs, all your slide messages, all of your guidelines, PDFs you've got, whatever.

And then also on top of that, actual context regarding ads, like any content you see online, you can just drop into the brain and say, okay, now include this and now include this. And just over time, it's going to get so powerful, the tool that's built, like customised for your brand and has all the context that it needs to have that you guys have in your brains in the folder. So it's fun.

You can just see it getting better over time. It's so exciting to watch. Brain dump your brain.

Exactly. It's a brain dump to your brain. Of the brain.

Anyway, we're at time. Thank you guys so much for joining. I think it's likely because we're going to be doing the core sessions on this time slot, Thursdays at 12 Eastern.

So it's likely that the next one, possibly two webinars of these are going to overlap with the course. So we won't be doing them. But as soon as the course is over, we will be right back into these monthly webinars.

So hopefully we get to see you guys there. Again, we will put in the link in your Slack channels as soon as the landing page is ready. If not, you'll see an announcement on socials on Tuesday.

We would love for you guys to have you and your teams inside of inside of the course. The only thing I'll say is if you would consider yourself more advanced, then we're going to spend for whole three or four whole sessions on just like advanced use cases. But we are going to have a lot of people in there who are newer to code code.

So the first one, possibly two sessions, definitely the first one may not be as applicable for you. But like I'm I want to get to use cases as soon as possible, because I know that's where people can get the most value as soon as you understand the fundamentals. That's just a bit of a caveat.

We would love to see you guys all there, like inside of the course and learning how to use the Parker MCP to build authentically. Yeah, yeah. And I've been thinking that stuff while trying to build a Parker into our company OS.

So having that stuff in separate functions has been interesting. Yeah, yeah, yeah. It's it's like we said, everything's reversible.

So you can you can just ask the AI like how to how to best build it and restructure if you need to. But yeah, it's a lot. Anything else, Jimmy, you want to cover? I don't think so.

I mean, again, like we truly are here to help. If you guys are confused about Parker Brain or how to use it best or if it's set up, OK, like we're all on Slack, you can hit us up. We are more than happy to jump on calls because so far it's like every time that we jump on a call, we get them to that like aha moment of like, oh, like I get this.

So, yeah, use us. We're truly here to make your lives easier and show you guys the way to a gigantic creative strategy. Awesome.

Well, thank you guys for spending your Thursday lunch with us. We very much look forward to hopefully seeing you inside the course. If not, we'll be back with the monthly webinars after the course.

Thank you, everyone. Have a great rest of your week and we'll see you soon
