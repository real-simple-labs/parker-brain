# Audio — Voiceover, Songs, Music, SFX

Audio is generated EARLY (right after the script locks), because VO take lengths dictate clip lengths and the song's beat structure dictates the storyboard. Two audio modes:

- **Mode A — VO-led** (narrator-led, character-follow, claymation, paper, crochet, skeleton): generate the voiceover per line first → each line's duration sets its clip's duration → clips are generated silent (or native-audio muted) → one continuous VO layered over the assembled cut.
- **Mode B — character-dialogue-led** (talking-character 3D formats): the dialogue lives in the video prompts and the video model's native audio performs it (Kling 3.0 is the most expressive). Keep good takes; for a recurring character voice across clips, re-voice with a fixed voice + `sync_so` lipsync, or mute and layer ElevenLabs accepting minor off-sync.
- **Mode C — song-led** (sung VO): the song is generated FIRST and becomes the entire audio track; visuals are mapped to its beat structure.

## Tool routing (pick by what's connected)

| Need | First choice | Fallback |
|---|---|---|
| Voiceover takes | **ElevenLabs MCP** — `generate_tts {text, voice_id, model_id:"eleven_v3"}`: full v3 audio-tag control, real ElevenLabs voices; audio saves locally and auto-plays; bills the ElevenLabs account | Higgsfield `generate_audio {model:"text2speech_v2", variant:"elevenlabs"}` — keeps takes as Higgsfield job ids that feed the server-side assembler directly |
| Underscore music | **ElevenLabs MCP** — `generate_music {prompt, duration_seconds:<ad length>, instrumental:true}`: licensed-clean for ads, EXACT duration control | Suno / brand library |
| Full sung-VO ad song | **Suno** (external) — strongest lyric adherence + structure tags | ElevenLabs `generate_music` with vocals (cleanest licensing; less lyric-exact) |
| Hero SFX | **ElevenLabs MCP** — `generate_sound_effect {prompt, duration_seconds}` | Stock libraries |

Routing rule: if final assembly is server-side on Higgsfield (`explainer_video`), Higgsfield TTS keeps the plumbing simplest (job ids in, no re-import). If the edit happens in CapCut, or the read needs v3 audio tags or a specific ElevenLabs voice, use the ElevenLabs MCP and hand the local files to the editor (or `media_upload_widget` them into Higgsfield). ElevenLabs MCP calls spend real credits — same one-take-per-line discipline as everything else, and every generated take auto-plays so the user hears it immediately.

## Voiceover

**On Higgsfield:** `list_voices` → pick voice (returns `voice_id` + `voice_type`) → `generate_audio` with `model: "text2speech_v2", variant: "elevenlabs"` (or default `seed_audio`) — one call per VO line, SAME voice_id/voice_type every call. One line = one take = one clip. Higgsfield cannot generate music or SFX (speech only).
**Direct in ElevenLabs (mid-2026):** `eleven_v3` is the flagship for ad reads and characters — supports **audio tags** inline: `[whispers] [excited] [sighs] [sarcastic] [laughs] [pause] [rushed] [drawn out]` placed before the clause they modify; keep tags sparse and matched to a voice that can plausibly do them. v3 modes: Creative (most expressive) / Natural (balanced — default for ads) / Robust (ignores tags). On v2 models: narration ≈ stability 0.6–0.8, similarity ~0.75, style 0.2–0.4; character/UGC ≈ stability 0.3–0.5, style 0.7–1.0 (high stability + high style = stiff-yet-overacted; don't combine).

**Voice direction by archetype:**
| Role | Direction |
|---|---|
| Warm narrator (Pixar-style B/D) | Storytelling not selling; gentle authority with wonder; slight smile; medium pace with deliberate pauses; speed 1.1–1.15x |
| Intimate clay narrator | Like a friend telling a secret; slightly hushed, crafted; slower — let words breathe; European accents work for premium/skincare; speed 1.0–1.1x |
| Villain / problem character | Cast by archetype, not customer demographic: deep gravelly smug, whiny anxious, droopy deadpan — each character gets its OWN distinct voice |
| Hero product character | Calm, confident, slightly authoritative; contrast with chaotic villains |
| Authority proof voice (multi-narrator) | Grounded, more clinical; often opposite gender from the emotional voice for clean separation |
| Skeleton progression narrator | One calm, dramatic narrator; documentary gravity; lets the escalation do the work |

**Voice Design (creating a custom voice by text):** `Native English. [Gender], [age range]. Studio-quality recording. Persona: [2–5 words]. Emotion: [2–3 adjectives].` + 1–2 sentences on timbre and pacing ("warm, slightly gravelly, conversational pace with confident pauses"). Specific accents ("slight Southern drawl") work; "foreign" doesn't; avoid audio-FX words (reverb, phone).

**Pronunciation QA (mandatory):** listen to every take start-to-finish; brand names are the #1 failure. Fixes, cheapest first: FULLY phonetic respelling in the script — verified in production on a three-character alphanumeric brand name: letter-by-letter spelling ("AY Gee One") still mushes together on ElevenLabs preset voices, while a fully phonetic respelling ("aye jee won") reads clean (generate 2–3 respelling variants as cheap test takes and let the user pick by ear before re-taking real lines). Spell the brand the same way at EVERY occurrence including URLs (respell the brand inside URLs too: "drink dot aye jee won dot com") — mixing respellings inside one take reintroduces the failure. Then: v3 inline IPA `/…/`; v2 SSML alias tags. Also spell out numbers ("twenty percent", "nineteen ninety-eight").

**VO text is plain speech.** No stage directions or parentheticals in the spoken text (tags excepted), no em-dashes; ellipses only as deliberate pause marks. If a line sounds like ad copy when read aloud, rewrite it.

## Songs (Suno for sung-VO song ads; ElevenLabs Music for clean clearance)

For full song ads, Suno remains the specialist: Parker writes the complete kit below; the user (or an operator) pastes it into Suno (v5/v5.5, paid plan — commercial rights require Pro/Premier at generation time). When the brand needs airtight licensing or an exact runtime, generate instead with the ElevenLabs MCP: `generate_music {prompt: <style + lyrical direction>, duration_seconds: 30}` — trained on licensed data, cleared for ads, but less lyric-exact than Suno. Suno's two boxes:

**STYLE box** (~15–30 words, front-load genre+mood; 1,000-char limit but short wins):
`[genre + era], [vocal style — e.g. bright female lead / male rap / warm folk vocalist], [tempo — e.g. 120 BPM upbeat], [mood], [production — clean commercial polish / lo-fi / vintage]`
Never name real artists, songs, or brands as style references (auto-rejected) — describe the sound instead ("melodic rap, emotional vocals, ambient synths, slow trap drums").

**LYRICS box** (the script IS the lyrics) with structure meta-tags:
```
[Intro 2]
[Verse] …
[Chorus] …
[Verse 2 — only if 30s+] …
[Chorus] …
[Bridge — only if 60s] …
[Outro: 2 bars]
```
- Hook in the first 5 seconds; brand/hook line lands in the first chorus.
- 4–8 syllables per line; real verses and choruses with real rhyme — a song, not a "buy buy buy" jingle.
- Sing the ANGLE (customer outcome), and put the unique mechanism in a verse.
- Genre-authentic vocabulary; chorus repetition scaled to length (15s = hook + one chorus pass; 30s = verse-chorus-verse-chorus; 60s = full structure).
- Phonetically respell brand names in the lyrics ("AY gee one") — vocals sing exactly what's written.
- Length control: there's no duration setting — control with lyric volume + `[Outro: 2 bars]` (prevents hard cutoffs better than `[End]`); generate 60–90s, cut the best 30 in the edit. Generate 2–3 takes; pick the take whose rhythm best fits the planned visuals, THEN storyboard to its beats.

**Genre map by target demo:** moms → pop/indie pop/light acoustic (Gen X/40+ moms → country, soft pop, throwback) · Gen Z women → pop, hyperpop, R&B, indie pop · Gen Z men → hip-hop, trap, EDM, indie rock · millennial women → pop, alt-pop, R&B · millennial men → indie rock, hip-hop · Black men → hip-hop, R&B, trap, neo-soul · Black women → R&B, neo-soul, pop · Latino/a → reggaeton, Latin pop, bachata · tech/SaaS → EDM, lo-fi, electro-pop · fitness → hip-hop, EDM, hard rock, trap · outdoor → folk, indie folk, americana · luxury → ambient, modern jazz, cinematic pop · pet owners → folk, indie pop, country · skincare/beauty → pop, R&B, hyperpop · gamers → EDM, synthwave, dubstep · boomers → country, classic rock, soft pop · wellness/spiritual → ambient, indie folk, soft acoustic · trades/blue-collar → country, classic rock, southern rock · foodies → indie pop, jazz-pop, acoustic. Closest fit + one-line reason when the demo is off-map.

**Licensing note (July 2026):** Suno commercial license = Pro/Premier plans; Warner settled/licensed, but Sony litigation and a UMG/Concord suit are open — fine for paid social per common practice, but flag to risk-averse brands. **ElevenLabs Music v2 is the clean-clearance alternative** (trained on licensed data, cleared for ads on paid plans, section-by-section regeneration) — recommend it when the brand needs airtight rights.

## Music under VO (underscore)

Generate directly when the ElevenLabs MCP is connected: `generate_music {prompt: <brief below>, duration_seconds: <ad length + 2s tail>, instrumental: true}` — otherwise Suno or the brand's library. Briefs by style: *Pixar-style:* `whimsical orchestral, playful piano melody, warm strings, uplifting, builds gently from curious to hopeful, cinematic but not overwhelming, [brand modifier]` · *Claymation:* `minimal acoustic, gentle fingerpicked guitar or soft piano, calm and intimate, handcrafted feel, slightly whimsical but grounded, [e.g. Scandinavian minimalism]` · *Skeleton:* `tense curious bed under the build, lift at the payoff`. Mix: duck music −15 to −20 dB under VO; music swells in the hook and payoff, sits low elsewhere.

## SFX & native audio policy

- VO-led formats: generate clips silent where the model allows (`generate_audio: false` / `sound: "off"` — also cheaper) or mute in the edit; ONE continuous VO/song over the assembled cut. Never rely on per-clip generated audio.
- Talking-character formats: keep the native performance when it's good (Kling's is genuinely expressive); it already includes room tone.
- Hero SFX (whooshes, pops, product sounds): 2–3 layers max in the edit — `generate_sound_effect {prompt: "soft papery whoosh with a gentle pop", duration_seconds: 1.5}` on the ElevenLabs MCP (royalty-free on paid plans), or stock libraries. Seedance under-specified audio defaults to unwanted music — suppress explicitly.
- Assembly on Higgsfield: the `explainer_video` assembler marries each clip with its VO take server-side (see higgsfield-pipeline.md); music/SFX layering beyond that happens in the edit (CapCut).
