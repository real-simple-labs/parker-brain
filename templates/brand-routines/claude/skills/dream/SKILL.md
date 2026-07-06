---
name: dream
description: Parker's dreaming run for the brand and the person using it — the planning half of the living layer. Reads the day's comms (the conversations the user had with Parker first, then any connected comms) against the vault and returns proposals across six buckets — context updates, skill improvements, schedules to create, new ideas to research, new open loops, and the person (what Parker now understands about them and what to tee up for them) — into dreaming/proposals/pending. Captures verbatim; proposes, never applies; promotion runs through self-improve with the human in the loop. Use daily as a scheduled routine, or when asked to "dream", brainstorm overnight, or "what were you thinking about".
---

# Dream — the generative half of the living layer

Dreaming is how Parker stays *living*. It is the offline cycle where Parker thinks about everything it has accumulated for the brand and comes back with proposals: ways to improve its own context and skills, recurring work it could take off the user's plate, and fresh ideas worth chasing. The feeling it is built to create: Parker was thinking about the brand overnight — "I was thinking about this last night, here's what I'd suggest."

**Dreaming proposes; self-improvement disposes.** Nothing here is applied on its own. Every proposal lands in `dreaming/proposals/pending/` and is promoted only through the `self-improve` routine, with the human in the loop.

## When it runs

**Daily.** Brand dreaming runs on the conversation and the accumulated knowledge, so it refreshes as the brain grows and surfaces on a morning rhythm — that daily cadence is what makes the morning suggestion possible.

## What it reads (the day's comms, against the vault)

**The day's comms are the subject; the vault is the ground.** The conversations the user had with Parker are the first and richest source — read them closely and let them drive the run. Then any team comms the brand has connected (iMessage, Slack, email, transcripts) via MCP as those come online. Read the day's comms *against* the brand's own surfaces — `sub-context-docs/`, `personas/`, `competitors/`, `running-notes/`, `open-loops/`, `hypotheses/`, `validations/`, `audits/`, `source-pulls/`, `idea-bank/`, and fresh Parker MCP / web data — to know whether something said today is new, contradicts what's on file, or closes something already open.

**Capture verbatim — this is the hard rule.** Record what was *actually said*: the exact words, the exact ask, the exact idea, quoted. Generalizing is the failure mode — a flattened "the user wanted stronger hooks" is something the executing arm can't build from; the real line is. An LLM's instinct is to summarize; resist it. Quote more, not less, and carry that source language intact into every proposal.

## What it produces — proposals only

Write each as a file in `dreaming/proposals/pending/[YYYY-MM-DD]-[id].md`, and log the run's raw observations under `dreaming/runs/[YYYY-MM-DD]/`. Each proposal carries its reasoning so a *rejected* dream teaches Parker what doesn't land, exactly as a rejected idea or open loop does.

Six buckets of proposal:

1. **Context updates.** When a conversation or fresh read reveals something the brand context docs don't yet capture or get wrong, propose the edit (point at the doc and the change; do not make it). This bucket also carries **new surfaces**: when a connected tool keeps surfacing a kind of truth the brain has no home for, or the team keeps asking about a domain with no standing doc, propose growing the brain — the new folder or doc, what feeds it, and what it would be watched for — per `parker-system/system/growing-the-brain.md`. The scaffold is a floor, not a ceiling; dreaming is where growth is supposed to start.
2. **Skill improvements.** When the way the user works with Parker exposes a gap or a better way to run a kind of task, propose the skill change. These are brand-observed but often promote *upward*, since skills are global — flag that.
3. **Schedules to create.** When the user keeps asking for the same kind of job, propose standing it up as a repo-native schedule ("you've asked me this a few times — want me to run it weekly?"). A schedule is **not** an MCP workflow (see `schedules/README.md`). Name the task, cadence, what it reads, what it updates, and the deliverable; the proposal lands in `schedules/proposed/` and does not run until confirmed.
4. **New ideas to research.** When an open loop, a validation, a conversation, or a freshly scraped signal could be run with, route the good ones to the idea bank under its own rules, as `[~]` proposed (see `harvest-ideas`).
5. **New open loops.** When the day surfaced something with real pull and an answerable question, write it as a proper open loop — observation, named pull, the one exact question, justification, territory — and feed it into `open-loops/`. Capture the loop; `self-improve` weights and promotes it, not this run.
6. **The person.** Dream about the human, not just the work — this is what makes the brain feel like it knows them. Two things. First, what Parker now understands about the person: a read on who they are, their process, their craft, a preference or a standing rule they revealed today — proposed as an update to `users/[user-id]/user-profile.md`, carrying the full verbatim moment that showed it. Their own words in their own profile is the point here, so quote them exactly, not the pattern. Second, the tee-up: the proactive morning suggestion aimed at *them*, not the brand — what they'll likely need next given what they're working on, what to prep before they ask, a nudge on a deadline or a thread worth picking back up. Read everything connected to build this read. Profile-update proposals route through `improve-system` for the person to confirm; nothing is written to the profile in this run.

## Hard rules

- **Capture verbatim, never generalize.** Record exactly what was said — quoted — in the run notes and carry that source language into every proposal. A paraphrase has already lost the signal. Quote more, not less.
- **Proposes, never applies.** Every output is a proposal in `dreaming/proposals/pending/`. No context doc, skill, schedule, idea, or loop is promoted without going through `self-improve` and the human.
- **Preserve the reasoning** behind every proposal, accepted or dismissed.
- **Never quote a person where the pattern would do.** Brand dreaming stays inside the brand; still, surface the pattern, not the raw private message.
- **Honor the brand hard rules** on any drafted idea or copy (see `CLAUDE.md` and `running-notes/brand-notes-from-org.md`).
- **Ground in the vault.** A dream that could have been written without this repo is a failed dream. Load the `parker-system/creative-strategy-context/` docs per the `CLAUDE.md` routing table before proposing anything creative.
- Self-contained: read only in-repo surfaces and live data. No factory (`parker-brain`) paths at runtime.

## Note on global product dreaming

The factory also runs a *global product dreaming* stream that reads anonymized signals across all brands (struggles + value, for cross-pollination). That stream lives with the factory's `self-improvement/product-signals/`, **not** in this brand repo, because it must never let one brand see another's data. This skill is **brand dreaming only** — the stream that stays inside the brand.

## Deliverable

A dated run folder under `dreaming/runs/`, a set of proposal files in `dreaming/proposals/pending/`, and a short morning-suggestion summary: "here's what I was thinking about — N proposals, the top one is …".
