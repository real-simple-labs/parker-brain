# Review Gates — The "Does It Look Dang Good?" Rubric

The final quality gate before anything ships. Run it via the `ad-creative-reviewer` agent when agents are available (it can open the images and video frames); otherwise run this rubric inline as a deliberately adversarial pass — fresh eyes, hunting for reasons to kill, not reasons to approve. The scaffolding guarantees on-format; this gate guarantees GOOD. Most AI ads in the feed are mediocre precisely because nobody ran this pass.

**Posture:** skeptical by default. "Fine" is a fail. The bar is not "acceptable AI ad" — it's "would this crack the top 20% of ads in this account" (Parker's library defines that bar when connected: how do the hooks, craft, and specificity compare to the ranked winners?). Every criticism must cite the specific line, prompt, or frame. No rubber stamps, no sandwich praise.

## Verdicts

- **SHIP** — passes every kill question, scores strong across both rubrics.
- **FIX** — specific repairable failures; list them ranked by impact, each with the stage to loop back to (script / image / video / audio / assembly) and the concrete fix.
- **KILL** — the concept itself is weak (hook dead on arrival, angle generic, style-format mismatch); recommend the replacement direction. Killing a weak concept before video credits is the cheapest decision in the pipeline.

## Copy rubric (score each 1–10; any kill question failing = not SHIP)

1. **Hook (kill question: would a scrolling thumb stop?)** — declarative, specific, states a hidden truth or opens an unbearable loop. Test the verbal, visual, and text hook SEPARATELY — each must work alone, silently, at thumbnail size. Generic pattern ("Tired of X?") = kill.
1b. **Pacing (kill question: is the problem in motion by second 8 and the turn by ~16?)** — time the beats against the clock, not the runtime percentage; compare against Parker's top-impression ads in the category (winners run 5–45s, product visible in the first seconds). Held tails, single-register stretches over ~15s, or a missing music bed = FIX at the edit.
2. **Read-aloud test** — every VO line sounds like a person talking, not written ad copy. AI-tells (em-dashes, hype adjectives, "game-changer/seamless/revolutionary"), corporate voice, or tongue-twisters = FIX with rewritten lines.
3. **Beat discipline** — one idea per beat; each beat a concrete physical image; escalation real (stakes rise, not just time passing); mini-loops pull beat to beat.
4. **The turn** — the product enters as the answer to the opened loop, in ONE clean beat, after the pain is fully built. Product bolted on early or late = FIX at script.
5. **Specificity** — numbers, sensory detail, customer language from the research. Count the abstract claims; each one is a demerit ("supports wellness" = kill-level generic).
6. **Voice-format fit** — villains taunt with zero remorse, heroes stay calm, narrators carry gravity, lyrics are genre-authentic and singable (4–8 syllables). A timid villain or a jingle-that-chants-the-brand = FIX.
7. **CTA** — rides the transformation, soft, offer-tied (guarantee/trial). Hard "buy now" or momentum-killing legal paragraph = FIX.
8. **Compliance + IP** — claims within policy (no cure/disease language, no personal-attribute callouts, no before/after violations), zero franchise/studio references, brand claims doc respected. Any failure here = automatic not-SHIP regardless of scores.

## Visual rubric (score each 1–10)

1. **Scroll-stop (kill question: is frame 1 arresting at feed size?)** — judge the FIRST frame and thumbnail at small scale (the squint test): single readable subject, strong silhouette, emotion legible. Cluttered or generic first frame = FIX.
2. **Style integrity** — the material actually reads: thumbprints in clay, fibers in felt, grain in paper, stitches in crochet, studs in brick. Smoothed-out texture, realism drift, or vector drift = FIX at image stage with escalated texture defense. Motion must match the lane's cadence (judder for stop-motion lanes, planar for paper).
3. **Character consistency** — same face, proportions, outfit, material treatment in EVERY shot. Compare frames side by side; any shot where the character reads as a different person = FIX (re-anchor to hero reference).
4. **World consistency** — palette and lighting hold across all shots (the P1 lock); sets feel like one world, not a moodboard.
5. **Composition per shot** — one focal point; 9:16 headroom; safe zones respected; the product legible and label-accurate against the reference photo. Product illegible in its hero shot = FIX.
6. **AI-tells sweep** — hands and fingers, garbled or phantom text, floating/merged objects, broken anatomy, dead eyes, extra limbs, impossible physics (outside the style's intent). Any visible tell in a shipped frame = FIX; this is the #1 credibility killer.
7. **Emotional read** — each shot actually expresses its beat's emotion (cover the captions and check: can you FEEL the beat order?). Beautiful-but-flat frames = FIX with expression/pose direction.
8. **Statics-specific** — the three-read test (0.5s: visual subject lands → 2s: headline lands → 5s: support/CTA lands); headline spelling verified letter-by-letter (OCR-check, never trust a glance); text inside safe zones; hierarchy obvious at thumbnail size; 5–6 winning-anatomy elements present (hook, sub-0.5s visual, one promise, proof element, CTA, non-central logo).
9. **The discriminator pass (kill question: would a media buyer clock this as AI-generated?)** — play the GAN: put the static next to its real reference ad and hunt for what gives the fake away. AI tells to hunt: sparse poster-like layout where winners are copy-dense · rendered-looking product where winners use real photography · absence of imperfection (no casual punctuation, no UI chrome, no blur, no mess) · generic "designed ad" energy instead of native platform energy (screenshot, advertorial, phone photo). A static with no real reference ad behind it fails this gate automatically. KILL anything that reads as an AI template poster — it burns brand credibility even when the copy is right.
10. **Rights & lane sweep** — zoom every generated human and prop: image models dress athletes in real brands by default (production-verified: a masters-runner render shipped wearing Under Armour and Mizuno logos — instant rights kill; the fix is an explicit unbranded-wardrobe line in the prompt). Also check the product itself: any animation-lane styling (character faces, stylized packs) on a photoreal static is an automatic FIX with the real packshot anchor.
10b. **The perfection kill (the gate that actually decides)** — production-verified failure mode: a 4-static batch passed every craft check (letter-perfect type, clean anatomy, zero logo leaks) and was still rejected on sight because every image was immaculate. "Absence of imperfection" isn't one tell on a list; it's the master tell. Ask of every photoreal static: *would this frame pass as a real artifact — a photo a person actually took, a screenshot someone actually cropped?* If it looks like an award entry or a TV ad, it fails ("I want it to look like it's from social media" — the ugly-ads doctrine). Polish is permitted ONLY when the reference winner is equally polished AND every human in frame is real. A synthetic person in a testimonial format is an automatic KILL, not a comp: the format's entire persuasive engine IS the real person, so there is nothing to preview. Craft checks (gates 1–8) qualify an ad; this gate decides it.
11. **Strategy fit + design-psychology spot-check** — does the ad serve the brand's LIVE strategy priority (not a superseded lens), in the register that priority calls for? Then the one-second test: view the static for one second — was the first read the hook? Is there a money shot (or a reference-justified type-led exception)? A beautiful ad aimed at last month's strategy is a KILL, not a FIX.

## Audio rubric (when takes/finals exist — flag for human listen where the reviewer can't play audio)

1. Delivery matches the character direction (villain assertive, narrator warm) — a timid villain is a regeneration, not a keep.
2. Brand names and product words pronounced correctly (the #1 audio failure — check every occurrence).
3. Pacing: lines breathe at the style's speed; no rushed tails, no dead air over motion.
4. Mix: VO clearly above music (ducked −15 to −20 dB); no per-clip audio seams; SFX support beats rather than clutter.

## Process (how to actually run it)

1. Read the kit/script COLD first — before any context — and note your honest first-reaction on the hook (that reaction is the viewer's).
2. For assets: open every image at full size AND at thumbnail scale; for video, extract frames (first, last, +1/sec) and review the strip in order; play finished video if the environment allows.
3. Score both rubrics; answer the kill questions first — a kill question failing ends the review early with FIX/KILL.
4. When Parker is connected, pull 2–3 top-ranked ads in the category and say plainly whether this ad beats, matches, or trails them — and why.
5. Output format:

```
VERDICT: SHIP / FIX / KILL
One-line reason.

Copy: [scores + the 2–3 sharpest observations, each citing a line]
Visual: [scores + the 2–3 sharpest observations, each citing a frame/prompt]
Audio: [observations or "flagged for human listen: <checklist>"]

FIX LIST (ranked by impact):
1. [failure] → [stage to loop back to] → [the concrete fix]
...

The bar: [how it compares to the swipe-file bar / Parker's ranked winners]
```

**Cadence:** run at two points — after Stage 2 on the script alone (kills are cheapest here) and at Stage 6 on the assembled ad. Statics batches get one pass per batch. A FIX verdict loops back to its stage, and the re-review checks ONLY the fix list plus a fresh AI-tells sweep.
