---
name: brand-idea-bank-maintenance
description: Maintain a brand-specific idea bank from context docs, research, Parker data, user conversations, manual ideas-tab saves, expert signals, competitor ads, organic videos, and internal Parker observations.
triggers:
  - update the brand idea bank
  - add this to the idea bank
  - save this idea
  - backfill the idea bank
  - build the idea bank
  - ideas tab
  - save this concept
  - Parker should remember this idea
---

# Brand Idea Bank Maintenance

## Goal

Maintain the living idea bank for a specific brand. The brand idea bank stores ideas Parker may want to retrieve later for hooks, scripts, headlines, briefs, audits, concept generation, and creative strategy.

The brand idea bank spec lives at `prompts/ideas-and-briefs/brand-idea-bank.md`. Read that spec before creating, updating, merging, or curating entries.

## What feeds the idea bank

Parker should create or update idea-bank entries from:

- brand context docs
- source pulls and research extracts
- competitor docs and ad-account evaluations
- monthly and quarterly audits
- Parker MCP ad and creative reads
- organic video and social research
- expert signals
- user conversations
- manually saved ideas from the ideas tab
- internal Parker observations during work

## What you are working from

The keep-or-cut judgment this skill makes on every entry runs on the canonical ideation method, not a generic gut call. Before deciding what belongs, load what `global/knowledge/creative-strategy/expertise-routing.md` names for idea-bank and ideation work: `ideation-and-brainstorming.md`, the senior-strategist reasoning for what an idea is, where ideas come from, and what makes one worth keeping. The storage schema this skill fills lives in its spec, `prompts/ideas-and-briefs/brand-idea-bank.md`; the spec is how that reasoning gets stored, so read both before curating. Brand and creative data pull through the Parker tools inventoried in `system/parker-tools.md`.

From the ideation method, the bar an entry has to clear is freshness, not familiarity. The ice box is for new directions worth targeting — a fresh angle, a different visual, a hook the brand is not already running — and every entry carries what was liked and why, because that note is what makes a half-baked idea retrievable later. The capture bar is lower than a concept's on purpose: a hook, a format, a storyline, a single line of customer language, or a visual is enough to log when something resonated. But what counts as worth keeping is relative to the brand's goal and the state of its account, so weigh the idea against both where they are known. An entry that never speaks the method's language proves the method was never opened.

## How this skill runs

1. **Identify the active brand.** Use the brand the user is working in or the brand tied to the current task.

2. **Find the source of the idea.** The source may be a link, a local context doc, a Parker result, a user conversation, or an ideas-tab save.

3. **Decide whether it belongs.** Save the idea only if it gives a strategist a fresh direction to act on — a new angle, visual, hook, or format the brand is not already running — and is specific enough to retrieve later. Do not save generic strategy observations, and do not log the brand's own known assets reflected back, because an award, channel, or credibility marker the brand already advertises hands the strategist nothing to test. Record what was liked and why so the half-baked idea stays retrievable.

4. **Write or update the entry.** Use one file per idea under `z-brands/[brand]/idea-bank/entries/`.

5. **Update the index.** Add or update the concept name, source type, winning elements, stage of awareness, status, and source path.

6. **Keep adaptation separate.** Do not write how the brand should run a competitor, inspiration, affinity, or expert-sourced idea inside the source entry. That work belongs in future concept-generation and grading runs.

## Backfill mode

Run backfill mode when a brand idea bank is first created or when the user asks to build it from context.

Read the brand profile, sub-context docs, source pulls, competitor docs, audits, and available user conversation memory. Pull ideas that Parker would want to retrieve during creative work. Create entries for the strongest ideas and leave a note in the index naming what source areas still need backfill.

## Continuous maintenance mode

During normal user conversations, add candidates when the user explicitly saves an idea, when the ideas tab contains a manual save, or when Parker notices a reusable pattern that belongs to the active brand.

During expert-signal intake, always make an idea-bank routing decision. If the expert source contains a brand-specific creative idea, update the active brand's idea bank. If the idea is reusable but not brand-specific, update `global/knowledge/creative-strategy/parker-taste/` instead of forcing it into one brand. If the signal is method-only or measurement-only, record that no idea-bank entry was created.

When the user says an idea is not useful, mark it rejected and preserve the reason if the reason teaches a brand boundary.

## Output structure

### Idea Bank Updates

List entries created, updated, merged, rejected, or marked stale.

### Index Updated

Name the index path updated.

### Gaps

Name any source areas that still need backfill or access.

## Hard rules

- The idea bank is the brand's idea memory, not a strategy doc.
- Preserve source, winning elements, justification, stage of awareness, and notes.
- Manual ideas-tab saves should enter unless marked throwaway.
- User conversation ideas can enter when durable.
- Use narrative reconstruction for videos, ads, posts, and visual examples.
- Do not add adaptation instructions to source entries.
- Keep evidence strength visible.
