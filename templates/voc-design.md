# Voice of Customer — design principles

Updated 2026-05-18.

This doc explains why VoC lives where it lives and how Parker uses it. For the doc template itself, see [templates/voc-template.md](templates/voc-template.md).

---

## The principle

A Voice of Customer library is a curated messaging bank of exact phrases, metaphors, and patterns pulled from real customer language. Parker references it at execution time, when generating customer-facing work like scriptwriting, ad copy, email, landing pages, and hooks, so the output speaks the same language as the customer.

## How VoC differs from personas

| Personas | Voice of Customer |
|---|---|
| Who the customer is | How the customer talks |
| Identity, segmentation, day-in-life | Exact phrases, metaphors, jargon |
| Referenced at strategy time | Referenced at execution time |
| Synthesized one-pager plus sub-context docs | Curated library of attributed snippets |

Both pull from the same source docs. They synthesize that raw material in two different directions.

## Sources

Shared with personas, with Reddit called out separately because unprompted Reddit discussion is one of the highest-signal sources for unfiltered customer language.

- customer-reviews.md
- ad-comments.md
- post-purchase-surveys.md
- brand-reputation.md
- reddit.md
- other-reviews.md
- ad-account.md, included because winning ad copy is a signal of what language already converts

## Categories

Working draft. Refine as the first brand populates and the library shape becomes visible.

- **Pain phrases** — the customer's own words for the problem before the product has solved it
- **Outcome phrases** — the customer's own words for the realized result after the product has worked
- **Metaphors** — the analogies the customer uses to make sense of the product, the problem, or the outcome
- **Objection phrases** — pre-purchase doubts the customer surfaced in their own words
- **Aspirational phrases** — the customer's language for who they want to become or what they want their life to look like
- **Trigger moments** — what was happening in the customer's life at the moment they decided to buy
- **Surprise and delight phrases** — unexpected positives the customer surfaced about the product or experience
- **Category jargon** — insider language the customer uses that signals fluency in the category
- **Anti-language** — what the customer explicitly hates about competitor or industry messaging, which tells Parker what not to say

## Attribution requirement

Every snippet in the library carries first-class attribution. Required fields at minimum: the verbatim snippet, the category, source metadata including platform and ID and date, recurrence count, source diversity, first-seen and last-seen dates, confidence value, and the brand_self_echo flag.

The recurrence field is what separates a golden nugget from a one-off review. A phrase that appears many times across multiple source types is a pattern. A phrase that appears once in a single source is noise until it recurs.

## Persona and behavioral signal tagging

People speak in the identity that is active for them at the moment. The voice of a frugal-self mom sounds different from the voice of an aspirational-self professional. VoC snippets are tagged by persona identity so Parker pulls the right voice when generating copy for a specific persona.

A phrase can be tagged to multiple personas if it shows up across segments. The tag distribution itself is signal. A phrase that is universal across personas is brand-level language. A phrase that concentrates in one persona is segment-level language.

Behavioral signal tagging adds a second dimension. Personas are identities, not trigger events. Trigger events are behavioral signals layered on top of an identity. Language varies by both. A caregiver-first parent in the first months postpartum and a caregiver-first parent years later share the identity voice but speak different salient pain and trigger phrases.

VoC snippets carry two tags. The identity tag references which persona speaks this way and is durable. The behavioral signal tag references which situational state activates this language and is optional.

When Parker generates copy targeting a specific persona with a specific behavioral signal active, it pulls snippets matching both tags first, then falls back to identity-only snippets for general voice. This keeps the voice consistent across behavioral signals while letting the salient pain or trigger swap to match what is on the customer's mind right now.

## Parker's edge

Humans cannot read tens of thousands of reviews and pull out language patterns at scale. An LLM can do this continuously. The VoC library should auto-refresh as new source data lands, and surface:

- **Emerging phrases** — new language showing up in the last 30 days that was not there before. May indicate a shift in pain points, a new objection forming, or a competitor stealing mindshare.
- **Fading phrases** — language that used to appear but is not appearing anymore. May indicate that the product has solved a problem, or that a category trend has died.
- **Cross-source agreement** — a phrase that appears independently in multiple source types. High-confidence pull.
- **Brand-self echo** — phrases that only appear after the brand introduced them in marketing. Low-confidence. The brand is teaching customers to talk back, not picking up organic language.

The brand-self echo flag is critical. It is the same chicken-and-egg trap that applies to personas, applied to language.

## How skills reference the VoC library

At execution time, customer-facing skills load the VoC library as a knowledge doc. The skill's strategy or process tells it which categories and which persona tags to pull from. The skill picks the category set that matches what it is generating and the identity tag that matches the targeted persona, then optionally narrows further by the active behavioral signal.

## Cadence

Refresh whenever any source doc refreshes. Emerging phrases shift on a daily timescale. Category jargon shifts on a monthly timescale. The library carries per-snippet first-seen and last-seen dates so age can drive confidence weighting, the same doc-age-awareness principle that applies to context docs.
