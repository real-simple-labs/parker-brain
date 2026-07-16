# Image Prompting — Start Frames & Character Consistency

Images are the cheap layer — get every frame right here before any video credits are spent. Typically 15–19 images for a 60s ad (one per VO line/beat, plus hero references), numbered P1, P2, P3… Generate ALL images for the ad before animating anything.

## Prompt anatomy (every start frame)

```
[LOCKED STYLE BLOCK — verbatim from styles.md]
+ [CHARACTER BIBLE — verbatim, if a recurring character is in shot]
+ [SCENE: what's happening, where, props — one beat, matching its VO line]
+ [CAMERA: shot type + angle, stated inside the world]
+ [LIGHTING/PALETTE: matching P1 — "warm palette matching P1, NO cool grey tones"]
+ [NEGATIVE/CLOSER: "No text, no captions, no words, no letters, no watermark, no UI."]
```
Write conversationally, not keyword soup — brief the model like a creative director in full sentences, strong verbs, positive framing ("empty bathroom counter," not "no clutter"). Front-load what matters most (early tokens weigh heaviest). Compose in the video's final aspect ratio (9:16) and leave headroom for motion.

## The three-layer consistency system (this is the whole game)

1. **Locked text.** One Character Bible paragraph — age, face, eyes, distinctive features, outfit, material treatment — pasted word-for-word into every prompt where the character appears. Never paraphrase; "blazer" stays "blazer." Change ONE variable per generation (scene OR pose OR expression).
2. **Hero reference image.** Generate P1 first: a clean, well-lit, full-body neutral shot of the character in the locked style — the master anchor. It also locks the world: palette, lighting, set dressing.
3. **Reference the HERO, not the previous image.** Every later shot attaches the hero image (and re-attaches on every single generation) with an anchor phrase: *"Using the attached character as reference — keep its exact face, eyes, proportions, and [material] style identical. Now show it [new action/setting]."* Chaining output→output compounds drift; always point back to the master. If drift accumulates anyway, mint one fresh clean reference from the best recent frame and re-anchor to that.

**Product fidelity:** in EVERY shot containing the product, attach the real product photo as a second reference and instruct "the product matches the attached reference exactly — label, colors, proportions." Never let a model draw packaging or logos from memory. Production-verified upgrades when the pack must read REAL:
- **Source a large, clean, front-facing packshot** (retailer listings are reliable: Amazon `data-old-hires` image) — a product small inside a lifestyle/composite photo gets re-interpreted.
- **"Photoreal product in an animated world"**: prompt the scene as the animated style with ONE photorealistic element — the pack "reproduced exactly, like a real product composited into an animated world." A personified face can still be blended into a plain area "without altering any label element."
- **Label micro-type WILL garble** (fails consistently at 1k across models — 4/4 in production). Keep only the wordmark + one tagline on generated packs; drop fine-print rows and certification seals (fake-looking seals are also a compliance risk — put those claims in the VO or restore real fine print as an editor overlay on statics).
- **Typos get surgical edits, never re-rolls**: "Keep this image EXACTLY as it is; make exactly ONE correction: the tagline must read, letter-perfect, '…'".

**On Higgsfield:** `generate_image` with `params.medias: [{value: "<hero job_id or imported media_id>", role: "image"}]` (nano_banana models use role `image`/`image_references` — check `models_explore` for the model's declared roles). A completed generation's **job id works directly as a reference value** — no download/re-upload loop. Import external product photos with `media_import_url` (or `media_upload_widget` for local files) first.

## Model selection (Higgsfield ids)

| Model | Use when | Notes |
|---|---|---|
| `nano_banana_2` | **Default for all start frames** | Fast, cheap, excellent stylized rendering; conversational prompts; multi-reference (attach character + product together, name each image's job: "Image 1 is the character, Image 2 is the product"); no seed param — reference anchoring IS the consistency lever; "edit, don't re-roll": ask for adjustments conversationally instead of regenerating. |
| `nano_banana_pro` | Hero references, 4K finals — BUT verify what actually serves | Catalog's "ultimate quality, text and diagrams" tier — however Higgsfield has silently served `nano_banana_2` on every `nano_banana_pro` request across three production batches. **The submit response's `model` field shows the served model immediately — read it on job 1 of every batch** and fall back if downgraded. |
| `seedream_v5_pro` (statics primary) | **Photoreal statics, anything text-heavy (UI recreations, quote cards, label fidelity)** | Production-verified: serves as requested, letter-perfect multi-line text and iOS UI at 2k, exact layout-DNA transfer from reference ads. Won the head-to-head against NB2 and openai_hazel on rendered text. |
| `nano_banana_2_lite` | Bulk cheap drafts | 1k only. |
| `seedream_v4_5` | Stylized/illustrative lanes; crochet (its universal negative block works as a "Negative:" line); when Nano Banana's look isn't landing | Structured prompts, front-loaded priority, 30–100 words; supports seed; up to 10 refs — 3–5 angles of the same subject gives the most stable identity. **The model swap is a style lever**: same prompt on the other family often fixes a stubborn look. |
| `seedream_v5_pro` / `_lite` (edit duties) | Instruction-heavy edits, multi-subject scenes (see statics-primary row above) | Natural sentences; JSON-structured prompts work for multi-subject layouts; hex codes paired with names ("#FF006E hot pink"); negative prompts only reactively. |
| `gpt_image_2` / `openai_hazel` | Exact typography, designed layouts (statics) | Best instruction-following and text accuracy; slow + pricier; 4 input images max, reference by index ("put the character from Image 1 into the scene from Image 2"); quality medium/high for small text. |
| `image_auto` | Unsure | Routes by intent. |
| Utilities | — | `outpaint` (extend a frame), `remove_background`, `upscale_image`/Topaz (finals), `flux_kontext` (style transfer/edits). |

## Workflow discipline

1. **P1 = the world-lock shot.** Generate 2–4 variations in one call (`params.count`); pick the best; that's the hero reference AND the palette/lighting anchor for every prompt after it.
2. Generate scene frames in VO-line order, hero ref attached every time; 2–3 variations for important frames (cheap on drafts).
3. **Critique loop:** if an output misses, say exactly what's wrong and update the PROMPT (or edit conversationally); if it misses twice, rewrite the prompt or swap model families. Re-rolling the same prompt a third time is waste.
4. When a needed shot has no VO line (community shot, POV screen close-up, reaction insert), add it — the storyboard serves the edit, not just the script.
5. Reference-image rescue: if text prompting can't hit the style, attach a style reference (a frame from a reference ad, or a look pulled from the swipe board) and instruct "match this visual style only — not its content."
6. Keep a shot manifest as you go: `P# · VO line · type (A/B/C) · job_id · chosen variant` — video generation and assembly depend on it.

## Style-specific reminders (details in styles.md)

- Pixar-style: personified products get faces/arms/hero poses; miniature characters interacting with the product; clean minimal backgrounds.
- Claymation: "visible thumbprint impressions" in every prompt; age + "smooth youthful clay skin" to avoid creepy faces; medium shots.
- Paper: physicality block verbatim; camera inside the world; "papercraft" near faces/products; saturated palettes (origami = pastel).
- Crochet: 5-part prompt order (scene → universal positive → lighting template → universal negative → product ref); diorama framing carries the yarn texture; simple poses only.
- Skeleton: the chosen Character Bible block verbatim + theme/palette fill; hero reference is the "clean neutral full-body" shot.
- End frames (Type B shots): same setting, lighting, character — ONLY the action resolved to its final landed state.

## No text in start frames

Never bake captions, on-screen words, titles, labels, subtitles, watermarks, or UI into video start frames — text is added in the edit. End every image prompt with the negative line. Only exception: the user explicitly asks for in-image text, or the image IS a static ad (static-ads.md has its own text rules).
