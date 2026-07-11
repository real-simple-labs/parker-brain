---
name: update-parker-skill
description: Make a correct update to Parker's prompts, system docs, rubrics, knowledge docs, training corpus, or brand outputs — and propagate the change everywhere it needs to land. Use this skill whenever you are changing any part of the Parker context-engineering system, including tightening a rule, adding a principle, propagating a pattern, adding or modifying a prompt, adding a knowledge doc, or evolving a skill. The skill exists because Parker's docs are highly cross-referenced and inheritance-driven, and updates that look local often have non-obvious downstream impact.
triggers:
  - update the open-loops system
  - tighten this rubric
  - propagate this change across prompts
  - add a new VoC category
  - add this principle to the rubric
  - update the X methodology
  - fix this prompt
  - add a new knowledge doc
  - create a new skill
  - this rubric change means X needs to be re-run
  - make this update
  - apply this rule across all prompts
  - we need a skill that does X
  - update the system to handle X
---

# Update Parker Skill (v1)

## Goal

Make a correct update to Parker's context-engineering system — prompts, system docs, rubrics, knowledge docs, training corpus, skills, or brand outputs — without introducing drift, breaking cross-references, or missing downstream impact.

The skill is **not** for making changes that live entirely inside one file with no dependents. If the change is local to one prompt and that prompt is not referenced by anything else, just edit the prompt. The skill is for changes whose blast radius extends past the file the user pointed at, which in Parker's system is almost any rule, principle, or pattern change.

Before proposing a system update, check `self-improvement/` for reasoning traces or patterns that explain why similar changes were previously accepted, rejected, rerouted, or left in review. If the current request creates a new durable lesson, create or update a reasoning trace through `self-improvement-intake`.

## Global changes require human-in-the-loop. Always.

**This is the most important rule in this skill.** Global changes — anything touching the canonical system docs, rubrics, knowledge docs, templates, prompts, skills, or training corpus — require explicit human approval before any edits land. The skill always proposes the change first, waits for approval, then executes. No exceptions.

The reason: global changes have wide blast radius. A system-doc edit propagates to every prompt that loads it at runtime. A rubric change reshapes every open-loops generation across the system. A prompt edit affects every brand that runs that prompt. The cost of catching a wrong update at proposal time is one extra message in chat. The cost of catching it after propagation is undoing the change across many files and re-running affected brand outputs.

### What counts as global

- Any edit to a system doc, rubric, knowledge doc, methodology doc, or template at the `parker-v2/` top level (e.g., `system/open-loops-system.md`, `creative-strategy-context/creative-strategy-fundamentals.md`, `creative-strategy-context/public-ad-library-analysis.md`, `templates/voc-design.md`, `templates/personas-template.md`).
- Any edit to a prompt at `prompts/**`.
- Any edit to a skill at `skills/**` — including this one.
- Any new entry to the reasoning library at `parker-v2/reasoning-layer-notes/`.
- Any change to master index docs (`parker-v2/README.md`, prompt-category READMEs, training-corpus README).
- Any change to the master file structure.

### What is not global (and the skill can act more autonomously on)

- Brand sub-context-doc re-runs that apply an already-approved rule change to the brand's outputs. (Re-running is propagation of an already-approved rule, not a new global change.)
- Running-notes entries for a brand session.
- Source-pulls additions for a brand.
- Brand-specific README updates that index brand-only content.
- Brand-specific persona-profile or open-loops roll-up updates that follow from already-approved methodology.

When in doubt, treat the change as global and propose.

### The propose-then-execute pattern

The skill produces a structured proposal before any edits. The proposal includes:

1. **Canonical doc(s) being edited** — by path.
2. **Current content** — the relevant section quoted or summarized so the user can see what is being changed.
3. **Proposed new content** — the new wording or structure, complete enough that the user can give a yes/no without further questions.
4. **Why** — what is wrong with the current and how the proposed fix changes behavior. If a failure-mode diagnosis is part of the fix, name it.
5. **Propagation scope** — which dependent docs need updates, what kind (reference-paragraph edit vs full re-write), and how many files are affected.
6. **Training corpus updates** — which cases or reasoning entries need to change and how.
7. **Brand outputs flagged for re-run** — which outputs will need re-running after this change lands, with the impact named explicitly.
8. **Index doc updates** — which READMEs need new entries or updated entries.
9. **Migration impact** — every release ships its `migrations/vN.md` in the same change, per `migrations/README.md` and the Releases And Migrations rules in `CLAUDE.md`; the proposal decides what goes inside. Real steps when the change reshapes the brand repo itself (a renamed or moved path a brain references, a new standing file outside the copied bundle, an edit to brand-authored content, a brand-brain layout change); a one-liner no-op ("Nothing to do; record `vN`.") when the change is method-only or lives entirely in the copied bundle the pin bump's re-sync delivers.

The user then approves, redirects, or rejects. The skill executes only after explicit approval. If the user asks for changes to the proposal, the skill re-proposes — it does not start editing and assume the user will catch the differences.

### What counts as approval

A clear yes. "Go ahead," "do it," "yes," "approved," "execute," "ship it." If the user says "looks good but..." that is not approval — the "but" is the redirect, and the skill re-proposes.

Silence is not approval. If you can't tell whether the user approved, ask.

## Why this skill exists

Parker's docs are an inheritance graph, not a flat directory. A rule lives in one canonical place. Prompts reference the rule by loading the canonical doc alongside themselves at runtime. Training cases document how the rule was derived. Brand outputs are the consequence of the rule running. A change to the canonical rule has implications at every layer.

When updates happen ad-hoc, three failure modes recur:
- **Drift**: a rule is added to some prompts but not others, and runtime behavior diverges.
- **Stale references**: a knowledge doc is added but the prompts that should reference it aren't updated, so runtime model never loads it.
- **Stale outputs**: a rule changes but the brand outputs that were generated under the old rule are not flagged for re-run, so production state silently violates the new rule.

This skill exists to catch all three at update time.

## How this skill runs

The skill runs in two phases: **propose** (always, for global changes) and **execute** (only after explicit user approval). Steps 1–5 below produce the proposal. Steps 6–10 are the execution.

### Phase 1 — Propose (no edits yet)

1. **Identify what kind of update this is.** The propagation pattern depends on the update type. See the process index in `processes/INDEX.md` for the major types and which process to load. If the update doesn't match a named type, use the general-update process as a starting point.

1a. **Check prior reasoning traces.** Search `self-improvement/` for related corrections, approvals, rejections, product rules, taste boundaries, or prompt rules. These traces are not automatically canonical, but they explain the user's prior reasoning and should shape the proposal.

2. **Identify the canonical location.** Every rule, principle, knowledge piece, or template has one canonical home. The canonical home is where the change goes first. See `references/canonical-locations.md` for the full map.

3. **Identify the dependency graph.** Which docs reference the canonical doc? Two kinds of dependencies matter:
   - **Runtime references** — docs that say "load alongside this prompt" or "see [X] for the methodology." These inherit at runtime.
   - **Logical references** — docs that don't formally reference the canonical doc but encode the same rule in their own language. These drift if not updated.

   Use `grep -r` to find both kinds across the relevant directories.

4. **Decide the propagation scope.** Three patterns:
   - **Inherit via reference** — change only the canonical doc; runtime references propagate automatically. Use when the canonical doc is loaded alongside at runtime and the prompts already reference it correctly. Lowest-effort, lowest-drift-risk option.
   - **Inherit via reference + tighten prompt reference paragraphs** — change the canonical doc; update the short reference paragraph each prompt carries so the new rule is invoked by name at runtime. Use when the rule needs to be explicitly named in each prompt's section to be reliably invoked.
   - **Direct edit each affected file** — when the inheritance pattern doesn't exist for this rule, or when the rule is encoded in each prompt's own language. Highest-effort, highest-drift-risk; use only when the inheritance pattern can't be added.

5. **Write the proposal and wait.** Use the structure defined under "The propose-then-execute pattern" above. The proposal must include all eight elements (canonical doc, current content, proposed content, why, propagation scope, training corpus updates, brand-output re-runs, index updates). Then stop. Do not edit. Wait for the user to approve, redirect, or reject.

   If the user redirects, revise the proposal and present again. Do not start editing and assume the user will catch the differences.

   If the user rejects, the skill ends. No edits.

### Phase 2 — Execute (only after explicit approval)

6. **Make the canonical change.** Edit the canonical doc first. Write it as the new source of truth.

7. **Propagate per the approved scope.** If inheriting via reference, verify each dependent prompt actually loads the canonical doc by name. If updating reference paragraphs, make the same edit consistently across all affected prompts.

8. **Capture the reasoning per the approved scope.** If the change is a new open-loops reasoning move or prior, add it to `creative-strategy-context/creative-strategy-fundamentals.md`. If the change reshapes how a prompt should work, add a new entry to `reasoning-layer-notes/` documenting the move.

9. **Update index docs per the approved scope.** READMEs that list affected docs need to reflect new files, new sections, or new references. Common ones: `parker-v2/README.md`, `prompts/brand-profile/README.md`, brand README files.

10. **Output the diff summary.** Tell the user exactly what changed at the canonical layer, what propagated where, what indexes were updated, and what brand outputs are flagged for re-run. This is the contract — the user should be able to verify the update is complete.

   Brand-output re-runs are flagged but not executed in the same turn unless the user explicitly asks. A rule change is one global update; the brand-output re-runs that follow are propagation of an already-approved rule and can be queued as a separate batch.

## Principles every new skill is born with

New skills inherit the system's structural standards at creation time, not by retrofit. When this skill is used to add a skill (or materially reshape one), check the draft against these before proposing it:

- **Creative deliverables get both ship gates.** Any skill whose output includes words a customer will read or hear wires the two-gate sequence: the `context-grounding-review` agent first (inputs — was it built from the right method docs, brand context, and pulls; a bounce means re-pull and regenerate), then the `creative-voice-review` agent (surface — does it read human). Each gate gets its receipt block in the output structure (Grounding Review, Voice Review) and its hard rule, and every bounce is captured through `self-improvement-intake` as a one-line reasoning trace so the routing layer learns from the catch. The five creative skills are the reference wiring.
- **Strategy-first baseline for creative skills.** A skill that executes tactically — scripts, headlines, hooks, assets, iterations — loads the brand's committed strategy (`strategy/`) as the frame before anything else, and checks the idea bank (including evaluated ideas) for the entry the request should execute from. A request that cuts against the committed strategy is surfaced with the conflict named, never silently executed; a brain without those surfaces yet gets one line saying so.
- **Enforcement is structural, never just instructional.** A behavior that must survive a cloned brain on a stranger's machine uses the stack: a deterministic check where one is possible (a script that cannot be argued with), an independent reviewer context where judgment is needed — independent *and equipped*: the reviewer never wrote the draft it grades, and it loads the same canonical expertise the work was built from before judging — and an output contract that makes a skipped step visible in the output itself. Instruction text alone is the failure mode, not a design.
- **Canonical-doc-plus-reference, never pasted rules.** A new skill references the canonical doctrine by name (`spoken-script-voice.md`, `ai-writing-tells.md`, the routing map) rather than copying its rules inline — pasted copies drift on the next canonical edit.
- **Register-match customer language.** Written sources (reviews, surveys, threads) ship verbatim in written deliverables and get voiced — same vocabulary, re-cadenced for the mouth — in spoken ones, per the written-vs-spoken rule in `spoken-script-voice.md`. A skill that touches customer language in both registers carries this distinction explicitly.
- **Provenance on anything durable.** Outputs that later work depends on carry their sources per `system/attribution-principle.md`, and receipts (Brand Context Applied, sign-offs, gate blocks) are part of the output contract, not optional trim.
- **Ship-list check.** A new skill that adds files outside `.claude/skills/` (agents, scripts, knowledge docs) extends the onboarding-runner ship step in the same pass — and if already-built brains need the file too, the release's migration carries it (`migrations/README.md`) — or the skill works in the factory and points at nothing in every brand brain.

## When NOT to use this skill

Skip the full process when:

- The change is a typo, wording cleanup, or local clarification that has no semantic effect on the rule's meaning.
- The change is fully contained inside one brand's output and doesn't affect rules or methodology.
- The change is a new running-notes entry for a brand. Running notes are append-only and have no dependency graph.

In these cases, edit directly.

## Anti-patterns this skill exists to prevent

**Executing a global change without explicit approval.** The single hardest rule in this skill. The proposal-then-execute pattern is not optional. The skill always proposes global changes and waits for the user before any edits land. Skipping the proposal because the change "seems obvious" or "is small" is the failure mode that produces the worst kind of drift, because the user never sees the change before it lands.

**Treating a redirect as approval.** "Looks good but change X" is not approval. The "but" is the redirect, and the skill re-proposes with X changed. Editing under a "looks good but" surfaces the X-change but also propagates whatever else the skill assumed was approved.

**Duplicating content in multiple prompts.** When the same rule is written in five places, each version drifts on the next edit. Canonical-doc-plus-reference is the answer; if you find yourself pasting the same paragraph into N prompts, stop and add a knowledge doc instead.

**Forgetting cross-references in index docs.** A new prompt or knowledge doc that isn't indexed in its README is hidden from the next reader. Always update the README.

**Forgetting the training corpus.** When the rule changes, the case files that derived the rule become out of date with the rule itself. Update them so the corpus stays internally consistent.

**Not flagging downstream re-runs.** A rule change without a brand-output re-run flag silently leaves production state stale. Always state which outputs need re-running, even if you're not the one doing the re-run.

**Adding new principles without examples.** A rule that says "do X" without showing what X looks like in practice will be applied inconsistently. Pair every new principle with at least one worked example, ideally pulled from a training case.

**Updating prompts before the canonical doc.** When the canonical doc is the source of truth, updating prompts first means the prompts now point at a doc that doesn't match. Always edit canonical first.

## What v1 covers and what comes later

This is a v1. It covers the structure, the canonical locations, the propagation patterns, and the major anti-patterns. The processes are sketched in `processes/INDEX.md` and one detailed process is provided.

Coming in v2 (riff items the user has flagged):
- Detailed process files for each update type.
- The full dependency-graph reference doc.
- A canonical-locations reference doc with the complete map.
- A diff-output template for the closing summary.
- An "is this update worth doing?" pre-check, since some proposed updates are better deferred or rejected outright.
