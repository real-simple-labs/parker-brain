# Parker self-improvement system

This is Parker's file-backed v1 method for getting better as the user and the team use it. The goal is not to remember every chat fragment. The goal is to preserve the reasoning traces that should change future behavior.

This doc is the **reasoning-trace substrate** of the living loop — the memory of *why* each change happened. The executing arm itself (how dreaming's five-bucket proposals get disposed, and how open loops run their lifecycle) is `self-improvement/the-living-loop.md`; the planning arm is `self-improvement/dreaming-system.md`. Read the loop for the motion; read this for the trace that motion leaves behind. Every applied change in the loop should carry a trace back to the proposal and conversation that caused it.

Doc type: system methodology. Scope: Parker-wide learning from user feedback, strategist judgment, expert signals, prompt failures, successful outputs, and repeated taste boundaries. Cadence: continuous capture during conversation; weekly curation; promotion only after approval, repetition, or strong evidence.

---

## Purpose

Parker improves when it can remember not only what changed, but why the change happened and what historical context shaped the decision.

The self-improvement system captures those reasons as **reasoning traces**. A reasoning trace is the explanation behind a correction, approval, rejection, reroute, strategic decision, hypothesis edit, taste boundary, or prompt rule. The trace should preserve the decision context: the user's stated why, the historical context that led to it, prior related decisions, rejected paths, relevant examples, constraints, and the tradeoff Parker should remember. It is the training signal Parker should use later when deciding what to load, what to write, what to avoid, and what to propose.

The system has four jobs:

1. **Capture feedback while it is fresh.** When the user corrects Parker, says "make this a rule," likes a direction, rejects a direction, or explains why something is wrong, Parker should preserve the underlying rule.

2. **Separate local preference from durable method.** Some feedback belongs only to one output. Some belongs to a brand. Some belongs to a skill, prompt family, or system-level rule. Parker must classify the scope before applying.

3. **Route learning into living surfaces.** A trace can update `CLAUDE.md`, a skill, a prompt, a brand note, a swipe file, an expert-signal candidate, a pattern-to-monitor file, or a review queue. It should not die in chat history.

4. **Keep the user in the loop.** Parker can infer a candidate lesson, but the user is the authority on the why and the history behind it. When the decision context is not explicit, Parker should ask for a context dump or confirmation before promoting the trace.

5. **Promote carefully.** One trace can create a candidate. Repeated traces, explicit user approval, or strong performance evidence can promote the candidate into a canonical rule.

---

## What counts as a reasoning trace

Capture a reasoning trace when the user does one of these:

- Corrects Parker's behavior and explains why.
- Says a rule should apply across prompts, docs, or the product.
- Approves a specific output because of a named reason.
- Rejects an output because it violated a taste boundary, product rule, or strategic principle.
- Reroutes where content should live.
- Gives expert content and asks what Parker or the user should learn.
- Edits Parker's hypothesis, framework read, hook description, or strategic recommendation.
- Names a repeated failure mode.
- Names a useful diagnostic distinction.

Do not create a trace for routine status updates, obvious typo fixes, one-off wording preferences, or source facts that already belong in a brand context doc.

---

## Trace schema

Every trace should use this shape.

```yaml
---
trace_id: YYYY-MM-DD-[short-slug]
date_captured: YYYY-MM-DD
source: chat, expert_signal, brand_output_review, prompt_run, audit_review, user_edit, other
source_ref: path, chat pointer, or short description
trigger_type: correction, approval, rejection, reroute, strategic_decision, hypothesis_edit, context_rule, taste_boundary, prompt_rule, product_rule
scope: local_output, user, brand, team, skill, prompt_family, system, product_architecture
brand: brand slug or global
team: creative-strategy, performance, organic-social, search, influencer, brand-pr-comms, partnerships, retention, global
confidence: strong, mixed, thin
status: captured, candidate, applied, rejected, superseded, needs_review
target_surfaces:
  - path or Parker surface
promotion_condition: explicit approval, repeated traces, account evidence, expert corroboration, or already applied
---
```

**A `user`-scoped trace** is a learning about the person, not the brand: who they are, their role, their process, their craft, how they like Parker to work, and the standing rules they set. It lands in `users/[user-id]/user-profile.md`, and where it touches how work gets done or who does it, it also rolls up into `operations-and-team.md`, the team profile, and the user-by-user part of `brand-notes-from-org.md`.

**Keep the full moment that caused a trace, verbatim — a hard rule, and the one the Anthropic team stressed.** Every trace records the real scene, word for word, not a paraphrase: the person's exact words, the Parker output they were reacting to, and enough of the surrounding conversation to understand why the rule exists. A correction is meaningless without the thing it corrected. When more history is needed to make the moment legible, keep more history. This is memory, not cross-brand product canon, so the verbatim belongs in the trace and rides into the surface it updates. The abstracted rule drifts; the full moment does not.

The body should answer:

- **What happened:** the user signal or output behavior, with the verbatim moment attached — their words, the Parker output, the surrounding exchange.
- **Decision context:** the user's why plus the historical context, prior decisions, rejected paths, examples, constraints, and tradeoffs that shaped the judgment.
- **Why it matters:** the underlying lesson Parker should carry forward.
- **Inferred rule:** the rule Parker should consider using later.
- **Scope judgment:** where the rule should and should not apply.
- **Routing:** where it was saved, what was updated, and what still needs review.

---

## File-backed v1 locations

The v1 learning layer lives under `self-improvement/`.

- `reasoning-traces/[YYYY-MM]/` - individual trace files.
- `review-queue.md` - traces that need the user approval or repeated evidence before promotion.
- `patterns/INDEX.md` - repeated learning patterns Parker is watching.
- `applied-changes.md` - promoted traces that changed canonical docs, prompts, skills, or brand surfaces.

This folder is not a replacement for brand memory, expert signals, or prompt docs. It is the routing layer that says what should change and why.

---

## Routing rules

Use the narrowest correct route.

- **Local output issue:** fix the output; capture a trace only if the issue is likely to recur.
- **Brand-specific learning:** route to `z-brands/[brand]/running-notes/`, brand rules, or the brand swipe file.
- **Creative-strategy operating pattern:** route to `global/knowledge/creative-strategy/parker-taste/patterns-to-monitor/` or expert-insights candidates.
- **Expert content:** route through `expert-signal-intake` first, then link any self-improvement trace to the saved expert signal.
- **Prompt or skill behavior:** create a self-improvement trace and route to the affected prompt or skill as a candidate.
- **System-level rule:** create a self-improvement trace, update `CLAUDE.md` only when the user explicitly asks or the rule is already clearly approved, and route larger changes through the update process.

Do not force every trace into a canonical edit. Capturing the reason is already useful. Promotion is a separate decision.

---

## Continuous capture loop

When feedback appears in conversation:

1. **Hear the correction.** Identify whether the user is fixing a local output, giving a product rule, or teaching Parker a reusable distinction.
2. **Name the trace.** Summarize the durable lesson in one sentence.
3. **Classify scope.** Decide whether the lesson is local, brand-specific, team-specific, skill-specific, prompt-family, or system-wide.
4. **Capture the decision context.** Save the why, the historical context, prior related decisions, rejected paths, examples, constraints, and tradeoffs. If that context is missing, invite the user to context dump before promotion.
5. **Route it.** Update the living surface if already approved; otherwise create a trace and candidate.
6. **Reflect it back.** Tell the user what Parker learned, what is still only a candidate, and what needs human confirmation.

This loop should be lightweight. Do not interrupt the user's workflow to over-document. Capture only the parts that will make future Parker meaningfully better.

---

## Weekly curation loop

Run weekly or before a major prompt/skill refresh:

1. Review new traces in `reasoning-traces/[YYYY-MM]/`.
2. Cluster repeated themes.
3. Promote repeated or approved rules into `applied-changes.md`.
4. Update affected prompts, skills, context docs, or brand surfaces.
5. Keep unresolved items in `review-queue.md` with a promotion condition.
6. Mark stale or contradicted traces as rejected or superseded.

Promotion should preserve provenance: cite the trace IDs that caused the change.

---

## Hard rules

- Preserve the user's decision context, not just the edited outcome.
- Keep the user as the human in the loop. Do not silently promote Parker's inferred why or incomplete historical context.
- Do not treat one correction as a universal rule unless the user says it is global or the pattern repeats.
- Do not create new docs when an existing living surface can absorb the learning.
- Do not hide uncertainty. Mark thin traces as thin.
- Do not overwrite brand-specific rules with global Parker rules.
- Do not update prompts or skills from one trace unless the user explicitly approves the promotion.
- Always connect an applied change back to the trace or source that caused it.

---

## Worked example

**User signal:** the user says the monthly hook audit should not include static ads.

**Trace:** Parker captures a prompt rule with monthly hook audit scope.

**Inferred rule:** Monthly hook audits should analyze video/organic-style hooks only; static ad reads belong in static-specific audits.

**Route:** Update `CLAUDE.md` because the user explicitly made it a product rule, update the monthly hook audit prompt, and flag existing monthly hook audit outputs for re-run if they include static ads.

**Do not route:** Do not add this to brand swipe files. It is not an idea. It is audit behavior.
