---
name: improve-system
description: Apply the self-improvement system on demand. Read the accumulated reasoning traces and update this brand's and this user's living context to reflect what Parker has learned. Use when Jimmy runs /improve-system or asks Parker to apply what it has learned, fold the traces in, or get this brand's context up to date with recent feedback.
triggers:
  - /improve-system
  - improve system
  - improve the system
  - apply the reasoning traces
  - apply what you've learned
  - fold in the traces
  - update this brand's context with what you've learned
  - curate the reasoning traces
  - run self-improvement
  - bring the context up to date with my feedback
---

# Improve System

## Goal

Turn the reasoning traces Parker has been capturing into actual updates to the two surfaces the user named when they ran this: **this brand's** context and **this person's** context. Capture already happened — `self-improvement-intake` wrote the traces during conversation. This skill is the application pass: read every relevant trace, cluster the repeated ones, and fold the promotable learning into the living surfaces so future runs inherit it.

This is the on-demand form of the weekly curation loop in `self-improvement/self-improvement-system.md`. Read that method before applying anything — it is the governing authority on scope, promotion, and the human-in-the-loop rule. This skill executes its application step against one brand and one user.

## Where this skill sits

- `self-improvement-intake` **captures** — passive, during conversation, writes traces.
- `improve-system` **applies** — invoked by the user, reads the traces, updates brand and user context.
- `dream` **proposes** — generative, surfaces new directions; this skill is corrective, it folds in what was already decided.

Running this skill is the user opening the door to apply learning. It is not a blanket promotion of every trace. Per-trace promotion conditions still hold: apply what is clearly promotable, draft what is plausible but needs a look, and leave thin or contested traces in review. The user invoking the command does not turn a one-off correction into a universal law.

## What this skill updates

The user named two targets. Stay inside them.

- **Brand context** — `z-brands/[brand]/brand-profile.md`, `z-brands/[brand]/running-notes/brand-notes-from-org.md` and its children, most often `brand-rules.md` for fact-based DOs and DON'Ts and `success-definition.md` for the north star, plus the relevant sub-context doc, open loop, or brand idea bank when a trace clearly belongs there.
- **User context** — `users/[user-id]/user-profile.md` for the user's role and durable working preferences, and `users/[user-id]/[brand-id]/brand-notes-from-user.md` for how this user engages with this brand.

Traces scoped to a skill, a prompt family, or the system architecture are **not** applied here. This skill updates brand and user context. Surface those broader traces in the report so they route through their own promotion path — `update-parker-skill` for skill changes, the prompt family for prompt rules, the curation loop for system docs — rather than being quietly written into brand or user context where they do not belong.

## How this skill runs

1. **Load the method.** Read `self-improvement/self-improvement-system.md`. It governs scope classification, the promotion conditions, and the hard rules. This skill does not restate them; it obeys them.

2. **Set the scope.** Identify the brand and the user this pass is for. Default to the current brand in context and the current user. If either is ambiguous, ask before touching anything — applying one brand's traces to another, or one user's preferences to the team, is the failure this skill must never cause.

3. **Gather the traces.** Read across `self-improvement/reasoning-traces/[YYYY-MM]/`, the repeated themes in `patterns/INDEX.md`, and anything parked in `review-queue.md`. Keep the ones whose `scope` is brand-specific to this brand, or user-specific to this user. Hold aside skill, prompt-family, and system-scoped traces for the report. Skip traces already marked `applied`, `rejected`, or `superseded`.

4. **Cluster and dedupe.** Group traces that teach the same lesson. A lesson repeated across three traces is stronger evidence than one; note the count, because repetition is itself a promotion condition. Keep the trace IDs together — provenance travels with the change.

5. **Decide what is promotable.** For each cluster, check the promotion condition from the method: explicit user approval, repeated traces, account or performance evidence, expert corroboration, or already-applied-elsewhere. A cluster that meets one is ready to fold in. A cluster that is thin, single-source, or contested is not — it stays in review with its promotion condition recorded.

6. **Fold each promotable lesson into its narrowest correct surface.** Use the brand and user targets above. Update the living surface; do not create a net-new doc when an existing one absorbs the learning. Preserve the decision context, not just the outcome — the surface should carry why, drawn from the trace. Cite the trace IDs inline or in the surface's provenance so the change can always be traced back. A brand-specific gate goes to `brand-rules.md`; a durable user preference goes to `user-profile.md`; an idea-bank-worthy idea routes through the idea bank's own rules as `[~]` proposed, never auto-trusted.

7. **Mark state honestly.** Where a trace cleanly meets its promotion condition and the user has invoked this pass to apply it, write the update as applied and record it in `applied-changes.md` citing the causing trace IDs. Where the application is Parker's reasonable read but the why is thin or the scope is uncertain, write it `[~] pending review` and leave the user a clear decision. Update each handled trace's `status` to `applied` or back to `needs_review`.

8. **Keep the human in the loop.** Parker can fold in what is clearly decided, but it does not silently promote an inferred why or stretch a local correction into a brand rule. When the decision context behind a cluster is missing, do not guess it — surface the cluster and invite the user to confirm or context-dump before it is promoted.

9. **Report back.** Tell the user what landed where: what was applied to the brand, what was applied to the user, what is `[~] pending review`, what stayed in the queue as thin, and which skill/prompt/system traces need their own promotion route. Lead with the changes made.

## Hard rules

- Read `self-improvement-system.md` first and obey its hard rules; this skill is its application arm, not a replacement.
- Only ever touch the brand and user named for this pass. Never bleed one brand's or one user's traces into another, and never overwrite a brand-specific rule with a global one.
- Apply only what meets a promotion condition. Invoking the command does not promote every trace; thin, single-source, or contested traces stay in review.
- Preserve decision context and cite the causing trace IDs on every applied change. A change with no provenance is not allowed.
- Do not silently infer a missing why. Ask the user when the decision context behind a cluster is unclear.
- Do not apply skill, prompt-family, or system-scoped traces here. Surface them for their own promotion route.
- Do not create net-new docs when a living surface can absorb the learning.
- Mark applied as applied and provisional as `[~] pending review`. Do not blur the two.

## Output structure

### Applied To Brand
The brand surfaces updated, what changed, and the trace IDs behind each.

### Applied To User
The user surfaces updated, what changed, and the trace IDs behind each.

### Pending Review
Drafts written `[~]` that need the user's look, and clusters held back as thin or contested with their promotion condition.

### Routed Elsewhere
Skill, prompt-family, and system-scoped traces surfaced for their own promotion path.
