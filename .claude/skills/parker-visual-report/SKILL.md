---
name: parker-visual-report
description: Generate a shareable visual ad-performance report (the Parker card-gallery format) for any brand connected to the Parker MCP — real embedded ad creative, performance stats, theme grouping, and key takeaways, published as a claude.ai Artifact. Use when the user asks for a visual report, ad roundup, weekly wire, or creative performance report for a brand.
---

# Parker visual report

Build a visual ad-performance report in the Parker report UI (KPI row → theme sections with horizontally scrolling ad cards → key-takeaway insight boxes), with the **actual ad creative embedded**, and publish it as an Artifact the user can open and share.

The finished report must match `template.html` in this skill folder — same classes, same structure. Do not redesign it. The template is the contract.

## Inputs to resolve first

1. **Brand.** Call `get_available_brands` on the **production Parker MCP** (server prefix `mcp__832d2199-0f4e-4ffc-909d-0a11dce8f18a__` — never the Parker Dev server `0518149e…`). If the user named the brand, match it; if ambiguous (same name in multiple orgs), ask. Lock the `brand_id`.
2. **Window.** Default `last_7d`. Accept any user-specified preset (`last_30d`, `last_90d`, custom dates).
3. **Scope.** Default: top 20 ads by period spend. Honor overrides (top N, active-only, video-only, etc.).

## Step 1 — Pull the data (two windows, always)

**Pull A — the report window.** One call to `search_facebook_ads_sql`:

- `brandId`, `dateRangePreset`, `metricsMode: "period_only"`, `groupBy: "ad"`, `sortBy: "period_spend"`, `sortOrder: "desc"`, `statusFilter: "all"`, `limit: 20`, **`includeTags: true`** (per-ad AI tags are what make the tag-economics section possible; ~30–80 tokens/ad, cheap).
- The default fields already include `text_hook` / `verbal_hook` / `visual_hook`, `angle`, `image_storage_url` / `video_storage_url`, `parkerWebUrl`, `media_hash`, `created_time`, per-ad period metrics, **and per-ad `custom_metrics`** (where new-customer purchase counts live when the brand tracks them). The response's `summary.period_summary` (totals + demographics), `lifetime_summary`, and `summary.tags_summary` feed the KPI row and takeaways — do not make extra calls for them.
- If the result exceeds the token cap it is saved to a file — parse it with `python3` (not jq; often unavailable). Never re-request with heavy include flags to "fix" this.

**Pull B — the prior window, same shape** (`startDate`/`endDate` for the immediately preceding equal period). Join on `facebook_ad_id` to compute per-ad **WoW spend trend** — this is what separates a high-riser from a fatiguing ad, and it is invisible in a single window. Also count churn: how many of this window's top 20 were absent from the prior top 20, and which prior top spenders fell out entirely.

**NC-CPA.** Look for a new-customer purchase event in each ad's `custom_metrics` (names like "New customer purchase"). If present, compute NC-CPA = spend / NC purchases per ad and treat it as the primary acquisition lens. `list_custom_metrics` shows every definition if unsure. If no NC event exists, say so — blended CPA is then the ceiling of what you can claim.

**Metric framing rule.** Check `aov` in the summary. If AOV is a placeholder (~$2, typical of newsletter/lead-gen brands where signups log as "purchases"), ROAS is meaningless — lead with **CPA (cost per signup)** and say so. For real e-commerce brands, ROAS, CPA, and NC-CPA all carry, with the standard last-click caveat.

**KPI target.** The verdicts grade against a target. Ask the user once for the brand's target NC-CPA or ROAS; if unknown, grade against the **account's own lifetime baseline** (lifetime ROAS/CPA from the summary) and say plainly in the report that no formal target is on file.

## Step 2 — Analyze (the ad-account method)

This layer applies the Parker ad-account method (canonical docs: `creative-strategy-context/ad-account-analysis.md` and `selecting-ads-to-iterate-on.md` in any brand-brain repo — read them if one is on disk; the distilled rules below make the skill work standalone).

**The spend-first read.** Top spend = Meta's prediction of the most potent ad (the breakdown effect: the system allocates toward predicted efficiency, so allocation itself is information). Start every read there — then immediately run the KPI check, because Meta's vote and the acquisition economics can disagree, and when they do, that disagreement IS the finding.

**Classify every top ad by trend + run time, not by a single-window snapshot:**
- **Slow-burner** — long run time (months), steady or gently rising WoW spend, stable efficiency across windows. The account's real winners. Top iteration priority.
- **High-riser** — spend jumping fast WoW. Only a winner if efficiency holds while it scales; a spend spike with worsening NC-CPA is Meta exploring, not a proven ad. Watch one more window before iterating.
- **Fatigued** — spend falling hard WoW (Meta already pulled it). Don't iterate, don't "fix" — let it wind down.
- **Learning** — launched <3 days ago. Exempt from all verdicts; flag early signals only.
- **Promo caveat** — never mark a promo-flagged ad (discount/offer creative, `occasion_promotion` tag) as an iteration candidate; promos spike and die by design.
- **Review/kill** — meaningful spend (>~2% of the top-20 total) at near-zero purchases across both windows. But never recommend killing an at-scale ad for a *slightly* high CPA — the method tolerates variance at high spend.

**Benchmarks** (directional, from the method): hook rate ≥30% good, ≥50% elite; hold rate ≥12%; outbound CTR ≥1%. The small-spend-high-ROAS trap: a $300 ad at 1.5 beats a $30 ad at 5.0 — low-spend/high-ROAS ads sweep low-hanging fruit and dry out; never headline them as winners.

- **Tag economics (required).** Join each ad's per-ad `tags` (emotion / ad_format / awareness_level) to its spend, purchase value, and NC purchases, then compute per-tag: spend touching the tag, share of top-N spend, ROAS, and NC-CPA. This is the report's sharpest lens — *share is Meta's allocation; per-tag NC-CPA is what the allocation bought* — and it routinely surfaces the funding-vs-earning inversion (the most-funded format/emotion earning worst). Collapse tags that resolve to a single ad into one labeled row (e.g. "ASMR · POV — 1 ad") instead of repeating identical rows. Report tag **coverage** honestly: untagged spend (catalog/DPA feeds, fresh launches) gets its own row and a note, never silently dropped.
- **Theme grouping.** Group the ads into 2–5 creative themes by reading `angle`, hooks, and format — not by ad-name tokens. Themes should name a creative approach a strategist would recognize. Each theme gets a one-line title with its ad count + combined spend, and a 1–2 sentence `theme-desc` that carries a method read (trend, NC-CPA band, what's scaling vs. what's converting), not a restatement of the cards.
- **KPI row (4 cards).** Spend analyzed; ROAS or CPA with the prior-window and lifetime comparison; NC purchases + blended NC-CPA when available; and one distribution fact (top-20 churn, delivery skew, dominant angle). Pick what's most informative this window.
- **Verdict strip (required).** After the theme sections, a 3-column strip — **Iterate now / Watch / Review** — listing the specific ads with one-line reasons (trend + NC-CPA). This is the operational deliverable; a report without verdicts is a gallery.
- **Key takeaways (3–4 insight boxes).** These are the product. Strong candidates: the account-vs-its-own-baseline plateau or recovery; where Meta's allocation disagrees with NC economics; the cheapest acquisition unit nobody's scaling; churn/survival rate of new creative; a served-vs-depicted audience gap; concentration risk (one evergreen carrying the account). Every claim carries its number and window. No filler.

## Step 3 — Media pipeline (the part that makes it work)

The Artifact sandbox CSP blocks all external media (`auth.heyparker.ai`, supabase, everything except a few library CDNs). Remote `<img>`/`<video>` URLs render blank. The fix: **fetch the bytes at build time and inline as base64 `data:` URIs** — self-contained content always renders.

Work in a scratch dir (e.g. `/tmp/parker-media-<brand>/`):

1. **Dedupe by `media_hash`** — variants share creative; download each unique asset once.
2. **Static images:** `curl -s --max-time 20 "<image_storage_url>" -o name.jpg`. Verify non-zero size and `file` says JPEG.
3. **Videos — poster frame only, never embed the mp4:**
   `ffmpeg -y -hide_banner -nostats -loglevel error -ss 0.5 -i "<video_storage_url>" -frames:v 1 -vf "scale=320:-1" -q:v 4 name-poster.jpg`
   ffmpeg streams the remote URL and reads only the first ~0.5s — no full download. Run **one ffmpeg call per Bash invocation** with exactly these quiet flags; batching them in a shell loop has corrupted filenames via progress-output interference. Check exit code per file, verify all files exist with sane sizes before embedding.
4. **Size guard:** posters at 320px wide are ~15–55KB each — fine. If a static jpg exceeds ~300KB, downscale it the same way (`ffmpeg -i in.jpg -vf "scale=480:-1" -q:v 5 out.jpg`); a 160px card doesn't need a 686KB image. Keep the final HTML under ~3MB.
5. **Embed with python3**, replacing each card's placeholder `ad-media` div with
   `<img src="data:image/jpeg;base64,..." alt="..." loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block" />`
   inside the same `ad-media` / `ad-media tall` wrapper. Count placeholders before and after — the replace must hit exactly N and leave zero.

If an asset genuinely can't be fetched, leave that card's SVG placeholder (it's in the template) rather than breaking the page.

## Step 4 — Build the HTML

Copy `template.html` from this skill folder as the base and fill it:

- **Header:** eyebrow = "Performance report — <date range>", h1 = report title, sub = scope line ("Top N ads by 7-day spend, grouped by copy theme. Scroll each row to browse. Tap any card to open in Parker.").
- **Tag layer (required, right after the KPI row):** the "Where the money went — and what it earned" section from the template — three columns (By emotion / By format / By awareness), each tag a bar row: label, spend-share bar (accent fill, scaled to the category max), share %, and per-tag NC-CPA colored `sv-g/m/w`. Top 5–6 tags per category, an Untagged row when material, and the coverage note underneath.
- **Cards:** one per ad, in spend order within each theme. `rank-num` = overall spend rank + format. Status pill from `effective_status`. `hook-line` = the ad's hook or headline, verbatim, quoted, clamped. Stats, in order: **Spend**, **WoW** (signed %, or "new (date)" / "new to top 20"), **ROAS or CPA**, **NC-CPA** when available, **Hook** for videos. Whole card is an `<a>` to the ad's `parkerWebUrl` (target `_blank`).
- **Stat colors** (relative to this account's own distribution, not absolute dogma): green `sv-g` = clearly better than account average, amber `sv-m` = around average, red `sv-w` = clearly worse. Apply to NC-CPA (or CPA) and hook rate at minimum; big negative WoW gets `sv-w`.
- **Verdict strip:** the 3-column Iterate / Watch / Review block from the template (a `kpi-row` with 3 columns), placed between the last theme and Key takeaways. Column titles colored green/amber/red; each entry is bolded ad # + name fragment with a one-line reason.
- **CTA:** the card footer is the muted "See more ↗" text link (`see-more` class) — never a boxed button.
- **Light mode only, by design.** The template carries no dark-mode blocks — do not add `prefers-color-scheme` or `data-theme` styling. The report always renders on the white ground.
- **Brand bar (top of report):** a small flex row above the eyebrow — the brand's real favicon (20px, embedded as a data URI) + brand name + org name muted. Fetch the logo at build time: read the brand site's HTML for the `<link rel="icon">` href (Shopify brands serve it from their CDN; Google's s2 favicon service is often blocked — go to the site directly, with a browser UA) and embed the bytes. If no logo is fetchable, keep the names and omit the img. With the brand named in the bar, the h1 stays generic ("Weekly creative roundup") rather than repeating the brand.

## Step 5 — Publish

Write the file to the session scratchpad, publish with the `Artifact` tool (favicon 📰; keep it stable across redeploys). Re-publishing the same file path updates the same URL. In the closing message: the artifact link, one line on what's in it, and the takeaways in a sentence or two — don't re-narrate the page.

## Failure notes (learned the hard way)

- Remote media in artifacts silently renders blank — no error. Always inline; never ship remote `src` URLs and assume they worked.
- `search_facebook_ads_sql` may briefly disappear if the Parker MCP reconnects — retry ToolSearch; `search_northbeam_attribution` with `facebookAdId` is the fallback for single-ad lookups.
- bash 3.2 on macOS: no `declare -A`. Use a name↔file list or python3.
- The same ad concept often runs as multiple ad IDs (separate entities). Show them as separate cards but reuse the deduped media, and flag the fragmentation in a takeaway if spend is split across near-identical entities.
