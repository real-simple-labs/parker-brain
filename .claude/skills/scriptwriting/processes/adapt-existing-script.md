# Process — Adapt Existing Script

1:1 structural deconstruction of a single reference script, then brand substitution. The structural skeleton stays — segment count, order, emotional arc, pacing, audio pattern. The brand-specific content changes — product, claims, customer language, voice.

This is the default scripting path. The reference comes from find-reference-ads (which picked the single strongest candidate from Parker's ad databases — internal favorites, Parker favorites, or the global AI-tagged DB, queried via Parker MCP) or from a reference script the user provided directly. The adaptation grounds the output in the brand baseline so the script reads as belonging to this brand.

## Required inputs

- One reference script with full transcript and timing.
- Brand baseline — the brand's existing scripts. The baseline tells you what the brand's pacing, voice, hook patterns, and CTA style look like.
- Brand profile, ICP, voice of customer.
- Compliance constraints.

## Philosophy

The reference is already working. The job is not to redesign it. The job is to understand what makes it work, then tell the same story for the brand using the brand's product, language, voice, and structural fingerprint.

Preserve the structural skeleton. Rewrite every word. Match the brand baseline.

## When to pick

- **Default for any scripting request.** Run find-reference-ads first to pick the strongest reference, then this process with that single reference as input.
- **When the user provides a specific reference.** Skip find-reference-ads and run this directly.

## Execution

### Step 1 — Deconstruct the reference

Break it into beats. Per beat:
- Timestamp range.
- What is said (verbatim).
- What is shown.
- The emotional arc beat — opening tension, proof reveal, transformation, close.
- The audio pattern — music shifts, dialogue intensity, SFX moments.

### Step 2 — Identify the structural skeleton

Extract:
- Segment count.
- Pacing pattern (cuts per beat, energy progression).
- Proof type (testimonial, demonstration, before-after, expert claim).
- Emotional arc (where intensity peaks, where it releases).
- Hook framework.
- CTA shape.

This is what gets preserved. Do not change it.

### Step 3 — Load the brand baseline

Before writing, read the brand's existing scripts. Note:
- Pacing norms — how fast does this brand cut?
- Hook patterns — what kinds of openers does this brand favor?
- Voice — formal, casual, cheeky, warm, austere?
- CTA style — direct, conversational, urgent, soft?
- Length norms.
- Recurring quirks or signature moves.

The adapted script must match this fingerprint. If the reference's pacing is faster than the brand's norm, slow it to the brand's norm. If the reference's hook is more direct than the brand's voice, soften it. The structural skeleton stays, but the voice and pacing land in the brand's register.

### Step 4 — Substitute the brand into the structure

For each beat:
- Same beat purpose, different brand content.
- Same word count per beat. The reference's pacing is part of what works.
- Same emotional intensity. Match the energy.
- Brand-specific proof. If the reference uses a testimonial, the substitution uses one of the brand's verified testimonials. If the reference uses a before-and-after, the substitution uses an observable result the brand can show. If a proof type is compliance-blocked, swap for the nearest compliant equivalent.
- Brand voice. Every line reads as something the brand would say. The brand baseline is the reference for this.

### Step 5 — Drift audit

Compare the adapted script against the reference structure beat by beat. If the adapted script has drifted — more beats, different pacing, different emotional arc — pull it back. The discipline is fidelity to the skeleton plus fidelity to the brand fingerprint.

## Compliance substitutions

When the reference makes a claim the brand cannot make, substitute with the closest compliant equivalent:
- Before/after → routine + small observable win.
- Medical claim → sensory or experience claim.
- Price-anchored claim → value framing.
- Controversy → curiosity.

## Output content

The reference-adaptation path delivers in the four-part contract from `creative-strategy-context/adapting-scripts.md` — Overview, Script, Script with Storyboard, Fidelity Summary — per the output-contract-precedence rule in the skill's SKILL.md. The deconstruction in Steps 1 and 2 and the drift audit in Step 5 are internal working that informs the output, never shown to the user. What reaches the user:

- The adapted script in full with visual cues, in the brand's voice fingerprint.
- The brand baseline elements applied — pacing norm, voice match, CTA style, signature moves — surfaced in the brief, not as a deconstruction dump.
- The fidelity read confirming structural match to the reference, written as the Fidelity Summary's prose, not a comparison table.
- Compliance flags surfaced during substitution.

## What never to do

- Redesign the structure. Fidelity is the discipline.
- Carry any of the reference words verbatim. Every word gets rewritten.
- Substitute a claim the brand cannot defend. Compliance walls override.
- Bloat the script past the reference's word count.
- Drop or add beats. The structure stays the same.
- Skip the brand baseline load. Without it, the adaptation drifts away from the brand's structural fingerprint and reads as a competitor's script with the brand name swapped in.
- Blend multiple references. Adaptation is 1:1 against a single chosen reference. find-reference-ads picks the one; this process adapts it.
