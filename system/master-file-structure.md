# Parker v2 — Master File Structure

Updated 2026-06-03.

This is the canonical file tree for Parker v2. Evolved from the 2026-05-12 baseline through the 2026-05-18 personas reorg, the 2026-05-21 sub-context reorg, and the 2026-05-28 **teams expansion** — Parker now serves 8 marketing teams under a shared foundation.

---

## Loading sequence

1. **Always loaded** on every user message:
   - Recent 100 messages from chat-history
   - `brand-profile.md`
   - `running-notes/brand-notes-from-org.md`
   - `running-notes/refresh-schedule.md` — the aggregated freshness view, so Parker can flag a stale doc on any turn without opening it (see `system/refresh-cadence.md`)
   - `user-profile.md`
   - `brand-notes-from-user.md` per user, per brand

2. **Planner step** — Parker decides (a) which team's context is in play and (b) whether a skill is needed. The planner reads team profile YAML frontmatter and skill YAML frontmatter to pick.

3. **Team-driven loads** — when a team is active, load:
   - `teams/[team]/profile.md`
   - `teams/[team]/notes-from-org.md` (team-aware brand memory)
   - `users/[user]/[brand]/teams/[team]/notes-from-user.md` (team-aware user memory)
   - Plus any team-specific `sub-context-docs/` the picked skill references

4. **Skill-driven loads** — picked skill's SKILL.md, then strategy.md, then picked process file, then only the components that process actually references.

5. **Voice of Customer loads** — customer-facing skills additionally load `personas/voice-of-customer/voice-of-customer.md` and filter by the `identity_tag` and `behavioral_signal_tag` the skill is targeting.

`/memory/` is not a folder. It is the always-loaded subset assembled by application code before calling the LLM.

---

## The tree

```
parker/
│
├── users/                                          ← Per-user state
│   └── [user-id]/
│       ├── user-profile.md                         ← Role + onboarding answers + working prefs
│       └── [brand-id]/                             ← Per-user, per-brand
│           ├── brand-notes-from-user.md            ← How THIS user engages with THIS brand (cross-team)
│           ├── teams/                              ← Per-user, per-brand, per-team
│           │   ├── creative-strategy/notes-from-user.md
│           │   ├── performance/notes-from-user.md
│           │   ├── organic-social/notes-from-user.md
│           │   ├── search/notes-from-user.md
│           │   ├── influencer/notes-from-user.md
│           │   ├── brand-pr-comms/notes-from-user.md
│           │   ├── partnerships/notes-from-user.md
│           │   └── retention/notes-from-user.md
│           └── chat-history/
│               ├── [YYYY-MM]/[conversation-id].md
│               └── summaries/
│                   ├── [YYYY-MM]-monthly.md
│                   └── [YYYY]-yearly.md
│
├── z-brands/                                         ← Per-brand context (the heavy half). This per-brand tree is the buildable CORE, not a closed set: a standing brain grows new first-class surfaces (email, SEO, PR, support, whatever the org connects) per system/growing-the-brain.md
│   └── [brand-id]/
│       │
│       ├── brand-profile.md                        ← MAIN — narrative synthesis of foundation
│       │
│       ├── sub-context-docs/                       ← FOUNDATION (11 docs) — every team reads these
│       │   ├── brand-identity-analysis.md          ← + brand guidelines and claims (folded 2026-06-10)
│       │   ├── operations-and-team.md              ← + marketing org and budget (folded 2026-06-10)
│       │   ├── website-and-product-audit.md
│       │   ├── organic-channels-inventory.md       ← inventory only; deep audit in teams/organic-social/
│       │   ├── performance-targets-and-metrics.md  ← scoreboard + channel mix and attribution (folded 2026-06-10)
│       │   ├── reputation-analysis.md              ← in-the-wild perception (was public-perception)
│       │   ├── community-and-forums.md
│       │   ├── customer-journey-and-persona-discovery.md ← renamed from customer-and-persona-discovery 2026-06-10
│       │   ├── category-and-market-research.md
│       │   ├── competitive-landscape.md
│       │   └── marketing-calendar-and-campaigns.md ← active+recent campaigns, seasonal moments, past major campaigns, product launches+collabs
│       │
│       ├── running-notes/                          ← Living docs synthesized from chats
│       │   ├── brand-notes-from-org.md             ← Narrative summary of the 5 below
│       │   ├── current-work.md
│       │   ├── org-and-usage.md
│       │   ├── missing-context.md                  ← the running list of what the brand has not yet told us
│       │   ├── refresh-schedule.md                 ← aggregated freshness view (see loading sequence above)
│       │   ├── success-definition.md
│       │   ├── brand-rules.md
│       │   └── recent-validations.md
│       │
│       ├── strategy/                               ← PHASE 2 — who to target + what to lead with, for approval
│       │   ├── README.md
│       │   ├── product-priority.md                 ← the WHAT: lead SKU or next-swing vector (generated)
│       │   └── strategic-roadmap.md                ← diagnosis + top-3 priorities, the gate into Phase 3 (generated)
│       │
│       ├── idea-bank/                              ← PHASE 3 ideation — brand-specific living idea bank
│       │   ├── README.md
│       │   ├── index.md
│       │   ├── entries/[YYYY-MM-DD]-[concept-slug].md
│       │   └── evaluation-[YYYY-MM-DD].md          ← idea-evaluation: the graded, ranked shortlist
│       │
│       ├── sprints/                                ← PHASE 3 rounds — a sprint is the container; briefs nest inside
│       │   ├── README.md
│       │   ├── [YYYY-MM-DD]-[sprint-slug]/         ← one planned creative round
│       │   │   ├── sprint-plan.md                  ← sprint-plan: sized round + split + concept map (planning columns)
│       │   │   ├── briefs/
│       │   │   │   └── [concept-slug].md           ← brief-creation: concept + variations + creator direction + 3 validations
│       │   │   └── retro.md                        ← round retrospective; feeds the next sprint's sizing
│       │   └── _unplanned/                         ← ad-hoc co-pilot briefs with no planned round behind them
│       │       └── briefs/[concept-slug].md
│       │
│       ├── dreaming/                               ← Brand dreaming (planning arm): proposals from the day's comms, read vs the vault
│       │   ├── README.md
│       │   ├── runs/[YYYY-MM-DD]/                   ← each run's observations
│       │   └── proposals/{pending,applied,dismissed}/[YYYY-MM-DD]-[id].md  ← five-bucket proposals (context/skill/schedule/idea/open-loop) + reasoning
│       │
│       ├── schedules/                              ← Repo-native cron routines that run inside the brain (NOT MCP workflows; see system/schedules.md)
│       │   ├── README.md
│       │   ├── [schedule-slug].md                   ← task, cron cadence, runs, reads/updates, delivers, status, origin
│       │   └── proposed/[schedule-slug].md          ← dreaming-suggested, awaiting user confirmation
│       │
│       ├── workflows/                              ← Recurring automations on the Parker-MCP product surface (distinct from schedules/)
│       │   ├── README.md
│       │   ├── [workflow-slug].md                   ← task, cadence, sources, skills, deliverable, status, origin
│       │   └── proposed/[workflow-slug].md          ← dreaming-suggested, awaiting user confirmation
│       │
│       ├── .claude/                                ← Makes the brain self-running; STAMPED from templates/brand-routines/ at build time
│       │   ├── settings.json                        ← wires the hooks below + "outputStyle": "Parker" (switches on the voice layer) + the deny rules that keep the mount read-only
│       │   ├── output-styles/parker.md              ← Parker's voice as a Claude Code output style — the system-prompt layer; copied out of the mount's .claude/output-styles/
│       │   ├── hooks/craft-context.py               ← injects the live craft catalog + sources-receipt rule every turn
│       │   ├── hooks/git-guard.py                   ← PreToolUse guard on Bash: on parker-brain-org repos blocks the git commands that move history/network/working tree (push, pull, fetch, clone, commit, rebase, merge, reset, restore, checkout, clean, stash, set-url) and gh aimed at the brand repo — Parker Desktop owns the sync, per save-brain; mount ops and read-only git pass
│       │   ├── README.md
│       │   └── skills/{dream,self-improve,research-loops,update-brain,harvest-ideas,evaluate-ideas,refresh-context,save-brain,setup-routines,get-started}/SKILL.md  ← the routine bundle + the on-demand get-started walkthrough (self-contained at runtime, with one exception: update-brain runs the mount's scripts/sync-executable-layer.py on a pin bump to re-sync the copied executable layer deterministically)
│       │
│       ├── personas/                               ← First-class, brand-id level
│       │   ├── personas-profile.md                 ← MAIN — identity-first persona synthesis
│       │   ├── persona-voice-library.md            ← Emotional language companion with verbatim evidence
│       │   ├── lifecycle-journey-maps.md           ← Per-persona lifecycle movement + transition risks
│       │   ├── sources/                            ← 6 source docs that feed personas + VoC
│       │   │   ├── customer-reviews.md
│       │   │   ├── ad-account.md
│       │   │   ├── ad-comments.md
│       │   │   ├── post-purchase-surveys.md
│       │   │   ├── reddit.md
│       │   │   └── other-reviews.md
│       │   └── voice-of-customer/                  ← Nested under personas (same source material)
│       │       ├── voice-of-customer.md            ← MAIN — language-layer synthesis
│       │       ├── voc-corpus-profile.md           ← Measured customer-language corpus spine
│       │       └── phrases/
│       │           ├── pain.md
│       │           ├── outcome.md
│       │           ├── metaphor.md
│       │           ├── objection.md
│       │           ├── aspirational.md
│       │           ├── trigger-moment.md
│       │           ├── surprise-delight.md
│       │           ├── category-jargon.md
│       │           └── anti-language.md
│       │
│       ├── competitors/                            ← 2–3 direct competitor audits
│       │   └── [competitor-id]/
│       │       ├── competitor-snapshot.md          ← MAIN per competitor
│       │       └── sub-context-docs/
│       │           ├── brand-identity.md
│       │           ├── website-and-product-audit.md
│       │           ├── organic-channels-audit.md
│       │           ├── ad-account-evaluation.md
│       │           ├── reviews-and-customer-language.md
│       │           ├── public-perception.md        ← (reputation-analysis)
│       │           ├── community-and-forums.md
│       │           ├── customer-and-persona-discovery.md
│       │           └── running-notes-on-competitor.md
│       │
│       ├── working-thesis-synthesis.md             ← Hypotheses about the state of this brand
│       │
│       ├── teams/                                  ← THE 8 MARKETING TEAMS
│       │   │
│       │   ├── creative-strategy/
│       │   │   ├── profile.md                      ← Team one-pager, loaded when active
│       │   │   ├── notes-from-org.md               ← Team-aware brand memory (loaded when active)
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── creative-strategy-posture.md
│       │   │   │   ├── creative-history.md
│       │   │   │   ├── format-inventory.md
│       │   │   │   └── creative-diversity-state.md
│       │   │   ├── internal/                       ← About this brand
│       │   │   │   ├── 90-day-creative-strategy-audit-[YYYY-Q].md
│       │   │   │   ├── 90-day-performance-audit-[YYYY-Q].md
│       │   │   │   ├── 90-day-diversity-audit-[YYYY-Q].md
│       │   │   │   └── monthly/
│       │   │   │       ├── performance-report-[YYYY-MM].md
│       │   │   │       ├── organic-tiktok-audit-[YYYY-MM].md
│       │   │   │       └── hook-audit-[YYYY-MM].md
│       │   │   ├── external/                       ← About competitors
│       │   │   │   ├── 90-day-creative-strategy-audit-[YYYY-Q].md
│       │   │   │   ├── 90-day-performance-audit-[YYYY-Q].md
│       │   │   │   ├── 90-day-diversity-audit-[YYYY-Q].md
│       │   │   │   └── monthly/
│       │   │   │       └── top-impression-ads-[YYYY-MM].md
│       │   │   └── landscape/                      ← About the market / category
│       │   │       └── gaps-opportunities-inspo.md
│       │   │
│       │   ├── performance/
│       │   │   ├── profile.md
│       │   │   ├── notes-from-org.md               ← team-aware brand memory
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── ad-account-evaluation.md    ← canonical home (creative-strategy reads from it)
│       │   │   │   ├── attribution-reality.md
│       │   │   │   ├── scaling-and-pacing-posture.md
│       │   │   │   ├── audience-and-targeting-map.md
│       │   │   │   ├── creative-testing-posture.md
│       │   │   │   ├── performance-history.md
│       │   │   │   └── platforms/
│       │   │   │       ├── meta-ads.md
│       │   │   │       ├── tiktok-ads-and-shop.md
│       │   │   │       └── programmatic.md
│       │   │   ├── internal/
│       │   │   ├── external/
│       │   │   └── landscape/
│       │   │
│       │   ├── organic-social/
│       │   │   ├── profile.md
│       │   │   ├── notes-from-org.md               ← team-aware brand memory
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── content-pillars-and-cadence.md
│       │   │   │   ├── creator-and-ugc-pipeline.md
│       │   │   │   ├── community-management-posture.md
│       │   │   │   ├── format-library.md
│       │   │   │   ├── organic-history.md
│       │   │   │   └── platforms/                  ← deep platform audits
│       │   │   │       ├── tiktok.md
│       │   │   │       ├── instagram.md
│       │   │   │       ├── youtube.md
│       │   │   │       ├── threads.md
│       │   │   │       ├── x.md
│       │   │   │       └── linkedin.md
│       │   │   ├── internal/
│       │   │   ├── external/
│       │   │   └── landscape/
│       │   │
│       │   ├── search/                             ← paid + SEO
│       │   │   ├── profile.md
│       │   │   ├── notes-from-org.md               ← team-aware brand memory
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── keyword-universe.md
│       │   │   │   ├── query-intent-map.md
│       │   │   │   ├── serp-audit.md
│       │   │   │   ├── content-cluster-map.md
│       │   │   │   ├── technical-seo-state.md
│       │   │   │   ├── google-ads-account.md
│       │   │   │   └── search-competitive-posture.md
│       │   │   ├── internal/
│       │   │   ├── external/
│       │   │   └── landscape/
│       │   │
│       │   ├── influencer/
│       │   │   ├── profile.md
│       │   │   ├── notes-from-org.md               ← team-aware brand memory
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── partner-roster-and-history.md
│       │   │   │   ├── brand-fit-rubric.md
│       │   │   │   ├── partner-tier-system.md
│       │   │   │   ├── partnership-performance-archive.md
│       │   │   │   ├── brief-library.md
│       │   │   │   └── contracts-and-rights.md
│       │   │   ├── internal/
│       │   │   ├── external/
│       │   │   └── landscape/
│       │   │
│       │   ├── brand-pr-comms/
│       │   │   ├── profile.md
│       │   │   ├── notes-from-org.md               ← team-aware brand memory
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── press-kit.md
│       │   │   │   ├── exec-voice-and-bios.md
│       │   │   │   ├── narrative-arcs-and-tentpoles.md
│       │   │   │   ├── coverage-history.md
│       │   │   │   ├── media-relationships.md
│       │   │   │   ├── crisis-playbook.md
│       │   │   │   └── brand-campaigns-history.md
│       │   │   ├── internal/
│       │   │   ├── external/
│       │   │   └── landscape/
│       │   │
│       │   ├── partnerships/                       ← affiliate + retail + co-marketing
│       │   │   ├── profile.md
│       │   │   ├── notes-from-org.md               ← team-aware brand memory
│       │   │   ├── sub-context-docs/
│       │   │   │   ├── affiliate-roster-and-terms.md
│       │   │   │   ├── retail-relationships.md
│       │   │   │   ├── co-marketing-history.md
│       │   │   │   ├── partnership-performance-archive.md
│       │   │   │   └── distribution-map.md
│       │   │   ├── internal/
│       │   │   ├── external/
│       │   │   └── landscape/
│       │   │
│       │   └── retention/                          ← email + SMS, outcome-framed
│       │       ├── profile.md
│       │       ├── notes-from-org.md               ← team-aware brand memory
│       │       ├── sub-context-docs/
│       │       │   ├── post-purchase-personas.md
│       │       │   ├── segmentation-map.md
│       │       │   ├── journey-inventory.md
│       │       │   ├── esp-and-sms-platform-state.md
│       │       │   ├── list-health-and-deliverability.md
│       │       │   ├── repeat-and-churn-cohorts.md
│       │       │   ├── win-back-history.md
│       │       │   └── nps-and-csat-state.md
│       │       ├── internal/
│       │       ├── external/
│       │       └── landscape/
│       │
│       │   Each team folder above also gets the team-scoped pipeline:
│       │       open-loops/promoted/[YYYY-MM]/, open-loops/archived/[YYYY-MM]/,
│       │       hypotheses/{tested,denied,awaiting-user}/[YYYY-MM]/,
│       │       validations/{validated,invalidated,insufficient-evidence,inconclusive}/[YYYY-MM]/,
│       │       re-validations/{scheduled, results/[YYYY-MM]/}
│       │
│       ├── open-loops/                             ← ORG-WIDE (cross-team or brand-strategic)
│       │   ├── promoted/[YYYY-MM]/
│       │   └── archived/[YYYY-MM]/
│       │
│       ├── hypotheses/                             ← ORG-WIDE
│       │   ├── tested/[YYYY-MM]/
│       │   ├── denied/[YYYY-MM]/
│       │   └── awaiting-user/[YYYY-MM]/
│       │
│       ├── validations/                            ← ORG-WIDE
│       │   ├── validated/[YYYY-MM]/
│       │   ├── invalidated/[YYYY-MM]/
│       │   ├── insufficient-evidence/[YYYY-MM]/
│       │   └── inconclusive/[YYYY-MM]/
│       │
│       └── re-validations/                         ← ORG-WIDE
│           ├── scheduled/
│           └── results/[YYYY-MM]/
│
├── .claude/skills/                                 ← Global skills. ACTUAL location: flat under .claude/skills/ (the only dir Claude Code loads skills from). The team-namespaced tree below is the [planned] target shape, not the current layout.
│   ├── creative-strategy/
│   │   ├── scriptwriting/
│   │   ├── hooks/
│   │   ├── headlines/
│   │   ├── brief/
│   │   └── analyze-ads/
│   ├── performance/
│   │   ├── scaling-plan/
│   │   ├── test-design/
│   │   ├── budget-shift-memo/
│   │   ├── weekly-pacing-read/
│   │   └── creative-fatigue-read/
│   ├── organic-social/
│   │   ├── post-draft/
│   │   ├── content-calendar/
│   │   ├── trend-fit/
│   │   ├── community-reply/
│   │   └── monthly-organic-audit/
│   ├── search/
│   │   ├── keyword-shortlist/
│   │   ├── serp-brief/
│   │   ├── meta-title-and-description/
│   │   ├── pmax-asset-draft/
│   │   ├── search-ad-copy/
│   │   ├── seo-content-brief/
│   │   └── internal-linking-plan/
│   ├── influencer/
│   │   ├── partner-shortlist/
│   │   ├── partner-brief/
│   │   ├── partner-outreach/
│   │   └── partner-post-mortem/
│   ├── brand-pr-comms/
│   │   ├── press-release/
│   │   ├── byline-draft/
│   │   ├── statement/
│   │   ├── exec-talking-points/
│   │   ├── media-pitch/
│   │   └── award-submission/
│   ├── partnerships/
│   │   ├── co-marketing-brief/
│   │   ├── retail-program-one-pager/
│   │   ├── affiliate-recruitment/
│   │   └── pdp-refresh/
│   └── retention/
│       ├── campaign-brief/
│       ├── email-draft/
│       ├── sms-draft/
│       ├── subject-line/
│       ├── segment-shortlist/
│       ├── journey-audit/
│       └── win-back-design/
│
│   (each skill folder: SKILL.md, strategy.md, processes/INDEX.md + [process].md,
│    references/knowledge/[name].md — same anatomy as v1)
│
├── .claude/agents/                                 ← Subagent definitions Claude Code loads on clone (not skills — independent reviewer contexts the skills spawn)
│   ├── context-grounding-review.md                 ← The grounding gate, runs FIRST: verifies the output was built from the right method docs, brand vault docs, and tool pulls — runs scripts/grounding-check.py (verbatims trace, cited sources exist), derives the right context independently from the routing catalog, diffs against the output's vocabulary evidence. Bounced = re-pull and regenerate.
│   └── creative-voice-review.md                    ← The voice gate, runs SECOND: runs scripts/voice-lint.py, judges per creative-strategy-context/ai-writing-tells.md, returns per-line verdicts. Both spawned by the creative skills' ship gates; ship to brand brains with their checkers and doctrine as one bundle.
│
├── .claude/settings.json                           ← Committed factory config: "outputStyle": "Parker" activates the voice layer for every session in this repo
├── .claude/output-styles/                          ← The chat-voice layer (not an agent, not a skill)
│   └── parker.md                                   ← Parker's voice as a Claude Code output style, injected into the system prompt itself (keep-coding-instructions: true keeps the engineering discipline). Hand-mirrored from prompts/_parker-voice-block.md — voice edits land in the block first. Ships to every brand brain via the onboarding runner and the propagate script.
│
├── references/                                     ← Global knowledge, namespaced by team
│   └── knowledge/
│       │
│       ├── global/                                 ← Cross-team marketing literacy
│       │   ├── how-to-use-parker.md
│       │   ├── stages-of-awareness.md              ← creative-strategy origin, applies cross-team
│       │   ├── emotions-and-desires.md             ← creative-strategy origin, applies cross-team
│       │   ├── ad-formats.md                       ← creative-strategy origin, applies cross-team
│       │   ├── positioning-frameworks.md
│       │   ├── the-buyer-journey.md
│       │   ├── brand-vs-performance-tension.md
│       │   ├── creative-data-loop.md
│       │   ├── attribution-fundamentals.md
│       │   ├── statistical-significance-for-marketers.md
│       │   ├── customer-research-methods.md
│       │   ├── segmentation-fundamentals.md
│       │   ├── youtube-notes/[video-id].md
│       │   └── podcast-notes/[episode-id].md
│       │
│       ├── creative-strategy/
│       │   ├── scriptwriting-principles.md
│       │   ├── yapper-ads.md
│       │   ├── andromeda.md
│       │   ├── how-to-make-killer-ads.md
│       │   ├── hook-frameworks.md
│       │   ├── ad-archetypes.md
│       │   ├── script-structures.md
│       │   ├── visual-grammar.md
│       │   ├── creative-diversity-frameworks.md
│       │   ├── creative-testing-frameworks.md
│       │   ├── how-to-read-an-ad.md
│       │   ├── brand-voice-translation.md
│       │   ├── the-one-thing-principle.md
│       │   ├── the-feeling-test.md
│       │   └── the-creative-brief-skeleton.md
│       │
│       ├── performance/
│       │   ├── ad-buying-principles.md
│       │   ├── account-structure-principles.md
│       │   ├── scaling-frameworks.md
│       │   ├── creative-volume-and-fatigue.md
│       │   ├── testing-frameworks.md
│       │   ├── incrementality-and-lift.md
│       │   ├── attribution-and-privacy.md
│       │   ├── platform-mechanics-meta.md
│       │   ├── platform-mechanics-tiktok.md
│       │   ├── platform-mechanics-google.md
│       │   ├── platform-mechanics-programmatic.md
│       │   ├── pacing-and-budget-rhythms.md
│       │   ├── reading-mer-and-blended.md
│       │   ├── diagnosing-a-bad-week.md
│       │   ├── creative-as-targeting.md
│       │   └── conversion-rate-math.md
│       │
│       ├── organic-social/
│       │   ├── platform-native-conventions.md
│       │   ├── algorithm-realities.md
│       │   ├── ugc-direction.md
│       │   ├── content-pillar-frameworks.md
│       │   ├── formats-by-platform.md
│       │   ├── organic-hook-and-payoff.md
│       │   ├── engagement-vs-reach-economics.md
│       │   ├── community-building-frameworks.md
│       │   ├── post-cadence-rules.md
│       │   ├── trend-hijacking-vs-trend-driven.md
│       │   ├── the-anatomy-of-a-viral-post.md
│       │   ├── how-to-read-comments.md
│       │   ├── meme-language-and-decay.md
│       │   └── distribution-flywheels.md
│       │
│       ├── search/
│       │   ├── seo-principles.md
│       │   ├── google-ranking-factors.md
│       │   ├── search-intent-taxonomy.md
│       │   ├── keyword-research-frameworks.md
│       │   ├── query-clustering.md
│       │   ├── content-cluster-strategy.md
│       │   ├── on-page-fundamentals.md
│       │   ├── technical-seo-checklist.md
│       │   ├── link-building-frameworks.md
│       │   ├── e-e-a-t-and-authority.md
│       │   ├── ai-overviews-and-llm-search.md
│       │   ├── google-ads-account-structure.md
│       │   ├── pmax-mechanics.md
│       │   ├── brand-vs-non-brand-bidding.md
│       │   ├── landing-page-message-match.md
│       │   └── shopping-feed-optimization.md
│       │
│       ├── influencer/
│       │   ├── influencer-marketing-principles.md
│       │   ├── ftc-compliance.md
│       │   ├── creator-economy-state.md
│       │   ├── partner-tier-economics.md
│       │   ├── compensation-models.md
│       │   ├── whitelisting-and-allowlisting.md
│       │   ├── usage-rights-and-contracts.md
│       │   ├── partner-brief-anatomy.md
│       │   ├── partner-fit-scoring.md
│       │   ├── ugc-vs-influencer.md
│       │   ├── ambassador-program-design.md
│       │   └── post-campaign-debrief-frameworks.md
│       │
│       ├── brand-pr-comms/
│       │   ├── pr-principles.md
│       │   ├── crisis-comms-playbook.md
│       │   ├── earned-media-strategy.md
│       │   ├── narrative-architecture.md
│       │   ├── exec-voice-development.md
│       │   ├── thought-leadership-frameworks.md
│       │   ├── founder-led-narrative.md
│       │   ├── press-release-anatomy.md
│       │   ├── byline-anatomy.md
│       │   ├── pitch-anatomy.md
│       │   ├── media-relationship-fundamentals.md
│       │   ├── embargoes-and-exclusives.md
│       │   ├── tier-1-vs-tier-2.md
│       │   ├── moments-vs-always-on.md
│       │   └── award-submission-frameworks.md
│       │
│       ├── partnerships/
│       │   ├── affiliate-marketing-principles.md
│       │   ├── retail-media-and-shopper.md
│       │   ├── co-marketing-frameworks.md
│       │   ├── affiliate-program-design.md
│       │   ├── commission-structure-principles.md
│       │   ├── partner-recruitment-frameworks.md
│       │   ├── amazon-listing-optimization.md
│       │   ├── retail-program-mechanics.md
│       │   ├── pdp-anatomy.md
│       │   ├── in-store-vs-digital-shelf.md
│       │   ├── retail-media-networks.md
│       │   ├── co-marketing-deal-structure.md
│       │   └── distribution-pyramid.md
│       │
│       └── retention/
│           ├── retention-marketing-principles.md
│           ├── deliverability.md
│           ├── email-design-principles.md
│           ├── sms-conventions-and-compliance.md
│           ├── ltv-frameworks.md
│           ├── segmentation-frameworks.md
│           ├── journey-mapping-frameworks.md
│           ├── flow-anatomy.md
│           ├── subject-line-frameworks.md
│           ├── preview-text-and-from-name.md
│           ├── list-hygiene-and-sunsetting.md
│           ├── subscriber-lifecycle.md
│           ├── repeat-rate-and-cohort-math.md
│           ├── esp-and-sms-platform-mechanics.md
│           ├── rfm-and-predictive-analytics.md
│           ├── nps-and-csat-frameworks.md
│           ├── review-collection-mechanics.md
│           ├── referral-program-design.md
│           └── a-b-test-frameworks-for-retention.md
│
├── tools/                                          ← Tool inventory + schemas
│   ├── INDEX.md
│   └── [tool-name].md
│
├── self-improvement/                               ← File-backed v1 learning loop + global product dreaming
│   ├── README.md
│   ├── the-living-loop.md                          ← spine + executing arm: dreaming (plan) → human review → self-improvement (execute) across the five streams
│   ├── dreaming-system.md                          ← planning arm: reads the day's comms, proposes the five buckets
│   ├── self-improvement-system.md                  ← reasoning-trace substrate: the why behind each change (the executing arm itself is the-living-loop.md)
│   ├── applied-changes.md
│   ├── review-queue.md
│   ├── patterns/
│   │   └── INDEX.md
│   ├── product-signals/                            ← Global product dreaming, anonymized + cross-brand
│   │   ├── struggles/[YYYY-MM]/[id].md             ← anonymized friction/bug patterns from conversations
│   │   ├── value/[YYYY-MM]/[id].md                 ← anonymized delight/value use cases
│   │   └── use-case-library.md                     ← running anonymized library for cross-pollination
│   └── reasoning-traces/
│       └── [YYYY-MM]/[YYYY-MM-DD]-[trace-slug].md
│
├── global/                                         ← Cross-brand dreaming pool, namespaced by team
│   └── teams/
│       ├── creative-strategy/
│       │   ├── ads/
│       │   │   ├── ai-tagged-ads/
│       │   │   ├── parker-favorites/
│       │   │   └── internal-favorites/
│       │   ├── organic-tiktok/[YYYY-MM-DD]/[video-id].md
│       │   ├── expert-insights/
│       │   │   ├── INDEX.md
│       │   │   ├── inbox/
│       │   │   ├── curation/
│       │   │   └── [source-id]/{source.md, [YYYY-WW]/[content-id].md}
│       │   └── parker-taste/
│       │       ├── parker-ideas.md
│       │       ├── idea-bank/{INDEX.md, [item-id].md}
│       │       └── patterns-to-monitor/{INDEX.md, [pattern-id].md}
│       │
│       ├── performance/
│       │   ├── signals/
│       │   │   ├── platform-updates/[YYYY-WW]/[id].md     ← Meta/TikTok/Google releases
│       │   │   ├── attribution-shifts/[YYYY-WW]/[id].md
│       │   │   └── benchmarks/[YYYY-WW]/[id].md
│       │   ├── expert-insights/[source-id]/{source.md, [YYYY-WW]/[content-id].md}
│       │   └── parker-taste/
│       │       ├── parker-ideas.md                        ← POV on what's working in paid right now
│       │       ├── idea-bank/                            ← scaling case studies, account structures
│       │       └── patterns-to-monitor/
│       │
│       ├── organic-social/
│       │   ├── signals/
│       │   │   ├── trending-content/[YYYY-WW]/[id].md
│       │   │   ├── format-breakouts/[YYYY-WW]/[id].md
│       │   │   └── algorithm-shifts/[YYYY-WW]/[id].md
│       │   ├── expert-insights/[source-id]/...
│       │   └── parker-taste/
│       │       ├── parker-ideas.md
│       │       ├── idea-bank/
│       │       └── patterns-to-monitor/
│       │
│       ├── search/
│       │   ├── signals/
│       │   │   ├── serp-shifts/[YYYY-WW]/[id].md          ← AI Overviews developments
│       │   │   ├── google-announcements/[YYYY-WW]/[id].md
│       │   │   └── ranking-factor-research/[YYYY-WW]/[id].md
│       │   ├── expert-insights/[source-id]/...
│       │   └── parker-taste/
│       │       ├── parker-ideas.md
│       │       ├── idea-bank/
│       │       └── patterns-to-monitor/
│       │
│       ├── influencer/
│       │   ├── signals/
│       │   │   ├── creator-moves/[YYYY-WW]/[id].md        ← deals, exits, drama
│       │   │   ├── regulatory-updates/[YYYY-WW]/[id].md   ← FTC, platform rules
│       │   │   └── breakout-creators/[YYYY-WW]/[id].md
│       │   ├── expert-insights/[source-id]/...
│       │   └── parker-taste/
│       │       ├── parker-ideas.md
│       │       ├── idea-bank/
│       │       └── patterns-to-monitor/
│       │
│       ├── brand-pr-comms/
│       │   ├── signals/
│       │   │   ├── pr-case-studies/[YYYY-WW]/[id].md
│       │   │   ├── crisis-examples/[YYYY-WW]/[id].md
│       │   │   └── narrative-trends/[YYYY-WW]/[id].md
│       │   ├── expert-insights/[source-id]/...
│       │   └── parker-taste/
│       │       ├── parker-ideas.md
│       │       ├── idea-bank/
│       │       └── patterns-to-monitor/
│       │
│       ├── partnerships/
│       │   ├── signals/
│       │   │   ├── retail-shifts/[YYYY-WW]/[id].md
│       │   │   ├── affiliate-program-moves/[YYYY-WW]/[id].md
│       │   │   └── co-marketing-examples/[YYYY-WW]/[id].md
│       │   ├── expert-insights/[source-id]/...
│       │   └── parker-taste/
│       │       ├── parker-ideas.md
│       │       ├── idea-bank/
│       │       └── patterns-to-monitor/
│       │
│       └── retention/
│           ├── signals/
│           │   ├── esp-platform-updates/[YYYY-WW]/[id].md  ← Klaviyo, Attentive, Postscript
│           │   ├── deliverability-shifts/[YYYY-WW]/[id].md
│           │   └── lifecycle-case-studies/[YYYY-WW]/[id].md
│           ├── expert-insights/[source-id]/...
│           └── parker-taste/
│               ├── parker-ideas.md
│               ├── idea-bank/
│               └── patterns-to-monitor/
│
└── parker-system/                                  ← System-level Parker config
    ├── system-instructions.md
    ├── skill-anatomy-schema.md
    ├── file-conventions.md
    ├── attribution-schema.md
    └── dreaming/
        ├── INDEX.md
        ├── runs/
        │   └── [YYYY-WW]/                          ← Folder per week, per-team + brand-level files
        │       ├── creative-strategy.md
        │       ├── performance.md
        │       ├── organic-social.md
        │       ├── search.md
        │       ├── influencer.md
        │       ├── brand-pr-comms.md
        │       ├── partnerships.md
        │       ├── retention.md
        │       ├── personas.md                     ← brand-level persona dream observations
        │       └── voc.md                          ← brand-level VoC dream observations
        └── proposals/
            ├── pending/[YYYY-WW]/[id].md           ← target file is implicit from the path being modified
            ├── approved/[YYYY-WW]/[id].md
            └── rejected/[YYYY-WW]/[id].md
```

---

## What changed on 2026-08-07

**Webinar transcripts get a home.** Parker's monthly customer webinars now land in the product brain so users can ask what was announced, demoed, or answered on a given call — something no method doc carries.

- **NEW `global/knowledge/webinars/`** — `INDEX.md` (the catalog, newest first, one dense entry per session, plus the convention for adding the next one) and one file per webinar, named `YYYY-MM-DD-monthly-webinar.md`. Each file carries frontmatter, a **What this session covered** digest written to answer most questions without opening the transcript, and the verbatim transcript below it. Seeded with the 2026-08-06 session. Because product state moves fast between sessions, the index is newest-first and states the rule: where two sessions disagree about what exists, the newer one wins.
- **Scope discipline.** First-party Parker sessions only. Host and attendee names as spoken on the call; no private brand outputs, account data, or spend figures — where a demo showed real numbers on screen, the transcript says so without the numbers. Third-party expert transcripts keep routing through `expert-insights/` and get promoted as generalized method, not stored raw. `README.md`'s "raw transcripts" exclusion carries this carve-out explicitly.
- **Two standing read cautions**, stated in the index and on each file: product state described in a webinar is dated to that call, and figures the hosts say live are `stated`, not verified specs.
- **NEW: fine-tuned skills — a brain grows downward, not just sideways.** `system/growing-the-brain.md` gains a "Growing a skill, not just a surface" section: a brand-authored skill built from the team's own corpus (their scripts, iterations, briefs, or feedback history, wherever it lives), written as a delta on the factory skill rather than a fork, living in the brain's own `.claude/skills/` under a **distinct name** so `scripts/sync-executable-layer.py`'s bundle map never sees it and it survives every pin bump. This is the missing third rung of the adaptation ladder — brand docs first, fine-tuned sibling second, editing a copy in place only when neither works — and it beats editing a copy because the sibling keeps taking factory improvements through the skill it references. `templates/brand-brain-CLAUDE-template.md` carries the runtime half: the precedence rule (a fine-tuned skill is the default for its craft, the factory skill the method underneath it) in the execution-routing bullet, and a "## The map" line so the planning pass can see what exists. Ships with real-step `migrations/v15.md`, because the brain's root `CLAUDE.md` is brand-authored and outside the sync bundle.
- **NEW `hooks.md` #22 — Trigger-Event hooks.** The opener that lands the single concrete moment a problem became undeniable, almost always because another person registered it. Distinguished explicitly from #14 (Trigger *Word*, charged vocabulary) and #18 (Storytelling, which opens a journey and pays off with an arc). `customer-review-mining-method.md` gains the matching qualifying signal so the mining pass actually hunts the moment rather than the condition, with the pattern-vs-single-instance and personal-attribute governors named. The hardcoded hook-format list in `analyzing-public-ad-accounts.md` was updated to match — it had also silently drifted past #21 (Permission / Zone 1).
- **Watch entry 8 added, entry 6 partially promoted** in `creative-strategy-context/parker-taste/patterns-to-monitor/INDEX.md`. New: trigger-event animation (AI-animated, often sung, opening on the moment rather than the problem) — logged as a watch item rather than canon because it is single-source, the evidence offered was impression rank rather than performance, and animation / trigger-open / song are confounded in every example. Entry 6 (purchase-trigger capture) was partially promoted: its research half is corroborated and now lives in the review-mining method, while the checkout-survey capture stays on the list, with the problem trigger and the purchase trigger explicitly separated so they don't get collapsed. `ai-animation-prompting.md` stays a placeholder with the candidate content and the missing pieces named — the source described what the format does, not how to prompt it, and inferring prompting method from finished ads is the fabrication the attribution rules exist to prevent.
- **Impression rank scoped, per a maintainer correction.** `analyzing-public-ad-accounts.md` now states it unconditionally at the top: impression rank is a substitute for data you don't have, never a supplement to data you do. It is the right proxy for competitors, inspo, and affinity brands whose accounts are unreachable, and the wrong one the moment Parker has account access, where `ad-account-analysis.md`'s real spend and performance data always wins. Repeated at point of use in the step-five lens list, and carried into `global/knowledge/best-use-cases.md` and the webinar transcript's digest.
- **`global/knowledge/best-use-cases.md` extended** from the 2026-08-06 session — swipe files and briefs off the discovery database, Reddit, affinity-brand follow-through, cross-client agency analysis, fine-tuning a skill on your own back catalog with the CLAUDE.md override, feeding the brain outside content, the hypothesis-tracker routine, and a habits section (yap, plan mode, nothing is permanent). Durable use cases get promoted here; the transcript stays as the receipt.
- **`2026-07-02-monthly-webinar.md` backfilled** into the same folder — the session where the Parker brain was first walked through end to end for customers. It is *older* than the seed entry, so it carries a supersession note at the top plus a table of what had moved by 6 August (Discovery, Discover Brands, Northbeam, post-purchase surveys, Reddit, and the closed gap where Claude Code couldn't see Parker web-app chats — `search_chat_history` exists now). Its digest states plainly that almost everything in the session was already canon, and its "What this session contributed" section lists only the five things that genuinely weren't.
- **Connect your own tools *before* the build.** The build sequence gated on the Parker MCP and pushed the team's own tools (Notion, Slack, Drive) to `/get-started` after the build finished. The build is the heaviest read Parker ever runs on a brand, so a tool live at that moment gets read *into* the foundation while one connected after has to be reconciled against a finished V0. `prompts/onboarding-runner.md` gains a short pre-Phase-0 step (ask what the team works in, wire it up, log what they name but don't connect — explicitly **not** a gate, since the Parker MCP remains the only connection the build needs), `.claude/skills/set-up-brain/SKILL.md` gains the matching step 1b, and `system/parker-tools.md` carries the standing rule. The intake's closing gap question also gains a yardstick for how much to say — everything you'd tell an agency you just hired, or a new strategist joining the account.
- **`system/parker-tools.md` inventory corrected — three tools, including the Reddit gap.** Two were missing outright: `search_swipe_file` (the org's saved inspiration — **org-scoped, not brand-scoped**, written to by the Chrome extension and every save button, with AI analysis on many saved Facebook ads) and `brand_discovery` (ranks external brands against the client on audience persona, positioning and tone, returns a competitor/inspo/affinity lens per match, and is what populates the affinity set). Both surfaced by the 2026-07-02 session's headline demos; verified present in the live toolset on 2026-08-07. The third is a **correction, not an addition**: the "flag this for eng" section stated Parker had *no native reach into Reddit or any forum*, which was true when written and stopped being true when Reddit shipped (in limited testing on 6 August, live now). `search_reddit_posts_and_comments` joins the table — the brand's own indexed posts and comments as flat peers from curated subreddits scraped on a schedule, gated on that brand completing Reddit onboarding, with the semantic leg taking 4–10 short keyword phrases rather than a sentence. The section keeps its real constraint (still no open-web search; forums other than Reddit still unreachable) but now says to check Reddit before calling a community question `data-limited`. The stale claim lived in exactly one place.
- **`best-use-cases.md` extended again** from the 2026-07-02 session with the durable use cases it added: connecting tools before the build (in the "pour your real context in" section), auditing your own working week to find what to automate, a review-agent pass over generated output — the post-generation counterpart to the pre-generation judges — and routines being set up by saying so in the chat rather than in a settings screen. **A coverage audit against both transcripts in the same pass** caught two more from the 2026-08-06 session that the first promotion missed: extending the brain past paid creative into the other channels a team runs (the method was in `system/growing-the-brain.md`, but nothing told a *user* it was possible), and browsing the discovery database with the format filter off — the "what should we make?" direction, read as a diff against the brand's own library. The 2026-08-06 file's promotion list records them as items 10 and 11. Deliberately not promoted from that session: the Fable 5 build recommendation (point-in-time model call, not repeated), the Higgsfield local-assets limitation (contested live and never tested), and the roadmap items. No watch entry was opened — the session made no craft-method claim that isn't already canon.

---

## What changed on 2026-06-18

**Performance (media-buying) knowledge tree comes online — the second team after creative-strategy.** Media buyers are a real and growing share of Parker's users, and the architecture already reserved the `performance` team for them (knowledge docs named under `references/knowledge/performance/`; per-team expert-insights pipeline). On disk, the active v1 convention places a team's knowledge + expert-insights + parker-taste together under `global/knowledge/[team]/` (this is where creative-strategy actually lives), so the performance tree was instantiated at `global/knowledge/performance/`.

- **NEW `global/knowledge/performance/expert-insights/`** — mirrors the creative-strategy intake system one-for-one: `INDEX.md`, `inbox/`, `context-update-candidates/`, `curation/`. Carries one extra discipline: media-buying numeric claims (CPA lift, wasted-spend %, "leaked deck" stats) stay `stated` until grounded in the brand's account data or a second source. The durable method (often externally grounded) is separated from a source's self-interested numbers.
- **NEW `global/knowledge/performance/incrementality-and-lift.md`** — the first canonical performance knowledge doc, seeded `[~]` from the 2026-06-18 Meta Performance Summit signal. Covers incrementality vs attributed credit, conversion-lift / holdout design, the three-layer measurement stack, lift→MTA/MMM calibration, and the measurement rhythm. Method written as canon; source percentages held as directional only.
- The remaining named performance docs (`attribution-and-privacy`, `account-structure-principles`, `platform-mechanics-meta`, `pacing-and-budget-rhythms`, `ad-buying-principles`, `scaling-frameworks`, `creative-volume-and-fatigue`, `testing-frameworks`, `reading-mer-and-blended`, `diagnosing-a-bad-week`, `creative-as-targeting`, `conversion-rate-math`) remain `[planned]` — routed as candidates, written as corroboration arrives.
- `parker-taste/` for performance is not yet built; performance signals route to knowledge docs for now.

---

## What changed on 2026-05-28

The big move: **teams expansion.** Parker now serves 8 marketing teams under one shared foundation.

### Brand-id level
- **NEW `teams/` wrapper** at brand-id level holds the 8 teams. The existing `creative-strategy/` folder moved inside `teams/` and gained `profile.md` + `sub-context-docs/` to match the universal team shape.
- Every team has the same internal shape: `profile.md` + `sub-context-docs/` + `internal/` + `external/` + `landscape/`. `landscape/` replaces `market/` (better word) and applies to every team, not just creative-strategy.

### Foundation `sub-context-docs/`
- **4 new docs added:** `marketing-org-and-budget`, `channel-mix-and-attribution`, `marketing-calendar-and-campaigns`, `brand-guidelines-and-claims`.
- **1 rescope:** `organic-channels-audit` → `organic-channels-inventory` (inventory only — deep audit now lives under `teams/organic-social/`). `performance-targets-and-metrics` stays as the creative-strategy performance scoreboard.
- **`ad-account-evaluation` relocated** from foundation to `teams/performance/sub-context-docs/` (canonical home; creative-strategy reads from it).

### Personas
- **`voice-of-customer/` now nests under `personas/`** (was a sibling). Same source material feeds both, so the nesting reinforces the relationship. VoC's structure (one-pager + phrases/) unchanged.

### Skills
- **Skills namespaced by team:** `skills/[team]/[skill-name]/`. With 47 skills across 8 teams, namespacing is the difference between findable and a swamp. Skill anatomy (SKILL.md + strategy.md + processes + references) unchanged.

### Knowledge
- **`references/knowledge/` namespaced by team** + a new `global/` tier for cross-team marketing literacy.
- **Promoted to global tier** (from creative-strategy origin): `stages-of-awareness`, `emotions-and-desires`, `ad-formats`. These apply across every team — retention uses awareness stages for segments, performance uses ad-formats for paid social, etc.
- ~105 knowledge docs total across 8 teams + global tier. Authored by domain experts (one per team — being identified).

### Dreaming
- **`global/` restructured to `global/teams/[team]/`.** Each team has its own signal pool + expert-insights pipeline + parker-taste (parker-ideas + idea-bank + patterns-to-monitor). Creative-strategy keeps its `ads/` + `organic-tiktok/` pools; other teams use `signals/` with team-specific buckets (performance: `platform-updates/`, `attribution-shifts/`, `benchmarks/`; search: `serp-shifts/`, `google-announcements/`; etc.).
- **Per-brand expert syntheses moved** from `z-brands/[brand]/creative-strategy/external/expert-takes-on-category/` to per-team: `z-brands/[brand]/teams/[team]/landscape/expert-takes-on-category/`. Each team produces its own monthly synthesis filtered for the brand's category.
- **`parker-system/dreaming/runs/` becomes a folder per week** with per-team files (8) + brand-level files (personas.md, voc.md).
- **No cross-team structure.** Parker has access to all signals and can reason across teams when authoring proposals — explicit cross-team pool/proposal type adds nothing.

### Memory
- **Memory now team-aware.** Each team gets its own `notes-from-org.md` (per-brand, per-team) and per-user `notes-from-user.md` (per-user, per-brand, per-team). Brand-level memory (`running-notes/brand-notes-from-org.md`, `user-profile.md`, `brand-notes-from-user.md`) preserved for cross-team truths.
- **Brand idea banks are brand-level memory.** `z-brands/[brand]/idea-bank/` is the canonical home for brand-specific ideas from context docs, research, user conversations, ideas-tab saves, and routed expert signals. Team taste files can reference these ideas, but the brand folder owns the brand-specific entry.
- **Loading sequence updated:** when planner picks a team, three additional always-loaded files come in — `teams/[team]/profile.md`, `teams/[team]/notes-from-org.md`, `users/[user]/[brand]/teams/[team]/notes-from-user.md`.
- **Extraction routing:** the extraction prompt decides whether an observation is team-scoped (routes to `teams/[team]/notes-from-org.md` or per-team user notes) or cross-team (routes to brand-level). Default to team memory; promote up if the pattern recurs across teams (dreaming proposes the promotion).

### Open loops / hypotheses / validations
- **Two buckets, same pipeline shape.** Org-wide (brand-level) bucket for cross-team or brand-strategic items; per-team buckets for domain-scoped items inside each team folder.
- Each item carries a team-tag in frontmatter even when in the team folder — supports queries and supports promotion when a team-scoped loop turns out to affect another team.
- Promotion direction matches memory: default team-scoped; dreaming proposes promotion to org-wide when a loop/hypothesis recurs across teams or affects brand strategy.

---

## What changed on 2026-05-21

- **`ad-account-evaluation` and `reviews-and-customer-language` no longer brand sub-context prompts** — they're produced by their own dedicated context docs and other docs reference their output. ad-account-evaluation now lives under `teams/performance/`; reviews-and-customer-language content lives under `personas/sources/customer-reviews.md`.
- **`public-perception` renamed to `reputation-analysis`** (and pivoted to the reputation method).
- **`public-perception`, `community-and-forums`, and `customer-journey-and-persona-discovery` are brand sub-context docs** (previously listed only under competitor).

---

## What changed on 2026-05-18

- **`z-brands/[brand-id]/personas/` is a first-class folder.** Holds the personas one-pager + voice-of-customer + 6 source docs that feed both. Reputation context lives in `sub-context-docs/reputation-analysis.md` and informs messaging constraints, not core persona proof.

---

## Notable architectural decisions

- **Foundation = every team reads it.** `sub-context-docs/`, `personas/`, `competitors/`, `running-notes/`, `working-thesis-synthesis.md` all sit at brand-id level above `teams/`.
- **Teams are siblings with the same shape.** `profile.md` + `sub-context-docs/` + `internal/` + `external/` + `landscape/`. The planner picks which team's context is in play.
- **Skills are global, not per-brand.** Per-brand customization happens via strategy.md + memory. Skills are namespaced by team in the folder, not per-brand.
- **Two reference tiers.** Skill-local references live under each skill. Cross-skill knowledge lives at top-level `references/knowledge/` namespaced by team, with a `global/` tier for cross-team marketing literacy.
- **Competitor audits live under their brand.** They are per-brand context, not global.
- **Each team's `internal/external/landscape/` mirrors creative-strategy's pattern.** Internal = this brand. External = competitors. Landscape = market/category. Not all populated on v1; structure stays ready.
- **Open-loops, hypotheses, validations live in two buckets.** Org-wide bucket at `z-brands/[brand]/{open-loops,hypotheses,validations,re-validations}/` for cross-team or brand-strategic items. Per-team buckets inside each team folder for domain-scoped items. Each item also carries a team-tag in frontmatter. Promotion from team to org-wide is dreaming-proposed when patterns recur.
- **The old-ads corpus lives in the knowledge tier.** In the active creative-strategy v1, the historical print-ad swipe library lives at `creative-strategy-context/old-ads/` (README + INDEX + `entries/`, organized by industry and by mechanic), resolving in brand brains at `parker-system/creative-strategy-context/old-ads/` through the pinned mount (the propagate script's deliberate-add covers legacy copy-based brains). The weekly idea hunt's historian lens retrieves from it; entries are describe-and-link, public-domain and openly archived material only.
- **Expert signals are team-scoped first.** In the active creative-strategy v1, user-provided expert content lives at `creative-strategy-context/expert-insights/`, and cross-brand taste lives at `creative-strategy-context/parker-taste/`. The post-launch team architecture moves the same pattern to `global/teams/[team]/expert-insights/` and `global/teams/[team]/parker-taste/`. Brand-specific creative ideas route from expert signals into the brand idea bank. Every saved expert signal also names context targets and propagation status. Proposed updates to prompts, skills, context docs, taste files, and brand memory route through the relevant `context-update-candidates/` folder before promotion.
- **Self-improvement is file-backed in v1.** `self-improvement/` stores reasoning traces from user corrections, approvals, rejections, reroutes, strategic decisions, hypothesis edits, and product rules. `self-improvement/self-improvement-system.md` is the canonical method. Traces can create candidates immediately, but promotion into prompts, skills, or system docs requires explicit approval, repeated evidence, or strong corroboration.
- **Re-validations separate from validations.** Validations do not live forever.
- **Chat history per user, not per brand.** Brand-level current-work.md is synthesized across all users.
- **System instructions and routing logic are one file.** Parker's identity is the planner. Routing logic is the system prompt. Memory-loading is backend code, not a Parker file.

---

## The dreaming loop

Parker has an offline learning cycle that runs weekly. Updated 2026-05-28 — dreaming now fans out across all 8 teams.

### Three layers

1. **Per-team signal pools at `global/teams/[team]/`** — each team has its own scrape pool (`signals/` or team-specific subfolders), expert pipeline (`expert-insights/[source-id]/`), and evolving Parker taste (`parker-taste/parker-ideas.md` + `idea-bank/` + `patterns-to-monitor/`). Creative-strategy keeps its `ads/` + `organic-tiktok/` pools. Other teams use the `signals/` umbrella with team-specific buckets (e.g., performance has `platform-updates/`, `attribution-shifts/`, `benchmarks/`; search has `serp-shifts/`, `google-announcements/`).
2. **Per-brand expert synthesis** at `z-brands/[brand]/teams/[team]/landscape/expert-takes-on-category/[YYYY-MM]-synthesis.md` — each team produces its own monthly synthesis filtered for the brand's category. Creative-strategy gets ad-strategist takes; performance gets media-buyer takes; search gets SEO/AI-Overview takes; etc.
3. **System-level dreaming at `parker-system/dreaming/`** — weekly run folder with per-team + brand-level files; proposals routed by the path they propose to modify.

### Weekly cycle

Scrape → categorize per team → Parker dreams per team → Parker proposes per team → Parker updates each team's taste → per-brand category syntheses run per team → humans review per team. Approved proposals get applied via full file replacement. Rejected proposals preserve reasoning so Parker learns what doesn't fly.

### Dreaming operations

**Brand-level (run across all brands weekly):**
- **VoC dream** — scan `personas/sources/` and propose additions, demotions, removals to `personas/voice-of-customer/voice-of-customer.md`
- **Persona dream** — scan `personas/sources/` and propose refinements to existing personas, new emerging persona candidates, retirement of unsupported personas

**Per-team (run for each of the 8 teams weekly):**
- **Team sub-context dream** — scan `teams/[team]/sub-context-docs/` against new signals → propose updates
- **Team knowledge dream** — scan `references/knowledge/[team]/` against new expert content → propose updates / new docs
- **Team skill dream** — scan `skills/[team]/` against generated work + new patterns → propose refinements / new skills
- **Per-brand category synthesis** — roll up `global/teams/[team]/expert-insights/` filtered for this brand's category into `z-brands/[brand]/teams/[team]/landscape/expert-takes-on-category/[YYYY-MM]-synthesis.md`
- **Team taste update** — update `global/teams/[team]/parker-taste/parker-ideas.md` + idea-bank + patterns-to-monitor

**Note on cross-team:** No dedicated cross-team pool or proposal type. Parker has access to all signals and can reason across teams when authoring a proposal — explicit cross-team structure adds nothing on top of that.
