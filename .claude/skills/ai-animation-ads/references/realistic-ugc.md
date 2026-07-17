# Realistic AI UGC — the start-frame method

The realism counterpart to the animation lanes: photorealistic creator-style talking-head video (UGC, testimonial-style presenter, demo-to-camera). Source: practitioner guide (2026-07) on Gemini Omni UGC workflows, encoded near-verbatim; execution routing adapted to this stack. The animation lanes drop defenses with charm; this lane wins when the format itself IS the message — "a real person like you uses this." It pays for that realism with the heavier platform AI-disclosure label (SKILL.md hard rule on AI disclosure applies in full here).

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
- **Dialogue is unverified until transcribed:** prompt enhancers can silently strip the quoted line from the final model prompt on ANY roll (observed: the same prompt kept the dialogue on one roll and dropped it on the next — the model then improvises on-theme lines that can breach claims gates, e.g. an invented literal-completeness claim). Every clip gets transcript-verified word-for-word before it counts as done. On deviation: re-roll with the line framed as "She says exactly these words and nothing else: …" — observed to force the enhancer to preserve the quote verbatim, where a passed `enhance_prompt: false` flag was silently overridden by the backend. Verify the transcript again after the re-roll.

### Execution routing (three paths)

| Path | What it is | Constraints |
|---|---|---|
| **Higgsfield `veo3`** (in-stack) | Frame-to-video with native audio — takes a `start_image`, speaks the prompted dialogue | The frame-to-video method, executable end-to-end in this stack today; check `models_explore` for current variants/cost |
| **Higgsfield `gemini_omni`** (in-stack) | Gemini Omni Flash — reference-driven (`image_references`/`video_references` roles, i.e. the **ingredients** method), native audio, 4–10s, 720p, 16:9/9:16 | No start_image role: expect product drift; anchor with ONE clean frame-style reference and OCR the product in review |
| **Google Flow** (manual lane) | Full Gemini Omni — frame-to-video + ingredients + text-to-video at flow.google | Not MCP-connected: deliver the Kit (below) |

Model catalogs move monthly — run `models_explore` before assuming this table is current.

### Google Flow Kit Mode

When the user runs Flow themselves (or asks for the setup), deliver a paste-ready kit:

- The generated start frames (one per clip), 9:16.
- Per-clip prompt lines (`make her say "…"`) with the duration each dialogue fits.
- **Session plan:** generate ALL clips of a multi-clip video **in one Flow session, back to back** — voice stays consistent within a session and can change across sessions. A 30s video = three 10s clips, same session, no closing the tab.
- **Do not use Flow's built-in character features** — the voices come out robotic. Frame-to-video with your own frames gets the natural native voices.
- Account economics (2026-07, verify before quoting): free tier for testing; Google AI Ultra $200/mo = 25,000 credits; a 4s video ≈ 7 credits, a 10s video < 15 credits — hundreds of videos/mo, vs $150–300 per video for human UGC creators.

### Voice consistency in-stack

The same-session trick is a Flow behavior. In-stack: generate a multi-clip batch in one run and review voice match across clips; if a clip's voice drifts, either re-roll that clip or strip native audio and lay a single ElevenLabs VO across the cut (audio.md) — one voice per role is already the rule.

## Gates (same rig as every lane, one addition)

1. **Frame gate** before video spend: reality pass + perfection kill + persona fit + product-label OCR at zoom (review-gates.md; design reviewer when agents are available).
2. **Script gate** on the dialogue: hooks, banned words, AI-isms, compliance (scriptwriting.md).
3. **Ship gate** on final clips: ad-creative-reviewer / review-gates.md, then the critic.
4. **Testimonial truth (the lane-specific gate):** a synthetic presenter must never voice a fabricated *personal experience* as if it were a real customer's ("I've been taking this for 6 months and…" from a person who does not exist). Script the lane as creator-style presenter/demo/announcer content — claims about the product, not fake first-person history. Real testimonial language belongs to real customers, quoted under the brand's testimonial rules. The allowed zone for synthetic first-person is the universal present-tense admission ("Me neither"); any product-usage history or personal-results claim ("I take this every morning and…") is over the line.
5. **AI disclosure:** photorealistic AI content carries the full platform AI label. That is the cost of this lane — never strip it, and weigh it in the format pick (an obviously-animated ad wears the lighter label; a realistic UGC ad wears the heavy one and must be strong enough to survive it).
6. **Polish-match the reference:** a photoreal AI clip cleaner than its real-UGC reference is a soft AI tell. The perfection kill applies to finishing, not just plates — the edit adds native compression crush and caption chrome until a side-by-side with the reference matches for grubbiness.

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
