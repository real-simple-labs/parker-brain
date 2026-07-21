# Scenario C — Audience Expansion

**New persona, audience-breaking SKU.**

The brand exists and has real authority somewhere, but this new audience does not yet recognize the brand as theirs. Treat it like a near-cold launch in the new persona's world. Mode 3 thinking: the brand introduces itself in this audience's terms, not its own.

This is the slowest of the three to write, the highest-stakes if the voice is wrong, and the most likely to fail. It requires the most upfront persona work and the most genuine invention.

## The posture

The existing brand voice may not apply. The existing winning angles likely do not transfer. The existing UGC may actively work *against* the ad if it features the wrong audience — footage of the original audience telegraphs to the new one that this brand is not for them.

*A brand known for head-shaving products launches a razor bundle for women's legs and body. The existing male-focused voice and creative will not land with a woman solving a leg-shaving problem. The ad has to start in her world: how women in this category talk about shaving, what objections they hold about a men's grooming brand crossing over, what proof they actually trust. Barbershop tone and locker-room jokes torch the ad before it has a chance.*

*The opener lives in her problem — "if you've ever tried to shave your legs and ended up with bumps you can see for a week, this is for you" — and only then earns the brand's right to be in the conversation: "the engineering that made [X] work for [original audience], now built for legs."*

## The persona gate — this does not start without it

**Stop before writing.** The new audience's persona is a required input to every downstream step, not a nice-to-have. Work down this list in order:

1. **The brand's own persona vault.** Check `personas/` and `sub-context-docs/` for an existing persona covering this new audience. A brain that has run persona work may already have it.
2. **The persona prompt tree.** If nothing covers the new audience, run `parker-system/prompts/personas/` — the gold-layer synthesis is `personas-profile.md`, supported by `persona-voice-library.md` for how they actually talk. The method behind it is `parker-system/creative-strategy-context/persona-research-and-creative-strategy-process.md`.
3. **The mini-brief fallback.** If neither is available, ask the user three questions inline, then flag that a full persona pass is recommended before scaling spend:
   - **Who is this for**, specifically? Not "women" but the segment and the need — "women who shave their legs and keep getting razor bumps."
   - **What is their core problem, in their own words?** Their language, not the brand's category language.
   - **What would make them trust this product?** Which proof types land with *them*, which is often not what lands with the existing audience.

Whichever path produced it, the persona output needs to carry: the avatar, their problem language, their objections (especially their objection to a brand that did not start in their world), the proof types they actually trust, and voice samples.

Scenarios A and B get a light persona refresh — encouraged, not blocking. Scenario C is blocking. **A Scenario C launch done fast is usually a launch done badly.** If the brand is rushing, push back gently and get the persona locked first.

## Angle set

Produce **three to five fresh persona angles, built from scratch in the new audience's voice.** Cover at minimum:

- **A problem angle** — their pain, in their words, from the persona's problem language.
- **An identity angle** — this is for someone like you. The new audience needs to see themselves in the frame.
- **A social proof angle** — people in *your* world are using this. Not the original audience's world.
- **An objection-handling angle** — "isn't this for [other audience]?" The objection is real and it is better answered than avoided.

**Do not reuse existing-persona hooks.** Not as a starting point, not "adapted," not as inspiration. This is the single most common Scenario C failure and it is usually committed out of habit rather than decision — the existing hooks are right there, they are proven, and they are proven *for a different audience*.

## Script moves

- **Persona-first hook in the new audience's language.** Not the brand's existing tone. The first three seconds establish that this ad knows who it is talking to.
- **Objection handler up front.** "You might know us for [X] — here's why this is for you." Naming the mismatch early defuses it; leaving it unnamed lets it sit under the whole ad.
- **Re-pitched brand authority.** Translate what made the brand credible in its original world into language and signals *this* audience values. The engineering, the manufacturing, the years of practice — the substance often transfers even when the relationship does not.
- **"Made for [audience], not adapted from [old audience]"** — only if true, and only if it can be substantiated. If the product genuinely is a re-badge, this line is a lie the audience will find.
- **Social proof drawn from the new audience** — beta users, pre-launch testers, creators from the new audience's world. Existing customers from the original audience are worse than no proof here.

## Proof

The hardest proof position of the three, because almost nothing inherits cleanly.

- **Existing reviews and UGC generally do not transfer,** and featuring the original audience can actively hurt. The exception is proof about *the brand* rather than the product-for-this-audience — manufacturing quality, service, founder credibility — which can carry if it is framed as brand character rather than category authority.
- **Beta testers and pre-launch users from the new audience are the highest-value proof available.** Worth pursuing before launch specifically because nothing else fills the gap.
- **Demo-as-proof carries well** here, because a demonstration is audience-neutral — the product working is the product working.
- The mechanism re-pitch is honest proof when true: the engineering that solved the original problem is real, verifiable, and transferable in a way that the customer relationship is not.

Full set in `proof-substitution.md`.

## Phase

Warm-audience recapture mostly does not apply — the brand's warm list is the *old* audience, and the new audience has no warm pool yet. If the brand's existing list contains a meaningful slice of the new audience (women already buying the men's product as gifts, for instance), that slice is worth a targeted warm ad. Otherwise this launch starts cold.

## Awareness stage

Usually starts further back than the canonical solution-aware default, because the new persona does not know the brand at all. Problem-aware is the common entry: open in their problem, in their language, then introduce the solution category, then the product, then the brand.

A Scenario C launch to a problem-aware audience is a slower opener than anything else this skill produces. That is correct, not a flaw — the context has to be built before the product can land.
