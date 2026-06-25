# Onboarding runner — build a brand brain from scratch

This is the single entrypoint for standing up a new brand's brain end to end. When the task is "build [brand]'s brain," follow this runner: it sequences every prompt in dependency order, writes each output to the right place in the flat standalone layout, ships the craft layer into the repo, and stamps the operating contract. It is the executable version of the build order in `prompts/README.md` — read that first for why the phases are a backbone and not a turnstile, then run this for the mechanics.

Run this inside an interactive Claude session with Parker MCP reachable. Headless is walled off today, so the runner assumes a live session. It assumes zero brand-provided inputs: every foundation prompt reads from the source itself through Parker MCP, over time, not from a brief the brand hands over.

**You are teaching, not only building.** Assume the person running this has little sense of what Parker is or how a brand brain works; for many it is the first time they have ever seen anything like it. So narrate as you go: at each phase, say in plain language what you are about to do, why it matters, and what they will have when it is done, in their words and not the system's. Explain the what and the why; keep the machinery (agents, embedded blocks, loops, tiers) out of sight. The build is their first lesson in the thing they now own, so treat every phase as a chance to show them what it is, not a silent batch job to grind through. And signpost the whole way: at every phase boundary and every decision gate, say plainly where they are, what just happened, what's next, and what — if anything — you need from them, so a choice never feels like a surprise or a trap and it always feels safe to ask a question or pause.

## What this runner produces — the flat standalone layout

A brand brain is a self-contained repo a marketing team opens and talks to, not a folder inside the product brain. The factory prompts describe their outputs in `z-brands/[brand]/…` terms because that is the product brain's internal tree, but a shipped brand brain is flatter and stands alone. The runner is the mapping layer: wherever a prompt says to write to a `z-brands/[brand]/…` path, write to the flat path in the table below instead.

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
- `dreaming/`, `schedules/`, `workflows/`, `.claude/` — the living layer. `dreaming/` and `workflows/` are README-only at build time (each populated by its own runs). `.claude/` and `schedules/` are **stamped from `templates/brand-routines/`**: the six routine skills + the craft-loading hook, and the four schedule recipes (repo-native cron, `system/schedules.md`). This is what makes the brain self-running the moment it's cloned.
- `creative-strategy-context/` — the craft layer, copied in during Phase 0.
- `system/` — the runtime system layer, copied in during Phase 0: the tool inventory, the operating model, and the open-loops / refresh / schedules mechanisms the brain runs on. This is the subset of the factory's `system/` the brain actually reads at runtime; the factory-internal docs and the product-architecture map stay behind (a standalone brain's situational awareness is `CLAUDE.md`'s "## The map" plus the vault index in `brand-profile-narrative.md`, not the factory system map).
- `prompts-run-log/` — the build log.

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

> "Run the prompt at `prompts/<path>.md`. Open it and read it in full, including every block it embeds and the entry context it names, before you write anything. Execute it exactly as written — its section structure, its claim labels, the expertise docs it tells you to load, its denominators, and its open-loops tail are all mandatory; none may be skipped, shortened, or rewritten. Brand: `<name>`, `brand_id`: `<id>`. Write the output to `<flat path>`. You may read these upstream docs: `<paths>`."

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

- **Where they're in control.** Name the moments they'll be asked to choose or confirm, so it's obvious nothing big happens without them: the go-ahead to start at all, what to do if the data connection isn't ready, which competitors to use, and the big one — **approving the strategy before Parker builds anything on top of it.** Tell them they can pause, ask questions, or change direction at any point.

- **When it becomes theirs to use.** They get a real, usable brain at the end, saved to their own GitHub, that they open and talk to in plain language — and you'll walk them through exactly how when you get there.

Keep it short and human — a friendly map of the trip, not a wall of text or a contract. The point is that before a single thing runs, they understand what they're setting up, that it's safe, and that they're the one driving. Then move to the heads-up below.

## Before you run it — the heads-up and the go-ahead

Quick, honest heads-up before we dive in, then a real go/no-go. Building a brand brain is a *big* job — Parker reads the whole account, the reviews, the comments, the organic, and the competitors, and writes the entire vault from scratch. All that reading and writing burns a fair amount of usage. No way around it: good context isn't free.

So here's the deal, plainly and with love: we **strongly recommend running this on a Max or 20x Max plan.** On a lighter plan it can absolutely still run — it just might chew through your whole five-hour usage window, and on a heavy build maybe make a dent in the week. We'd rather you know that going in than hit a wall halfway through a persona.

And honestly? It's worth it. It costs what it costs because Parker is doing a real strategist's homework — reading everything, writing it all down, connecting the dots — and that depth is the whole point. It's what takes the AI from "helpful chatbot" to "the strategist who actually knows your brand."

Make this a gate, not a footnote: say the above in your own warm words, then **ask the user to confirm they want to kick off the full build now.** If they'd rather wait, switch plans first, or start smaller, that's a perfectly fine answer — offer to pick it back up whenever. Do not start Phase 0 until they've said go.

## Phase 0 — new repo, connect, scaffold, ship the craft, read in

Do all of this before running a single content prompt.

1. **Stand up the brand's own repository — do not build inside this `parker-brain` clone.** This product brain is the read-only factory teams clone; the brand brain is a **separate, standalone repo for that brand.** Before any of the git mechanics, gauge their GitHub comfort and meet them there: ask how familiar they are with GitHub and git. If they are new to it, slow down and explain in plain terms what a repository is, what cloning means, and why the brand gets its own repo separate from this one, and offer to walk them through each step rather than assuming they can follow a command; if they are fluent, move briskly and skip the explanation. Then confirm with the user where it should live, initialize a new git repo (a new GitHub repo for the brand) distinct from `parker-brain`, and build everything below inside it. Every brand output is committed there, never back into the cloned product brain. The flat standalone layout above is the shape of this new repo.
   - **If they're starting from zero on GitHub**, walk these in order and explain each as you go, rather than assuming any of it is obvious: (1) if they don't have a GitHub account, have them create a free one at github.com; (2) make sure the GitHub CLI is available and signed in — run `gh auth login` and have them follow the browser prompt, since that sign-in is what lets you create and push repos on their behalf; (3) once signed in, *you* create the brand repo for them with `gh repo create <brand>-brain --private`, rather than making them click through the web UI. Default the repo to **private** unless they say otherwise — it holds their brand's data. If they already use GitHub day to day, skip the explanation and go straight to creating the repo.
2. **Connect and confirm the brand.** Parker MCP must be reachable. Call `get_available_brands`, confirm the right brand with the user, and lock its brand_id. Several brands share a name across orgs, so the id is the anchor for every pull that follows. **If the MCP is not connected or a test fails** — no brand list, pulls error or return empty — don't silently push on, and don't hard-stop either: make it the user's call, as a required choice you wait on. Explain plainly that without the Parker MCP, Parker can't reach the live source — the ad account, organic socials, reviews, surveys, the competitor library — so the build would lean on general knowledge instead of their real data, and **it will not be nearly as good.** Then give them three options and wait for their pick: **(a) pause** here while they set up or connect the MCP, and come back to it; **(b) connect it now**, and you re-run the test and continue; or **(c) continue without it**, understanding the brain will be thin and every claim data-limited until the real data is wired in later. This is a gate — do not proceed past it on your own judgment. The **Parker MCP is the one connection that carries all of it** and is the recommended path, though independent platform exports can feed the same evidence more manually; the full reminder is in `system/parker-tools.md`. Whichever they pick, never fabricate data to fill the gap.
   - **Test the tools, don't just ping them.** Reachable is not the same as operable. Run a quick operability check — a light pull from each major surface (ads, customer reviews, ad comments, organic social, post-purchase surveys, and the competitor library) — to confirm each actually returns data, not merely that the connection is up. A surface that errors or comes back empty now is one that would silently hole the build later, so name it to the user plainly and log it in `running-notes/missing-context.md`. As you run each test, explain in plain language what that tool reaches and why it matters, since the person watching likely has no idea what Parker can see — this is the first place they learn what their brain is made of.
   - **Decide the competitive set with the user — a real choice, not an assumption.** While you are in the tools, query the available database of brands Parker can reach. Parker *can* pick a competitive set from that database on its own, but that's our selection from what happens to be available, not necessarily who the user would name themselves. So preface it honestly and let them choose: tell them that, left alone, Parker will choose competitors from the brands in our database, and ask whether they would rather **(a) go into the Parker app and add the specific competitors they care about** — the sharper option, since they know their real rivals — or **(b) let Parker pick the set from what's in our database** and move on. Wait for their pick. If they choose to add their own, pause the competitor branch (B below) until they've done it; if they're fine with Parker's selection, note which brands were chosen and why so the choice is visible in the build. Explain what a competitor analysis gives them either way, so the decision feels worth making.
3. **Scaffold the flat repo.** Create the top-level tree above inside the brand's repo. Drop the standing README files into `personas/sources/` is not needed here, but seed `open-loops/`, `hypotheses/`, `validations/`, `re-validations/`, `dreaming/`, `schedules/`, and `workflows/` with their README scaffolds so the living layers have a home before they fill.
4. **Ship the craft layer and the system layer.** Two copies, both so the brain is self-contained and references nothing in the factory at runtime. No prompt does this; the runner does.
   - **Craft:** copy the full `global/knowledge/creative-strategy/` tree into the brand repo as `creative-strategy-context/`. After the copy, the expertise-core block's `creative-strategy-context/expertise-routing.md` reference resolves inside the brand repo.
   - **System:** copy the **runtime** system docs from the product brain's `system/` into the brand repo's `system/` — `parker-tools.md`, `three-phase-operating-model.md`, `open-loops-system.md`, `refresh-cadence.md`, and `schedules.md`. These are the docs the brain reads to operate: what it can pull, how it works a brand, and the loop / refresh / schedule mechanisms. **Leave the factory-internal docs behind** — `master-prompt-review.md`, `system-of-records.md`, `master-file-structure.md`, `attribution-principle.md` — they are for building and maintaining the factory, not running the brain (the attribution rules the brain needs are already inlined in `CLAUDE.md`). **Do not ship `parker-system-map.md`** either: it maps the factory/product architecture (teams, z-brands, prompts, the shared foundation) and would misdescribe a standalone single-brand brain. The brain's own situational awareness is `CLAUDE.md`'s "## The map" plus the always-loaded vault index in `brand-profile-narrative.md`. After the copy, rewrite any `global/knowledge/creative-strategy/` path inside the shipped system docs to `creative-strategy-context/` so their cross-references resolve in the flat repo.
5. **Read the entry context.** Open `CLAUDE.md`, `system/three-phase-operating-model.md`, `system/open-loops-system.md`, and `creative-strategy-context/expertise-routing.md` — all now present in the brand repo from step 4. The routing map names which method docs each prompt must load before it analyzes.
6. **Open the build log.** Start `prompts-run-log/[YYYY-MM-DD]-full-buildout.md` and record each prompt as it runs, with the source pulled and the date, so the brain carries its own provenance.

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

**The gate.** When Parker is driving the strategy, stop here and present the roadmap for the user to approve, adjust, or reject. Approval is what turns the call into committed direction and unblocks Phase 3. Hold the gate lightly per the operating model's governing rule: a co-piloting user who already knows their direction does not have to formally approve a roadmap before Parker helps them execute. The roadmap is the artifact when Parker is asked to set the strategy, not a permission slip the user has to sign before Parker will write a script.

## Phase 3 — make the work

Only once the roadmap is the agreed direction. The judgment runs as three prompts on one spine:

1. `brand-idea-bank` — capture the pile, transferred verbatim, ungraded.
2. `idea-evaluation` — grade the whole pile against the approved roadmap into a ranked shortlist plus a brief-first handoff.
3. `brief-creation` — build the shortlist's top picks into concepts with variations, creator direction, and the three validations.

## Stamp the operating contract

Last, make the brand brain readable as itself:

1. **`CLAUDE.md`** from `templates/brand-brain-CLAUDE-template.md`. Fill the brand name, the brand hard rules from `running-notes/brand-notes-from-org.md`, and the standing strategic direction once the roadmap is approved. Delete the template's header block.
2. **`README.md`** — the brand-facing map: the run date, the brand, the data surfaces pulled and the ones dark, and where to start reading. Note that the methodology now ships in-repo at `creative-strategy-context/`.
3. **`running-notes/refresh-schedule.md`** from `templates/refresh-schedule-template.md`. Walk every standing doc the build produced, read its `generated_on` and `refresh_by` frontmatter, and fill the matching line so the schedule is a true aggregate of the brain's freshness on day one. From here on, every prompt re-run updates its own line. This is the file Parker watches to know when to tell the user a doc is due; the cadence policy behind it is `system/refresh-cadence.md`.
4. **The folder indexes for the surfaces that grow.** Generate `competitors/INDEX.md` now — one line per competitor profile: the folder name, the rival, and the one-line read of what it is — so the always-loaded `brand-profile.md` can point at it instead of enumerating every rival. (`audits/INDEX.md` is created the same way the first time an audit exists — the audit cadence owns it, not the cold start, since a fresh build has no audits yet.) These two folders grow without bound, so they carry their own generated index rather than bloating the one-pager; every other standing doc is listed directly in the brand-profile's vault index. One line per doc, pointers not findings; regenerate when the folder's contents change.
5. **The living-loop routine bundle** from `templates/brand-routines/`. Copy `claude/` → `.claude/` (rename the dot) and `schedules/` → `schedules/`. These are the self-contained routine skills (`dream`, `self-improve`, `harvest-ideas`, `evaluate-ideas`, `refresh-context`, `setup-routines`), the craft-loading `settings.json` hook, and the four schedule recipes — so the brain is self-running the moment it's cloned. Replace `[brand]` / "the brand" with the brand name where it reads naturally; leave the brand-rule pointers (`CLAUDE.md`, `running-notes/brand-notes-from-org.md`) as-is, since they resolve inside the brain. The schedules ship un-armed; the brand owner runs `/setup-routines` once per cloud instance to register the cron. The method behind the bundle is `self-improvement/the-living-loop.md` + `dreaming-system.md` + `system/schedules.md`.

## Verify the build — confirm the brain is complete and correctly wired

The per-prompt review pass above checks that each document followed its own prompt. This is the other half: a **build-completion review** that checks the brain as a whole was actually assembled and wired, not just that the individual docs are good. Run it after stamping and before you save or onboard, because the failures it catches are silent — a brain can be full of excellent docs and still be missing the routine bundle, still carry template placeholders, or still point at factory paths that won't resolve once cloned.

Spawn a review subagent whose only job is structural completeness. Give it this runner and the brand repo, and have it verify each of these, reporting **pass** or **fail with the specific gap**:

- **The layout is whole.** Every top-level surface from the flat layout exists, and every prompt the dependency graph required produced its output — cross-check against `prompts-run-log/`. A branch that was deliberately blocked (e.g. competitors, when the set wasn't configured in the Parker app) is noted as deferred, not silently counted as missing.
- **The contract is stamped, not templated.** `CLAUDE.md` and `README.md` are filled with the real brand — no `{{BRAND_NAME}}`, no leftover `[brand]` placeholders, no template header block left behind.
- **The craft and system layers shipped.** `creative-strategy-context/` is present, the runtime `system/` docs are present, and no shipped doc still points at a `global/knowledge/creative-strategy/` path that won't resolve in the standalone repo.
- **The brain is self-running.** The routine bundle actually landed: `.claude/skills/` holds the six routine skills (`dream`, `self-improve`, `harvest-ideas`, `evaluate-ideas`, `refresh-context`, `setup-routines`), `.claude/settings.json` carries the craft-loading hook, and `schedules/` holds the recipes. **This is the check that catches `/setup-routines` never appearing** — a missing `.claude/skills/` is a hard fail, not a warning.
- **The freshness ledger is real.** `running-notes/refresh-schedule.md` lists every standing doc with a true `generated_on` / `refresh_by`, and the generated folder indexes (`competitors/INDEX.md`, and `audits/INDEX.md` if audits exist) are present and match their folders.
- **The provenance holds.** Standing docs carry their claim labels and stamps; nothing reads as fabricated to fill a gap.

On any fail, the orchestrator fixes the named gap directly — re-copy the bundle, re-run the missing prompt through the fidelity contract, rewrite the dangling path, refill the placeholder — then re-verifies. Only once this passes is the build allowed to be called done, and only then do you save and onboard. Log the verdict in `prompts-run-log/`.

## Save the brain to GitHub

The whole build so far lives only on this machine. Before onboarding, save it: commit everything and push it to the brand's GitHub repo, so the work is backed up, openable from anywhere, and shareable with the team. **Do not skip this.** A brain that was never pushed is one closed terminal away from gone, and the person who just spent hours on it almost certainly won't think to do it themselves.

1. Stage and commit every build output with a plain message, e.g. `Initial brand brain build — <brand>, <date>`.
2. Push to the brand repo's `main` on GitHub (`git push -u origin main`).
3. Confirm it landed: give them the repo URL, tell them everything is now saved there, and explain in one line what that means — their brain is backed up in the cloud, and they (or a teammate) can reopen it any time, on any machine, by cloning or opening that repo.

If the push fails (auth not set, no remote, branch mismatch), fix it with them now rather than leaving the brain unsaved.

## Onboarding — show them what they have and how to use it

Everything above was **setup**: you built the brain. This is the **onboarding**: you hand it over and teach them how to get value from it. Do not end the session on "the build is done." A brand brain is worth nothing to someone who doesn't know what it is or what to ask it, and most people finishing this step are exactly that person. Slow down and walk them through it, conversationally — this part is as much the deliverable as the docs are.

1. **Show them what just got built, in plain language.** Walk the brain they now own: the audit that read their account, the personas of who actually buys, the voice-of-customer library of how those people talk, the competitor reads, the strategy and its top priorities, and the idea bank and briefs. Tie each to something concrete from their own data so it lands as real and not abstract. The goal is that they understand what the brain knows and where it lives.

2. **Show them how to open it and talk to it.** This is the rung a novice most needs and most often misses: the brain is just a repo, and you use it by opening that repo in Claude Code (or the Claude app) and talking to it in plain language — no commands, no special syntax, you ask it things the way you'd ask a sharp colleague who already knows the brand. Show them how to start a session against the brand repo, then give them one real question to try out loud so the mechanic clicks — open it, type a plain question about their own brand, watch it pull from the vault and answer. Make sure they can do it themselves before moving on.

3. **Explain the schedules, then arm them.** This brain can keep itself fresh on its own, but only once the schedules are registered, and that's a per-instance step you can't do for them silently. Explain what each routine does and why it matters before running anything: **refresh-context** re-reads the account on a cadence so the brain never quietly goes stale; **dream** lets it think between sessions and surface ideas unprompted; **harvest-and-evaluate** runs the idea cycle so good ideas get captured and graded instead of evaporating; **self-improve** lets it get better at this specific brand over time. Then offer to arm them with `/setup-routines` — a one-time setup, not a chore handed back to them — and let them choose which to turn on.

4. **Recommend where to start, grounded in their data.** Don't leave them at a blank prompt. From what the build actually surfaced, suggest two or three concrete first moves and say why each is worth it: the strongest open loop to chase, the whitespace the audit found, a script for the lead persona in their own customers' language, a read on why a metric moved. Make every suggestion specific to this brand, so the first thing they do with Parker is something that matters to them, not a toy.

5. **Make it a conversation, not a handoff.** Invite their questions and actually go back and forth — what does this mean, can it do that, why did you recommend this, where did that number come from. Answer plainly, show them by doing when you can, and let them drive. This back-and-forth is the real onboarding: the better they understand what they have, the more they'll get out of it.

## What this runner does not build

- **`content-pipeline/`** is a brand-specific production-to-launch subsystem, not a factory output. Build it only when a brand asks for it; do not scaffold it by default.
- **`dreaming/` and `workflows/`** are living layers populated by their own offline runs, not at build time. Scaffold the READMEs and leave them empty. (`.claude/` and `schedules/` are different — those ship *populated* from `templates/brand-routines/` per step 4 above, because the routines must travel with the brain.)
- The audit cadence layer (`prompts/audits-*`) runs its **first pass during the cold start** (Phase-1 branch E), so the account one-pagers have a real packet to synthesize and the brain ships with a baseline read of the account; only its recurring re-runs are ongoing, fired by the refresh-sweep schedule on each audit's named interval from its `generated_on`. The open-loops advance and validate skills, and self-improvement and dreaming, are the genuinely ongoing layer that keeps a standing brain fresh — they run on a brain that already exists, not during the cold start. The *routines that invoke all of this* (the `.claude/` skills + `schedules/` recipes) ship at build time, so the standing brain can run itself.
