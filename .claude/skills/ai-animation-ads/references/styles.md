# Style Library — AI Animation Ads

Every ad locks ONE style before any image is generated. The style block goes **verbatim at the top of every image prompt and every video prompt** in that ad — consistency across 15+ shots comes from repeating the exact block plus re-attaching hero references, never from "same style as before."

## Universal style rules (apply to every style)

1. **One style per ad.** Test a second style as a separate ad from the same script — that's free creative diversity, not a remix.
2. **Lock palette and lighting in the first image (P1), then enforce.** Models drift toward cool blue-grey defaults. Every prompt after P1 carries a palette continuity line: `Soft warm diffused lighting matching P1, [PALETTE NAME] palette, NO [OPPOSITE] tones.` This one line fixes more continuity breaks than anything else.
3. **State the camera position in every prompt** ("eye level with the character," "worm's-eye up at the shelves," "overhead on the bathroom counter"). The angle is free per shot; naming it is not.
4. **No text in video start frames, ever.** No captions, titles, labels, watermarks, UI. End every image prompt with: `No text, no captions, no words, no letters, no watermark, no UI.` Captions are added in the editor. (Statics are the exception — see static-ads.md.)
5. **IP-safe phrasing.** The swipe-file shorthand for these looks is "Pixar style" / "Disney style," and models respond to those tokens — but for paid commercial ads the safer practice is descriptive language ("high-end 3D animated feature film style"). Never build a paid ad on a named franchise look (Simpsons, GTA, a specific film's characters): it's a trademark/trade-dress risk and practitioners who spot those ads say they wouldn't run them. Descriptive blocks below are written brand-safe; add style tokens only if the brand accepts the risk.
6. **Two identical failures = wrong prompt, not bad luck.** Don't re-roll a third time; rewrite the prompt (or switch image model — the model swap is a style lever of its own).

## Style selection matrix

| Brand/product signal | Best-fit style |
|---|---|
| Health, wellness, family, transformation story, broad audience (women 25–45, parents) | **3D feature animation ("Pixar-style")** |
| Craft, care, premium ingredients, trust-signal categories (skincare, supplements, food/bev, baby) | **Claymation** |
| Handmade warmth, gifting, editorial/explainer arguments, premium depth | **Paper family** (pick a sub-style) |
| Cozy, tactile, disarming charm; fragrance/personal care; standing out from polished feeds | **Crochet/knitted diorama** |
| App/SaaS, list-driven educational scripts, high-volume cheap testing | **Flat 2D vector** |
| Playful/edgy brand + escalating "what happens if" script | **Skeleton character** (see formats.md — it carries its own 4-look character library) |

The scroll-stop logic: people process animated storytelling the way they process cartoons as kids — lower ad defenses, higher comprehension. The style is the pattern interrupt; the script still does the selling.

---

## 1. 3D Feature Animation ("Pixar-style")

**Communicates:** instant familiarity and warmth; emotional storytelling; aspirational but safe. Highest visual novelty / scroll-stop in feed right now.

**Style block (open every prompt with it):**
> High-end 3D animated feature film style, rounded soft geometry, warm colour palette, soft ambient lighting, cinematic depth of field, studio-quality render, subtle subsurface scattering on skin and materials, clean minimal background.

**Scene-type prompt patterns (fill and append the style block):**
- *Product hero:* `[PRODUCT DESCRIPTION] in a bright minimal studio, miniature [CHARACTER/ELEMENT] interacting with the product, warm palette, cinematic composition`
- *Problem visualisation:* `[VISUAL METAPHOR FOR PROBLEM], warm but slightly muted colours conveying [EMOTION], expressive character face showing [PAIN EMOTION]`
- *Mechanism:* `cross-section view of [BODY PART / MECHANISM], [INGREDIENT/TECH] working at microscopic level, glowing particles, warm scientific aesthetic`
- *Transformation:* `[CHARACTER/SCENE SHOWING OUTCOME], bright warm lighting, vibrant colours, radiant glow, aspirational uplifting mood`
- *Personified product:* `[PRODUCT] rendered as an animated character with a [PERSONALITY] face, [eyes/arms/expression details], hero pose, soft warm glow, kind sculpted expression`

**Production notes:** close-ups work well · cuts and morphs both work · speed-map 2–2.5x in the edit · lip-sync YES in talking-character formats (include exact dialogue in video prompts), NO in narrator-led (prohibit explicitly) · keep backgrounds "Apple keynote" minimal so the character carries the frame.

---

## 2. Claymation

**Communicates:** craftsmanship, care, authenticity. The visible handmade texture transfers to the brand; disarms "this is an ad" defenses.

**Style block:**
> High-end claymation style, stop-motion animation aesthetic, visible clay and plasticine texture on all surfaces, fingerprint impressions in materials, miniature set design, soft diffused lighting, handcrafted tactile quality, minimal studio backdrop, warm earthy colour palette.

**The ten claymation production rules (these make or break it):**
1. **Voice-over only — characters NEVER move their mouths**, in every variant, even first-person lines. Enforce in every video prompt: `the character's mouth stays closed, no lip-sync, no speaking on screen.` Never paste a dialogue line into a claymation video prompt without that constraint.
2. Hard cuts AND soft dissolves both work — dissolves lean intimate, hard cuts suit fast list-style beats. Mix freely per script pacing.
3. No literal set morphs ("kitchen reshapes into bedroom") — models break. Use camera moves + dissolves/cuts; reserve morphs for one element flowing into an adjacent one.
4. Avoid extreme close-ups — macro exposes seams and turns fingerprints into blemishes. Live in medium / medium-close shots.
5. Speed-map 1.5–2x, never 2.5x (claymation reads jittery at high speed). Sung-VO variants 1.3–1.7x.
6. Palette-lock line in every prompt after P1 (see universal rules).
7. Multiple characters: one hero focal point, supporting characters still and listening, eyes may shift toward hero.
8. **"Visible thumbprint impressions"** is the magic anti-smoothing phrase — repeat it in every prompt; escalate if outputs come back polished.
9. Character continuity: feed P1 as reference into every prompt where the character reappears + "the same character from P1, identical facial features."
10. When an element must read real (a wound, a stain, a label): give physical constraints — "recessed into the surface, not raised," "concentrated only where it would naturally appear" — cartoon treatment stays on the hero only.

**Anti-creepy-face fix:** specify age ("early-30s"), "smooth youthful clay skin with subtle thumbprint texture (not heavy weathered texture)," "soft features," frame to include the hairline.

**Scene-type patterns:** same four scene types as Pixar, re-skinned — e.g. mechanism: `cross-section diorama of [BODY PART] presented like a sculpted stage set, [INGREDIENTS] as tiny claymation elements, miniature science lab aesthetic, wide medium shot`.

---

## 3. Paper family (5 sub-styles)

Every frame must read as **photographed physical paper** (grain, edge thickness, real cast shadows — or it drifts to flat vector) and be **shot from inside the paper world** (or the model shows you a craft object on a desk). Strike the words "diorama / shadow box / tabletop / model" from paper prompts — they trigger the exterior-view failure; re-anchor with "the paper scene fills the entire frame, the camera is inside the scene."

**Physicality block (append to every paper image prompt, verbatim):**
> Everything in frame is real physical paper, photographed — visible paper grain and fibers, cut edges showing paper thickness, real cast shadows, soft studio lighting, the paper scene filling the entire frame.

**Color:** saturated and high-contrast, palette stated explicitly per prompt — except origami (soft pastels). Say **"papercraft," not "paper cut,"** near faces and products (paper-cut blurs features). In video prompts always name the cadence: `stop-motion cadence, 12 fps judder, slight frame-to-frame jitter, no motion blur` (soften to "subtle stepped motion" for lane 1).

**Sub-style locked blocks (pick one per ad):**

1. **Layered papercraft world** (premium, hero products, parallax pushes):
> Layered papercraft world — everything built from stacked cardstock with visible paper thickness, deep layered depth between foreground, midground and background paper planes, layered cast shadows, paper quilling details, the camera inside the scene and the paper world extending past every edge of the frame.

2. **Flat construction-paper cutout** (comedy, skits, lo-fi charm):
> Flat construction-paper cutout scene — simple layered flat card shapes, snipped edges, visible paper grain, jointed paper puppet characters, soft drop shadows between the layers, bold flat colors, the scene filling the entire frame with the camera inside the paper world.

3. **Handmade stop-motion paper** (handmade warmth; proven for short-form product ads):
> Handmade paper stop-motion scene — torn paper edges, visible glue seams, construction-paper grain, hand-placed imperfection, soft practical lighting with visible falloff, the scene filling the entire frame.

4. **Mixed-media collage** (editorial/explainer arguments, human-subject stories — product stays a photographic cutout with scissor-cut edges):
> Mixed-media paper collage world — the entire scene built from cutouts composed into one deep coherent scene: black-and-white photographic cutout faces on hand-drawn paper bodies, clothing collaged from colorful patterned paper, structures built from cardboard and newspaper fragments, vintage magazine clippings, washi tape strips and vintage stamps tucked through the scene, hand-drawn ink details over the paper, rich saturated collage colors against newsprint neutrals, the camera inside the scene.

5. **Origami world** (calm premium, transformation concepts; pastel exception):
> Origami world scene — everything folded from paper with clean geometric creases: delicate origami figures, crisp angular folds on every object, pleated paper details, soft pastel-colored papers, soft diffused lighting casting gentle shadows that reveal the dimensional paper folds, the handcrafted feel of a stop-motion paper world, the scene filling the entire frame with the camera inside the paper world.
(For origami, swap the physicality block wording to "real physical folded paper" / "crisp crease lines, folded edges showing paper thickness.")

**Paper's superpower — material transitions between scenes** (use at setting changes; hard cuts inside a setting): storybook page turn · cut-through push (into a cutout opening) · layer peel · assemble/disassemble (pieces slide out, next scene's pieces slide in) · pop-up unfold · torn reveal · foreground wipe. Prompt language example: `the entire paper scene lifts at one edge and turns like a storybook page, revealing the next scene beneath`.

**Paper failure fixes:** vector drift → physicality block + "everything in frame is real photographed paper" · framed-box/workbench view → strike craft-object words, add interior camera · collage reads flat-lay → background must be scenery (sky, street, room), never a board · faces/labels blur → "papercraft" phrasing + attach references · motion smooths → name the judder cadence · "stop motion" alone drifts to claymation → always pair with "paper."

---

## 4. Crochet / knitted diorama

**Communicates:** handmade coziness with absurdist charm; extremely scroll-stopping for personal care/fragrance/home.

**Master frame:** every scene is a fully handmade crocheted and knitted miniature stop-motion world. **Frame the WORLD as the diorama — never describe "a crocheted man" or "knitted skin"** (inconsistent results); the diorama framing carries yarn texture onto characters automatically. (Note: "diorama" is CORRECT here, unlike paper — yarn worlds don't suffer the exterior-view failure the same way; keep the scene filling the frame regardless.)

**Universal positive (append to every image prompt, verbatim):**
> The entire scene is fully crocheted and knitted — every surface, character, object, and skin is made of visible yarn stitches and fabric loops. No realistic skin, no smooth surfaces, no photorealistic textures anywhere in the frame. Every element, including hands, arms, faces, and backgrounds, must have visible knit and crochet stitch texture throughout. Stop-motion animation diorama scene, handmade knitted and crocheted miniature world.

**Universal negative (for models that support it — Seedream):**
> realistic skin, smooth skin, photorealistic hands, photorealistic faces, realistic textures, smooth surfaces, CGI render, claymation, clay texture, Pixar style, Disney style, 3D animation, plastic texture, flat cartoon, airbrushed, anime, illustrated, 2D, studio lighting, ring light, HDR, symmetrical lighting, harsh shadows, perfectly exposed.

**Universal video-prompt closing line (end every I2V prompt, verbatim):**
> Ensure the entire scene remains fully crocheted and knitted throughout every frame — all characters, objects, and surfaces must retain visible yarn stitch texture with no realistic or smooth surfaces at any point. Non-CGI. Non-cinematic. Animations must start at the first frame. Non-disney.

**Lighting: ONE motivated source per scene** — pick a template: daytime indoor `soft natural light from a small diorama window to the left` · bar/evening `warm motivated light from tiny knitted overhead pendant lamps` · night street `warm soft glow from tiny crocheted streetlamps` · bathroom `soft cool flat natural light from a window to the left` · outdoor day `soft diffused daylight from above-left` · cozy living room `warm lamplight from a tiny knitted floor lamp`. Never: studio lighting, ring light, HDR, harsh shadows.

**Battle-tested limitations:**
- Simplify poses: standing, sitting, single-arm gestures, leaning, walking. No finger work or two-handed object manipulation (yarn hands fail).
- Particles/mist/vapor fail (render as CGI smoke). Replace with **a small handful of yarn-ball orbs** in product-matching colors (amber=scent, blue=hydration, green=freshness, gold=energy, white=purity) that drift, bob, hover — never burst. Before-states: orbs fade; after-states: orbs persist.
- Scent/evaporation moments: use **character-based storytelling** instead of particles (sniffs wrist + grimaces → lifts collar + smiles).
- Image prompt order: scene description → universal positive → lighting template → universal negative → product reference tag (attach real product photo when in shot).
- Video prompt order: primary motion → secondary stillness → camera (locked / slow push / slow pull only) → universal closing line.

---

## 5. Flat 2D vector animation

**Communicates:** clean app-explainer energy; cheap to iterate at volume; the style app brands (e.g. Liven) run at scale. Weakest emotional texture of the family — wins on clarity and cost, not charm.

**Style block:**
> Flat 2D vector animation style, bold simple shapes, thick clean outlines, limited saturated palette of 4–5 colors, flat shading with subtle grain texture, generous negative space, modern editorial illustration look, non-photorealistic.

**Notes:** motion is slides/pops/wipes (planar, snappy, 0.2–0.4s eases) · characters simplified geometric humans, no lip-sync (narrator-led) · this style tolerates on-screen diagram labels better than any other, but still default text to post · strong fit for the video-explainer workflow's server-side pipeline (see higgsfield-pipeline.md).

---

## The material-swap menu — 16 quick looks

The full breadth of the family: the SAME scene can be re-skinned into any physical-material world, and the material choice alone changes the ad's emotional temperature. Deep lanes above (3D feature, clay, paper, crochet, flat 2D) have their full rulebooks in this file; **every other look below has a complete production kit — locked style block, texture defense, negative, lighting, motion cadence, face/speech verdict, failure fixes — in material-styles.md. When a style is picked from this table, load material-styles.md and use its kit verbatim.** All inherit the universal rules (texture defense, palette lock, camera in scene).

| Style | Anchor seeds | Notes / watchouts |
|---|---|---|
| Pixar-style 3D | §1 above | Lip-sync capable — the talking-character lane |
| Claymation | §2 above | Proven workhorse |
| Felt stop motion | needle-felted wool puppets, visible wool fibers, fuzzy edges, handmade miniature sets, soft practical light | Warmest of all; great for calm/family brands |
| Plush toy | soft plush characters, fabric seams and stitching, embroidered eyes, huggable proportions | Comfort/baby/pet categories |
| Marionette | carved wooden puppet, visible strings, jointed limbs, small theater-stage set, warm stage light | Strings read "being controlled" — useful metaphor |
| Animatronic | lifelike robotic figure, subtle mechanical joints and skin seams, showbiz uncanny | Deliberately eerie; horror-comedy angles only |
| Plastic doll | glossy fashion-doll plastic, molded hair, dollhouse set | Say "vintage fashion doll," never a doll brand name |
| Action figure | articulated joints, matte molded plastic, collector-shelf or blister-pack framing | Masculine/nostalgia lanes |
| Wooden doll | carved and turned wood, visible grain, peg joints, folk-toy warmth | Heritage/craft brands |
| Paper cutout | §3 lane 2 above | Full paper family has 5 lanes |
| Cardboard | corrugated cardboard world, visible flutes, craft-brown hand-cut edges, hot-glue seams | Lo-fi charm; cheap-honest tone |
| Brick-built | plastic building-brick world, studded bricks, minifigure-style characters | Say "plastic building bricks," NEVER the brand name (trademark) |
| Miniature model | tilt-shift scale-model world, model-railway detail, tiny figures | Systems/logistics stories ("your gut as a city") |
| Boxed diorama | handcrafted scene inside a lit display box, museum-diorama staging | The one lane where an exterior box IS the look (unlike paper — see §3) |
| Porcelain doll | glazed porcelain figure, delicate painted features, antique softness | Elegant but eerie-adjacent; premium/heritage only |
| Balloon | everything twisted from balloons, glossy inflated surfaces, visible knots and seams | Maximum absurdist scroll-stop; party/kids/fun brands |

### Style-menu grid generator (show, don't describe)

When presenting style options, generate the menu as ONE image — the brand's own scene swapped through the materials — with `nano_banana_pro` (text rendering handles the labels):

> Create a 4×4 grid image. Every cell shows the exact same scene — [ONE-SENTENCE BRAND SCENE, e.g. "a tired man in a grey robe stirring a green drink at his kitchen counter, morning light"] — each rendered in a different physical material style. Cells left to right, top to bottom: 1 high-end 3D animated feature film style, 2 claymation with visible thumbprints, 3 needle-felted wool stop motion, 4 plush toy with fabric seams, 5 wooden marionette with visible strings, 6 lifelike animatronic robot, 7 glossy vintage fashion doll, 8 articulated action figure, 9 carved wooden doll, 10 flat paper cutout, 11 corrugated cardboard, 12 plastic building bricks, 13 tilt-shift miniature model, 14 handcrafted boxed diorama, 15 glazed porcelain doll, 16 twisted balloon sculpture. Identical composition, palette and lighting mood in every cell so only the material changes. Label each cell with its style name in a small white rounded pill with bold black text at the bottom of the cell.

Ask the user to pick by name, recommend the best fit for the brand in one line, then lock that style's block. (A 3×3 subset grid of the most brand-plausible styles is often the better ask — 16 is the full tour.)

## Custom styles

When the user asks for a look outside this library (felt puppets, LEGO-like bricks*, pixel art, watercolor, brainrot absurdism): build a custom locked block from the same fundamentals — (1) name the material/render world, (2) physicality/texture defense line, (3) camera-inside-the-scene line, (4) palette + lighting, (5) universal negative for what it drifts toward, (6) motion cadence line for video. Lock it and use verbatim like any library style. (*Avoid literal trademarked brand looks — see universal rule 5.)
