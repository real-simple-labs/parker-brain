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

Division of labor: `hooks.md` is the reference taxonomy and examples (what the formats are, done well); `hook-psychology.md` is the reasoning layer (why hooks work, how to pick from mechanism, how to diagnose a weak one); and this skill plus its `processes/` are the steps (analyze the brand, pick, write, check). The process files are the execution layer — the writing playbook for each format family. They assume `hooks.md` and `hook-psychology.md` are loaded and carry only how to write that format well. If a process and `hooks.md` disagree on what a format is, `hooks.md` wins; if a process and `hook-psychology.md` disagree on why it works, `hook-psychology.md` wins.

## How this skill runs

1. **Load brand context.** Brand voice, ICP, personas, voice of customer, compliance, current creative challenges, what has been tested. No output without this loaded.

2. **Identify ICP and emotion first.** Before picking any format, name the specific person and the specific emotion the hook will activate. If those cannot be named, the hook will be generic. This is a gate — if ICP and emotion are not clear from brand context, ask before proceeding.

3. **Run strategy.md to pick the hook format(s).** Different brand types, awareness stages, and emotional drivers point to different formats. The strategy doc holds the decision logic and the format menu.

4. **Load and execute the picked process file(s).** Each format process holds the writing playbook for that family of hooks — execute it against the psychology `hooks.md` defines for the format. If the picked format has no standalone process, write it from `hooks.md` directly.

5. **Write the hooks.** Typically 2-4 hook recommendations per request, with deep justification on each. Quality over quantity.

6. **Run the must-haves check.** Every hook must pass relevance, clear promise, zero confusion, emotional targeting, and native format.

7. **Format output per the structure below.**

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

## Hard rules

- **ICP + emotion first, always.** Every hook is targeted to a specific person feeling a specific emotion. Generic hooks fail.
- **No copy-paste from format examples.** Each hook must follow the psychological principle of the format while being built from the brand's actual audience language and pain points. Generic hooks with product names swapped in are not hooks. The examples in `hooks.md` are for you to learn the structure from — never surface them verbatim to the user as if they were the recommendation.
- **Only what TO test, never what to avoid.** Recommend hooks to test. Do not produce "what not to test," "deprioritize these," or "skip these formats" sections, even framed as opportunities.
- **80% of creative energy on the first three seconds.** That is the discipline of hook writing.
- **Narrative visual description, not shorthand.** When describing the visual hook, write as if a creative team or another model has never seen the video and needs to picture the first three seconds from your words. Move through what the viewer sees and hears in order. A label is only a handle, and a checklist of visual fields is not a description.
- **Hook is not product intro.** Hooks set up the conflict, the curiosity, or the qualification. The product introduction comes later.
- **Relevance over raw attention.** Wrong-audience attention is wasted spend. Qualifying the right person in frame one is more valuable than stopping every scroll.
- **Native format.** Every hook must pass the "would this live on the organic feed" test. 2022-era ad styling is dead.
- **Source the customer language from real reviews and comments.** Never write hooks in marketing voice.
- **Compliance walls apply.** Forbidden terms remain forbidden in hooks. Push back, explain, offer compliant alternatives.
- **No predicted metric improvements.** Never claim "this hook will improve hook rate by X%."
- **Match pacing to audience age.** Under 30 → cut every 2-3 seconds. 30-50 → 3-4 seconds. Over 50 → 3-5 seconds. Total ad length roughly matches age range.
- **No fabricated stats or claims** in hook copy. Every claim traces to verified data.
