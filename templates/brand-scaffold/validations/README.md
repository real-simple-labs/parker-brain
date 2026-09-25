# Validations

The verdicts. When a hypothesis gets tested, the result lands here in one of four states, and the finding flows back into the standing docs it touches.

## What lives here

- `validated/[YYYY-MM]/[loop-slug].md`: the evidence says yes.
- `invalidated/[YYYY-MM]/[loop-slug].md`: the evidence says no. That's a known dead end, which is worth having.
- `inconclusive/[YYYY-MM]/[loop-slug].md`: strong evidence both ways, or the question turned out bigger than the test.
- `insufficient-evidence/[YYYY-MM]/[loop-slug].md`: not enough data to call it either way.

Each closure doc leads with the finding and its state. The method is in `parker-system/system/open-loops-system.md` and `.claude/skills/open-loops-validate/`. A validated finding that can decay gets a re-check scheduled in `../re-validations/`.

A new brain starts with this folder empty.
