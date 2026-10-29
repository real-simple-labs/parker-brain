# v45 — the build runs as one agent and reads the data once (2026-10-29)

A brain build ran each of its prompts in its own helper agent, and checked each output with another one. Every helper started empty, so it read the method again and pulled the brand's data again: one build made about a thousand Parker calls and read the same ads, reviews, comments, and competitor libraries many times over. The person pays for all of it out of their own Claude or Codex plan, and on a lighter plan the plan ran out long before the brain was built.

The first setup still builds every document and every audit. What changed is how.

## What shipped

- **One agent, no helper agents.** In `prompts/onboarding-runner.md`, "One agent, one prompt at a time" replaces the delegation contract: the build session runs every prompt itself, one at a time, branch by branch. The fidelity rule stays: every prompt is opened and read in full from its file before it runs, never from memory of a sibling or a summary. Each output is saved the moment it is done. After a compaction the build re-reads `BUILD-STATUS.md` and the next prompt's file; at a usage limit it stops cleanly, writes where it stopped, and resumes from there.
- **The data is pulled once.** New "Pull the data once" and Phase 0 step 8: the build pulls the brand's shared data into `build-data/`, with an `INDEX.md`: the brand's own ads (compact rows by window, breakdowns, the hook history, one file per ad for the ads the docs describe), the customer-language corpus (reviews, survey responses, ad comments), organic and TikTok, Reddit and forums, web pages, and each rival's library. Ad tools are asked for compact rows, with the heavy analysis only for the ads a doc describes. The folder carries its own `.gitignore` (`*`), so it never syncs; closeout deletes it.
- **Every prompt reads from it.** The expertise block (synced into 73 prompts) and the team-conversations block (16) now say: during a build, read `build-data/` first, pull only what it lacks and save that back for the next prompt, and treat a pull from earlier in the build as the fresh pull (a slice more than 7 days old gets pulled again). `voc-corpus-profile`, `brand-idea-bank`, and `gaps-opportunities-inspo` carry no expertise block and got the same rule in their source sections. Only the build's own steps read the folder: a refresh, a routine, or an on-demand run pulls live as before, even while a build is paused.
- **No check agent.** The per-prompt review and the build-completion review are passes the same agent runs itself, against the same checklists. A failed check gets one fix pass; a doc that still falls short is marked blocked and raised at the next phase boundary.
- **The rest follows the runner.** `/set-up-brain`, `prompts/README.md`, the factory `CLAUDE.md`, and `system/usage-logging.md` (a one-agent build is labeled as a whole, with the stage `coordinator`) describe the new build.

## Migration

`migrations/v45.md`: nothing to do. A new build moves the pin to the newest release before it starts, so it gets this runner. A build already underway keeps the runner of its pin: automatic updates wait while a `BUILD-STATUS.md` sits at the root.
