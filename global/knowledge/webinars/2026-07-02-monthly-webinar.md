---
doc: webinar-2026-07-02
team: global
date: 2026-07-02
last_updated: 2026-08-07
purpose: Verbatim transcript and digest of Parker's monthly customer webinar on Thursday 2 July 2026. Covers what shipped in the Parker app that month (AI tagging, the swipe file and Chrome extension, the Discovery and Discover Brands betas), the first full public walkthrough of what the Parker brain is and how to set it up, and a run of real Claude Code sessions demoing reports, competitor digests, static generation, and routines.
provenance: Transcript supplied by Alex on 2026-08-07, logged five weeks after the live session. Auto-transcribed, lightly punctuated, speaker labels not marked in the source — attribution below is inferred from context (Alex hosts, Jimmy co-hosts, Manish speaks at the open). Stored verbatim and complete through the sign-off. Logged after the 2026-08-06 session, so it enters the folder as the older of the two.
summary: The session where the Parker brain was first walked through end to end for customers. Alex covers the month's app releases — AI tagging across every ad, the swipe file and Chrome extension, the Discovery and Discover Brands betas — then spends most of the hour on the brain, its setup sequence, and real Claude Code sessions. Jimmy demos the new /set-up-brain intake and pushes the review-agent pattern. The strongest durable contribution is the setup order, connect your own tools before the build, and the prompt where you describe your own week and ask what can be automated.
source_type: first-party Parker customer webinar
speakers: Alex (host), Jimmy (co-host), Manish (opening remarks), live attendees in chat
transcript_status: complete — runs from the open through the closing sign-off
---

# Monthly webinar — Thursday 2 July 2026

> **Superseded on product state. Read this first.**
>
> This session is **five weeks older** than the [2026-08-06 session](2026-08-06-monthly-webinar.md), and the product moved a long way in between. Several things described here as "in beta," "coming soon," or "not pushed yet" had **shipped** by 6 August. Where the two sessions disagree about what exists, **the newer one wins** — check the August file, or the live product, before telling anyone something is or isn't available.
>
> The specific supersessions are called out inline below and collected under [What has since changed](#what-has-since-changed).
>
> **Two standing cautions**, same as every file here. Product state is as of 2 July 2026. And every figure the hosts say live — prompt counts, member counts, view counts — is `stated`, said from memory on a call, not a verified product spec.

---

## What this session covered

### The framing

Alex's stated goal for the hour: clear up confusion about what the Parker brain is. Some people had read the launch tweet the previous week and assumed the brain was **a separate product from Parker**. His answer, made twice — it isn't. The data sources built into the Parker app over the preceding months are exactly what feed the brain, and they're what make its outputs good: AI tagging on your own account, your performance data, competitors' tagged ad libraries. "You can't get the AI tagging on your ad account, the performance on your ad account, the competitor's ad libraries that are also AI tagged and all those other things. That's what makes the brain's outputs that much more intelligent on top of all the creative jazzy context that it has."

He also chose to demo **saved chats rather than live prompting**, deliberately, because the point of the session was exposure to use cases rather than watching one get built.

Jimmy prefaced with an honest disclaimer that set the tone for the whole session: **the setup experience was not simple yet**, there was a lot of work to do on their end, and he'd be in the chat helping anyone who hit a snag. Manish opened with thanks and a note that the brain was being built on customer feedback.

Alex polled the room on Claude Code comfort, 0 to 10. The answer was **a wide mix** — several 8s and 9s, several in the middle, some who had never opened it.

### What shipped in the Parker app

**AI tagging — the big one.** Every ad in your account is now AI-tagged across **five variables**, and so is every ad in the Inspiration tab, for every brand you follow, with no work from you. Tags are editable per ad.

What it unlocks is reporting: which ad formats are spending best, the awareness-level distribution across your account or just the last 30 days, and the same cuts against competitors. Alex noted he does most of this reporting **through Claude Code rather than in the app**.

The combined move he named, and the one worth stealing: take a competitor's **top 10 ads by impressions**, then look for **commonalities in the AI tags** across that set — format, emotion. Impression rank narrows to probable winners, the tags say what they have in common.

> **Reading note added on capture.** That move only holds for accounts you can't see inside. Impression rank is a substitute for data you don't have, never a supplement to data you do — for your own account or any client account you have access to, the real spend, ROAS and fatigue data wins and impression rank is a downgrade. The canonical rule is at the top of [`analyzing-public-ad-accounts.md`](../../../creative-strategy-context/analyzing-public-ad-accounts.md). Alex's own framing on the call was consistent with this: he described impression rank as the best correlate available "besides the ones that are in your actual account, but obviously we can't see any of those."

**Brock asked how awareness level gets tagged.** Answer: **Eugene Schwartz's five stages of awareness**. Parker watches every ad and assigns the stage it judges the ad to sit at. Alex's caveat, given unprompted: it's **not an exact science** — some ads can't be pinned to a single stage, so it picks the most applicable one. His read overall was "pretty accurate."

**Not available: custom tags.** Requested by several people, under internal discussion, no commitment. **On the roadmap: auto-tagging by persona and angle.**

**Swipe file and the Chrome extension.** Boards, folders, team sharing — Alex was upfront that this view is familiar and not revolutionary. What he liked is that it removes a separate tool from the workflow: **every ad anywhere in Parker has a one-click save-to-swipe-file button** — the Inspiration tab, the TikTok tab, the performance tab.

The **Chrome extension** saves from outside Parker: Facebook Ad Library, Instagram posts and Reels, Pinterest, TikTok, and YouTube Shorts. You can also paste an ad-library URL straight into the app and pick a board.

**Ben asked for saving by Instagram DM.** Not available. Alex called it a great suggestion, said it had been requested by several people, and that he wouldn't be surprised to see it soon.

**Performance tab, minor updates.** Assets downloadable as **GIF** (for retros and reports), and **live shareable reports**. A full written debrief had gone out in the customer Slack channel.

**In beta at the time.** The **Northbeam integration** — Northbeam visible in the performance tab, with the option to have every query read Northbeam data instead of, or alongside, the ad-account data. And the **post-purchase survey integration**, which Alex said was already live for some brands and would be with everyone very soon.

**The Discovery tab — beta.** Every ad from every brand any Parker customer has saved, pooled into one queryable database and filterable by any AI tag. His demo filtered to **AI animation ads sorted by impressions**; the results came back ranked **#1 in their own libraries**, verifiable on each ad's performance trend. He flagged it was **slow to load** in beta and that he needed to fix that. More filters were coming, **industry** named specifically — so you could ask for winning ads in skincare, or authority-figure ads in health. Someone asked about **filtering by country**: Alex said language wouldn't be difficult, country he'd have to check with the team. **Open at the time: whether Discovery stays its own tab or gets folded into Inspiration.**

**Discover Brands — beta, and not yet shipped on the day.** Alex and Jimmy disagreed live about how close it was: Jimmy said it would go out right after the webinar, Alex said he still had a final pass and didn't think it was ready. It finds brands that sell to your audience but **aren't direct competitors** — similar tone, positioning, or angle — shows the comparison across those variables, and lets you view their ad library or follow them. It came from repeated customer requests.

The workflow he built on it, and the reason he prefers it: **find brands selling to a similar audience but not competing → see what's working for them by impressions → use that as inspiration.** "That is way better than just looking in the Facebook ad library at a random brand." His reasoning for avoiding competitors specifically: "I don't want to copy my competitors because then you're just one step behind."

### The Parker brain — what it is

Alex's plain definition: Parker's knowledge, open-sourced into a brain you connect to Claude Code, so you can do your creative strategy inside Claude with everything else Claude can connect to.

The clearest argument he made for why it exists at all was a build-versus-ship story. Customers had been asking Parker to build **ad production** into the app. "We could have spent a few weeks building that on the engineering side, or we could have spent time working on this brain, where now you can... just say, look at my competitor's ads by impressions, find me the top five static ads, and use the Higgsfield MCP to go and build these ads for me."

His framing of Claude Code versus the regular Claude chat, and the reason he pushes it: a chat doesn't compound, a folder does. Every correction and every piece of feedback gets written into the folder, so the whole thing gets smarter each time. "There should be no reason why you ever need to have a chat in Claude chat again."

### Setting it up — the sequence he taught

**1. Connect your tools first, before you generate the brain.** This was his lead instruction, and he gave the reason: generating the brain is the most token-intensive step in the whole process, so anything connected beforehand gets pulled into the build itself rather than bolted on after a V0 already exists.

Where: **Customize → Connectors.** His own set, named live — **Canva**, **Google Calendar** (for call transcripts), **Higgsfield** (generation), **Parker MCP**, **Slack**, and **Gamma** (for retro decks). His rule of thumb: anything you currently use to do strategy should be in there.

**2. Install the Parker MCP.** Connectors → add a custom connector → name it Parker → paste the link (available in Parker settings; Tanner also shared it in chat). Test it works.

**3. Clone the repo and ask for a brain.** Roughly: *clone this repo and produce a Parker brain for my client X.* If you're a single brand with one org, you don't have to name the client — Parker reads your account. Agencies and multi-brand orgs do. If it's ambiguous, it asks. Each brand lives in its own folder on the laptop; Alex showed two of his.

**4. Or use `/set-up-brain`** — newly released, and Jimmy demoed it. It detects an existing brain and **asks before deleting anything**. Then it runs an intake of roughly **10 questions**: main business objective, paid-social objective, north-star metrics, and so on. It ends with an open one — *is there anything else I need to know about your brand?*

**5. Jimmy's calibration for that last question, and it's the useful bit.** Voice dictate it, and pitch the level of detail like this: **if you're a brand, tell it everything you'd want an agency you just hired to know. If you're an agency, tell it everything you'd tell a new strategist joining the account** — the processes, the tools, the data sources, where your ideas database lives, what the asset statuses mean. His worked example: "I have our Notion MCP attached. That's where our database of all of our ideas lives and the status of the different assets live."

**6. Then the build runs.** Jimmy: roughly **80 to 100 prompts** spin up, running a full audit of the brand, its competitors and its creative strategy, plus transferring Parker's creative-strategy knowledge across.

**7. Plan and model guidance.** Alex recommended the **Claude Max plan, ideally 20x**. The build takes **a number of hours**. On the 5x plan it still works — you'll just hit the five-hour usage limit a couple of times along the way. His framing: it's token-intensive **only on the first build**; running it afterwards is far more manageable. Jimmy added: **use Fable 5 to generate the brain** if you have the credits — "the output truly is amazing" — with the same warning that it burns through them.

Both of them offered direct help repeatedly. Jimmy had been sharing a Calendly link for setup calls.

### The use cases he demoed

**Monthly creative report.** "Go and produce me a monthly creative report." It built a slide deck. He then said *now build it with Gamma*, because Gamma is what AdCrate uses for retros, and got back an editable Gamma file he liked better. His emphasis, twice: **zero prompting** — he gave no direction on which metrics, what structure, or what recommendations to include. Then he made it a routine: delivered every Monday at 9am.

**Correcting it live, which is the part worth copying.** In the same breath as setting the routine he said: *if you're over-indexing on ROAS too heavily here, I want you to focus more on spend as a primary metric inside the ad account.* Then his own honest aside — "I probably should have said update the context to reflect this and we'll see if it does that or not." A correction only compounds if it's written down.

**Competitor analysis.** He pointed it at **The Farmer's Dog**, one of Open Farm's biggest competitors: read the account, find what's working via top ads by impressions, juxtapose it against the client, and give recommendations. One prompt, no direction on shape.

**Competitor digest into Slack.** "Check my main competitors' ad libraries, look for ads in the last seven days, see if there's anything interesting, if there's something new I need to know, send it to me in Slack as a digest." It ran, and posted into AdCrate's internal Open Farm channel. He then said *set it up as a routine*, and it did — now every Monday.

**Jimmy's note on routines: you don't need the routines tab.** Natural language in the chat is enough — "I love this presentation, can you set this up to generate every Monday at 8am and send it to Slack?" — and it wires it up for you.

**Statics from external winners.** "Look at my external brands by impressions and find ones that make the most sense for us to recreate, then draft the copy for us to recreate them." It went through the Parker MCP and produced roughly **ten statics** through Higgsfield with the copy untouched. His honest read: some weren't good, but several he'd consider **pretty much good to go**, spun up in a few minutes.

**Statics from customer sentiment.** "Search through my brand's customer reviews, Facebook ad comments, et cetera. Look for emotionally loaded customer sentiment, cluster them" — then turn the clusters into statics. One prompt, no intervention. He showed the output and called the copy on one of them not great.

**Populating the ideas library.** After the brain generated ad ideas, he said *now go and populate all of these into our ideas library in Notion* — and **six ideas** landed in AdCrate's real Notion database. His point: whatever your ideas live in — a spreadsheet, a Google Doc, Notion — it writes into your existing workflow rather than replacing it. And it can be a standing routine: ten fresh ideas every Monday morning off your competitors or inspiration brands.

**Following a brand into Parker from the chat.** A competitor analysis surfaced a brand that wasn't saved in his Parker and flagged it as a good comp. He said *follow this inside Parker* — and it was there in the app. The point he wanted landed: the brain and the web app aren't two separate things, and natural language in Claude Code can act on the app.

**TikTok.** "Search TikTok for the top performing videos in my brand's category for the last 90 days." It returned videos plus scripts to recreate them. One he liked for Open Farm had **10 million views** (`stated`).

**Jimmy's add — the review agent.** If a one-shot generation isn't good enough, layer a second agent on top: "set up a separate review agent that's going to look through all of the ads that are generated and essentially give feedback on how to make the copy better and then regenerate the ad with that feedback in mind." His framing of the whole session, really: Parker ships the foundation, you build on it.

**Alex's advice to anyone new, and the strongest single tip in the session.** Once you're set up, **voice dictate for ten minutes**: this is how I spend my week, on Mondays I do this, on Tuesdays this, this is what takes most of my time, this is what I have to do myself, this is what I'd love to automate. Then ask what it can help with, given what's connected. "That's how I got the ideas for a lot of these prompts."

### Architecture and open questions

**Overnight dreaming.** The routines set up during onboarding mean the brain improves itself overnight — it reads the conversations you had and updates its own context. His examples of what it learns: that he indexes on spend over ROAS, how he likes scripts written, what he wants from headlines, and that he prefers not to work off direct competitors' ad libraries.

**A question from chat: are Parker MCP conversations in Claude Code saved back into Parker's context?** Jimmy's answer, on the day: within Claude Code, yes — and with a shared GitHub setup, your teammates' conversations too. But **"Claude Code will not be able to see the internal conversations that you're having within the Parker web app today."** Alex added they were working on it, toward a shared brain the whole team can access, and called this the V1.

> **Superseded.** The Parker MCP now carries `search_chat_history`, which reads prior Parker threads across web and Slack, brand-scoped and multi-teammate, with an author name on web threads so you can tell which colleague said what. The gap Jimmy described was real on 2 July and is closed.

**Higgsfield and local assets — left unresolved on the call, and still unresolved here.** Alex's experience was that the Higgsfield MCP **couldn't pull assets from a local folder**, and that he'd been manually uploading through an upload box in Claude Code. Jimmy wasn't sure. Alex noted that his own Alex OS folder has a brand-assets folder that Claude does reference when building landing pages, so the limitation may be specific to Higgsfield rather than general. Nobody tested it live. **Treat as an open question, not a documented limitation.**

**Terminal versus the desktop app.** Someone asked whether the terminal is faster. Alex hadn't used the brain in the terminal. Jimmy confirmed the CLI works and is the better route if you want to parallelize heavily.

**The IDE.** Alex demoed part of the session inside an IDE and deliberately skipped explaining it as beyond the scope of the call.

### Community and logistics

- The **prompt list** from the session was to be circulated with the recording.
- A Slack channel, **"Parker Brain Private Beta,"** roughly **70 to 75 people** (`stated`), where Alex said he shares things that don't make it to Twitter or public channels.
- The team offered themselves directly for setup calls.
- **Teased, not committed:** a possible **eight-week Claude Code creative-strategy program**, free for existing customers. Jimmy framed it as "rumour on the street." This became the **free six-week course** announced on the 6 August call, starting 27 August 2026.
- Alex's stated reason for the course idea: "there's no content on how to use it as a creative strategist. So we're all just trying to figure it out."

### What has since changed

Everything in this list was in beta, unreleased, or absent on 2 July and had moved by the 6 August session. **The August file and the live product are the current authority.**

| Described here as | State by 2026-08-06 |
|---|---|
| Discovery tab — beta, slow to load, industry filter "coming" | Shipped, with the impression sort called the differentiator |
| Discover Brands — not pushed, Alex wanted a final pass | Shipped as affinity-brand discovery, scoring on audience, positioning and tone |
| Northbeam integration — in beta | `search_northbeam_attribution` is a live Parker MCP tool |
| Post-purchase surveys — beta for some brands | Live; two MCP tools, chained lookup → semantic |
| Claude Code can't see Parker web-app conversations | Closed — `search_chat_history` reads web and Slack threads |
| Reddit — not mentioned at all | Built and in limited testing as of 6 August |
| Eight-week program — "rumour on the street" | Announced: free six-week course, starts 27 August 2026 |

---

## What this session contributed

**Most of this session was already canon before it was logged.** The swipe file, affinity brands, impression-rank reads, the reporting and competitor-digest and static-generation prompts, Notion idea-library population, following brands from the chat, TikTok mining, routines on a schedule, dreaming, and the "correct it once and it stays corrected" pattern were all already in [`best-use-cases.md`](../best-use-cases.md) and the method docs — several of them promoted from the 2026-08-06 session five weeks later, where the same operator said them again more fully.

Checked and found already covered: AI tagging and the tag taxonomy (`prompts/_notion-ai-tagging-and-foundational-context.md`, which also carries a **stronger** rule on awareness tagging than Alex's live caveat — copy is the primary signal, and the tag is a posture, not a sequence of beats); impression rank as a proxy and its hard scope limit; the affinity-over-competitor preference; the Max-plan usage warning; the intake question set; Eugene Schwartz's five stages; judges as a quality gate.

**Five things genuinely weren't in the repo. That's the whole list.**

1. **Connect your own tools before the build, not after.** The build sequence had the Parker MCP connection as a Phase 0 gate and pushed the team's own tools — Notion, Slack, Drive — to `/get-started` *after* the build finished. Alex's reasoning is what makes it a real rule and not a preference: the build is the most token-intensive pass the brain ever runs, so a tool connected first gets read *into* the build, while one connected after has to be bolted onto a finished V0. → promoted to `system/parker-tools.md`, `prompts/onboarding-runner.md`, `.claude/skills/set-up-brain/SKILL.md`, and `best-use-cases.md`.

2. **The calibration heuristic for how much context to hand over.** Jimmy's onboarding-an-agency / training-a-new-strategist framing gives a person a concrete yardstick where the intake's open question previously just asked what's missing. → promoted alongside item 1.

3. **The workflow-audit prompt.** Describe your own week out loud — what you do, what eats the time, what you'd love automated — then ask what can be taken off your plate given what's connected. Nothing in the repo told a user to point Parker at their *own working process*; every use case pointed it at the brand's data. Alex named this as the source of most of his own prompts. → promoted to `best-use-cases.md`.

4. **The review-agent loop on generated output.** `best-use-cases.md` had judges scoring *ideas before generation*. Jimmy's pattern is the other half — a second agent critiquing *generated output* and regenerating against its own feedback. Different stage, different job. → promoted to `best-use-cases.md`.

5. **Two Parker MCP tools missing from the canonical inventory.** The session's two headline demos — the org swipe file and affinity-brand discovery — are backed by `search_swipe_file` and `brand_discovery`, neither of which appeared in `system/parker-tools.md`. Verified present in the live Parker MCP toolset on 2026-08-07. → added to the inventory.

**Deliberately not promoted:** the Fable 5 build recommendation (a point-in-time model call, not repeated on 6 August); the Higgsfield local-assets limitation (contested live, never tested, unresolved); the product roadmap items (custom tags, persona and angle auto-tagging, Instagram DM saving, country filtering); and everything superseded in the table above. No new watch entry was opened in `parker-taste/patterns-to-monitor/` — this session made no craft-method claim that isn't already canon.

---

## Full transcript (verbatim)

> Auto-transcribed from the live session. Speaker labels are not marked in the source. Alex hosts throughout, Jimmy co-hosts and takes the `/set-up-brain` demo and the review-agent segment, and Manish speaks briefly at the open.

What's up, everybody? Hope you're doing well. Let me just see if I can enable the chat. Give me a thumbs up in the chat or a hate in the chat, if you can hear.

I still don't know why I haven't fixed this in my Zoom settings, but for some reason, my Zoom account, it doesn't like it when... My chat just does not work all the time. So if you are tired of messaging in the chat, just make sure it's selected to everyone rather than just hosting panellists. So if any questions come up, people can see what is being asked.

But good to see everyone in there. Thank you. Good to see everyone in here.

And today we have a very fun one. I will give it a couple of minutes because we're a little early. We're going to be talking about a lot of new things that have launched.

A lot has happened over the last couple of weeks. The Parker Brain, what it is, how it can help you, how to set it up, and what the use cases are. I've been using it a lot over the last week or so.

And things get very fun. You can... I mean, the sky is literally the limit with this brain inside of a code. So I want to walk through that today.

For the majority of the session, we'll wait for other people to get on and then we can crack on into that. I'm going to be bringing Jimmy up when he joins. Hopefully he's going to be inside of here.

If you just joined, give us a thumbs up or a hey in the chat. Good to see everyone, super pumped to get into this. I'll give it like one more minute and then we can get started.

What's up, everyone? What's up? What's up? What's up? Okay. Okay. So no Jimmy yet.

So we can, I guess, get started. Before we do, Manish, anything that you would like to say? Yeah. Hey, everyone.

I think... am I on video as well? I need to allow you to... there you go. Cool. You should be able to turn it on now.

There we go. Nice. Good stuff.

Just wanted to say thank you, everyone, for being here and super excited to be building all of the stuff that we're doing on the Parker end with the evolution with the Parker brain and building that for you all with your feedback and for the benefit of everything that you guys are doing. So excited to see you all here. Make sure to ask questions in the chat.

I think the default is that it says to host and panellists. So if you could actually just like flip that back to everyone and then everyone can see the messages. It's not just a message to the host and the panellists.

So cool. Thanks, everyone. I do apologise.

I need to change that somewhere. Oh, yeah. The default.

Yeah. You'd think I'm more technical and able to sort that out, but I'm clearly not. Anyway, let's get cracking.

You know, it's a serious one today because we brought Jimmy on as well. Those of you who were in the course last year might remember us going back and forth with a bunch of these like rift sessions on creative strategy. Today's going to be something similar to that.

There's a lot of new things that I want to share from inside of the product. And we are going to spend the bulk of today's session talking about the Parker brain, what it is, how to instal it, what it can actually do for you, what you can connect to it. And ultimately, I'm just going to be sharing or Jimmy and I are going to be sharing how we've been using it so far and enabling you guys to begin to use it yourself.

Jimmy, before I share my screen and get this deck up, is there anything you want to preface this call with? No, I mean, I would just love as Alex is going through this, if anyone wants to just throw in the chat like where they are at with the brain creation setup process, if they've hit any snags or whatever, just let me know and I can kind of be monitoring that. To preface, we know that it is not a simple experience. There's a lot of work that that is to be done on our end to make it much more seamless for you guys to just be able to set up easily.

So I appreciate anyone that has gone through and tried to do it so far. Alex will have a lot of tips on how to do it well. But yeah, I'm happy to be over in the chat if people have any immediate questions as well.

Or I just love to hear if you've tried it, if you haven't tried it, all the different things. Awesome. Let's get started.

Then I'm going to share my screen. We can head right into it. This call is being recorded.

So if you want to send it to Teams after, then I'm sure a recording is going to be circulated because there's probably a lot that we're going to share. And there's a lot of prompts, a lot of workflows, use cases. So don't worry about taking notes or taking it all down.

You guys can see my screen? Perfect. Thank you. So I first want to talk about new features.

What is new inside the platform today? Because there's been a lot that's been pushed live since we last spoke. A few of the most notable ones being AI tagging. So now every ad in your ad account is AI tagged by five different variables.

And that allows you to do a bunch of reporting off the back end. You can do reporting and see which ad formats are spending the best in my account, which awareness levels, give me a distribution of my awareness levels for every ad in my account or every ad that we launched in the last 30 days. We've got that for your accounts and also for anything that's in the inspiration tab.

So all of the brands inside of here that you're following, every single one of their ads has been AI tagged for you. You do not have to do anything. It's just going to be AI tagged for you.

If you want to go and edit tags, you can edit tags on any ad. We have had a few requests recently for custom tags. Right now that is not available.

It is being discussed and it may well be able to be done at some point. We are already looking at auto tagging by persona and angle. That is on the roadmap, absolutely.

And then possibly the opportunity to add your own custom tags inside of here as well. I found this really useful to, like I said, do reporting, making visual reports inside of Parker, or actually more so in my case, doing it through Cloud Code in the brain, where I'm looking at, look at my competitors for the last 30 days and give me a breakdown on what kind of ad formats they're running in the new ads that they've launched. If you combine this with the sort by impressions, it gets really interesting because you can say, look at my competitor and their top 10 ads by impressions and see if there's any commonalities in the AI tags, like ad format, emotions, et cetera.

Alex, can you hover on the awareness level one? I think Brock in the comments had a question about it, about how it's tagged. Yeah. So the question, sorry, I don't have the chat up.

I didn't have the chat up. So yeah, it's based on Eugene's watch five stage of awareness. Yeah, that's correct.

So obviously you guys know that Parker watches every single one of your ads. So based on its analysis, it then dictates which of the five stages of awareness that it believes that ad to be. Now, it's not an exact science because there are some ads that you can't classify to one awareness level, but it's best to work out where roughly it believes the ad to be most applicable to of the five awareness levels.

So I found it to be pretty accurate overall. Okay. We also have a swipe file and the Chrome extension.

So a lot of you here, I'm assuming will be using some kind of swipe file tool. If you do now want to do that one side of Parker, you can save all of your ideas inside of here. Let me go to an account that does have a swipe file that's already being used.

I'm not going to show you anything revolutionary here. A lot of you will be familiar with a view like this, but you can create boards, you can create folders, you can share this as a team. All of your inspiration gets stored in one place.

What I really like about this is that, I mean, obviously I use Parker for all of our creative strategy internally. You can save ads and content from external places. You can also save it from the app.

So I spend a lot of time in the inspiration tab. And if I want to look at some of my competitors or some of my affinity brands, you can just one-click save. Under every single ad, you can just save to the swipe file.

Same thing with the TikTok tab, same thing with the performance tab. Anywhere you are in Parker, if you see an ad, there will be a safe swipe file button. So it just makes it really easy to build that swipe file without having to go and use different tools in your workflow and just have that one place for your whole team to be able to save them.

There is also a Chrome extension. I believe in the broadcast that was sent out in the Notion doc, there is a link to that. If there's not, then let's get it added, Tana.

That is going to allow you to save ads in Facebook ad library, Posts and Reels, Instagram, Pinterest, TikTok, and YouTube Shorts. Oh, you can also just go, yeah, new idea and instal the extension here. Or if you have the Facebook ad library and you can just paste it inside of here, decide which board you want to save it to and click save.

And that's going to save to your swipe file. Instagram DM is a great suggestion, Ben. We are working on that.

That is definitely something that I would love to have. So right now you can't DM ads to Parker and have them saved, but that's been requested by quite a few people. So I wouldn't be surprised to see that in there soon.

There's a few minor tabs on the performance, a few minor updates in the performance tab. I'm not going to spend too much time on that right now because there's a lot that I want to go through. I mean, there's a full debrief inside of your Slack channel that Tana's put.

You can now download assets as a GIF if you want to put them into, you know, retros or reports, which I think is pretty cool. And then live shareable reports, which is requested by a lot of you. And then finally, the Parker brand MCP, which you're going to go into in a moment.

Currently in beta and going to be with you soon, if it's not with you already, the Northbeam integration has been requested by a lot of you. So you're able to see Northbeam inside of your performance tab and have every query look at Northbeam data instead of, or as well as the actual ad account data. Post-purchase surveys integration, which a lot of you, I mean, I don't know if that's been made publicly available or if that's still in beta.

If it is still in beta, it'll be with you very soon because we have got brands using that already. That's just another data source. And finally, something that I'm very intrigued by is the discovery tab.

Now, TBD on whether this is going to be its own tab or whether it's going to be baked into inspiration. This is basically a hub to discover new ads that from any brand that is saved inside of Parker. So all of our customers have saved thousands of brands and we have aggregated them all into this one view where you can query them by any filters you want.

So for example, if I wanted to see AI animation ads, I can filter down to that and you have all of our AI tags here, which is pretty useful. This, because it's still in beta, does take a little bit of time to load, but basically this is going to allow me to find all ads by whatever AI tag I want, or by searching it or by looking for certain videos that are AI animations that are top by impressions. This is really interesting to me because when this loads, what it's going to do is it is going to show you AI animation ads, but it's going to be sorted by impressions.

So at the top here, there'll be a load of AI animation ads that are ranked near the top by impressions inside of their ad library. So you might see a bunch of ads that are top by impressions under this criteria. Again, I need to improve the speed here because this is taking a little bit too long for now, but here you go.

So these are all, you can see here, number one, number one, number one, number one. These are all AI animation ads that are ranked number one currently by impressions inside of their ad libraries. You can verify that by just looking on the ad performance trend here.

Again, here at Parkour, even though it's not a one-to-one correlation, we are pretty bullish on the idea of sorting by impressions in external ad libraries because there's a better correlation between that than any other metric, obviously besides the ones that are in your actual account, but obviously we can't see any of those. We can't see how much these ads have spent and what their metrics are, but we can see the rank by impressions, which this is a pretty cool thing if you want to look at different types of ads that you want to produce and find what are probably a good proxy for performing ads in that category. We're going to add more filters here soon, like industry ads, industry, for example, and other ones.

You can see what are some performing ads in the skincare niche or what are some performing authority figure ads in the health space. I found this tab really useful so far. Filter by country is an interesting suggestion.

Currently, no. I'd have to check with the team to see how easy that would be to implement, but language shouldn't be difficult at all. I'd have to check by country.

Then, something else on this page that I have also been using a lot recently is the Discover Brands tab. Now, again, this is still beta, so this hasn't been fleshed out. This isn't going to be the final version of it, but the concept is.

A lot of you have told us that you want to find brands that sell to the same audience or the same personas as you do, but are not direct competitors. What we've done is we've looked at every brand in our database that you guys have saved, again, thousands of brands and been able to look them up against each other. You can see for your brand, here are the brands that are not direct competitors of yours, but they have a similar tone, positioning, or angle to you.

You can see a comparison between them and you in all those different variables. You can go and see their ad library. You can follow them if you want.

This is really useful, again, because I find myself often in the position of, oh, I want to go and get some new inspiration. I don't want to copy my competitors because then you're just one step behind. You can get a lot of good ideas for winning angles, winning ideas from people who sell or brands you sell to a similar audience than you, but are not actually selling.

They're not direct competitors. I found this very useful to find new brands to follow. And then again, personally, if you are talking about recreating ads from other brands, I found this to be the best workflow.

Find brands that sell to similar audiences, but not competitors. See what's working for them by impressions, and then go and look at that for inspiration. That is way better than just looking in the Facebook ad library at a random brand.

Very excited for that. It's not too far away. It hasn't been pushed yet to users, but it will after the webinar.

Yeah, I didn't know it was that close. I still think I've got a final pass on this, so I don't think it's ready to go out yet, but it's almost there. The recommendations are good.

I'm happy with them from an Outpost perspective. And again, this will work inside the chat and inside of Crawlcode for the brain, too, when you are querying and saying, you know, find me some similar brands to my brand, but they're not selling the same product that we can use as inspo for ads and give me some suggestions off the bat for that. Very cool.

Exciting feature. That is close. Okay.

So, Parker Brain, what is it? How do you instal it? And what can it actually do? So, we're going to spend the next 45 minutes on this. There will be time for questions. I do, like, I know usually in these calls, we spend time just, like, I'm live prompting and doing strategy today.

I actually just want to show you a bunch of chats that I've been having, because I think with this kind of stuff, you're going to see how this all fits together. I think there's been a little bit of confusion, partially because I haven't put out much content on this since we tweeted it last week. Some people think this is, like, a separate product to what Parker offers, but I'm hoping by the end of today, you'll see that how it all fits together.

Like, all the different data sources and all the things that we've added into Parker and are adding into Parker over the last few months are what feed the brain, and it's what makes the outputs as good as they are. And really, it's just, like I said, it's a the reason I want to show you different chats I've had rather than doing chats live is you really are only bound by your own imagination. And I want to give you as many different use cases that I've had to allow you to go and either copy what I've done or think of use cases yourself, of which there will be, you know, a lot by the end of this call, because everyone's got their own workflows, everyone's got their own tools that they use, and it's going to be really interesting to see how you guys go and run with this.

So, what is the brain? Basically, what we have done is we are open sourcing a lot of the Parker knowledge to a brain that you can connect to your Cloud code so that inside of Cloud, you can do your strategy as if you were doing in Parker. I mean, the difference being, well, number one, it's in Cloud. Number two, you can connect to all of the other things that you can connect to in Cloud.

Here's like a really simple example of this, and I'm going to show you a bunch of chats soon, so don't worry if it doesn't make sense yet. A lot of people in these webinars have been saying, like, we want you to add production into Parker. We could have done that.

We could have spent a few weeks building that on the engineering side, or we could have, like, spent time working on this brain, where now you can connect, you can inside of Cloud code, you can just say, look at my competitor's ads by impressions, find me the top five static ads, and use the Pigsfield MCP to go and build these ads for me, and you can have that done inside of your Cloud. I'm going to show you examples of chats that I've been having and ideas to go and use this, but the idea is that we're giving, like, enabling you to go and connect to all of these different tools, whilst at the same time using the Parker brain and connecting to the Parker data sources on top of the knowledge that we have been compounding over the last year or so inside of the tool. I'm just curious, before I go into this, can everyone drop in the chat a number out of ten as to, like, how comfortable you feel inside of Cloud code? And, like, you know, obviously, no judgement there.

I literally am just curious to understand who's got on the call today. Ten being I use this every day, and I am super comfortable with it, and I do everything inside of Cloud code, naught being I've never used it before. Where would you lie on that scale? Okay.

We've got a few eights and nines, a few people in the middle. Okay. So, we've got a really nice mix of people here today.

Okay. So, let me go and share my Cloud code now. Oh, dear.

So many terms. Need to make sure I've got the right one. There we go.

So, the idea here, and, Jimmy, feel free to jump in at any point. The idea of Cloud code is that, like, instead of Cloud AI, like, the normal Cloud chat, where you are basically reliant on memory of Cloud or of chat GPT to ensure that it gets better over time. With Cloud code, you can work inside of folders that live on your laptop, whereby every time that you, like, give a piece of feedback or you do something differently, you can save it to this folder, so that, in theory, it gets, like, the whole folder gets smarter every time that you use it.

We'll go through a few examples in a moment. But, like, what I'm trying to encourage people to do, like, internally add with this brain, and hopefully for all of you guys, really, once you start using this, there should be no reason why you ever need to have a chat in Cloud chat again. Because the chat from Cloud chat does not compound like a chat in Cloud code does.

And there's not really anything you can do in the chat that you can't do or meaningful that you can't do inside of Cloud code. You have all the same connectors, all the same skills. I look at this as, like, you know, code work on steroids.

I haven't used code work in quite a bit since I've called the Cloud code bug. So, let's have a look of an actual true example. Oh, by the way, this is the example I was referring to, like, just a minute ago, where I said, look at my external brands, my impressions, and find ones that make the most sense for us to recreate, then draft a copy for us to recreate them.

And it literally went and did this via the park at MCP, and then it went and made, like, what I would consider to be static ads that are pretty much good to go, and I didn't even touch the copy. And it went and did, like, ten of those. I mean, some of them weren't that good.

But, like, I literally just spun them up in a few minutes. So, yeah. That's just kind of an idea of what you can do here.

First, I want to talk about how you go and set this up, because I know a lot of people in this call may not have set their Parker brain up. It's actually pretty simple. Now, what I would say, before you go and set this brain up, the brain itself is really powerful, but it gets even more powerful when you're able to connect all the tools that you already use in your current creative strategy workflow.

So, what you want to do is you want to go to customise up the top here. You want to go to connectors and just add in anything that you currently use to do strategy inside of here. So, you'll see here I have my Canva in here.

I have my Google Calendar in here, so I can see call transcripts. I have Higgs field in here, which is what I use for generation. I have the Parker MCP, obviously.

I have Slack in here. I have Gamma in here somewhere to make decks for retros. Basically, anything that you use, you'll want to have in here as a connector, because this is what's going to really bring this brain to life when it can go and tap into the things that you're already doing and pull that context into the brain.

And the reason I think doing that before you generate the brain is because if you do that, then when you go and generate the brain, which is the most token intensive part of this whole process, it can already pull in that information rather than adding in after when the kind of V0 of the brain has already been generated. So, that's the first thing. Go and connect everything that you currently do as a connector inside of Ford.

Then what we're going to do is we're going to go and grab the link from GitHub. Now, I'm sharing the tabs, so you didn't see me grab from GitHub, but I just went and got the link here. We're literally going to come in and say something along the lines of clone this repo and go and produce a Parker brain for my client X. Oh, sorry.

I forgot to mention the MCP. I'll go inside and say it. So, what this is like, the Parker brain already has context of what it needs to do to get itself set up.

But you just want to say like, hey, you've got access to the MCP. Go and produce a brain, a Parker brain for my client X. As you can see here, I've got a couple of examples. This is one of my clients.

It's called Open Farm Brain, Flakes Brain. They are like separate folders on my laptop and every time I want to do a chat inside of Claude, I will come into this group and I will chat inside of here. One thing I should have mentioned, this requires you to have the MCP, the Parker MCP installed.

If you don't have that installed, Tana, can we drop a link in the chat to the guide to set it up? Again, super simple. All you're going to have to do is go back to connectors where we were. You're going to have to add a custom connector.

Just call it Parker and then add the link that Tana is going to share. You can even find it in the Parker settings, or the link Tana's going to share. Just add that and then test it works and you should be good to go.

Yeah, so you're going to say client's repo, go and produce a Parker brain for my client X. I mean, if you are a single brand and you don't have any other organisations inside your Parker, you don't need to necessarily define for which client because Parker's going to look at your account and do it on that. If you are an agency or a multi-brand org, you're going to need to define which one you want it to go and make it for. If Parker's unsure, Claude via Parker is unsure, then it will ask you which account do you need to set this up for and you can go and confirm it and it'll go and get set up for you.

Is it just for Alex or other brand owners too? Am I missing something? No, you got asked to join a Discord community. Did I? Just, yeah. Oh, it's the message above Alex.

Oh, sorry, sorry. Yeah, you're good. Hey, one thing too, just so it's helpful.

We actually just released a new onboarding process as well. So once you do everything that Alex just talked about, Alex, I can share my screen and just like show them what this new process is going to look like because it's really, really helpful before you go and run the whole audit system. So like Alex said, and this is kind of our demo account, so I had to tell it delete the other one that's there, but you actually can use this backslash.

And once you say like clone this GitHub repo, that will be able to be there. So if you just go into, you know, set up this or set up Brain, it's going to know exactly what to do. It asked me a few questions again, just like, hey, do you actually want to delete this? I said yes.

As soon as that's done, it's actually going to go through some questions to get more context about you and your organisation. So in this case, it's asking what's the main business objective for AG1 right now. And let's just say, you know, they're launching a new 65 plus line.

We can say that's our biggest objective. And then what is the objective on paid social? So in general, what are you using Facebook for? We'll say, hey, new subscriber acquisition. And then do you have any North Star metrics? So it's going to go through a bunch of questions just to get as much context as possible at the very end.

And I won't go through all this. There's not a tonne of questions. I think there's probably around 10 that it's going to ask you.

But at the end, it's also going to say, hey, is there anything else that I need to know about your brand? And if you already have those connectors set up like Alex was talking about, like if you have Google Drive or Notion or Airtable or Slack or any other, you know, MCP that you have that you do your creative operations in, I would just like use WhisperFlow or voice dictation and be like, OK, I have our Notion MCP attached. That's where our database of all of our ideas lives and the status of the different assets live. And just give it as much context into everything that you guys do.

If you have a Google Sheet with all the ideas, whatever, as long as that as long as you already have it connected to Claude, you can give it as context before it goes and runs the whole audit, because what's going to happen is there's going to be like 80 to 100 prompts that spin up and essentially will run like a full audit on your brand, competitors, creative strategy, as well as transferring over all of our creative strategy knowledge. So the more information that you can give it right away, I like to say like assume that, you know, if you are if you are a brand and you're like onboarding an agency, think about everything that you would want that agency to know. And that's like the level of context.

Or if you're an agency, assume that you're training a new strategist onto an account, like tell it everything, tell it all the processes, the tools, the data sources that you use, and it will factor all of that into the build out of this audit. So it should hold your hand a little more than if you tried to set this up before, which is really helpful, because again, we just we just want it to be as easy as possible and have all the context that it needs to generate a really, really good result. So you should see something like this to even make the responses and outputs even better.

One thing that I want to caveat here, just to be up front, when you are generating these brains, I would recommend being on the Claude Max plan. And actually, I would recommend being on the 20X usage plan. What is going to happen when you generate this brain, is there are going to be a tonne of audits, prompts, schedules that are running in the background for you.

It will take a number of hours to set this brain up. And that is because this is going to go deeper context wise than anything else on the market. And it's going to learn your brand better than anything ever has before.

So if you do do it on the Claude Max 5X plan, you will, I mean, it will work. You'll just probably run into your five hour limit a couple of times to get there. So it is token intensive, but it's only token intensive the first time that you set it up.

Once you've got it set up, you know, it's a lot, a lot more manageable, you wouldn't have to have that plan. But if you're not, and if you do want this to be done in like one, one pass rather than having to hit the five hour, the token limit a couple of times, then I would recommend the 20X Max plan. Okey-doke.

So let's get back to that. By the way, if this is like new to people or anyone here is not familiar or thinks that they may struggle with the setup of this, please feel free to reach out to us. Team, make yourself available in the chat, please.

We are here to help you guys in any way that you can. I know that Jimmy has been sending out his candle link offering to set it up with people or go through any questions with people who are users of Parker. The same thing for someone else was sending out a candle link.

If there's any way whatsoever that we can help, we are down to help you guys get this set up for you. Because once you've got the initial brain set up, then that's when things really get fun. It just takes, like I said, it's easy.

It's not anything that anyone can't do, but like it just takes some time, a couple hours to get this first initial brain set up. Okey-doke. So once you've got it set up, then this is where it gets fun.

And this is where if you've got your tools connected, you can really start to take the different parts of Parker and connect it to all of the different tools that you have. So let's just look through a few examples and then maybe Jimmy and I can riff on like how you guys continue to use this and what it actually looks like to use it inside your brand. So I asked Claude to build me a creative report for my brand.

I know that a lot of people here probably do some form of reporting or retros. And maybe that's on you. Maybe that's on someone else in the team.

It does take a lot of time for anything like we are internally. It can be very time intensive to do this. So I just said, go and produce me a monthly creative report.

And it went and put together a slide deck. I actually then prompted and said, now build it with Gamma, because Gamma is actually what we use for a lot of our retros. So I wanted to do it inside of there instead.

And it built me a editable Gamma file, which I'll have to reshare to show you. OK, here we go. Built me this presentation.

And this was with zero prompting, by the way. I didn't give it any direction on what I want to see in here, what metrics, what I would need it to have recommendations wise. And it built this kind of retro.

I could easily have given it things that I needed included in here or a template that I wanted it to follow and had this done for me really easily. So I've already been enjoying producing some of these. Oh, sorry.

This is the actual slide deck version. Oh, there was a Gamma version. I had.

Here we go. It's pretty similar. The Gamma version.

A little bit prettier. I'm a fan of it. Again, with zero prompting.

And I could easily brush this up, turn it into a template. And I'm going to show you in a second how to put that on a schedule so that you don't have to do it. And it literally just gets delivered to your Slack every whenever you want it to be delivered in there.

I also got it to look at one of Open Farm's biggest competitors. So the farmer's dog is one of their big competitors. I got it to do analysis on their ad account.

Look at what's working for them. Again, looking at their top ads by impression and finding what is what's happening for them. And then juxtapose that versus like our customer and get it to give us some recommendations for here.

And again, like this was all done in one prompt. This was not me giving it any direction on exactly what I want to see in this report. I can get it to build stuff like this.

And I can then say deliver this to me inside of Slack every Monday morning or whatever that be. The way that I would do that, if I go back to core code now, the way that I would do that is I just say, I want this delivered to me as a routine every Monday at 9 a.m. If you're over indexing on let's say ROAS too heavily here, I want you to focus more on spend as a primary metric inside the ad account. So I'm sending out the routine.

And then like what I'm doing here, and this is where the kind of file system comes into play, is I'm giving it feedback. And you want to do this as much as you can. Because what you do when you give this feedback is you update the kind of context so that the next time you use it, it gets smarter and it learns how you interact and how you work as a creative strategist.

I probably should have said update the context to reflect this and we'll see if it does that or not. So you can set up routines here. As you can see inside of this, I mean, there wasn't one prompt I had.

I set up another one that looked at competitors and did exactly that. And I actually got this to send it to Slack for me as well. Yeah, one thing on routines too, you don't actually have to build it within the routines tab.

You can just use natural language within the chat. Say like, hey, I love this presentation. Can you set this up to generate every Monday at 8 a.m. and send it to Slack? And it will do it for you.

So don't worry about having to go into routines and manually try to figure it out. Yeah. And again, that's why you want to have all your connectors added in here.

Because it just makes it so easy for Claude to put everything together and really get integrated inside of your workflow rather than just doing it all inside of one platform. I want to see if there's a, yeah, I mean, this was an example of me doing this. Check my main competitors ad libraries.

Look for ads in the last seven days. See if there's anything interesting. If there's something new that I need to know, send it to me in Slack as a digest.

It did that. As you can see, yeah, it sent a digest to our internal open form channel inside of Slack. And then I just said, well, I was actually prompting it to see if it can set up as a routine.

And then I said set it up as a routine. And it did that. And that was the routine that you guys just saw.

So now every Monday it sends that into my Slack channel. And that was just a template one. I'd make it a little better than it actually was.

But whether that's a gamma report or just a digest or a breakdown of what their ads are by AI tags, by emotion, just whatever you would want, you can get delivered to you really easily. And this is what I mean when we say the world is really your oyster. This stuff, you can connect any tool that you want to and have it be directly linked in with the Parker MCP.

Another example of this, and I'm going to show something that some of you guys might not have seen before. So don't take too much note of this if you're not familiar with what this is. This is what's called an IDE.

Basically it's just another way to display code. That's probably beyond the scope of today's webinar. But I was going through the brain and it was coming up with ideas for me for ads.

So then I said to it, now go and populate all of these ideas into our ideas library inside of Notion. And it went and did that. So Parker was dreaming overnight about all of the different conversations that we've had.

If you set up those routines in the onboarding, it will literally improve itself overnight. It will look at all the conversations you've had and it will update its context. So it knows, oh, actually Alex wants to index on spend more than ROAS.

And Alex has to write his scripts like this. And he likes headlines like this. And he prefers not looking at direct competitors ad library.

So it will update this context all the time so that it gets smarter and smarter. And as you can see here, this is literally our ideas library ad crate. All of these six ideas were populated by Claude via the Parker MCP and they're just straight into our workflow.

So whatever your current workflow is, whether you have a spreadsheet for ideas, whether you do it inside of a Google Doc, whether you do it inside of Notion like we do, it's filled out all of this. And again, I was just more so playing around with it to test it. But I could have done all the prompting inside of Claude code to say this is what I like.

I like this idea, this idea, this idea. Take this part of this idea and put it into Notion. Or populate this every Monday morning with 10 fresh ideas by looking at our competitors or our inspiration brands and seeing what we've done.

So it really all does link into one place. The stuff that you do on the web app feeds the stuff inside of the IDE and vice versa. And you can also use natural language to prompt things inside of here.

So I don't know if I can find the chat because I've got a lot of chats ongoing here at the moment. This is not the one, but I'll just tell you guys anyway. I was doing a competitor analysis earlier inside of here and it surfaced a new competitor and it said this brand is not saved into your Parker, but I thought that would be a good comp.

So I said, follow this inside of Parker. And then I went inside of Parker and it was followed inside of there. So it's not like they're two separate things.

The stuff that you do inside of here can talk to the stuff inside the web app and vice versa. So just bear in mind that you can just with natural language go and do things inside of the Parker web app from your Parker brain for the brand that you've got it set up for. What have we got in the chat here? Conversations with Parker MCP by Claude Code saved to the Parker context too.

Is that not what Dreamy is, Jimmy? Not in the, I mean, in these conversations, yes. So if you're talking within Claude Code, it can look at all of that. Or again, if you have like the shared GitHub setup, then it can look at all your team members conversations.

But yeah, technically Claude Code will not be able to see the internal conversations that you're having within the Parker web app today. Yeah. Got it.

Got it. Got it. Yeah.

Thank you for clearing up. And as Manish said, we are working through that right now. So it is more like a shared brain that all of your team can access.

But this is the V1. The exciting thing with this is that there are so many more, like it's so much more intelligence that's going to be added over the next few weeks. This is an early version of the brain and it's only going to get stronger.

There's only going to be more things that you can do with that as we go on. Let's have another look at some more use cases here. By the way, all the prompts that I've shared today, I've put together in a doc I'm going to send out or ask Tanner to send out either today or tomorrow when the recording of the webinar goes out.

So don't worry about taking them down. And honestly, what you can do and what I would genuinely advise you doing, especially if you're new to code is when you get everything set up, just whisper flow or voice dictate for like 10 minutes and say, this is everything that I do. Like this is how I spend my week currently on Mondays.

I do this on Tuesday. I do this. This is what takes the most of my time.

This is what I absolutely have to be doing. I have to be writing scripts. I have to be doing overall strategy.

I would love to be able to automate my reporting. I would love to automate my iteration suggestions and just tell the brain or code, this is what I do currently. How can you help me? This is like looking at the tools that you've got connected to you.

And I bet it will give you some suggestions of things that it could go and automate or like help you streamline significantly. Because that's how I got the ideas for a lot of these prompts. Originally, I was just asking it like, this is what I've got.

This is what you've got access to. How can you help me? So yeah, sometimes the Higgs field MCP is a little bit, a little bit weird, but I've been doing this, using this for a lot of static generations. I think there's another chat here I've used for this.

Oh yeah. So I just said, search through my brands, customer reviews, Facebook ad comments, et cetera. Look for emotionally loaded problems that we solve.

I'm sorry, emotionally loaded, like customer sentiment, cluster them. And then we're going to take those and turn them into static ads. And again, this is without like any intervention from me.

It went and generated these. Again, I'm gonna have to share to show a couple of these, but I would consider these pretty much good to go inside the ad account. I don't have any more.

Yeah. Okay. Copy's not great on that, but yeah.

I mean, this is actually one prompt. And again, I could easily have said, I want you every Monday morning to go through my affinity brands I've saved on Parker, find their top angles or find their top static ads by impressions or whatever you want to search for. And then I want you to go and turn this into like, use my voice of customer, my ad comments and my reviews, turn this into static ads for me.

I want you to deliver me the static ads via that using the Hicksfield MCP into a messaging Slack every Monday. I mean, I haven't tried that, but I imagine it would work. And it literally get them delivered every Monday for me to approve and then launch this on my ad account.

Yeah. And one other cool thing too, is again, like, I hope you guys know, all we wanted to do was provide the foundation for this. So you guys can go and add whatever you want.

So like, for example, you could say also, I want you to also set up a separate review agent. That's going to look through all of the ads that are generated and essentially give feedback on how to make the copy better and then regenerate the ad with that feedback in mind. So truly like, we are just trying to provide you guys the foundation of everything that you need, but just get creative and like, oh, if they're not great in one shot, try adding in an AI review agent and see how much better the outputs can get.

And like, that's what we would love to brainstorm with you guys on is just if you guys need help, again, learning how to do this or setting it up or getting creative and how you could use AI more, especially with like the foundation. We want to help because like the ideas are endless. It's what Alex and I have been talking about.

And it's like, we really did just allow you as a creative strategist to like be completely unlocked with being able to use AI. So yeah, just please use this as a resource is the TLDR. Yeah, absolutely.

You can still use the MCP in the same way that you would use it in the app as well. So for example, I was just saying, you know, search TikTok for the top performing videos in my brands category for the last 90 days. And it found me a bunch of TikToks that I could recreate somewhere in here as well.

Yeah. It gave me the script to go and recreate these. I actually thought this was a really good inspo for Open Farm.

I'm not sure if my screen or not showing the right screen to show you. It was a very cute dog. We got 10 million views.

That's a really good inspo for Open Farm. So yeah, the possibilities are endless. And like we said, we just want to the foundation for you guys to build on top of.

You're more than welcome to use just the Parker brain and don't layer any of your own content on top of it, but like go and fine tune it and make it specifically yours. You know, the way that you write scripts or the way that you do headlines or the way that you go through about iterations may be different to the way that I do it or way that the team do it or way that another agency may do it. So go and train it and give it feedback because it will get smarter every time that you use it.

And when that compounds, you really get something that is like hooked into some of the different places and knows you so well, they just make sure it creates a strategy a lot easier. And then when you learn that on top of routines and getting things delivered to you in Slack or an email or whatever, getting your retros delivered, updating your ideas library, like spreadsheets, whatever you've got in your current process, it makes it really, really powerful. So we just want to enable you guys to go and build some really cool stuff on here.

And we're going to keep doing these sessions. I'm actually thinking of making them more frequent again, just to like riff with you guys or make these drop ins. So I can just come here and answer any of your questions that you've got and help you guys set up some really cool things to create a strategy.

So, yeah, that is that's a quick whistle stop tour of the brain and what it can do. And remember, there's still a lot of docs being added to this over the next few weeks. It's only going to get stronger and stronger as we train it and then as you continue to train it.

So super, super excited. We have to chat in a second. One thing I will say, if anyone here is not, if you want to keep up with this stuff, there is a Slack channel called the Parker Brain Private Beta, I believe.

If you're not in there, just say hey in the chat right now and someone on the team will get you added. Or reach out to us directly. We'll get you added as a channel with like 70 or 75 people in there right now.

I'm going to be sharing some things in there that don't make it to Twitter and don't make it to public. So if you want to see some cool use cases that we're not sharing publicly, I'm going to share those in there too. So make sure you're in that channel.

But yeah, we just want to offer ourselves as a resource to you guys and allow people who want to build to go and build. And to reiterate, this is not separate to the original Parker product. This is just like they both help each other and hopefully you decide to see today how what we've done inside the web app and the data sources that have been added there is what feeds the brain and makes that that much stronger because you can't get the AI tagging on your ad account, the performance on your ad account, the competitor's ad libraries that are also AI tagged and all those other things.

That's what makes the brain's outputs that much more intelligent on top of all the creative jazzy context that it has. Tanner or Liam or someone from the team, let's make sure that we pick up on everyone in the chat who would love to be inside this channel. Jimmy, what have I missed? I think you did a pretty good job.

One thing too, Alex and I and the team are going to be coming out with a lot more educational content with deeper dives into all these different processes and skills and more insights into the brain over the coming weeks. So yeah, just stay tuned. If it's still not feeling super clear, again, no worries.

I'm telling you, we're going to do everything that we can to educate you guys and to become power users and really know how to unlock the full potential with what the foundation of this is. But yeah, I think that was pretty good. Awesome.

Any other questions, feel free to put them in the chat. Did we close the, do you use terminal, we find it faster? I actually haven't used the brain as a terminal yet. Is it possible? With the CLI, yeah, definitely.

If you want to like really paralyse things, you can definitely do it that way. Yeah. One other thing too, definitely use, if you have the credits and the capability, use Fable 5 to generate the brain.

Fable 5 is really impressive if you have not played around with it yet. So if you have not yet generated the brain, I recommend Fable 5, but again, just note, it will go through a lot of your credits and your tokens. So just be prepared for that.

But the output truly is amazing. Like you do just have a, really like the purpose of what we try to solve with the brain is we believe that if AI just has all the context that it needs, the reasoning ability of these models is there to be a, in this case, very strong creative strategist. So that was our goal with the Parker brain.

It's like, how can we just give it all the context that it would need, the data sources that it would need, the knowledge stocks that it would need, and then you guys providing all of your internal tribal knowledge and tools. And that's our bet on how we can actually get AI to not be AI slop within creative strategy in the future. So couple more questions.

Yeah. I actually am curious to get your guys' thoughts on this about the folder of assets. My understanding is that, I mean, at least if you're using the Higgs field MCP and someone else also asked like, do you need to use Higgs field MCP? No.

I mean, that's the one that I use because I think it's best for being able to choose different models, but there are, I'm sure are the ones you can use too. I thought that the Higgs field MCP couldn't pull assets from local folders to use it for generations. So what, I mean, I may be wrong here.

What's been happening for me when I've been doing this is the Higgs field MCP actually has like an upload box in cloud code that I was actually manually uploading the asset to. I don't know if I'm doing something wrong and maybe it works that way. But that's what I've come across so far.

Yeah. Funny enough, I forget. I was talking with someone yesterday about the same concept of like, can AI just go in and if there's like a Google drive full of, you know, photos or images, can it actually, can the MCP actually go in, download them, get an understanding or like use it as raw context? I don't know.

What's in most cases? Yes. Because like, I've got that in my, in my cloud, like in my like Alex OS, I've got like a brand assets folder. And like when I'm building landing pages, it can reference and pull in those assets.

So I don't, it's just whether the Higgs field MCP can, because unless it was, you know, lying earlier, it was telling me that I need to upload into the box. Maybe, I don't know, like maybe it can pull from a local folder. Maybe it can't.

Yeah. Okay. Yeah.

Yeah. Yeah. That's exactly what I do.

Like I, I've got a brand assets folder, so you should be good. Guys, how are we feeling about this? Like, is this exciting to people? Is this like confusing? Is it overwhelming? Are you like, just, I just want to get my hands on it and like, just start trying it out. I'm curious to get your guys' thoughts.

Yeah. And roast us because the internal team has been roasting us already on the process of getting it set up. So you are not alone if, if, if you're in that camp.

Oh yeah. We're about to start cooking. Let's go.

Yeah. I'm going to be sharing some things inside the side channel that I'm super excited about guys. It is, it is, it is like kind of overwhelming, especially if you're new, it's a cloud code.

One thing I will say, because yeah, I must admit, like, I, I would say that I was a little late to the cloud code train, but like, once you, once you start familiarising yourself and you, and you start using it yourself, like it becomes second nature and you have like a, like you'll have like a wow moment. Like, oh my goodness. Like every, like it's, there are just new levels to what's possible now.

And you know, now I'm like, why would anyone ever use cloud chat? Like when you've got cloud code. So, you know, I'd imagine that you'll get yourself familiarised pretty quickly and please do reach out to us. Like we're happy to set up calls to help walk you through, answer questions and like help you set up your organisations.

Rumour on the street is there could be a chance that Alex and I run back a creative strategy cloud code eight week programme. So nothing official yet. That's just been what I've been hearing on the street, but we'll, we'll keep you guys in the loop if anything materialises there.

You guys would obviously all get access for free. But yeah, would, would love to, because I've actually, I realised recently that like, it has become more and more apparent to me that all work is going to be done inside of that, whether it's core code, codex or whatever, it will like, will be done inside of some form of file structure like that. But there's no content on how to use it as a creative strategy.

So we're all just trying to figure it out. So we're going to keep on hammering away at this and just share with what, with you guys, what we learned along the way. And hopefully it will help everyone here get a lot more efficient and make a lot more money ads with it.

So it's super exciting stuff. Okay. Well guys, thank you so much for joining us today.

That was a really fun one. We're going to get the recording sent out. So if you want to circulate to your teams, you're more than welcome to also send out the prompt list as well.

So yeah, thank you for dropping in with us and we'll see you soon.
