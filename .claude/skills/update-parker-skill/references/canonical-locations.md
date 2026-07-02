# Canonical locations (v1 sketch)

Where each kind of content lives in the Parker system. The canonical location is the single source of truth for that content. Everything else either references it or derives from it.

## System rules and methodology

| Topic | Canonical | Inherits-from / derived |
|---|---|---|
| Open-loops rules, weighting, verdict template | `system/open-loops-system.md` | `_open-loops-core-block.md` (generation) + `open-loops-roll-up.md` (grading) |
| Senior-strategist open-loops reasoning | `global/knowledge/creative-strategy/creative-strategy-fundamentals.md` | Loaded via expertise-routing; the block + roll-up carry the operational rubric |
| Ad-account analysis methodology | `global/knowledge/creative-strategy/public-ad-library-analysis.md` | Prompts reference it |
| Customer-review mining methodology | `global/knowledge/creative-strategy/customer-review-mining-method.md` | Prompts reference it |
| Personas design | `templates/personas-design.md` + `templates/personas-template.md` | Prompts reference them |
| Voice of customer design | `templates/voc-design.md` + `templates/voc-template.md` | Prompts reference them |
| Attribution principle | `system/attribution-principle.md` | All persistent-claim docs reference |
| Self-improvement system | `self-improvement/self-improvement-system.md` | Reasoning trace capture, routing, curation, and promotion |
| Master file structure | `system/master-file-structure.md` | (Reference only) |
| Master prompt review rubric | `system/master-prompt-review.md` | (Reference only) |

## Prompts

| Category | Canonical | Notes |
|---|---|---|
| Brand profile sub-context-docs | `prompts/brand-profile/[name].md` | README indexes them |
| Brand-profile narrative synthesis | `prompts/brand-profile/brand-profile-narrative.md` | Pulls from all sub-context docs |
| Brand-profile foundations (authoring reference) | `prompts/brand-profile/_foundations.md` | NOT loaded at runtime; canonical wording each prompt embeds |
| Competitor profile sub-context-docs | `prompts/competitor-profile/[name].md` | One per slice per competitor |
| Personas sub-context-docs | `prompts/personas/[name].md` | One per source surface |
| Personas synthesis | `prompts/personas/personas-profile.md` | Pulls from all persona sources |
| Voice-of-customer extractors | `prompts/voice-of-customer/voc-[category].md` | 9 categories |
| Voice-of-customer assembly | `prompts/voice-of-customer/voice-of-customer-assembly.md` | Rolls up the 9 extractors |

## Database and memory specs

| Type | Canonical | Notes |
|---|---|---|
| Global AI-tagged ads DB | `prompts/global-databases/global-ai-tagged-ads-db.md` | Schema, capture prompt, curate prompt |
| Internal favorites DB | `prompts/global-databases/internal-favorites-db.md` | Schema, capture prompt, curate prompt |
| Parker favorites DB | `prompts/global-databases/parker-favorites-db.md` | Schema, capture prompt, curate prompt |
| Expert signal DB | `prompts/global-databases/expert-signal-db.md` | User-provided expert content, team-scoped market awareness, file-backed v1 staging |
| Brand idea bank | `prompts/ideas-and-briefs/brand-idea-bank.md` | Brand-specific idea memory maintained from docs, research, conversations, manual ideas-tab saves, and routed expert signals |

## Self-improvement

| Type | Canonical | Notes |
|---|---|---|
| Self-improvement method | `self-improvement/self-improvement-system.md` | Canonical method for reasoning traces |
| Reasoning traces | `self-improvement/reasoning-traces/[YYYY-MM]/` | Individual learning traces from corrections, approvals, rejections, reroutes, and strategic decisions |
| Review queue | `self-improvement/review-queue.md` | Traces awaiting approval, repetition, or evidence |
| Self-improvement patterns | `self-improvement/patterns/INDEX.md` | Repeated learning patterns Parker is watching |
| Applied changes | `self-improvement/applied-changes.md` | Promoted traces that changed canonical surfaces |

## Training corpus

| Type | Canonical | Notes |
|---|---|---|
| Open-loops training corpus (archived) | `parker-v2/archive/open-loops-training/` | The before/after exercise that built the open-loops system; its reasoning is distilled into `creative-strategy-context/creative-strategy-fundamentals.md` and the block + roll-up |
| Brand-audit reasoning library | `parker-v2/reasoning-layer-notes/NN-[topic]/transcript.md` + `reasoning.md` | One folder per audit session |

## Brand outputs

| Type | Canonical | Notes |
|---|---|---|
| Brand narrative one-pager | `z-brands/[brand]/brand-profile.md` | Synthesis output |
| Brand sub-context-docs | `z-brands/[brand]/sub-context-docs/[name].md` | One per slice |
| Personas one-pager | `z-brands/[brand]/personas/personas-profile.md` | Persona synthesis output |
| Voice-of-customer library | `z-brands/[brand]/voice-of-customer.md` | (May not exist yet for all brands) |
| Consolidated open-loops roll-up | `z-brands/[brand]/open-loops/[date]-consolidated-roll-up.md` | Rubric-applied versions supersede |
| Running notes | `z-brands/[brand]/running-notes/[date]-[topic].md` | Append-only |
| Source pulls | `z-brands/[brand]/source-pulls/[date]-[topic].md` | Raw research material |
| Brand idea bank | `z-brands/[brand]/idea-bank/` | Living idea bank; one entry per idea plus index |
| Competitor sub-context-docs | `z-brands/[brand]/competitors/[group]/[competitor]/sub-context-docs/[name].md` | Per-competitor mirror of brand-side structure |
| Competitor snapshot synthesis | `z-brands/[brand]/competitors/[group]/[competitor]/sub-context-docs/competitor-snapshot.md` | Rolls up the competitor's sub-context-docs |

## Global signal pools

| Type | Canonical | Notes |
|---|---|---|
| Creative-strategy expert insights | `global/knowledge/creative-strategy/expert-insights/` | Active v1 home for user-provided creative-strategy expert signals |
| Creative-strategy Parker taste | `global/knowledge/creative-strategy/parker-taste/` | Active v1 home for cross-brand creative taste, idea bank, and patterns to monitor |
| Team expert insights | `global/teams/[team]/expert-insights/` | Expert signal entries staged by team |
| Team Parker taste | `global/teams/[team]/parker-taste/` | Cross-brand team taste, idea bank, Parker ideas, and patterns to monitor |

## Skills

| Type | Canonical | Notes |
|---|---|---|
| Skill definition | `skills/[name]/SKILL.md` | Frontmatter (name, description, triggers) plus body |
| Skill processes | `skills/[name]/processes/[name].md` | One per process; INDEX.md lists them |
| Skill references | `skills/[name]/references/[name].md` | Reference material the skill loads |

## Index docs that need updates when content is added

| Index | What it lists |
|---|---|
| `parker-v2/README.md` | Top-level reference docs |
| `prompts/brand-profile/README.md` | Brand-profile prompts |
| `prompts/global-databases/README.md` | Database and memory specs |
| `parker-v2/reasoning-layer-notes/README.md` | Brand-audit reasoning library transcripts |
| `z-brands/[brand]/README.md` | Brand-specific outputs |

## What's NOT canonical here (because it's derived or runtime-only)

- Prompt reference paragraphs that point at a canonical doc — these are derived; the canonical doc is the source.
- The brand-profile sub-context-docs in `z-brands/[brand]/sub-context-docs/` — these are outputs of running the prompts.
- The `MEMORY.md` file in the auto-memory system — this is operational state, not canonical content.

## Coming in v2

- The full dependency graph showing which prompts reference which canonical docs.
- The "what gets stale when X changes" map.
- The runtime-load profile for each prompt category.
