# AGENTS.md

See `CLAUDE.md` for the full Parker product-brain operating contract, repo rules, and prompt/skill/knowledge standards. That file is the source of truth for how to work in this repository.

## Cursor Cloud specific instructions

This is a documentation / prompt / skill "product brain" repo, not a conventional application:

- **No dependencies, no build.** There is no `package.json`, `requirements.txt`, or lockfile. The content is markdown. The only executable code is `scripts/*.py` (pure Python 3 standard library — no `pip install` needed) plus `scripts/propagate-to-brand-brains.sh` (bash). System `python3` (3.12) is all that's required.
- **No automated test suite.** `evals/` is an empty placeholder. The scripts' `--check` modes are the closest thing to lint/tests.

Runnable tooling (all from the repo root):

- `python3 scripts/sync-open-loops-core.py --check` — drift lint: verifies the marker-delimited shared blocks embedded across prompts/templates still match their source files. Exit 1 on drift. Run (without `--check`) to fix drift.
- `python3 scripts/build-doc-map.py` — regenerates the creative-strategy doc catalog inside `global/knowledge/creative-strategy/expertise-routing.md`. Must be run after adding/editing any doc in `global/knowledge/creative-strategy/`. The region between the `DOC-MAP` markers is generated — never hand-edit it. Idempotent when the catalog is already in sync.
- `python3 scripts/voice-lint.py DRAFT_FILE` — deterministic AI-writing-tell scan. Runs against creative *deliverable* drafts (scripts, hooks, headlines, copy), never against repo context/prompt/system docs. Exit 1 when flags are found.
- `python3 scripts/grounding-check.py OUTPUT_FILE [BRAIN_ROOT]` — traces quoted verbatims and cited file paths in a creative/strategy output against the brain on disk. `BRAIN_ROOT` defaults to the current directory. Exit 1 on findings.
- `scripts/propagate-to-brand-brains.sh [brand-repo ...]` — re-ships the factory bundle into standing brand-brain repos. Needs target repo paths (args or `PARKER_BRAND_BRAIN_REPOS`); it is not runnable standalone in this repo and writes to *external* brand repos, so do not run it as a self-test here.

Note: `.claude/skills/` and `.claude/agents/` are loaded by Claude Code at runtime; the `.claude/hooks/` referenced by some docs ship only with the brand-routines template (`templates/brand-routines/`), not with this factory repo.
