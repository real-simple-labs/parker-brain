---
name: collaborative-brief-artifact
description: Render a creative brief (a set of concepts) into a shareable, collaborative HTML artifact the whole team marks up together — comment on each concept, resolve comments, edit the text inline, and save it all back into the one file, no backend. This is the collaboration-and-presentation layer, not the brief-writing method. It takes concepts (handed to it, or assembled from the Parker account as an on-ramp) and lays them out as one self-contained file with the real source-ad creative embedded and linked back to Parker. Use when someone wants a brief the team can comment on and edit together, a collaborative or shareable brief, or a review doc for the weekly creative call. Do NOT use it to decide what the concepts should be — that is harvest-ideas, evaluate-ideas, iterations, and the briefs docs.
---

# Collaborative brief artifact

Render a creative brief into one self-contained HTML file that a team **collaborates on** — reads before the weekly call, comments on to pre-align, edits live during the call, then hands to the creative team. Comments, resolve, inline text-edit, and save-into-the-file all work with **no backend**. Send the file around; everyone who opens it sees the notes.

## What this skill is — and is not

**This skill IS the collaborative artifact.** Its value is the collaboration surface — per-concept comments, resolve, inline edit, save-into-the-file, share — plus the embedded, Parker-linked source creative. It turns a brief into a document a team can work on together and hand off.

**It is NOT how to decide the concepts.** The strategy — which winners to iterate, what net-new to test, the personas/motivators/angles — is authored by the brief-writing skills, and this skill does not replace them:
- `harvest-ideas` / `evaluate-ideas` — find and rank the ideas.
- `iterations` — what to hold fixed and vary on a winner.
- `briefs/` docs + `ideation-and-brainstorming.md` — the concept thinking itself.

**Route the content decision to those; this skill takes the resulting concepts and makes them collaborative.** If you're handed concepts (from those skills, a brief doc, or the user), render them straight in. If you're not, you *may* assemble a starter set from the account (Step 2) so the artifact isn't empty — but that assembly is the on-ramp, not the purpose. When the user's real ask is "what should we make," stop and route to the brief-writing skills; only come here to make an existing brief collaborative.

**Not to be confused with `parker-visual-report`** — that is a read-only weekly ad-performance report (metrics, verdicts, no editing). This one is an **editable, commentable** brief the team works on.

The finished file must match `template.html` in this skill folder — same classes, same structure, same collaboration scripts. The template's markup is the contract; do not redesign it. Only fill it.

## Inputs to resolve first

1. **Brand.** Call `get_available_brands` on the Parker MCP; match the brand the user named (ask if ambiguous). Lock the `brandId`.
2. **Window.** Default `last_30d`. Accept any preset.
3. **Scope & cohorts.** Default 6 concepts across two cohorts. The two cohorts in the template are **Freebie** (iterations on this window's proven winners, varied personas) and **Persona** (net-new dedicated to one focus persona). These labels come from the brand's own sprint structure — if the brand runs a different split, adapt the two `.cohort` sections and their headers, but keep the two-cohort shape unless told otherwise.

## Step 1 — Pull the evidence (live)

One `search_facebook_ads_sql` call: `brandId`, `dateRangePreset`, `metricsMode:"period_only"`, `groupBy:"ad"`, `sortBy:"period_spend"`, `sortOrder:"desc"`, `statusFilter:"all"`, `limit:8`, `includeTags:true`, `includeExtendedFields:true`. This returns, per ad: `parkerWebUrl`, `image_storage_url`/`video_storage_url`, `media_hash`, hooks (`text_hook`/`verbal_hook`/`visual_hook`), `angle`, `ad_type`, `effective_status`, per-ad tags, per-ad `custom_metrics`, and period metrics. Read `custom_metrics` for the **New Customer Purchase** cost (NC-CPA) — the primary acquisition lens.

For net-new concepts sourced from customer language, also pull reviews/comments (`search_customer_reviews_semantic`, `search_facebook_ad_comments_semantic`) so a card's insight can carry a verbatim signal. For a market signal, `search_competitor_facebook_ads` — but **never name a competitor in customer-facing creative** (internal source lines may reference "a category leader" generically).

Every number on a card comes from this pull, not memory.

## Step 2 — Get the concepts (provided, or assembled as an on-ramp)

**If concepts were handed to you** — from `evaluate-ideas`, a brief doc, or the user — render those as-is and skip to Step 3. That is the normal path: this skill presents and makes-collaborative a brief that already exists.

**Only if you must populate an empty brief**, assemble a starter set from the account — through the method, not from scratch — and tell the user it's a draft to refine, since deciding the concepts is really the job of the brief-writing skills:
- **Iterations** (Freebie cohort) — read `creative-strategy-context/selecting-ads-to-iterate-on.md` and `iterations.md`. For each proven winner, name the one lever (hook rate weak → hook rebuild; body proven → hold it) and write the concept as *what to hold fixed and what to vary*.
- **Net-new** (Persona cohort) — read `ideation-and-brainstorming.md` and `customer-review-mining-method.md`. Source each from a real review/comment/industry signal and a dedicated persona.
- **Ground it in the vault** — personas from `personas/personas-profile.md`; angles, motivators and prior ideas from `idea-bank/` and `briefs/`; voice and do/don'ts from `brand-lens.md`.

Each concept carries, verbatim into the card:
- **name** and **number** (sequential across the whole brief).
- **cohort** (Freebie / Persona → `co-freebie` / `co-persona`).
- **iteration type** — `Iteration` (class `iter`) or `Net New` (class `new`).
- **format** — `Video` (play icon) or `Static` (image icon).
- **persona / motivator / angle** (the triad).
- **source + insight** — the source *type* (Top Ad / Review / Comment / Industry signal) with its real metrics, and the **insight** it taps (bold the lever). This is "why this concept exists."
- **creative direction** — 2–4 plain sentences on what the concept is and how to execute it. This is what creative reads.

**Honor the brand hard rules in every card:** no competitor names in creative or concept copy, profanity censored, video concepts note the paid-actor disclosure in the direction, no health/medical claims.

## Step 3 — Media & logos

The file is opened in a normal browser (not the Artifact sandbox), so remote Parker media loads directly — no base64 needed. Dedupe by `media_hash`.
- **Static:** `<img class="mi" src="{image_storage_url}" alt="" loading="lazy">`.
- **Video:** `<video class="mv" src="{video_storage_url}#t=1.2" muted playsinline preload="metadata"></video><span class="play">&#9654;</span>` — the `#t=1.2` seeks past a black first frame; `pointer-events` is off in CSS so the click hits the link.
- Wrap **both** in `<a class="media" href="{parkerWebUrl}" target="_blank" rel="noopener" title="Open source ad in Parker">…<span class="open">Open in Parker &#8599;</span></a>`. The `.media` CSS carries a denim fallback so a card still reads if an asset fails.
- **Logos:** the Parker mark is already inlined in `template.html` — keep it. Fetch the brand's favicon (its site's `<link rel="icon">`; Shopify brands serve it from their CDN), inline it as a data URI, and drop it into `{{BRAND_LOGO}}`; put the brand name in `{{BRAND_NAME}}`.

## Step 4 — Assemble from template.html

Copy `template.html`. Fill it:
- **Header:** replace `{{BRAND_NAME}}` and `{{BRAND_LOGO}}`; the Parker mark, Edit / Share / Print / Save, and all collaboration scripts stay exactly as-is.
- **Eyebrow / title:** `{{SPRINT_LABEL}}` (e.g. "Creative Sprint · Week of Jul 14, 2026"), `{{DATE}}`.
- **Summary row:** concept count, format split, iteration/new split. Leave the `#openTotal` cell — the script fills it.
- **Concepts:** replace the two `<section class="cohort">` blocks (the worked example) with your concepts, using the **exact card markup** shown there. Critical: every editable text element needs `data-field="{id}-{field}"` (name, persona, mot, angle, insight, dir), and `data-concept` / `data-thread` must both equal the card's id (`c1`, `c2`, …) or comments won't attach.
- **Footer:** the sources/attribution line — window, attribution basis, "no competitor names, no health claims," paid-actor note.
- **State:** leave `#brief-state` as `{ "version": 1, "edits": {}, "comments": {} }`, or seed 1–2 short "Parker" observations to model the comment feature.

## Step 5 — Save & share

Write the file to `reports/concept-brief-{YYYY-MM-DD}.html` in the brand repo. Tell the user: open it (double-click), and **send the file** to the team — anyone can comment, resolve, and edit; **Save** writes their notes back into the file (in place on Chrome/Edge, or a downloaded copy elsewhere) to pass along. It also prints clean to PDF for the creative handoff.

## How the collaboration works (already built into template.html — don't rebuild)

- **Comment:** each card has a comment button + thread. First comment asks for a name once; it's remembered on that device for the session and tags every later comment. Comments resolve/reopen/delete. Authorship saves into the file so teammates see who said what; the name itself stays per-device (not baked into the shared copy).
- **Edit:** the header **Edit** toggles Parker's inline edit — every `data-field` becomes click-to-edit (gold outline), and each card gets a hover-× to drop a concept. Edits persist and save into the file.
- **Save:** serializes the current comments + edits back into `#brief-state` and writes the file, stripping runtime-injected nodes so re-opens never duplicate.
- **Share:** a modal with the file link and the "send this file" note.

## Honest limits (state them if asked)

- **No backend, so it's async, last-save-wins.** Two people editing the same copy offline then both saving → the second overwrites. Fits the pre-call → align → handoff flow; not live multiplayer.
- **Real Parker auth needs Parker to serve the page.** The name step is a lightweight identity, not a verified login. The template already has the hook: if a Parker-served page exposes the logged-in user (`window.__PARKER_USER__`), wiring it back to auto-attribute comments is a small change — a future native-artifact upgrade, not something a standalone file can verify.

## Sources this skill leans on

Parker MCP (ads, reviews, comments, competitor library) · `creative-strategy-context/`: `selecting-ads-to-iterate-on.md`, `iterations.md`, `ideation-and-brainstorming.md`, `customer-review-mining-method.md` · brand vault: `personas/personas-profile.md`, `idea-bank/`, `briefs/`, `brand-lens.md` · brand hard rules in `CLAUDE.md`.
