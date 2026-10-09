# v35 — the recreate skill (2026-10-09)

The Parker app's Recreate button drifted. It started as a faithful recreation of one ad in the brand's voice, and a later version turned it into "three new concepts," which is a different job. The team agreed to make one `/recreate` skill the single source of truth, so the app and Claude run the same thing. It was built and tested in an internal brain first, on one competitor static and one competitor video, and both came back as faithful recreations.

## What shipped

- **`.claude/skills/recreate/SKILL.md`.** Recreates one ad (a competitor or inspiration ad, a swipe-file save, a TikTok, or one of the brand's own ads) as close to the original as the brand allows. It gets the real ad first, never from memory: the Parker ad record, competitor ads, the swipe file, TikTok, a pasted video URL, or a pasted image. It decides once whether the ad is a video or a static (a carousel runs the static method card by card; a video that's one still frame with text counts as static) and runs exactly one method, never both: `creative-strategy-context/adapting-scripts.md` for video, `creative-strategy-context/static-ad-recreation.md` for a static. It carries the original v1 Recreate prompt verbatim. With a brain it loads that brain's brand lens, brand identity analysis, brand rules, and customer language, and never another brand's; without one it works from Parker's brand profile plus live review and ad-comment pulls, and says so. No invented stats (`[STAT NEEDED — verify before publishing]`), compliance substitutions flagged, the original ad link at the top, and it stops after the recreation unless asked for variations.
- **Index docs** name the new skill: `README.md`, `system/parker-system-map.md` (skill library and update log), `system/master-file-structure.md`, `prompts/onboarding-runner.md` (Phase 0's list of what ships), `creative-strategy-context/expertise-routing.md` (next to the two method docs), the brand `CLAUDE.md` template, and the routine bundle README.

## How it reaches brains

The bundle map in `scripts/sync-executable-layer.py` already copies every folder under `.claude/skills/`, so new brains get the skill from the scaffold and standing brains get it from `/update-brain` on the pin bump. The two method docs it reads are already in the mount at `parker-system/creative-strategy-context/`. The brand `CLAUDE.md` template now names `recreate` among the craft skills; that file is a seed, so only new brains get the new wording. Standing brains don't need it: the skill registers and triggers from its own description.

## No review gates, on purpose

Unlike `scriptwriting`, `headlines`, `hooks`, `ai-ad-generation`, and `iterations`, `recreate` doesn't spawn the `context-grounding-review` and `creative-voice-review` ship gates. That's a deliberate call, not a gap: a recreation's job is to stay as close to the original as the brand allows, and a rewrite pass pulls the lines away from it. The skill says so, and runs `creative-voice-review` when the user asks for it after seeing the recreation.

## Screenshots and carousels

A screenshot has no link, so the output says "No link given" instead of stopping or inventing one. Parker pulls everything out of the screenshot and asks the user what to make from it, offering a static first since that's the usual answer. A carousel runs through the static method card by card: every card captured in order, then each one recreated with the same count, order, copy mechanics, and layout.

## Migration

`migrations/v35.md`: no-op. The skill ships through the bundle.
