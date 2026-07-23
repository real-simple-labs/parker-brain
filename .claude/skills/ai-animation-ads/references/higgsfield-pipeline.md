# Higgsfield Pipeline — Executing the Ad with MCP Tools

How to run the whole production through the Higgsfield MCP (`generate_image` / `generate_video` / `generate_audio` + utilities). If the Higgsfield MCP is not connected, switch to **Kit Mode** (bottom) — the same prompts, delivered paste-ready.

## The job model

- Every `generate_*` call submits an **async job** and returns a job id. Poll `job_status` with `{jobId, sync: true}` until terminal, then read the result URL(s). Use `job_display` to render a result in the UI; `show_generations` / `show_medias` to browse history.
- **A completed job id is reusable as a reference**: pass it directly as `medias: [{value: "<job_id>", role: "…"}]` on later generations — hero images chain into scene frames and start frames without any download/re-upload.
- External assets (product photos, reference ads, style refs): `media_import_url` for HTTPS URLs → `media_id`; `media_upload_widget` for the user's local files (never ask for chat attachments — remote tools can't read them). `medias[].value` takes media_id or job_id, NEVER a raw URL.
- Roles vary by model — check `models_explore(action:'get', model_id:…)` when unsure: video models use `start_image` / `end_image` / `image_references` / `audio_references`; image models use `image` or `image_references`.
- If a call returns a `recovery_tool`, call it immediately — don't explain or ask first.

## Credit discipline (run this before every production)

1. `balance` — know the budget before promising an ad. A full 15-clip premium ad can run hundreds of credits; if the balance can't cover the plan, say so and offer the draft-tier plan or Kit Mode.
2. `get_cost: true` on a representative call of each stage (one image, one draft clip, one final clip) — preflight the whole ad's cost and state it before generating.
3. Ladder: drafts on cheap models/resolutions → finals only for approved shots. Never batch-fire premium video before one clip has validated the style's motion.
4. `params.count` (1–4) batches variations in one call for images — cheaper and faster than serial re-rolls.

## The production run (Mode A: VO-led ad, the default)

```
0. balance → get_cost preflight → confirm plan + budget with user
1. media_import_url / media_upload_widget → product photo, any style refs      → media_ids
2. VOICE   list_voices → user picks (or match archetype from audio.md)
           generate_audio {model:"text2speech_v2", variant:"elevenlabs",       → one job per VO line
                           voice_type, voice_id, prompt:"<line>"}                (same voice every call)
           ElevenLabs MCP alternative: generate_tts per line (see audio.md
           routing) — local files; media_upload_widget them in if assembling
           on Higgsfield, or hand straight to the CapCut kit.
           Listen; note each take's duration → clip lengths. QA pronunciation.
3. HERO    generate_image {model:"nano_banana_2", prompt:<style block +        → hero job_id
           character bible + neutral full-body>, aspect_ratio:"9:16", count:3}   (pick best)
4. FRAMES  per shot: generate_image {model:"nano_banana_2", prompt:<shot       → P1…Pn job_ids
           prompt>, medias:[{value:hero_job_id, role:"image"},
           {value:product_media_id, role:"image"}], aspect_ratio:"9:16"}
           Type B shots need a second (end-frame) image.
5. CLIPS   draft: generate_video {model:"seedance1_5", prompt:<motion>,        → draft clips
           duration:4|8, resolution:"720p", generate_audio:false,
           aspect_ratio:"9:16",   ← ALWAYS pass explicitly: Seedance defaults
           to 16:9 even when the start image is portrait (verified in production)
           medias:[{value:P#_job_id, role:"start_image"} (+ end_image)]}
           final: re-run approved shots on kling3_0 {mode:"pro",
           sound:"off", duration:<≈VO line length>} or veo3_1
6. ASSEMBLE explainer_video {width:720, height:1280,                           → final MP4 job
           items:[{video:<clip1 job>, audio:<vo1 job>}, …in order…],
           subtitles:{font:"patrick"|"caveat"|"marker"|"anton"} — only if wanted}
           Each block's voice take is fitted to its clip window (padded/
           pitch-safe sped); clips are never stretched.
7. FINISH  bytedance_video_upscale {preset:"aigc"} or topaz_video → 4K
           reframe → other aspect ratios · video_deflicker if stop-motion flickers
8. QA      virality_predictor {action:"create", params:{model:"virality_predictor",
           medias:[{role:"video", id:<final job id>}]}} → hook/retention read
```

**Mode B (talking-character ad):** skip step 2 for dialogue lines — the dialogue rides in each video prompt and `kling3_0` `sound:"on"` performs it (most expressive native voices). Keep clip audio; assemble with `items:[{video: job}]` (no `audio` key keeps the clip's own sound). If a recurring character needs one consistent voice: generate takes via step 2, then `sync_so` (Sync Lipsync 3) with `input_video` + `input_audio` roles to re-voice each clip.

**Mode C (song ad):** the song comes from Suno (external) or the ElevenLabs MCP (`generate_music` — exact `duration_seconds`, licensed-clean; Higgsfield itself has no music model and its `generate_audio` is speech-only). Deliver the Suno kit (audio.md) or generate directly; get the audio file in (`media_import_url` for URLs, `media_upload_widget` for local files) → storyboard to its beats → clips silent → assemble with the song as one audio item, or hand off to CapCut for beat-cut precision.

**Statics:** `generate_image` on `nano_banana_pro` (text) / `gpt_image_2` (typography) with product + logo refs, or the managed lane: `ms_image` (requires `style_id` from `show_marketing_studio {type:'image_style'}`; brand kits via `type:'brand_kit'`). 2K+ resolution for finals.

## Assembly notes

- **`explainer_video` uses FIXED 10-second windows per block (verified in production)** — every clip is padded/held to 10s, so a 10-clip ad of 4–8s clips comes back as a draggy 100s cut. Use the server assembler ONLY when all clips are ~10s (the explainer format). **For VO-paced ads with variable clip lengths, assemble locally**: normalize each clip (`scale=720:1280,fps=30`, h264+aac), lay each silent clip's voice take with `atempo` (take longer than clip → speed up pitch-safely) or `adelay`+`apad` (shorter → lead-in + pad), `-t <clip length>` each block, then concat-demux with `-c copy`. A bundled ffmpeg is always available via `pip install imageio-ffmpeg` (`imageio_ffmpeg.get_ffmpeg_exe()`) — no brew needed. Or hand the clips + takes to CapCut with the assembly checklist.
- **Transitions in local assembly:** group clips into segments split at scene changes (hard cuts inside a segment via concat), then chain `xfade=transition=fade` + `acrossfade` between segments with matching durations (0.35–0.6s; offset = running duration − d, probed from the actual files). Place dissolves only where audio is safe — over silence, delays, or line tails, never over a spoken word (check each block's take timing first). Doctrine: dissolve into the turn and into the end card; keep snap cuts where comedy or pace lands.
- Each item = `{video: <clip job id>, audio: <voice job id, optional>}` + output `width`/`height`. Subtitles (optional) are transcribed from the voiceover server-side and burned as timed captions — never put subtitle text in prompts.
- Prefer CapCut/manual edit instead when the ad needs: speed-mapping (2–2.5x Pixar-style, 1.5–2x clay), beat-cut precision on songs, layered music + SFX, or styled captions beyond the built-in fonts. In that case deliver the clips + VO takes + an assembly checklist (order, trim dead frames, transitions 0.5–0.7s, duck music −15 to −20 dB, export 1080×1920 then upscale).
- Caption norm if styling manually: word-by-word highlight, ~42px clean sans, white with black outline, centered around 65% height, 1–4 words at a time; keep the final product/CTA frame clean of captions.

## Other Higgsfield lanes worth knowing

| Lane | Tools | When |
|---|---|---|
| Managed product ads | `marketing_studio_video` + `show_marketing_studio` (products, avatars, hooks, settings, **ad_reference** = recreate a reference ad's scenario) | Fast UGC/product-style ads outside the animation system; "make a video like this ad" |
| Viral templates | `presets_show` + `generate_video {model:"higgsfield_preset", preset_id}` | One-off template effects |
| Flat-2D explainer | `get_workflow_instructions("video-explainer")` | Narrated non-photoreal explainers — Higgsfield's own bundled pipeline (style-key + 10s blocks); good for the flat-2D style lane |
| Motion transfer | `motion_control` | Puppeteer a character image with a reference video's motion |
| Image edits | `outpaint_image`, `remove_background`, `upscale_image` | Frame surgery |

## Kit Mode (no Higgsfield MCP, or user prefers manual)

Deliver the complete production kit as one artifact/markdown doc, in this exact order, fully copy-paste-ready:
1. Research brief + chosen format/style/angle (one page)
2. Script with 5 hook variants + numbered VO line list (for ElevenLabs)
3. Character Bible + hero reference prompt (generate FIRST, then feed as reference)
4. Image prompts P1…Pn — each self-contained (style block + bible + scene + negative), labeled with its VO line and consistency instructions per tool (Nano Banana: attach hero + conversational anchor phrase; Midjourney: `--cref <hero URL> --cw 100 --ar 9:16`; Seedream: hero in the reference slot)
5. Video prompts V1…Vn — labeled with start(/end) frame, target model, duration ≈ VO line, lip-sync or no-lip-sync per format
6. Audio kit — ElevenLabs voice direction + settings (or Suno style + lyrics boxes)
7. Assembly checklist (order, speed-map, captions, music duck, export specs)

The kit must run without this conversation: someone pasting into Higgsfield's UI, Kling, ElevenLabs, and CapCut should never need to ask a question.
