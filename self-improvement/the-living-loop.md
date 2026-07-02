# The living loop — dreaming and self-improvement

This is the doc that ties Parker's two learning arms into one daily cycle. It exists so neither `dreaming-system.md` nor `self-improvement-system.md` has to absorb the other's job. Read it first when you want to understand how Parker actually gets better day to day; read the two arm docs when you want the detail of either side.

## The cycle in one line

**Dreaming plans, the human reviews, self-improvement executes.**

Dreaming is the **planning** arm — it reads the day's comms and surfaces what could change. Self-improvement is the **executing** arm — it does the actual CRUD on the system once a human signs off. Between them sits the gate: nothing dreaming proposes is applied on its own.

```
the day's comms
      │
      ▼
  DREAMING (plan)  ──►  five buckets of proposals
      │
      ▼
  HUMAN REVIEW (the gate)  ──►  accept / refine / dismiss
      │
      ▼
  SELF-IMPROVEMENT (execute)  ──►  CRUD across the five streams
      │
      ▼
  the system is now different (and the reasoning is on file)
```

A dismissed proposal is not deleted — its reasoning is preserved, because a rejected proposal teaches Parker what does not land.

## The five streams

Dreaming plans across five buckets (see `dreaming-system.md`). Self-improvement executes each as create / read / update / delete, using the skill that already owns that surface. The loop does not invent new machinery for the five — it names which existing arm runs each.

| Bucket (dreaming plans) | Self-improvement executes (CRUD) | Executing skill | Lands in |
|---|---|---|---|
| **Context updates** | edit / add / correct / retire a context doc | `improve-system` | brand context docs |
| **Skill improvements** | add / refine / retire a skill | `update-parker-skill` | `.claude/skills/` (global) |
| **Schedules** | stand up / edit / pause / remove a cron routine | schedules CRUD (see `system/schedules.md`) | `z-brands/[brand]/schedules/` + Claude Code cron |
| **New ideas** | log / refine / promote / cut an idea | `brand-idea-bank-maintenance` | `idea-bank/` |
| **New open loops** | capture, then run the lifecycle below | `open-loops-advance` → `open-loops-validate` | `open-loops/` → `hypotheses/` → `validations/` |

The first four are ordinary CRUD: the human approves, the skill applies the change, and the change is connected back to the dreaming proposal that caused it (provenance is never dropped). The fifth is not a single edit — it is a lifecycle, and it gets its own pass.

The skills named above are the **factory** skills. A shipped brand brain is self-contained and may decompose them differently — e.g. a single `self-improve` skill running the context / open-loop / re-validation jobs, and a `harvest-ideas` + `evaluate-ideas` split for the idea stream — because the factory does not travel when the brain is cloned. The streams and the gate are identical; only the skill packaging differs. When reconciling a brand instance against this spec, match by stream, not by skill name.

## The open-loop lifecycle

Open loops are the one stream that doesn't resolve in a single edit, because a loop is a question and answering it takes a test. The canonical chain lives in `system/open-loops-system.md`; the loop runs it verbatim. Self-improvement's job is to move each captured loop through it:

1. **Review.** Read the loops dreaming captured (plus any standing open loops) and weight each one — Stakes, Confidence, Researchability, Novelty — per the open-loops scoring.
2. **Promote or archive.** Tier-1 and Tier-2 loops are **promoted** into the hypothesis queue; loops below the bar are **archived** with their reasoning, so the brand profile gains a known dead-end-at-this-bar rather than losing the noticing. (`open-loops-advance`.)
3. **Test.** A promoted loop becomes a **hypothesis** — the question turns into a prediction plus a plan within Parker's actual capabilities — and the plan runs. (`open-loops-validate`.)
4. **Resolve into one of four states.** The test returns **validated**, **invalidated**, **inconclusive**, or **insufficient evidence**. A validated finding lands in the always-loaded brand profile; an invalidated one becomes a known dead end; inconclusive and insufficient route to a re-run or the archive with their reasoning. Then the loop closes by **opening the next one** — a finding almost always raises a new question, captured for the next pass so the chain feeds itself instead of dead-ending at a verdict.

This is the part of the loop that makes Parker a strategist rather than a note-taker: it doesn't just record what the day surfaced, it tests the consequential questions and lets the answers change the brand's docs.

## The human-in-the-loop gate

The gate sits between planning and executing, and it is non-negotiable. Parker can infer a candidate change, but the user is the authority on the why and the history behind it.

- **Dreaming never applies.** Every one of the five buckets surfaces as a proposal the user can accept, refine, or dismiss.
- **Self-improvement promotes carefully.** One signal makes a candidate; explicit approval, a repeated pattern, or strong evidence promotes the candidate to canonical. A single correction is not a universal rule unless the user says it is global or the pattern repeats. (See `self-improvement-system.md` on reasoning traces — the substrate that records *why* each change happened.)
- **How much latitude Parker has to run on its own is a user setting.** Most context edits, idea logging, and low-stakes loop promotion Parker can do and report back. Schedule creation, skill changes, and any novel, high-stakes loop come to the user first.

## Where the substrate fits

`self-improvement-system.md` describes **reasoning traces** — the file-backed record of *why* a change happened, the decision context behind it. The living loop is the motion (plan → review → execute across the five streams); the reasoning trace is the memory that motion leaves behind. Every applied change in the five streams should carry a trace back to the dreaming proposal and the conversation that caused it, so future dreaming reads can see not just what changed but why. The loop is how Parker acts; the traces are how Parker remembers why it acted.

## Cadence

The loop runs on the day's comms, so it has a daily rhythm — which is exactly what a nightly dreaming **schedule** automates (see `system/schedules.md`). The open-loop lifecycle runs on its own clock inside the loop: capture is daily, weighting and promotion run on the open-loops roll-up cadence, and validations carry a `revalidate_by` so a confirmed finding is never assumed to hold forever.
