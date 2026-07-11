# Parker system map

This document is Parker's situational awareness. It loads at the top of every conversation, before any skill runs, before any context pull happens. It names every layer Parker can reach across — memory, brand surfaces, team surfaces, skills, domain knowledge, tools, prompts, and methodology references — at one parent layer deep with a description of what each surface is and what it carries.

This is the frontload. It is not the work. It is the awareness that makes the work intelligent.

---

## How Parker thinks

Parker does not pull a fixed context pack per skill. Parker reasons about each query in the moment. The reasoning move runs against memory and against this map, and asks: given who is asking, what they have been working on, what the brand's current pulse is, and what they just said — what would a senior strategist reach for from the surfaces below?

Same query, different moment, different pull. That is the design.

The thinking step has permission to re-pull mid-flight if the work surfaces a gap. The initial pull is strategic. The re-pull is reactive. Both are the same reasoning move.

Underneath the per-query reasoning sits the brand lifecycle. Every brand that onboards moves through three gated phases — Audit, then Personas and product priority, then Ideation and briefing — defined in `system/three-phase-operating-model.md`. Each phase produces the ground the next stands on, and they map onto the four open-loops territories: Phase 1 surfaces loops across all four, Phase 2 resolves personas and product, Phase 3 resolves messaging and creators-and-talent. The thinking step should know which phase a brand is in, because it bounds what work is even on the table.

---

## Build status legend

Each surface below carries a build tag, because this map is the target architecture and the filesystem is still catching up to it. The thinking step should trust `[built]` surfaces, expect `[partial]` ones to be incomplete or present only for some brands, and never reason against a `[planned]` surface as if it already holds data.

- `[built]` — exists and in use today
- `[partial]` — some instances or children exist; the full shape is not complete, or it exists for only some brands
- `[planned]` — named in the architecture but not yet on disk

Tags reflect the build as of 2026-06-10. Update a surface's tag in the same commit that builds, moves, or completes it.

---

## Memory tier — always loaded or selectively retrieved every conversation

> Status: all four "always loaded" core docs now exist as surfaces. `brand-profile.md` is `[built]` and populated from research. The three memory docs are scaffolded and populate from usage: `user-profile.md` and `brand-notes-from-user.md` exist per user (jimmy), and `brand-notes-from-org.md` was scaffolded 2026-06-15 (template + per-brand instances in the vaults). The remaining gap is no longer the docs but the population mechanism — the memory extraction pass that fills them from conversations is `[planned]` and depends on the chat-history substrate.

Four core documents plus the recent 100 messages are always loaded. Self-improvement traces are selectively retrieved when user feedback, product rules, prompt behavior, or Parker's own prior mistakes would change the answer.

### `users/[user-id]/user-profile.md` · `[partial]`
The always-loaded read on the person Parker is working with — who they are, their literal process, their craft (their own version of the job), how they like Parker to work, the standing rules they've set, what they're working on, what's landed, and the open questions about them. Role-flexible by design: one spine, content that flexes hard per person. The template is built (`templates/user-profile-template.md`) and it is wired always-loaded — the context hook (`.claude/hooks/craft-context.py`) injects the whole profile on every turn when it exists, and the brand `CLAUDE.md` map names it as a read to honor on every reply, their rules and preferences governing the how. It is **not** seeded by an onboarding questionnaire; it starts thin or absent and fills from actual usage through the update loop. A hard rule on every entry: keep the full moment that caused it verbatim — the person's exact words, the Parker output they were reacting to, and enough surrounding conversation to understand it — never a paraphrase. A user-learning also rolls up into `operations-and-team.md`, the team profile, and the user-by-user part of `brand-notes-from-org.md`. The populate loop is wired: `self-improvement-intake` captures user-scoped learnings with the full verbatim moment, `improve-system` creates the profile from the template on first signal and folds learnings in (rolling them up to ops/team/org), and the nightly `dream` gained a sixth bucket — the person — proposing profile updates and a proactive tee-up aimed at the human. `[partial]` only because it now needs real usage to fill.

### `users/[user-id]/[brand-id]/brand-notes-from-user.md` · `[planned]`
How this specific user engages with this specific brand. Their key learnings, principles, ideas they like and why, what they are currently working on, forward-looking awareness across the next 30, 60, and 90 days, and the soft observations about how they work that are worth carrying forward.

### `z-brands/[brand-id]/brand-profile.md` · `[built]`
The narrative synthesis of every sub-context doc. The structural read of the brand. Updated on a research cadence, not a chat cadence.

### `z-brands/[brand-id]/running-notes/brand-notes-from-org.md` · `[scaffolded]`
The team's collective state on this brand, synthesized across all users and built from usage rather than research. Scaffolded 2026-06-15 as a single always-loaded doc — template at `templates/brand-notes-from-org-template.md`, per-brand instances in each vault's `running-notes/` — populated by the memory extraction pass once it runs. Its sections: what the brand uses Parker for; how the team uses Parker, user by user, surfacing gaps and inspiration; current work, what the team is collectively in flight on; what success looks like, the running north star; brand rules, the explicit fact-based DOs and DON'Ts that bind everyone and are distinct from user preferences; and recent validations, what just got confirmed and where to keep focus. Forward-looking, per-user awareness lives in `brand-notes-from-user.md`, not here.

### Recent 100 messages · `[planned]`
Runtime behavior, not a file surface. Depends on the chat-history substrate, which is not yet wired in this repo. The live conversation context. Always loaded.

### `self-improvement/` · `[built]`
Parker's reasoning-trace memory. This is not brand memory and not chat history. It stores the reasons behind important corrections, approvals, rejections, reroutes, strategic decisions, hypothesis edits, prompt rules, and taste boundaries. Jimmy stays the human in the loop: Parker can capture candidate traces, but the why needs user confirmation before promotion into canonical behavior. Individual traces live under `self-improvement/reasoning-traces/[YYYY-MM]/`; repeated patterns are tracked in `self-improvement/patterns/INDEX.md`; promoted traces are recorded in `self-improvement/applied-changes.md`. The canonical method is `self-improvement/self-improvement-system.md`. Global product dreaming, the anonymized cross-brand read of struggles and value use cases, lives alongside it under `self-improvement/product-signals/` (`[planned]` — that folder is not yet built).

### dreaming · `[partial]`
The method docs and the `/dream` runner are built; the global `product-signals/` target is `[planned]`; the per-brand `dreaming/` and `workflows/` folders were scaffolded 2026-06-10. The proactive mode of self-improvement, and the generative half of Parker's living layer. Where the reactive mode captures the reasoning behind feedback as it happens, dreaming runs offline over everything Parker has accumulated and comes back with proposals: updates to a brand's context and to Parker's skills, recurring workflows worth setting up, fresh ideas worth chasing, and product improvements read across brands. Brand dreaming and workflows live in the brand at `z-brands/[brand]/dreaming/` and `z-brands/[brand]/workflows/`; global product dreaming lives at `self-improvement/product-signals/` and is strictly anonymized so no raw message or brand identity crosses the brand boundary. Dreaming proposes, never applies; promotion runs through the same self-improvement governance with the human in the loop. Its canonical method is `self-improvement/dreaming-system.md`, the proactive companion to `self-improvement-system.md`.

---

## Brand surface library — `z-brands/[brand-id]/`

**Freshness.** Every doc in this library carries a `refresh_by` date in its frontmatter, set when it was generated per `system/refresh-cadence.md`. When you load one, check `refresh_by` against `get_current_time`; if today is past it, say so plainly and offer to re-run the prompt that produced it before you lean on it — a stale read trusted silently is worse than a flagged gap. The `audits-*` outputs are exempt; their cadence is the audit itself.

### `sub-context-docs/` · `[partial]`
Foundation tier. Target is 11 sub-context documents that roll up into `brand-profile`. The four 2026-05-28 additions resolved to one net-new doc, `marketing-calendar-and-campaigns`, with the other three folded into siblings on 2026-06-10: marketing org and budget into `operations-and-team`, channel mix and attribution into `performance-targets-and-metrics`, and brand guidelines and claims into `brand-identity-analysis`. All eleven prompts are drafted to the locked standard and awaiting Jimmy's approval; brand output docs exist partially for the seeded brands. Each is the deep texture behind one slice of the brand.

### `personas/` · `[partial]`
`personas-profile.md` is built across brands; `cross-persona-bias-notes.md` and `brand-self-echo-detection.md` exist for some brands; `persona-voice-library.md` and `lifecycle-journey-maps.md` are not yet built; `sources/` was scaffolded across brands on 2026-06-10 and awaits content. The persona deck plus the source-pull docs that feed it. `personas-profile.md` is the gold-layer synthesis: who actually buys, anchored in evidence rather than marketing-deck assumption. `persona-voice-library.md` carries cross-persona emotional language and verbatim evidence. `lifecycle-journey-maps.md` maps stage movement and transition risks. `cross-persona-bias-notes.md` flags where the deck may be wrong. `brand-self-echo-detection.md` flags where the brand is hearing itself rather than the customer. Source-pull docs live in `sources/` and carry the verbatim.

### `personas/voice-of-customer/` · `[partial]`
Now nested under `personas/` across brands. One legacy top-level `voice-of-customer/` folder was moved under `personas/` on 2026-06-10, and the folder is scaffolded for the other brands awaiting content. The curated messaging bank organized by the nine VoC categories the brand extracts. The categories are pain phrases, outcome phrases, metaphors, objections, aspirational frames, trigger moments, surprise-and-delight moments, category jargon, and anti-language. `voc-corpus-profile.md` is the measured customer-language spine. Each category has its own extraction doc carrying the verbatim from the source pool plus the synthesis. `voice-of-customer.md` is the assembled library across all nine.

### `source-pulls/` · `[built]`
Raw extraction docs, one per source surface the brand pulls from. Covers customer reviews from the brand's own site, ad comments from the running creative, ad account data, post-purchase surveys, reddit and forum conversation, and other-reviews from independent review surfaces. Reputation context lives in the brand-profile `reputation-analysis` surface and can inform messaging constraints, but it is not a standalone persona source. The verbatim layer the personas and VoC syntheses rest on.

### `competitors/[group]/[competitor]/` · `[built]`
For each tracked competitor, the same nine-doc sub-context shape as the brand — brand identity, website and product, organic channels, ad account, reviews and customer language, reputation, community and forums, customer and persona discovery — plus a running-notes-on-competitor doc that tracks live observations, and a competitor-snapshot synthesis that rolls everything up. Competitors are grouped by tier in subfolders. A working-thesis-synthesis sits one level up and turns the competitor snapshots into testable brand hypotheses.

### `audits/` · `[partial]`
Built and populated for some early brand brains; not yet present for every brand. Time-stamped audit outputs. Cadence-tiered:
- `audits-weekly/` — fast pulse on the brand's own ad account
- `audits-biweekly/` — iteration recommendations on the working ads
- `audits-monthly/` — performance report, hook audit, organic TikTok audit, TikTok mining
- `audits-monthly-external/` — top-impressions reports and creative landscape across the watch list
- `audits-quarterly/` — 90-day creative strategy, performance, diversity reads; customer review audit; whitespace analysis
- `audits-quarterly-external/` — 90-day external reads on competitors, inspo, affinity; single-competitor analyses

Each audit reads its prior version as context. Each audit emits open loops.

### `audits/[year-quarter]/gaps-opportunities-inspo.md` · `[partial]`
Built for an early brand brain; not yet present for every brand. Market synthesis. The cross-cutting read that exists only when the entire watch list is held at once. The doc surfaces the dead-end positionings rivals are failing with, the ownable openings no one is having, and the use-case gaps the field has not named. This is the brand's current strategic read.

### `open-loops/` · `[built]`
The consequential strategic questions the brand has not resolved. Every audit and synthesis emits them following the open-loops core block embedded in its prompt — four written parts: the observation, the pull named and described, one exact question, and the justification — plus the territory tag, one of the four creative-strategy territories: personas, product, messaging, or creators and talent. The territories are the signals every audit reads for and the lens the system uses to check coverage. Generation captures liberally and never pre-kills; the grading pass at `prompts/open-loops/open-loops-roll-up.md` runs the verdict template, consolidates, scores on the four weights, and routes. Loops route to two outcomes:
- `promoted/[year-month]/` — loops that cleared the verdict template and got elevated for hypothesis formation
- `archived/[year-month]/` — loops that were cut, with the reason

Open loops are not data-pull gaps. They are strategic forks where the answer would route to two materially different futures. Data hygiene issues belong in each doc's frontmatter `data_limitations` field, not in open loops.

### `hypotheses/` · `[partial]`
Scaffolded across all brands 2026-06-10; structure and README on disk, no entries yet. Open loops that became formed hypotheses — structured into a specific claim, the test that would confirm or disconfirm it, and the success criterion. Three states:
- `tested/[year-month]/` — hypotheses that have been run, awaiting validation verdict
- `denied/[year-month]/` — hypotheses Parker proposed that the user rejected, with the reasoning preserved so future passes do not re-propose the same shape
- `awaiting-user/[year-month]/` — hypotheses queued for user sign-off before they go to test


### `validations/` · `[partial]`
Scaffolded across all brands 2026-06-10; no entries yet. Hypotheses that have been tested, with the verdict and the evidence. Four verdict states:
- `validated/[year-month]/` — confirmed, with the research that grounds it. These are the brand's most important reads going forward.
- `invalidated/[year-month]/` — disconfirmed, with the reason. The brand should not re-propose this shape.
- `insufficient-evidence/[year-month]/` — could not be resolved with what was available, with the specific gap named so a later pull can close it
- `inconclusive/[year-month]/` — tested but the read is mixed, requiring a sharper test design

The `recent-validations.md` file inside `brand-notes-from-org/` summarizes the freshest verdicts in narrative form; the validations folder carries the depth and the receipts.

### `re-validations/` · `[partial]`
Scaffolded across all brands 2026-06-10; no entries yet. Validations that have a re-test scheduled because the underlying signal may decay:
- `scheduled/` — upcoming re-tests with the trigger condition
- `results/[year-month]/` — completed re-tests with the verdict


### `strategy/` · `[partial]`
Phase 2 of the operating model. Holds the two decisions made once the audit is complete and presented to the user for approval: `product-priority.md`, the WHAT — the lead SKU or the next-swing vector, and `strategic-roadmap.md`, the diagnosis plus the top-3 priorities that gate Phase 3. Produced by the prompts in `prompts/strategic-roadmap/`. Scaffolded across all brands 2026-06-10; the deliverables generate once the audit is approved.

### `idea-bank/` · `[built]`
The brand's idea memory — reusable ad ideas, concepts, hooks, and formats worth stealing, captured as one folder per idea under `entries/` with an `index.md` roll-up. Scaffolded across the early brand brains, populated for some and empty for others. This is idea memory, not strategy: entries carry the novelty check, the reasoning, the why-now, the source examples that teach the idea, and the spark — the one-breath brand collision recorded at the moment of noticing when it arrives naturally — but never the build (no storylines, variations, scripts, or briefs; that is concepting). Entries also carry their hunt lane, so the weekly evaluation can read coverage per lane. Filled by the structured weekly hunt (`harvest-ideas`: hunt brief, cold pass, hunter lenses including the far-transfer wildcard and the trend lane) and by incidental capture during other work. New entries land as `[~]` proposed and become trusted taste only on Jimmy's approval. The reusable cross-brand counterpart lives in the knowledge tier at `creative-strategy-context/parker-taste/idea-bank/`.

### `sprints/` · `[partial]`
Phase 3 rounds. A sprint is the container for one planned creative round, and briefs nest inside it. Each `sprints/[YYYY-MM-DD]-[sprint-slug]/` holds a `sprint-plan.md` — the round sized from the account's spend and net-new-evergreen cadence, split across SKUs and personas, with the concept map every brief builds from (produced by `prompts/ideas-and-briefs/sprint-plan.md`) — a `briefs/` folder of execution-ready concepts built from that map (`prompts/ideas-and-briefs/brief-creation.md`, each carrying its variations, creator direction, and the three validations of data, inspo, and strategy), and a `retro.md` that feeds the next round's sizing. Ad-hoc co-pilot briefs with no planned round behind them land in `sprints/_unplanned/briefs/`. Gated on an approved strategic roadmap. Empty until the first round is planned.

### `prompts-run-log/` · `[built]`
Operational record of which prompts were run when, against which inputs, with which outputs.

---

## Team tier — `z-brands/[brand-id]/teams/[team]/` · `[planned]`

> Status: no brand has a `teams/` directory yet. Creative-strategy context currently lives flat in the brand's `sub-context-docs/` and in `creative-strategy-context/`, not under `teams/creative-strategy/`. This whole tier is the target shape; treat every surface in it as `[planned]`.

The brand surface library above is the foundation every team reads. The team tier is what makes a brand's intelligence team-specific. Parker v2 is architected for eight marketing teams under shared foundation. V1 ships creative-strategy only; the other seven come online as each team's context and knowledge populates.

### Teams in the architecture
Creative strategy is the v1 team. The other seven are performance, organic social, search, influencer, brand PR comms, partnerships, and retention. Each team owns its own profile, its own sub-context docs, its own internal and external and landscape folders, its own skills, and its own knowledge docs.

### `teams/[team]/profile.md`
The team's identity and how it operates inside this brand.

### `teams/[team]/sub-context-docs/`
Team-specific texture the cross-team foundation does not carry. For creative strategy, four docs — creative-strategy posture is how the brand currently frames its creative bets, creative history is what the brand has tested over time and what has worked, format inventory is the brand's running catalog of which ad formats sit in rotation, and creative diversity state is the read of where the brand's portfolio is concentrated or spread.

### `teams/[team]/landscape/`
The team's read of the outside world. For creative strategy, includes the expert-takes-on-category synthesis.

---

## Skill library — `.claude/skills/`

Skills do the work at runtime. They live under `.claude/skills/` because that is the only directory Claude Code loads skills from — a folder anywhere else is inert markdown a clone never registers — so this is what lets a cloned repo (factory or brand brain) pick the skills up and invoke them. Each skill folder carries the same four-part anatomy: `SKILL.md` is the entry point and trigger surface, `strategy.md` is the reasoning layer that decides which process applies to a given query, `processes/` holds the specific playbooks the strategy picks from, and `references/` holds the supporting docs and examples the processes draw on. The post-launch architecture still intends to namespace skills by team; the v1 build keeps them flat under `.claude/skills/` and tags each with its team. New skills are checked at creation against the birth principles in `update-parker-skill` — the two ship gates for creative deliverables, structural over instructional enforcement, canonical-doc-plus-reference, register-matched customer language, provenance, and the ship-list check.

Every skill listed below is `[built]` and present under `.claude/skills/`.

### `scriptwriting/`
Writes scripts for video ads. Loads brand context, runs against the script-adaptation playbook, picks a process based on whether the script is being adapted from a reference or built net-new.

### `hooks/`
Writes opening lines, first frames, and on-screen text for hooks. Loads brand voice, ICP, personas, VoC, hook history. Routes to a hook-format process based on the brand's gap and the candidate format.

### `headlines/`
Writes headlines for statics. Loads brand context, runs the lifestyle or problem-solution headline process based on the static type.

### `iterations/`
Recommends high-confidence iterations on a performing ad. Five processes — audience iteration, edit-pacing iteration, hook iteration, messaging-angle iteration, static-headline iteration. Loads brand context plus the ad's performance data plus the iteration history.

### `ad-account-analysis/`
Reads what the Meta data is actually saying — account audit, single-ad diagnosis, placement read, demographic breakdown, fatigue check. Routes to a process based on the question shape.

### `ai-ad-generation/`
Generates AI-assisted ad creative. Static and video.

### `update-parker-skill/`
Meta-skill for updating other skills based on user feedback and new patterns.

### `expert-signal-intake/`
Draft-first intake for any expert knowledge source Jimmy provides. Classifies the source against the four components a skill is made of — context docs, knowledge docs, tool calls, processes — decides which it updates, and drafts that change at its real surface marked `[~] pending review`, rather than leaving it in an inbox. Separates expert claim from Parker inference, records source limits, and makes the idea-bank routing decision. Canonical spec is `prompts/global-databases/expert-signal-db.md`.

### `brand-idea-bank-maintenance/`
Maintains the brand and cross-brand idea banks. Runs the novelty check before any new entry, keeps entries as idea memory rather than strategy, and holds proposed entries at `[~]` until Jimmy approves them to trusted taste.

### `self-improvement-intake/`
Captures reasoning traces from normal conversation. Use when Jimmy says to remember something, make something a rule, explains why an output is wrong, approves or rejects a direction for a reason, reroutes content, or asks Parker to get better from the conversation.

### `improve-system/`
The application arm of self-improvement, invoked by the user with `/improve-system`. Where `self-improvement-intake` captures traces, this skill reads the accumulated reasoning traces and folds the promotable ones into one brand's and one user's living context — brand-profile, brand-rules and the running-notes children, user-profile, and brand-notes-from-user. Applies what meets a promotion condition, drafts the plausible as `[~] pending review`, leaves thin traces in the queue, and surfaces skill, prompt, and system-scoped traces for their own promotion route. Obeys `self-improvement-system.md`.

### `dream/`
The on-demand brand runner for the dreaming system, invoked with `/dream`. Reads the brand's conversations and tribal knowledge and comes back with proposals framed as the morning suggestion: context updates, skill gaps, new ideas routed to the idea bank, and workflows worth scheduling. Proposes, never applies — everything lands under `z-brands/[brand]/dreaming/` and `z-brands/[brand]/workflows/proposed/` for human-in-the-loop promotion. Runs brand dreaming and workflow detection only; global product dreaming stays the offline cross-brand stream. Canonical method is `dreaming-system.md`.

### `.claude/agents/context-grounding-review.md` · `[built]` — an agent, not a skill
The grounding gate, and the first of the two ship gates (it changes content; the voice gate changes lines). The five creative skills spawn it on every finished draft before the voice review. It reviews as a **peer strategist, not a citation checker**: its first move is reading the method docs the task routes to — end to end, the same reads the generator owed — so its judgment happens through the methods' own reasoning rather than general marketing opinion. Then it runs the deterministic checks (`scripts/grounding-check.py`: quoted verbatims trace to the vault, cited sources exist on disk, receipts present) and reviews on three dimensions: the right context loaded and pulled (vocabulary evidence, not claimed sources), nothing fabricated, and the methods **applied, not just opened** — every misapplication finding must cite the doc passage it violates, and where a method leaves a call to judgment, the writer's call stands. Returns `grounded` or `bounced` with missing loads, missing pulls, and misapplications named; a bounce means re-pull and regenerate. This is the routing map's closing test made independent instead of self-graded, and every bounce is reasoning-trace material for how the planner should have routed.

### `.claude/agents/creative-voice-review.md` · `[built]` — an agent, not a skill
The independent ship gate for creative copy. The five creative skills (`scriptwriting`, `headlines`, `hooks`, `ai-ad-generation`, `iterations`) spawn it on every finished draft; it runs the deterministic tells scan (`scripts/voice-lint.py`), judges the flags against the brand's voice profile per the doctrine at `creative-strategy-context/ai-writing-tells.md`, catches what regex can't, and returns per-line verdicts with rewrites in the brand's register — never touching hook format, framework beats, claims, or sourced customer language. Its verdict appears in each output's required Voice Review block. It is a subagent definition, not a skill: a fresh reviewer context so the writer never grades its own draft. Ships to brand brains as a trio with the linter and the doctrine doc.

---

## Knowledge tier — domain reasoning docs

Knowledge docs hold the field-level expertise. They are not brand-specific and they are not skill-specific. They are the canonical thinking on a domain. Today these live at `creative-strategy-context/`; the post-launch architecture moves them under `global/teams/[team]/knowledge/` per team plus a `global/knowledge/` tier for cross-team principles.

### `creative-strategy-context/` · `[built]`
The current home of creative-strategy domain knowledge. Holds the canonical reads on scriptwriting principles, hook frameworks, headline generators, ad-format taxonomies, AI-assisted ad generation, video prompting, persona-to-roadmap process, adaptation playbooks, the old-ads corpus (`old-ads/` — the historical print-ad swipe library the weekly hunt's historian lens digs, organized by industry and mechanic), and the voice doctrine pair — `spoken-script-voice.md` for the spoken register and `ai-writing-tells.md` for the written AI-slop signs, the latter enforced at ship time by the `creative-voice-review` agent and `scripts/voice-lint.py`.

### `creative-strategy-context/expert-insights/` · `[built]`
The provenance and review-queue layer for expert knowledge sources. Working knowledge from a source is drafted into the context and knowledge docs Parker actually retrieves from; this folder holds only the saved signal, the source limits, and a single review-queue pointer per intake, plus the `context-update-candidates/` that wait for corroboration before promotion. Paired with the `expert-signal-intake` skill and the `expert-signal-db` spec.

### `creative-strategy-context/parker-taste/` · `[built]`
Reusable cross-brand creative taste — the patterns that recur across brands and the cross-brand `idea-bank/` of ideas worth stealing anywhere, plus `patterns-to-monitor/` for signals not yet confirmed as taste. The reusable counterpart to a brand's own `idea-bank/`. Entries are proposed `[~]` and become trusted taste only on Jimmy's approval.

### `global/knowledge/performance/` · `[partial]`
The performance (media-buying) knowledge tree — the second team to come online after creative-strategy, because media buyers are a real and growing share of Parker's users. One canonical doc is seeded: `incrementality-and-lift.md` (`[~]` pending review) — the read on incrementality vs attributed credit, conversion-lift / holdout testing, the three-layer measurement stack, and the measurement rhythm. The other named performance docs (attribution-and-privacy, account-structure-principles, platform-mechanics-meta, pacing-and-budget-rhythms, and the rest) are `[planned]` and fill in as corroboration arrives.

### `global/knowledge/performance/expert-insights/` · `[built]`
The provenance and review-queue layer for media-buying expert sources, mirroring the creative-strategy intake. Adds one discipline: numeric claims about money stay `stated` until grounded in account data or a second source. Seeded 2026-06-18 with the Meta Performance Summit signal, which stood up the tree.

### Forward direction
The remaining teams each get their own knowledge tier as they come online — organic-social knowledge, search knowledge, influencer knowledge, brand-PR knowledge, partnerships knowledge, retention knowledge. A global knowledge tier holds the cross-team principles that any team may need.

---

## Tools tier — what Parker can call out to · `[built]`

Tools are the external integrations Parker can invoke at runtime when a question requires fresh data rather than what is already on disk. The Parker MCP tool surface is live; the formal in-repo registry described under Forward direction is `[planned]`.

### Tool categories
Ad library readers cover Meta, TikTok, and the public surface of the platforms Parker mines. Customer review readers cover the brand's first-party review surface, third-party review sites, and the reddit and forum surface. Ad account readers cover the brand's Meta and TikTok ad accounts where authentication is set up. Search and SERP readers cover Google and the brand's category keyword universe. Database tools cover the global ad databases the brand has curated.

### Forward direction
Tool integrations expand as the team grows. The exact tools available at any moment live in a tools registry the runtime resolves.

---

## Prompt library — `prompts/` · `[built]`

The prompts that generate the brand surfaces above. Prompts produce context. They are not typically consumed at runtime.

- `audits-*/` — the 17 audit prompts organized by cadence
- `brand-profile/` — the 14 brand sub-context prompts plus the synthesis
- `competitor-profile/` — the 9 competitor sub-context prompts plus the snapshot and working-thesis synthesis
- `personas/` — the persona source-pull prompts, the synthesis, the voice and emotion companion, lifecycle maps, and the bias passes
- `voice-of-customer/` — the corpus profile, 9 VoC extraction prompts, and the assembly
- `market-synthesis/` — `gaps-opportunities-inspo.md`, the quarterly market read
- `global-databases/` — prompts that build cross-brand reference databases
- `open-loops/` — `open-loops-roll-up.md`, the grading stage: collects every doc's loops, runs the verdict template, consolidates by territory, scores on the four weights, and routes to promoted, backlog, brand-routed, or archived
- `_open-loops-core-block.md` — the single source for the open-loops rubric block embedded verbatim in every context-doc prompt, synced by `scripts/sync-open-loops-core.py`

---

## System-level references — `parker-v2/` · `[built]`

Methodology documents that govern how Parker reads the brand surfaces.

- `creative-strategy-context/analyzing-public-ad-accounts.md` — the canonical read on how to analyze public ad accounts
- `creative-strategy-context/customer-review-mining-method.md` — the canonical read on how to mine customer reviews
- `creative-strategy-context/persona-research-and-creative-strategy-process.md` — the process bridge from persona research to diagnosis, roadmap, and sprint execution
- `system/attribution-principle.md` — the attribution metadata schema every doc carries (locked 2026-06-08: inline in the markdown)
- `system/open-loops-system.md` — the open-loops pipeline architecture
- `self-improvement/self-improvement-system.md` — the reasoning-trace capture, routing, curation, and promotion method
- `self-improvement/dreaming-system.md` — dreaming, the proactive mode: brand dreaming, workflows, and anonymized global product dreaming
- `system/master-file-structure.md` — the canonical file tree for the whole system
- `system/master-prompt-review.md` — the rubric for reviewing any prompt

---

## The thinking step

Before any skill runs, Parker runs the thinking step. The thinking step is the highest-leverage reasoning move in the system. Its job is to decide what to pull, not to do the work.

Inputs to the thinking step:
- The user's current message
- The four memory documents
- The recent 100 messages
- This system map

The reasoning move:
- What is this user actually asking?
- What thread of work does this query belong to, based on `brand-notes-from-user` and the conversation history?
- What is the brand's current pulse, based on `brand-notes-from-org` and the recent-validations summary?
- What would change Parker's answer? What is freshest? What is in tension with the query? What would surprise the user? What contradiction does Parker want to hold?
- Which surfaces from the brand surface library would a senior strategist open before touching this question?

Output of the thinking step:
- A bespoke pull list with rationale per pull, ordered by priority
- Permission to re-pull mid-flight if the work surfaces a gap the initial pull did not cover

The pull list is not exhaustive. A senior strategist opens four surfaces, not forty. The thinking step is strategic — it pulls what would change the answer and ignores what would only pad the context.

---

## What this document is not

This is not the full inventory of files for any brand. It is the schema. For the brand-specific instance — which audits have actually been run, which validations are fresh, which open loops are promoted — the live filesystem of `z-brands/[brand-id]/` carries the answer, alongside the freshness signals in each doc's frontmatter.

This is not a document the user reads. It is Parker's own awareness layer.

---

## Keep this map living

This document evolves with the system. When a new surface enters the brand library, a new skill ships, a new audit cadence is added, or a new pipeline state is introduced, this map gets updated in the same commit. A map that drifts from the filesystem is worse than no map at all, because the thinking step will reason against a fiction.

Triggers for updating this map:

- A new skill is added under `.claude/skills/`. Add an entry to the skill library naming what the skill does and what it loads.
- A new audit prompt or audit cadence is added. Update the audits subsection in the brand surface library to name the new cadence and what its output is for.
- A new sub-context doc is added or an existing one is split. Update the sub-context-docs entry to reflect the new shape.
- A new memory document is added or an existing one is split. Update the memory tier section.
- A new self-improvement trace category, routing rule, or promotion state is added. Update the self-improvement memory and system-level references.
- A new pipeline state is added to the open-loops, hypotheses, or validations folders. Update the corresponding entry.
- A new methodology doc lands under `parker-v2/`. Add it to the system-level references section.
- A new domain knowledge doc lands under `creative-strategy-context/` or the team-namespaced knowledge tiers. Update the knowledge tier section.
- A new tool integration comes online. Update the tools tier section to name the category and what the tool returns.
- A new team comes online inside a brand. Update the team tier section to name what the team owns.
- The thinking step's reasoning move changes. Update the thinking step section.

When updating, preserve the structure and append or refine inside the relevant section. Do not rewrite the map from scratch. Note the date in the update log so the evolution carries its own history.

The map's job is to stay current. The thinking step's job is to reason against it. The two together are what makes Parker living.

---

## Update log

| Date | Change |
|---|---|
| 2026-06-02 | Initial draft. Names the memory tier, the brand surface library, the skill library, the open-loops and hypotheses and validations pipeline, the system-level references, the thinking step, and the maintenance discipline. |
| 2026-06-02 | Added the team tier, the knowledge tier, and the tools tier. The map now spans every layer Parker can reach across, from memory through brand surfaces through team surfaces through skills through domain knowledge through tools through prompts through system-level references. Maintenance triggers expanded to cover the three new tiers. |
| 2026-06-02 | Future-pass note: the map currently lists tool categories rather than enumerated tools, and teams beyond creative strategy as the planned shape rather than as live surfaces. As tools register and teams come online, those sections need to deepen from category descriptions into named entries. |
| 2026-06-02 | Stripped the per-surface "Pull when..." instructions so the model reasons about pulling on its own rather than following hardcoded routing rules embedded in each surface description. |
| 2026-06-02 | Thickened the descriptions on `brand-notes-from-org`, `voice-of-customer`, `source-pulls`, `competitors`, `open-loops`, `hypotheses`, `validations`, the Skill library intro, and the creative-strategy team sub-context so Parker can see what each surface carries without having to navigate into it. |
| 2026-06-03 | Added the self-improvement layer: `self-improvement/self-improvement-system.md`, `self-improvement/` reasoning traces, and the `self-improvement-intake` skill. Parker now has a file-backed way to preserve why corrections and strategic decisions happened. |
| 2026-06-04 | Added dreaming as the proactive mode of self-improvement, documented at `self-improvement/dreaming-system.md` under the self-improvement folder. Brand dreaming + workflows at `z-brands/[brand]/dreaming/` and `z-brands/[brand]/workflows/`, anonymized global product dreaming at `self-improvement/product-signals/`. Self-improvement now has a reactive mode (traces) and a proactive mode (dreaming). |
| 2026-06-04 | Organized loose top-level docs into parent folders: `system/` (map, file-structure, prompt-review, attribution-principle, open-loops-system), `planning/` (roadmap, ce-build-tracker), `templates/` (personas + voc templates and design), self-improvement docs into `self-improvement/`, method docs into `creative-strategy-context/`. Removed `audits/`. All path references rewritten. |
| 2026-06-08 | Added two user-invoked global skills. `improve-system` (`/improve-system`) is the application arm of self-improvement: it reads the accumulated reasoning traces and folds the promotable ones into one brand's and one user's living context. `dream` (`/dream`) is the on-demand brand runner for the dreaming system: it reads the brand and returns morning-suggestion proposals. The self-improvement layer now has capture (`self-improvement-intake`), application (`improve-system`), and generation (`dream`). |
| 2026-06-10 | **Three-phase model + brand-tree reconcile synced.** Added the three-phase lifecycle to "How Parker thinks." Brand surfaces updated: `strategy/` (Phase 2) and `briefs/` (Phase 3) added; the loop pipeline (`hypotheses/`, `validations/`, `re-validations/`), `personas/{sources,voice-of-customer}/`, and per-brand `dreaming/`+`workflows/` flipped `[planned]`→scaffolded across all brands; `idea-bank/` now all three brands; VoC nested under `personas/`; `sub-context-docs/` retargeted to the folded 11. |
| 2026-06-08 | **Build-status pass after a drift audit against the filesystem.** Added the build-status legend (`[built]`/`[partial]`/`[planned]`) and tagged every surface. Key corrections: the always-loaded memory tier is mostly `[planned]` (only `brand-profile.md` is built; `users/` memory and org running-notes do not exist yet); team tier, `hypotheses/`, `validations/`, `re-validations/`, and per-brand dreaming/workflows folders are `[planned]`; `sub-context-docs/` is `[partial]` (11 of a 14-target, different set); VoC currently sits at brand top level, not nested under `personas/`. Added surfaces the map had omitted: brand `idea-bank/`, the `expert-signal-intake` and `brand-idea-bank-maintenance` skills, and the `expert-insights/` and `parker-taste/` knowledge surfaces. |
| 2026-07-07 | **Phase 3 gains a sprint-plan step, and briefs move under sprints.** Added `prompts/ideas-and-briefs/sprint-plan.md` between `idea-evaluation` and `brief-creation` — it sizes the round from account spend + net-new-evergreen cadence, splits it across SKUs and personas, sets variation counts, and emits the concept map. Phase 3 is now four prompts (capture → evaluate → plan → build). The brand `briefs/` surface became `sprints/`: a sprint is the container, holding `sprint-plan.md`, a nested `briefs/`, and `retro.md`; ad-hoc co-pilot briefs live in `sprints/_unplanned/briefs/`. Grounded in senior-strategist concepting transcripts; the method is in `creative-strategy-context/ideation-and-brainstorming.md`. |
| 2026-06-08 | Scaffolded the `users/` memory tier so `/improve-system` has real targets. `users/jimmy/user-profile.md` plus `users/jimmy/[brand]/brand-notes-from-user.md` for early brand brains, as `[~]` skeletons carrying their section structure and awaiting onboarding + accumulated traces. |
| 2026-06-18 | **Performance (media-buying) knowledge tree comes online** — the second team after creative-strategy. Added `global/knowledge/performance/expert-insights/` (`[built]`, mirrors the creative-strategy intake with an added "numbers stay stated until grounded" discipline) and the first canonical performance doc `incrementality-and-lift.md` (`[~]` seeded). Knowledge tier section updated; remaining performance docs `[planned]`. Driven by the 2026-06-18 Meta Performance Summit expert signal. |
| 2026-07-03 | **User-profile foundation — the user layer, mirroring the brand system.** Built the role-flexible `templates/user-profile-template.md` (who they are, their process, their craft, how they like Parker to work, the standing rules they've set with the full verbatim moment that caused each, current focus, what's landed, open questions) and wired it always-loaded: the context hook injects the whole profile every turn when it exists, and the brand `CLAUDE.md` map names it as a read to honor on every reply. No onboarding questionnaire — it builds from usage. A user-learning rolls up into ops, team, and org notes. `user-profile.md` moved `[planned]` → `[partial]`. The reactive + nightly user-dreaming loop that populates it, and the verbatim-full-moment capture rule across that loop, is the next phase. |
| 2026-07-03 | **Strategy-first baseline for tactical execution.** The five creative skills now load the brand's committed strategy (`strategy/` — working thesis, roadmap calls) as the frame before any tactical work, and check the idea bank (including evaluated ideas) for the entry a request should execute from — a matched entry executes with its reasoning carried, a request that cuts against the committed strategy is surfaced with the conflict named rather than silently executed, and a fresh brain without those surfaces says so in one line. The grounding reviewer reads `strategy/` and `idea-bank/` in its become-the-strategist pass and flags strategy contradictions (cited to the strategy passage, never its own strategic taste) and obviously-matched-but-unused idea-bank entries. Birth principles gain strategy-first and the independent-*and-equipped* reviewer standard. |
| 2026-07-03 | **The grounding agent becomes a peer strategist.** From Jimmy's correction that the reviewer wasn't equipped to judge whether output sounds like a creative strategist: `context-grounding-review` reshaped so its first move is reading the routed method docs end to end — learning the craft before holding anything to it — and its review gains the applied-not-just-opened dimension: a new MISAPPLIED METHODS section where every finding must cite the doc passage the output violates (hook diagnosed without naming the job it fails, iteration on a high-ROAS-low-spend ad against the selection doc's warning, blended references against the 1:1 rule). Guardrail: misapplication means contradicting what a doc states; judgment calls the method leaves open stay the writer's. `grounded` now also requires no recommendation-changing misapplication. |
| 2026-07-03 | **Register-translation rule + skill birth principles.** `spoken-script-voice.md` gains the written-vs-spoken customer-language rule: written verbatims (reviews, surveys, threads) ship as-is in written deliverables and get *voiced* into spoken scripts — same vocabulary, re-cadenced for the mouth with in-register disfluencies — with the exact written verbatim carried in the Script Brief's VoC phrases so provenance survives the voicing. Both review agents made register-aware (the voice gate flags pasted written cadence in spoken work; the grounding gate traces voiced lines through their paired brief verbatim). `update-parker-skill` gains "Principles every new skill is born with" so future skills inherit the gates, the structural-enforcement stack, canonical-doc-plus-reference, the register rule, provenance, and the ship-list check at creation time. |
| 2026-07-03 | **The grounding gate lands beside the voice gate.** New subagent `.claude/agents/context-grounding-review.md` and deterministic checker `scripts/grounding-check.py` (verbatim trace against the vault, cited-source existence, receipt presence). The five creative skills now run two gates in order: grounding first (was the output built from the right method docs, brand context, and pulls — `bounced` means re-pull and regenerate), voice second (does it read human). Each carries a required receipt block (Grounding Review, Voice Review). `expertise-routing.md`'s closing test is now enforced by the agent rather than self-graded; sign-off stamps become corroboration the gate verifies. Ships to brand brains in the same bundle as the voice gate. Rationale: self-attested loads and sign-offs are the instructional pattern; the gate creates the consequence for under-pulling that bakes the routing instinct in, with bounces feeding the self-improvement loop. |
| 2026-07-03 | **The creative voice-review gate lands.** New knowledge doc `creative-strategy/ai-writing-tells.md` (the written AI-slop signs, generalized from Wikipedia: Signs of AI writing, with the false-positive discipline), new deterministic linter `scripts/voice-lint.py`, and new subagent `.claude/agents/creative-voice-review.md` — the first entry in `.claude/agents/`. The five creative skills (`scriptwriting`, `headlines`, `hooks`, `ai-ad-generation`, `iterations`) now carry a mandatory ship gate: spawn the reviewer on the finished draft, fix to a `ships` verdict, and carry the receipt in a required Voice Review output block. Enforcement is structural — deterministic lint the model can't argue with, a reviewer context that didn't write the draft, and an output contract that makes a skipped gate visible. Ships to brand brains via the onboarding-runner ship step and the propagate deliberate-adds list. Wired into `expertise-routing.md`; `spoken-script-voice.md` stays canonical for the spoken register. |
| 2026-07-10 | **Git simplification + hard enforcement (v6).** The v5 token-in/token-out remote bracket is retired — credentials now live in `origin` and an auth error means the two-line refresh (`setup_parker_brain` → `set-url` → retry); rationale recorded in `system/brain-git-sync.md`. Enforcement moved to where the failures happen: `session-start.py` now *runs* the start-of-session pull itself when the tree is clean (loud, actionable failure otherwise), and `save-brain` + the brand `CLAUDE.md` template state the never-ask mandate as prompt-level absolutes — every change commits and pushes immediately, asking permission to save is itself a failure, every file-touching turn ends with a clean-and-pushed self-check, and only an explicit user "don't commit" overrides it (a Stop-hook enforcer was built and deliberately dropped: blocking guards risk trapping turns behind persistent git errors and can't see the user's override). Factory policy change alongside: every release ships its `migrations/vN.md`, with one-liner no-ops for method-only releases. |
| 2026-07-10 | **Factory tags synchronize only during `/update-brain` (v7).** The session-start and save flows stay focused on the brand repo and the checked-out submodule pin; neither needs release-tag refs. Before it discovers the latest factory release, `/update-brain` now runs `git -C parker-system fetch origin --prune --prune-tags`, which replaces moved tags and removes deleted ones so an old local ref cannot block or distort the comparison. The hook settings also fail open when a script is missing or the session is launched off-root, while preserving `git-guard` blocking when the guard script is present. The session hook's expired-credential behavior is unchanged: it reports the failure and instructs the agent to call `setup_parker_brain`, update `origin`, and retry before work. |
| 2026-07-10 | **The token leaves the shell (v8).** Claude Code's permission classifier blocks any Bash command carrying a live token, which killed v6's refresh (`set-url` with the tokenized URL) and tokenized clones on default permissions. Credentials move to git's store file `.git/parker-credentials` — one line, written with the Write tool, never transiting a shell command — with `origin` on the plain URL and a one-time two-entry wiring (a blank `credential.helper` entry that shuts out the user's own keychain helpers, then `store --file .git/parker-credentials`); clones ride a temp credential file via the same double `-c` pattern. `git-guard.py` now blocks raw-token commands and helper-less managed clones, and accepts the file (or a legacy token-in-origin) as credentials. `save-brain`, `session-start.py`, the brand `CLAUDE.md` template, the onboarding runner, and both bundle READMEs re-pointed at `/save-brain` as the one full procedure; history and rationale in `system/brain-git-sync.md`, which also names the cross-repo duty: the `setup_parker_brain` tool message still teaches the blocked flow and must catch up. Ships as `v8` with real-step `migrations/v8.md` (flip origin to the plain URL, wire the helper, mint the file). |
| 2026-07-10 | **The git procedure: `save-brain` + `git-guard`.** Agents kept mishandling git in brand brains (user's own login, `gh`, bare `git push`, submodule-less clones, expired 1-hour tokens left in the saved remote). New routine-bundle skill `save-brain` carries the canonical procedure — credentials minted fresh from `setup_parker_brain` each time, explicit `git push origin main` bracketed by token-in/token-out on the remote, pull-with-submodules before work, commit often push immediately, conflicts best-effort keeping both sides, never `gh`/force-push/branches, self-hosted exception detected from the origin URL — and new PreToolUse hook `git-guard.py` enforces it deterministically at the moment of the mistake (fails open; block messages teach the fix). Brand `CLAUDE.md` template gains the always-loaded "How this brain saves itself" section; maintainer rationale in `system/brain-git-sync.md`. Ships as `v5` with `migrations/v5.md` (stamps the CLAUDE.md section, patches team-customized settings.json). |
| 2026-07-10 | **The fast update: `/update-brain`'s copied-layer re-sync becomes a script.** New `scripts/sync-executable-layer.py` — the machine-readable twin of the onboarding-runner's copy list — re-syncs a brand brain's copied executable layer (craft + routine skills, review-gate agents, hooks, checker scripts, schedule recipes) on every pin bump by hash-comparing each copy against the old pinned tag: untouched files refresh silently, team-edited files stay theirs and are listed, nothing is deleted. The update-brain routine template drops per-file interactive offers for a single short release question ("Keep it quick" contract), and its canonical-build hole walk becomes a silent existence check (one digest line, generation on explicit ask only). `migrations/README.md` gains the division of labor: migrations run first and never touch bundle-map paths, the script runs once at the end. Ships as `v4` with `migrations/v4.md`. Rationale: a no-op release bump was taking 5+ minutes of hand-diffing and long questions. |
| 2026-06-19 | **Ad-selection added as Phase A of the `iterations` skill.** New context doc `creative-strategy/selecting-ads-to-iterate-on.md` (the selection method: spend judged in account context, run time, the breakdown effect, the promo-top-spender caveat, slow-burner vs high-riser, 60-day account trends). The `iterations` skill now owns the full flow in two phases: Phase A chooses which ads to iterate on (from the selection doc) and Phase B makes the iterations (from `iterations.md`). Entry routing: a named ad goes straight to Phase B; an account-level "what should we iterate on" runs Phase A → checkpoint → Phase B. (The briefly-separate `select-ads-to-iterate` skill was folded in.) Wired into `expertise-routing.md`. |
