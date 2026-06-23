# Onboarding runner — build a brand brain from scratch

This is the single entrypoint for standing up a new brand's brain end to end. When the task is "build [brand]'s brain," follow this runner: it sequences every prompt in dependency order, writes each output to the right place in the flat standalone layout, ships the craft layer into the repo, and stamps the operating contract. It is the executable version of the build order in `prompts/README.md` — read that first for why the phases are a backbone and not a turnstile, then run this for the mechanics.

Run this inside an interactive Claude session with Parker MCP reachable. Headless is walled off today, so the runner assumes a live session. It assumes zero brand-provided inputs: every foundation prompt reads from the source itself through Parker MCP, over time, not from a brief the brand hands over.

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

## Phase 0 — new repo, connect, scaffold, ship the craft, read in

Do all of this before running a single content prompt.

1. **Stand up the brand's own repository — do not build inside this `parker-brain` clone.** This product brain is the read-only factory teams clone; the brand brain is a **separate, standalone repo for that brand.** Confirm with the user where it should live, then initialize a new git repo (a new GitHub repo for the brand) distinct from `parker-brain`, and build everything below inside it. Every brand output is committed there, never back into the cloned product brain. The flat standalone layout above is the shape of this new repo.
2. **Connect and confirm the brand.** Parker MCP must be reachable. Call `get_available_brands`, confirm the right brand with the user, and lock its brand_id. Several brands share a name across orgs, so the id is the anchor for every pull that follows. **If the MCP is not connected** — no brand list, pulls error or return empty — stop and tell the user plainly: the brain cannot be built from the source without a data path. Parker needs some way to reach the ad account, organic socials, reviews, surveys, and the competitor library; the **Parker MCP is the one connection that carries all of it** and is the recommended path, though independent platform exports can feed the same evidence more manually. Do not fabricate a build from general knowledge. The full reminder is in `system/parker-tools.md`.
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

**Close the build by reminding them to arm the routines.** The schedules don't fire until someone registers them, and that's a per-instance step you can't do for them silently. So once the brain is stamped, tell the user plainly: the routines (refresh, dream, idea cycle, self-improve) are ready but not yet on a schedule, and you'll set them up whenever they want — they just have to say the word and you'll run `/setup-routines`. Make it a one-line offer, not a chore handed back to them.

## What this runner does not build

- **`content-pipeline/`** is a brand-specific production-to-launch subsystem, not a factory output. Build it only when a brand asks for it; do not scaffold it by default.
- **`dreaming/` and `workflows/`** are living layers populated by their own offline runs, not at build time. Scaffold the READMEs and leave them empty. (`.claude/` and `schedules/` are different — those ship *populated* from `templates/brand-routines/` per step 4 above, because the routines must travel with the brain.)
- The audit cadence layer (`prompts/audits-*`) runs its **first pass during the cold start** (Phase-1 branch E), so the account one-pagers have a real packet to synthesize and the brain ships with a baseline read of the account; only its recurring re-runs are ongoing, fired by the refresh-sweep schedule on each audit's named interval from its `generated_on`. The open-loops advance and validate skills, and self-improvement and dreaming, are the genuinely ongoing layer that keeps a standing brain fresh — they run on a brain that already exists, not during the cold start. The *routines that invoke all of this* (the `.claude/` skills + `schedules/` recipes) ship at build time, so the standing brain can run itself.
