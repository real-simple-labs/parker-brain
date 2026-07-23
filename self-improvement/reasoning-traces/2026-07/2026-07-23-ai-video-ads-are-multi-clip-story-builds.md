# Trace — AI video ads are multi-clip story builds, studied from real ads, not defaulted to one generation

**Date:** 2026-07-23
**Surface:** ai-ad-generation skill (new `ai-video-ad-build` default process) + new canon doc `ai-video-ad-structure.md` + `veo3-video-prompting.md` pointer
**Signal type:** user correction, then four redirects during propose-then-execute

## What happened

Jimmy flagged that AI animation video prompts were defaulting to a single 8-second clip. The routing literally said "Default for video asks → video-single-shot." Across the session he redirected four times, each widening or sharpening the fix: (1) the first proposal was structure-only arithmetic — he asked whether Parker understood how to pick a good length for each clip; (2) "study the art of short form films + the combo of pacing and keeping attention like advertising" — the doctrine needed film craft, not just math; (3) "use the parker mcp to study all the other ai animation ads from a pacing perspective" with max results ~50 — evidence over general advice; (4) "why just gruns??? why not the global discovery feature? And really look at ads at multiple lengths - some from other brands are like 5-10 mins. Which is good. That is great storytelling." Plus draft edits: rename the process, don't paste the architecture list into the process (make the model open the canon doc), no product-entry percentage rule (teach when the handoff feels natural), lean output (they want the ad; generate it directly when Higgsfield is connected), and story-layer invention is the craft, not fabrication.

The study that resulted: 231 unique AI Animation creatives across 20 brands (six org scopes approximating global discovery, which timed out), 13 cut-by-cut video analyses from 0:10 to 2:58. Median 52s; over a third run past a minute; zero ship as one 8-second clip.

## The lesson

1. **A generation constraint is not a creative default.** The tool's cap (8 seconds) had silently become the ad's length across the canon, the router, and every process description. When a technical limit shows up as a deliverable shape, that is a bug in the doctrine, not a property of the format.
2. **Study the corpus before writing craft canon.** The first two proposals were plausible and wrong-by-thinness. The verified shot lists overturned specifics (the 50-60% product-entry "rule" died on contact with the 0:00 mascot ads and the 78% long-form entries) and surfaced doctrine no reasoning pass produced: the bottle episode, the scene-as-unit shift in long form, scheduled information reveals, caption churn as the second pacing layer.
3. **One brand's library is a case study, not a corpus.** The first pull looked like 75 ads but was 96% Grüns. Sweep wide across scopes before computing a distribution; say so when the global feature is unavailable and an approximation stood in.
4. **Long runtimes are a lane, not an anomaly.** Jimmy explicitly values 5-10 minute animated storytelling. The long lane has different DNA (VSL/infomercial arcs, named protagonists, advocate characters, reveal scheduling) — a doctrine that stops at 60 seconds miscovers a third of what runs.
5. **Percentages are not processes.** Where a corpus shows a numeric pattern, the canon teaches the *mechanism* (the handoff is a story event a trusted character performs once the problem is earned) and keeps the numbers as observations. Jimmy rejects rigid numeric rules for gray creative judgment — consistent with the no-forced-buckets principle.
6. **The deliverable is the ad.** Output contracts for creative generation stay lean: plan header, clips, edit notes. Receipts compress to a line. When a generation tool is connected, offer the finished clips, not just prompt text.
7. **Split the story layer from the fact layer.** For character-driven formats, invention is the engine (Disney-style). Anti-fabrication rules scope to facts: numbers, claims, prices, fake-real customers. Writing "never fabricate" without that split would have banned the format's core craft.

## How to apply

When a creative-format doctrine is being written or fixed: pull the real ads first (wide, multi-scope, multiple lengths, dedupe by creative), analyze a spread cut-by-cut, and only then write the canon — with observations labeled verified, mechanisms taught instead of thresholds, story invention explicitly licensed, fact integrity explicitly scoped, and the process file referencing the canon doc instead of inlining its lists.
