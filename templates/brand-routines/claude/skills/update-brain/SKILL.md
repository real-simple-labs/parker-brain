---
name: update-brain
description: The weekly check that keeps this brain current with the parker-brain standard — without overriding anything the team chose. Compares the pinned parker-system/ release against the newest factory tag and offers the bump as one short question; on a yes the migrations run and a script re-syncs the copied skills deterministically. What the team declines stays declined; what they modified stays theirs. Use weekly as a scheduled routine, or when asked to update the brain, check for updates, sync with the standard, or "what's new in Parker".
---

# Update brain — offer the current standard, never impose it

The factory keeps improving after a brain ships: new method docs, sharper skills, new prompts, new system machinery. And a brain's own build can have holes — a source pull that never ran, a doc a dead session skipped. Left alone, both kinds of gap are invisible: the freshness system re-runs what is stale but cannot see what is missing, and a brain never learns the factory grew. This routine is the eyes for both — it finds every gap between this brain and the current standard, and turns each one into an offer.

**The one rule that governs everything here: offer, never override.** This brain belongs to the team. A doc they deleted was deleted for a reason. A skill they modified is theirs now. A gap they declined to fill last month is a decision, not an oversight. This routine's job is to make sure they always have the *opportunity* to take what's new and fill what's missing — and to remember their answers so it never nags. Nothing is ever applied, overwritten, or regenerated without their yes.

## When it runs

**Weekly** as a scheduled routine, early Monday, so the week starts with the offer list ready. Also runnable on demand whenever someone asks what's new or wants to bring the brain up to the standard.

## Terminology

Remember that most users are likely unfamiliar with git, so don't confuse the user with terms like "diff", "push to main", "pull a tag" - use commonly understood terms like "changes", "save new files", "download a new version". When describing changes, do it from a non-technical perspective: "improved the monthly report" instead of "refactored the report validation script". 

## The two comparisons

### 1. The brain vs the current factory — what's new in the standard

Read the brain's update posture from `running-notes/standard-sync.md` first — it decides which of two shapes this comparison takes. If the ledger is missing or unreadable, say so plainly and stop; never guess at what the standard contains.

Before deciding the mode or doing any comparison, also read `parker-system/migrations/README.md` and any `migrations/vN.md` newer than this brain's last-applied migration — a release can change the filesystem shape or how the two modes work, and that context belongs in the comparison before the offer is framed.

**Connected mode — `parker-system/` is a pinned submodule and the posture is `follow` (the standard shape).** The factory arrives whole or not at all, so there is no per-file diffing of the method: the offer is the *release*. Fetch the factory's tags (`git -C parker-system fetch --tags`) and compare the pinned release against the newest `vN` tag. If the pin is current, this comparison is one line in the digest. If the factory has moved:

- Name the new release and what changed — the factory's `release-notes/` entries and `migrations/` files between the pinned tag and the new one say exactly this; read them and put it in plain words.
- Offer the bump. **On a yes:** check out the new tag in `parker-system/`, then walk the factory's `migrations/` files in order — every `vN.md` with the old pin < N ≤ new pin — and apply each as written (they are agent-executable instructions: layout moves, re-runs, new files outside the copied bundle). Migrations that touch the brain's own data are still shown before applying. Then re-sync the **copied executable layer** — the craft skills, routine skills, review-gate agents, hooks, and checker scripts the build copied out of the mount into `.claude/`, `scripts/`, and `schedules/` — by running `python3 parker-system/scripts/sync-executable-layer.py --from <old pin>`. The script applies the three piles below deterministically: untouched copies refresh silently, team-edited files stay theirs and are listed, nothing is deleted. Its report is the truth — never re-diff those files by hand, and never turn its per-file lines into questions. Finally commit the moved pin and record the new release in the ledger and in `parker_config.json` (`parker_brain_version`).
- Never edit anything *inside* `parker-system/` — the mount is read-only; an update is only ever the pin moving.

**Decoupled mode — the posture is `own-factory` or `independent`, and `parker-system/` is the team's own vendored copy (or their own factory fork).** The team owns their method now, so the comparison is informational: fetch the public factory (shallow clone; the remote is recorded in the ledger), compare the methodology layers — the generating prompts, the craft knowledge in `parker-system/creative-strategy-context/`, the runtime system docs, the skills — and sort every difference into three honest piles:

- **New in the factory, absent here** — a method doc, skill, prompt, or system doc the factory added since this brain decoupled. These are the main offers: name each, say in one plain line what it does and why the factory added it, and offer to bring it in.
- **Changed in the factory, unmodified here** — the brain's copy matches an older factory version. Offer the refresh; this is the safe pile, since the team never touched theirs.
- **Changed here, by the team** — the brain's copy differs from every factory version because the team edited it. **Theirs wins, full stop.** Surface it once as a note ("your scriptwriting skill has local changes; the factory version also moved — want to see what changed there?") and never offer it again unless the factory ships something newer still.

Under `independent`, soften even that: one "FYI, the factory moved" line in the digest unless they've asked for offers.

In both modes, the brand lens, `expert-insights/`, and everything outside the methodology layers are never even compared — they are brand property, invisible to this routine.

### 2. The brain vs its own canonical build — what was never generated

Walk the generating prompts the brain ships in `parker-system/prompts/` against the standing docs actually on disk, using the build's own path map (shipped inert in `parker-system/prompts/onboarding-runner.md`). Every prompt whose standing output does not exist at its flat path is a hole the freshness system cannot see — a persona source pull that never ran, a sub-context slice a dead session skipped, a VoC category that came back empty and was never retried. This walk is an existence check only — does the doc exist at its path — never a read of doc contents, and it never becomes questions: its whole result is one line in the digest ("2 standing docs were never generated: X, Y — ask me to fill them"). Generate a missing doc only when the user explicitly asks, running its prompt in full through the brain's own methodology, exactly as a build would have. A doc the team deliberately deleted lands here too — which is why the ledger's memory applies: a hole they declined to fill stays out of the digest until something changes.

## Keep it quick

On the standard layout a routine update is a two-minute exchange, not a review session. One question per update, total: "New Parker update: vA → vB — <one plain sentence from the release notes>. Recommended — want it?" with short options (Take it / Skip / What changed?). Before the yes, do nothing beyond reading the release notes and migration files for the range — no diffing, no file-by-file analysis, no inventory of the brain. Never enumerate synced or skipped files inside a question, and keep option labels to a few words; "What changed?" is where the detail lives for whoever wants it. A team-edited file the sync script leaves alone is a one-line note in the closing summary, never a question. Close with a summary of five lines or fewer: the release taken, what the script refreshed (counts, not file lists), what stayed theirs, and any holes.

## The memory — decline once, not weekly

`running-notes/standard-sync.md` is this routine's ledger: the factory remote, the update posture (`follow` / `own-factory` / `independent`), the release the brain is pinned to (or was last compared against), which migrations have been applied, and every offer with its answer — taken (and when), declined (and why, when they gave a reason), or deferred. A declined offer is not raised again unless the factory version of that item has changed since the decline. This is what makes the routine a colleague and not a nag: it remembers what the team already said.

One connected-mode caveat on that memory: if the team declined an earlier release and later accepts a newer one, every migration between the old pin and the new one still runs. Declining a *release offer* does not skip the migrations those releases carried — the pin bump walks `vN.md` in order for the whole range.

## How the offers land

- **In an interactive run**, offer through the popup question form and apply what they take on the spot. On the standard layout that means the one release question from "Keep it quick" — the sync script handles the files, no per-file choices. Only a decoupled brain gets the grouped offer list (new craft, changed docs, missing outputs), each with take / decline / show-me-more choices. Whatever they take: stamp everything with its source and date, and update `refresh-schedule.md` and any affected INDEX in the same pass.
- **In a scheduled run with nobody there**, apply nothing. Write the offer list to the ledger, note it in the digest (the sync script's `--dry-run` report is how a scheduled run sees what a bump would touch without touching it), and let the next conversation (or the user's tap) carry the decisions. The Monday morning message is "here's what's new in the standard and what your brain is missing — want any of it?", never "here's what I changed."
- **Either way, the digest is plain:** what's new and why it matters, what's missing and what it would add, what was declined before and stayed declined. In Parker's voice, sized to what's actually there — a week with nothing new is one line, not a report.

## Hard rules

- **Offer, never override.** Nothing is copied, regenerated, or edited without the user's explicit yes, in any mode. No exceptions, including "obviously safe" ones.
- **The team's changes always win.** A locally modified file is surfaced once and left alone. Deleted is a decision. The brand lens and expert-insights are never compared, never offered against.
- **The mount is untouchable.** In connected mode, never write inside `parker-system/` — an update is the pin moving to a new release tag plus the migrations that release ships, nothing else. A brain that wants to edit the method decouples first (`/disconnect-factory`).
- **Remember the answers.** The ledger is read before any offer is made; a declined item stays quiet until the factory moves again.
- **Generate, don't fabricate.** A missing standing doc is filled by running its own generating prompt in full — never by writing a summary that looks like one.
- **Methodology comes from the factory; brand truth comes from the brand.** This routine copies method and generates outputs from data. It never invents brand content to fill a hole.
- Ask through the popup question form whenever a run needs the user; a question in plain chat strands the routine.
- Honor the brand hard rules on anything regenerated.

## Deliverable

A brain whose owner always knows exactly how it differs from the current standard — every gap offered with a plain reason, every taken item applied cleanly with provenance and fresh stamps, every declined item remembered — and a `running-notes/standard-sync.md` ledger that carries the whole history of what was offered and what the team chose.
