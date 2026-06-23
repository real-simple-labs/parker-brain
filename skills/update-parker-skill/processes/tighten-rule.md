# Process: tighten a rule

The most common update type and the one with the highest drift risk. A rule sharpens, narrows, or hardens — usually because the existing rule had a loophole that produced bad outputs in practice.

The defining example: the open-loops system used to say "If a loop has several tightly related sub-questions, list them as exact questions too." That permitted the multi-question failure mode. The tighten-rule update replaced it with "One question per loop, almost never more" plus an explicit "the sub-question list is the tell, fix it" diagnosis.

## When to use this process

- The rule's current wording permits the failure mode you want to forbid.
- Existing brand outputs were generated under the old rule and now violate the new rule.
- The dependent prompts reference the canonical doc but don't quote the rule directly, so propagation is via inheritance.

## Steps

### 1. Find the canonical home of the rule

The rule lives in one of:
- A system doc at `parker-v2/[topic]-system.md` or similar
- The open-loops reasoning doc at `global/knowledge/creative-strategy/creative-strategy-fundamentals.md`
- A methodology doc at `parker-v2/[topic]-method.md`

If the rule exists in multiple places, the one that gets loaded at runtime alongside prompts is the canonical home. The others are derived.

If you can't tell which is canonical, ask before editing. Editing the wrong one is silent drift.

### 2. Diagnose the loophole

Before writing the new wording, name explicitly what the old wording permitted. The loophole is what the model was using to produce the bad output. The new rule has to close it.

Common loophole patterns:
- A permissive clause ("you may also...") that gives the model an escape hatch
- An ambiguous boundary ("tightly related" with no definition)
- A rule that names what to do without naming what NOT to do
- A rule that has the right idea but no diagnostic for "you're doing it wrong"

### 3. Write the new wording

Three components for a tight rule:
- **The rule itself** — stated affirmatively in one sentence.
- **The diagnosis** — name the failure mode the rule prevents, so the model can recognize when it's drifting. "The sub-question list is the tell."
- **The narrow exception, if any** — defined precisely so it can't be used as the old loophole.

A rule without a diagnosis is a rule the model will drift past. The diagnosis is what makes the rule self-correcting.

### 4. Update dependent training corpus

The rule lives in two places: the canonical doc that runs at runtime, and the training corpus that derived it. Both need to agree.

For rules that derive from the senior-strategist open-loops reasoning, update `global/knowledge/creative-strategy/creative-strategy-fundamentals.md` (or the verdict template in `prompts/open-loops/open-loops-roll-up.md` if it is a grading rule).

### 5. Check if the prompt reference paragraphs need updating

The prompts reference the canonical doc by name (e.g., "run every candidate through the verdict template in `system/open-loops-system.md`"). If the canonical doc was updated and the reference paragraph still invokes the right behavior, no prompt edits are needed — inheritance handles it.

If the canonical change introduced a new named step that the prompts need to invoke explicitly, update each prompt's reference paragraph to name the new step. Do this consistently across all affected prompts.

### 6. Flag brand-output impact

Existing brand outputs were generated under the old rule. List which ones are affected. Common cases for an open-loops rule change:
- The consolidated rubric-applied roll-up needs to be re-scored
- Per-sub-context-doc open-loops sections need to be re-run
- The persona profile may have open-loops that need re-evaluation

State the impact explicitly in the diff summary. Don't silently leave production state stale.

### 7. Output the diff summary

Tell the user:
- What changed at the canonical layer (the new wording)
- Why (the loophole closed, with the failure-mode named)
- Whether prompts needed reference-paragraph updates (and which ones)
- Whether training-corpus updates landed (and where)
- Which brand outputs need re-running (and which can wait)

## Anti-patterns specific to tighten-rule

**Editing the rule in the prompt instead of the canonical doc.** When a prompt has its own version of a rule that drifts from the canonical, editing the prompt makes the drift permanent. Always edit canonical first; prompt reference paragraphs are derived.

**Tightening without naming the failure mode.** A rule that says "don't write four sub-questions" without naming the failure mode ("the sub-question list is the tell that the strategic question hasn't been found") doesn't give the model a diagnostic. The model will drift past.

**Tightening without an example.** A rule that says "do X" without showing what X looks like leaves the model to interpret. Pair with a worked example from the training corpus.

**Forgetting the brand-output impact.** A rule change with no brand-output flag means the existing roll-ups, sub-context docs, and persona profiles silently violate the new rule. Always flag.

**Adding the rule to one prompt instead of propagating.** If the rule lives in the canonical doc, inheritance via reference handles propagation. If the rule lives in each prompt's reference paragraph, propagate to all. Never add it to one and leave the others.
