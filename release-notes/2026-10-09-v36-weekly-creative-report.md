# v36 — the weekly creative report skill (2026-10-09)

Every agency sends its clients a weekly report, and most of them get built by hand in slides or a spreadsheet. This skill is for the starter pack: one command that pulls the week, reads it like a strategist, and hands back a report that's ready to send to a brand's CMO and team. The look follows the Parker V2 visual direction, and it was tested against the made-up example brand and two real ads from an internal brain, one video and one static, to check the ad links and the video stills.

## What shipped

- **`.claude/skills/weekly-creative-report/SKILL.md`.** The flow: find the brand, run the first-time setup, set the week (last full Monday to Sunday), pull the data through Parker, read it through the own-account methods (`ad-account-analysis.md`, `ad-metrics-glossary.md`, `killer-performance-ads.md`, `andromeda-v2.md`, plus `selecting-ads-to-iterate-on.md` and `iterations.md` for next week's moves), write the report's data file, render it, look at it, save it to `audits/[YYYY-MM]/weekly-creative-report-YYYY-WW.html` and `.json`, and hand it over. It works with or without a brand brain.
- **`render_report.py`.** Turns the data file into one HTML page with inline SVG charts and no scripts, plus a PDF when Chrome, Chromium, or Edge is installed. Standard library only. It warns on anything that would make the report look broken or mislead: a missing "why" line, an ad with no link, a percent left unconverted, a format mix that doesn't add to 100%.
- **`report-schema.md`.** The data file contract and the writing guide for every section.
- **`setup-template.md`.** The shape of the saved setup answers.
- **`fixtures/weekly-creative-report-example.json`.** A full worked example for a fictional brand, every section filled.
- **Index docs** name the new skill: `README.md`, `system/parker-system-map.md` (skill library and update log), `system/master-file-structure.md` (the skill and the new `running-notes/weekly-report-setup.md`), `prompts/onboarding-runner.md`, `creative-strategy-context/expertise-routing.md`, the brand `CLAUDE.md` template, and the routine bundle README.

## What the report holds

The week's verdict in one line and three takeaways; a scorecard led by the brand's north star with week-over-week change, goals, and an 8-week sparkline on each tile; spend and north-star charts for the last 8 weeks; the top creatives with thumbnails, the numbers, and why each one works; new launches and early signals; a watch list where every flagged ad carries an action; where the spend went by format; what we learned; and next week's plan with owners. The byline, results source, and data-through date sit in the footer. There's no notes or sources section on the page. The data file still keeps `sources` and a `basis` line on every insight, so the brain's copy says where each claim came from without printing stated or inferred labels on a client's page.

## Setup, once

The first run reads the brand intake (`brand-rules.md`, `success-definition.md`, the performance targets doc) and asks up to four questions in one popup, each pre-filled: who reads it, what leads it, weekly goals, and whose name goes on it. An agency gets one more: report on only the ads it launched, or the whole account. If it's their own ads, Parker offers the tag it already sees in campaign or ad names first (or a separate ad account, or a start date), tests the rule with one filtered pull, and says what it caught before saving. The filter scopes Parker's totals too, so the report shows the agency's own numbers plus a "Share of account spend" tile. Answers save to `running-notes/weekly-report-setup.md`. For the first three reports Parker asks what to change and saves the answers as standing requests.

## Every ad links to the actual ad

Parker stores each ad's media at a public link (`video_storage_url` or `image_storage_url`) that opens with no login. Every ad name, thumbnail, and table row links there, so a CMO can click through and see or watch the ad. Statics use their own image as the thumbnail. Video ads get a still pulled from the video when `ffmpeg` is installed; without it, the browser shows the video's first frame and the PDF shows a placeholder. The skill never links a client to the Parker dashboard, which needs a login.

## The look

Parker V2, as the design team described it in Slack: a light canvas with soft prism washes, frosted glass panels with 24px corners and no shadows, Fraunces 300 for the title and headline, DM Sans for everything else, and dark glass play buttons over video. The exact V2 color tokens live in the app's design system file, which this repo can't see, so the tints are a close match. Chart colors come from a palette validated for colorblind readers, and the page is light only so it looks the same on every screen and in its PDF.

## One gotcha it handles

The ad tool reports rates as percents (`hook_rate: 33.64` means 33.64%). The data file wants fractions, so the skill says to divide by 100, and the renderer warns when a percent looks unconverted.

## How it reaches brains

The bundle map in `scripts/sync-executable-layer.py` already copies every folder under `.claude/skills/`, so new brains get the skill from the scaffold and standing brains get it from `/update-brain` on the pin bump. The worked example is in the mount at `parker-system/fixtures/`. The setup file is written by the skill on its first run, so it needs no seed. The brand `CLAUDE.md` template now names the skill; that file is a seed, so only new brains get the new wording, and standing brains don't need it because the skill registers and triggers from its own description.

## Still being tuned

This is new. The first few reports should be reviewed before they go out, which the skill says on its first runs.

## Migration

`migrations/v36.md`: no-op. The skill ships through the bundle.
