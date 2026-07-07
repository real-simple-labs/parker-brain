---
name: dream
description: Run the dreaming system on demand for a brand and the person using it. Read the day of comms — the conversations the user had with Parker, plus any connected comms — against everything Parker has accumulated, and come back with proposals across six buckets: context updates, skill improvements, schedules to create, new ideas to research, new open loops, and the person (what Parker now understands about them and what to tee up for them). Framed as the morning suggestion. Use when Jimmy runs /dream or asks Parker what it has been thinking about, what it would suggest, or to dream on a brand.
triggers:
  - /dream
  - dream
  - dream on this brand
  - what have you been thinking about
  - what would you suggest for this brand
  - run dreaming
  - go think about this brand
  - what should we be working on
  - surface some ideas for this brand
---

# Dream

## Goal

Make it true that Parker was thinking — about the brand, and about the person using it. The user runs this and Parker reads the recent comms — first and foremost the conversations the user had with it — works out what it would do differently or chase next, and comes back with proposals the user can accept, refine, or dismiss. The feeling to create is the morning suggestion: "I was thinking about this, and here is what I would suggest." Never a change already made. The dreaming covers the human as well, not just the work: Parker gets to know the person over time and tees up what would genuinely help them.

Dreaming is the **planning** arm. The canonical method is `self-improvement/dreaming-system.md`; the full daily cycle (plan → human review → execute) is `self-improvement/the-living-loop.md`. Read both before running. Dreaming proposes, self-improvement disposes, the human stays in the loop. This skill executes the brand-dreaming stream on demand for one brand.

## Where this skill sits

- `improve-system` and the other executing skills **apply** what was already decided — corrective.
- `dream` **proposes** new directions Parker worked out on its own — generative.

Nothing this skill writes is applied on its own. Every output is a proposal that routes through the executing arm for promotion, exactly as `the-living-loop.md` describes. A dismissed dream is not deleted — its reasoning is preserved, because a rejected proposal teaches Parker what does not land just as a rejected idea-bank idea or archived open loop does.

## What this skill reads

A full sweep of everything connected, read against the vault. The Parker conversations are the richest single thread — read them closely — but they are the center of a wider sweep, not the whole of it. Each run, pull from every connector the user has linked: work email, Slack, calendar, task manager, Notion, docs, call and meeting transcripts, and the rest, to build the picture of the person and the organization, not just the Parker chat. Sweep the market too: the tracked competitor ad libraries, the organic niche feeds, and the open web for launches, pricing moves, press, and cultural moments. The brand's accumulated knowledge — its context docs, open loops, hypotheses, validations, idea bank — is the **ground** the whole sweep is read *against*, so Parker can tell whether something is genuinely new, contradicts what is on file, or closes something already open. Any source not connected this run is skipped and logged as a one-line blind spot, never guessed. **Sweep the work, not the private life:** the subject is the business, the org, and the market, never the person's private world. Within any source, read only what bears on the work and skip anything that reads as personal or private — personal texts, a family/health/money matter, a clearly-personal calendar entry. Purely personal channels like iMessage aren't swept at all. When in doubt whether it's work or private, leave it out.

Global product dreaming — the anonymized cross-brand read of struggle and value — is the slower offline stream and is **not** the job of a single user-invoked brand dream. It does not run here. If this pass surfaces a struggle or value pattern worth the global layer, contribute only the anonymized pattern, never the raw conversation, never the brand identity, per the privacy hard rule.

## How this skill runs

1. **Load the method.** Read `dreaming-system.md` for the streams, the five buckets, the storage layout, and the privacy hard rule, and `the-living-loop.md` for how the proposals get executed.

2. **Set the scope.** Identify the brand. Default to the current brand in context; ask if ambiguous.

3. **Read the day's comms against the vault, and capture verbatim.** Start with the conversations, add any connected team comms, and read them against the brand's accumulated knowledge to know what is genuinely new. As you read, preserve the exact words — quote the ask, the correction, the idea, the line that caught your eye. Do not summarize into a theme; the verbatim source is what every proposal downstream is built from.

4. **Produce the five-bucket proposals.**
   - **Context updates.** When a conversation reveals something the brand context docs do not capture or get wrong, propose the edit at the real living surface — not a net-new doc when an existing one absorbs it.
   - **Skill improvements.** When the way the user worked with Parker exposed a gap or a better way to run a task, propose the skill change. Brand-observed but usually promote upward, since skills are global — note that.
   - **Schedules to create.** When the user keeps asking for the same kind of job, propose a repo-native schedule rather than a repeated manual ask: "you've asked me to do this a few times now — want me to just run it every week?" Name the task, cadence, what it reads, what it updates, and what it delivers. A schedule is **not** an MCP workflow — see `system/schedules.md`. It does not run until the user confirms.
   - **New ideas to research.** When an open loop, a validation, a conversation, or a freshly scraped signal could be run with, route the strong ones to the brand idea bank under the idea bank's own rules, as `[~]` proposed — never self-trusted.
   - **New open loops.** When the day surfaced something with real pull and an answerable question, write it as a proper open loop (observation, named pull, the one exact question, justification, territory) per `system/open-loops-system.md`, and feed it into the open-loops pipeline. Capture the loop; do not weight or promote it here.
   - **The person.** Dream about the human, not just the work. Three things: what Parker now understands about them — a read on who they are, their process, their craft, a preference or standing rule they revealed — proposed as an update to `users/[user-id]/user-profile.md`, carrying the full verbatim moment that showed it. What to tee up for them — the proactive morning suggestion aimed at them, not the brand: what they'll likely need next given what they're working on, what to prep before they ask, a nudge on a deadline or a thread worth picking back up. This includes keeping the profile's "what they're working on" section live — read their actual task list and active work across the ecosystem and update the 30/60/90 to match: finished tasks roll into "what's landed," new ones appear, shifting priorities re-sort the horizon. And a better profile — a proposed change to how the profile itself is built when a new section, a split, or a sharper cut would serve this person better, per the growing-the-doc principle in the template. **Survey their whole ecosystem to build this read** — every MCP and connector they've linked: calendar, email, Slack, task manager, Notion, docs, call transcripts, and the rest, not just the Parker chats. Their real day lives across those tools; the fuller the ecosystem Parker sees each night, the truer it knows them and the more it can tee up, and the more they connect, the better it gets. All of it routes through `improve-system` for the human to confirm; nothing is written to the profile here.

5. **Write the outputs as proposals.** Save the run's observations under `z-brands/[brand]/dreaming/runs/[YYYY-MM-DD]/`, and each proposal under `z-brands/[brand]/dreaming/proposals/pending/` with its reasoning. Schedule proposals also surface at `z-brands/[brand]/schedules/proposed/`; open-loop proposals feed `z-brands/[brand]/open-loops/`; person proposals (profile updates + tee-ups) go under `dreaming/proposals/pending/` tagged for the user so `improve-system` folds the confirmed ones into `user-profile.md`. Everything lands as a proposal; promotion is a separate, human-approved step.

6. **Surface it as the morning suggestion.** Report what Parker was thinking about and what it would suggest — the proposals, with their reasoning, framed so the user can accept, refine, or dismiss each. Do not present any of it as done.

## Hard rules

- Read `dreaming-system.md` and `the-living-loop.md` first and follow them; this skill is the on-demand brand runner for the planning arm.
- **Capture verbatim, never generalize.** Record exactly what was said — the exact words, quoted — in the run notes and carry that source language intact into every proposal. A paraphrase has already lost the signal. When in doubt, quote more, not less.
- Propose, never apply. Every output is a proposal that routes through the executing arm with the human in the loop.
- Preserve the reasoning for every proposal, including ones the user dismisses.
- Privacy is absolute. Even brand dreaming never quotes a person where the pattern would do. Global product dreaming does not run here; if a pattern is worth the global layer, contribute the anonymized pattern only — no raw message, no brand identity, nothing that crosses the brand boundary.
- Route new ideas through the idea bank's own rules as `[~]` proposed; Parker does not fill its own idea bank with trusted taste.
- Write open loops to the open-loops spec; capture them, do not weight or promote inside this skill.
- Do not create net-new context docs when a living surface can absorb the proposed update.

## Output structure

### What I Was Thinking About
The morning-suggestion framing: a short read of what stood out across the day's comms, read against the vault.

### Context Proposals
Proposed edits to brand context docs, each with its reasoning and target surface, marked `[~] pending review`.

### Skill Proposals
Gaps or better ways to run a task, noted as brand-observed and flagged where they would promote upward.

### Schedule Proposals
Repeated asks worth standing up as repo-native routines, each naming the task, cadence, sources, what it updates, and deliverable, awaiting the user's confirmation.

### Idea Proposals
New ideas and concepts routed toward the brand idea bank under its own rules, as `[~]` proposed.

### Open-Loop Proposals
New loops the day surfaced, each written as observation, pull, the one exact question, justification, and territory, fed into the open-loops pipeline.

### The Person
What Parker learned about the human today — the read on who they are, their process, their craft, a preference or standing rule they revealed — each proposed as a `user-profile.md` update with the full verbatim moment that showed it. And the tee-up: the proactive morning suggestion aimed at them, what they'll likely need next and what to prep before they ask. Proposals, routed through `improve-system`; nothing written to the profile here.
