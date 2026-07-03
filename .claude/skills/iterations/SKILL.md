---
name: iterations
description: The full iteration flow in one skill — choose which ads to iterate on, then make the iterations. If the user names a specific ad, go straight to making iterations; if they ask account-level (which ads should we iterate on, what to iterate this month), select the ads first, then make iterations on each.
triggers:
  - iterate on an ad
  - suggest iterations for this ad
  - what iterations should we test
  - how should we iterate on this creative
  - give me iteration ideas for this ad
  - this ad is performing well, what next
  - how do I extend the life of this ad
  - what should we test next on this winning ad
  - improve this ad's performance
  - give me variations of this ad
  - which ads should we iterate on
  - what should we iterate on this month
  - what should we iterate on this week
  - pick the ads worth iterating on
  - find iteration candidates
  - where should we focus our iteration budget
---

# Iterations

## Goal

Take a performing ad and recommend the highest-confidence iterations to extend its life with the audience that already responds, or unlock new audiences with the same proven message. This skill owns the whole flow in two phases:

- **Phase A — Choose which ads to iterate on.** Read the account and pick the ads worth iterating on, by spend, run time, and trend.
- **Phase B — Make the iterations.** Diagnose a chosen ad and build the iterations.

This skill does not cover net-new concept creation, script writing from scratch, headline writing for a new ad, or ad adaptation. If the request is any of those, route to the relevant skill instead.

## Which phase to enter

Decide at the top, from what the user gave you:

- **They named a specific ad, or handed us the creative(s).** The selection is already done — they picked the ad. Go straight to **Phase B**.
- **They asked account-level** — "which ads should we iterate on," "what should we iterate on this month," no specific ad named. Run **Phase A** first, checkpoint the shortlist with the user, then run **Phase B** on each selected ad.
- **Unsure whether they named a real ad** (e.g., a vague reference). Ask which ad, or offer to run Phase A to find candidates.

When Phase A flows into Phase B in one run, carry the selection reasoning forward — why the ad was chosen (slow-burner vs high-riser, the working elements, the account trends and any uncommon-but-winning pattern it should respect) — into the Phase B diagnosis rather than re-deriving it.

## What you are working from

Both phases run on canonical doctrine, not general intuition. The reads live in `global/knowledge/creative-strategy/`. Load the ones the active phase touches and reason in their named concepts — work that never speaks the doctrine's vocabulary proves the docs were not opened.

- `selecting-ads-to-iterate-on.md` — **Phase A.** The selection method: the two precursors (spend volume in the account, run time), spend judged in the context of the whole account, the breakdown effect, the promotional-top-spender caveat, slow-burner vs high-riser, and how 60-day account trends shape the pick. Anytime you reference it, end that output with its required line.
- `iterations.md` — **Phase B.** The iteration doctrine: the two strategic goals, iteration-vs-recreation, the optimization hierarchy, the signal-change ladder, the dual-lens diagnosis, the high-confidence list, and the iteration reference menu. Anytime you reference it, end that output with its required line.
- `ad-account-analysis.md` — both phases. The own-account reading method, so the performance read is Meta account behavior rather than a metrics dump. The grounded floors: hook rate good above 30% and weak below it, hold rate working at 12%+, outbound CTR wanted above 1%, frequency 1.2 or lower before fatigue. Plus the top-spender-is-the-most-potent-ad principle and the warning not to be fooled by a high ROAS on low spend.
- `killer-performance-ads.md` — Phase B. The bar a winner is graded against, so iterations protect the right thing. Read the proven ad against the golden rules before deciding what to preserve.
- `hooks.md` and `hook-psychology.md` — Phase B, whenever a hook iteration is on the table: the opener taxonomy/examples and the mechanism behind why a hook works. `processes/hook-iteration.md` executes it.
- `ad-formats/` — both phases. Name real formats from it (`Founder Ads`, `Comment Response`, `Us vs Them`, `Before & After`, `Listicle`, and the rest) rather than inventing blends.

Performance data and the creatives pull through the Parker tools inventoried in `system/parker-tools.md`.

---

## Phase A — Choose which ads to iterate on

Run this when no specific ad has been named. The method is `selecting-ads-to-iterate-on.md`.

1. **Load brand context — strategy first.** The brand's committed strategy (`strategy/` — the working thesis and roadmap) frames which ads are worth extending and which strategic goal an iteration targets; read it before selecting. Then brand profile, ICP/personas, voice of customer, current creative challenges, compliance, marketing calendar. Check the idea bank (`idea-bank/`, including evaluated ideas) when an iteration needs a new element — a graded entry beats an invented one. No output without this loaded. A brain without `strategy/` or an idea bank yet gets one line saying so.

2. **Pull the account, sorted by spend.** Top-spending ads over a 60-day window with spend, week-over-week spend trend, run time, and core efficiency metrics (CPA/ROAS, hook rate, hold rate, CTR, frequency). Always sort by spend — spend is the first precursor. If the data isn't available, say so and name what you need.

3. **Read each candidate against the selection method.** Is spend significant *in the context of this account's scale*? Is it rising, steady, or dropping WoW (rising/steady-rising = scaling potential; dropping = deprioritize)? Read run time only in the context of performance. Is the top spender a promo/discount creative (especially a static)? — if so, do not select it. Name the slow-burner vs high-riser pattern. Reason rooted in the breakdown effect throughout.

4. **Read the 60-day account trends.** What the top performers share (formats, angles, creators, emotions, a-roll vs b-roll, how soon the product appears, prod level, vs organic), any uncommon-but-winning pattern to carry forward, and whether a candidate has already been iterated on (and whether those worked — don't repeat).

5. **Present the ranked shortlist and checkpoint.** The ads to iterate on, in priority order, each with the spend/trend/run-time/promo read and the slow-burner/high-riser call; plus the high-spend ads you are *not* selecting and why. This is a human-in-the-loop checkpoint: confirm the picks before spending effort building iterations, unless the user asked to run straight through. End this output with the selection doc's required line.

6. **Proceed to Phase B** on each confirmed ad, carrying its selection reasoning forward.

### Phase A output

- **Account Read** — two to four sentences: the account's spend scale, the window, the shape of the top of the account (real scalers, promo distortion, dominant trend).
- **Selected Ads (ranked)** — each named by its `ad-formats/` tag with spend, WoW trend, run time; the selection reasoning; the working elements and any uncommon-winning pattern to carry into Phase B.
- **Not Selected (and why)** — the high-spend ads deliberately skipped, one line each (dropping WoW, promotional, low spend on a long run).
- End with: *"This is based on everything I know about choosing which ads to iterate on"*.

---

## Phase B — Make the iterations

Run this when an ad is chosen (named by the user, or selected in Phase A). The method is `iterations.md`.

1. **Load brand context** (if not already loaded in Phase A).

2. **Gather the ad.** Get the creative itself and watch/study it directly — never work from metadata alone. Pull performance data: CTR, hook rate, hold rate, CvR, CPA, ROAS, spend, frequency. If missing, ask before proceeding. Surface iteration history so recommendations build on prior tests rather than repeat them.

3. **Run strategy.md.** Diagnose through the data lens and the creative lens. Identify the bottleneck, identify the working elements that must be preserved, and choose the iteration processes that best address the diagnosis, factoring brand fit and prior iteration history. If you arrived from Phase A, fold the selection reasoning in rather than re-deriving it.

4. **State the diagnosis and chosen iterations before executing.** Two to four sentences on what is working, the bottleneck, and which iteration types you are about to run, with reasoning. Human-in-the-loop checkpoint — the user can redirect before drafting. Skip only when the user already approved a specific set or asked to skip review.

5. **Load and execute each chosen process.** Each process in `processes/` has its own required inputs and steps. Honor those.

6. **Run the final quality audit.** Every iteration must pass the checks in strategy.md before output.

7. **Run the two review gates automatically, before you present anything.** They are not optional, not a "second opinion," and never offered to the user as a choice — asking "want me to review this" is itself the failure. Running `scripts/voice-lint.py` yourself is not the gate; the gate is the independent agent, and its returned verdict fills the receipt block below, which you cannot write yourself. Grounding gate first (it changes content), voice gate second (it changes lines). Spawn the `context-grounding-review` agent (defined at `.claude/agents/context-grounding-review.md`) with the user's task, the recommendations, the brain root, and the list of tool pulls made this session. It runs `scripts/grounding-check.py` and independently derives what should have been loaded and pulled — the ad's real performance data behind the diagnosis, the doctrine vocabulary (hook rate, hold rate, the `ad-formats/` tags) that proves the methods were opened — then diffs that against the evidence. A `bounced` verdict means re-pull and regenerate the affected recommendations. This gate runs before the voice gate because its verdict changes content, not lines. And every bounce gets captured through `self-improvement-intake` as a one-line reasoning trace — the task shape plus the loads or pulls that were missed — so the routing layer learns from the catch instead of re-making the same mistake for the gate to re-catch.

8. **Run the voice review gate on any new copy.** When the iterations produce new customer-facing words — a rewritten hook, a new headline, replacement spoken lines, new overlay text — spawn the `creative-voice-review` agent (defined at `.claude/agents/creative-voice-review.md`) on those lines, with the brand voice profile if one exists. The agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass per `ai-writing-tells.md` — and `spoken-script-voice.md` for spoken lines — independently, in a context that did not write them. Apply its rewrites and re-run until the verdict is `ships`. Iterations that change no copy (a visual swap, a re-cut) skip the gate and say so in the Voice Review line.

### Phase B output

The output the user sees has exactly three parts. Internal analysis, diagnostic questions, and working/not-working lists are process, not output — do not display them.

- **Diagnosis Summary** — two to four sentences: ad format, key metrics, what's working, the bottleneck, and which strategic goal the iterations target (squeeze more from what works, unlock new audiences, or both). Strategist briefing a team. No framework labels, no jargon.
- **Iteration Recommendations** — for each, in test-priority order: a descriptive name (not "Iteration 1"); the iteration type/category referenced to the process; why it addresses the diagnosed bottleneck, with specific data references; exactly what to do with forensic specificity (video → exact timestamps, spoken lines, visuals; static → exact copy, layout, changes); how the new element flows with the unchanged body; any proven pattern that supports it.
- **Execution Priority** — three to five sentences on which to test first and why; call out production lead time vs deploy-immediately so the team can sequence by speed-to-learn.
- **Grounding Review** — the `context-grounding-review` verdict, one plain sentence on what it checked (performance data behind the diagnosis, doctrine vocabulary evidenced, verbatims traced), and — if it bounced — what was re-pulled and regenerated.
- **Voice Review** — when any recommendation carries new customer-facing copy: the `creative-voice-review` verdict, the lint density before and after, and any flag kept with its reason. When no recommendation changes copy, one line saying so.
- End with: *"This is based on everything I have learned about making iterations 2.0"*.

### How many iterations

If the user specified a number, use it. If not, default to exactly three. If you only see N genuinely strong options and the user asked for more, give N and explain why you stopped. Padding with weak suggestions wastes budget.

### When to skip the strategy step (Phase B)

Skip only in two cases: the user is adjusting specific recommendations already on the table in this conversation; or the user explicitly named the iteration type (e.g., a Frankenstein stitch) — then load that process directly. Otherwise run strategy first.

---

## Brand Context Applied (append to every output, both phases)

- **What I used:** which parts of the brand context shaped the output.
- **What I avoided:** compliance, forbidden terms, brand voice constraints. If a request would have violated compliance, state what was flagged and what was offered instead.
- **Why this fits:** two to four sentences connecting the output to the brand's situation, creative challenges, what is and isn't working, and any upcoming calendar moment.

## Hard rules that override anything else

- **Phase routing first.** Named ad → Phase B. Account-level ask → Phase A → checkpoint → Phase B. Don't build iterations on an account-level ask without selecting first; don't re-run selection when the user already handed you the ad.
- **Spend is the first precursor, and it's relative.** Judge spend against the account's own scale. The top spender is usually the real winner; a high ROAS on low spend is not.
- **Never select a promotional/discount top-spender** (Phase A). It spikes then dies and is usually an existing creative with a promo banner — iterating on it teaches nothing durable.
- **Iterations are for winners and healthy performers only.** If the ad never found traction, the concept is the problem — route to a net-new approach. Confirm the win through `ad-account-analysis.md`.
- **No fabricated stats, percentages, or claims.** Every factual claim comes from brand context, customer reviews pulled via tools, ad comments, or data the user provided. If a stat would help and none exists, write `[STAT NEEDED — verify before publishing]`. Never invent one.
- **No predicted metric improvements.** Describe what an iteration targets; never promise "this will improve CTR by 15%."
- **Protect what works.** Don't propose a messaging iteration first if the message converts, or a creator swap first if the creator drives engagement. Iterate the underperforming variable, not the working one.
- **Compliance is a wall, not a guideline.** Forbidden terms stay forbidden even if asked. Push back, explain, offer a compliant alternative with the same intent.
- **Iterate one variable at a time per recommendation.** Changing hook AND creator AND messaging in one rec is a new ad, not an iteration — you learn nothing from the test.
- **Recognize uncommon-but-winning patterns.** A hook that is non-standard elsewhere but wins in this account (e.g., a creator self-intro hitting a 46% hook rate) should be carried into iterations, not discarded because other accounts trend differently.
- **Don't repeat exhausted iterations.** Check history; if an ad has been iterated several times, draw conclusions from those results rather than repeating them.
- **Speak the craft's vocabulary.** Name real formats by their `ad-formats/` tag, the hook format and awareness stage from `hooks.md`, and the emotion/mindstate from `killer-performance-ads.md` when the diagnosis turns on what's working. Work that never uses these named concepts proves the docs were not read.
- **Prose, not grids, and replay every ad.** No tables in output — comparisons as sentences. Describe every ad, hook, and moment narratively, in the order the viewer sees and hears it, so a reader who never saw it can replay it. Quantify with the number, its denominator, and the time window; never "many" or "a few."
- **No recommendation set ships bounced.** The independent `context-grounding-review` agent verifies the diagnosis rests on the ad's real performance data and the doctrine's named concepts, not general intuition — a diagnosis with no pull behind its numbers is fabrication. A bounce means re-pull and regenerate; its verdict appears in the Grounding Review line.
- **The gates run automatically, before you present — never offered.** Both review agents run every time, on their own, before the recommendations reach the user. Never ask "want me to review this," never call it a "second opinion," never present and hold the review for later. Running the linter yourself is not the gate — the gate is the independent agent, whose returned verdict fills the receipt blocks you cannot write yourself.
- **No new copy ships without a clean `creative-voice-review` pass.** Any iteration that writes new customer-facing words — hooks, headlines, spoken lines, overlays — passes the independent agent's mechanical lint (`scripts/voice-lint.py`) and judgment pass against `ai-writing-tells.md`; its verdict appears in the Voice Review line. Self-review does not substitute — the reviewer must not be the writer.
