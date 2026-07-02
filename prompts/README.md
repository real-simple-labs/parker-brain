# Running the prompts — the build order for standing up a brand brain

This is the order to run the prompts when the job is to build a brand's brain from scratch: a fresh clone of this repo, Parker MCP connected, a new brand to audit. It is the cold-start sequence, not a daily checklist.

**To execute the build, follow `prompts/onboarding-runner.md`.** That runner is the executable version of this order: it scaffolds the standalone brand-brain layout, ships the full factory method into the brand repo — the skills (craft + routine) into `.claude/skills/` where Claude Code loads them on clone, and the prompts, creative-strategy knowledge, and runtime system docs under `parker-system/` — maps each prompt's output path, and carries the approval gates. Shipping the prompts is what lets the brain refresh and rebuild its own docs later by re-running the exact prompts that made them. This README is the why and the sequence; the runner is the how.

**Read this first: the phases are a backbone, not a turnstile.** Per `system/three-phase-operating-model.md`, the three phases are how Parker thinks, not a gate the user has to pass. If someone just asks for a script, an idea, or a quick read, give it to them — the phases run silently underneath, and the answer is better because Parker has the audit in its head, not because the user sat through it. This build order is for the one situation where the task genuinely is "set this brand up" or "figure out what our strategy should be." Then you walk it in order, because you can't decide who to target before you've read the brand, and you can't brief ideas before you know who you're targeting.

## Phase 0 — Before any prompt

- **Build in the brand's own repo, not in this clone.** `parker-brain` is the open-sourced factory teams clone for the prompts, skills, and methodology; the brand brain is a **separate, standalone repository for that brand.** Initialize a new git repo for the brand, distinct from `parker-brain`, and write every output there — never commit brand data back into the cloned product brain. `onboarding-runner.md` → Phase 0 carries the mechanics.
- **Connect and confirm the brand.** Parker MCP must be reachable (an interactive session reaches it; headless is walled off today). Call `get_available_brands`, confirm the right brand, and lock its brand_id — several brands can share a name across orgs. If the MCP is not connected, the brain cannot be built from the source: tell the user Parker needs some way to reach the ad account, organic socials, reviews, and surveys — the Parker MCP carries all of it, or independent platform exports can feed it more manually (`system/parker-tools.md`).
- **Read the entry context.** `CLAUDE.md` (how Parker thinks and what this repo is), `system/parker-system-map.md` (the surfaces), `system/three-phase-operating-model.md` (this spine), `system/open-loops-system.md` (the loop pipeline), and `global/knowledge/creative-strategy/expertise-routing.md` (which method docs each prompt must load).
- **Assume zero brand-provided inputs.** Every foundation prompt reads from the source itself — the ad account, the site, reviews, organic — through Parker MCP, and reads it over time (year-over-year, seasonal), not as a one-day snapshot. Brand confirmation is a later upgrade, never a prerequisite.
- **How to run one prompt.** Open it and follow it; it loads its own expertise through the embedded blocks and `expertise-routing.md`. Write its output to the brand's space under `z-brands/[brand]/...`, mark every claim stated / inferred / verified, and end with open loops. Run output goes in the brand's repo, never back into this product brain.

## Phase 1 — Audit (learn everything)

Know the brand cold; don't plan yet. The numbered list below is the readable sequence; the binding **dependency graph** (which branches run in parallel vs. what is hard-blocked) lives in `onboarding-runner.md` → "Run order and dependencies." Read that before executing.

**First, the internal audit baseline.** Run `prompts/audits-*` once now — the quarterly cuts (the 90-day creative-strategy audit anchor, plus performance, diversity, customer-review, and whitespace), the monthly cuts (hook audit, performance report, organic-TikTok, TikTok mining), and the first biweekly iterations report + weekly snapshot — into their date buckets under `audits/`. The account one-pagers in step 1 are *syntheses of these audits*, so the packet has to exist before they can synthesize it. From here on these re-run on a schedule from each audit's `generated_on`; the first pass is part of the build.

1. **Brand foundation sub-context docs.** Run each prompt in `prompts/brand-profile/` except `_foundations.md` (the shared scaffold every one embeds) and `brand-profile-narrative.md` (the synthesis, next). These are the slices — brand identity, website and product, ad-account evaluation, performance targets, reputation, organic channels, customer-journey-and-persona discovery, category and market, marketing calendar, operations, community and forums, visual vocabulary. Each writes to `z-brands/[brand]/sub-context-docs/` and emits open loops.
2. **brand-profile-narrative.** Run after the slices exist. It synthesizes them into `z-brands/[brand]/brand-profile.md` — the always-loaded one-pager — and pulls the slices' open loops together. It points to the slices by filename; it does not reproduce them.
3. **Competitor profiles.** Identify the competitive set from the ad account and Parker MCP, then for each competitor run the `prompts/competitor-profile/` slices and roll them up with `competitor-snapshot.md`. Mirrors the brand-side structure under `z-brands/[brand]/competitors/[group]/[competitor]/`.
4. **Persona research.** Run the source-pull prompts in `prompts/personas/` (ad-account, ad-comments, customer-reviews, other-reviews, post-purchase-surveys, reddit, brand-reputation, brand-self-echo-detection), then synthesize with `personas-profile.md`, plus `persona-voice-library.md`, `lifecycle-journey-maps.md`, and `cross-persona-bias-notes.md`. Output to `z-brands/[brand]/personas/`.
5. **Voice of customer.** Run `voc-corpus-profile.md` and the extraction slices in `prompts/voice-of-customer/`, then `voice-of-customer-assembly.md`. Output to `z-brands/[brand]/voice-of-customer.md`.
6. **Cross-cut synthesis.** `prompts/market-synthesis/gaps-opportunities-inspo.md` reads across the foundation and competitors for the openings.
7. **Open-loops roll-up.** Once the docs above have emitted their loops, run `prompts/open-loops/open-loops-roll-up.md` to consolidate, grade, tier, and route them into one prioritized agenda. This is the bridge into Phase 2.

Phase 1 output: the always-loaded brand-profile, the competitor snapshots, the personas and voice-of-customer library, and the graded open-loop set.

## Phase 2 — Decide the strategy

Turn the audit into a point of view. Persona-led, drawing on all four buckets — personas, product, messaging, talent.

Phase 2 has four strategy inputs, one per territory, each resolving its Phase-1 evidence into a committed recommendation. Run the four inputs first, then synthesize.

8. **persona-strategy-input** (`prompts/strategic-roadmap/persona-strategy-input.md`) — the WHO: which persona to lead acquisition against, who is emerging, who to deprioritize, from the served-vs-buyer read.
9. **product-priority** (`prompts/strategic-roadmap/product-priority.md`) — the WHAT: which SKU leads, or where the next swing is, each candidate sized against the economics before committing.
10. **messaging-strategy-input** (`prompts/strategic-roadmap/messaging-strategy-input.md`) — what the brand should lead with saying, the territory, register, and proof, from where the brand, the customer, and the field diverge.
11. **creator-talent-strategy-input** (`prompts/strategic-roadmap/creator-talent-strategy-input.md`) — who should be on camera, from the talent-persona match, the casting that has won, and the roster gaps.
12. **strategic-roadmap** (`prompts/strategic-roadmap/strategic-roadmap.md`) — synthesizes the four inputs into a diagnosis and the brand's top three priorities in order, each carrying its persona, its evidence, and the open loop it still rests on. It leads with whichever bucket carries the most weight and shows how the others follow.

**The gate.** When Parker is driving the strategy, present the roadmap for the user to approve, adjust, or reject before Phase 3 — approval is what turns the call into committed direction. When the user is already driving their own direction, this is not a permission slip; help them execute.

## Phase 3 — Make the work

Only once the roadmap is the agreed direction.

Phase 3's judgment runs as three prompts on one spine — capture, then evaluate, then build — and the split is deliberate: capture stays generous because grading happens later, separately, so the bar never quietly suppresses what gets logged.

13. **brand-idea-bank** (`prompts/ideas-and-briefs/brand-idea-bank.md`) — the brand's always-on idea memory. Capture runs continuously through everything Parker does, not only here, and it transfers each idea across verbatim rather than summarizing it.
14. **idea-evaluation** (`prompts/ideas-and-briefs/idea-evaluation.md`) — grade the whole captured pile against the approved roadmap: the priority each idea serves, the lever it pulls, its evidence band confidence-first, and the roads-not-taken kill list. Output is a ranked shortlist naming which ideas go to briefs first, written to `z-brands/[brand]/idea-bank/evaluation-[YYYY-MM-DD].md`.
15. **brief-creation** (`prompts/ideas-and-briefs/brief-creation.md`) — take the shortlist's top picks and promote each into a concept, its two or three variations, and the creator direction, each carrying its three validations: account data, in-the-wild inspo, and the strategy tie to the roadmap. Output to `z-brands/[brand]/briefs/`.

## Baseline at cold start, then ongoing

The audit cadence layer is the one piece that is **both**: its first pass is part of the cold start, and from then on it re-runs on a schedule. The account one-pagers (`ad-account-evaluation`, `performance-targets-and-metrics`, `organic-channels-inventory`) are defined as syntheses of these audits, so the audits have to exist before the build can synthesize them — generating the one-pager first is what leaves it reading "no audit packet existed, this is the baseline." So the entire `prompts/audits-*` family — weekly, biweekly, monthly, quarterly, **and** the external/competitor cuts — runs once during Phase 1 as the t0 baseline (none deferred), and after that the refresh-sweep schedule re-reads the account on each audit's named interval from its own `generated_on`.

## Ongoing — not part of the cold start

Genuinely ongoing, run only on a standing brain: the open-loops advance and validate skills work loops into hypotheses and verdicts and feed the findings back into the brand-profile; and self-improvement and dreaming promote learning over time. Run these on a standing brain, not during onboarding.

**Never run as a build step.** The embedded blocks (`_expertise-core-block`, `_parker-voice-block`, `_open-loops-core-block`, `_notion-ai-tagging-and-foundational-context`, `brand-profile/_foundations`) are *included* by the content prompts, never executed standalone. `prompts/global-databases/*` is global product setup, not part of a brand build.
