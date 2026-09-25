# v23 — the brain scaffold (2026-09-25)

Setting up a new brand brain used to be the model's job: create the folders, copy 162 method files out of the mount, stamp the templates, make the Codex symlink, write the config. None of it needs judgment, all of it cost tokens and time, and it went wrong in ways the build verification had to catch. Now a plain script does it in seconds, and the same scaffold ships with every release so Parker's backend can create a brand's repo already set up, with no git on the server.

A scaffolded brain is usable before it's built. Parker works from live pulls and saves what the team tells it into the running notes and the brand lens, and the full build runs whenever they're ready.

## What shipped

- **`scripts/scaffold-brain.py`.** `init` scaffolds the brand folder it runs in (needs the mount attached; never overwrites a file; refuses a built brain). `manifest` writes the scaffold for a release as GitHub tree entries. `push` applies a manifest to a fresh GitHub repo the way the backend will, for testing against a sample repo.
- **Two lists define an empty brain.** The bundle map in `scripts/sync-executable-layer.py` (method files, copied verbatim, re-synced by `/update-brain`) and `SEEDS` in the scaffold script (brand-owned starting files, written once). A file every brain needs belongs in one of them. `CLAUDE.md`, `system/brain-scaffold.md`, `migrations/README.md`, and the `update-parker-skill` ship-list check all say so.
- **The `.scaffolded` marker.** Written by the scaffold, deleted by the build once its verification passes. The runner and `/set-up-brain` route a marked folder as a cold start with setup done; the session-start hook and `/get-started` tell the model and the person the brain isn't built yet; apps read its presence from the root listing as "not built," with no extra API call.
- **The release manifest.** `.github/workflows/release-scaffold.yml` runs the scaffold tests and attaches `brain-scaffold.json` (182 entries, about 950 KB) to every published release. The first one ships with v23.
- **Seeds.** The brand `CLAUDE.md` in a not-built-yet form (brand name filled in; the phase and build-status sections say plainly that nothing is built and how to work until it is), a starter `README.md`, six living-layer folder READMEs (`templates/brand-scaffold/`), the brand lens and running notes with every blank labeled "Not captured yet," and `standard-sync.md` filled with the pinned release.
- **Onboarding runner and `/set-up-brain`.** Phase 0 step 3 attaches the mount and runs the scaffold; step 5 describes what shipped instead of telling the model to copy it. The stamp step fills the seeded files rather than re-creating them. Verification gains a mechanical check (`sync-executable-layer.py --dry-run` must report every copy present and unedited, with `scaffold-brain.py init --restore-copies` as the repair) and ends by deleting the marker. On a folder that's already scaffolded, the pin doesn't move before the build; the script flags it if it did.
- **Method files stay brand-neutral.** The runner no longer swaps the brand name into copied skills and schedules. That swap had no purpose (the files find the brand through `CLAUDE.md`) and it quietly froze every copy it touched, since `/update-brain` treats a changed copy as the team's. `schedules/README.md`'s title drops its `[brand]` placeholder for the same reason.
- **Tests.** `tests/test_scaffold_brain.py` builds a fixture factory from the working tree, scaffolds a brand both ways, and checks they match; that the update sync sees every copy as untouched; that a manifest replayed through git's own index clones into a brain whose mount initializes at the release; that no placeholder leaks; and the push helper's call sequence and fresh-repo refusal.

## For the other Parker repos

- **Web app:** its "is this brain built" check has to treat a `.scaffolded` file at the root as not built. A check that counts files alone calls every scaffolded brain built. This has to ship before the backend starts scaffolding.
- **Backend:** fetch the manifest, fill four placeholders, then create tree, create commit, move the branch on a repo created with `auto_init: true`, and only on a fresh one. Steps and a TypeScript reference are in `system/brain-scaffold.md`.

## Migration

`migrations/v23.md` is a no-op: the bundle re-sync delivers everything.
