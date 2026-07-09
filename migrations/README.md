# Migrations — how structural changes reach standing brains

A brand brain pins this factory at a release tag (`v1`, `v2`, …) via its `parker-system/` submodule. Moving the pin delivers new *method* automatically — but a change that reshapes the **brand repo itself** (a renamed path, a relocated file, a new standing surface, a new hook) doesn't arrive by pulling the mount. Migrations are how those changes travel.

## The contract

- **One file per release that needs one:** `migrations/vN.md`, named exactly after the tag it belongs to. A release with no structural changes ships no migration file — absence means "just move the pin."
- **Plain markdown, written for the agent running it.** A migration is a set of imperative, checkable instructions addressed to the Claude instance updating a brand brain: what to move, create, re-run, or edit *in the brand repo*, in what order, and how to verify it landed. Assume the brain being migrated was built at the previous release; state it explicitly when a step only applies to older layouts.
- **Idempotent and honest:** every step should be safe to re-run (check before acting: "if the file is already at the new path, skip") and must never touch brand data except in ways the instructions name. Steps that modify brand-authored content are shown to the team before applying, per `/update-brain`'s offer rules.
- **Applied in order by `/update-brain`:** when a brain accepts a pin bump from `vA` to `vB`, every `vN.md` with A < N ≤ B runs, in ascending order. The brain's `running-notes/standard-sync.md` records the highest migration applied.

## The maintainer rule

Any factory change that alters the brand-brain layout, renames or moves a path a brain references, adds a standing file brains should carry, or changes the committed `.claude/` bundle **must ship its migration in the same PR**, plus a `release-notes/` entry. `/update-parker-skill` carries this as a checklist item. Cutting a release (`git tag vN`) is manual and deliberate; the tag is what makes the accumulated changes — and their migration — visible to standing brains.
