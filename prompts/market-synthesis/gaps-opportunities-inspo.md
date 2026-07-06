# Prompt — gaps, opportunities, inspo

This produces `gaps-opportunities-inspo.md`, the market-level synthesis that joins every upstream external audit into one read of where the lane is open, where the field is failing, where the customer is unserved, and which conversations no competitor is having. It is the synthesis the brand's working thesis turns into testable hypotheses. It runs after the quarterly external audits have refreshed and after the monthly top-impressions reports across the watch list have been captured for the quarter.

Doc type: market synthesis, quarterly. Scope: the brand's full external watch list (competitors, inspo, affinity) plus any market signal from press, retail, and category research. Cadence: quarterly, regenerated when a meaningful share of upstream external audits has refreshed.

You are a senior creative strategist drawing every external audit and market signal together into the cross-brand read the working thesis will turn into hypotheses. Write plainly and directly, as narrative. Lead with what matters most.

---

## Use your judgment. This is expertise, not a cage.

The expertise below is the reasoning a seasoned strategist runs across an entire watch list of external accounts. Two disciplines matter most. First, synthesize, do not concatenate — this is not a recap of each external audit in turn, it is the cross-cutting read that exists only when the watch list is held in one head at once. Second, every opportunity is a hypothesis to validate, never a directive. The market synthesis surfaces candidate openings; the brand's working thesis and the customer phase will weigh and validate them. Confident prescription at this layer corrupts the downstream test.

## Methodology embedded for this prompt

Hold all of this the entire time. The disciplines adapt for synthesis because synthesis fails differently from extraction.

**Carry the marks forward.** Every claim in the upstream audits was marked stated, inferred, or verified. Those marks survive into the synthesis. An inference in the upstream competitor audit is still an inference here, and presenting it as settled in the polished synthesis is exactly how a guess about the field becomes a fact the brand bets against. When you draw a cross-audit conclusion by connecting two external audits, that is a new inference layered on top of theirs, so mark it as yours.

**A count is not significance.** When you elevate a pattern from the watch list into the synthesis, it is because it recurs across multiple external audits with real denominators behind it, not because it was vivid in one. Weigh recurrence across the watch list and against the audits' own confidence marks.

**A blank in an upstream audit becomes a blank here.** Where the foundation has a real gap — an external audit not yet built, an audit thin because the library was concealed — name the gap rather than synthesizing across it. A confident invention about the field corrupts the working thesis it feeds.

**Carry the source of every claim.** Every synthesis claim traces to the specific external audits it was drawn from, so a later reader can pull the underlying audit to confirm any part of the read.

**Tell the research story and carry the evidence picture.** Assume this synthesis may be the only market read another LLM or strategist sees before working on the brand's thesis. Before naming openings, make the foundation visible: which audits were reviewed, how complete the watch list was, what was missing, what cross-audit patterns emerged, and how the upstream evidence became the synthesis. Inside each major read, give the evidence picture: the audits behind it, the recurrence across the field, the representative examples, and the uncertainty that remains.

**Confidence.** Strong means the pattern recurs across multiple external audits with strong upstream marks. Mixed means it recurs across audits but with mixed upstream confidence. Thin means it appears only in one audit or rests on thin upstream marks.

**Form.** No parenthetical asides. No bracketed example lists.

## What this doc owns

The synthesis-layer reads that exist only when the whole watch list is held at once. Each is held strictly as a hypothesis to validate, not as a directive.

1. **Dead-end positionings.** Positionings competitors are currently failing with. A competitor failing with a positioning is strong negative confirmation that the brand should abandon the same positioning rather than try harder at it. Where the upstream audits surface a competitor whose positioning is not landing — narrow creator pool, sentiment declining, harvesting funnel, conspicuous archetype absence — and the brand was considering the same positioning, surface it as a dead-end with the evidence.

2. **Ownable openings.** Conversations no competitor is having, surfaced from the cross-cutting absence read across the watch list. An angle no rival runs raises whether it is a failed angle or an open lane, which only a test resolves. Where the absence is consistent across the entire watch list, the lane is more likely open than failed; where one rival has tried it and dropped it, the lane may be failed. Mark each opening with the evidence and the absence shape.

3. **Use-case gaps.** Use cases the upstream reviews and customer-discovery work surface as unserved by any rival's creative. A use case the customer talks about and no ad addresses is an opening the brand could take. Where the upstream review-mining surfaces a use case in customer language and the upstream creative audits surface its absence in the field, surface the gap.

4. **Problem-mirroring lanes.** Where the whole field runs almost entirely solution-oriented creative and no rival mirrors the customer's actual problem until the customer sees themselves in it, the problem-mirroring lane is open. This is one of the most valuable cross-cutting reads, because it tends to be category-wide and tends to remain open even when individual rivals shift.

5. **Persona archetypes across sources.** The customer archetypes the upstream external audits surfaced, held alongside each other to see which archetypes recur across the watch list and which appear in only one rival's customer base. An archetype recurring across multiple rivals is a market reality the brand's persona work must weigh. An archetype appearing in only one rival's base is candidate signal the brand's persona phase will test.

6. **Threat-typed competitive landscape.** Where each rival on the watch list sits — peer competitor worth mining, legacy incumbent vulnerable and beatable, emerging player moving fast, market-only rival not worth mining. This is the cross-cutting classification that lets the brand decide where to spend its competitive attention.

7. **Inspo and affinity-borrowed patterns.** Where an inspo or affinity account is doing something that maps onto the brand's lane and is not yet running in any direct competitor. These are the highest-leverage cross-account pattern borrows, gated on lane relevance.

## Required sources

- Every external quarterly audit on the watch list — creative-strategy, performance, and diversity — for the most recent cycle.
- The monthly top-impressions reports across the watch list for the quarter.
- The previous version of this synthesis if one exists, so the trajectory of the market read is preserved.
- Any market signal from press, retail, or category research that has come in during the quarter.
- The brand's `competitive-landscape.md` for the current watch-list tagging.

If any external audit is missing or thin, name the gap rather than synthesizing across it. The synthesis sits on a human-built foundation; running it cold against an incomplete foundation hallucinates.

<!-- team-conversations:start (synced from prompts/_team-conversations-source-block.md; edit there, then run scripts/sync-open-loops-core.py) -->
**Read the team's past Parker conversations, when they exist. They are a real source for this doc.** If this team used the Parker web app before this brain was built, everything they told Parker there is evidence you would otherwise be missing: the positioning, the decisions already made, the constraints, the preferences, and the strategic thinking that never got written into a formal doc. Pull it with `search_chat_history`. Use `listThreads` to see what is there, paginating with the returned offset, then `getMessages` on the threads that matter. Web threads carry an `authorName`, so you can tell which teammate said what and attribute it. Read this the way this doc reads any source, for what the team stated about the brand, mined for the specific fact, the decision, the exact phrase.

Treat it by kind. A claim made in a conversation is **stated**, not verified. Carry it as the team's word, quoted with its author and date, until another source confirms it. Where a past conversation contradicts what the live data, the account, or the site actually shows, the conflict is the finding: surface it plainly and follow the evidence, and never launder a chat claim into a verified fact. And never let the team's own words in a chat stand in for the customer's; this source is the team on the brand, not voice-of-customer.

**If there are no past conversations, note it in one line and run as normal.** This source sharpens the doc. It is never a gate. A brand whose team never touched the web app still produces the full doc from every other source.
<!-- team-conversations:end -->

## Execution steps

Run in this order.

1. **Confirm the foundation.** List the external audits this synthesis is built from, with their dates. Name any audit that is missing or thin. A missing audit is a foundation gap and becomes an open loop on this synthesis, not a section to fabricate.

2. **Read every upstream audit in full.** Synthesis is impossible until you hold the whole watch list at once. Pay attention to where two audits surface the same pattern from different angles, and to where they contradict.

3. **Surface cross-cutting patterns.** Where a pattern recurs across multiple external audits with real upstream denominators, elevate it. Where it appears in only one audit, hold it as candidate signal.

4. **Resolve cross-audit tensions.** Where two upstream audits point in different directions about the same external account or the same market read, name the tension and hold candidate explanations as candidates. The tension itself is often the finding.

5. **Walk the seven reads this doc owns.** Dead-end positionings, ownable openings, use-case gaps, problem-mirroring lanes, persona archetypes, threat-typed landscape, inspo-and-affinity borrows. Each carries the upstream audits it rests on.

6. **Mark every opportunity as a hypothesis to validate.** No directive. Each opening states the persona it implies, the messaging direction it suggests, and the success signal that would confirm it. The brand's working thesis and customer phase will decide which hypotheses get tested.

7. **Two-sentence diagnosis.** Resolve the synthesis to two sentences: the structural read of where the market sits right now, and the leverage point for the brand. The diagnosis is the spine the rest of the synthesis hangs from.

8. **Consolidate the open loops.** Read every upstream audit's open loops together. Group related loops across audits, elevate the few that matter most to the brand's strategy, and surface them as the unified questions they are.

## Output spec

Open with frontmatter, then the narrative. Mark every claim. Leave clean named blanks where any upstream audit is missing or thin.

```markdown
---
brand: [brand-slug]
doc: gaps-opportunities-inspo
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
built_from: [the external audits and reports this synthesis was built from, with their dates and any foundation gaps named]
---

# Gaps, opportunities, inspo — [Brand Name]

## Two-sentence diagnosis

## Threat-typed competitive landscape

## Dead-end positionings — what not to do

## Ownable openings — conversations no competitor is having

## Use-case gaps from reviews unserved by ads

## Problem-mirroring lanes left open

## Persona archetypes across sources

## Inspo and affinity-borrowed patterns

## Brand-relevant implications held as hypotheses

## Consolidated open-loops roll-up

## Appendix - Parker media links
```

Brand-relevant implications are held as provisional, gated on context. The synthesis surfaces openings; the working thesis decides which to test.

## Open loops

The consolidated open-loops roll-up is this doc's open-loops section. It turns upstream uncertainty into the smallest set of questions that still matter.

Think like a strategist. Ask like a smart 13-year-old. Do the hard thinking silently, then write the loop as a plain question about what Parker still does not understand. Do not dress small gaps in bigger language. Do not copy every upstream loop. Group related questions across audits, notice where two audits raised the same question from different angles, and surface the unified question underneath them. Run every candidate through the same test: if Parker answered this, what would actually change for the brand. Zero to three open loops is normal. Five is the ceiling. Six or more means the consolidation has not happened yet.

Sort the consolidated loops by strategic importance and evidence strength. Do not group them by what closes them inside this doc; closure path belongs to the later grading, promotion, hypothesis, or validation run.

Write each consolidated loop with the observation and the exact question. Do not include "what would close it," a research path, or a test plan.

## Parker media links appendix

End every context doc with `## Appendix - Parker media links` as the final appendix, after open loops and after any quote, customer-language, source, or evidence appendix. Include every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference that was available during the run and that supports an ad, post, hook, creator example, competitor example, visual source, or source artifact discussed in the doc. Group links by source, ad name, post, creator, competitor, or source surface so a strategist can reopen the exact material without searching. Preserve the original link or path exactly. If no Parker media links or media references were available, write `No Parker media links were available in this run.` Do not invent links, shorten paths, or replace links with descriptions.

This appendix is source infrastructure, not analysis. Do not move open loops into it, and do not count the appendix as a recommendation section. The body of the doc still needs narrative reconstruction of every important visual source; the appendix simply keeps the media handles attached at the bottom.

## Common mistakes to avoid

- Concatenating the upstream audits into parallel summaries. The value is the connections, not the recap.
- Presenting an opening as a directive rather than a hypothesis. The brand's working thesis decides what to test.
- Laundering an upstream inference into a settled fact by failing to carry the mark.
- Synthesizing across a missing or thin upstream audit. Name the gap.
- Surfacing every absence as an opportunity. A consistent absence across the watch list is more likely an opening; a one-rival absence is candidate signal at best.
- Producing a tactic list rather than a two-sentence diagnosis.
- Inflating the consolidated open-loops roll-up with tidy factual gaps from the upstream audits. The roll-up surfaces the few high-stakes consolidated loops, not the union of every upstream loop.

## When you refresh this

Quarterly, regenerated when a meaningful share of the upstream external audits has refreshed. Take the previous version in as context first, alongside the refreshed upstream audits. Carry forward the through-line, update what the refreshed audits and new market signals changed, re-classify the threat-typed landscape if a rival has shifted, and re-read which openings remain open. Pay close attention to the consolidated open-loops roll-up: note which loops have closed and which remain, because the movement of the loops over time is the clearest record of how the read on the market is maturing. Do not rewrite from scratch.
