# v29 — the voice gate always ends (2026-10-01)

The five creative skills re-ran the `creative-voice-review` gate "until the verdict is `ships`," but one of the reviewer's findings can't be fixed by rewriting: copy that is clean but generic because the brand's voice corpus is thin or missing. On a new or unbuilt brain that kept the gate `flagged` forever. Separately, a few skills that run inside a brain still named the factory's old `z-brands/[brand]/` paths.

## What shipped

- **A third verdict, `needs-corpus`.** The reviewer returns it only when its rewrites leave no line-level flag but the copy still sounds like no one. It ends the gate: the skill ships the lines, says so in the Voice Review block with the corpus that would fix it, and adds a line to `running-notes/missing-context.md`. Fixable flags always mean `flagged`, so it can't become a shortcut.
- **Three passes at most.** The skill hands the reviewer its last return on each re-run, and the reviewer verifies its own rewrites instead of starting over. If the third pass is still `flagged`, the skill stops and ships with the open flags shown as unresolved, never as passed.
- **Where:** `.claude/agents/creative-voice-review.md` (the canonical verdicts); the gate step, hard rule, and Voice Review receipt in `scriptwriting`, `hooks`, `headlines`, `iterations`, and `ai-ad-generation`; one sentence in `creative-strategy-context/ai-writing-tells.md`; the agent's entry in `system/parker-system-map.md`.
- **`z-brands/[brand]/` means the brain's root.** One sentence in the factory `CLAUDE.md`, which every brain carries at `parker-system/CLAUDE.md`, says so and points at the runner's path map for the few paths that differ. `brand-idea-bank-maintenance`, `expert-signal-intake`, and `improve-system` now name the brain's own paths (`idea-bank/entries/`, `sub-context-docs/brand-profile-narrative.md`, `sub-context-docs/operations-and-team.md`), and `improve-system` and `self-improvement-intake` read the self-improvement method at `parker-system/self-improvement/`, where a brain keeps it, instead of the brain's own `self-improvement/` traces folder.
- **Tests run the same in a cloud session.** `tests/test_runtime_hooks.py` gains a `local_env()` helper that drops the two cloud-run signals (`CLAUDE_CODE_REMOTE`, `PARKER_CLOUD_RUN`), and every direct hook call in it and in `tests/test_scaffold_brain.py` uses it. Before, `test_git_guard_retains_both_envelopes` failed whenever the suite ran inside a Claude Code cloud session, because the git guard steps aside in a cloud run (v24) and that call passed the session's variables through.

## For the other Parker repos

Nothing.

## Migration

`migrations/v29.md`: nothing to do. Everything here is a copied skill or agent, which the pin bump's re-sync delivers, or a doc read from the mount.
