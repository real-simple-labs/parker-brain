# Material Style Kits — Full Blocks for the 16-Look Menu

Complete production kits for every material world beyond the deep lanes (3D feature, claymation, paper, crochet, flat 2D — those live in styles.md). Each kit follows the pattern proven in production on paper/crochet/clay, generalized: the blocks marked "verbatim" go word-for-word into every prompt of that ad. Kits 3–16 are extrapolated from those tested patterns — treat first runs as calibration and tighten the block after seeing outputs.

## Shared doctrine (all material worlds)

1. **Frame the WORLD as the material, never the character.** "A world where everything is needle-felted wool" renders a wool-textured character; "a felted man" comes back inconsistent. (The crochet diorama-framing trick, generalized.)
2. **Texture defense in every prompt** — each kit's phrase is its anti-smoothing insurance; repeat it in video action lines too ("the felt arm lifts," "the balloon torso bobs") so texture survives motion.
3. **One motivated light source per scene**, named ("warm lamplight from a tiny workshop lamp on the left"). Never studio/ring/HDR unless the kit says so.
4. **Simple poses.** Standing, sitting, leaning, single-arm gestures. No finger work, no two-handed manipulation — miniature hands fail in every material.
5. **Particles become material-native objects.** Scent/energy/magic clouds render as CGI smoke and break the world. Substitute per material (table below), keep to a small drifting handful, color-matched to the product.
6. **Stop-motion cadence by default** in video prompts: `stop-motion cadence, 12 fps judder, slight frame-to-frame jitter, no motion blur` — exceptions noted per kit (marionette, animatronic, balloon, miniature move differently).
7. **VO-only speech by default** — mouths in these materials don't move; use the mouth-stays-closed constraint from video-prompting.md. Exceptions noted per kit.
8. Everything else from styles.md universal rules applies: palette lock to P1, camera inside the scene, no text in frames, IP-safe naming.

**Particle substitution table:** felt → wisps of dyed wool · plush → tiny pom-poms · marionette → sequins hung on fine threads · plastic/action figure → translucent molded-plastic stars · wooden → curled wood shavings · cardboard → hand-cut cardboard stars on wire · brick-built → translucent round studs · miniature → tiny practical light points · diorama → dust motes in the beam · porcelain → glaze glints (sparse) · balloon → mini balloon orbs · animatronic → indicator LEDs. Crochet's original: yarn-ball orbs. Before-states: they fade; after-states: they persist and drift.

---

## 3. Felt stop motion

- **Reads as / best for:** the warmest lane of all — handmade care, softness, family/wellness/sleep brands, gentle problem stories.
- **Style block (verbatim):** `Needle-felted wool stop-motion scene — every character, object and surface needle-felted from dyed wool, visible wool fibers and fuzzy halo edges catching the light, slightly uneven handmade surfaces, miniature handcrafted set, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Everything in frame is real felted wool, photographed — individual fibers visible, fuzzy silhouette edges, matte dense wool, no smooth surfaces, no plastic sheen anywhere.`
- **Negative:** smooth skin, plush velour fur, clay texture, CGI render, 3D animation, plastic, glossy surfaces.
- **Light:** soft warm practical light with gentle falloff (window or tiny lamp).
- **Motion:** 12 fps judder; subtle frame-to-frame fiber shimmer ("fiber boil") is authentic — allow it; slow gestures, head tilts, gentle leans. No fast action.
- **Faces & speech:** bead or felt-dot eyes, stitched mouth. VO-only, mouth never moves.
- **Watch for:** drifts to plush toy (rounder, furrier) → strengthen "needle-felted, dense matte wool"; video smooths fibers away → repeat wool words in every action line.

## 4. Plush toy

- **Reads as / best for:** comfort, baby/kids, pets, cozy self-care; disarming comedy when adult problems live in a soft-toy world.
- **Style block (verbatim):** `Plush toy world — every character a soft stuffed plush with visible fabric weave and stitched seams, embroidered eyes and nose, huggable toy proportions with stubby limbs, oversized soft props, cozy fabric textures on every surface, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Everything in frame is real stuffed plush, photographed — fabric weave, stitched seams and slight fur pile visible, shapes softly deformed under their own weight.`
- **Negative:** hard plastic, felted wool, clay, realistic anatomy, CGI smoothness.
- **Light:** warm and even, nursery-soft.
- **Motion:** squeeze-and-settle deformation, gentle bobbing hops; plush tolerates slightly smoother motion than felt (puppet-like rather than strict 12 fps). Comedy variant: muppet-style flap-mouth IS allowed here (the one soft-material lip-sync exception) — commit to it fully or stay VO-only.
- **Faces & speech:** embroidered features or safety eyes. Default VO-only; flap-mouth for comedy formats.
- **Watch for:** anatomical drift → "toy proportions, stubby limbs, no fingers"; fur reads CGI → "photographed real plush, visible stitching."

## 5. Marionette

- **Reads as / best for:** control and manipulation metaphors — the built-in villain device ("your cravings pulling the strings"); heritage-theatrical brand tones.
- **Style block (verbatim):** `Marionette theater scene — carved wooden puppets with visible taut control strings rising out of the top of frame, jointed limbs with visible articulation gaps at elbows and knees, painted wooden faces with worn paint, miniature theater stage with painted canvas backdrops, warm stage lighting from the footlights, fine dust in the light beams, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real carved wood and string, photographed — wood grain and paint wear visible, strings always present and taut, stage boards beneath every character.`
- **Negative:** missing strings, smooth 3D animation, human skin, organic bending limbs.
- **Light:** warm stage light, low angle, gentle haze.
- **Motion:** NOT 12 fps judder — marionettes swing smoothly with pendulum weight: limbs dangle and settle after each move, slight bounce on landings, head tilts on a delay. Write the strings into the motion ("the strings lift its arm; the hand settles with a small swing").
- **Faces & speech:** painted, static. VO-only (a hinged jaw variant exists but reads ventriloquist — only if the concept wants that).
- **Watch for:** the model deletes the strings → name them in EVERY prompt; limbs bend organically → "rigid jointed limbs, articulation gaps at the joints."

## 6. Animatronic

- **Reads as / best for:** deliberate uncanny — horror-comedy angles, "the old way is a machine pretending to care," retro theme-park nostalgia. Use sparingly; it unsettles by design.
- **Style block (verbatim):** `Vintage animatronic show scene — a lifelike robotic character with subtly wrong smoothness, visible skin seams at the jaw and neck, exposed servo joints at the wrists, glassy unblinking eyes, staged on a themed show-set with spotlight pools and worn carpet, the scene filling the entire frame.`
- **Texture defense (verbatim):** `A real animatronic figure, photographed — silicone skin with seams, mechanical joints visible, glassy reflective eyes, show-set staging.`
- **Negative:** fully human realism, warm organic motion, cartoon proportions.
- **Light:** hard spotlight pools, dark surround.
- **Motion:** stiff, slightly delayed; head turns that overshoot and correct; a repeated idle sway loop reads authentic. This is the ONE material where visible jaw-flap lip-sync is the aesthetic — deliberately imperfect, slightly out of time. Mechanical servo whirs belong in the audio.
- **Faces & speech:** jaw-flap lip-sync allowed and encouraged; eyes never blink.
- **Watch for:** reads as just a person → push seams, servos, glassy eyes; too horrifying for the brand → warm the light, slow the motion, add dust-mote nostalgia.

## 7. Plastic doll (vintage fashion doll)

- **Reads as / best for:** beauty/lifestyle satire, "picture-perfect life" irony, dollhouse domesticity. Strong for female-skewing DTC with a wink.
- **Style block (verbatim):** `Vintage fashion doll scene — glossy molded-plastic dolls with painted faces, rooted synthetic hair, visible mold seams and stiff doll joints, staged in a pastel dollhouse set with miniature plastic furniture and printed cardboard backdrops, bright even toy-catalog lighting, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real plastic dolls, photographed — glossy specular highlights on molded plastic, rooted-hair strands visible, dollhouse scale cues in every prop.`
- **Negative:** any doll brand name, human skin, clay, cartoon render.
- **Light:** bright, even, toy-catalog (the deliberate exception to moody practicals).
- **Motion:** stiff-jointed stop-motion poses — hop-pivots, arm raises from the shoulder only; rooted hair sways a beat late.
- **Faces & speech:** painted, frozen smiles. VO-only — the frozen face against a confessional VO line is the joke.
- **Watch for:** trademark drift → never name doll brands, avoid signature logos/faces; CGI-toon drift → "photographed real plastic doll."

## 8. Action figure

- **Reads as / best for:** masculine nostalgia, fitness/energy/grooming, "assemble your loadout" collector energy, hero-journey escalations.
- **Style block (verbatim):** `Action figure scene — articulated plastic action figures with visible ball joints and panel lines, matte molded costume detail with painted edge wear, posed dynamically on a detailed miniature playset, dramatic hobby-photography lighting with practical haze and debris, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real action figures, photographed — visible joints, matte plastic with paint wear, toy-photography depth of field.`
- **Negative:** video-game CGI, live-action human, smooth seamless skin.
- **Light:** dramatic, low-key, rim-lit, haze.
- **Motion:** heroic pose → snap to next pose (toy-photography stop-motion); tiny debris and flash-paper practicals; low orbiting camera. Fights and stunts work HERE better than any other material — pose-to-pose reads as intended style, not failure.
- **Faces & speech:** molded. VO-only; the stoic frozen face suits gravelly narrator formats.
- **Watch for:** drifting into real CGI character → "photographed toy, visible articulation."

## 9. Wooden doll

- **Reads as / best for:** heritage, craftsmanship, "made the old way," premium simplicity; grandparent-warm storytelling.
- **Style block (verbatim):** `Carved wooden doll scene — figures turned and carved from wood with visible grain and tool marks, peg joints, painted folk-art details worn soft at the edges, miniature wooden furniture, warm workshop lighting, faint sawdust in the air, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real carved wood, photographed — grain, tool marks and worn paint visible on every surface, peg-jointed limbs.`
- **Negative:** smooth plastic toy, clay, CGI, glossy varnish everywhere.
- **Light:** warm workshop lamp or window light.
- **Motion:** 12 fps judder; stiff pivots at peg joints; rocking side-to-side walks; heads rotate as one piece.
- **Faces & speech:** painted, static. VO-only.
- **Watch for:** smooth-toy drift → "visible grain and tool marks"; too rustic/rough → "folk-art painted details, lovingly worn."

## 10. Cardboard

- **Reads as / best for:** lo-fi honest charm, startup/budget energy, "no fancy packaging, just the product" angles, playful DIY comedy.
- **Style block (verbatim):** `Cardboard world scene — everything hand-cut from corrugated cardboard, visible flutes on every cut edge, craft-brown surfaces with marker and paint details, hot-glue seams and tape joints, slight warps and bends, the scene filling the entire frame with the camera inside the cardboard world.`
- **Texture defense (verbatim):** `Real corrugated cardboard, photographed — raw cut edges showing the flutes, tape and glue visible, hand-cut imperfection everywhere.`
- **Negative:** clean vector, thin paper cutouts (that is the paper lane), plywood, plastic.
- **Light:** soft daylight or single desk lamp; shadows show the flutes.
- **Motion:** planar slides and hinge-folds like paper, plus cardboard's own move — panels wobble and flex when they land; 12 fps judder.
- **Faces & speech:** marker-drawn features. VO-only.
- **Watch for:** merging with paper cutout → "thick corrugated cardboard, visible flutes on the cut edges."

## 11. Brick-built

- **Reads as / best for:** construction/assembly metaphors ("your routine, built one brick at a time"), family-friendly comedy, systems explainers. **IP: say "plastic building bricks / brick-built" — NEVER the brand name, no branded logos or signature minifig faces.**
- **Style block (verbatim):** `Brick-built world scene — everything constructed from generic plastic building bricks with visible studs on every surface, glossy molded brick-people with cylindrical heads, simple printed faces and claw hands, modular brick furniture and vehicles, bright even lighting, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real plastic building bricks, photographed — studs visible, glossy molded plastic, seam lines between bricks.`
- **Negative:** brand names/logos, clay, smooth CGI characters, realistic humans.
- **Light:** bright and even.
- **Motion:** authentic brickfilm grammar — characters slide and hop, arms pivot at shoulders only, expressions change by stop-motion face-swap between frames, and the signature move: objects ASSEMBLE brick-by-brick (the perfect mechanism/transformation visual). 12–15 fps stepping.
- **Faces & speech:** printed faces; expression swaps yes, lip-sync no.
- **Watch for:** drifting into the trademarked look → generic bricks, invented face prints, no recognizable sets.

## 12. Miniature model (tilt-shift)

- **Reads as / best for:** systems stories — "your gut is a city at rush hour," supply chains, before/after world states; awe-scale product claims.
- **Style block (verbatim):** `Tilt-shift miniature model world — a hyper-detailed scale-model scene photographed with shallow tilt-shift focus, model-railway trees and tiny figures, working miniature lights, visible model-maker detail, the camera hovering inside the miniature world like a giant observer.`
- **Texture defense (verbatim):** `A real handbuilt scale model, photographed — tilt-shift blur bands, model-railway textures, tiny painted figures frozen mid-stride.`
- **Negative:** real-world footage, full-size photography, CGI cityscape.
- **Light:** miniature practicals (tiny streetlights, window glows) + soft overhead.
- **Motion:** the world is the character — slow crane and aerial drifts over the model; tiny vehicles crawl; lights flicker on in waves. Human figures stay frozen or barely move (authentic to the medium).
- **Faces & speech:** figures too small for faces. Narrator formats only.
- **Watch for:** becoming live-action aerial footage → "scale model, tilt-shift focus bands, model-railway detail."

## 13. Boxed diorama

- **Reads as / best for:** chaptered stories (each box = one beat, era, or symptom), collections, memory/nostalgia, museum-of-your-life concepts.
- **Style block (verbatim):** `Handcrafted boxed diorama scene — a miniature world built inside a warmly lit wooden display box, layered depth from foreground props to a painted backdrop, tiny practical lights inside the box, museum-diorama staging, dust motes in the light.`
- **Texture defense (verbatim):** `A real handcrafted diorama, photographed — visible craft materials, painted backdrop brushwork, miniature props with handmade imperfection.`
- **Negative:** CGI, full-size rooms, video-game render.
- **Light:** the box's own tiny practicals; dark surround.
- **Motion:** the signature grammar — open on the box exterior, PUSH IN until the world fills the frame, then treat the interior like a miniature model; transition between beats by pulling out of one box and into the next (box-to-box = this material's page-turn). Unlike paper (where an exterior view is a failure), here the box IS the aesthetic — but spend most screen time inside.
- **Faces & speech:** figures mostly still. Narrator formats.
- **Watch for:** the camera never entering (whole ad shot from outside) → storyboard interior shots explicitly.

## 14. Porcelain doll

- **Reads as / best for:** heirloom/premium/fragrance, antique elegance; deliberately uncanny angles when the concept wants a shiver. Narrow lane — confirm brand appetite first.
- **Style block (verbatim):** `Porcelain doll scene — glazed porcelain figures with delicate hand-painted faces, fine crazing in the glaze, lace and fabric costumes, antique dresser and lace-curtain staging, soft window light, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real glazed porcelain, photographed — glaze sheen with fine crazing lines, hand-painted features, fabric costume texture against the hard porcelain.`
- **Negative:** horror staging (unless wanted), clay, plastic doll gloss, human skin.
- **Light:** soft window light, gauzy.
- **Motion:** nearly still — slow head turns as one piece, fabric stirs in a draft, camera does the emotional work; music-box audio pairing is the natural fit. Painted eyes never move.
- **Faces & speech:** painted, static. VO-only.
- **Watch for:** unintended horror drift → warm the light, add lace and softness, slow everything; intended horror → cool the light and let stillness linger.

## 15. Balloon

- **Reads as / best for:** maximum absurdist scroll-stop; party/kids/fun brands — and energy stories: a balloon person slowly DEFLATING through the afternoon then re-inflating is a complete before/after mechanism in one image.
- **Style block (verbatim):** `Balloon sculpture world — every character and object twisted from glossy latex balloons, visible knots, seams and pinch points, squeaky inflated volumes, saturated party colors, clean bright set, the scene filling the entire frame.`
- **Texture defense (verbatim):** `Real inflated latex balloons, photographed — specular sheen, slight translucency where light passes through, twist-knots visible at every joint.`
- **Negative:** CGI blobs, plastic, rubber toys, matte surfaces.
- **Light:** bright soft key + colored bounce from the balloons themselves.
- **Motion:** buoyant bobbing, squeaky twists, gentle bounces with overshoot — smooth and floaty, NOT 12 fps judder. Deflate/inflate = the built-in transformation verb; a pop is the catastrophe beat (use once, if ever).
- **Faces & speech:** marker-dot eyes on the balloon head. VO-only.
- **Watch for:** CGI-blob drift → "real latex, knots and seams visible"; over-popping (reads violent) → deflation over destruction.

---

**Numbering note:** kits 1–2 (3D feature, claymation) and the paper/crochet/flat-2D lanes live in styles.md with their deeper production rulebooks. The style-menu grid generator in styles.md renders all 16 side-by-side for the user to pick from.
