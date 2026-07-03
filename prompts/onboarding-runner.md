# Onboarding runner — build a brand brain from scratch

This is the single entrypoint for standing up a new brand's brain end to end. When the task is "build [brand]'s brain," follow this runner: it sequences every prompt in dependency order, writes each output to the right place in the flat standalone layout, ships the craft layer into the repo, and stamps the operating contract. It is the executable version of the build order in `prompts/README.md` — read that first for why the phases are a backbone and not a turnstile, then run this for the mechanics.

The user-facing front door to all of this is the **`/set-up-brain`** skill — it opens with a welcome, calibrates to how comfortable the person is with GitHub and Claude Code, and runs this runner step by step, ending by handing off to `/get-started`. This file is the canonical method; `set-up-brain` is the experience that runs it. When invoked directly without the skill, follow it the same way: open warm, teach as you go, and hand off to `/get-started` at the end.

Run this inside an interactive Claude session with Parker MCP reachable. Headless is walled off today, so the runner assumes a live session. It assumes no brand-provided inputs are required: every foundation prompt reads from the source itself through Parker MCP, over time, not from a brief the brand hands over. An optional brand intake — the short list of things Parker genuinely cannot observe on its own — sharpens the build when the user provides it, but it is never required and never a gate.

**You are teaching, not only building — but teach at the moments, not in a stream.** Assume the person running this has little sense of what Parker is or how a brand brain works; for many it is the first time they have ever seen anything like it. Teach in plain language at the moments a person is actually listening: the welcome, the intake, each phase opening and closing, and the finish — what you are about to do, why it matters, and what they will have when it is done, in their words and not the system's. Between those moments, the build runs quiet: progress lives in `BUILD-STATUS.md` (the status file section below), not in a stream of step narration nobody reads. Explain the what and the why; keep the machinery (agents, embedded blocks, loops, tiers) out of sight. And signpost the whole way: at every phase boundary and every decision gate, say plainly where they are, what just happened, what's next, and what — if anything — you need from them, so a choice never feels like a surprise or a trap and it always feels safe to ask a question or pause.

## What this runner produces — the flat standalone layout

A brand brain is a self-contained repo a marketing team opens and talks to, not a folder inside the product brain. The tree below is the **buildable core** — the performance-marketing shape the factory knows how to construct cold — not a closed taxonomy: a standing brain grows new first-class surfaces as the org connects more of itself, per `system/growing-the-brain.md` (shipped into the brain as a runtime doc). The factory prompts describe their outputs in `z-brands/[brand]/…` terms because that is the product brain's internal tree, but a shipped brand brain is flatter and stands alone: the brand's *data* sits flat at the repo root, the executable skills (craft + routine) live in `.claude/skills/` where Claude Code actually loads them on clone, and the rest of the factory's *method* is copied in under `parker-system/`, so the brain can refresh, rebuild, and execute itself with no link back to the factory. The runner is the mapping layer: wherever a prompt says to write to a `z-brands/[brand]/…` path, write to the flat path in the table below instead.

The target top-level tree, brand repo root:

- `CLAUDE.md` — the operating contract, stamped from the template at the end.
- `README.md` — the brand-facing map, stamped at the end.
- `sub-context-docs/` — the foundation reads, including `brand-profile-narrative.md`, the always-loaded one-pager read first.
- `source-pulls/` — the raw source reads that feed personas and voice-of-customer.
- `personas/` — `personas-profile.md`, the analyses, and `voice-of-customer/`.
- `competitors/` — the deep per-rival profiles plus `_competitive-set.md`.
- `audits/` — the cadence layer, date-bucketed, with `external/` underneath each period.
- `strategy/` — the Phase-2 deliverables.
- `idea-bank/`, `briefs/` — the Phase-3 creative memory and execution artifacts.
- `open-loops/`, `hypotheses/`, `validations/`, `re-validations/` — the loop pipeline, single bucket, no team split.
- `running-notes/` — `brand-notes-from-org.md`, `missing-context.md`, and `refresh-schedule.md`, the consolidated record of when every standing doc was last run and when it is due to be re-run.
- `.claude/skills/` — **all the skills, and the one place Claude Code actually loads them from.** A skill only registers as an invocable skill when it lives under `.claude/skills/<name>/SKILL.md`; a folder anywhere else (a top-level `skills/`, or under `parker-system/`) is inert markdown that a clone never picks up. So both kinds live here together: the *routine* skills (the six scheduled routines, the `setup-routines` installer, the on-demand `get-started` walkthrough — stamped from `templates/brand-routines/`) and the full set of *craft* skills (scriptwriting, hooks, headlines, iterations, ad-account-analysis, ai-ad-generation, the open-loops pipeline, idea-bank maintenance, and the living-loop / intake skills — copied from the factory's own `.claude/skills/`). Every craft skill ships, not a curated subset. When the brand team clones the brain, these load automatically after the one-time workspace-trust prompt, and the brand `CLAUDE.md` routes every execution-shaped task through `.claude/skills/<skill>/`.
- `.claude/settings.json`, `schedules/`, `dreaming/`, `workflows/` — the rest of the living layer. `dreaming/` and `workflows/` are README-only at build time (each populated by its own runs). `.claude/settings.json` (the context hook, which injects the craft catalog every turn) and `schedules/` (the six schedule recipes, repo-native cron — `parker-system/system/schedules.md`) are stamped from `templates/brand-routines/`. Together with `.claude/skills/` this is what makes the brain self-running the moment it's cloned.
- `parker-system/` — the rest of the factory methodology, copied in during Phase 0 so the brain is self-contained and can refresh, rebuild, and reason on its own with no dependency on the factory at runtime. Three layers under it:
  - `parker-system/prompts/` — every generating prompt, the exact ones that built the brain. This is what lets a refresh re-run a doc's *own* generating prompt instead of improvising, and what lets the team rebuild or extend any doc later. Without it the refresh routine has nothing to run.
  - `parker-system/creative-strategy-context/` — the craft knowledge layer: the method docs, the expert-insights, parker-taste, and ad-formats the analysis reasons through.
  - `parker-system/system/` — the runtime system docs the brain runs on: the tool inventory, the operating model, and the open-loops / refresh / schedules mechanisms. This is the subset of the factory's `system/` the brain actually reads at runtime; the factory-internal docs and the product-architecture map stay behind (a standalone brain's situational awareness is `CLAUDE.md`'s "## The map" plus the vault index in `brand-profile-narrative.md`, not the factory system map).
- `prompts-run-log/` — the build log.
- `BUILD-STATUS.md` — the live build ledger, at root only while the build runs; archived into `prompts-run-log/` at completion (see the status file section below).
- `parker_config.json` — the cross-session resume anchor for setup tracking; written at the end of Phase 0 step 2 (see Setup Status Tracking below).

### The path map — factory path to flat path

- `z-brands/[brand]/brand-profile.md` writes to `sub-context-docs/brand-profile-narrative.md`.
- `z-brands/[brand]/sub-context-docs/*.md` writes to `sub-context-docs/*.md`.
- `z-brands/[brand]/personas/sources/*.md` writes to `source-pulls/*.md`.
- `z-brands/[brand]/personas/*.md` writes to `personas/*.md`.
- `z-brands/[brand]/personas/voice-of-customer/voice-of-customer.md` writes to `personas/voice-of-customer/voice-of-customer.md`.
- `z-brands/[brand]/personas/voice-of-customer/voc-corpus-profile.md` writes to `personas/voice-of-customer/voc-corpus-profile.md`.
- `z-brands/[brand]/personas/voice-of-customer/phrases/[name].md` writes to a flat `personas/voice-of-customer/voc-[name].md`, one file per category, no `phrases/` subfolder.
- `z-brands/[brand]/competitors/[id]/…` writes to `competitors/[id]/…`, same shape, and the roster writes to `competitors/_competitive-set.md`.
- Every audit the cadence prompts produce writes to `audits/[YYYY-MM]/` for monthly cuts and `audits/[YYYY-Q]/` for quarterly cuts; the external cuts write to `audits/[YYYY-MM]/external/` and `audits/[YYYY-Q]/external/`. The newest audit is the account's present tense.
- `gaps-opportunities-inspo.md` writes to the current quarter's `audits/[YYYY-Q]/gaps-opportunities-inspo.md`.
- `z-brands/[brand]/strategy/*.md` writes to `strategy/*.md`.
- `z-brands/[brand]/idea-bank/…` and `z-brands/[brand]/briefs/…` write to `idea-bank/…` and `briefs/…`.
- `z-brands/[brand]/{open-loops,hypotheses,validations,re-validations}/…` write to the same folders at root, single bucket, with no org-wide-versus-team split, because a standalone brand brain has no team split.
- `z-brands/[brand]/running-notes/…` collapses to `running-notes/brand-notes-from-org.md` and `running-notes/missing-context.md`.

## Run order and dependencies — read this before executing

The phases below are the sequence, but what actually governs the build is the dependency graph, not a rigid line. Run independent work in parallel; respect the hard blocks (`←` means "blocked on, do not start until that exists").

**Phase 1 — five independent branches, then their synthesis nodes.** Each branch reads raw sources through Parker MCP and depends on nothing but Phase 0, so the five run in parallel:
- **A. Brand foundation slices** — every prompt in `prompts/brand-profile/` *except* `_foundations.md` (embedded scaffold) and `brand-profile-narrative.md` (synthesis, below). Independent of each other, with one ordering note: the account-synthesis slices `ad-account-evaluation`, `performance-targets-and-metrics`, and `organic-channels-inventory` are *synthesis-of-audit* one-pagers, so they are blocked on branch E below.
- **B. Competitor profiles** — identify the set first, then each rival's `prompts/competitor-profile/` slices (independent per rival).
- **C. Persona source pulls** — the eight source prompts in `prompts/personas/`: ad-account, ad-comments, customer-reviews, other-reviews, post-purchase-surveys, reddit, brand-reputation, brand-self-echo-detection.
- **D. VoC extractions** — `voc-corpus-profile` + the ten `voc-*` slices in `prompts/voice-of-customer/`.
- **E. Internal audit baseline** — the audit cadence layer, run once now as the **t0 baseline** that the cadence then re-runs from. Reads the ad account (and reviews/organic) through Parker MCP; independent of A–D. Run **every** audit prompt as its first pass: the quarterly cuts (`audits-quarterly/90-day-creative-strategy-audit` — the anchor — plus `90-day-performance-audit`, `90-day-diversity-audit`, `customer-review-audit`, `quarterly-whitespace-analysis`), the monthly cuts (`audits-monthly/monthly-hook-audit`, `monthly-performance-report`, `monthly-organic-tiktok-audit`, `monthly-tiktok-mining`), the first `audits-biweekly/biweekly-iterations-report` + `audits-weekly/weekly-performance-snapshot`, **and the external/competitor cuts** (`audits-quarterly-external/*` — `90-day-creative-strategy-audit-external`, `90-day-performance-audit-external`, `90-day-diversity-audit-external`, `single-competitor-ad-analysis` — and `audits-monthly-external/*` — `monthly-creative-landscape`, `monthly-top-impressions-report`), which read the tracked competitor set built in branch B and write to `audits/[YYYY-Q]/external/` and `audits/[YYYY-MM]/external/`. The external cuts depend on branch B's competitor set existing; everything else here depends only on the connected account. The whole audit family is generated at the baseline — none of it is deferred to "first scheduled run." Why this is here and not "ongoing": the foundation's account one-pagers are *defined as syntheses of these audits*, so the audits must exist before the one-pagers can synthesize anything — building the one-pager first is what leaves it saying "no audit packet existed, this is the baseline." Generate the baseline now; the schedule re-runs each audit on its named interval from its own `generated_on`.

Then the synthesis nodes, each blocked on its branch:
- `ad-account-evaluation` ← branch E (anchored on the 90-day-creative-strategy audit; folds in the performance/diversity/hook cuts); `performance-targets-and-metrics` and `organic-channels-inventory` likewise fold in their matching cuts.
- `brand-profile-narrative` ← all of A (which now includes the audit-synthesized slices).
- `competitor-snapshot` (per rival) ← that rival's slices; `working-thesis-synthesis` ← all snapshots.
- `personas-profile` ← all of C; then `persona-voice-library`, `lifecycle-journey-maps`, `cross-persona-bias-notes` ← `personas-profile`.
- `voice-of-customer-assembly` ← all of D.
- `gaps-opportunities-inspo` ← A + B.
- `open-loops-roll-up` ← **everything above** (it consolidates every doc's open loops). Always the last Phase-1 step and the bridge into Phase 2.

**Phase 2 — four inputs in parallel, then the roadmap, then the gate.**
- `persona-strategy-input`, `product-priority`, `messaging-strategy-input`, `creator-talent-strategy-input` each read Phase-1 outputs → run in parallel.
- `strategic-roadmap` ← all four inputs.
- **Gate:** roadmap approved (or the user is already driving their own direction) before Phase 3.

**Phase 3 — strict line.** `brand-idea-bank` (capture) → `idea-evaluation` ← idea-bank + approved roadmap → `brief-creation` ← the shortlist.

**Never run as a build step** (these are *included* by other prompts or are global setup, never executed standalone in a brand build):
- The embedded blocks: `_expertise-core-block`, `_parker-voice-block`, `_open-loops-core-block`, `_notion-ai-tagging-and-foundational-context`, and `brand-profile/_foundations`.
- `prompts/global-databases/*` — global product setup, not part of a brand cold start.

**Baseline at cold start, then ongoing** (build the first run now; the schedule re-runs it after):
- `prompts/audits-*` (weekly → quarterly, plus the external cuts) — run once as the Phase-1 branch E baseline so the account one-pagers have a packet to synthesize, then refreshed on each audit's named interval from its `generated_on` (see `system/refresh-cadence.md`). The recurring re-runs are what the refresh-sweep schedule drives; only the *re-runs* are ongoing, the *first* run is part of the build.

**Ongoing, not cold start** (these run on a brain that already exists — the brain runs them itself, do not run them during onboarding):
- The open-loops advance/validate skills, and self-improvement + dreaming.

## How to delegate a prompt — the fidelity contract

This build may fan out: any prompt can run in its own subagent, and independent branches *should* run in parallel. But a subagent is handed a **pointer to the prompt, never a retelling of it.** This is the rule that keeps the build honest. The failure mode it exists to kill is silent shortening: the orchestrator, fanning out, describes a prompt in its own words — "run the brand identity analysis, focus on positioning and pricing, write it here" — and the agent, never having opened the file, executes that paraphrase instead of the prompt. The paraphrase always drops what lives *inside* the file: the locked section structure, the embedded blocks (`_parker-voice-block`, `_open-loops-core-block`, `_expertise-core-block`, `_foundations`), the expertise-routing loads, the claim labels, the open-loops tail. A shortened prompt under-retrieves and under-delivers, and the output drifts to a generic guess.

So the orchestrator never summarizes, paraphrases, condenses, or restructures a prompt's instructions into an agent's task. It passes only what the file cannot carry itself: the brand and `brand_id`, the flat output path, and the paths of any upstream docs the prompt may read. The agent's task message takes this shape and no more:

> "Run the prompt at `parker-system/prompts/<path>.md`. Open it and read it in full, including every block it embeds and the entry context it names, before you write anything. Execute it exactly as written — its section structure, its claim labels, the expertise docs it tells you to load, its denominators, and its open-loops tail are all mandatory; none may be skipped, shortened, or rewritten. Brand: `<name>`, `brand_id`: `<id>`. Write the output to `<flat path>`. You may read these upstream docs: `<paths>`."

The prompt is run from the brain's own `parker-system/prompts/`, not the factory clone — Phase 0 shipped it there, and the same in-brain prompt is what every later refresh re-runs. Its methodology references (`parker-system/creative-strategy-context/`, `parker-system/system/`) resolve against the bundle shipped alongside it.

If a prompt feels small enough that paraphrasing it seems harmless, that is precisely the case where the paraphrase still strips the embedded blocks — pass the pointer anyway. The orchestrator's job is routing and sequencing, never re-authoring the prompt.

## Review pass — did the output follow the prompt

Every prompt's output gets a review before any node that depends on it runs. After the output exists, spawn a **separate review subagent** — not the agent that wrote it. Give it two paths only: the original prompt file and the produced output. Its single job is fidelity to the prompt; it does not redo the work, pull sources, or judge whether the strategy is *right*. It opens the prompt, derives the prompt's own requirements, and verifies the output against them:

- every required section the prompt specifies is present, in the prompt's structure — none dropped or replaced with a thinner generic version;
- every claim carries a stated / inferred / verified / data-limited label;
- counts carry their denominators; no invented, smoothed, or filled numbers;
- the open-loops tail is present and in the canonical four-part form;
- `generated_on` and `refresh_by` are stamped;
- the sign-off lines for the method docs the prompt required to be loaded are present — the proof the expertise was actually read, not skipped;
- the output reads as built from the full prompt, not a paraphrase of it — whole missing sections are the tell that the prompt was shortened on the way in.

It returns a verdict: **pass**, or **fail** with each gap quoted against the part of the prompt it violates. On a fail, the orchestrator **re-runs the prompt once automatically** — full pointer per the fidelity contract above, with the review's named gaps appended as what to fix — then reviews the re-run. If the re-run also fails, stop escalating: surface the doc and its remaining gaps to the user rather than looping. Either way, log every verdict (pass, re-run, or surfaced) in `prompts-run-log/` so the build carries its own quality record. A doc that has not passed review is not consumed by a downstream synthesis node; the review gates the hand-off, not just the file.

This pass is also the standing detector for the shortening problem: if outputs keep failing on "whole sections missing," the orchestrator is still paraphrasing prompts somewhere — tighten the fidelity contract before continuing.

## Open by orienting them — what this is and what's about to happen

The moment the user kicks this off — they paste in a "clone this repo" instruction, or just say "set up my brand" — stop and orient them before you touch anything. Assume they have little idea what this is. A person who doesn't know what's about to happen to their account, their data, or their time does not feel safe, and making this feel easy and safe is half the job. So open warm and plain, in your own words, covering four things and no more:

- **What this is.** They're about to build a *brand brain* — a private, living workspace that reads their actual marketing data (their ad account, their reviews, their customers' own words, their competitors) and turns it into a senior strategist's worth of context that Parker can then think with. Not a chatbot and not a template: their own brand's intelligence, in their own repo, that they own and keep.

- **What's about to happen, in three phases.** Give the trip a shape so nothing feels like a black box. First Parker **learns the brand cold** — the audit, reading the account, reviews, personas, and competitors. Then Parker **decides a point of view** — the strategy: who to target, what to say, what to make. Then Parker **makes the work** — ideas and briefs built off that strategy. Each phase builds on the one before, and they'll watch it happen.

- **Where they're in control.** Name the moments they'll be asked to choose or confirm, so it's obvious nothing big happens without them: the go-ahead to start at all, what to do if the data connection isn't ready, which competitors to use, and the big one — **the strategy roadmap review, at the moment they chose in the intake.** Tell them they can pause, ask questions, or change direction at any point.

- **When it becomes theirs to use.** They get a real, usable brain at the end, saved to their own GitHub, that they open and talk to in plain language — and you'll walk them through exactly how when you get there. It arrives running, too: the standing routines (the weekly refresh, the nightly dreaming, the idea cycle) come armed as part of the build, and turning any of them down or off is one command once they're in.

Keep it short and human — a friendly map of the trip, not a wall of text or a contract. The point is that before a single thing runs, they understand what they're setting up, that it's safe, and that they're the one driving. Then move to the heads-up below.

## Before you run it — the heads-up and the go-ahead

Quick, honest heads-up before we dive in, then a real go/no-go. Building a brand brain is a *big* job — Parker reads the whole account, the reviews, the comments, the organic, and the competitors, and writes the entire vault from scratch. All that reading and writing burns a fair amount of usage. No way around it: good context isn't free.

So here's the deal, plainly and with love: we **strongly recommend running this on a Max or 20x Max plan.** On a lighter plan it can absolutely still run — it just might chew through your whole five-hour usage window, and on a heavy build maybe make a dent in the week. We'd rather you know that going in than hit a wall halfway through a persona.

And honestly? It's worth it. It costs what it costs because Parker is doing a real strategist's homework — reading everything, writing it all down, connecting the dots — and that depth is the whole point. It's what takes the AI from "helpful chatbot" to "the strategist who actually knows your brand."

Make this a gate, not a footnote: say the above in your own warm words, then **ask the user to confirm they want to kick off the full build now — through the popup question form, per the standing rule.** If they'd rather wait, switch plans first, or start smaller, that's a perfectly fine answer — offer to pick it back up whenever. Do not start Phase 0 until they've said go.

## Setup Status Tracking

Use the `update_parker_brain_setup_status` tool (Parker MCP) at every phase boundary. This is the **product-side telemetry** — it powers the team's monitoring page, so the user can see build progress without watching the terminal. It complements, never replaces, the `BUILD-STATUS.md` file below: the status file is the in-repo user-facing ledger and the resume checkpoint; this tool is the hosted view of the same journey. On a resume, the two anchors work together — `parker_config.json` carries the `run_id` for the start call, and the status file's ledger says exactly which prompts are done.

### Start

On resume, call as soon as the brand repo is open. On a fresh run, call only after Phase 0 creates the repo and locks `brand_id` (steps 1–2 below).

Check for `parker_config.json` in the brand repo root.

- **File exists** → pass its `run_id`. This is the only resume signal.
- **No file** → omit `run_id`. A new run is always created.

```
update_parker_brain_setup_status(mode: "start", brand_id, run_id?)
```

- `resumed: false` → fresh run, proceed.
- `resumed: true` → skip phases ≤ `last_completed_phase_index`. Any phase stuck mid-run has been auto-reset to `failed` — re-run it.

Then write and commit `parker_config.json` to the repo root with the returned `run_id`. This is the cross-session resume anchor — if it is not written before the session ends, the next session cannot resume and will start a new run.

```json
{
  "run_id": "",
  "brand_id": "",
  "brand_name": "",
  "github_repo_url": "",
  "parker_brain_version": "",
  "created_at": ""
}
```

### Each Phase — call twice

```
update_parker_brain_setup_status(mode: "update_phase", brand_id, run_id,
  phase_name, phase_index, phase_status: "in_progress" | "completed" | "failed",
  metadata?, errors?)
```

- `phase_index` starts at 1, increments by 1. **Never reuse an index — upsert will silently overwrite the previous phase record.**
- Use phase names that match the runner's own section and branch names so tracking is consistent with the build log. Examples: `"Phase 0 — Repo & Scaffold"`, `"Phase 1A — Brand Foundation"`, `"Phase 1B — Competitor Profiles"`, `"Phase 1C — Persona Source Pulls"`, `"Phase 1D — Voice of Customer"`, `"Phase 1E — Audit Baseline"`, `"Phase 1 — Synthesis"`, `"Phase 2 — Strategy Inputs"`, `"Phase 2 — Strategic Roadmap"`, `"Phase 3 — Idea Bank"`, `"Phase 3 — Idea Evaluation"`, `"Phase 3 — Brief Creation"`, `"Stamp Operating Contract"`, `"Verify Build"`, `"Save to GitHub"`, `"Onboarding"`. Add or split as the actual work requires.
- To retry a failed phase, call again with the same index and `phase_status: "in_progress"`.
- **Include all errors even if the phase ultimately completed** — non-fatal errors matter for auditing.

**Error shape:**

```json
{
  "timestamp": "",
  "type": "tool_call_failed | mcp_error | github_error | network_error | unknown",
  "tool": "",
  "message": "",
  "raw": {},
  "attempt": 1,
  "fatal": false
}
```

### Done

```
update_parker_brain_setup_status(mode: "complete", brand_id, run_id,
  run_status: "completed" | "failed", github_repo_url?, errors?)
```

**Always call this at the end, success or failure.** If skipped, the run stays `in_progress` forever and the admin sees it as incomplete.

## The build status file — one page the user watches, one record the build resumes from

A full build is dozens of prompt runs over hours. The person who kicked it off cannot follow that in a terminal transcript, and they should not have to: the honest answer to "where are we and how much is left" must live in one file, always current, written for them. Create **`BUILD-STATUS.md`** at the brand repo root during the Phase 0 scaffold and treat keeping it true as part of every step, as binding as writing the outputs themselves.

What it holds, top to bottom:

- **The header:** brand, when the build started, the current phase, and one plain-language line on what is happening right now. If the build is waiting on the user for anything, say so here in bold, first — this is the single most important state to surface.
- **The scoreboard:** each phase and branch with a done / total count (for example "Personas: 9 of 12"), so progress is legible at a glance without reading anything else.
- **The full prompt ledger:** every prompt the build will run, grouped by branch, each marked `pending`, `running`, `done`, or `blocked` (with one line on why). This ledger is the checkpoint — see resuming, below.
- **Needs attention:** anything blocked or failed that will need the user or a retry, each with one plain line.
- **What happens next**, in one or two lines.

Update it at every state change: a prompt starts, finishes, fails, or gets blocked; a phase opens or closes; the build starts waiting on the user. Rewrite the file in place — it is a live view, not an append log (`prompts-run-log/` keeps the permanent provenance). When the build completes, move it into `prompts-run-log/` as the build's final record so the repo root stays clean.

**When the build needs the user, ask through the popup question form — always.** This is the rule that keeps a build from stalling silently: the popup form is what fires a notification on the user's machine, and a question typed into the chat fires nothing, so a user who stepped away has no way to know the build is waiting. Every ask goes through the form — the intake questions, the GitHub and comfort questions, the roadmap gate, a blocker that needs their call — with real options, the form's free-text answer for anything open, and a skip or proceed-without choice so nothing hard-blocks. Mark the wait in `BUILD-STATUS.md` at the same time. A question asked outside the form is a question the user may never see.

**The narration contract.** The status file is what frees the chat from noise. Speak in chat at the moments that deserve a person's attention: the welcome and intake, a phase opening or closing (a few plain sentences on what just got built and what starts now), anything that needs their input or approval, a blocker that will not resolve itself, and the finish. Everything else — per-prompt progress, review verdicts, retries — goes to `BUILD-STATUS.md` and the run log, not the chat. During the long stretches, tell the user once: the build is running, `BUILD-STATUS.md` is the page to watch, and you will speak up when something needs them or a phase turns over. Teaching stays in the phase-boundary moments, where a person is actually listening — a wall of step-by-step narration teaches nothing, because nobody reads it.

**The failure policy.** A build that halts silently on one bad call is how a one-hour setup becomes a four-day one. When a tool call or prompt run fails on something transient — a timeout, an empty pull, an API error — retry it once before anything else. A review fail already re-runs once per the review pass above. If something still fails after its retry, mark it `blocked` in the status file with a plain reason, keep building everything that does not depend on it, and collect the blocked items to raise with the user at the next natural pause (a phase boundary or the finish) — never sit waiting mid-build on something the user has not been told about, and never let one blocked doc stop the sixty that do not need it.

**Resuming an interrupted build.** Sessions die, timeouts happen, people close laptops. The prompt ledger makes recovery cheap: on any fresh session where the brand repo has a `BUILD-STATUS.md` that is not marked complete, offer to resume before anything else. To resume, call `update_parker_brain_setup_status(mode: "start")` with the `run_id` from `parker_config.json` (see Setup Status Tracking above), then reconcile the ledger against the repo — confirm each `done` prompt's output actually exists on disk (and passed review per the run log), demote anything missing back to `pending` — then continue from the first pending item, in dependency order, updating the ledger as you go. The user should never rebuild finished work, and never have to reconstruct where a dead session left off.

## Phase 0 — new repo, connect, scaffold, intake, ship the craft, read in

Do all of this before running a single content prompt.

1. **Stand up the brand's own repository — do not build inside this `parker-brain` clone.** This product brain is the read-only factory teams clone; the brand brain is a **separate, standalone repo for that brand.** Before any of the git mechanics, gauge their GitHub comfort and meet them there: ask how familiar they are with GitHub and git. If they are new to it, slow down and explain in plain terms what a repository is, what cloning means, and why the brand gets its own repo separate from this one, and offer to walk them through each step rather than assuming they can follow a command; if they are fluent, move briskly and skip the explanation. Then confirm with the user where it should live, initialize a new git repo (a new GitHub repo for the brand) distinct from `parker-brain`, and build everything below inside it. Every brand output is committed there, never back into the cloned product brain. The flat standalone layout above is the shape of this new repo.
   - **If they're starting from zero on GitHub**, walk these in order and explain each as you go, rather than assuming any of it is obvious: (1) if they don't have a GitHub account, have them create a free one at github.com; (2) make sure the GitHub CLI is available and signed in — run `gh auth login` and have them follow the browser prompt, since that sign-in is what lets you create and push repos on their behalf; (3) once signed in, *you* create the brand repo for them with `gh repo create <brand>-brain --private`, rather than making them click through the web UI. Default the repo to **private** unless they say otherwise — it holds their brand's data. If they already use GitHub day to day, skip the explanation and go straight to creating the repo.
2. **Connect and confirm the brand.** Parker MCP must be reachable. Call `get_available_brands`, confirm the right brand with the user, and lock its brand_id. Several brands share a name across orgs, so the id is the anchor for every pull that follows. **If the MCP is not connected or a test fails** — no brand list, pulls error or return empty — don't silently push on, and don't hard-stop either: make it the user's call, as a required choice you wait on, asked through the popup question form. Explain plainly that without the Parker MCP, Parker can't reach the live source — the ad account, organic socials, reviews, surveys, the competitor library — so the build would lean on general knowledge instead of their real data, and **it will not be nearly as good.** Then give them three options and wait for their pick: **(a) pause** here while they set up or connect the MCP, and come back to it; **(b) connect it now**, and you re-run the test and continue; or **(c) continue without it**, understanding the brain will be thin and every claim data-limited until the real data is wired in later. This is a gate — do not proceed past it on your own judgment. The **Parker MCP is the one connection that carries all of it** and is the recommended path, though independent platform exports can feed the same evidence more manually; the full reminder is in `system/parker-tools.md`. Whichever they pick, never fabricate data to fill the gap.
   - **Test the tools, don't just ping them.** Reachable is not the same as operable. Run a quick operability check — a light pull from each major surface (ads, customer reviews, ad comments, organic social, post-purchase surveys, and the competitor library) — to confirm each actually returns data, not merely that the connection is up. A surface that errors or comes back empty now is one that would silently hole the build later, so name it to the user plainly and log it in `running-notes/missing-context.md`. As you run each test, explain in plain language what that tool reaches and why it matters, since the person watching likely has no idea what Parker can see — this is the first place they learn what their brain is made of.
   - **Decide the competitive set with the user — a real choice, not an assumption.** While you are in the tools, query the available database of brands Parker can reach. Parker *can* pick a competitive set from that database on its own, but that's our selection from what happens to be available, not necessarily who the user would name themselves. So preface it honestly and let them choose (through the popup question form): tell them that, left alone, Parker will choose competitors from the brands in our database, and ask whether they would rather **(a) go into the Parker app and add the specific competitors they care about** — the sharper option, since they know their real rivals — or **(b) let Parker pick the set from what's in our database** and move on. Wait for their pick. If they choose to add their own, pause the competitor branch (B below) until they've done it; if they're fine with Parker's selection, note which brands were chosen and why so the choice is visible in the build. Explain what a competitor analysis gives them either way, so the decision feels worth making. The intake in step 4 also captures who they consider real competitors versus inspiration; together these seed `competitors/_competitive-set.md`.
3. **Scaffold the flat repo.** Create the top-level tree above inside the brand's repo, including `running-notes/`, so the intake in the next step has a home for its answers. Seed `open-loops/`, `hypotheses/`, `validations/`, `re-validations/`, `dreaming/`, `schedules/`, and `workflows/` with their README scaffolds so the living layers have a home before they fill; `personas/sources/` needs no README. Create `BUILD-STATUS.md` now too, per the status file section above, with the full prompt ledger laid out as `pending` — and show the user where it lives: this is the one page that always says where the build is, what is done, and what is left, so they never have to scroll the chat to find out.
4. **Run the brand intake — capture what only they can tell you (optional, never a gate).** Now that the brand is connected and the repo is scaffolded with somewhere to store the answers, and before the slow craft copy in the next step, capture the short list of things Parker genuinely cannot figure out on its own. Everything Parker *can* observe — what's running, what converts, who actually buys, what customers say — it discovers from the data and should never ask for. This intake is only the un-observable: the brand's own intent, definitions, and rules. It is **optional and skippable.** If the user would rather just build, capture nothing, log the unanswered items to `running-notes/missing-context.md`, and let every prompt run as normal. The intake makes the build sharper; it is never a prerequisite.

   **Just begin the full intake — do not open with a meta-choice about how much of it to run.** There is no "quick version vs full version vs skip" menu; that forces them to pick a mode before they have answered anything, which is a decision they do not want. Lead in naturally and present the first card. The opt-out is always there without a menu: every single question is skippable, and they can say "just build it" at any point to stop. The default is the complete designed set; if a choice over depth ever is surfaced anyway, the full intake is the default and the recommendation, never a trimmed quick one.

   Make it easy and personal, the same way the rest of onboarding is calibrated. Lead with what you can already see from the account so each question is framed off real context, prefer a quick pick over an open question, and let them paste a link instead of typing. **Work through the whole set, not just a couple.** It is short and most are a quick pick, so move briskly: batching a few related questions at a time is good, better than one ping each, but cover all of them rather than stopping after the first handful. Calibration changes how much you *explain* a question, not which questions you ask: every item here is something only they can tell you, so none is a "basic" to skip for a fluent user. If they don't know an answer or don't want to give one, skip that single item and log it; let them tap out of the rest if they choose, but don't quietly drop half the list on your own. Write answers to the running-notes homes below, creating those files from their factory templates (`templates/brand-rules-template.md`, `templates/success-definition-template.md`) if the scaffold has not yet.

   **Move through it as one flowing conversation with a thread, not a random grab-bag.** Go in the order below, which builds from the big picture down to the details: first what success even means for this brand, then how they measure it, then how the account and the work are organized, then the market, then the close. Group each cluster into a single batch, name the thread as you move between clusters so it reads as a logical progression. If they defer an item ("I'll share it later"), note it as pending in `missing-context.md` and move on — do not re-ask the same item later in the session.

   **On format: every question goes through the popup question form. No exceptions, none as plain chat.** The reason is mechanical, not aesthetic: the popup form is what fires a notification on the user's machine — a question typed into the chat fires nothing, so a user who stepped away never learns the build is waiting on them, and the whole thing stalls silently. So every ask, including the open-ended ones, arrives as a form. Batch each cluster into one popup (a few related questions per card), give every question real options plus its built-in free-text answer, and always include a skip choice so nothing blocks. For the items that want a paste — the naming-convention doc, the brief template — the form asks first ("I'll paste it next" / "there isn't one" / "skip"), and only after they choose to paste do you receive it in chat; the form got their attention, the paste follows while they're present. Same for the gap question: ask it as a form with the free-text answer carrying their words. Do not switch to an open prose list of questions at any point; a question outside the form is a question the user may never see.

   **First, what success means for this brand** — the lens every later read runs through:
   - **Their main business objective right now** — scale acquisition, improve efficiency, launch a product, hit a revenue target, or improve retention. → `running-notes/success-definition.md`
   - **Primary campaign objective** — Sales, Leads, Traffic, Awareness, or App installs. → `running-notes/brand-rules.md`
   - **North-star metric, and whether hitting its goal is the whole definition of success** — ROAS, CPA, MER, CVR, AOV, or another. → `running-notes/brand-rules.md`
   - **The secondary metrics they still weigh.** → `running-notes/brand-rules.md`
   - **When two ads in one ad set diverge on spend, does higher spend win or do they weigh efficiency too.** → `running-notes/brand-rules.md`
   - **Where they read performance — in-platform numbers or a third-party tool** such as Northbeam or Triple Whale. → `running-notes/brand-rules.md`

   **Then, how the account and the work are organized:**
   - **Ad naming convention** — have them walk it through, or paste a link to the spreadsheet. → `running-notes/brand-rules.md`
   - **Brief template** — share it, saved verbatim to `briefs/_brief-template.md` so every brief the brain writes matches their format.

   **Then, the market and the economics:**
   - **Who they consider real competitors, plus any aspirational brands.** → seeds `competitors/_competitive-set.md`
   - **Optional, only if handy — unit economics:** what a customer is worth, rough gross margin, LTV or payback window, and the max CPA they will tolerate. It sharpens every performance read. → `running-notes/brand-rules.md`

   **Then one build logistics question, so the build never has to stop and wait for them:** partway through, Parker drafts the strategic roadmap — the direction everything after it builds on. Do they want to pause there and review it before the build continues, or should the build keep going and present the roadmap for their review at the end? Default to reviewing at the end: the pause is the right call only for someone who plans to watch the build live, and most people will not. Record the answer in `BUILD-STATUS.md`; the Phase 2 gate honors it.

   **Last, the gap question** — once the structured set is done: based on everything they told you, what do they still feel you're missing, and what is the one thing a smart outsider always gets wrong about this brand. → `running-notes/missing-context.md`

   Whatever is captured is *stated* brand input, not verified fact. The targeted generating prompts carry the `brand-intake` block, which tells them to honor the brand's intent and definitions, treat descriptive claims as stated until the data confirms them, and surface conflicts rather than swallowing them. Anything skipped stays an open question in `missing-context.md`, never a blocker.
5. **Ship the factory method into the brand repo — the skills into `.claude/skills/` and the rest into `parker-system/`.** Copy the whole factory method in so the brain is self-contained and references nothing in the factory at runtime. No prompt does this; the runner does. Two destinations:

   **First, the skills — into `.claude/skills/`.** This is the only directory Claude Code loads skills from; a skill copied anywhere else (a top-level `skills/`, or under `parker-system/`) is inert and a clone never registers it. Copy the **entire** factory craft-skill set from the factory's own `.claude/skills/` into the brand brain's `.claude/skills/`, *alongside* the routine bundle stamped from `templates/brand-routines/` — every craft skill, not a curated subset: the creative-execution skills (`scriptwriting`, `hooks`, `headlines`, `iterations`, `ad-account-analysis`, `ai-ad-generation`), the open-loops pipeline (`open-loops-advance`, `open-loops-validate`), idea-bank maintenance (`brand-idea-bank-maintenance`), and the living-loop / intake skills (`improve-system`, `self-improvement-intake`, `expert-signal-intake`). The few factory-maintenance skills (`propagate-craft`, `update-parker-skill`) come along too and sit inert in a brand brain, the same way the factory-orchestration prompts do — don't curate them out. **One name collision to respect:** the factory craft set and the routine bundle both define a `dream` skill; the routine `dream` (the scheduled dreaming run, the brain's canonical one) wins, so do not overwrite it with the craft `dream`. After this, the brand `CLAUDE.md` routes every execution-shaped task through `.claude/skills/<skill>/`, and on clone they all load after the workspace-trust prompt. (Skills reference each other and the craft knowledge by paths that resolve the same in the factory and the brain, so a straight copy is all it takes.)

   **Then `parker-system/`** — create it and copy in the other three layers:
   - **Prompts:** copy the factory `prompts/` tree to `parker-system/prompts/`. This is the change that makes a brain refreshable: the exact generating prompts now live in the brain, so the refresh routine re-runs a doc's *own* prompt instead of improvising, and the team can rebuild or extend any doc later. Every prompt the build runs is run from here, not from the factory clone (see the fidelity contract). The factory-only orchestration files come along but stay inert in a brain: `parker-system/prompts/onboarding-runner.md` and `prompts/README.md` describe the factory build, and `prompts/global-databases/*` is global product setup — none of these are run inside a standing brain.
   - **Craft knowledge:** copy the full `global/knowledge/creative-strategy/` tree to `parker-system/creative-strategy-context/`. After the copy, the expertise-core block's `parker-system/creative-strategy-context/expertise-routing.md` reference resolves inside the brand repo, and so does every method-doc reference the normalized prompts carry.
   - **System:** copy the **runtime** system docs from the product brain's `system/` to `parker-system/system/` — `parker-tools.md`, `three-phase-operating-model.md`, `open-loops-system.md`, `refresh-cadence.md`, `schedules.md`, and `growing-the-brain.md`. These are the docs the brain reads to operate: what it can pull, how it works a brand, the loop / refresh / schedule mechanisms, and how the brain grows new surfaces as the org connects more of itself. **Leave the factory-internal docs behind** — `master-prompt-review.md`, `system-of-records.md`, `master-file-structure.md`, `attribution-principle.md` — they are for building and maintaining the factory, not running the brain (the attribution rules the brain needs are already inlined in `CLAUDE.md`). **Do not ship `parker-system-map.md`** either: it maps the factory/product architecture (teams, z-brands, prompts, the shared foundation) and would misdescribe a standalone single-brand brain. The brain's own situational awareness is `CLAUDE.md`'s "## The map" plus the always-loaded vault index in `brand-profile-narrative.md`. After the copy, rewrite any `global/knowledge/creative-strategy/` path inside the shipped system docs to `parker-system/creative-strategy-context/` so their cross-references resolve in the brain.

   The prompts ship already normalized to `parker-system/` paths — they reference `parker-system/creative-strategy-context/`, `parker-system/system/`, and `parker-system/prompts/` rather than factory paths, so a copy is all that's needed and the references resolve as-is. The brand data the build produces (sub-context-docs, personas, audits, strategy, the loop pipeline, running-notes) stays flat at the repo root per the path map above; the factory method lives under `parker-system/`, with the executable `skills/` kept as its own top-level folder beside it.
6. **Read the entry context.** Open `CLAUDE.md`, `parker-system/system/three-phase-operating-model.md`, `parker-system/system/open-loops-system.md`, and `parker-system/creative-strategy-context/expertise-routing.md` — all now present in the brand repo from step 5. The routing map names which method docs each prompt must load before it analyzes.
7. **Open the build log.** Start `prompts-run-log/[YYYY-MM-DD]-full-buildout.md` and record each prompt as it runs, with the source pulled, the date, and its review verdict, so the brain carries its own provenance. The log is the permanent record; `BUILD-STATUS.md` is the live view — the log accumulates, the status file stays current.

## Phase 1 — audit

Know the brand cold before planning. Run the four branches and their synthesis nodes per the dependency map above, writing each output to its flat path:

1. The internal audit baseline (branch E): the quarterly cuts (the 90-day creative-strategy audit anchor, plus performance, diversity, customer-review, and whitespace), the monthly cuts (hook audit, performance report, organic-TikTok, TikTok mining), and the first biweekly iterations report + weekly snapshot, each written to its date bucket under `audits/`. Run this before the account one-pagers, which synthesize it.
2. The brand-profile sub-context slices — with the account one-pagers (`ad-account-evaluation`, `performance-targets-and-metrics`, `organic-channels-inventory`) synthesizing the branch-E audits — then `brand-profile-narrative` to synthesize them all.
3. The competitor set and each competitor's profile, rolled up per rival, plus `_competitive-set.md` and the cross-competitor working thesis.
4. The persona source pulls, then `personas-profile`, the voice library, lifecycle maps, and bias notes.
5. The voice-of-customer corpus profile, the extraction slices, and the assembly.
6. `gaps-opportunities-inspo` across the foundation and competitors.
7. `open-loops-roll-up` to consolidate, grade, tier, and route every doc's loops into one prioritized agenda.

Every output marks each claim stated, inferred, verified, or data-limited, carries denominators on counts, ends with open loops, and stamps `generated_on` and `refresh_by`.

## Phase 2 — decide the strategy

Run the four strategy inputs first, each resolving its territory's Phase-1 evidence into a committed recommendation, then synthesize:

1. `persona-strategy-input` — the WHO.
2. `product-priority` — the WHAT.
3. `messaging-strategy-input` — what to lead with saying.
4. `creator-talent-strategy-input` — who should be on camera.
5. `strategic-roadmap` — synthesizes the four into a diagnosis and the top three priorities in order.

**The gate.** When Parker is driving the strategy, the roadmap needs the user's eyes: approve, adjust, or reject is what turns the call into committed direction. **When it happens is theirs, decided back in the intake's logistics question.** If they chose to pause here, stop, present the roadmap, and ask for the approve-adjust-reject call **through the popup question form** (so they actually get notified the build is waiting) — and mark the wait plainly in `BUILD-STATUS.md` so anyone glancing at it sees the build is on them, not stuck. If they chose to keep building (the default), do not stop: proceed into Phase 3 with the roadmap as the working direction, mark it "drafted, awaiting review" in the status file, and make its review the first item of the hand-off at the end — with the honest caveat there that the ideas and briefs were built on a roadmap they have not yet blessed, so an adjustment to it may re-rank them. Hold the gate lightly per the operating model's governing rule either way: a co-piloting user who already knows their direction does not have to formally approve a roadmap before Parker helps them execute. The roadmap is the artifact when Parker is asked to set the strategy, not a permission slip the user has to sign before Parker will write a script.

## Phase 3 — make the work

Only once the roadmap is the agreed direction. The judgment runs as three prompts on one spine:

1. `brand-idea-bank` — capture the pile, transferred verbatim, ungraded.
2. `idea-evaluation` — grade the whole pile against the approved roadmap into a ranked shortlist, naming which ideas go to briefs first.
3. `brief-creation` — build the shortlist's top picks into concepts with variations, creator direction, and the three validations.

## Stamp the operating contract

Last, make the brand brain readable as itself:

1. **`CLAUDE.md`** from `templates/brand-brain-CLAUDE-template.md`. Fill the brand name, the brand hard rules from `running-notes/brand-notes-from-org.md`, and the standing strategic direction once the roadmap is approved. Delete the template's header block.
2. **`README.md`** — the brand-facing map: the run date, the brand, the data surfaces pulled and the ones dark, and where to start reading. Lead the "where to start" with the one move that needs no map — **open the repo and run `/get-started`** for a guided walkthrough of what's here and what to do first — then list the docs. Note that the method now ships in-repo — the skills (craft + routine) in `.claude/skills/` where they load on clone, and the rest under `parker-system/` (`prompts/`, `creative-strategy-context/`, `system/`) — so the brain can refresh, rebuild, and execute on its own without the factory.
3. **`running-notes/refresh-schedule.md`** from `templates/refresh-schedule-template.md`. Walk every standing doc the build produced, read its `generated_on` and `refresh_by` frontmatter, and fill the matching line so the schedule is a true aggregate of the brain's freshness on day one. From here on, every prompt re-run updates its own line. This is the file Parker watches to know when to tell the user a doc is due; the cadence policy behind it is `parker-system/system/refresh-cadence.md`.
4. **The brand lens — where this brand's tribal knowledge lives.** Seed `parker-system/creative-strategy-context/_<brand>-lens.md` from `templates/brand-lens-template.md`. This is the standing overlay the expertise layer loads on top of the generic method on every creative output, so the brand's own knowledge keeps shaping the work long after onboarding. Fill it with whatever the brand has already told us that a generic method can't know — voice rules, do's and don'ts, claims and language constraints, what has worked and failed for them, positioning nuances, named preferences — pulled from `running-notes/brand-notes-from-org.md` and anything the user corrected or insisted on during the build. If little brand-specific knowledge has surfaced yet, still create the file as a labeled scaffold so the surface exists and fills over time; the refresh and self-improve routines add to it as the brand teaches Parker more. Keep it sourced and dated per the attribution rules, and mark each line stated or verified.
5. **The folder indexes for the surfaces that grow.** Generate `competitors/INDEX.md` now — one line per competitor profile: the folder name, the rival, and the one-line read of what it is — so the always-loaded `brand-profile.md` can point at it instead of enumerating every rival. (`audits/INDEX.md` is created the same way the first time an audit exists — the audit cadence owns it, not the cold start, since a fresh build has no audits yet.) These two folders grow without bound, so they carry their own generated index rather than bloating the one-pager; every other standing doc is listed directly in the brand-profile's vault index. One line per doc, pointers not findings; regenerate when the folder's contents change.
6. **The living-loop routine bundle** from `templates/brand-routines/`. Copy `claude/` → `.claude/` (rename the dot) and `schedules/` → `schedules/`. These are the self-contained routine skills (`dream`, `self-improve`, `research-loops`, `update-brain`, `harvest-ideas`, `evaluate-ideas`, `refresh-context`, `setup-routines`, `get-started`), the context hook (`settings.json` + `hooks/craft-context.py`, which injects the live craft catalog into every turn — a Claude Code hook, no relation to ad hooks), and the six schedule recipes — so the brain is self-running the moment it's cloned. Replace `[brand]` / "the brand" with the brand name where it reads naturally; leave the brand-rule pointers (`CLAUDE.md`, `running-notes/brand-notes-from-org.md`) as-is, since they resolve inside the brain. Then arm the schedules right here, as part of this step: run `/setup-routines` in build mode — all six recipes registered at their default cadences, in the user's timezone when the session knows it, reconciling rather than duplicating anything already registered, and no approval gate, because the go-ahead they gave at the top covers it and the orientation told them the brain arrives running. The finish still owes them the one plain sentence of disclosure: what's running, when, and that `/setup-routines` changes the cadence or turns any routine off. (A brain later cloned onto a *new* cloud instance arrives un-armed all the same — schedules are per-account and can't be committed — which is what running `/setup-routines` by hand remains for.) The method behind the bundle is `self-improvement/the-living-loop.md` + `dreaming-system.md` + `parker-system/system/schedules.md`.

## Verify the build — confirm the brain is complete and correctly wired

The per-prompt review pass above checks that each document followed its own prompt. This is the other half: a **build-completion review** that checks the brain as a whole was actually assembled and wired, not just that the individual docs are good. Run it after stamping and before you save or onboard, because the failures it catches are silent — a brain can be full of excellent docs and still be missing the routine bundle, still carry template placeholders, or still point at factory paths that won't resolve once cloned.

Spawn a review subagent whose only job is structural completeness. Give it this runner and the brand repo, and have it verify each of these, reporting **pass** or **fail with the specific gap**:

- **The layout is whole.** Every top-level surface from the flat layout exists, and every prompt the dependency graph required produced its output — cross-check against `prompts-run-log/`. A branch that was deliberately blocked (e.g. competitors, when the set wasn't configured in the Parker app) is noted as deferred, not silently counted as missing.
- **The contract is stamped, not templated.** `CLAUDE.md` and `README.md` are filled with the real brand — no `{{BRAND_NAME}}`, no leftover `[brand]` placeholders, no template header block left behind.
- **The full method shipped — skills in `.claude/skills/` and the `parker-system/` bundle.** `parker-system/` carries its three layers — `prompts/` (the generating prompts, so the brain can refresh and rebuild itself), `creative-strategy-context/` (the craft knowledge), and the runtime `system/` docs. No shipped doc still points at a factory `global/knowledge/creative-strategy/` or unprefixed `system/` path that won't resolve in the standalone repo. **Cross-check the skills by name:** every craft skill from the factory's `.claude/skills/` is present in the brain's `.claude/skills/` alongside the routine bundle — count them and compare, don't eyeball — because a skill that isn't in `.claude/skills/` does not load on clone, and a half-shipped layer leaves the brand `CLAUDE.md`'s `.claude/skills/<skill>/` routing pointing at nothing. A missing `parker-system/prompts/` or a short `.claude/skills/` is a hard fail: without the prompts the refresh routine has nothing to re-run, and without the full skills set Parker can't execute the craft it's told to route through. (Confirm a single `dream` — the routine one — survived the merge, not two.)
- **The brain is self-running.** The routine bundle actually landed: `.claude/skills/` holds the nine bundled skills (`dream`, `self-improve`, `research-loops`, `update-brain`, `harvest-ideas`, `evaluate-ideas`, `refresh-context`, `setup-routines`, `get-started`), `.claude/settings.json` carries the context hook with its `hooks/craft-context.py` script beside it, and `schedules/` holds the recipes. **This is the check that catches `/setup-routines` or `/get-started` never appearing** — a missing `.claude/skills/` is a hard fail, not a warning. And the clock is actually running: the six routines are registered as scheduled agents on this instance (list them to verify) and each `schedules/*.md` is marked active — stamped-but-never-armed is a named miss, not a silent pass.
- **The freshness ledger is real.** `running-notes/refresh-schedule.md` lists every standing doc with a true `generated_on` / `refresh_by`, and the generated folder indexes (`competitors/INDEX.md`, and `audits/INDEX.md` if audits exist) are present and match their folders.
- **The provenance holds.** Standing docs carry their claim labels and stamps; nothing reads as fabricated to fill a gap.
- **The status file closed out.** `BUILD-STATUS.md` shows every ledger item resolved (`done`, or `blocked` with a named reason the user has seen), and it has been moved into `prompts-run-log/` as the build's final record — the repo root carries no live status file once the build is done.

On any fail, the orchestrator fixes the named gap directly — re-copy the bundle, re-run the missing prompt through the fidelity contract, rewrite the dangling path, refill the placeholder — then re-verifies. Only once this passes is the build allowed to be called done, and only then do you save and onboard. Log the verdict in `prompts-run-log/`.

## Save the brain to GitHub

The whole build so far lives only on this machine. Before onboarding, save it: commit everything and push it to the brand's GitHub repo, so the work is backed up, openable from anywhere, and shareable with the team. **Do not skip this.** A brain that was never pushed is one closed terminal away from gone, and the person who just spent hours on it almost certainly won't think to do it themselves.

1. Stage and commit every build output with a plain message, e.g. `Initial brand brain build — <brand>, <date>`. By this point `BUILD-STATUS.md` lives in `prompts-run-log/` (the verification above checks it), so the archived copy is what gets committed, not a live status file at root.
2. Push to the brand repo's `main` on GitHub (`git push -u origin main`).
3. Confirm it landed: give them the repo URL, tell them everything is now saved there, and explain in one line what that means — their brain is backed up in the cloud, and they (or a teammate) can reopen it any time, on any machine, by cloning or opening that repo.

If the push fails (auth not set, no remote, branch mismatch), fix it with them now rather than leaving the brain unsaved.

## Onboarding — show them what they have and how to use it

Everything above was **setup**: you built the brain. This is the **onboarding**: you hand it over and teach them how to get value from it. Do not end the session on "the build is done." A brand brain is worth nothing to someone who doesn't know what it is or what to ask it, and most people finishing this step are exactly that person. Slow down and walk them through it, conversationally — this part is as much the deliverable as the docs are.

**Run `/get-started` live with them now, as the hand-off.** That skill — stamped into the brain at `.claude/skills/get-started/` — is the canonical walkthrough, so do it by running it rather than improvising your own version here. It reads the brain you just built and, calibrated to how familiar this particular person is with files, GitHub, and tools like this, covers what the brain is, what the three build passes produced, how the files work and how they grow it, what Parker can actually pull and do, what skills are, how to connect their other tools, what the brain does on its own (already running — armed during the build) and how to adjust it, how to bring teammates in, and where to start — paced one thing at a time, grounded in this brand's own data, ending on a single first move. The skill carries the full method; don't re-list it here.

The reason this is a skill and not just narration: the live build session is the *first* time someone needs this, not the only time. A teammate who clones the brand repo next month, or the same user returning in a fresh session, gets the same orientation by running `/get-started` themselves — it reads the brain's current state, so it always teaches what the brain has become. Close the hand-off by telling them that: the walkthrough is always here, for anyone, any time. The brand `CLAUDE.md` also has the brain offer it proactively on a first-encounter session, so a first-timer who never reaches this runner still gets pointed at it.

## What this runner does not build

- **`content-pipeline/`** is a brand-specific production-to-launch subsystem, not a factory output. Build it only when a brand asks for it; do not scaffold it by default.
- **`dreaming/` and `workflows/`** are living layers populated by their own offline runs, not at build time. Scaffold the READMEs and leave them empty. (`.claude/` and `schedules/` are different — those ship *populated* from `templates/brand-routines/` per the Phase-0 stamp and the onboarding hand-off above, because the routines must travel with the brain.)
- The audit cadence layer (`prompts/audits-*`) runs its **first pass during the cold start** (Phase-1 branch E), so the account one-pagers have a real packet to synthesize and the brain ships with a baseline read of the account; only its recurring re-runs are ongoing, fired by the refresh-sweep schedule on each audit's named interval from its `generated_on`. The research cycle (`research-loops`, sequencing the roll-up and the advance and validate skills), self-improvement, and dreaming are the genuinely ongoing layer that keeps a standing brain fresh — they run on a brain that already exists, not during the cold start. The *routines that invoke all of this* (the `.claude/` skills + `schedules/` recipes) ship at build time, so the standing brain can run itself.
