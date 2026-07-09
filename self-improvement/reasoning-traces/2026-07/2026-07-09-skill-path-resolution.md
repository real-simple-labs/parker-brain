---
doc: reasoning-trace
title: "Day-one creative-skill audit: the gates and strategy baking were built right; the doc paths were the break"
status: executed 2026-07-09 on the skill-path-resolution branch
date: 2026-07-09
---

# Day-one creative-skill audit and the path-resolution fix

Jimmy asked for a day-one audit: a brand clones the repo, builds the brain, and its very first prompt is "write me a script" — does everything generated come out baked in strategy, and does the review layer make it human and strip the AI-isms?

## What the audit confirmed (no changes needed)

- All five creative skills (scriptwriting, hooks, headlines, iterations, ai-ad-generation) load the committed strategy and idea bank first, surface conflicts instead of silently executing, and degrade honestly when `strategy/` doesn't exist yet.
- Both ship gates (context-grounding-review, then creative-voice-review) run automatically in all five, with agent-returned verdict blocks as the output contract. "Asking whether to review is itself the failure."
- The shipped `settings.json` hook enforces "creative deliverables have no casual path" on every user prompt, so a plain-chat ask still routes through the skill.
- The deterministic layer works: voice-lint.py (smoke-tested, caught negative parallelism and rhetorical self-question instantly), grounding-check.py, and the pull-log hook that gives the grounding agent an unfakeable record of MCP pulls.
- The onboarding runner ships the whole gate bundle and verifies it by name, including test-running both checkers inside the new brain.

## The break

The skills' method-doc references did not resolve in a shipped brain. Three shapes coexisted: `global/knowledge/creative-strategy/...` (factory-only), bare `creative-strategy-context/...` (legacy-flat-only, and broken in the factory too), and unprefixed `system/<doc>.md`. In the current nested brain layout (`parker-system/creative-strategy-context/`), all three pointed at nothing. Nothing rewrote them: propagate normalized only `system/` docs and `CLAUDE.md`, and the runner claimed skill paths "resolve the same in the factory and the brain" — false, and contradicted by the runner's own Phase-0 check. The only mitigation was the model globbing around failed reads: instruction-luck, not structure. The two reviewer agents had solved this correctly (doc names + explicit glob-across-layouts rule); the skills had not.

## The fix (structural, three layers)

1. **Canonical:** all five creative skills standardized on factory paths (15 files fixed, including the strays broken in the factory itself), plus a "Path resolution" convention paragraph in each SKILL.md: paths are the factory's, ship-time normalization rewrites them, and a failed path means glob for the doc by filename — a missing read is never the fallback.
2. **Deterministic:** new `scripts/normalize-brain-paths.py` (layout-aware, placeholder-protected, idempotent; verified on simulated nested and flat brains — 35/36 files rewritten, zero residuals, zero double-prefixes, second run rewrites nothing). Propagate runs it in both layout branches and ships it into each brain's `scripts/`.
3. **Runner truth-fix:** the false "straight copy is all it takes" sentence replaced with the explicit normalization step; the Phase-0 verification now names the exact grep that must return nothing and the recovery command.

## The durable lesson

A reference that resolves in the authoring environment is not a reference that resolves in the shipped environment. When files ship into a different layout, path correctness must be produced by a deterministic ship-time step and verified by a mechanical check — never assumed from "a straight copy is all it takes," and never left to the model's ability to glob around a miss. The reviewer agents' name-plus-glob convention is the right authoring pattern for anything that must run in multiple layouts.
