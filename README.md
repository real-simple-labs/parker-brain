# Parker Brain

`parker-brain` is the clean product intelligence layer for Parker.

It contains the production-facing prompts, skills, system instructions, methodology, templates, generalized knowledge, fixtures, and evals that can power Parker for users.

> **New to Parker?** New customers get 1 month free with code **`PARKERBRAIN`** — limited spots → **[heyparker.ai](https://heyparker.ai)**
>
> **Full instructions doc:** [here](https://docs.google.com/document/d/1zsNCydlMu8u6sBlaqiL5TEIAE-aAYUOFj-mlbRjf9VE/edit?usp=sharing)
> 
> 📺 **Setting up your brand's brain?** Watch the [setup walkthrough](https://drive.google.com/file/d/1zxs88XEx1-zdbHjO-DfNc70a3zuGYnuF/view) for full onboarding instructions.

This repo is not the private OS/lab. Raw prompt experiments, test brand outputs, MCP snapshots, planning notes, raw expert inboxes, and private reasoning traces stay in the OS/lab repo unless they are sanitized and promoted.

## Open Source Availability

This repository is public source-available under the [PolyForm Noncommercial License 1.0.0](./LICENSE.md). You may use, study, modify, and share it for noncommercial purposes.

Commercial use is not permitted under this license. If you need commercial rights, you need a separate written license from the copyright holder.

This is intentionally not an Apache, MIT, or BSD-style open-source release. Those licenses allow commercial use; this repo is shared publicly so teams can inspect and build on the Parker brain for noncommercial purposes while keeping commercial rights reserved.

## Make Parker your own

The goal of this repo is to hand you a strong foundation and then get out of your way. What's here is the starting point — the full creative-strategy knowledge, the prompts and skills, the system architecture, and the initial structure for a brand brain — assembled so you don't have to build any of it from scratch. **It is meant to be built on, not just run.** Take it, wire it into your brand and your tools, and make it the best version of Parker for your team.

That means:

- **Extend and customize freely.** Tune the prompts, add skills, adapt the methodology, reshape the structure to fit how your team actually works. The foundation is opinionated so it's useful on day one, not so it's fixed forever.
- **Build on top in your own repo, not in this one.** "Make it your own" happens in your brand's repository (see below), where the brain learns your brand and your team grow it over time. This clone stays the clean factory you can always pull improvements from.
- **The brain is built to improve itself with you.** Connected tools, the refresh and self-improvement routines, and human feedback all feed back into the brain — the more you use it and the more you teach it, the better it gets. We give you the engine and the starting context; how good it becomes is up to you.

## Using this for a brand

`parker-brain` is the read-only factory. **A brand brain you build from it lives in its own separate repository — you do not build on top of this repo.** That brand repo is provisioned by the **`setup_parker_brain` tool on the Parker MCP**: it creates the brand's private GitHub repo — or retrieves the existing one — and returns short-lived credentials to clone and push with, so you never create the repo by hand. The brand repo is the whole workspace: the brand's data sits flat at its root, the executable skills (craft + routine) are copied into `.claude/skills/` — the one directory Claude Code loads skills from, so they register the moment the brain is cloned — and this factory is mounted at **`parker-system/` as a git submodule pinned to a release tag** (`v1`, `v2`, …). Nothing is copied or path-rewritten: every prompt, craft doc, and system doc resolves inside the mount at the same `parker-system/…` paths the prompts already carry, the brain can refresh and rebuild its own docs by re-running the exact prompts that generated them, and updates arrive only when the brain's weekly `/update-brain` routine offers the newer release and the team says yes (applying `migrations/` in order). The mount is read-only — the brain's committed settings deny edits under it — and clones use `git clone --recurse-submodules` (a session-start hook catches a clone that skipped it). Commit and push the brand repo often; pull it (with `--recurse-submodules`) before working — the full git procedure (credentials, conflicts, the self-hosted exception) is the brain's `save-brain` skill, enforced by its `git-guard` hook and explained in `system/brain-git-sync.md`. The most important instructions for creating a Parker Brain are in `prompts/onboarding-runner.md` - it is the executable cold-start sequence, and `prompts/README.md` is the why behind it.

The data tools the prompts call run through the **Parker MCP**. If it is not connected, Parker has no live reach into the ad account, organic socials, reviews, surveys, or the competitor ad library — the Parker MCP is the one connection that brings all of it online at once, though independent platform exports can feed the same evidence more manually. `system/parker-tools.md` is the canonical tool inventory.

To stand one up, sign up and connect the Parker MCP at **[heyparker.ai](https://heyparker.ai)** (new customers get 1 month free with code `PARKERBRAIN`, limited spots), then run this in Claude Code:

```
Set up my brain for my brand [brand], follow instructions in here: https://github.com/real-simple-labs/parker-brain
```

**The skills are still under testing.** They ship as foundations — the full context and methodology so a team can stand these capabilities up and build on them — not as guaranteed-final products. Scriptwriting in particular is actively being trained. Treat skill output as a strong starting point a human should review.

## What Belongs Here

- `CLAUDE.md` - production-ready Parker operating contract and repo guidance.
- `prompts/` - production prompts for context docs, audits, personas, VoC, market reads, and databases.
- `.claude/skills/` - runtime skill instructions (scriptwriting, hooks, headlines, iterations, ad-account analysis, AI ad generation, the open-loops pipeline, and more). They live under `.claude/skills/` because that is the only directory Claude Code loads skills from, so they register and work the moment this repo is cloned.
- `.claude/agents/` - subagent definitions, loaded the same way. The creative skills spawn two independent ship gates on every draft, in order: `context-grounding-review` verifies the work was actually built from the right method docs, brand context, and data pulls (`scripts/grounding-check.py` traces quoted verbatims to the vault and resolves cited sources; the agent diffs the output's vocabulary against what a strategist would have loaded — a bounce means re-pull and regenerate), then `creative-voice-review` verifies it reads human (`scripts/voice-lint.py` plus the judgment pass against `creative-strategy-context/ai-writing-tells.md` and the brand's voice profile). Grounded first, human-sounding second.
- `system/` - product-level methodology, retrieval, attribution, open-loop, and review standards.
- `templates/` - reusable document templates.
- `global/knowledge/` - approved generalized knowledge.
- `self-improvement/` - product methodology for feedback, dreaming, and promotion behavior, not raw traces.
- `open-loops-training/` - training and rubric material used by the open-loops system.
- `fixtures/` - sanitized examples only.
- `evals/` - quality gates and regression checks.
- `release-notes/` - versioned summary of brain changes.

## What Does Not Belong Here

- Raw customer or brand outputs.
- Private test brands.
- Planning docs and build trackers.
- Raw transcripts and reasoning-layer notes.
- Raw expert-signal inboxes.
- Prompt-review scratch audits.
- Personal working preferences that are not product rules.
- Unsanitized MCP snapshots or source packets.

## Promotion Rule

Most learning starts in the private OS/lab. It enters this repo only after it is generalized, attributed, reviewed, and safe to ship.

Promotion flow:

1. Develop and test in the OS/lab.
2. Validate against real or fixture data.
3. Extract the durable product lesson.
4. Remove private or brand-specific details unless approved as a fixture.
5. Update the relevant prompt, skill, system doc, knowledge doc, fixture, or eval here.
6. Record the reason in a commit message, release note, or provenance comment.

## Current Status

Initial seed created from the Parker v2 transition workspace on 2026-06-04.

Before public or external distribution, confirm that methodology examples, fixtures, and knowledge docs are sanitized and do not include private brand, customer, prompt-run, MCP snapshot, or reasoning-layer material.

## Public Release Checklist

- Keep `.env`, `.env.*`, local settings, build artifacts, logs, and dependency folders ignored.
- Run a tracked-file secret scan before publishing.
- Replace any private or named-brand training examples with sanitized fixtures.
- Rewrite git history into a single curated commit before pushing to the public remote.
- Create a migrations/vN.md file for the new version
