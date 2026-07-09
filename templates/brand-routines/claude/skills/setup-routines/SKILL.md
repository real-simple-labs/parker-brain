---
name: setup-routines
description: Arms the brand brain's standing routines (refresh-context, dream, harvest+evaluate ideas, research-loops, update-brain, self-improve) as scheduled cloud agents so they run on cadence without being asked. The job definitions already travel with this repo; this skill registers the schedules, which are per-account and can't be committed. The onboarding build runs it automatically at the stamp step (build mode, no questions); run it yourself after cloning the brain into a new Claude Code cloud instance, or any time to change a cadence or turn a routine off.
---

# Setup routines — arm the schedules

The routine *jobs* (`/refresh-context`, `/dream`, `/harvest-ideas`, `/evaluate-ideas`, `/research-loops`, `/update-brain`, `/self-improve`) already travel with this repo and are live the moment it's cloned. What does **not** travel is the *schedule* — cron cloud agents are bound to an individual account and can't be committed to git. This skill registers them for this instance.

## How it works

For each routine below, create a scheduled cloud agent (a "routine") whose prompt is simply to run the corresponding skill in this repo. Use the **`/schedule`** skill / command to create each one (it manages the cron cloud agents). The cadence and the exact prompt for each are also recorded in `../schedules/*.md` — those schedule docs are the canonical recipe; this skill is the guided installer.

This skill runs two ways. **Build mode** — the onboarding build invokes it at the stamp step: register all six routines at the default cadences below with no questions asked, using the user's timezone when the session already knows it (from intake or the account) and the suggested times otherwise. The build's go-ahead covers the consent and the build's finish carries the disclosure, so don't re-ask here. **Guided mode** — a person invokes it: before registering, confirm their timezone, which routines they want, and that the instance's data sources (Parker MCP server, web tools) are connected — a scheduled run can only do what the connected tools allow.

**Say what it costs — plainly, once, at the right moment.** Every scheduled run is a real Claude Code session doing real reading and writing, and it draws from the same usage as everything else on the account — the plan's usage limits on a subscription, per-token billing on an API account. Six routines with dreaming daily is a meaningful standing draw, and dreaming is the biggest single driver. In guided mode, say this before registering and let it shape their picks — turning dreaming down to a few days a week, or starting with a subset, is a perfectly good answer. In build mode, don't interrupt the build with it, but make sure the finish's disclosure sentence carries it: what's running, when, that it consumes usage on this account, and that `/setup-routines` changes the cadence or turns any routine off.

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
   - **Check for another instance's schedules first — this brain may be shared.** Schedules are per-account, so a teammate may already have these routines armed on *their* account: read the `../schedules/*.md` status lines before registering anything. If they're marked active (registered by someone, with a date), say so plainly and ask before arming: two accounts running the same weekly refresh or nightly dream means every routine fires twice — double the usage, and two cloud runs pushing generated docs into the same repo. The right setups are one teammate owning the schedules, or splitting the routines between accounts — never the same routine armed twice. Only arm a duplicate when the prior instance is being retired, and note the handover in the status line.
2. **Register each routine** via `/schedule`, one per row above (all six). **Prefix every schedule's name with the brand** — "[brand]: dream", "[brand]: standard updates" — because schedules are account-level, and an account running two brand brains would otherwise hold two indistinguishable "dream" jobs; the prefix is also what the reconcile step matches on. The scheduled prompt should be minimal — e.g. *"Run the /dream routine for the brand brain in this repo. Follow the skill exactly; propose, never apply."* — letting the committed SKILL.md carry the method. For the idea cycle, schedule a single weekly agent that runs `/harvest-ideas` then `/evaluate-ideas` in sequence.
3. **Verify** — list the scheduled routines back to the user with their next-run times, and confirm each points at the right skill.
4. **Record** — note in each `../schedules/[slug].md` that the schedule is registered for this instance (status: active, plus who registered it and when), and commit the change, so the schedule doc reflects reality and a teammate's later `/setup-routines` run can see the routines are already owned.

## Notes

- **Re-runnable safely**: if a routine is already registered, update it rather than duplicating. List existing scheduled routines first and reconcile — matching on this brand's name prefix, so another brain's routines on the same account are never touched.
- **Subset is fine**: a user may want only dreaming + ideas at first. Register what they confirm; leave the rest documented in `../schedules/` for later.
- **Manual fallback**: every routine can also be run on demand by invoking its skill directly (`/dream`, `/self-improve`, …) without any schedule — useful for a first manual pass before arming the cron.
- Self-contained: this skill only registers schedules that point at in-repo skills. It does not depend on the factory.
