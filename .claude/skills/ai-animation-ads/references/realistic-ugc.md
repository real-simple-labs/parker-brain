# Realistic AI UGC — the start-frame method

The realism counterpart to the animation lanes: photorealistic creator-style talking-head video (UGC, testimonial-style presenter, demo-to-camera). Source: practitioner guide (2026-07) on Gemini Omni UGC workflows, encoded near-verbatim; execution routing adapted to this stack. The animation lanes drop defenses with charm; this lane wins when the format itself IS the message — "a real person like you uses this." It pays for that realism with the heavier platform AI-disclosure label (SKILL.md hard rule on AI disclosure applies in full here).

## RULE ZERO — the reference is the whole video, not its first frame

## THE THREE REVIEWS (owner law — every UGC ad runs all three, as agent passes)

1. **STRATEGY REVIEW** (pre-adaptation, on the reference pick + segment map): does this align with what OUR brand is trying to achieve? Is the reference's MECHANIC AVAILABLE to us — or is it built on attacking our own category position (a gummy brand's "powders taste like a lawn" slam cannot be transplanted INTO the powder brand's mouth)? Is every product, prop, and SKU in the map VERIFIED against the brand vault (never model memory — a hallucinated SKU is a killed ad)? How exactly does each beat adapt for our brand? Run the strategy reviewer agent; REVISE or KILL before any script work.
2. **SCRIPT REVIEW** (pre-spend): voice, AI-isms, human-sounding register, presenter zone, claims — the creative-voice-review + ai-writing-tells pass already specified in gate 0.
3. **EDIT REVIEW** (post-assembly, pre-delivery): the `ugc-edit-reviewer` agent on the assembled master + cut plan — cut integrity (no clipped words), gesture-word sync (a salute lands ON "Scout's honor", never before it), action-referent order, dead air, caption sync, retention pacing, delivery specs. Nothing ships on an unreviewed edit.

Owner-graded lesson (a first-frame-only recreation earned a D-minus): recreating a winner from its first frame strips everything that made it win — the arc, the actions, the on-screen text, the length. Before any plate:

1. **Pull the reference's full anatomy:** rip frames every ~2s and VIEW them; pull its script, storyboard, on-screen-text track, and length (the ad-library analysis when the ad is tracked).
2. **Read the true camera grammar from the frames** (propped-static vs handheld vs selfie-arm) — never import a grammar the reference doesn't have; a misread thumbnail becomes a fake-looking foreground limb.
3. **Build the segment map:** one row per scene — time range · shot · physical action · spoken line · on-screen caption.
4. **Adapt segment by segment** with the scriptwriting/adaptation doctrine: keep each segment's MECHANIC, swap in the brand's truths, and run every adapted line through the claims gates (the reference's claims are not your brand's claims). Two hard sub-rules: **mechanic availability** — a beat built on attacking our own category position is unavailable, full stop; and **vault-verified props** — every SKU/product/prop in the map is confirmed from the brand vault or live site, never from memory.
5. **Every segment gets a physical product action** (grab, shake, open, scoop, pour, sip, show). A static talking head is a zoom call, not an ad.
6. **One plate per segment** (HERO-referenced for identity continuity), one clip per segment, then captioned assembly. A single clip is a hook test, never a delivered ad; the ad's length is inherited from the segment map.

## The core doctrine: slop in, slop out

**The starting frame is the foundation of everything.** If the starting frame looks like AI slop, the video will look like AI slop. If it looks real, the video has a real chance. Spend the iteration budget on the frame, not on video re-rolls — frames cost cents, video costs real credits. This is the same start-frame-first discipline as the animation pipeline (Stage 4 before Stage 5), applied to photorealism.

## The three input methods (and the one to default to)

| Method | Control | When |
|---|---|---|
| Text-to-video | Lowest — the model invents everything | Throwaway b-roll only |
| Ingredients-to-video (reference images) | Medium — strong for combining assets, but **the product drifts**: the model interprets the reference and renders something *like* it, not it | Only when no single frame can hold all the assets |
| **Frame-to-video** | Highest — the video follows exactly what is in the starting frame: product stays consistent, character stays consistent | **The default for everything**, especially product-in-hand |

Tested side by side: frame-to-video with the product placed in the starting frame beats ingredients-to-video on product accuracy. Even when you have product reference images, put the product IN the frame rather than feeding it as an ingredient.

## Building the starting frame

### Step 1 — real reference, always

Never prompt a UGC frame from scratch; that is the difference between realistic output and obvious AI. Hunt a real reference:

- TikTok: search "UGC" for general creator-style content, or the niche ("skincare", "supplements", "fitness"). Find a video whose lighting, composition, and person fit — someone who would actually promote this product category (persona-fit is a gate, not a preference; wrong-persona references fail the reference-fit scorecard same as statics).
- Pinterest works the same way for aesthetic references.
- Screenshot the **first frame** of the chosen video. That screenshot is the reference.

### Step 2 — extract a JSON prompt with a reasoning vision model

Upload the reference screenshot to a **thinking-enabled** vision model and use this exact prompt:

> "give me a very detailed JSON prompt to recreate this image one to one. ignore all text and buttons on the screen."

- "ignore all text and buttons" strips the TikTok/Pinterest UI chrome out of the description.
- A reasoning model analyzes the image before writing; non-reasoning models transcribe the surface and the detail gap shows in the render.

**Likeness gate (non-negotiable):** the screenshot is a composition/lighting/styling reference ONLY. Before generating, swap the person's identity in the JSON to a generic synthetic description (age range, vibe, styling — not the real creator's face). The shipped frame must be a generated synthetic person; a real creator's likeness never ships without a signed release. Same rights sweep as every other lane.

### Step 3 — generate the frame in a FRESH context

- Do **not** generate in the same chat/context that analyzed the reference — it still holds the original image and recreates it too literally (which is both a quality and a likeness problem). Open a fresh context.
- Paste the JSON **as text** (not as a code attachment), request **9:16** for vertical.
- In-stack: run the JSON through the primary statics image model via the Higgsfield MCP (image-prompting.md model table; the technique is tool-agnostic — the source guide uses GPT Image 2, any letter-perfect photorealistic model works).
- **Product placement:** prompt the product into the frame ("she holds the [product]") with the product packshot attached as reference media. The frame locks it; frame-to-video keeps it.
- The frame passes the design/reality review (review-gates.md — reality pass, perfection kill, persona fit, label OCR at zoom) BEFORE any video credits are spent. A killed frame costs cents; a killed clip costs credits.
- **Micro-print floor:** 2K plates garble label print below ~4px. Acceptable for VIDEO when sub-legible at delivery scale; for STATICS (pinch-zoomable) composite the real packshot label block onto the plate instead.

## Generating the video

The prompt is simple — the frame already did the work:

> make her say "[dialogue]"

- **Dialogue budget ↔ duration:** too much dialogue in too short a clip and the character talks unnaturally fast. Conversational pace is ~2.3 words/sec: a 10s clip holds ~20–25 words, a 4s clip ~9. Time the script lines (scriptwriting.md pacing) before setting duration, not after.
- 10s is the workhorse duration; shorter only when the line is genuinely short.
- **The last second is sacrificial:** frame-to-video models love to invent a reach-to-camera end-recording gesture on selfie clips, smearing the product in the final ~0.5–1s. Never place payoff dialogue after T-1s; direct "finishes speaking with a beat to spare, holds the pose, no ending gesture"; plan the edit cut before the gesture — and any QA claim of "legible to the end" gets checked against the true final frames, not the contact sheet.
- **Dialogue is speech calibrated to the reference transcript:** a grammatically clean copy line spoken aloud is an AI tell — but so is performed casualness (scripted ums/likes, directed laughs: "cheesy"). The ruler is the REFERENCE'S OWN TRANSCRIPT: count its actual filler words and match its register. Most winning UGC is casual through STRUCTURE, not filler — short reactive declaratives, contractions, real-time discovery ("okay, that's actually pretty good"), honest asides ("not gonna lie") — often with zero ums. Add filler only where the reference's transcript itself uses it. Protect the final wording through generation ("says exactly these words and nothing else") and keep delivery directions plain — no directed laughs or performed self-deprecation.
- **Dialogue is unverified until transcribed:** prompt enhancers can silently strip the quoted line from the final model prompt on ANY roll (observed: the same prompt kept the dialogue on one roll and dropped it on the next — the model then improvises on-theme lines that can breach claims gates, e.g. an invented literal-completeness claim). Every clip gets transcript-verified word-for-word before it counts as done. On deviation: re-roll with the line framed as "She says exactly these words and nothing else: …" — observed to force the enhancer to preserve the quote verbatim, where a passed `enhance_prompt: false` flag was silently overridden by the backend. Verify the transcript again after the re-roll.

### Execution routing (three paths)

| Path | What it is | Constraints |
|---|---|---|
| **Higgsfield `gemini_omni`** (in-stack, PRIMARY) | Gemini Omni — the realism pick (the source guide's core claim: beats Kling/Seedance for UGC, and native-audio voice quality is the reason). Reference-driven (`image_references` role), 4–10s, 9:16 | Run it frame-anchored by passing the segment's PLATE as the single image reference; OCR the product in review for drift |
| **Higgsfield `veo3`** (fallback) | Frame-to-video with native audio via `start_image` | Use only when strict start-frame control outranks voice — its fast variant's voice failed a human ear; if used, best variant only (`veo-3-preview`) |
| **Google Flow** (manual lane) | Full Gemini Omni — frame-to-video + ingredients + text-to-video at flow.google | Not MCP-connected: deliver the Kit (below) |

**Model tier is never a savings lever** (owner directive): best available model, variant, and resolution, always — draft tiers exist to test motion, not to cap quality. Model catalogs move monthly — run `models_explore` before assuming this table is current.

### Google Flow Kit Mode

When the user runs Flow themselves (or asks for the setup), deliver a paste-ready kit:

- The generated start frames (one per clip), 9:16.
- Per-clip prompt lines (`make her say "…"`) with the duration each dialogue fits.
- **Session plan:** generate ALL clips of a multi-clip video **in one Flow session, back to back** — voice stays consistent within a session and can change across sessions. A 30s video = three 10s clips, same session, no closing the tab.
- **Do not use Flow's built-in character features** — the voices come out robotic. Frame-to-video with your own frames gets the natural native voices.
- Account economics (2026-07, verify before quoting): free tier for testing; Google AI Ultra $200/mo = 25,000 credits; a 4s video ≈ 7 credits, a 10s video < 15 credits — hundreds of videos/mo, vs $150–300 per video for human UGC creators.

### Voice consistency in-stack

The same-session trick is a Flow behavior. In-stack: generate a multi-clip batch in one run and review voice match across clips; if a clip's voice drifts, either re-roll that clip or strip native audio and lay a single ElevenLabs VO across the cut (audio.md) — one voice per role is already the rule.

## The ugly-ad aesthetic (owner law — Barry Hott doctrine)

UGC must look like it was shot on a phone one morning, not in a studio. Polish reads as "ad"; lo-fi reads as "person." The premium look IS the AI tell.

- **Plate prompts — BANNED:** "shallow depth of field", "background blurred", "bokeh", "soft/diffused daylight", "cinematic", "beautiful". **REQUIRED:** deep focus (phone front-camera optics — background as sharp as the subject), a genuinely cluttered lived-in space (dishes in the rack, cords, mail on the counter), mixed household lighting with slightly blown window highlights and mild white-balance drift, slightly off-center framing, visible sensor noise.
- **The ugly finish pass** runs on every assembled master AFTER upscaling (the upscaler's denoise cleans in the wrong direction): sensor grain + slight phone-processing oversharpen + lifted blacks + a crf 27-28 compression crush. Side-by-side with the real reference, the AI clip should match its grubbiness.
- Perceived "quality drop" and "too premium" are the same defect — AI smoothness. Texture restores both realness and perceived sharpness.

## The ugly-ad aesthetic (owner law — Barry Hott doctrine, iPhone-2018 calibration)

UGC must look like it was shot on a phone one morning — specifically a 2018-era phone (Snapchat-2017 vibes): still 1080 HD, but single-exposure camera behavior with none of the modern computational-photography advancements. Polish reads as "ad"; lo-fi reads as "person." The premium look IS the AI tell.

- **Plate prompts — BANNED:** "shallow depth of field", "background blurred", "bokeh", "soft/diffused daylight", "cinematic", "beautiful". **REQUIRED:** deep focus (phone front-camera optics — background as sharp as the subject), a genuinely cluttered lived-in space (dishes in the rack, cords, mail on the counter), hard mixed household light with the window BLOWN OUT (clipped white, no HDR recovery), slight warm indoor white-balance cast, slightly off-center framing, fine sensor noise.
- **The ugly finish pass** runs on every assembled master AFTER upscaling (the upscaler's denoise cleans in the wrong direction): fine luma noise + aggressive 2018-style edge sharpening (slight visible halos) + punchy single-exposure contrast (blacks slightly crushed, highlights clipped — NOT lifted-black modern flatness) + a subtle warm cast + Snapchat-grade recompression (~crf 26 at 1080). Side-by-side with the real reference, the AI clip should match its grubbiness.
- Perceived "quality drop" and "too premium" are the same defect — AI smoothness. Texture restores both realness and perceived sharpness.

## The edit pass — attention is currency (owner law)

Generation produces takes; the EDIT makes the ad. After clips pass their gates, before delivery:

1. **Dead air is banned.** Measure speech spans (silencedetect); jump-cut every inter-phrase pause over ~0.25s, trim silent lead-ins and tails. Jump cuts are native UGC grammar — the reference winners are full of them.
2. **Pace is edited, not just written.** Speech runs ~1.1x (pitch-preserved). Silent action beats speed-ramp 2–3x so the action reads without costing time; a reaction money-shot ramps gently (~1.5x). A raw generated clip is a TAKE, never the delivered pace.
3. **Text on screen from frame one — as a HEADLINE (owner law).** The ad OPENS with the hook line in a headline treatment: larger stacked platform-native pills, prominent position, on screen from the first frame through the hook beat — a call-in, not a transcript. It is copywriting, written through the headline doctrine (shortest implicating callout). The normal speech pills take over after the hook beat. Alternative hook devices when a headline doesn't fit the concept: comment-response sticker, poll sticker.
   **Platform-native chrome fidelity (owner law):** style the captions as the platform's own text tool renders them, not a generic box. TikTok classic style = PER-LINE background pills hugging each line's width, stacked with merged rounded junctions, bold geometric sans (TikTok Sans; closest system fallback Helvetica Neue Bold), tight padding, black-on-white. Viewers have the native chrome memorized — "a little different" reads AI, same discriminator logic as the pixel-perfect OS-UI rule.
   **End cards pass the art-direction gate** like any type-led static: designed brand field with depth (vignette/grain), display-set headline hierarchy, product INTEGRATED (large, shadowed, cropped at the frame edge), a real CTA element (button pill + domain) — never text floating on a flat color.
4. **The edit gets its own review pass** judged on retention — "would a viewer stay through every second?" — separate from the correctness gates.
   **The delivery QC checklist** (run on the assembled master, every item verified with evidence, not memory):
   - Action-referent continuity: every spoken line that references an action ("smells fine") has its action VISIBLE — an aggressive cut that deletes a referenced beat breaks the ad's logic; ramp beats, don't delete them.
   - Punch-in presence: no static take runs longer than ~2.5s without a zoom alternation (100% ↔ ~108% on phrase boundaries; ~110% for a close-up money beat).
   - Loudness: normalize to −16 LUFS / −1.5 dBTP for social delivery; verify per-segment levels match within ~1 dB before concat.
   - Caption safe zones: pill bottom edges clear the platform's bottom-chrome zone (~80% frame height) and stay off the right rail.
   - Native resolution: deliver 1080x1920 — upscale generated 720p sources (UGC preset) before the edit; normalize SAR after upscaling.
   - Cross-segment continuity: face crops compared side by side across segments (micro-drift adjudicated), audio levels metered, and a HUMAN listen for voice-timbre match — the one check automation cannot clear.


## Gates (same rig as every lane, one addition)

0. **Script gate BEFORE ANY SPEND (owner law):** every spoken line passes the creative-voice-review agent AND the AI-writing-tells review before a single clip is generated. Hunt copywriting DNA wearing casual clothes: tricolon drumbeats, fragment-punch cadence ("that whole shelf? Gone."), spoken taglines ("one scoop, done"), performed-honesty tags ("not gonna lie"), self-answered setup-payoff ("Me neither"), repeated openers across segments. Casual word choice does not clear written rhythm.
1. **Frame gate** before video spend: reality pass + perfection kill + persona fit + product-label OCR at zoom (review-gates.md; design reviewer when agents are available).
2. **Script gate** on the dialogue: hooks, banned words, AI-isms, compliance (scriptwriting.md).
3. **Ship gate** on final clips: ad-creative-reviewer / review-gates.md, then the critic.
4. **Testimonial truth (the lane-specific gate):** a synthetic presenter must never voice a fabricated *personal experience* as if it were a real customer's ("I've been taking this for 6 months and…" from a person who does not exist). Script the lane as creator-style presenter/demo/announcer content — claims about the product, not fake first-person history. Real testimonial language belongs to real customers, quoted under the brand's testimonial rules. The allowed zone for synthetic first-person is the universal present-tense admission ("Me neither"); any product-usage history or personal-results claim ("I take this every morning and…") is over the line.
5. **AI disclosure:** photorealistic AI content carries the full platform AI label. That is the cost of this lane — never strip it, and weigh it in the format pick (an obviously-animated ad wears the lighter label; a realistic UGC ad wears the heavy one and must be strong enough to survive it).
6. **Polish-match the reference:** a photoreal AI clip cleaner than its real-UGC reference is a soft AI tell. The perfection kill applies to finishing, not just plates — the edit adds native compression crush and caption chrome until a side-by-side with the reference matches for grubbiness.
7. **Native captions ship with the ad:** if the reference runs caption pills, the delivery carries native-style captions (edit layer — rendered pills overlaid per segment, synced to the spoken lines). A captionless clip is unfinished, not minimal.
8. **Human-ear voice gate:** automated QA under-detects AI voice — an analyzer has called a voice "natural, perfect lip-sync" that the owner clocked instantly as AI. Route realism lanes through the strongest audio-native model, and a human listens before anything ships.
9. **Per-clip product OCR + zero-typo proof (ship law):** the label gate runs on every rendered clip, not just the plate — rip frames per clip, zoom the pack, verify the label verbatim against the real packshot; reference-driven models can drift a label mid-motion from a verified plate. And every rendered text element added in the edit (caption pills, check rows, end card) is proofread letter by letter before overlay. Any drift or typo = kill and re-roll.

## Failure quick-list

| Symptom | Fix |
|---|---|
| Frame looks AI-slick (perfect skin, staged light) | Re-anchor: pull a grittier real reference, re-extract JSON; add casual-photography imperfections (image-prompting.md reality pass) |
| Product wrong in the video | Product was an ingredient — put it in the start frame and re-run frame-to-video |
| Character talks too fast | Dialogue over budget for the duration — cut words or lengthen the clip, never both unchanged |
| Voice changes between clips | Same-session rule broken (Flow) / cross-batch drift (in-stack) — regenerate in one session/batch or unify with one VO in post |
| Voice sounds robotic | Built-in character/avatar feature was used — rebuild via frame-to-video with own frames |
| Generated person resembles the reference creator | Likeness gate failed at Step 2 — rewrite the JSON's identity block generic, regenerate; never ship a lookalike |
| Spoken dialogue deviates from the script | The prompt enhancer stripped the quoted line — re-roll with the "says exactly these words and nothing else" framing (an enhance-off flag gets overridden); transcript-verify again before delivery |
| A limb or device reads as a fake foreground mass | Camera grammar was imported, not read from the reference — re-read the reference frames, rebuild the plate with the reference's true grammar and a clean foreground |
| Voice reads AI to a human ear | Automated QA passing is not clearance — switch to the strongest audio-native model (the Omni lane) and regenerate |
