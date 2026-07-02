---
name: setup-routines
description: One-time setup for a fresh brand brain instance. Registers the standing routines (refresh-context, dream, harvest+evaluate ideas, research-loops, update-brain, self-improve) as scheduled cloud agents so they run on cadence without being asked. The job definitions already travel with this repo; this skill arms the schedules, which are per-account and can't be committed. Run once after cloning the brain into a new Claude Code cloud instance, or when asked to set up / register / schedule the routines.
---

# Setup routines — arm the schedules (run once per instance)

The routine *jobs* (`/refresh-context`, `/dream`, `/harvest-ideas`, `/evaluate-ideas`, `/research-loops`, `/update-brain`, `/self-improve`) already travel with this repo and are live the moment it's cloned. What does **not** travel is the *schedule* — cron cloud agents are bound to an individual account and can't be committed to git. This skill registers them once for this instance.

## How it works

For each routine below, create a scheduled cloud agent (a "routine") whose prompt is simply to run the corresponding skill in this repo. Use the **`/schedule`** skill / command to create each one (it manages the cron cloud agents). The cadence and the exact prompt for each are also recorded in `../schedules/*.md` — those schedule docs are the canonical recipe; this skill is the guided installer.

Before registering, confirm with the user: their timezone, and that the instance's data sources (Parker MCP server, web tools) are connected — a scheduled run can only do what the connected tools allow.

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

1. **Confirm prerequisites** — timezone, connected MCP/web tools, and that the user wants all four (or a subset).
2. **Register each routine** via `/schedule`, one per row above (all six). The scheduled prompt should be minimal — e.g. *"Run the /dream routine for the brand brain in this repo. Follow the skill exactly; propose, never apply."* — letting the committed SKILL.md carry the method. For the idea cycle, schedule a single weekly agent that runs `/harvest-ideas` then `/evaluate-ideas` in sequence.
3. **Verify** — list the scheduled routines back to the user with their next-run times, and confirm each points at the right skill.
4. **Record** — note in each `../schedules/[slug].md` that the schedule is registered for this instance (status: active), so the schedule doc reflects reality.

## Notes

- **Re-runnable safely**: if a routine is already registered, update it rather than duplicating. List existing scheduled routines first and reconcile.
- **Subset is fine**: a user may want only dreaming + ideas at first. Register what they confirm; leave the rest documented in `../schedules/` for later.
- **Manual fallback**: every routine can also be run on demand by invoking its skill directly (`/dream`, `/self-improve`, …) without any schedule — useful for a first manual pass before arming the cron.
- Self-contained: this skill only registers schedules that point at in-repo skills. It does not depend on the factory.
