# Parker's tools — what Parker can actually pull

> The canonical inventory of what **Parker** can reach to research and validate. Every prompt or skill that says "how to validate," "where to look," or names a data pull grounds in this list — never invent a tool, and never assume Parker has a tool just because the build environment does. When the toolset changes, update here in the same pass; the `system-of-records` audit checks references against it.

Parker's tools are the **Parker MCP** set. That is the runtime toolset — the brand's own data, plus a fetch-a-known-page reach into the web. Parker reasons over what these return, plus the model's own domain knowledge. Tool names below are the **current** Parker MCP names; they are the literal strings prompts and skills should reference.

## If Parker MCP is not connected — read this first

Every data tool below depends on the brand's data actually being reachable. If the Parker MCP is **not connected** for this brand — no `get_available_brands` result, every pull returns empty or errors — Parker has no live reach into the ad account, organic socials, reviews, surveys, or the competitor library. Do not paper over that with general marketing knowledge or invented numbers.

When the connection is missing, say so plainly and name what it takes to fix it:

- Parker needs **some way to reach the brand's marketing data** — the ad account, organic social, customer reviews, post-purchase surveys, the competitor/inspo ad library. The **Parker MCP is the one connection that carries all of it**, so it is the recommended path: connect it and every tool below comes online at once.
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
| Post-purchase surveys | `semantic_search_post_purchase_survey`, `lookup_post_purchase_survey` | what the buyer says at the moment of paying. Chain them: `lookup` finds responses by numeric score → `semantic` pulls those respondents' text |
| Organic social — own + tracked | `search_and_manage_organic_social` | the brand's (and tracked brands') organic posts, stats, competitive reports, and tracking roster; also subscribes/unsubscribes organic tracking |
| TikTok and video | `search_tiktok_videos`, `analyze_video_from_url`, `analyze_uploaded_video` | niche-creator corpus, and full-video reads of a URL or an uploaded file |
| A specific web page Parker already has the URL for | `get_webpage` | **fetch only** — it reads a known URL, it does not search |
| Prior conversations | `search_chat_history` | what was discussed before, across web and Slack |
| Memory write-back | `update_custom_working_memory` | the one live write into Parker memory (org / brand / user scopes) |
| Render a report or chart in chat | `show_widget` (+ `visualize_read_me`, `validate_report_data`) | present an SVG/HTML report or visualization. Read-me first, then widget, then the data self-audit; never plot numbers a tool did not return |

**Not a research tool:** `manage_insights_subscriptions` is the user-facing recurring-reports product — the catalog, subscriptions, custom insight definitions, and their schedules — not a way to answer a loop.

## Beyond Parker MCP — the team's own connected tools

Parker MCP is the brand-data spine, but it is not the only thing the brain should reach for. **Encourage the team to connect their own MCPs to this brain inside Claude** — Notion, Airtable, Slack, Gmail, calendar, and the rest of where the brand's work actually lives. The more of the team's real operating context the brain can see, the less it runs on stale or missing information. Each one carries truth Parker can't get from the ad account:

- **Notion / Airtable** — the product roadmap, content calendar, brand guidelines, project trackers, briefs in flight.
- **Slack** — what the team is actually deciding and reacting to, day to day.
- **Gmail / calendar** — launches, partner and agency threads, meetings, what's coming up and when.

Treat these as **first-class, live sources, and actively keep the brain in sync with them** — don't wait to be asked. When something pulled from a connected tool changes what the brain knows, fold it in:

- Operational and organizational truth — team roster and roles, current campaigns, what the brand said it's working on, upcoming launches — updates `running-notes/` and closes the matching line in `running-notes/missing-context.md`.
- A fact that **contradicts or supersedes** a standing context doc is a flag, not a silent overwrite: surface the conflict, then offer to update the doc (or re-run its prompt) with the new source noted.
- Anything durable carries its provenance per `attribution-principle.md` — name the source surface (which tool), the date, and whether it was stated by a person or observed in the data. A line from a Slack thread or a Notion page is **stated** until verified, same as any other source.

The discipline mirrors the refresh and self-improvement loops: pull widely from whatever is connected, reconcile it against what the brain already believes, and keep the brain current — proposing changes to durable docs, updating the live organizational layer directly. A brain wired into the team's real tools should feel like it already knows what's going on, because it does.

## The web-search gap — flag this for eng

Parker MCP has **no general web-search tool.** `get_webpage` fetches a URL Parker already has; it cannot search the open web to *find* threads, forums, articles, or competitor pages. So Parker has **no native reach into Reddit or any forum** to discover conversation — only to read a specific page when the link is already in hand, plus any historical archive that has been pulled in (the PullPush Reddit archive, where it exists).

Whether Parker's product runtime adds open-web search — via the host model, if web search is enabled there — is **unconfirmed and a deployment question for eng.** Until it is confirmed:

- Ground validation in **owned data** (the MCP surfaces above), **known-URL fetches** (`get_webpage`), and **historical archives**.
- A loop that can only be answered by *searching* the open web is, for now, **constrained** — name it as such rather than writing a plan around a search Parker may not be able to run.

This matters well beyond open loops: any audit, persona pull, or community read that assumes live open-web search is assuming a capability not in Parker's confirmed toolset.

## Not Parker's tools — the build harness

When Parker's prompts and skills are **run as foreground agents during the build** — the way a brand brain gets regenerated — the runner is a Claude Code environment with its own toolset: `Read`, `Grep`, `Glob`, `Bash`, `Edit`, `Write`, `Agent`, `Skill`, `ToolSearch`, `WebSearch`, `WebFetch`, and a deferred set. **These are the build environment's tools, not Parker's.** In particular the build harness *can* search the web (`WebSearch`); Parker, per the gap above, may not. Never let a prompt assume Parker has a tool that actually belongs to the harness that ran it.
