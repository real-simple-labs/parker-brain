# v46 — installed packages and build output stay out of the brain (2026-11-03)

An agent that builds a code project inside a brain can save the whole project with it. In one brain, agent sessions saved 3,823 `node_modules` files and about 1,000 source maps, and the brain grew past what Parker Desktop lists in full. None of those files is knowledge, and the project's install or build command makes them again.

## What shipped

- **`templates/brand-scaffold/gitignore`:** a second group of rules under its own comment: `node_modules/`, `.next/`, `.nuxt/`, `.vercel/`, `.parcel-cache/`, `.venv/`, `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, and the source maps `*.js.map`, `*.mjs.map`, `*.cjs.map`, `*.jsx.map`, `*.ts.map`, `*.css.map`. It is the same list Parker Desktop is to write into each brain's `.git/info/exclude` ([parker-desktop#615](https://github.com/real-simple-labs/parker-desktop/pull/615)). The exclude file covers a computer with the app; the `.gitignore` also covers cloud runs and every other clone.
- **Not on the list, on purpose:** raw data, run output and logs (`*.log`), `.mastra/`, `.netlify/`, `.turbo/` and loose `*.pyc` files. Teams keep raw dumps on purpose, and each of the others can hold data nothing makes again. When Parker Desktop takes a folder off a computer, ignored files go without a backup, so the list holds only what a command builds again.
- **`scripts/scaffold-brain.py`:** when the scaffold meets a `.gitignore` the folder had already, it adds each missing group under its own comment (before, every comment went above all the missing rules). `tests/test_scaffold_brain.py` checks the manifest and the merge.
- **`system/brain-sync.md`, `system/brain-scaffold.md`, `system/master-file-structure.md`:** the `.gitignore` notes follow.

Left as it is: no rule in the brand `CLAUDE.md` and no new check in the guard hook. The ignore rules do the job for every agent; a file the brain holds already stays saved.

## Migration

`migrations/v46.md` (auto-apply): adds the rules the brain's `.gitignore` lacks, under the same comment, and verifies with `git check-ignore`. It never removes a line and never takes a file out of git.
