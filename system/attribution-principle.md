# Attribution — design principle

Updated 2026-05-18.

## The principle

Everything Parker writes into a living doc must carry source attribution. Not just that it was noted, but where it came from. Attribution is first-class metadata, not buried in prose. The UI surfaces it on click or hover for every persistent claim.

Two layers:

- **Quantitative attribution:** confidence, sample size, sources-agreed count, recency
- **Qualitative attribution:** direct quote, conversation reference, URL, exact ad pulled, expert insight that triggered the note

## Where attribution applies

- **brand-notes-from-org.md** — every claim about how the org uses Parker, what success looks like, etc.
- **brand-notes-from-user.md** — every observation about how this user works
- **user-profile.md** — every preference and rule extracted from chat
- **parker-ideas.md** — every cross-brand pattern, every strategic claim, every ad worth stealing
- **personas-profile.md** — every persona claim, identity layer, and behavioral signal
- **voice-of-customer.md** — every snippet, traced to the specific source artifact that produced it
- **Open loops** — most important. Which scrape, which date, which ad or conversation or observation triggered it
- **Hypotheses** — what evidence motivated the prediction
- **Validations** — what sources were checked, what they said, with direct quotes

## Chat log retrievability

For memory specifically, attribution must include the ability to pull the actual chat log. Not just a reference, but the underlying messages.

A strategist seeing a memory claim should be able to click the source and see the exact conversation excerpt that produced it.

Implications:

- Attribution metadata stores message IDs, not just conversation IDs
- The backend exposes a query path from a memory claim back to the underlying messages
- The UI affordance is a modal or side panel with the relevant chat excerpt highlighted
- Long-term chat archival must remain queryable down to the message ID, not only summarized. Summarization for context is fine. Underlying messages remain retrievable for attribution.

## Example attribution block for a memory claim

```yaml
attribution:
  - type: chat
    conversation_id: conv_01HXYZ...
    message_ids: [msg_022, msg_023, msg_024]
    snippet: "We tried 'lifter persona' twice — never worked"
    user_id: user_abc
    timestamp: 2026-05-15T14:32:00Z
```

The message_ids field is what enables click-through retrieval.

## Why attribution matters most for open loops

Open loops can multiply quickly. Without attribution, the team cannot tell signal from noise. Attribution makes the pipeline auditable. Every promoted loop traces back to specific evidence, and the team can sanity-check the scoring against the source material.

## Implementation hooks across the roadmap

- **Phase 0:** every doc stores its content plus a structured attribution field, **inline in the markdown** (locked 2026-06-08 — see below). This locks the storage structure that personas, VoC, open loops, memory, and ideas all depend on.
- **Phase 3:** open-loop detection prompts must populate the attribution field, not just the observation.
- **Phase 4:** chat-log retrievability backend. Every memory claim exposes a query path to the underlying messages.
- **Phase 5:** dreaming proposals attach their source set so reviewers can see why Parker is suggesting a change.
- **UX track:** every persistent claim is hoverable or clickable to reveal sources.

## Where attribution metadata lives — LOCKED 2026-06-08

Attribution lives **inline in the markdown doc itself**, not in sidecar files. Sidecar is rejected. The decision was between inline and a paired sidecar file; inline wins because it survives file moves, stays greppable, needs no join to read provenance, and matches the pattern the templates already use.

Two inline placements, by altitude:

- **Doc- or section-level provenance** lives in a yaml block — frontmatter for whole-doc provenance, an end-of-section yaml block for per-section provenance. The reference implementation already exists: the `sources_used` / `sources_available_but_unused` / `confidence` block in `templates/personas-template.md`, and the frontmatter `sources_synced` block plus per-snippet attribution in `templates/voc-template.md`. New and revised docs follow that shape.
- **Per-claim provenance** travels with the claim, inline, not buried in prose. Quantitative attribution (confidence, sample size, sources-agreed, recency) and qualitative attribution (quote, conversation reference, URL, exact ad, triggering expert insight) attach to the claim they justify.

Doc bloat is the accepted cost. It is mitigated by keeping per-claim blocks terse and rolling shared provenance up to the nearest section or frontmatter block rather than repeating it on every line.

The one piece this does not yet build is message-level chat-log retrievability — the `message_ids` click-through described above. That stays Phase 4 backend work. Inline markdown attribution carries the conversation reference; the query path down to individual messages is added later and does not change the inline storage decision.
