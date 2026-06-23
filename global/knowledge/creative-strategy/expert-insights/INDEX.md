# Creative Strategy Expert Insights Index

This is the file-backed v1 home for knowledge-source intake in creative strategy. The runtime behavior lives in `skills/expert-signal-intake/SKILL.md`; the signal schema is `prompts/global-databases/expert-signal-db.md`.

## How this system works

Intake is **approval-gated and propose-first**. When Jimmy hands Parker a knowledge source, Parker studies it in full, decides which of Parker's four skill components should learn from it — context docs, knowledge docs, tool calls, or processes — and writes the **exact, verbatim change it would make** as a proposal in the review queue, surfacing the same plan to Jimmy. Parker does **not** modify the real surface until Jimmy approves. On approval Parker applies the proposed text exactly; on modify it applies Jimmy's version; on deny nothing is written.

The folders here hold provenance and the review queue, not Parker's working knowledge. Working knowledge lives in the context docs and knowledge docs themselves, because that is where Parker retrieves it; a knowledge change that only ever lives in this folder is one Parker will never call — which is exactly why an approved proposal gets applied to its real surface, then this folder gets out of the way.

Jimmy provides the source in v1. The default capture path for video is upload through Gemini in Parker Vault. Parker saves the provenance receipt (the one pre-approval write), proposes the verbatim change, and on approval applies it and routes any reusable creative idea to a swipe file.

## Current Status

- Created: 2026-06-03
- Automation status: manual upload and draft capture only
- Curate cadence: monthly
- MCP status: file-backed staging, MCP-ready schema

## Entry Locations

- `inbox/` - raw or partially processed user-provided expert videos, links, transcripts, screenshots, and summaries.
- `context-update-candidates/` - the review queue: one pointer per intake to the drafted change at its real surface, marked `[~]` pending Jimmy's review, plus true candidates that await corroboration before any draft is written.
- `[source-id]/source.md` - source profile once a source becomes recurring.
- `[source-id]/[YYYY-WW]/[content-id].md` - saved expert signals from recurring sources.
- `curation/` - monthly and quarterly synthesis passes.

## Active Signals

- [2026-06-19 - Emotional delivery and timing — valence/intensity + TEEP](inbox/2026-06-19-emotional-delivery-timing-teep.md) - **applied (Jimmy approved).** New knowledge doc `emotional-delivery-and-timing.md` defining the emotional-landing-state mechanism and the **TEEP** model (Trigger→Exploration→Evaluation→Purchase) — previously referenced in the persona prompts but never defined. TEEP made a required brief input in `brief-creation.md`; wired into routing for hooks, briefs, and persona reads. Third source on valence/intensity (cross-referenced to `hook-psychology.md` #11, not duplicated). Numbers stated-only.
- [2026-06-19 - Permission hooks / the Emotional Zone Audit / soft creative](inbox/2026-06-19-permission-hooks-zone-1-soft-creative.md) - **applied (Jimmy approved).** Performance-creative article on calm/soft creative for an exhausted market. Added valence×intensity + the headspace-at-exposure rule + an AI-defaults-to-Zone-4 caution to `hook-psychology.md` #11, and a new **Permission / Zone 1** format to `hooks.md` #21; wired into `skills/hooks/strategy.md`. **Second independent source for the valence/intensity zone framework**, which corroborated and promoted the 12-combination zone candidate. Method is two-source + affect science (circumplex); the article's numbers (CAC, engagement multiples) are stated-only and kept out of canon.
- [2026-06-18 - Dara Denney's nine "converting" Meta hooks (anti-bloat verdict)](inbox/2026-06-18-dara-denney-nine-converting-hooks.md) - **resolved 2026-06-22 (Jimmy approved the #8 sharpen).** Credible-operator content video, but ~7 of 9 hooks are already in the `hooks.md` taxonomy — **no new format entries** added, to avoid diluting the doc. The one net-new, non-ephemeral item — the funnel-stage siblings of #8 (how do I *pick* = decision/solution-aware; how to *start* = activation/most-aware) — was applied as a one-line sharpen to `hooks.md` #8. Two trend-ephemeral executions (whisper/ASMR sound hook, Snapchat-filter visual hook) routed to patterns-to-monitor, not canon. Best insight is a testing point (big swings, reformat top-5 across all hooks) → iterations. Numbers stated, not shown.
- [2026-06-18 - The 12-combination ad-iteration system (Sarah)](inbox/2026-06-18-12-combination-ad-iteration-system.md) - mixed-confidence operator-educator signal from a pasted YouTube training transcript, illustrated on two Norse Organics ads. Key themes: the finite 12-combination grid (4 valence/intensity zones × 3 selves) for iterating a winning ad with the angle held fixed, attributing wins to communication via naming conventions, zone-coherence as a script/edit rule, a TEE funnel lens, music-to-self matching, and building the LLM a clean "communication brain." Performance inferred from ad-library run dates; zone/self labels explicitly subjective.
- [2026-06-18 - Neurologically sound hooks and the first second (Tether Lab / Neurons Inc research)](inbox/2026-06-18-neurologically-sound-hooks-first-second.md) - **applied 2026-06-22 (Jimmy approved).** Externally-grounded craft signal from a pasted YouTube community-call transcript recounting Neurons Inc / Dr. Thomas Zoega Ramsoe EEG research. Key themes: the real decision window is the first *second* not the first three (ad-vs-content triage ~100ms, emotion ~300ms, recognition/fatigue ~700ms, stay-or-go ~1s); the first second is won by the visual and sound hook, not the spoken line; and four brain-stopping mechanics (candid face mid-emotion, motion against the scroll, format-break object/partial-reveal, precognitive one-sided sound). Applied as the "The First Second" section in `hooks.md` and the four-element decision lens in `skills/hooks/strategy.md`. Exact ms figures second-hand and framed as directional.
- [2026-06-18 - Hijacking visual tension from organic content for two-second hooks (Sarah / School call)](inbox/2026-06-18-hijacking-visual-tension-organic-2-second-hooks.md) - **applied 2026-06-22 (Jimmy approved).** Second independent expert corroborating the first-second principle above, from a pasted YouTube community-call transcript that studies organic creators rather than ads. Key themes: open-loop on-screen *text* as a first-second carrier (refines "won by visual and sound"); two-second grabs that *stack* (face + fast angle-cut + sound); fast cutting; pointing/arrows/hands-holding-product; story-cold-open under rising sound; the visual-complexity↔text-load pairing rule; statics mechanics (object about-to-fall, wrong-environment, obvious-AI); and the steal-visual-tension-from-organic workflow. Applied as the "Two-second grabs that stack" subsection in `hooks.md` ("The First Second") and a refinement in `skills/hooks/strategy.md`. Named "studies" are second-hand/unlinked; color-sequence claim held out as directional.
- [2026-06-18 - Organic content playbook 2026 (Tonic Health / Sunny)](inbox/2026-06-18-tonic-health-organic-content-playbook-2026.md) - mixed-confidence founder operator signal from a pasted DC Diaries YouTube transcript. Key themes: native-setting hooks, value-first cadence (product 2-3x/month), novelty-bias / repeat-what-works, volume-over-perfection batch shoots, the comment-wave-as-research loop, organic-to-paid translation (named as already fatigued), and distribution-beats-spend. Reach figures and paid-translation results stated, not verified.
- [2026-06-03 - Meta 2026 creative scaling, persona remixing, and context engineering](inbox/2026-06-03-meta-2026-creative-scaling-persona-remix.md) - mixed-confidence operator signal from a pasted YouTube transcript. Key themes: persona-specific asset remixing, founder objection-handling, native wrappers, persona-level scaling, purchase-trigger research, and context engineering.
- [2026-06-03 - Creative forecasting volume, hit rate, churn, and half-life](inbox/2026-06-03-creative-forecasting-volume-hit-rate-churn.md) - mixed-confidence operator signal from a pasted YouTube transcript. Key themes: creative volume forecasting, winner survival, churn, half-life, test tax, under-volume versus low-quality diagnosis, and persona-led diversity planning.
- [2026-06-03 - Claude creative strategy OS and reasoning traces](inbox/2026-06-03-claude-creative-strategy-os-reasoning-traces.md) - mixed-confidence operator signal from a pasted YouTube transcript. Key themes: brand context versus domain context, skills as orchestration, selective context retrieval, framework databases, grading loops, psychological diversity, and reasoning traces.

## Review queue

See `context-update-candidates/README.md` for the live queue. The entries below predate the draft-first model and remain as candidates awaiting corroboration, not drafts.

- [2026-06-18 - The 12-combination ad-iteration system (Sarah)](context-update-candidates/2026-06-18-12-combination-ad-iteration-system.md) - candidate. Named additions to `iterations.md` (the 12-combination grid as an iteration axis; attribute wins to communication via naming conventions), zone-coherence as a rule for `scriptwriting.md`, a psychological-diversity-taxonomy note for `creative-strategy-fundamentals.md`, and a corroborating "communication brain" note near the brand-brain CLAUDE template. One self-reported framework, performance unverified; promote on corroboration or Jimmy's approval.
- [2026-06-18 - Organic content playbook 2026 (Tonic Health / Sunny)](context-update-candidates/2026-06-18-tonic-health-organic-content-playbook-2026.md) - candidate. Named additions to `organic-social-analysis.md` (native-setting hook, value-first cadence, novelty-bias repeat, comment-wave-as-research), with organic-to-paid translation routed to `adapting-scripts.md` and a native-setting-hook swipe-file proposal. One self-reported source; promote on corroboration or Jimmy's approval.
- [2026-06-03 - Meta 2026 creative scaling and persona remixing](context-update-candidates/2026-06-03-meta-2026-creative-scaling-persona-remix.md) - candidate. Persona/remix patterns route to patterns-to-monitor until a second source or account data corroborates them.
- [2026-06-03 - Creative forecasting volume, hit rate, churn, and half-life](context-update-candidates/2026-06-03-creative-forecasting-volume-hit-rate-churn.md) - candidate. Measurement framework awaiting account evidence before changing performance method.
- [2026-06-03 - Claude creative strategy OS and reasoning traces](context-update-candidates/2026-06-03-claude-creative-strategy-os-reasoning-traces.md) - candidate. Architecture-level signal that informs direction, not a single-surface edit.

## Swipe File Routing

- [Global creative-strategy taste swipe file](../parker-taste/swipe-file/INDEX.md) - updated with reusable cross-brand creative patterns from expert signals.
- Brand-specific expert ideas should route to `z-brands/[brand]/swipe-file/` when the active brand fit is clear.

## Routing Rules

- Save the signal here as provenance (the one pre-approval write), then propose the verbatim change in the review queue. The signal is the receipt; the approved-and-applied change is the deliverable.
- For video sources, prefer Parker Vault's Gemini upload path before link scraping.
- Classify every source against the four components — context docs, knowledge docs, tool calls, processes — before proposing, and propose updating an existing surface rather than creating a new one when the learning fits.
- Never modify the real surface before Jimmy approves. Show the exact change — old → new for edits, full content for new docs — not a summary. A single source can earn a proposed change, but only Jimmy's approval applies it; a mixed-confidence method-changing claim is a watch item until corroborated.
- On approval, apply the proposed text exactly and route brand-specific ideas to `z-brands/[brand]/swipe-file/`, reusable patterns to `global/knowledge/creative-strategy/parker-taste/swipe-file/`.
- Leave exactly one review-queue entry per intake — carrying the full verbatim proposal — so Jimmy never has to dig and never has to imagine the change.
