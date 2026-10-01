---
name: setup-routines
description: Arms the brand brain's standing routines (refresh-context, dream, harvest+evaluate ideas, research-loops, update-brain, self-improve) as scheduled cloud agents so they run on cadence without being asked. The job definitions already travel with this repo; this skill registers the schedules, which are per-account and can't be committed. The onboarding build runs it automatically at the stamp step (build mode, no questions); run it yourself after cloning the brain into a new Claude Code cloud instance, or any time to change a cadence or turn a routine off.
---

# Setup routines — arm the schedules

The routine *jobs* (`/refresh-context`, `/dream`, `/harvest-ideas`, `/evaluate-ideas`, `/research-loops`, `/update-brain`, `/self-improve`) already travel with this repo and are live wherever the folder lands. What does **not** travel is the *schedule* — cron cloud agents are bound to an individual account and can't travel with the folder. This skill registers them for this instance.

## How it works

For each routine below, create a scheduled cloud agent (a "routine") whose prompt gets the brain through the Parker MCP and runs the corresponding skill in that copy (step 2 has the exact prompt). Use the **`/schedule`** skill / command to create each one (it manages the cron cloud agents). The cadence and the exact prompt for each are also recorded in `../schedules/*.md` — those schedule docs are the canonical recipe; this skill is the guided installer.

This skill runs two ways. **Build mode** — the onboarding build invokes it at the stamp step: register all six routines at the default cadences below with no questions asked, using the user's timezone when the session already knows it (from intake or the account) and the suggested times otherwise. The build's go-ahead covers the consent and the build's finish carries the disclosure, so don't re-ask here. **Guided mode** — a person invokes it: before registering, confirm their timezone, which routines they want, and that the instance's data sources (Parker MCP server, web tools) are connected — a scheduled run can only do what the connected tools allow.

Check the scheduling capability before either mode. These recipes register Claude Code cloud schedules. In Codex, record scheduling as deferred in the build record or routine digest, leave unregistered recipes inactive, explain that the skills work on demand, and return successfully to onboarding. Do not attempt `/schedule` there or block build completion. A team's external cron is separate setup; before any headless job relies on hooks, trust the project and approve its hooks interactively. The contract is `parker-system/system/codex-support.md`.

**Say what it costs — plainly, once, at the right moment.** Every scheduled run is a real Claude Code session doing real reading and writing, and it draws from the same usage as everything else on the account — the plan's usage limits on a subscription, per-token billing on an API account. Six routines with dreaming daily is a meaningful standing draw, and dreaming is the biggest single driver. In guided mode, say this before registering and let it shape their picks — turning dreaming down to a few days a week, or starting with a subset, is a perfectly good answer. In build mode, don't interrupt the build with it, but make sure the finish's disclosure sentence carries it: what's running, when, that it consumes usage on this account, that the routines can save only from a cloud environment with full network access (or `git.heyparker.ai` allowed), and that `/setup-routines` changes the cadence or turns any routine off.

## The routines to register

| Routine | Skill | Cadence | Suggested cron |
|---|---|---|---|
| Context refresh | `/refresh-context` | Weekly | Mon 06:00 |
| Dreaming | `/dream` | Daily | 05:00 daily |
| Idea cycle | `/harvest-ideas` then `/evaluate-ideas` | Weekly | Mon 07:00 |
| Research cycle | `/research-loops` | Weekly | Wed 06:00 |
| Standard updates | `/update-brain` | Weekly | Mon 05:30 |
| Self-improvement | `/self-improve` | Weekly | Fri 16:00 |

Times are suggestions — confirm against the user's timezone and working rhythm. Dreaming runs earliest so its proposals are ready for a morning suggestion; the research cycle runs mid-week so Monday's refresh feeds it and its findings are fresh for Friday; self-improve runs end-of-week so it can dispose of the week's dreaming and research proposals and freshly captured traces.

## Steps

1. **Confirm prerequisites** (guided mode only) — timezone, connected MCP/web tools, and that the user wants all six (or a subset). Build mode skips this step and registers the full set at the defaults.
   - **Check what's already armed — in two layers, live state first.** List this account's live schedules via `/schedule` — that's the ground truth for what *this* account owns, and the reconcile step below works from it. Then read the committed `../schedules/*.md` status lines — the only visibility into *other* accounts, since you can't list a teammate's schedules. Treat the stamps as claims, not truth: if a stamp says this account armed a routine but the live list disagrees, trust the live list and fix the stamp. If the stamps say another instance armed them (registered by someone else, with a date), say so plainly and ask before arming: two accounts running the same weekly refresh or nightly dream means every routine fires twice — double the usage, and two cloud runs pushing generated docs into the same repo. The right setups are one teammate owning the schedules, or splitting the routines between accounts — never the same routine armed twice. Only arm a duplicate when the prior instance is being retired, and note the handover in the status line.
2. **Register each routine** via `/schedule`, one per row above: all six in build mode, and in guided mode only the ones the user picked in step 1. **Prefix every schedule's name with the brand** — "[brand]: dream", "[brand]: standard updates" — because schedules are account-level, and an account running two brand brains would otherwise hold two indistinguishable "dream" jobs; the prefix is also what the reconcile step matches on. For the idea cycle, schedule a single weekly agent that runs `/harvest-ideas` then `/evaluate-ideas` in sequence.
   - **The run gets the brain itself.** A cloud routine has no Parker Desktop beside it, and it usually can't read the brain's own storage on GitHub (that is what broke routines before v24). So:
     - attach the **Parker MCP** to each routine;
     - give it a repository it can read as its source (routines need one), but not this brain's: the public factory, `real-simple-labs/parker-brain`, works. The run clones the brain on its own and must never change that source repository;
     - run it in a cloud environment with **full network access**, or one whose allowed list has `git.heyparker.ai`. The default "Trusted" network lets the Parker MCP answer but blocks git to Parker's server (`host_not_allowed`), so the run could never save.
   - **The prompt is the cloud-run preamble plus the job.** Fill in the brand's name and its `brand_id`: copy the id exactly from `parker_config.json`, and check it against `get_available_brands` when the Parker MCP is connected. A wrong id fails the run's access check, so the routine would run and save nothing. Fill in [key command] too, word for word: it is the tool's `make_credential_command` (call `register_parker_brain_git_credential` once with only the `brand_id` and copy it from the answer). On Parker's production servers it is this, with the brand's id in place of `<brand_id>`:

     ```
     (s="parker_git_$(openssl rand -hex 32)" && printf 'protocol=https\nhost=git.heyparker.ai\nusername=parker-<brand_id>\npassword=%s\n\n' "$s" | git -c credential.helper= -c 'credential.helper=cache --timeout=86400' credential approve && printf '%s' "$s" | openssl dgst -sha256 -r | cut -c1-64)
     ```

     The command must sit in the prompt itself. A cloud session's safety check (auto mode) stops a stored key that only a tool's text asks for, because it never sees tool results; the same command in the routine's own prompt is the person's own request, and it passes.

     > This is a scheduled cloud run for the Parker Brain of [brand] (brand_id [brand_id]). No Parker Desktop runs here, so you get the brain and save it yourself. Get a fresh copy of that brain with the Parker MCP tool `register_parker_brain_git_credential` for that brand_id, even if this session started in another copy, and follow its steps exactly. Its first step makes the one-hour key for Parker's git server; run exactly this command for it (it keeps the key only in git's memory, writes no file, and prints only the key's hash, which is what you send the tool):
     >
     > [key command]
     >
     > Never print the key. Work only inside the new copy, and never change the repository this session started in: read the copy's `CLAUDE.md`, and run the job below by following its skill in `.claude/skills/`. When you are done, save as the copy's `.claude/skills/save-brain/SKILL.md` says under "In a cloud run": you have permission to push straight to `main` of that copy (`git push origin HEAD:main`), and you must not create a branch. If you can't get the brain, say so plainly and stop.
     >
     > Run the /dream routine for this brand brain. Follow the skill exactly; propose, never apply.

     The job line stays minimal, letting the committed SKILL.md carry the method; each schedule's recipe in `../schedules/` has its own.
   - **If the Parker MCP has no `register_parker_brain_git_credential` tool** (an older Parker MCP), register the routine the way it was before v24 — in this repo, with the job line alone — and tell the person plainly that a cloud run can do the work but can't save it yet. Run `/setup-routines` again once the tool is there.
3. **Verify** — list the scheduled routines back to the user with their next-run times, and confirm each points at the right skill.
4. **Record** — note in each `../schedules/[slug].md` that the schedule is registered for this instance (status: active, plus who registered it and when, and "saves in a cloud run (v26)" when its prompt starts with the cloud-run preamble above, key command included; the new line replaces the old one, a "needs re-arm" note included), so the schedule doc reflects reality and a teammate's later `/setup-routines` run can see the routines are already owned. The files save and sync like any other change (a self-managed team commits them).

## Notes

- **Re-runnable safely**: if a routine is already registered, update it rather than duplicating. List existing scheduled routines first and reconcile — matching on this brand's name prefix, so another brain's routines on the same account are never touched.
- **Subset is fine**: a user may want only dreaming + ideas at first. Register what they confirm; leave the rest documented in `../schedules/` for later.
- **Manual fallback**: every routine can also be run on demand by invoking its skill directly (`/dream`, `/self-improve`, …) without any schedule — useful for a first manual pass before arming the cron.
- Self-contained: this skill only registers schedules that point at in-repo skills. It does not depend on the factory.
