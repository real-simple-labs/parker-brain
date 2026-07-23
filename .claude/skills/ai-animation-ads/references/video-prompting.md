# Video Prompting — Animating the Storyboard

Each approved image becomes the start frame of one clip. The image already carries the full visual style, so video prompts describe ONLY motion, camera, dialogue/audio, and any state change. Short prompts animate cleaner than long ones. If a clip fails twice, simplify: cut background animation, reduce to one movement, shorten the dialogue.

**The ad's structure is decided before this doc opens.** Runtime, story architecture, beat map, the natural product handoff, cut cadence (fast–slow–fast, no metronome, one proof hold), layer-two pacing, and the audio spine all come from the canonical structure doctrine at `creative-strategy-context/ai-video-ad-structure.md` — grounded in the 231-creative AI Animation corpus study. This reference governs per-clip animation only: it animates a shot list that already exists. An 8-second generation cap is never the ad length.

## The director's decision — how many frames does each scene need? (run per shot)

- **Type A — start frame only, self-contained motion.** The action happens and resolves within the clip (vapor drifts and fades, character delivers a line and settles). Scene ends in the same visual state. → one image + a motion-arc prompt. **Default when unsure** — modern I2V handles full arcs from one keyframe.
- **Type B — start + end frame, state change.** Scene begins in one state, lands in a different stable state (bottle on counter → bottle in hand; neutral face → grimace). → start image + end image + a transition prompt. The end frame is the FINAL LANDED state, never mid-motion ("hand reaching" is wrong; either resolve it or reclassify as Type A). Start/end pairs are also how blended continuous ads are built: shot N's end frame = shot N+1's start frame.
- **Type C — start frame only, held shot.** Hero poses, product glows. → one image + subtle-motion prompt (breathing surface, drifting particles, slow push).

**One action per clip.** One camera move + one subject action + at most one background element. Overloaded prompts are the #1 cause of chaotic motion and wasted regens. Sequences = more clips, not longer prompts.

## Universal prompt skeleton

```
[ANIMATE INSTRUCTION] + [CHARACTER + DIALOGUE or VO-CONTEXT] + [MOVEMENT/BODY LANGUAGE]
+ [BACKGROUND ANIMATION — optional] + [CAMERA] + [STYLE CLOSER]
```
- **Style closer:** repeat the ad's locked style line identically in every clip prompt ("Pixar-style 3D animation" → use the ad's locked descriptive block name; "handmade stop-motion claymation"; the paper cadence line; the crochet closing line). Changing the wording between shots triggers different interpretations — verbatim repetition is the consistency mechanism.
- **Clip length = its VO line length** (most lines 2–5s; talking-character clips 5–10s). Match the model's duration param to the spoken length; trim dead tail frames in the edit.
- **Aspect:** 9:16 for paid social unless told otherwise.

## Talking characters (lip-sync formats — 3D/Pixar-style only)

Include the EXACT dialogue line — that's what drives lip-sync; without it you get generic mouth-flapping.

```
Animate this [BRIEF CHARACTER ID] talking [DELIVERY STYLE] to camera saying
"[EXACT DIALOGUE]". The [CHARACTER] [1–2 movement beats matching its energy].
[Optional background beat]. [Style closer].
```
- Delivery styles: directly / confidently / calmly / softly / with upbeat energy / with smug energy / nervously / delivering a confident closing line.
- **Delivery direction is part of the prompt.** If the villain sounds timid, re-prompt the energy ("assertive, menacing, taunting"), don't just re-roll.
- Multi-character frames: name who speaks; state that the others' mouths are closed, listening, reacting silently — or every face animates.
- Mascot rule: lip-sync works when the character has a visible mouth/jaw and roughly human facial proportions. No face = no lip-sync; make it a VO shot.
- Native audio gives a *different voice per clip*. For a recurring character across many clips: keep native audio if close enough per clip, or generate clips silent and apply one fixed voice with the lipsync tool (`sync_so` on Higgsfield) or mute + layer ElevenLabs and accept off-sync (acceptable in this genre).

**Movement vocabulary by archetype** (pick 1–2 per clip):
- *High-energy / villain:* shakes and vibrates with nervous energy · fidgets and shifts restlessly · liquid inside sloshes and surges · steam bursts erratically · eyes dart anxiously · shrugs mid-delivery as if confessing without remorse · leans toward camera as if getting in your face · cracks and crumbles slightly · wobbles as if barely holding it together.
- *Calm / hero:* surface subtly sways and breathes · glow softly pulses with each word · stands tall, subtle weight shifts · barely moves, calm presence · nods slightly with quiet confidence · warm glow radiates as it speaks · small confident gestures.
- *Product reveal:* supporting characters shift subtly and look toward the product · warm golden light gently brightens on its line · lid moves slightly as if alive · glances off-screen then back to camera.
- *Proof/CTA:* golden stars shimmer · review counter softly pulses · delivers the final line with a slight knowing smirk.

**Background animation** (optional, one max): neural pathways illuminate one by one · energy wave flows left to right · calming aura expands and breathes · energy graph pulses then crashes · light particles drift upward like embers · ingredient molecules float gently · shield barrier shimmers and solidifies · environment gradually brightens/darkens · background settles like a deep exhale.

## Voiceover-only formats (narrator-led, character-follow, ALL claymation/paper/crochet)

Never paste dialogue without the constraint — models lip-sync whatever is quoted. Describe the VO as context, then prohibit speech:

```
Animate this [CHARACTER]. [Eye/body movement matching the emotional beat — never mouth].
As a [TONE] voiceover says "[LINE]", [subtle scene/prop movement matching the beat].
The character's mouth stays closed, no lip-sync, no speaking on screen.
[Supporting characters remain still]. [Lighting note]. [Style closer].
```
- Sung-VO variant: characters move rhythmically (small bobs, sways, eye shifts on the beat) but never sing on screen.
- Character-follow: the character is a body in motion or being observed (walking, slumping, sleeping, shown in cross-section) while the narrator speaks.
- Claymation locomotion: full walking gaits come back jittery — prefer in-place motion (shudder, twitch, lurch, slump).
- Paper: all motion planar (slide, pivot, parallax push); name the stop-motion cadence every time.
- Crochet: end every prompt with the universal closing line (styles.md §4); camera locked / slow push / slow pull only.

## Transitions between scenes

- Default: hard cuts in the edit (free, reliable).
- Soft mix dissolves 0.5–0.7s between dialogue beats.
- **Generated transition clip:** `Create a seamless [STYLE] animated transition between the first shot and the second shot, with sound effects. No talking, no character lip-sync.` — start frame = last still of scene A, end frame = first still of scene B. This is the blended-continuous-ad technique; it's harder than it looks (be intentional about what can physically blend), so don't attempt it on a first ad.
- Paper styles: use the material transitions catalog (styles.md) — page turn, layer peel, pop-up unfold, torn reveal.
- Never write literal set morphs ("kitchen reshapes into bedroom") — models break; cut or dissolve instead.

## Model playbook (Higgsfield model ids · July 2026)

| Model | Use for | Key mechanics |
|---|---|---|
| `kling3_0` (std/pro/4k, 3–15s, start+end, sound on/off) | **Default finisher** for talking characters and hero clips | Prompt: camera → subject+action → environment → texture → audio/emotion. Dialogue syntax: `[Character: old bathroom scale, deep smug voice]: "line"`. Native audio is the most expressive (multi-voice, even singing). Multi-shot: label `Shot 1: … Shot 2: Cut to…` — ceiling 3–4 beats/15s; keep prompt density even across shots. Draft in `std` (often better adherence), finish in `pro`. |
| `kling3_0_turbo` (720/1080p, 3–15s, start frame) | Cheap drafts, timing tests | Same prompting, faster/cheaper, tighter lip-sync than std at 720p. |
| `kling2_6` (5/10s, start frame, sound) | Budget lip-sync fallback | Structure: scene → characters → action → camera → dialogue → ambience → avoid-list. |
| `seedance1_5` (4/8/12s, start+end, `generate_audio` bool) | **Cheap first passes** on every clip | Four layers: subject+action · quoted dialogue (triggers lip-sync priority) · environment audio cues · style/mood. It auto-adds music — pass `generate_audio: false` for silent (cheaper) or write "no music, only raw SFX". Loves stylized stills. |
| `seedance_2_0` / `_mini` (4–15s, refs: image/video/audio, 4k) | **Consistency king** for stylized/animated ads | @mention rig: attach refs, then `@Image1 as the first frame`, `@character keeps consistent appearance`, `@Video1` = motion/cadence transfer (feed a real stop-motion clip to lock claymation cadence), `@Audio1` = beat sync. Declare structure up front: `Total: 15s / 3 shots / 9:16`, then `Shot 1: …`. First 20–30 words carry the most weight. |
| `veo3_1` / `veo3_1_lite` (4/6/8s; lite has start+end) | Premium cinematic beats; VO-only B-roll | Formula: cinematography → subject → action → context → style + audio layers (`SFX: …`, `Ambient noise: …`). **Dialogue via the colon trick** — `The mascot says: line here` with NO quotation marks (quotes trigger burned-in subtitles) + append `(no subtitles)` and `no subtitles, no text overlays, no captions, no watermark`. `Narrator: 'line'` renders VO without lip-sync. Timestamp multi-shot: `[00:00-00:02] … [00:02-00:04] …`. Phrase exclusions positively. Always specify ambience or it hallucinates audience laughter. |
| `minimax_hailuo` (6/10s) | Cheapest expressive character motion | Describe ONLY motion, never re-describe the image; full sentences with strong verbs, no comma-tag lists; don't request wider framing than the input. |
| `wan2_7` (2–15s, start+end+audio ref) | Budget control play | First+last frame + audio reference (identity/voice lock); cheapest per second. |
| `sync_so` (Sync Lipsync 3) | Post-hoc lip-sync | Re-voice a finished clip with a fixed ElevenLabs/seed_audio take (input_video + input_audio; sync_mode bounce/loop/cut_off/silence/remap). |
| `topaz_video` / `bytedance_video_upscale` | Finishing | 2x upscale to 4K/60fps after assembly (Bytedance preset `aigc` suits AI footage). |
| `video_deflicker` · `reframe` · `video_background_remover` | Utilities | Fix stop-motion flicker · convert 9:16↔16:9/1:1 for placements · cutouts. |

**Cost ladder & discipline:** test motion on `seedance1_5`/`kling3_0_turbo`/`minimax_hailuo` at 480–720p short durations → regenerate only winning shots on `kling3_0` pro / `veo3_1` / `seedance_2_0`. Budget 2–3× the nominal clip count for rerenders. Preflight every batch with `get_cost: true` and check `balance` before starting a full ad (a 15-clip ad on premium models can run hundreds of credits). Never batch-fire all clips on a premium model before ONE clip has validated the style's motion.

## Anti-realism-drift kit (stylized content)

- Repeat the style descriptor first and identically in every clip prompt.
- Character face lock in every clip prompt: `keep the character's exact facial features — no character redesign, no eye or face changes`. Video models re-interpret faces during animation (verified in production: Kling rounded a hero frame's heavy-lidded eyes into wide-open ones; the cheaper Seedance draft held the face). Compare draft-tier outputs across models before committing the final tier.
- Claymation cadence: `visible clay texture and thumbprints, slightly stuttery 12fps stop-motion feel, animation on 2s, subtle frame jumps, miniature handcrafted set` + locked-off tripod (`camera_fixed: true` on Seedance) for authentic stop-motion.
- Paper: `stop-motion cadence, 12 fps judder, slight frame-to-frame jitter, no motion blur`.
- Negative/exclusion line for all animated work: no photorealism, no live-action, no lip-sync (where applicable), no subtitles, no text overlays, no watermark.
- Speed mapping happens in post (2–2.5x Pixar-style, 1.5–2x clay, 1.3–1.7x sung clay) — never prompt for speed.
