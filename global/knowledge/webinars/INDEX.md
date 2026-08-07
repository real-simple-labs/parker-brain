---
doc: webinars-index
team: global
last_updated: 2026-08-07
purpose: The catalog of Parker's monthly customer webinars. Each entry says what that session covered so Parker can decide whether to open the full transcript, and every transcript is stored verbatim so a user can ask what was said, what was announced, or what was demoed on any given call.
provenance: Started 2026-08-07 with the 2026-08-06 session, at Alex's request, as the standing home for webinar transcripts going forward. The 2026-07-02 session was backfilled the same day; it is older than the seed entry, so its product state is historical and its file carries a supersession note.
---

# Parker monthly webinars

This folder holds the transcripts of Parker's monthly customer webinars. They're first-party product sessions — Alex and the Parker team walking customers through what's new in the app, how the MCP and the brain get used day to day, and answering live questions.

They live in the product brain for one reason: **people should be able to ask Parker what was said on a webinar and get a real answer.** What shipped, what's coming, how someone demoed a workflow, what was said in response to a question. That's not something the method docs carry.

## What's here, and what isn't

- **Here:** Parker's own webinars — public-facing sessions delivered to customers. Speaker names for the hosts, attendee first names as they appear in the live Q&A, and the client and brand names the hosts mention themselves on the call.
- **Not here:** private brand outputs, account data, spend figures, or anything a client shared in confidence. Where a demo showed real numbers on screen, the transcript says so without the numbers.

## How to use these

Read the **What this session covered** digest at the top of any transcript first — it's dense on purpose, so most questions get answered without loading the whole thing. Drop into the verbatim transcript when the question is about exact wording, a specific answer to a specific person, or a detail the digest compressed.

Anything in a webinar that turns out to be a durable, generalized use case gets folded into [`global/knowledge/best-use-cases.md`](../best-use-cases.md), which is where Parker answers "how should I be using you?" The transcript stays as the receipt.

**Two standing cautions when reading these:**

1. **Product state has a date on it.** A feature described as "coming very shortly" or "in limited testing" was that on the day of the call, not today. Check the current state before telling a user something exists.
2. **The hosts' figures are `stated`.** Impression counts, database sizes, and time-saved comparisons are said live from memory. Carry them as claims from the call, not as verified product specs.

## Sessions

Newest first. Product state in an older session is historical — where two sessions disagree about what exists, the newer one wins.

| Date | Session | What it covered |
|---|---|---|
| 2026-08-06 | [Monthly webinar](2026-08-06-monthly-webinar.md) | The Discovery tab (every ad in Parker, filterable and sorted by impressions) and affinity-brand discovery. Reddit ingestion built into Parker, in limited testing. MCP use cases: building swipe files and full ad briefs off the discovery database, emotional trigger-event animation ads, one-prompt cross-client analysis for agencies. Making the brain your own: fine-tuning a scriptwriting skill on 300+ of your own Notion scripts, the CLAUDE.md override so fine-tuned skills beat the Parker system defaults, and feeding YouTube transcripts and tweets into the brain. Jimmy on building a daily hypothesis-tracker routine, extending the brain past creative strategy, plan mode, and Claude Code browser control (Claude sees the ad library you're scrolling and recreates from it). Closing: Alex's in-progress static skill that produced 230 image ads, Jimmy's plain statement of the audit → four-bucket strategy → ideation architecture, and a free six-week Claude Code / Codex course starting 27 Aug 2026 that pauses these webinars while it runs. |
| 2026-07-02 | [Monthly webinar](2026-07-02-monthly-webinar.md) | **Product state here is superseded by the 2026-08-06 session — check that file first.** The session where the Parker brain was first walked through end to end for customers. App releases: AI tagging across every ad on five variables (awareness level via Eugene Schwartz's five stages, asked by Brock), the swipe file and Chrome extension, GIF asset download, live shareable reports, Northbeam and post-purchase surveys in beta, and the Discovery and Discover Brands betas. Then the brain: what it is and why it isn't a separate product from the app, and the setup sequence — **connect your own tools before the build**, install the Parker MCP, clone and ask, or run Jimmy's newly-released `/set-up-brain` intake (~10 questions, "tell it what you'd tell an agency you just hired"), then 80–100 prompts and a few hours on a Max 20x plan. Real Claude Code sessions: a monthly creative report into Gamma with zero prompting, competitor analysis against The Farmer's Dog, a competitor digest into Slack turned into a Monday routine, statics from external winners and from clustered customer sentiment, six ad ideas written into AdCrate's Notion library, following a brand into Parker from the chat, and TikTok mining. Jimmy adds the review-agent loop; Alex's headline tip is to dictate your own week and ask what can be automated. Open and unresolved: whether the Higgsfield MCP can read a local assets folder. |

## Adding a new one

1. Save it as `YYYY-MM-DD-monthly-webinar.md` in this folder.
2. Give it the frontmatter block the 2026-08-06 file uses — `doc`, `team`, `date`, `last_updated`, `purpose`, `provenance`, `summary`, `source_type`, `speakers`, `transcript_status`.
3. Write the **What this session covered** digest above the verbatim transcript. Be specific: name the features, the prompts, the numbers, and who asked what. A vague digest means the transcript never gets opened at the right moment.
4. Add a row to the table above.
5. Pull any durable use case into `global/knowledge/best-use-cases.md` and note there that it came from this session.
