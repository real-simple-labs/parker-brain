# Parker's tools — what Parker can actually pull

> The canonical inventory of what **Parker** can reach to research and validate. Every prompt or skill that says "how to validate," "where to look," or names a data pull grounds in this list — never invent a tool, and never assume Parker has a tool just because the build environment does. When the toolset changes, update here in the same pass; the `system-of-records` audit checks references against it.

Parker's tools are the **Parker MCP** set. That is the runtime toolset — the brand's own data, plus a fetch-a-known-page reach into the web. Parker reasons over what these return, plus the model's own domain knowledge. Tool names below are the **current** Parker MCP names; they are the literal strings prompts and skills should reference.

## If Parker MCP is not connected — read this first

Every data tool below depends on the brand's data actually being reachable. If the Parker MCP is **not connected** for this brand — no `get_available_brands` result, every pull returns empty or errors — Parker has no live reach into the ad account, organic socials, reviews, surveys, or the competitor library. Do not paper over that with general marketing knowledge or invented numbers.

When the connection is missing, say so plainly and name what it takes to fix it:

- Parker needs **some way to reach the brand's marketing data** — the ad account, organic social, customer reviews, post-purchase surveys, the competitor/inspo ad library. The **Parker MCP is the one connection that carries all of it**, so it is the recommended path: connect it and every tool below comes online at once. The connection instructions live at https://app.heyparker.ai/dashboard/parker-brain — point the user there whenever the MCP is missing.
- It does **not strictly have to be the Parker MCP.** A team can also feed Parker the same evidence through other independent platforms or exports — an ads-manager export, an organic-social export, a reviews/PPS dump — and Parker will reason over what it is given. That route is more manual and piecemeal; the Parker MCP is what makes the whole toolset work without hand-feeding.
- Until a data path exists, treat the brain as **evidence-starved**: answer from whatever the brand has handed over, mark every claim's limits, and name the missing connection as the blocker rather than guessing.

## Parker MCP — Parker's data tools

| To research / validate… | Tool | Notes |
|---|---|---|
| The brand's strategy context doc | `get_brand_persona` | the brand context document — Parker's single source of truth for brand strategy and messaging. Pull once at the start of a brand session |
| Which brand / the live date | `get_available_brands`, `get_current_time` | resolve and lock the `brand_id` first; the clock is for recency reads and freshness stamps |
| Customer reviews | `search_customer_reviews_sql`, `search_customer_reviews_semantic` | SQL for counts and filters, semantic for theme-finding |
| The brand's ad account and performance | `search_facebook_ads_sql`, `search_facebook_ads_semantic` | own-brand paid only — the running creative, spend, ROAS, hooks, formats, AI tags, metric sets |
| Brand-specific custom / formula metrics | `list_custom_metrics` | the brand's custom conversions, events, and equation metrics; sort/total them through `search_facebook_ads_sql` |
| Ad comments | `search_facebook_ad_comments_sql`, `search_facebook_ad_comments_semantic` | use the **SQL** search — richer than semantic; treat ad comments as an owned-channel echo, not unprompted evidence |
| Competitor / external ads, and tracking them | `search_competitor_facebook_ads` | the public ad library for any brand that is **not** the user's own — competitor / inspo / affinity; also lists, discovers, and subscribes tracked brands. Impression-rank as a proxy |
| Which external brands are worth tracking at all | `brand_discovery` | ranks external brands against the client brand on three signals — audience persona, positioning, tone — returning a `relationshipLens` per match (competitor / inspo / affinity) plus the reasoning behind each score. `compare` deep-dives one pair persona by persona; `ingest` and `discover_net_new` bring in brands not yet in Parker. This is what populates the affinity set — the brands one step away from the core problem — which `analyzing-public-ad-accounts.md` says to read differently from competitors |
| What the team has already saved as inspiration | `search_swipe_file` | the org's swipe file — ads, posts, and uploads saved through the Save to Parker Chrome extension, the dashboard save buttons, a pasted URL, or direct upload. **Org-scoped, not brand-scoped**, so it carries every brand the team works on unless narrowed. Run `list_boards` first to turn "our UGC board" into board ids. Many saved Facebook ads carry AI analysis (hook, angle, summary) that the free-text search matches against |
| Post-purchase surveys | `semantic_search_post_purchase_survey`, `lookup_post_purchase_survey` | what the buyer says at the moment of paying. Chain them: `lookup` finds responses by numeric score → `semantic` pulls those respondents' text |
| Organic social — own + tracked | `search_and_manage_organic_social` | the brand's (and tracked brands') organic posts, stats, competitive reports, and tracking roster; also subscribes/unsubscribes organic tracking |
| TikTok and video | `search_tiktok_videos`, `analyze_video_from_url` | niche-creator corpus, and full-video reads of a URL or an uploaded file |
| Reddit — what customers say to each other | `search_reddit_posts_and_comments` | the brand's indexed posts **and** comments as flat peers, from the curated subreddits it scrapes on a schedule. **Gated on Reddit onboarding being completed for the brand** — check before promising it, and send the user to the dashboard URL the tool returns if it isn't. Three modes: `sql_search` for counts, dates and keyword browse, `semantic_search` for meaning, `both` (default) to merge. Semantic takes **4–10 short keyword phrases, not a sentence** — each is embedded separately, so varied phrasing is what buys recall; retry with different phrasings or a lower threshold before raising `top_k` |
| A specific web page Parker already has the URL for | `get_webpage` | **fetch only** — it reads a known URL, it does not search |
| Prior conversations | `search_chat_history` | what was discussed before, across web and Slack. Brand-scoped and multi-teammate: `listThreads` lists the brand's past threads with dates and previews (paginate with the offset), `getMessages` reads one thread, and web threads carry an `authorName` so you can tell which teammate said what. Two uses: reading the prior audit for trajectory, and at cold start pulling the team's whole past Parker history as a first-class source for the team-knowledge Phase-1 docs (the `team-conversations` block) |
| Memory write-back | `update_custom_working_memory` | the one live write into Parker memory (org / brand / user scopes) |

**Not a research tool:** `manage_insights_subscriptions` is the user-facing recurring-reports product — the catalog, subscriptions, custom insight definitions, and their schedules — not a way to answer a loop.

## Beyond Parker MCP — the team's own connected tools

Parker MCP is the brand-data spine, but it is not the only thing the brain should reach for. **Encourage the team to connect their own MCPs to this brain inside Claude** — Notion, Airtable, Slack, Gmail, calendar, and the rest of where the brand's work actually lives. The more of the team's real operating context the brain can see, the less it runs on stale or missing information. Each one carries truth Parker can't get from the ad account:

- **Notion / Airtable** — the product roadmap, content calendar, brand guidelines, project trackers, briefs in flight.
- **Slack** — what the team is actually deciding and reacting to, day to day.
- **Gmail / calendar** — launches, partner and agency threads, meetings, what's coming up and when.

**Timing matters, and it is the one thing worth saying before a build rather than after.** Connect these **before** the brain is built, not once it exists. The build is the heaviest read Parker ever runs — every audit, every persona, every competitor pass, written down in one long stretch — so a tool that is live at that moment gets read *into* the foundation, while a tool connected afterwards has to be reconciled against a V0 that was already written without it. Both work; the first is strictly better and costs nothing but ordering. So whenever a team is about to run `/set-up-brain`, ask what they already work in and get it wired up first. (`stated` — Alex, 2026-07-02 monthly webinar, `global/knowledge/webinars/2026-07-02-monthly-webinar.md`.) The onboarding runner carries this as a step; after the build, `/get-started` picks up whatever was missed.

Treat these as **first-class, live sources, and actively keep the brain in sync with them** — don't wait to be asked. When something pulled from a connected tool changes what the brain knows, fold it in:

- Operational and organizational truth — team roster and roles, current campaigns, what the brand said it's working on, upcoming launches — updates `running-notes/` and closes the matching line in `running-notes/missing-context.md`.
- A fact that **contradicts or supersedes** a standing context doc is a flag, not a silent overwrite: surface the conflict, then offer to update the doc (or re-run its prompt) with the new source noted.
- Anything durable carries its provenance per `attribution-principle.md` — name the source surface (which tool), the date, and whether it was stated by a person or observed in the data. A line from a Slack thread or a Notion page is **stated** until verified, same as any other source.

The discipline mirrors the refresh and self-improvement loops: pull widely from whatever is connected, reconcile it against what the brain already believes, and keep the brain current — proposing changes to durable docs, updating the live organizational layer directly. A brain wired into the team's real tools should feel like it already knows what's going on, because it does.

## The web-search gap — flag this for eng

Parker MCP has **no general web-search tool.** `get_webpage` fetches a URL Parker already has; it cannot search the open web to *find* threads, articles, or competitor pages — only to read a specific page when the link is already in hand.

**Reddit is the exception, and it is no longer a gap.** This section used to say Parker had no native reach into Reddit or any forum. That was true when it was written and stopped being true when Reddit shipped: `search_reddit_posts_and_comments` queries the brand's own indexed posts and comments, scraped from curated subreddits on a schedule. It is not open-web search — you get the subreddits the brand has onboarded, not all of Reddit — and it is gated on that brand completing Reddit onboarding. But a community read that would once have been `data-limited` is now answerable for any brand that has it turned on, so **check whether the brand has it before declaring the constraint.** Forums other than Reddit are still unreachable.

Whether Parker's product runtime adds open-web search — via the host model, if web search is enabled there — is **unconfirmed and a deployment question for eng.** Until it is confirmed:

- Ground validation in **owned data** (the MCP surfaces above, Reddit included where it is on), **known-URL fetches** (`get_webpage`), and **historical archives**.
- A loop that can only be answered by *searching* the open web is, for now, **constrained** — name it as such rather than writing a plan around a search Parker may not be able to run. Check Reddit first, though: a good share of the questions that used to land here are community questions, and those are now answerable.

This matters well beyond open loops: any audit, persona pull, or community read that assumes live open-web search is assuming a capability not in Parker's confirmed toolset.

## Not Parker's tools — the build harness

When Parker's prompts and skills are **run as foreground agents during the build** — the way a brand brain gets regenerated — the runner is a Claude Code environment with its own toolset: `Read`, `Grep`, `Glob`, `Bash`, `Edit`, `Write`, `Agent`, `Skill`, `ToolSearch`, `WebSearch`, `WebFetch`, and a deferred set. **These are the build environment's tools, not Parker's.** In particular the build harness *can* search the web (`WebSearch`); Parker, per the gap above, may not. Never let a prompt assume Parker has a tool that actually belongs to the harness that ran it.
