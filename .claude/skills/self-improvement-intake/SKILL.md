---
name: self-improvement-intake
description: Capture reasoning traces from user feedback, approvals, rejections, reroutes, expert learnings, and strategic decisions so Parker improves over time.
triggers:
  - make this a rule
  - remember this
  - learn from this
  - don't do that again
  - always do this
  - that's better
  - this should apply everywhere
  - why did you do that
  - parker should get better
  - self-improving
  - reasoning trace
  - capture this feedback
---

# Self-Improvement Intake

## Goal

Turn important feedback from normal conversation into durable Parker learning. The saved unit is the reasoning trace: what happened, the decision context behind it, why it mattered, what rule Parker should infer, where it applies, and what should change.

The canonical method lives at `self-improvement/self-improvement-system.md`. Read it before creating or updating traces.

## When this skill runs

Run this skill when Jimmy corrects Parker, approves a direction for a specific reason, rejects a direction, reroutes where content belongs, says something should become a rule, explains a taste boundary, or asks Parker to improve from a conversation.

This skill can also run after expert-signal intake when the expert source changes Parker's product architecture or operating method.

## How this skill runs

1. **Identify the learning moment.** Decide whether the user's message contains a durable lesson or only local feedback.

2. **Capture the decision context, with the full moment verbatim.** Preserve why the user made the correction or decision and the historical context that shaped it: prior related decisions, rejected paths, examples, constraints, and tradeoffs. Do not save only the changed output. And keep the real scene word for word — their exact words, the Parker output they were reacting to, and enough of the surrounding exchange to understand why the rule exists. A correction is meaningless without the thing it corrected. This verbatim-full-moment capture is a hard rule from `self-improvement-system.md`; when more history is needed, keep more. If the decision context is not explicit, invite the user to context dump or confirm Parker's inferred read before promotion.

3. **Classify scope.** Use the narrowest accurate scope: local output, **user**, brand, team, skill, prompt family, system, or product architecture. A learning about the *person* — who they are, their process, their craft, how they like Parker to work, or a standing rule they set for themselves — is `user`-scoped.

4. **Route to the living surface.** User-specific lessons go to `users/[user-id]/user-profile.md` (their rules, process, craft, preferences) and roll up to `operations-and-team.md`, the team profile, and the user-by-user part of `brand-notes-from-org.md` where they touch how work gets done. Brand-specific lessons go to brand memory or brand rules. Expert method signals go through expert insights. Prompt or skill lessons become candidates. System-level lessons go to self-improvement traces and, when approved, canonical docs.

5. **Create or update a trace.** Save new traces under `self-improvement/reasoning-traces/[YYYY-MM]/`. If an existing trace or pattern already covers the lesson, update it rather than creating a duplicate.

6. **Keep Jimmy in the loop.** Parker may create a candidate trace from an inferred lesson, but Jimmy must confirm the why and the relevant historical context before the trace becomes a promoted rule.

7. **Promote carefully.** Do not update prompts, skills, or system docs from one trace unless Jimmy explicitly approves the promotion or the trace is repeated and already aligned with canonical direction.

8. **Report back.** Tell the user what Parker learned, where it landed, what is still only a candidate, and where Parker needs the user's why.

## Trace categories

- **User learning:** who the person is, their process, their craft, how they like Parker to work, or a standing rule they set — routes to their user profile.
- **Strategic decision:** why a strategy split, recommendation, or direction changed.
- **Hypothesis edit:** why Parker's explanation of what worked was corrected.
- **Context rule:** what Parker should load, avoid loading, or treat as canonical.
- **Prompt rule:** how a prompt family should behave.
- **Skill rule:** how a runtime skill should reason or execute.
- **Taste boundary:** what quality bar, style, or creative judgment Parker should preserve.
- **Product rule:** how Parker v2 itself should be structured.

## Hard rules

- Do not save every chat turn.
- Do not over-promote one-off feedback.
- Do not silently infer the why or the missing history. Ask when the decision context is unclear.
- Do not blur brand-specific rules with global Parker rules.
- Do not create new docs when an existing trace, pattern, or living surface can absorb the learning.
- Do not rewrite prompts or skills from one trace without approval.
- Always preserve source, scope, status, and promotion condition.
- Keep the full moment verbatim — their words, the Parker output, the surrounding exchange — never a paraphrase. This is the hard rule the Anthropic team stressed, and it is what keeps a rule from drifting.
- When the user says "make this a rule," treat it as strong evidence and update the right canonical surface if the scope is clear.

## Output structure

### Learning Captured

Name the trace or existing surface updated.

### Scope

State whether the lesson is local, brand, team, skill, prompt-family, system, or product architecture.

### Routing

List what changed and what remains in review.

### Next Watch

Name what Parker should watch for in future conversations to confirm, reject, or sharpen the rule.
