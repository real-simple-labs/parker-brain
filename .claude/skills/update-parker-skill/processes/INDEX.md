# Update Parker Skill — process index (v1)

The major update types and which process to use. Most v1 processes are sketched here; detailed process files come in v2 as the skill earns its keep.

## The update types

| Type | What it is | Process |
|---|---|---|
| **tighten-rule** | A canonical rule needs to be sharpened, narrowed, or hardened. Example: "one question per loop, almost never more" replacing "list sub-questions too." | [tighten-rule.md](tighten-rule.md) — detailed process below. |
| **add-principle** | A new principle or reasoning move needs to be added to the system. Example: "the re-formulation step at weighting." | Sketch: edit the canonical doc (system / rubric / methodology). Add a worked example. Update the training corpus. Update the dependent prompts' reference paragraphs only if the new principle needs explicit naming at runtime. Flag brand-output re-runs if the principle changes scoring or evaluation. |
| **propagate-pattern** | An existing rule is being applied across more prompts than it currently covers. Example: adding the "load alongside this prompt" pointer to a knowledge doc from N prompts that didn't have it. | Sketch: identify the full set of prompts that should carry the pattern (use `grep -r` for the existing pattern as a template). Edit each consistently. Update the prompt-category README if the propagation changes the surface area of the system. |
| **add-prompt** | A new sub-context-doc prompt or other prompt joins the system. Example: `prompts/brand-profile/ad-account-evaluation.md`. | Sketch: write the prompt following the format of existing siblings (see _foundations.md if it exists for that category). Reference the relevant knowledge doc and `system/open-loops-system.md` in the standard "load alongside this prompt" form. Update the category README. Update any sibling prompt's "where this doc sits" section that lists the full set. |
| **add-knowledge-doc** | A new top-level reference doc joins the system. Example: `creative-strategy-context/public-ad-library-analysis.md`. | Sketch: write the doc at `creative-strategy-context/[topic]-[shape].md` with a one-line `summary` frontmatter (an honest "what this doc is"), run `python3 scripts/build-doc-map.py` to regenerate the catalog in `expertise-routing.md`, and add reference paragraphs to every prompt that should load it at runtime. |
| **add-skill** | A new skill joins the system. Example: this skill. | Sketch: create `skills/[name]/` with `SKILL.md` (frontmatter with name/description/triggers, body with Goal / Why / How / When-not / Anti-patterns), `processes/` directory, `references/` directory. Follow the format of `iterations/SKILL.md` or `ad-account-analysis/SKILL.md`. |
| **fix-prompt** | A specific prompt has a bug, ambiguity, or wrong rule. Example: removing the "list sub-questions too" loophole from prompts' open-loops section. | Sketch: check whether the bug exists in the canonical doc (system / rubric) or only in this prompt. If canonical, edit canonical and propagate. If prompt-only, edit prompt. Check sibling prompts for the same bug pattern. |
| **propagate-change-from-canonical-edit** | The canonical doc has already been edited and now the dependent prompts need to inherit the change. Example: the system doc was updated with a new step; prompt reference paragraphs need to invoke it by name. | Sketch: identify the dependent prompts. Update each prompt's relevant section to name the new step. Don't duplicate the canonical content — reference it. |
| **add-reasoning-move** | A new open-loops reasoning move or senior-strategist prior to capture. | Add it to `creative-strategy-context/creative-strategy-fundamentals.md` in the relevant section (priors, posture moves, or failure modes), in brand-agnostic form. |
| **add-reasoning-extraction** | A new reasoning-layer-notes entry joins the corpus. Example: any of `21-24` from earlier in the build. | Sketch: create `parker-v2/reasoning-layer-notes/NN-[topic]/transcript.md` and `reasoning.md`. Follow the structure of session 20. Update `reasoning-layer-notes/README.md` table. |
| **update-brand-output** | A brand sub-context doc, persona profile, or open-loops roll-up needs to be re-run because a rule changed. | Sketch: load the new rule. Re-run the affected open-loops sections per the current method. Document what changed in the file's frontmatter (`last_updated`, `rubric_applied`, etc.). Update brand README if the output set changes. |

## When the update doesn't match a named type

Use the general process from `SKILL.md`. The skill's body covers the universal moves: identify canonical location, identify dependencies, decide propagation scope, make the change, propagate, update training corpus, update indexes, flag downstream impact, output diff summary.

## When the update is a meta-change to this skill itself

Yes, this happens. Update `SKILL.md`, `processes/INDEX.md`, and any affected process file. No external dependencies to propagate. The skill is self-referential at this layer.
