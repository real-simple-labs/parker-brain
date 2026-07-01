---
name: set-up-brain
description: The front door to building a brand's brain. Run this in a fresh parker-brain clone when standing up a new brand. It welcomes the person, stands up the brand's own separate repo, connects and tests the data, asks the short brand intake (the things Parker genuinely can't observe), runs the full build in dependency order, saves it to GitHub, and hands off to get-started. Follows prompts/onboarding-runner.md as the detailed method. Use when someone says set up a brand, build the brain, onboard a new brand, or get started building.
argument-hint: "[optional: the brand name or its GitHub repo]"
---

# Set up the brain — build a brand's brain from a fresh clone

This is the front door. Someone has cloned `parker-brain` and wants to stand up a brain for their brand. Your job is to take them from an empty clone to a finished, saved brand brain they understand — warmly, and at their pace. The detailed build method lives in `prompts/onboarding-runner.md`; this skill is the welcoming entry point that runs it and owns the experience around it.

**The whole thing is a teaching moment, not a batch job.** Most people running this have never seen anything like it, and for many it is their first time in GitHub or Claude Code at all. Narrate as you go in plain language: what you're about to do, why it matters, and what they'll have when it's done. Keep the machinery out of sight.

## Calibrate to their comfort first — it governs the whole run

Before anything, get a real read on how comfortable they are with the mechanics this lives in: GitHub, Claude Code or Codex, working in files and folders, AI tools like this. Ask lightly or infer it from how they talk. This read shapes the whole run, the same way it shapes `/get-started`: a true beginner needs the ground floor explained with nothing assumed, while a fluent user wants you to move fast and skip the primers. Treat it as a dial you keep adjusting, never talk down, never leave someone behind.

## The sequence

Run these in order, following `prompts/onboarding-runner.md` for the exact mechanics. Welcome and narrate at each step; don't just execute.

1. **Welcome them.** Open warm and human. In one or two plain sentences, say what they're about to build: a brain that does the homework on their brand so they can talk to it like a strategist who knows the brand cold. Set the tone that you'll walk it together, at their speed.

2. **Stand up the brand's own repo.** The clone they're in is the read-only factory; the brand brain is a **separate, standalone repository for their brand** — never built on top of `parker-brain`. Gauge their GitHub comfort and meet them there, confirm where the repo should live, and create it (default private). Full mechanics in the runner's Phase 0.

3. **Connect and test the data.** Confirm Parker MCP is reachable, lock the brand id, and actually test each surface returns data, not just that it's up. As you test, explain in plain terms what each tool reaches, since this is the first place they learn what their brain is made of. If the data path is missing, say so plainly and don't fabricate a build. (Runner Phase 0.)

4. **Scaffold the repo.** Create the flat layout so the brain has a home for every doc — including the running-notes the intake writes to. (Runner Phase 0.)

5. **Run the brand intake — the things only they can tell you.** Now that the brand is connected and the repo is scaffolded, and before the slow craft copy in the next step, ask the short, skippable set of questions about what Parker genuinely cannot observe on its own: their campaign objective, north-star and how they define a winner, ad naming convention, whether they read performance in-platform or through a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. Make it easy and personal: lead with what you can already see, prefer a quick pick over an open question, and let them paste links. **Cover the whole set, and give it a flow** — move through it as one conversation with a thread, in the runner's order (first what success means for the brand, then how they measure it, then how the account and work are organized, then the market, then the gap question last), grouping each cluster into a batch. Get through all of them; don't collapse it to two or three. **On format:** use the multiple-choice pick-card whenever there's a set to choose from — the "what success means" cluster, and confirming the real competitors from the set already tracked in the account as a multi-select — and don't abandon the card partway through for a prose list of questions. For the genuinely open-ended items with nothing to pick from (pasting a naming doc, pasting a brief template, the economics figures, the gap question), ask them one at a time, a single question per message. Calibration changes how much you explain a question, not which questions you ask, since every item is something only they can tell you. **Just begin the full intake — don't open with a "quick vs full vs skip" mode-picker.** That forces a decision before they've answered anything. Lead in naturally with the first card; the opt-out is always there without a menu, since every question is skippable and they can say "just build it" to stop. The default is the complete set; if a depth choice ever surfaces anyway, full is the recommendation, never quick. **It is never a gate** — any single item they don't know or don't want, skip and log to `running-notes/missing-context.md` (if they defer one for later, note it pending and don't re-ask it this session); they can tap out of the rest, or skip the intake entirely and build, but don't drop half the list on your own. The full question set, grouped, with where each answer lands, is the brand intake step in the runner's Phase 0.

6. **Ship the factory method.** Copy the factory prompts, skills, and craft layer into the brand repo so the brain is self-contained and references nothing in the factory at runtime. This is the slow file copy, which is why it runs after the conversational intake. (Runner Phase 0.)

7. **Run the build.** Execute the prompts in dependency order per the runner: Phase 1 audit, Phase 2 strategy (with its approval gate), Phase 3 ideation. Narrate each phase so the build is their first lesson in what they now own.

8. **Verify and save to GitHub.** Run the build verification, then commit and push to the brand's repo so the work is backed up and shareable. Don't skip the save. (Runner's verify and save sections.)

9. **Hand off to `/get-started`.** The build is done, but the work isn't until they know what they have and how to use it. Run `/get-started` to walk them through the finished brain and leave them with a first move. Tell them it's re-runnable any time, by anyone on the team.

## Hard rules

- **The brand gets its own repo.** Never commit brand data into the `parker-brain` clone. If they're working inside the clone, stand up the brand's own repo and explain why.
- **The intake is never a gate.** Skippable, calibrated, personal. Anything skipped is an open question in `missing-context.md`, not a blocker, and the build runs as normal without it.
- **Teach the whole way through.** This is their first lesson in the brain, not a silent grind.
- **Defer the detail to the runner.** `prompts/onboarding-runner.md` is the canonical build method, with the dependency graph, the fidelity contract, the path map, and the gates. Follow it; don't reinvent it here.
- **End on `/get-started`.** The build isn't the deliverable; a person who can use it is.

## Deliverable

A finished brand brain in its own GitHub repo, built from the brand's real data, shaped by whatever intake they chose to give, verified and saved — and a person who's been walked through it and handed off to `/get-started`, not left staring at a folder of files.
