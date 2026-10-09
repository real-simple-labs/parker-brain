# v37 — Windows line endings and paths; recreate skill fixes (2026-10-09)

The Runtime checks job on `windows-latest` has failed on every push to `main` since at least v34, while Ubuntu and macOS passed. Four tests failed, for three reasons: CRLF line endings in the Windows checkout, backslash paths in a hook's text, and a lock-file read that Windows refuses.

## What shipped

- **`.gitattributes`: `* text=auto eol=lf`.** Git for Windows checks text files out with CRLF by default (`core.autocrlf=true`), and GitHub's Windows runners do too. Two tests copy working-tree files into a fixture repo and compare bytes against git's copies. The scaffold test's fixture factory got `---\r` lines, so `scripts/scaffold-brain.py` stopped in `setUpClass` with "expected a `---` line closing the template header". The release-sync test expected CRLF for `schedules/ideas-weekly.md` and got the LF the sync writes. Every checkout now gets LF, Windows included. The one file committed with CRLF, `fixtures/creative-tracker-example.csv`, keeps it: `text=auto` leaves a file alone when git already holds it with CRLF.
- **`craft-context` hook prints forward-slash paths.** On Windows it told the model to read `users\fixture\user-profile.md` and said the catalog's paths were relative to `parker-system\creative-strategy-context/`. The model reads these, the rest of the hook's text uses forward slashes, and forward slashes work on every OS, so the profile path, the catalog folder, and the fallback catalog path now print that way. `tests/test_runtime_hooks.py` checks all three.
- **`scripts/usage-log.py` no longer reads the locked byte.** Before taking its lock, the collector read the first byte of `.usage/.local/lock` to see whether the file was empty. Windows locks are mandatory, so when another collector held the lock, that read failed with `PermissionError`, and the hook printed `usage-log: unavailable (PermissionError)` and skipped that collection. It checks the file's size instead. This only bit with `usage_logging` on, on Windows, with two hooks firing at once (a subagent's Stop next to the main session's, for one). The cleanup error the same test sometimes showed ("The directory is not empty") followed from it: the test stopped on the first collector while the other five were still writing.

## Real Windows brains

The scaffold failure was test-only. `scaffold-brain.py` reads the factory from git objects at `parker-system/`'s HEAD (`ls-tree`, `cat-file`), which hold LF whatever `core.autocrlf` says, so a Windows user's scaffold never saw a `---\r` line. `sync-executable-layer.py` reads the mount the same way. The hook's paths and the lock fix do reach Windows users.

## Recreate skill fixes

A review of the v35 `recreate` skill found three gaps.

- **The hook and the skill gave opposite rules.** The `craft-context` hook tells the model on every message that any words a customer will read or hear ship with both gate receipts (Grounding Review, Voice Review). `recreate` skips those gates on purpose, so a recreation stays close to the original ad. With both rules in front of it, the model could run the gates anyway and pull the lines away from the original, or call its own recreation a skipped gate. The hook now names `recreate` as the one exception. The ship-gates rule in `update-parker-skill` says the same, so a later edit doesn't wire the gates back in.
- **Three lookups came back without the script.** `search_competitor_facebook_ads` returns no script or storyboard unless the call sets `includeAdDetails: true`, `search_tiktok_videos` returns no script without `with_video_report: true`, and a swipe-file search returns only a compact analysis until `mode: "get_analysis"` fetches the transcript and storyboard. The skill needs the transcript and a shot-by-shot view for a video, so each lookup line now says how to get them.
- **The brand-context and closing-line steps were vague.** "Both methods refuse to run without brand context" is true only for `static-ad-recreation.md`; the line now says what each method needs. Step 5's "the method's closing line" now gives the sentence each method's RULE line asks for, word for word, so the model doesn't have to find it at the top of the doc or invent one.

## Migration

`migrations/v37.md`: no-op. The hook, the `recreate` skill, and `usage-log.py` are bundle copies the pin bump's re-sync refreshes, and `.gitattributes` lives in the mount. A Windows brain's `parker-system/` checkout gets LF file by file as files change on later pin bumps. Nothing needs a fresh checkout: the brain's hooks and checkers read those files as text, and the scaffold and the sync read git's copies.
