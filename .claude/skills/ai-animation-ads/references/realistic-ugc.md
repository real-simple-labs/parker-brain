# Realistic AI UGC — the reference-parity pipeline

Photorealistic creator-style UGC (talking-head, demo, unboxing) that is production-ready AT generation. The architecture principle, learned the hard way across 13 graded owner corrections: **every quality failure was a measurable property the winning reference already had.** So the reference is not inspiration — it is a quantified spec, and every stage generates toward and reviews against its numbers. Measure, don't vibe.

This lane pays realism's tax: the full platform AI-disclosure label, and legal sign-off before spend. A synthetic presenter never voices personal usage history or results ("Me neither" yes; "I take this every day" no) — first-contact formats (unboxing, first-try) fit the zone natively.

## THE PIPELINE (run in order; nothing ships on a skipped stage)

### 0. Reference anatomy + PARITY SPEC
Pick the reference through the fit scorecard (same buyer/job/register, proven rank + days live, mechanic available, compliance-safe). Then extract its FULL anatomy:
- Rip frames every ~2s and VIEW them (the true camera grammar: propped/handheld/selfie — never import grammar the reference doesn't have).
- Pull the complete transcript, storyboard, and on-screen-text track (ad-library analysis when tracked).
- **Run `scripts/ugc_parity.py` on the reference video + transcript.** The output is the run's PARITY SPEC: speech density (winners: ~91%), utterance distribution (median 6–8 words, mostly ≤8, occasional 10–19 riffs — a distribution, not a cap), cuts/10s (~1.0–1.7) and median shot length (~4.5–6s), grade bands (saturation ~67–72, contrast-std ~61–64, texture ~5–10). Every later stage targets these numbers ±band.

### 1. REVIEW 1 — STRATEGY (agent pass, pre-adaptation)
On the reference pick + segment map: brand alignment; **mechanic availability** (a beat built on attacking our own category position is unavailable — a gummy brand's anti-powder taste slam cannot enter the powder brand's mouth); **vault-verified props** (every SKU/prop confirmed from the brand vault or live site, never model memory — a hallucinated SKU is a killed ad); adaptation direction per beat; awareness-cell fit and measurement plan. REVISE or KILL before any script work.

### 2. DIALOGUE — continuous narration at reference density
The single biggest structural rule: **the creator talks wall-to-wall; actions ride UNDER speech, never instead of it.** Write each 8s segment as ~18–21 words of continuous casual narration (≈2.4 w/s), shaped as the reference's distribution: mostly 3–8 word breaths, at most one longer riff. Object-driven in demo beats (words follow the hands: "Okay. The bag. This jar thing..."), no composed inventory sentences, no rhetorical scaffolding ("So if X, then Y"), no crafted images in mouths (if a phrase would look good ON a static, it's copywriting, not speech), filler only where the reference's own transcript has it.
**Mechanical validation FIRST:** word counts per breath vs the spec distribution, projected density (words ÷ segment seconds ≥ 2.2 w/s). Out of band = rewrite before judgment.
Then **REVIEW 2 — SCRIPT** (agent pass): creative-voice-review + ai-writing-tells + presenter zone + claims. Both checks pass before a credit moves.

### 3. PLATES — the ugly-ad start frames
One plate per segment, HERO-referenced for identity, product packshot referenced for labels. The aesthetic target is a 2018-era phone (still 1080-crisp, zero computational photography):
- **BANNED prompt words:** shallow depth of field, background blurred, bokeh, soft/diffused daylight, cinematic, beautiful.
- **REQUIRED:** deep focus (background as sharp as subject), genuinely cluttered lived-in space, hard mixed household light with the window BLOWN OUT, warm indoor cast, slightly off-center framing, fine sensor noise, natural skin.
- Gate every plate at zoom: reality pass, likeness (synthetic person, never a real creator's face), label OCR (readable-size text verbatim vs packshot; micro-print may blur sub-legible for video — statics composite the real label), prop continuity across plates (reference earlier plates for shared props — a box that re-renders per plate is a catchable tell).
- **Branded-prop truth:** any packaging prop the dialogue points at ("this is the box") is a brand surface — verify its real art from the vault or live site before generating, or keep the prop out of the named line. Model memory is banned for prop art, same law as SKUs.

### 4. CLIPS — best-of-2 takes, locked language
Omni primary (native-audio realism); per clip: handheld grammar matching the reference, **label-lock language** ("the label stays sharp, unchanged, correctly spelled in every frame"), **verbatim framing** ("she says exactly these words and nothing else, once, no repeats" — prompt enhancers strip plain quotes), action directed to happen WHILE she talks. Generate 2 takes per segment and pick winners at the gates.
Known failure modes: Omni doubles mid-phrases (~1 in 3 — the edit dedups them as jump cuts); repeated `failed` status on one segment across plates/prompts = engine issue, fall back to veo-3 BEST variant (start_image) and flag the voice join for the human ear; a `nsfw` flag on innocuous content = rephrase the physical direction and re-roll.

### 5. PER-CLIP GATES (ship law)
Every take: **transcript verification word-for-word** (deviation = re-roll or edit-dedup if the double sits in its own speech span) + **label OCR at zoom on ripped frames** (label drift mid-motion kills the take) + action-on-words check. Two traps this gate exists for: (a) gate the **SELECTED** take — zooming take B and shipping take A is how a drifted pack ships; (b) words are not enough — the pack **design** can drift while every word stays spelled (an invented accent color, a changed lockup). So the gate evidence includes a **cross-clip pack strip**: one pack crop per selected clip, side by side with the packshot; any visible design delta = re-roll that clip. Then upscale winners (bytedance `ugc` preset → 1080p) — and remember the upscaler denoises, so the grade pass comes AFTER.

### 6. EDIT — to the parity spec, not to a rhythm of its own
- **Density first:** cut silence gaps and duplicated phrases so assembled speech density lands ≥ ~88%. Trim any low-density take hard (a 6-word take occupies ~3s, not 8).
- **Cadence:** match the reference's cuts/10s and median shot length — do NOT add punch-ins beyond it; a zoom change only where the reference's own grammar would cut. Ramps (1.5–2.8x) only on silent action that must survive (a referenced action is never deleted — "smells fine" keeps its sniff).
- Joins: 12–20ms audio fades at every splice (splice clicks are audible); never let a rate boundary fall inside a word; dialogue levels within ~1.5dB across segments — **measured** (volumedetect per segment), not prompt-set, especially on engine-fallback clips which run their own gain.
- Any contents enumeration ("the bag, the jar, the scoop") diffs against the vault's kit manifest, every omission logged in the delivery notes — omission is fine (under-promise), unlogged omission is not.
- **Text layer:** headline treatment of the hook from the literal first frame (E32), persisting through the hook beat; then platform-native caption pills (per-line hugging pills, merged junctions, bold geometric sans) phrase-synced from measured speech windows; every text asset letter-proofed before overlay; pills clear the platform's bottom chrome; captions cover action beats (no uncaptioned valley).
- End card: art-directed (depth, display headline, integrated shadowed product, CTA pill + domain), gentle push-in, ~1.8s. **No source-slab composites:** a packshot pasted with its background rectangle is the un-integrated tell — key/cut out the product, add a contact or drop shadow, and grain-match the card to the footage's finish so it lives in the same camera world. The card headline compresses the ad's own strongest spoken value line, in the account's proven copy frames — never a convenience-only tagline the strategy docs reject.

### 7. GRADE — to the measured band
Apply the 2018 finish AFTER assembly and verify with the extractor: saturation into ~67–75 (AI sources are vivid — usually REDUCE), contrast-std ~60–68, texture ~6–11 (fine noise + modest sharpen — overshooting reads AI in the opposite direction), warm cast, blacks slightly crushed, highlights clipped, ~crf 26. Re-measure; out of band = adjust and re-encode.

### 8. REVIEW 3 — EDIT (agent pass) + PARITY CHECK
`ugc-edit-reviewer` on the master + cut plan, WITH the parity spec: cut integrity (no clipped words), gesture-word sync, action-referent order, dead air, caption sync, retention, specs — plus the measured deltas (density, cadence, grade) vs the reference. Apply fixes, re-verify.

### 9. FINAL GATE — the owner simulation (non-optional)
`creative-critic` on the assembled master with the full owner-feedback corpus: predicts the owner's grade, raises the objections he would raise. Below predicted A+ iterates (max 3) before delivery. This gate exists so corrections land internally — it is the reason the whole loop was built, and it runs on EVERY master, every time.

### 10. DELIVER with receipts
The master + the parity scorecard (reference vs master, all metrics) + the critic's verdict + per-gate evidence + the AI-disclosure and legal-sign-off flags. A delivery without the scorecard is unfinished.

## Standing laws (apply throughout)
- The reference is the whole video, never its first frame; its length and beat structure are inherited; a single clip is a hook test, never an ad.
- Frame-to-video over ingredients; product IN the plate; the plate is the consistency mechanism.
- Voice must pass the OWNER'S ear — automated "natural voice" verdicts under-detect; human listen before ship.
- Polish-match the reference: cleaner than the real thing is an AI tell (in both directions — the grade bands cut over-ugly too).
- Google Flow Kit Mode when executing manually: frames + per-clip prompts + same-session voice plan (voice stays consistent within a Flow session; never use Flow's built-in character features).
- Same synthetic creator across a brand's ads = account-native; vary wardrobe/setting per ad (identical outfits across "different days" is a batch-shot tell); never share a spoken closer between two creators' scripts.
