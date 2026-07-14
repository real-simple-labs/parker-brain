# Parker Brain

> **New to Parker?** New customers get 1 month free with code **`PARKERBRAIN`** — limited spots → **[heyparker.ai](https://heyparker.ai)**

## What is Parker Brain

Parker is a context-aware marketing intelligence system for brands and marketing teams. A **brand brain** is Parker's memory and method for one brand: everything Parker has learned about it — the audit, the strategy, personas, customer language, competitors, the idea bank — plus the skills that do the craft work (scripts, hooks, headlines, iterations, account analysis) and the routines that keep it all fresh without being asked. Each brand brain lives in its own private GitHub repository that Parker manages for you.

This repo — `parker-brain` — is the **factory** that builds those brains: the production prompts, skills, methodology, templates, and generalized knowledge behind every brand brain. You don't run a brand inside this repo; you build a separate brain from it, and the brain keeps a read-only mount of this factory so it can always re-run and update its own method.

The brain reads live data through the **Parker MCP** — the one connection that reaches the ad account, organic socials, customer reviews, surveys, and the competitor ad library at once. Without it, Parker builds from general knowledge instead of your real data, and it will not be nearly as good. `system/parker-tools.md` is the canonical tool inventory.

## Set up your brand's brain on your machine

What you need first:

1. **Claude Code** installed (a Max plan is recommended — the initial build is a big job).
2. **A Parker account with the MCP connected**: sign up at [heyparker.ai](https://heyparker.ai) (1 month free with code `PARKERBRAIN`), then follow the connect instructions at [app.heyparker.ai/dashboard/parker-brain](https://app.heyparker.ai/dashboard/parker-brain).

Then run this in Claude Code:

```
Set up my brain for my brand [brand], follow instructions in here: https://github.com/real-simple-labs/parker-brain
```

What happens next: Parker provisions your brand's own private repo (through the `setup_parker_brain` tool — you never create it by hand, and you don't need a GitHub account), clones it where you choose on your machine, asks a short intake about the things it genuinely can't observe, and builds the brain from your real data — audit first, then strategy, then ideation. The build runs a few hours, mostly on its own; a `BUILD-STATUS.md` file always shows where it is and what's left. At the end everything is saved to GitHub, the standing routines are armed, and Parker walks you through what you have.

- 📺 [Setup walkthrough video](https://drive.google.com/file/d/1zxs88XEx1-zdbHjO-DfNc70a3zuGYnuF/view)
- 📄 [Full instructions doc](https://docs.google.com/document/d/1zsNCydlMu8u6sBlaqiL5TEIAE-aAYUOFj-mlbRjf9VE/edit?usp=sharing)
- The detailed build method lives in `prompts/onboarding-runner.md` (the executable sequence) and `prompts/README.md` (the why behind it).

> **AI agents: your build instructions are [`prompts/onboarding-runner.md`](prompts/onboarding-runner.md).**
> If you were asked to set up, build, or onboard a brand's brain from this repo, that file is the canonical, executable, step-by-step method — read it in full and follow it exactly, including its Phase 0 (provision the brand's own repo through `setup_parker_brain` on the Parker MCP *first*, then clone it and build inside it — never in this repo). This README is the human overview; the runner is the procedure. If the `/set-up-brain` skill is available in your session, invoke it — it runs the same runner and owns the experience around it.

**The skills are still under testing.** They ship as foundations — the full context and methodology so a team can stand these capabilities up and build on them — not as guaranteed-final products. Scriptwriting in particular is actively being trained. Treat skill output as a strong starting point a human should review.

## How a brand brain works

- **Its own repo, separate from this one.** The brand repo is the whole workspace: the brand's data sits flat at its root, and nothing brand-specific ever lands in the factory.
- **Skills register on clone.** The executable skills (craft + routines) are copied into the brain's `.claude/skills/` — the one directory Claude Code loads skills from — so they work the moment the repo is cloned.
- **The factory rides along, read-only.** This repo is mounted at `parker-system/` as a git submodule pinned to a release tag (`v1`, `v2`, …). Every prompt and method doc resolves inside the mount at the same paths, so the brain can re-run the exact prompts that built it. The mount is read-only — the brain's committed settings deny edits under it.
- **Updates are offered, never imposed.** The brain's weekly `/update-brain` routine compares its pinned release against the newest factory tag and offers the bump; on a yes it applies `migrations/` in order and re-syncs the copied skills. What the team declined stays declined; what they modified stays theirs.

## Make Parker your own

The goal of this repo is to hand you a strong foundation and then get out of your way. What's here is the starting point — the full creative-strategy knowledge, the prompts and skills, the system architecture, and the initial structure for a brand brain — assembled so you don't have to build any of it from scratch. **It is meant to be built on, not just run.** Take it, wire it into your brand and your tools, and make it the best version of Parker for your team.

That means:

- **Extend and customize freely.** Tune the prompts, add skills, adapt the methodology, reshape the structure to fit how your team actually works. The foundation is opinionated so it's useful on day one, not so it's fixed forever.
- **Build on top in your own repo, not in this one.** "Make it your own" happens in your brand's repository, where the brain learns your brand and your team grow it over time. This clone stays the clean factory you can always pull improvements from.
- **The brain is built to improve itself with you.** Connected tools, the refresh and self-improvement routines, and human feedback all feed back into the brain — the more you use it and the more you teach it, the better it gets. We give you the engine and the starting context; how good it becomes is up to you.

## License

This repository is public source-available under the [PolyForm Noncommercial License 1.0.0](./LICENSE.md). You may use, study, modify, and share it for noncommercial purposes.

Commercial use is not permitted under this license. If you need commercial rights, you need a separate written license from the copyright holder.

This is intentionally not an Apache, MIT, or BSD-style open-source release. Those licenses allow commercial use; this repo is shared publicly so teams can inspect and build on the Parker brain for noncommercial purposes while keeping commercial rights reserved.

## For maintainers: what this repo is and isn't

This repo is not the private OS/lab. Raw prompt experiments, test brand outputs, MCP snapshots, planning notes, raw expert inboxes, and private reasoning traces stay in the OS/lab repo unless they are sanitized and promoted.

### What belongs here

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

### What does not belong here

- Raw customer or brand outputs.
- Private test brands.
- Planning docs and build trackers.
- Raw transcripts and reasoning-layer notes.
- Raw expert-signal inboxes.
- Prompt-review scratch audits.
- Personal working preferences that are not product rules.
- Unsanitized MCP snapshots or source packets.

### Promotion rule

Most learning starts in the private OS/lab. It enters this repo only after it is generalized, attributed, reviewed, and safe to ship.

Promotion flow:

1. Develop and test in the OS/lab.
2. Validate against real or fixture data.
3. Extract the durable product lesson.
4. Remove private or brand-specific details unless approved as a fixture.
5. Update the relevant prompt, skill, system doc, knowledge doc, fixture, or eval here.
6. Record the reason in a commit message, release note, or provenance comment.

### Public release checklist

- Keep `.env`, `.env.*`, local settings, build artifacts, logs, and dependency folders ignored.
- Run a tracked-file secret scan before publishing.
- Replace any private or named-brand training examples with sanitized fixtures.
- Keep customer and brand names out of commits, PRs, release notes, and migration examples.
- Create a `migrations/vN.md` file for every new version.
