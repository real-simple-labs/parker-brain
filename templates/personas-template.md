# Template — personas-profile.md

Updated 2026-05-18.

Copy-paste template for the persona one-pager. Personas are durable identities. Behavioral signals are situational overlays attached to a persona that can swap without rebuilding the persona.

---

## personas-profile.md

```markdown
---
brand: [brand-slug]
last_updated: YYYY-MM-DD
sources_synced:
  - customer-reviews: YYYY-MM-DD
  - ad-account: YYYY-MM-DD
  - ad-comments: YYYY-MM-DD
  - post-purchase-surveys: YYYY-MM-DD
  - brand-reputation: YYYY-MM-DD
  - reddit: YYYY-MM-DD
  - other-reviews: YYYY-MM-DD
persona_count: [integer]
flagship_persona: [persona-slug]
---

# Personas — [Brand Name]

## How to read this doc

Each persona below is an identity. An identity is a durable self-conception that should still describe the same person years from now. Trigger events and life-stage states are not personas. They are behavioral signals attached to a persona, captured in a separate sub-block so they can swap without forcing a rewrite of the persona itself.

When generating customer-facing work, pick the relevant persona for voice and identity, then layer the active behavioral signal or signals for what is salient right now.

## Cross-persona bias notes

This section surfaces where marketer bias may be distorting the picture. The framing is from Sarah Levinger: marketers tend to create the customer they are biased toward, so the signal in the data can be partly self-generated. Name the divergences so the team can sanity-check.

- **Brand-self echo:** Phrases or themes that only began appearing in customer language after the brand introduced them in marketing. These should be treated as low-confidence until they appear in unprompted channels.
- **Vocal minority risk:** Segments that are loudest in surveys, reviews, or social, but underrepresent purchase volume. Name the segment and quantify the gap between voice share and revenue share.
- **Stated-vs-revealed divergence:** Places where survey answers contradict observed purchase behavior. Name the contradiction and identify which source to trust for which kind of decision.
- **Sources that disagree:** Places where one source type points one direction and another points the opposite. Explain the likely reason for the disagreement.

---

## Persona 1: [Acronym + Name] — flagship

A single sentence describing who this person is in the world.

### Identity

- **Core identities:** The durable self-conceptions this person holds across contexts and across years. List the 2-4 that are most stable and most predictive of behavior. Anchor each one to evidence in the sources.
- **Contextual identities:** Self-conceptions that activate only in specific environments or social situations. These are stable identities, not trigger events. They differ from core identities in that they only show up under certain conditions. Name the condition that activates each one.
- **Outward vs real:** The places where this persona's publicly-presented identity diverges from their purchase-self. Anchor to a concrete behavior pattern in the sources where the customer claimed one thing and did another.

### Behavioral signals (currently observed)

Situational states that are active in some portion of this persona right now. These are not what defines the persona. They are overlays that shift what is salient at the point of purchase or engagement. Update this block as the customer base shifts. Do not let signal additions or removals trigger a rewrite of the persona itself.

For each signal, capture:

- The signal name in slug form
- A one-sentence description of the situational state
- The percent of this persona estimated to be in this state, with the source the estimate comes from
- The behavioral implications of the state

Aim for 3-6 signals per persona. Fewer means undercaptured. More often means signals are being conflated with identity.

### Voice signature

A single sentence describing how this person talks at a glance. Detailed phrases live in voice-of-customer.md, tagged with this persona's identity slug.

### Day-in-the-life

A short narrative from wake to bed. What this person consumes, who they talk to, and where the brand category enters their day. Anchor to behavioral evidence from the sources. The goal is to ground the persona in observed behavior rather than demographic stamps.

### What activates purchase

- **Trigger pattern:** What is observed to be happening in the customer's life when they actually buy. This is the revealed-behavior version of the trigger, not the self-reported version.
- **Stated reason vs revealed reason:** Where surveys and behavioral evidence diverge on the cause of purchase. Name both sides and identify which is load-bearing for marketing decisions.
- **Friction at the close:** What stops this persona at the final step of purchase, based on cart-abandonment, support tickets, and pre-purchase objection language in reviews.

### What we believe vs what we observed

- **High-confidence claims:** Claims about this persona that appear consistently across three or more source types. List each with the source count.
- **Single-source claims:** Claims that appear in only one source type. These may be real but require corroboration. List each with the source.
- **Common team assumptions the data does not support:** Things the team believes about this persona that the sources cannot verify. Surface these explicitly so the team knows where their picture is unbacked.

### Awareness and market sophistication

Where this persona sits on the classic awareness stages and on the sophistication level of the category they buy in. The point of capturing this is durable: a problem-aware persona in a saturated category needs a different shape of message than a product-aware persona in an early category, and that difference holds for years.

- **Awareness stage:** Problem-aware, solution-aware, or product-aware, with the evidence in the sources that anchors the call. Note any persona that splits across stages and the condition that determines which side they land on.
- **Market sophistication:** The sophistication level of the category as this persona experiences it, read against the competitive field. When many brands in the category make the same claim, this persona rewards specific receipts over generic promises. Name what counts as a specific receipt for this persona.
- **Implications for message:** What the awareness and sophistication read together imply for how to open with this persona. Hold this lightly — it is a shape, not a script.

### Message signals, frequency-ranked

The messages that actually drive this persona's purchase, ranked by how often they recur across the sources. This is where the biggest bet for this persona is identified, and where the brand's current emphasis can be checked against what the customer evidence actually supports. The brand often over-indexes on a message that ranks lower than it thinks.

For each ranked message, capture:

- The message in a short phrase, in the customer's own framing where possible
- The source types that surface it and the rough recurrence weight
- The persona's expression of it, since the same message lands differently on different personas
- Whether the brand currently leads with it, trails it, or misses it entirely

### Attribution

```yaml
sources_used:
  - type: customer-reviews
    last_pulled: YYYY-MM-DD
  - type: post-purchase-surveys
    last_pulled: YYYY-MM-DD
  - type: reddit
    last_pulled: YYYY-MM-DD
  - type: ad-account
    last_pulled: YYYY-MM-DD
  - type: ad-comments
    last_pulled: YYYY-MM-DD
  - type: brand-reputation
    last_pulled: YYYY-MM-DD
  - type: other-reviews
    last_pulled: YYYY-MM-DD
sources_available_but_unused: [list of source types that exist for the brand but did not contribute evidence to this persona]
confidence: [one of: strong, mixed, thin, hypothesis]
```

List only the sources that actually contributed evidence. The `sources_available_but_unused` field is important. A source that exists for the brand but yielded nothing for this persona is itself a signal worth surfacing, because it may indicate that the persona does not engage on that channel or that the persona is not well-represented in that source.

---

## Persona 2: [Acronym + Name] — secondary

Same structure as Persona 1.

---

## Persona 3: [Acronym + Name] — secondary

Same structure.

---

## Persona 4: [Acronym + Name] — emerging

Use the emerging slot for identity clusters that are showing up in the sources but do not yet have flagship or secondary status. These are candidates for next-quarter focus.

Same structure as Persona 1, with one addition: an explicit note describing what would move this persona up the ranking, expressed as evidence thresholds rather than calendar time.

---

## What we're watching

- **New behavioral signals emerging:** Signals showing up in the last 30 days that were not present in prior periods. Note which persona each signal is attaching to and where it was detected.
- **Behavioral signals fading:** Signals that used to be active in the customer base but are now declining. Surface these because a fading signal can be an early indicator that the persona itself is shifting underneath.
- **Potential new persona forming:** Identity clusters that do not fit any existing persona. Capture the cluster's distinguishing identity traits and which sources are surfacing it.
- **Personas suspected to be bias artifacts:** Personas the team historically targeted that the source data does not actually support. Flag for retirement or downgrade with the evidence.
```

---

## Conventions

### Persona identity slugs

Slug format is kebab-case. Each slug describes the durable identity. Slugs must read as identities, not as life stages or roles in a transaction.

This document is the canonical home of identity slugs for the brand. voice-of-customer.md references these values and must not introduce new identity slugs without them being added here first.

### Behavioral signal slugs

Slug format is kebab-case. Each slug describes a situational state that activates an identity in a specific way. Slugs must describe the state, not the persona.

This document is the canonical home of behavioral signal slugs for the brand. voice-of-customer.md references these values and must not introduce new signal slugs without them being added here first.

### Persona confidence

The per-persona `confidence` field is one of four values. The intent is directional, not precise. Confidence reflects how grounded the persona is in observed customer evidence at the time of writing.

- **strong**: Patterns backing this persona's core identity claims appear consistently across most of the source types that exist for this brand, and the supporting evidence is recent.
- **mixed**: Patterns backing this persona appear in some sources but not others, or sources agree on the core identity but disagree on secondary claims, or the supporting evidence is starting to age.
- **thin**: Patterns backing this persona appear in only one source type, or sources contradict each other on the core identity, or the evidence has aged significantly.
- **hypothesis**: The persona is asserted without supporting evidence from the brand's own customer-facing sources. Used when a brand is too new to have generated sources of its own, or when proposing an emerging persona before any source can corroborate it. The persona is reasoned from external signal rather than observed in the brand's customer base.

The confidence value is judged against what is available for this brand, not against an absolute threshold. A brand-new brand with only one source available can have a `strong` persona if the available source converges cleanly on the identity. A mature brand with seven sources available will need broad agreement to reach `strong`.

A persona at `thin` or `hypothesis` should not drive flagship-level strategy without an explicit override that names the reason and the expected validation path.
