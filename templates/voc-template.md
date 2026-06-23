# Template — voice-of-customer.md

Updated 2026-05-18.

Copy-paste template for the VoC database. Structured snippet store organized by category. Each snippet carries an identity tag, an optional behavioral signal tag, recurrence, source attribution, and a brand_self_echo flag.

Identity slugs and behavioral signal slugs are defined in personas-profile.md. VoC references those values and never introduces new slugs.

---

## voice-of-customer.md

```markdown
---
brand: [brand-slug]
last_updated: YYYY-MM-DD
sources_synced:
  - customer-reviews: YYYY-MM-DD
  - ad-comments: YYYY-MM-DD
  - post-purchase-surveys: YYYY-MM-DD
  - brand-reputation: YYYY-MM-DD
  - reddit: YYYY-MM-DD
  - other-reviews: YYYY-MM-DD
  - ad-account: YYYY-MM-DD
snippet_count_total: [integer]
category_counts:
  pain_phrase: [integer]
  outcome_phrase: [integer]
  metaphor: [integer]
  objection: [integer]
  aspirational: [integer]
  trigger_moment: [integer]
  surprise_delight: [integer]
  category_jargon: [integer]
  anti_language: [integer]
---

# Voice of Customer — [Brand Name]

## How Parker uses this library

At execution time, customer-facing skills load this library. The skill picks an identity tag for the persona being targeted and an optional behavioral signal tag for the situational state that is currently active. The identity tag drives voice consistency. The behavioral signal tag drives which salient pain or trigger to mirror in this specific moment.

Confidence weighting: prefer snippets with higher recurrence and broader source diversity. Treat single-source snippets as candidates rather than canon.

Flag any snippet where brand_self_echo is true. These phrases entered customer language only after the brand introduced them in marketing. They are low signal and high risk of marketing to ourselves.

---

## Pain phrases

What the customer says about the problem in their own words, before they have encountered the solution.

Each entry is a YAML block with the following fields:

```yaml
- snippet: [the verbatim phrase the customer used]
  category: pain_phrase
  identity_tag: [identity slug from personas-profile.md, or null if universal]
  behavioral_signal_tag: [signal slug from personas-profile.md, or null if not situation-specific]
  source:
    type: [one of: review, ad-comment, post-purchase-survey, brand-reputation, reddit, other-review, ad-account]
    platform: [the specific platform within the source type]
    review_id: [the platform-native identifier]
    date: YYYY-MM-DD
    url: [direct link to the source artifact]
  recurrence: [count of times this phrase or near-paraphrase appears across the source corpus]
  source_diversity: [list of source types this phrase appears in]
  first_seen: YYYY-MM-DD
  last_seen: YYYY-MM-DD
  confidence: [one of: strong, mixed, thin]
  brand_self_echo: [true or false, per the flag rules at the bottom]
  notes: [optional free text. Use this field to capture context that the structured fields cannot, especially when a snippet's confidence or echo status needs explanation]
```

---

## Outcome phrases

What the customer says after the product has worked. Capture the language they use to describe the result, the change in their life, and the emotional shift. Same YAML schema as pain phrases.

---

## Metaphors

How the customer analogizes the product, the problem, or the outcome. Metaphors are especially important because they reveal which mental model the customer uses to make sense of the category. Same YAML schema. Pay attention to brand_self_echo. Metaphors are the category most likely to be brand-taught rather than customer-organic.

---

## Objection phrases

Pre-purchase doubts the customer expressed in their own words. Capture both the surface objection and the underlying concern when the source contains both. Same YAML schema.

---

## Aspirational phrases

Statements about who the customer wants to become, or what they want their life to look like after the purchase. Distinct from outcome phrases: aspirational phrases describe a desired future state at the point of consideration, while outcome phrases describe the realized state after purchase. Same YAML schema.

---

## Trigger moments

What was happening in the customer's life at the moment they decided to buy. These are situational moments that activated an existing identity, not personas themselves. Same YAML schema. The behavioral_signal_tag field is especially important here and should rarely be null.

---

## Surprise/delight phrases

Unexpected positives the customer surfaces about the product or experience. These are valuable because they reveal value the brand may not be marketing on. Same YAML schema.

---

## Category jargon

Insider language for the category. Signals fluency. Capture the term and the conditions under which the customer uses it. Same YAML schema.

---

## Anti-language

What the customer explicitly hates about competitors, category messaging, or marketing tropes. This tells Parker what not to say. Same YAML schema.

---

## What's emerging

Phrases first seen in the last 30 days, with recurrence at or above 3. Surface these as candidates. They may indicate a new pain emerging, a competitor shifting messaging, or a new behavioral signal forming in the customer base.

For each emerging snippet, capture:
- The snippet text
- The first-seen date
- The source diversity at this point
- A provisional confidence
- A note on what might explain the emergence

## What's fading

Phrases that previously recurred but have not appeared in the last 60 days. Surface these for archive or demotion.

For each fading snippet, capture:
- The snippet text
- The last-seen date
- A hypothesis for why it may be fading

## Flagged for review

Snippets that meet any of these conditions:

- brand_self_echo is true and recurrence is high. The brand may be leaning on language it taught customers rather than language customers brought to the relationship.
- Single-source snippets that the team is treating as canonical. These should be verified before relying on them in production copy.
- Snippets with low source diversity but high recurrence in one channel. These could be vocal-minority artifacts rather than organic pull.
```

---

## Conventions

### Snippet confidence

The per-snippet confidence field is one of three values. The intent is directional, not precise. Confidence reflects how grounded the snippet is in observed customer language at the time of writing.

- **strong**: The phrase or close paraphrase appears across multiple source types for this brand, recurs at a rate that is notable relative to the brand's overall volume, and has appeared recently.
- **mixed**: The phrase appears in one source type with meaningful recurrence, or in multiple source types but only sporadically, or has been declining in recent activity.
- **thin**: The phrase appears once or rarely, in a single source type, has not been corroborated elsewhere, or is flagged as brand-self echo and should be treated as candidate language rather than canon.

Confidence is judged against what is available for this brand, not against an absolute threshold. A brand with only one source available can still have strong snippets if a phrase recurs heavily in that source. A brand with seven sources available needs cross-source presence to reach strong.

Snippets at thin confidence should not be used as primary copy and should appear in the Flagged for review section.

### brand_self_echo flag

Set to true when any of the following conditions hold:

- The phrase first appeared in customer language after the brand began using it in its own outbound marketing.
- The phrase's recurrence tracks the brand's creative refresh cycle, spiking when new creative ships and decaying as the creative ages.
- The phrase only appears in channels where the brand has surface-level control over the language environment, and is absent from channels where customers speak without any brand prompt.

When brand_self_echo is true, do not use the snippet as primary copy without an explicit override. The snippet should appear in the Flagged for review section.

### identity_tag and behavioral_signal_tag

Both fields reference slugs that are canonically defined in personas-profile.md. VoC references those values. VoC never introduces a new slug. If a snippet requires a new tag, the new identity or signal must first be added to personas-profile.md.

- identity_tag null means the snippet is universal across personas and represents brand-level language.
- behavioral_signal_tag null means the snippet applies to the identity broadly and is not specific to any situational state.
- A snippet that belongs to multiple identities should be entered once per identity, duplicating the snippet record with a different identity_tag each time. This keeps querying simple. Revisit this convention when scale forces a change.
