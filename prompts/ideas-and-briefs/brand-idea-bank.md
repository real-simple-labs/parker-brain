# Spec - brand idea bank

This specifies the brand idea bank, Parker's living idea memory for one specific brand. The idea bank holds the ideas circulating in Parker's head for that brand: references from competitors, inspiration sources, organic videos, expert content, context docs, user conversations, manual saves from the ideas tab, customer language, and Parker's own observed patterns.

Doc type: brand memory database spec plus capture, backfill, and maintenance prompts. Scope: one idea bank per brand. Cadence: capture is continuous; backfill runs when a brand file is created or rebuilt; curation runs monthly.

---

## Purpose

The brand idea bank exists because strategy work should not lose the ideas Parker notices along the way. A monthly audit may surface a great hook mechanic. A user conversation may name a promising concept. A competitor ad may reveal a useful proof pattern. A manual save in the ideas tab may capture a creative direction the team wants to preserve.

The idea bank is the place those ideas live until they are used, rejected, or retired. It is not a strategy doc and it is not a concept brief. It stores the source-backed idea and why Parker thinks it is worth holding.

This is the ideation layer, and ideation is not concepting. Ideation is the always-on playground where half-baked ideas get logged the moment they are noticed; concepting is the separate, dedicated work of pulling from that bank and building one idea out into a brief with variations. The idea bank holds the first and never the second. Its whole purpose is that a strategist should never concept from a blank page — they walk into concepting with a ranked bank to choose from rather than three hours of scouring. The full reasoning behind what an idea is, where ideas come from, and what makes one worth keeping lives in `global/knowledge/creative-strategy/ideation-and-brainstorming.md`; this spec is how that reasoning is stored.

## Storage and access

Each brand gets a first-class idea bank at:

`z-brands/[brand]/idea-bank/`

The folder contains:

- `README.md` - how to use the brand's idea bank.
- `index.md` - the searchable list of active ideas.
- `entries/[YYYY-MM-DD]-[concept-slug].md` - one idea per file.

Entries can also be mirrored into team taste files or pulled from global expert signals, but the brand-level idea bank is the canonical home for brand-specific ideas.

## Source surfaces

Parker should maintain the idea bank from these sources:

- Customer language. Reviews, survey responses, community posts, and the exact words customers use. This is the bread and butter for concepting, so customer-sourced ideas take priority over everything else.
- Old print ads and historical advertising. The strategist's gold mine, especially for statics, because nothing is new under the sun and the craft in old headlines and visuals outclasses most modern feed content. Adapt the shape of a strong old line or layout to the brand.
- Organic video and social research. The high-level idea, messaging, hook, or format pulled from a scroll, not only full concepts worth a one-to-one adaptation.
- Affinity brand paid ads. Brands close in nature to the product but not direct rivals, weighted above direct competitors because copying a competitor is rarely a novel way to scale.
- Competitor snapshots and competitor paid ads. The hooks and angles a rival is testing that could be adapted and run differently, kept with a note on how Parker would run it differently so it is never replicated one to one.
- The natural world and offline observation. A print ad on the subway, a phrase a stranger uses, a line from a friend, a hook the human brain produces in silence with a notebook.
- Brand sub-context docs, source pulls, and research extracts.
- Monthly and quarterly audits.
- Parker MCP ad data and creative reads.
- Expert signals routed from the expert signal database.
- User conversations with Parker.
- Manually saved ideas from the ideas tab.

The source can be missing a link when the idea comes from a conversation, an offline observation, or internal Parker observation. In that case, preserve the conversation reference, source doc path, or idea-tab ID, and describe the source well enough to retrieve it.

## Entry schema

Each idea-bank entry carries these fields.

- **concept_name** - short memorable name for the idea.
- **idea** - the reusable idea in one clear paragraph.
- **source_link** - link to the source when available.
- **source_path** - local doc path or Parker source reference when the idea comes from Parker work.
- **parker_media_links** - every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference available for the source. Preserve each link or path exactly. If no Parker media links or media references were available for the entry, write `No Parker media links were available for this entry.`
- **source_type** - competitor ad, inspiration ad, organic video, expert content, customer language, community post, user conversation, ideas tab save, internal Parker observation.
- **source_name** - brand, creator, expert, user, or doc that produced the idea.
- **date_added** - when the entry entered the idea bank.
- **winning_elements** - the parts worth saving, using tags such as hook, visual, script, headline, format, offer, angle, proof, pacing, creator, product demo, comment mechanic, emotional frame.
- **source_read** - narrative description of the source or idea. For visual sources, describe what happens in order so the reader can picture it without seeing it.
- **justification** - why this idea earned a place. For competitor ads, include running time, top impression status, spend signal, repetition, or placement when available. For organic videos, include views, engagement, comment energy, or visible cultural traction when available. For expert content, include credibility, recency, and tactical specificity. For user-saved ideas, preserve why the user saved it if known.
- **stage_of_awareness** - unaware, problem aware, solution aware, product aware, or most aware.
- **persona_or_audience_fit** - who this idea appears built for inside the brand's audience map.
- **brand_fit** - why this belongs near the brand, or what makes it risky.
- **notes** - caveats, open questions, adjacent ideas, and retrieval notes.
- **status** - raw idea, worth testing, adapted into concept, used, rejected, stale.

## Capture bar and qualifiers

The bar for the idea bank is lower than the bar for a concept, on purpose, because this is ideation and ideas do not need to be complete to be logged. A hook, a format, a storyline, a single line of customer language, or a visual is enough to capture when something about it resonates, as long as the entry records what was liked and why. Half-baked is the normal state of an idea-bank entry.

Capture runs in two modes, and they hold different bars.

- In a dedicated ideation session, the doors are open and Parker logs liberally. The job is to notice and record, not to filter.
- During other work, when Parker is running a context doc, an audit, or a research pass whose real job is something else, capture is incidental and selective. Log only the genuinely reusable idea the pass happens to surface, and leave the capture empty rather than padding it. Most analytical passes surface no reusable idea, and that is fine.

What makes an idea worth keeping is judgment, not a clean threshold, and the evidence differs by source.

- For paid sources, spend is the strongest signal that a concept is performing, and impression rank gets closer to it. But weigh the launch date against the count, because a newly launched ad has low impressions for lack of spend, not for lack of merit. Treat the read as an assumption.
- For organic sources, views and engagement are the confidence signal. Higher numbers raise priority; lower numbers lower confidence without disqualifying the idea.
- For old ads and offline finds, the signal is craft and durability rather than a metric, so justify these on the strength of the headline, the visual, or the structure.

The deepest qualifier is the brand's goal and the state of its account, because what counts as a good idea is relative to both. An idea that fits an awareness goal can be wrong for a brand that needs sales now. A blank-slate account has a low bar and a wide-open field, while a mature account that has tested everything forces a far more granular bar. Where the goal or account state is known, weigh the idea against it; where it is not, capture the idea and note that the fit is unverified.

## Capture prompt

Run this whenever Parker notices a brand-relevant idea in research, a user conversation, a manual idea save, a monthly audit, an expert signal, or a source pull.

You are deciding whether one idea belongs in the brand idea bank. Save it only if it gives Parker a reusable creative or strategic pattern for this brand.

First, name the idea. The concept name should be short enough to recall later and specific enough to distinguish it from similar ideas.

Second, describe the source as if the reader has never seen it. If it is a video, ad, or visual post, write the source_read as a narrative. Move through what appears on screen, what is said, what text appears, and what the viewer understands from the sequence. Do not reduce the source to a label.

Third, identify the winning elements. Tag the parts Parker should remember. The tags should explain what made the source worth saving, not what the brand should copy.

Fourth, tell the research story and carry the evidence picture. Treat the entry as context another LLM or strategist may read before concepting from the idea. The entry should show what source was reviewed, what reusable pattern was noticed, what exact line, visual, behavior, or source detail made it worth saving, how representative or thin the evidence is, and what uncertainty remains.

Fifth, preserve the media handles. Fill `parker_media_links` with every Parker media link, media file path, thumbnail path, video URL, ad-library link, post link, source URL, or media reference that came with the source. Preserve the original link or path exactly. If none were available, write `No Parker media links were available for this entry.`

Sixth, write the justification. Tie it to evidence from the source. Use ad performance signals, running time, impression rank, spend, repetition, organic views, comment energy, expert credibility, user save behavior, or repeated appearance across context docs when those signals are available. If the evidence is thin, mark it as thin.

Seventh, assign stage of awareness and audience fit. These are inferences. Mark uncertainty in the notes instead of pretending the fit is proven.

Output the entry in the schema's shape.

## Backfill prompt

Run when a brand idea bank is first created or when a brand's context has materially changed.

You are backfilling a brand idea bank from the brand's existing context. Read the brand profile, sub-context docs, source pulls, competitor docs, monthly audits, and saved user conversations available to Parker. Pull only ideas that are specific enough to be useful later.

For each candidate, ask whether Parker would want to retrieve this idea during hooks, scripts, headlines, briefs, audits, or concept generation. If the answer is no, do not save it.

Prioritize source-backed ideas with a clear winning element. Do not backfill generic observations. Do not turn every finding into an idea-bank entry.

Create entries, then update the brand idea-bank index with concept name, source type, winning elements, stage of awareness, status, and source path.

## Maintenance prompt

Run continuously during Parker work and monthly during curation.

During normal work, add an idea-bank candidate when an idea is explicitly saved by the user, when a user says to remember an idea, when a source contains a reusable creative pattern, or when Parker notices a repeated pattern across brand docs.

During monthly curation, merge duplicates, mark stale ideas, promote strong ideas to worth testing, and mark used ideas when they have become concepts, scripts, briefs, or ads. Preserve rejected ideas when the reason teaches Parker a brand boundary.

## Critical rules

1. Do not write how the brand should run competitor, inspiration, or affinity hooks inside the source entry. Adaptation belongs in future concept-generation, grading, and strategy runs.
2. Preserve the source-backed idea, the winning elements, the justification, and the awareness-stage read.
3. Manual saves from the ideas tab should enter the idea bank unless the user marks them as throwaway.
4. User conversations can create entries when the idea is durable enough to retrieve later.
5. Source links are preferred but not required when the source is a conversation, Parker MCP result, or local context doc.
6. Use narrative reconstruction for videos, ads, posts, and visual examples.
7. Keep weak evidence visible. A thin but interesting idea can be saved as raw idea, but it cannot be treated as proven.
8. An idea-bank entry is one idea, not a concept. Do not build out variations, a full storyline adapted for the brand, or a brief inside an entry. Adapting the idea to the brand and creating the two or three variations Meta needs is concepting work that happens later. A storyline is close to a concept and a hook is the start of one, while a format alone is not a concept because it carries no message. Capture each as the idea it is and leave the build for the concepting stage.
9. An entry must be a fresh angle to target, not a restatement of what the brand already knows or already runs. The idea bank is for new messaging, visuals, angles, hooks, and formats a strategist could go act on, never for the brand's existing known assets. An award, a collaboration, a channel, or a credibility marker the brand is already advertising is already known, so logging it hands the strategist nothing to test, and the entire point of ideation is to find the directions the brand is not already going. Apply this hardest when capturing from a doc about the brand's own reputation, identity, or ad account, where the temptation is to log the brand's current story back to itself. Before saving, ask whether this would give a strategist a new direction or merely repeat what is already in the brand's ads, and if it is the latter, do not save it. An authority moment earns a place only when the brand has genuinely not used it yet.
