---
name: hooks
description: Write hooks for a specific ad — the first three seconds that earn the click and the watch. Uses the proven hook formats from the canonical taxonomy, picks the right one for the brand and audience, and produces hooks built around a specific ICP and emotion.
triggers:
  - write me a hook
  - write hooks for this ad
  - new hook ideas
  - give me hook variations
  - what hook should I test
  - help me write the opening
  - first three seconds of this video
  - hook ideas for this brand
  - rewrite this hook
  - the opening isn't working
---

# Hooks

## Goal

Write the first three seconds of an ad — the moment that earns relevant attention or loses it. The hook is the gate. If the hook fails, the rest of the ad does not matter. The skill picks the right hook format for the brand and audience, then writes hooks built around a specific ICP feeling a specific emotion.

This skill writes hooks. It does not write full scripts (route to scriptwriting), iterate on existing winners (route to iterations), or evaluate which existing hooks are working (route to ad-account-analysis).

## What you are working from

The hook formats this skill writes from are grounded in the canonical taxonomy, not reinvented per run. Before writing, load what `global/knowledge/creative-strategy/expertise-routing.md` names for a hook task: `hooks.md`, the hook taxonomy and what makes hooks work, so the format named is a real one and the writing uses its concepts; `hook-psychology.md`, the cognitive science beneath the taxonomy, so the format is picked from the mechanism the brand's situation calls for and a weak hook can be diagnosed by which job (notice / stay / encode) it fails; `ad-formats/`, so the visual hook is named by what the account's tags actually call it; and `killer-performance-ads.md`, because a hook only earns its keep when it sets up a genuinely great ad. Brand and account data pull through the Parker tools inventoried in `system/parker-tools.md`. A hook set that never speaks the taxonomy's language proves the method was never opened.

**Path resolution:** the doc paths above are the factory's. In a shipped brand brain the same docs live under `parker-system/creative-strategy-context/` (craft) and `parker-system/system/` (runtime system docs); ship-time normalization (`scripts/normalize-brain-paths.py`) rewrites these references so they resolve there. If a path ever fails to resolve, glob for the doc by filename rather than skipping the load — a missing read is never the fallback.

Division of labor: `hooks.md` is the reference taxonomy and examples (what the formats are, done well); `hook-psychology.md` is the reasoning layer (why hooks work, how to pick from mechanism, how to diagnose a weak one); and this skill plus its `processes/` are the steps (analyze the brand, pick, write, check). The process files are the execution layer — the writing playbook for each format family. They assume `hooks.md` and `hook-psychology.md` are loaded and carry only how to write that format well. If a process and `hooks.md` disagree on what a format is, `hooks.md` wins; if a process and `hook-psychology.md` disagree on why it works, `hook-psychology.md` wins.

## How this skill runs

1. **Load brand context — strategy first.** The brand's committed strategy (`strategy/` — the working thesis, the roadmap's persona and messaging calls) frames which hooks are even in play; read it before writing, and check the idea bank (`idea-bank/`, including evaluated ideas) for an entry this request should execute from, carrying its reasoning. Then brand voice, ICP, personas, voice of customer, compliance, current creative challenges, what has been tested. No output without this loaded. A request that cuts against the committed strategy is surfaced with the conflict named, not silently executed; a brain without `strategy/` or an idea bank yet gets one line saying so.

2. **Identify ICP and emotion first.** Before picking any format, name the specific person and the specific emotion the hook will activate. If those cannot be named, the hook will be generic. This is a gate — if ICP and emotion are not clear from brand context, ask before proceeding.

3. **Run strategy.md to pick the hook format(s).** Different brand types, awareness stages, and emotional drivers point to different formats. The strategy doc holds the decision logic and the format menu.

4. **Load and execute the picked process file(s).** Each format process holds the writing playbook for that family of hooks — execute it against the psychology `hooks.md` defines for the format. If the picked format has no standalone process, write it from `hooks.md` directly.

5. **Write the hooks.** Typically 2-4 hook recommendations per request, with deep justification on each. Quality over quantity.

6. **Run the must-haves check.** Every hook must pass relevance, clear promise, zero confusion, emotional targeting, and native format.

7. **Run the two review gates automatically, before you present anything.** They are not optional, not a "second opinion," and never offered to the user as a choice — asking "want me to review this" is itself the failure. Running `scripts/voice-lint.py` yourself is not the gate; the gate is the independent agent, and its returned verdict fills the receipt block below, which you cannot write yourself. Grounding gate first (it changes content), voice gate second (it changes lines). Spawn the `context-grounding-review` agent (defined at `.claude/agents/context-grounding-review.md`) with the user's task, the hook set, the brain root, and the list of tool pulls made this session. It runs `scripts/grounding-check.py` and independently derives what should have been loaded and pulled — the taxonomy vocabulary, the ICP and VoC behind each hook's language — then diffs that against the evidence. A `bounced` verdict means re-pull and regenerate the affected hooks. This gate runs before the voice gate because its verdict changes content, not lines. And every bounce gets captured through `self-improvement-intake` as a one-line reasoning trace — the task shape plus the loads or pulls that were missed — so the routing layer learns from the catch instead of re-making the same mistake for the gate to re-catch.

8. **Run the voice review gate.** Spawn the `creative-voice-review` agent (defined at `.claude/agents/creative-voice-review.md`) on the finished hook set, handing it the exact text overlays and spoken lines, the brand voice profile if one exists, and the deliverable type. The agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass per `ai-writing-tells.md` — and `spoken-script-voice.md` for the spoken lines — independently, in a context that did not write them. Apply its rewrites and re-run until the verdict is `ships`. A flag that conflicts with sourced customer language keeps the source, with the reason carried into the Voice Review block. **Harness fallback:** if this session's harness cannot spawn subagents, the gates still run — execute the grounding checklist from `.claude/agents/context-grounding-review.md` and then the voice checklist from `.claude/agents/creative-voice-review.md` as separate, fresh passes, running `python3 scripts/grounding-check.py` and `python3 scripts/voice-lint.py` yourself, and mark both review blocks "run in-context — no subagent harness" so the degradation is visible.

9. **Format output per the structure below.**

## Output structure

### The Hook Recommendations

2-4 hooks, never more. Each one includes:

- A name that signals the move. Format pattern: "[Hook format] — [Specific ICP + emotion angle]."
- The hook itself — exact text overlay, exact spoken line, a narrative description of what happens visually in the first three seconds, exact vibe.
- The four hook elements specified — text overlay, sound, visual, vibe — even if some are unused for this hook.
- The ICP and the emotion the hook is built around. Specific person, specific feeling.
- Tag: **Safe bet** (a format proven for this brand or category), **Untapped opportunity** (a format the brand has not yet tested), or **Iteration** (a sharpening of an existing hook that is working).
- Two-to-four sentences on why this hook fits this brand's audience psychology and the format's psychological basis.

### Brand Context Applied

- **What I used:** ICP, persona work, customer language, voice of customer, brand voice, compliance.
- **What I avoided:** compliance walls, forbidden terms, off-brand voice.
- **Why this fits:** two-to-four sentences on why these hooks match the brand's current moment.

### Grounding Review

The grounding gate's receipt, required on every set: the `context-grounding-review` verdict, one or two plain sentences on what it checked (taxonomy vocabulary evidenced, verbatims traced, ICP and VoC behind each hook), and — if it bounced — what was re-pulled and regenerated before re-shipping. A set missing this block did not pass the gate.

### Voice Review

The gate's receipt, required on every set: the `creative-voice-review` verdict, the lint density before and after, one or two plain sentences on what was flagged and fixed, and any flag kept with its reason — a customer verbatim, or a pattern the brand's own winners genuinely use. A set missing this block did not pass the gate.

## Hard rules

- **ICP + emotion first, always.** Every hook is targeted to a specific person feeling a specific emotion. Generic hooks fail.
- **No copy-paste from format examples.** Each hook must follow the psychological principle of the format while being built from the brand's actual audience language and pain points. Generic hooks with product names swapped in are not hooks. The examples in `hooks.md` are for you to learn the structure from — never surface them verbatim to the user as if they were the recommendation.
- **Only what TO test, never what to avoid.** Recommend hooks to test. Do not produce "what not to test," "deprioritize these," or "skip these formats" sections, even framed as opportunities.
- **80% of creative energy on the first three seconds.** That is the discipline of hook writing.
- **Narrative visual description, not shorthand.** When describing the visual hook, write as if a creative team or another model has never seen the video and needs to picture the first three seconds from your words. Move through what the viewer sees and hears in order. A label is only a handle, and a checklist of visual fields is not a description.
- **Hook is not product intro.** Hooks set up the conflict, the curiosity, or the qualification. The product introduction comes later.
- **Relevance over raw attention.** Wrong-audience attention is wasted spend. Qualifying the right person in frame one is more valuable than stopping every scroll.
- **Native format.** Every hook must pass the "would this live on the organic feed" test. 2022-era ad styling is dead.
- **Source the customer language from real reviews and comments.** Never write hooks in marketing voice. And match the register to the surface: a written verbatim ships as-is in a text overlay, but a *spoken* hook line voiced from a review keeps the customer's words and gets re-cadenced for the mouth, per the written-vs-spoken rule in `spoken-script-voice.md`.
- **Compliance walls apply.** Forbidden terms remain forbidden in hooks. Push back, explain, offer compliant alternatives.
- **No predicted metric improvements.** Never claim "this hook will improve hook rate by X%."
- **Match pacing to audience age.** Under 30 → cut every 2-3 seconds. 30-50 → 3-4 seconds. Over 50 → 3-5 seconds. Total ad length roughly matches age range.
- **No fabricated stats or claims** in hook copy. Every claim traces to verified data.
- **No hook set ships bounced.** The independent `context-grounding-review` agent verifies the hooks were built from the real taxonomy, the brand's actual ICP and customer language, and traced sources — a hook set that never speaks the taxonomy's language proves the method was never opened. A bounce means re-pull and regenerate; its verdict appears in the Grounding Review block.
- **Check facts, not flavor.** The grounding gate verifies facts — numbers, sizes, specs, prices, claims must be real and trace. It does not hunt the exact source of every customer-voice line; a review-, comment-, or thread-sounding line that reads authentic and fits the brand register is fine unpulled, labeled illustrative in one line so no made-up quote runs as a real testimonial. Bounce for a wrong fact, never for an untraceable voice line.
- **The gates run automatically, before you present — never offered.** Both review agents run every time, on their own, before the set reaches the user. Never ask "want me to review this," never call it a "second opinion," never present and hold the review for later. Running the linter yourself is not the gate — the gate is the independent agent, whose returned verdict fills the receipt blocks you cannot write yourself.
- **No hook set ships without a clean `creative-voice-review` pass.** The independent agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass against `ai-writing-tells.md`; its verdict and the before/after lint density appear in the Voice Review block. Self-review does not substitute — the reviewer must not be the writer.
