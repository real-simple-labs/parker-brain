# Product Launch — Strategy

This document classifies the launch and routes to the right playbook. The classification drives every downstream decision — voice, proof types, hook angle, which existing ads to study, what the output even looks like — so it happens before any concept work.

The scenarios themselves, and the reasoning behind them, live in `parker-system/creative-strategy-context/new-product-launch-creative.md`. Load that first. This doc is the decision procedure on top of it.

## What to load before classifying

- The brand's committed strategy (`strategy/`) and idea bank (`idea-bank/`) — the frame the launch sits inside, and any evaluated entry this launch should execute from.
- Brand profile, ICP, personas, voice of customer, compliance rails.
- The brand's ad history — what has run, what has won, what has failed.
- The launch brief itself, plus any product URL, competitor refs, or past performance data attached to it.
- `new-product-launch-creative.md` — the scenarios and the newness taxonomy.

## Step Zero — the four questions

Answer in order. **If an answer is unknown, ask the user. Do not guess.** A wrong classification here is much more expensive to fix than a clarifying question, because every downstream decision inherits it.

### Question 1 — Scope

Is this an established brand with prior ad history and at least one proven SKU, launching something genuinely new?

Three routes out, all covered by the scope gate in `SKILL.md`: a first-ever product launch, a geographic expansion, or a restock / re-release / "limited edition" wrapper on an unchanged SKU. Only the third is subtle — the test is whether something new exists, not whether the brand is announcing something. A genuinely new colorway or flavor inside a limited drop is in scope.

### Question 2 — Audience fit

Does this product target an **existing persona** the brand has already advertised to successfully, or a **new persona** the brand has not yet served?

**This is the single most important question in the whole flow.** If the answer is unclear, ask before continuing.

The caveat that matters: "existing persona" does not have to mean every current buyer. A new SKU often targets a *slice* of the existing persona — the active subset of an athleisure buyer base, the new-mom subset of a baby brand's customers, the dads inside a broader audience. That is still Scenario B, with a refined persona slice, and the ad gets written to that slice's specific language rather than the general persona's.

### Question 3 — Type of newness

Pick the closest match from the taxonomy in the launch doc:

- **Same product, new attribute** — color, flavor, scent, fabric, size.
- **Same product family, new format, variant, bundle, or collection drop** — a gummy becomes a drink, a single becomes a bundle, a hero product spawns a spinoff, a seasonal collection lands.
- **Same product family, new audience entry** — the product type exists in the brand's world; the audience is new to the brand.
- **Wholly new category for the brand** — rare and risky.

If the launch sits between two entries, describe the actual state in plain language rather than forcing the closest label. The taxonomy is a lens.

### Question 4 — Deliverable type

What is the user actually asking for? Defaulting to a full script when they asked for five hooks wastes their time.

- Full script(s) plus storyboard — **the default if unspecified**
- Hooks only
- Ad copy and headlines only
- Founder or talking-head video script
- Shot list, or a pre-launch shot-list audit
- Multi-video theme, through-line, or launch content plan
- Format recommendations only

Each has its own output spec in `processes/deliverable-specs.md`. The shape of the deliverable changes the shape of the work.

## The scenario matrix

Questions 2 and 3 together produce the scenario.

| | Existing persona | New persona |
|---|---|---|
| **New attribute** | **Scenario A** — depth play | Rare. Usually means Q2 was answered too quickly; re-check. If genuinely new-audience, treat as **C**. |
| **New format / bundle / collection** | **Scenario B** — bridge and expand | **Scenario C** |
| **New audience entry** | Re-check Q2 — "audience entry" implies a new audience | **Scenario C** |
| **Wholly new category** | **Scenario B**, leaning C — the persona may follow the brand, but the category authority does not transfer | **Scenario C**, hardest case |

Two calls that come up constantly:

**Bundles.** Sometimes A (same use case, just packaged together), sometimes B (the bundle creates a new ritual, occasion, or completeness story). Diagnose on whether the SKU is new or the *use case* is new. Defaulting a bundle to a generic "new product" hook is the laziest move in launch creative.

**Collection drops.** Usually A. If the collection introduces a genuinely new format or use case rather than new attributes across the same silhouettes, it is B.

## Worked example

*A baby-care brand launching a cream conditioner, with non-UGC ads specified, three competitor benchmark refs, and one prior winning ad supplied.*

- **Q1** — established brand with prior ad history. In scope.
- **Q2** — existing persona; parents of young children, the same buyer base as the rest of the line.
- **Q3** — same product family (baby care), new format (a conditioner where there was none).
- **Verdict** — Scenario B, with a slight A tilt, because the audience and use case overlap heavily with the existing bath and body line.
- **Q4** — launch concepts and messaging, meaning multiple full scripts, with mandatory ingestion of the competitor refs and the prior winner during the diagnostic.

## The launch frame

Translate the scenario into the mental mode the writing runs through. The mode is the lens; it should not change mid-script.

**Mode 1 — more of what works (Scenario A).** Existing winning structures with the new attribute swapped in. The hook can often be the same hook, the proof the same proof, the persona voice unchanged. Replication with a swap, not reinvention. *A bestselling hoodie's winning hook — "POV: you finally found the perfect everyday hoodie" — becomes "POV: now in [new color]." Same hook DNA, swapped element, same proof, same shot cadence.*

**Mode 2 — bridge and expand (Scenario B).** Lead with brand authority and the existing customer relationship, then introduce the new format as a natural extension. Voice and persona unchanged, but the script does more work than Mode 1 because it is explaining a new use case. The bridge carries the hook. *"You already love [hero] — we made one for [new moment]."*

**Mode 3 — new world entirely (Scenario C).** The new persona does not know or trust the brand. Establish their problem-aware language first; the brand introduces itself in this audience's terms, not its own. Slowest to write, highest-stakes if the voice is wrong. *Open in her problem — "if you've ever tried to shave your legs and ended up with bumps you can see for a week, this is for you" — then earn the brand's right to be in the conversation. The existing audience's tone will torch the ad before it has a chance.*

## Angle strategy by scenario

**Scenario A.** Pull the top one or two proven angles from the closest existing SKU, then add one angle that explicitly showcases the new attribute. Drop and reveal mechanics, side-by-side with the existing line, "which one are you" personality framing, "new in [season]" using the brand's own collection vocabulary. Do not write three new angles — replicate what is working and let the newness show through.

**Scenario B.** Lead angle is the bridge: "if you loved [hero], we made [new]." Add two use-case angles specific to the new format or occasion. Pull at least one bridge testimonial — an existing customer trying the new SKU, letting them be the credibility source. For bundles, lead with the value of the format change (ritual, savings, completeness, a routine that finally fits together), never a generic new-product hook.

**Scenario C.** Produce three to five fresh persona angles built from scratch in the new audience's voice. Cover at minimum a problem angle (their pain in their words), an identity angle (this is for someone like you), a social proof angle (people in your world use this), and an objection-handling angle ("isn't this for [other audience]?"). **Do not reuse existing-persona hooks.** That is the most common Scenario C failure.

## Pairing awareness stage with scenario

The canonical stage definitions are in `killer-performance-ads.md`; the launch-specific mapping and the warm-phase override are in `new-product-launch-creative.md`. What this doc adds is the pairing rule.

Scenario and awareness stage are independent variables and both must be set. A Scenario A launch to a most-aware audience is short and punchy with no context needed — "meet the new, plus intro offer." A Scenario C launch to a problem-aware audience is a slower opener in persona language, then the brand reveal, then the product. These are not interchangeable, and an ad pitched at the wrong depth fails even when the scenario is right.

The warm-audience launch ad almost always targets most-aware. Cold-audience scaling covers everything else. Scenario C usually starts further back than the canonical solution-aware default, because the new persona does not know the brand at all.

## The process menu

Strategy picks; the processes execute.

- **diagnose-the-account** — the required pre-write diagnostic. Existing winners, closest SKU, equity language, warm-audience plan, past failures, product URL, competitor refs. Runs on every launch regardless of scenario.
- **scenario-a-depth-play** — Mode 1 execution. Angle set and script moves for attribute and collection-drop launches.
- **scenario-b-bridge-and-expand** — Mode 2 execution. The bridge, use-case demos, bridge testimonials, bundle handling.
- **scenario-c-audience-expansion** — Mode 3 execution. Persona-first angles, objection handling, re-pitched authority, and the persona mini-brief fallback.
- **proof-substitution** — honest proof when the SKU has none yet.
- **launch-phase-sequencing** — warm recapture versus cold scaling, and the pre-launch / launch-week / evergreen arc.
- **special-launch-contexts** — gifting and occasion launches, giveaway mechanics, multi-video through-lines.
- **deliverable-specs** — the output spec for each Question 4 deliverable type.
- **edge-cases-and-routing** — the substitution library, the persona-fit check, and the launch audit.

## Common mistakes this strategy exists to prevent

- Writing before classifying, then discovering mid-script that the scenario was wrong.
- Guessing on Question 2 because the brief did not say and asking felt slow.
- Treating an attribute launch so lightly that the launch goes invisible.
- Defaulting a bundle to "we have a bundle now."
- Writing a Scenario C launch in the existing persona's voice out of habit.
- Skipping the account diagnostic and producing creative that ignores what already works.
- Inheriting past winners without diagnosing past failures.
- Confusing launch phase (who is in the pool) with awareness stage (what they know).
- Producing a full script when the user asked for hooks.
