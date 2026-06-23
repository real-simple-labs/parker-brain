# System of records

> Status: `[~]` created 2026-06-11. The registry of every single source of truth in the Parker prompt system, what propagates from it, where, and how. The `/system-of-records` skill audits reality against this doc. When a new source of truth or a new propagation target is added, record it here in the same pass, or the audit goes blind to it.

The principle: every rule, concept, block, and method has exactly one home. Everything else either carries a synced copy of it or references it by path. Drift is any place where a copy has fallen out of step with its source, a reference points at nothing, or the same idea is stated two different ways in two places.

## The trees

Four trees hold prompts and canon. They are not independent; three of them are downstream of the first.

- **`parker-v2/`** is the canon and the lab. Every source of truth lives here. This is where edits happen.
- **`liquid-iv-brand-brain/parker-system/`**, **`nutrafol-brand-brain/parker-system/`**, **`the-perfect-jean-brand-brain/parker-system/`** are per-brand snapshots of the canon, shipped inside each vault so the brand brain is self-contained and portable. They should match `parker-v2/` for every shared file.
- **`parker-brain/`** is the product layer, the clean canonical repo. It mirrors `parker-v2/` canon but uses a different layout: method docs live under `global/knowledge/creative-strategy/` rather than `creative-strategy-context/`, and it omits brand-private material. Shared files should match content even though the path differs.

## Synced blocks (one source, many embeds, marker-enforced)

These are kept in step by `scripts/sync-open-loops-core.py`. Each has a source file and a marker pair; the text between the markers in every target must be byte-identical to the source. Run the script to push changes; run it with `--check` to detect drift without writing.

- **Open-loops core** — source `prompts/_open-loops-core-block.md`, markers `open-loops-core:start`/`end`, embedded in every context-doc-generating prompt across all four prompt trees.
- **Expertise core** — source `prompts/_expertise-core-block.md`, markers `expertise-core:start`/`end`, embedded in the same prompts.
- **Parker voice** — source `prompts/_parker-voice-block.md`, markers `parker-voice:start`/`end`, embedded in the four brand-brain `CLAUDE.md` files (the template plus the three brands). A brand brain's root `CLAUDE.md` sits outside `parker-system/` and is never rsynced, so `scripts/propagate-to-brand-brains.sh` runs `sync-open-loops-core.py --scan <brain>` after it mirrors the bundle, refreshing this block in each brain from factory canon.

## Hand-propagated canon (one source, copied, no marker)

These live in `parker-v2/` and are copied into the three vault `parker-system/` trees and into `parker-brain/` when they change. They have no marker enforcement, so they are the highest-drift surface and the audit checks them by content comparison.

- **The reasoning and method layer** — `global/knowledge/creative-strategy/` (the method docs, `expertise-routing.md`, `spoken-script-voice.md`, `visual-vocabulary-method.md`, and the brand lens overlays). In `parker-brain` these live under `global/knowledge/creative-strategy/`.
- **The system layer** — `system/` (`open-loops-system.md`, `parker-system-map.md`, `master-file-structure.md`, `master-prompt-review.md`, `attribution-principle.md`, `three-phase-operating-model.md`, and this doc).
- **The open-loops generation rubric** — `prompts/_open-loops-core-block.md`, synced into every context-doc prompt; the deeper reasoning is `global/knowledge/creative-strategy/creative-strategy-fundamentals.md`, loaded via expertise-routing.
- **The generator prompts** — everything under `prompts/`.
- **The skills** — `skills/`.
- **The templates** — `templates/` (the brand-brain CLAUDE template, the missing-context template, the persona and VoC templates).

## Reference sources (one source, pointed at, never copied inline)

Each of these is the single place a concept is defined. A prompt may reference it by path but must never re-define it inline with different words, because two definitions are two sources of truth.

- **The four territories and the six pulls** — defined in `system/open-loops-system.md` and carried operationally in the open-loops core block. Nowhere else defines them.
- **The two-stage open-loops model** (generation captures, grading decides) — `open-loops-system.md`, `_open-loops-core-block.md` (generation), and `prompts/open-loops/open-loops-roll-up.md` (grading).
- **Which method docs load per task** — `creative-strategy-context/expertise-routing.md`.
- **The three-phase operating model and the co-pilot principle** — `system/three-phase-operating-model.md`, with the runtime version in the synced voice block.
- **The prompt rubric and the locked structure** — `system/master-prompt-review.md`.
- **The canonical file tree** — `system/master-file-structure.md` and `system/parker-system-map.md`.
- **The claim marks** (stated, inferred, verified) — `system/attribution-principle.md`.

## What the audit checks

1. **Block drift.** `scripts/sync-open-loops-core.py --check` returns clean. Every synced block matches its source in every target.
2. **Tree parity.** Each shared file in the three vault `parker-system/` trees and in `parker-brain/` matches the `parker-v2/` source (accounting for parker-brain's path remap). Flag any file that diverged or is missing.
3. **Reference integrity.** Every file path a prompt or doc references resolves to a real file in that tree. Renamed or moved targets leave dead references; those are drift.
4. **Concept consistency.** The reference-source concepts above are described the same way everywhere and never re-defined divergently inline. No prompt contradicts the operating model, the territory definitions, or the marks.
5. **Hard-rule conformance.** No em dashes and no parenthetical example lists in prompts, per Jimmy's standing rules. Generating prompts carry both required synced blocks.
6. **Registry currency.** Every source of truth and propagation target described here still exists, and nothing new has appeared that this registry does not list.
