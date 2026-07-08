---
trace_id: 2026-07-03-user-profile-system
date_captured: 2026-07-03
source: chat
source_ref: Jimmy's initiative — a role-tailored user profile that loads every message, learns from chats, and gets a nightly human-dreaming pass, mirroring the brand system
trigger_type: product_rule
scope: product_architecture
brand: global
team: global
confidence: strong
status: applied
target_surfaces:
  - templates/user-profile-template.md
  - templates/brand-brain-CLAUDE-template.md
  - templates/brand-routines/claude/hooks/craft-context.py
  - self-improvement/self-improvement-system.md
  - .claude/skills/self-improvement-intake/SKILL.md
  - .claude/skills/improve-system/SKILL.md
  - .claude/skills/dream/SKILL.md
  - templates/brand-routines/claude/skills/dream/SKILL.md
  - self-improvement/dreaming-system.md
promotion_condition: already applied — Jimmy's directed initiative, built with his refinements
---

**What happened:** Jimmy launched the user-profile initiative: a deep, role-tailored understanding of the person using the brain — who they are, what they care about, their process, their taste, their likes and dislikes — living in a `user-profile.md` that loads into every message and updates from the chats, with a nightly dreaming pass for the human, not just the brand. The user-side mirror of the brand living-loop.

**Decision context:** A scaffold already existed (`users/[user-id]/user-profile.md` was a designated always-loaded surface; `improve-system` already targeted it), so the build extended the proven brand machinery rather than duplicating it. Jimmy's refinements shaped the template: "how they work" is the person's *literal process*, not personality labels; the "taste" section became *their craft* — their own version of the job, what makes them them at it — not "what's good to them"; a "rules they've set" section holds standing feedback so nobody has to say it twice; no parentheticals or example lists, kept loose so the model reasons instead of filling a form because it's so different per person; no onboarding questionnaire — it builds from usage because that's where the real signal is. Two hard rules he stressed, both from the Anthropic team: every entry keeps the **full verbatim moment** that caused it — the person's exact words, the Parker output they were reacting to, and enough surrounding conversation to understand it, never a paraphrase — and user-learnings **roll up** into ops, team, and org notes, not just the user doc. Always-load was wired two ways: the context hook injects the whole profile every turn when it exists (graceful when absent), and the brand CLAUDE.md map names it a read to honor on every reply. The loop: `self-improvement-intake` gained a `user` scope and captures user-learnings with the full moment; `improve-system` creates the profile from the template on first signal, populates the right sections, carries the verbatim, and rolls learnings up to ops/team/org; the nightly `dream` gained a sixth bucket — the person — proposing profile updates plus a proactive tee-up aimed at the human, reading everything connected aggressively.

**Why it matters:** The brain understood brands deeply and users barely. This closes that gap so the tool feels like it genuinely knows the person, adapts to their role and taste, honors their standing rules, and proactively helps them — the same care the brand system gets, pointed at the human.

**Inferred rule:** Memory of a person is only trustworthy if it carries the full moment that formed it, verbatim — the correction and the thing it corrected. Abstracted preferences drift; the real scene does not. And a person's memory is not siloed: it rolls up into the team and org picture.

**Scope judgment:** Foundation-first per Jimmy: the template + always-load shipped, then the loop. The nightly human-dreaming was folded into the existing `dream` (one pass, two lenses) rather than a separate run. Cross-brain user-profile sync (one person across multiple brand brains) is a known later concern; v1 learns the person as they show up in each brain. The verbatim-full-moment and roll-up rules are general to the whole self-improvement system, not just the user profile.

**Routing:** Template + CLAUDE.md map + context hook (foundation, committed separately); then `user` scope and the full-moment rule in `self-improvement-system.md`, user-learning capture in `self-improvement-intake`, lazy profile creation + populate + ops/team/org roll-up in `improve-system`, and the person bucket in both `dream` copies + `dreaming-system.md` + the dream schedule. System map updated. On the `user-profile-system` branch.
