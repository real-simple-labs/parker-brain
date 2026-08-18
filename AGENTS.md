# AGENTS.md

See `CLAUDE.md` for the full Parker product-brain operating contract, repo rules, and prompt/skill/knowledge standards. That file is the source of truth for how to work in this repository — read it in full; everything in it applies to you word for word.

## OpenAI Codex specific instructions

- **Voice:** there is no output-style layer here, so read `.claude/output-styles/parker.md` and speak that way from your first message — plain, warm, tenth-grade English, never a terminal printing a report.
- **Skills** load from `.agents/skills/`, a committed symlink to `.claude/skills/` — same SKILL.md files both harnesses read. Where the docs say `.claude/skills/`, that is your `.agents/skills/`.
- This factory repo carries no hooks of its own; the brand-brain hook bundle (and its Codex wiring) lives under `templates/brand-routines/`. The full Codex support contract is `system/codex-support.md` — read it before changing anything harness-facing.

## Cursor Cloud specific instructions

This is a documentation / prompt / skill "product brain" repo, not a conventional application:

- **No dependencies, no build.** There is no `package.json`, `requirements.txt`, or lockfile. The content is markdown. The only executable code is `scripts/*.py` (pure Python 3 standard library — no `pip install` needed) plus `scripts/propagate-to-brand-brains.sh` (bash). System `python3` (3.12) is all that's required.
- **No automated test suite.** `evals/` is an empty placeholder. The scripts' `--check` modes are the closest thing to lint/tests.

