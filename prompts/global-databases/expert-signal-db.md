# Spec - expert signal database

This specifies the expert signal database, Parker's cross-brand memory for expert content that changes how Parker understands the market. Expert content includes uploaded videos from Jimmy, links Jimmy gives Parker from social posts, newsletters, podcasts, articles, and community commentary. The saved unit is not the content item. The saved unit is the signal Parker can use later.

Doc type: global database spec plus capture and curate prompts. Scope: expert content across every marketing team Parker serves. Cadence: capture is continuous when Jimmy provides content; curate is monthly for team-level synthesis and quarterly for durable method updates.

---

## Purpose

The expert signal database keeps Parker in the loop as the market changes. Parker should not depend only on brand audits and ad accounts. It needs a living view of what strong operators, creators, platform specialists, strategists, and category observers are noticing now.

Three jobs the database does:

1. **Capture market change while it is still early.** Expert content often notices a platform shift, creative tactic, buyer behavior, or category pressure before it appears in a brand's own account.

2. **Separate expert claim from Parker inference.** Parker must preserve what the expert said, what evidence the expert showed, and what Parker believes it means. Opinion never becomes fact just because it was saved.

3. **Route signals into the right layer.** A signal can stay global, feed a brand idea bank, update a team taste file, become a candidate for a prompt or knowledge doc update, or sit as an open question until repeated signals make it stronger.

4. **Propagate learning into context docs over time.** Expert signals should not live in a dead inbox. Every saved signal must name the context docs, skill docs, prompts, brand docs, idea banks, taste files, or pattern-monitoring files it may affect. A single source can create a context-update candidate immediately. Promotion into canonical context requires either repeated signals, Parker account evidence, or explicit user approval.

5. **Prefer living updates over net-new sprawl.** Do not create a new context doc, candidate, pattern, or idea-bank entry just because a new source arrived. First search the existing expert signals, context-update candidates, taste files, brand idea banks, and relevant context docs. If the new source strengthens an existing theme, update the existing surface. Create a new file only when the signal introduces a distinct reusable idea, a new source artifact that needs attribution, or a new routing lane that would be muddied by merging it into an older entry.

## Storage and access

The canonical spec lives here. For creative-strategy v1, runtime entries live under `creative-strategy-context/expert-insights/`, and reusable cross-brand creative patterns live under `creative-strategy-context/parker-taste/`. The file-backed version is the v1 staging layer and uses the same schema the MCP-backed database should enforce later. Future non-creative teams can use Parker's global team signal pools under `global/teams/[team]/expert-insights/` once those layers exist.

Jimmy provides expert content in v1. The first capture path is uploaded video analyzed through Gemini's video understanding API. Parker does not scrape a watchlist yet. When automation arrives, it should create candidate entries for review rather than silently promoting every source into memory.

Team-scoped signals default to the team folder that can act on them. Creative strategy signals go to `creative-strategy-context/expert-insights/`. Performance, organic social, search, influencer, brand PR comms, partnerships, and retention signals use their own team folders when those layers exist.

## Acquisition layer

V1 acquisition is upload-first.

Jimmy uploads a video file into Parker Vault at `expert-intake`. The app sends the file to Gemini with the Files API, asks Gemini to read both audio and visuals, and saves a reviewable expert signal draft into `creative-strategy-context/expert-insights/inbox/`. This is the default path for TikTok videos, social screen recordings, YouTube clips, downloaded videos, and any expert clip where platform scraping is unreliable.

Link scraping is not the default v1 path. If Jimmy gives a link without a file, Parker should ask for a video upload, screen recording, transcript, screenshots, or manual summary. Official APIs, Apify, oEmbed, and third-party providers can enrich later versions, but the durable v1 system is upload to Gemini first.

## Schema

Each entry carries these fields.

- **signal_id** - stable ID using capture date, source, and short slug.
- **date_captured** - when Parker saved the signal.
- **date_published** - when the source content was published, if visible.
- **source_url** - the link Jimmy provided or the durable source link Parker found.
- **parker_media_links** - every Parker media link, media file path, thumbnail path, video URL, post link, source URL, uploaded-file reference, screenshot path, transcript path, raw-artifact path, or media reference available for the expert source. Preserve each link or path exactly. If no Parker media links or media references were available for the entry, write `No Parker media links were available for this entry.`
- **capture_method** - gemini video upload, manual summary, screenshot, transcript, official API, Apify, oEmbed metadata, or other.
- **uploaded_file_name** - original file name when the signal came from an uploaded video.
- **gemini_model** - Gemini model used for the video read when applicable.
- **raw_artifact_path** - local path to the Gemini draft, transcript, screenshot set, or other raw capture artifact.
- **source_platform** - the platform or publication where the content appeared.
- **source_type** - post, thread, video, podcast, newsletter, article, comment, livestream, slide, report.
- **expert_name** - person or organization behind the signal.
- **expert_credential** - why this source has reason to know, written plainly and only when supported.
- **team_scope** - the Parker team that should own the signal first.
- **brand_scope** - global, category-specific, or one or more named brands.
- **signal_type** - market trend, platform shift, creative tactic, customer behavior shift, category movement, measurement shift, operating practice, counter-signal, language shift, proof pattern.
- **source_read** - a narrative summary of what the source says or shows. For visual sources, write a scene-level description that lets the reader picture the post or video without seeing it.
- **expert_claim** - the claim the expert makes, separated from Parker's interpretation.
- **evidence_basis** - what the expert uses to support the claim. Use short quotes only when they are necessary and compliant.
- **Parker_inference** - what Parker believes the signal means for marketing strategy.
- **why_it_matters** - the practical importance of the signal.
- **freshness** - current, emerging, recurring, aging, or stale.
- **confidence** - strong, mixed, thin, or unverified.
- **actionability** - store only, watch, route to brand, route to idea bank, route to team taste, route to prompt update candidate, route to knowledge update candidate.
- **context_targets** - file paths or Parker surfaces that may need to absorb the signal over time.
- **proposed_context_updates** - concrete candidate changes, each with target path, proposed change, evidence, confidence, and promotion condition.
- **propagation_status** - inbox only, candidate created, applied to context, rejected, superseded, or needs more evidence.
- **idea_bank_routes** - brand idea bank, global Parker taste idea bank, patterns-to-monitor, no idea-bank value, or needs brand decision.
- **related_signals** - linked signal IDs when a pattern repeats.
- **notes** - caveats, access limits, or follow-up context.

## Capture prompt

Run this whenever Jimmy gives Parker an uploaded expert video, an expert link, or expert content.

You are evaluating one expert content item for Parker's expert signal database. Your job is to decide whether there is a durable signal worth saving, then create the entry in the schema's shape.

First, use the strongest available capture. For v1 video sources, prefer the Gemini upload path. If the user provides only a link and no reliable capture exists, ask for a video upload, screen recording, transcript, screenshots, or manual summary. Do not pretend Parker can scrape platforms that block reliable access.

Second, read the source content closely. If the source is a video or visual post, reconstruct what the viewer sees and hears in order. Write it like you are telling someone what happened in the source after they missed it. Do not use a category label as a substitute for the scene.

Third, preserve the media handles. Fill `parker_media_links` with every Parker media link, media file path, thumbnail path, video URL, post link, source URL, uploaded-file reference, screenshot path, transcript path, raw-artifact path, or media reference that came with the source. Preserve the original link or path exactly. If none were available, write `No Parker media links were available for this entry.`

Fourth, tell the research story and carry the evidence picture. Treat the saved entry as context another LLM or strategist may read without reopening the source. It should show what was reviewed, how the source was captured, what claim or pattern emerged, what evidence the expert used, which details support Parker's inference, what was missing, and what uncertainty remains.

Fifth, separate the expert claim from Parker's inference. The expert claim is what the source actually says. Parker's inference is what the claim may mean for a brand, a team, a platform, or a creative system. Never merge the two.

Sixth, judge whether the signal deserves memory. Save it only when it teaches Parker something reusable: a market shift, a repeated tactic, a platform behavior, a category tension, a buyer behavior, a proof pattern, or a useful counter-signal. Do not save generic advice, unsupported hot takes, or content that only repeats what Parker already knows.

Seventh, route it. If the signal is broadly useful, save it to the right team expert-insights folder. If it has direct implications for a brand, create a pointer for that brand. If it contains a usable creative idea, route it to the active brand idea bank when the brand fit is clear. If the idea is reusable but not brand-specific, route it to the team's Parker taste idea bank or patterns-to-monitor. If it suggests a Parker system update, mark it as a candidate and do not update the system from one source alone.

Idea-bank routing is mandatory. Every expert source should answer: did this create or update a brand idea-bank entry, a global taste idea-bank entry, a pattern-to-monitor entry, or no idea-bank entry? Do not force method-only or measurement-only signals into an idea bank, but do record the no-idea-bank decision.

Eighth, propagate it. Add context targets and proposed context updates to the saved entry. If the signal is useful but not yet strong enough to rewrite canonical method, create a candidate under the relevant expert-insights context-update candidates area and, where useful, add it to patterns-to-monitor. For creative strategy, that area is `creative-strategy-context/expert-insights/context-update-candidates/`. If the user explicitly approves a context-doc update, or if curation finds repeated evidence, apply the update to the relevant context doc with the source signal cited.

Before creating any new candidate or pattern, check whether an existing one should be updated instead. Parker's knowledge should feel like living context, not a pile of disconnected notes.

Output the saved entry plus its context propagation status. If the source is too thin, output a rejection note with the reason.

## Curate prompt

Run monthly for each team and quarterly across the whole database.

You are curating Parker's expert signals. Your job is to turn individual saved signals into useful market awareness without overstating the evidence.

First, cluster repeated signals by team, category, platform, source type, and strategic implication. A cluster matters when multiple sources point to the same change or when one source is unusually specific and credible.

Second, mark stale signals. A signal becomes stale when the platform changed, the source claim no longer appears true, the tactic became saturated, or the signal has not appeared again after enough time to matter.

Third, promote only what has earned promotion. A promoted signal can update a team taste file, a brand landscape synthesis, a knowledge doc, or a prompt candidate. A single expert post can create a candidate. It should not rewrite Parker's method on its own.

Fourth, apply or reject context-update candidates. For each candidate, decide whether to apply it, keep watching, route it to a brand, reject it, or supersede it. Applied changes must cite the source signal. Rejected changes should keep the reason so Parker learns what not to overfit to.

Fifth, produce a short synthesis. Name what changed, what Parker should watch, what brands or teams are affected, and what should be tested or researched next.

## Usage hooks

- Brand profile and market research prompts can read team-relevant expert signal syntheses when they need current market awareness.
- Monthly audit prompts can read expert signals to identify emerging tactics and platform shifts.
- Brand idea banks can pull expert-sourced ideas when the content contains a usable creative or strategic pattern.
- Team taste files can promote repeated signals into Parker's working taste.
- Prompt and knowledge updates can use expert signals as evidence, but only after review through the Parker update process.

## Critical rules

1. The user provides expert content in v1. Video upload through Gemini is the default capture path.
2. Save the signal, not the whole content item.
3. Do not launder opinion into fact.
4. Preserve source attribution and source limits.
5. For videos and visual posts, use narrative reconstruction.
6. Route brand-specific creative ideas into the brand idea bank.
7. Do not update Parker's prompts, skills, or knowledge docs from one expert link without a review step.
8. Do not pretend Parker can scrape blocked platforms. Ask for an upload or user-provided capture when link access is incomplete.
9. Every saved signal must include context targets and a propagation status so Parker's learning can move into the right docs over time.
10. Do not default to net-new docs. Update existing context surfaces when the new source reinforces an existing lesson.
11. Every saved signal must include an idea-bank routing decision. Expert content should feed brand idea banks or global taste idea banks whenever it contains a reusable creative pattern.
