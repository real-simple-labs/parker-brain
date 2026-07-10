# AGENTS.md

See `CLAUDE.md` for the full Parker product-brain operating contract, repo rules, and prompt/skill/knowledge standards. That file is the source of truth for how to work in this repository.

## Cursor Cloud specific instructions

This is a documentation / prompt / skill "product brain" repo, not a conventional application:

- **No dependencies, no build.** There is no `package.json`, `requirements.txt`, or lockfile. The content is markdown. The only executable code is `scripts/*.py` (pure Python 3 standard library — no `pip install` needed) plus `scripts/propagate-to-brand-brains.sh` (bash). System `python3` (3.12) is all that's required.
- **No automated test suite.** `evals/` is an empty placeholder. The scripts' `--check` modes are the closest thing to lint/tests.

