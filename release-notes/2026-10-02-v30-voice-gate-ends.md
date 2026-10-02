# v30 — the voice gate always ends (2026-10-02)

The five creative skills re-ran the `creative-voice-review` gate "until the verdict is `ships`," but one of the reviewer's findings can't be fixed by rewriting: copy that is clean but generic because the brand's voice corpus is thin or missing. On a new or unbuilt brain that kept the gate `flagged` forever. Separately, a few skills that run inside a brain still named the factory's old `z-brands/[brand]/` paths.

## What shipped

- **A third verdict, `needs-corpus`.** The reviewer returns it only when its rewrites leave no line-level flag but the copy still sounds like no one, and only after checking the brain for voice material it wasn't handed. It ends the gate: the skill ships the lines with the reviewer's note naming the corpus that would fix it, and adds that gap to `running-notes/missing-context.md` unless it's already listed. Fixable flags always mean `flagged`, so it can't become a shortcut.
- **Every rewrite lands, and protected lines don't block.** The skill applies the reviewer's rewrites whatever the verdict, since `ships` and `needs-corpus` describe the draft with them applied. A line the reviewer must leave alone (a sourced quote, a claim) goes under CONFLICTS and doesn't count against `ships` or `needs-corpus`.
- **Three passes at most.** The skill hands the reviewer its last return on each re-run; the reviewer checks its own rewrites landed and reads the whole draft aloud again, without re-flagging lines it already fixed. If the third pass is still `flagged`, the skill stops and ships with the open flags shown as unresolved, never as passed.
- **Where:** `.claude/agents/creative-voice-review.md` (the canonical verdicts); the gate step, hard rule, and Voice Review receipt in `scriptwriting`, `hooks`, `headlines`, `iterations`, and `ai-ad-generation`; one sentence in `creative-strategy-context/ai-writing-tells.md`; the agent's entry in `system/parker-system-map.md`.
- **`z-brands/[brand]/` means the brain's root.** One sentence in the factory `CLAUDE.md`, which every brain carries at `parker-system/CLAUDE.md`, says so and points at the runner's path map for the few paths that differ. The brain's `AGENTS.md` carries the same sentence for Codex, which never loads the factory's `CLAUDE.md`. `brand-idea-bank-maintenance`, `expert-signal-intake`, and `improve-system` now name the brain's own paths (`idea-bank/entries/`, `sub-context-docs/brand-profile-narrative.md`, `sub-context-docs/operations-and-team.md`), and `improve-system` and `self-improvement-intake` read the self-improvement method at `parker-system/self-improvement/`, where a brain keeps it, instead of the brain's own `self-improvement/` traces folder. `expert-signal-intake` names the cross-brand idea bank where it really lives, in the factory, read-only from a brain.
- **Tests run the same in a cloud session.** `tests/test_runtime_hooks.py` gains a `local_env()` helper that drops the two cloud-run signals (`CLAUDE_CODE_REMOTE`, `PARKER_CLOUD_RUN`), and every direct hook call in it and in `tests/test_scaffold_brain.py` uses it. Before, `test_git_guard_retains_both_envelopes` failed whenever the suite ran inside a Claude Code cloud session, because the git guard steps aside in a cloud run (v24) and that call passed the session's variables through.

## For the other Parker repos

Nothing.

## Migration

`migrations/v30.md`: nothing to do. Everything here is a copied skill or agent, which the pin bump's re-sync delivers, or a doc read from the mount.
