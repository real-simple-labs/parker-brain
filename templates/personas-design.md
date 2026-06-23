# Personas — design principles

Updated 2026-05-18.

This doc explains why personas live where they live and how Parker uses them. For the doc template itself, see [templates/personas-template.md](templates/personas-template.md).

---

## The principle

Personas is a first-class one-pager, sibling to brand-profile.md and competitor-profile.md. It is not a sub-doc of brand-profile. It has its own sub-context docs that feed it.

## Sub-context docs that feed personas

- **customer-reviews.md** — first-party reviews from the site and from retailer review surfaces
- **ad-account.md** — top-performing ads, with attention to which messages convert which personas
- **ad-comments.md** — unfiltered reactions on paid social ads
- **post-purchase-surveys.md** — self-reported reasons for buying captured at the moment of purchase
- **brand-reputation.md** — community threads, complaint sites, press coverage, and emergent reputation patterns
- **reddit.md** — unprompted customer discussion in topical communities
- **other-reviews.md** — third-party review surfaces outside the brand's direct control

## Framing inherited from Sarah Levenger

### Brands have many personas, not one

Most brands have a couple dozen avatars in their customer base. One is the current target focus. Several others could open up significant revenue but the brand is not speaking to them. The goal is to identify the main types and draft marketing strategies that silo the brand into each bucket. The goal is not to collapse to a single avatar.

### Naming personas matters

Naming a persona, rather than referring to it by demographic shorthand, makes the persona feel like a real person and signals how much effort went into thinking about them. Clinical demographic stamps describe almost no real people and are almost always rooted in marketer bias rather than observed behavior.

### Identity is the first thing to track

Sarah tracks 5 things when building avatars. Identity is the first and most important. The subconscious makes 95% of purchasing decisions on a daily basis. People are reactive at the point of purchase, not deliberative. Identity is what the subconscious is matching against when a decision happens.

### Identity layers

Each person carries multiple identities at once. Three layers matter:

- **Core identities** are the durable self-conceptions the person holds across contexts and across years.
- **Contextual identities** activate only in specific environments or social situations. They are stable identities, not trigger events, but they only surface under certain conditions.
- **Outward-facing identity versus real identity** is the gap between who someone wants to be perceived as and who they are when money is involved. Sarah's cashmere case study illustrates this. A brand asked customers which fabric they wanted, customers chose the premium answer because it sounded fancy, the brand built the product, and the customers did not buy. The frugal-self showed up at the checkout that the aspirational-self never represented in the survey.

### Personas are identities, not trigger events

A persona must be durable. It should still describe the same person years from now. Trigger events are situational and decay. Building a persona on a trigger forces a rebuild on the timeline of that trigger and misses the underlying who.

A **behavioral signal** is a situational state that activates the identity in a particular way right now. The identity tells Parker how the person talks and what they value. The behavioral signal tells Parker what is salient to them in this moment.

Implication for the persona doc structure: each persona has a stable identity block and a rotating behavioral signal block. Marketing strategies and skill outputs can target the same identity through multiple behavioral signals. Same voice, different salient pain or trigger.

### Marketer bias is the silent killer

Sarah's frame: brands generate marketing, marketing attracts a specific kind of customer, that customer's data becomes the canonical avatar, and the next round of marketing reinforces it. Chicken and egg.

How she audits the team: sit down with each team member individually, never together, and ask who they think the customer is. If everyone says the same thing, the founder's bias has propagated downstream. If answers diverge, the copy team, the ads team, the email team, and the SMS team are each marketing to different people without realizing it.

### The loudest customer is rarely the best customer

Sarah's anecdote: a brand listened to its loudest segment and built everything around them, when the actual core customer was a quieter, larger segment with different needs. Brands often fall into this trap twice before catching it.

## Parker's edge over Levenger's pictorial-survey method

Sarah uses pictorial surveys to bypass conscious bias. Parker cannot run pictorial surveys, but it can triangulate across all source types simultaneously and surface where stated reasons diverge from revealed behavior. The divergence is the gold.

What Parker should explicitly flag in the synthesized one-pager:

- Signals that appear in multiple source types, which indicates real pull
- Signals that appear in only one source type, which may indicate an echo chamber or marketer bias
- Places where stated reasons diverge from revealed behavior
- Places where the brand appears to be marketing to itself, with current customers echoing the brand's own copy back

## File structure

```
z-brands/[brand]/personas/
├── personas-profile.md
├── voice-of-customer.md
├── customer-reviews.md
├── ad-account.md
├── ad-comments.md
├── post-purchase-surveys.md
├── brand-reputation.md
├── reddit.md
└── other-reviews.md
```

Parallel to brand-profile.md with its sub-context docs and to each competitor's profile with its sub-context docs.

## Cadence

To be locked. Post-purchase surveys, ad comments, and customer reviews update continuously. Brand reputation drifts over weeks. Ad account performance shifts in days. Personas is likely the most volatile of the three one-pagers, so the refresh cadence is more aggressive than brand-profile.
