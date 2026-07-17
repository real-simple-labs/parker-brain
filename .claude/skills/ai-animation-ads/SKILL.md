---
name: ai-animation-ads
description: "End-to-end system for producing winning AI ANIMATION ads — video and static — from brand research to finished creative. Stages: research brief → format + style pick (talking-object/villain confession, narrator explainer, character-follow, skeleton progression, song ads × Pixar-style 3D, claymation, paper, crochet, flat 2D) → direct-response script → voiceover/song → start frames with locked character consistency → animated clips → assembly, captions, QA. Executes through the Higgsfield MCP when connected (Parker MCP for research/swipes); otherwise delivers a paste-ready production kit. Use whenever the user wants ads MADE with AI: any mention of AI ads, animated/animation ads, Pixar/claymation/stop-motion/paper/crochet/skeleton ads, talking product or object ads, song/jingle/Suno ads, static ads or statics batches, Higgsfield ads, realistic AI UGC or talking-head/testimonial-style AI video, Gemini Omni or Google Flow ads, 'make an ad for X', 'animate this script', or paid-social creative. Trigger even on sub-pieces — image prompts, animation prompts, ad voiceover, ad song, storyboard."
metadata:
  triggers: "make an ai ad · ai animation ad · animated ad · pixar/claymation/paper/crochet/skeleton ad · talking object ad · song/jingle/suno ad · static ad / statics batch · realistic ai ugc / talking-head ad · gemini omni / google flow ad · image or animation prompts for an ad · higgsfield ad · turn this script into an ad"
---

# AI Animation Ads — Director

Produce very strong static and video ads in the AI animation family, end to end. The premise, proven across hundreds of ad accounts and confirmed in Parker's own ad library: animated storytelling processes like the cartoons people grew up on — defenses drop, comprehension rises — while AI generation makes each ad fast and cheap enough to test in batches. The scaffolding below gets every ad to good; **the script and visual direction are what make it great, so spend the iteration budget there.**

## Operating principles

1. **One pipeline, staged, with gates.** Run the stages in order; do not advance past a gate the user hasn't confirmed. Detect where the user is entering (they may arrive with a script, or with finished images) and start at that stage.
2. **Script before visuals — the message dictates the pictures.** Sole exception: song ads, where the generated song's beat structure dictates the storyboard.
3. **Voice first for pacing.** In VO-led formats, generate voiceover takes right after script lock; each take's length sets its clip's length.
4. **Consistency is a system, not luck:** one locked style block + one locked character bible pasted verbatim into every prompt + every generation referencing the HERO image (never the previous output).
5. **Iterate where it's cheap.** Scripts cost nothing; images cost cents; video costs real credits. Get each layer approved before paying for the next. Two identical failures = rewrite the prompt (or swap model), never a third roll.
6. **Execute, don't just hand off.** With Higgsfield connected, run the generations, poll the jobs, assemble, and deliver a finished file. Without it, deliver the Kit (paste-ready prompts). Never make the user figure out prompting.
7. **Explain choices in one line.** When you pick a format, style, or angle, say why — the user learns the system as you go.

## The pipeline

| Stage | Output | Gate | Reference |
|---|---|---|---|
| 0. Research | 1–2 page brief (product physicals, castable characters, customer + pain language, proof, visualisable moments, claims guardrails) + 2–3 live reference ads mined from Parker's library when connected | Brief confirmed | scriptwriting.md · swipe-file.md (Parker mining) · brand vault |
| 1. Creative call | ONE recommended format + style + angle (+ duration, aspect, video/static/both) with menu shown | User picks | formats.md · styles.md |
| 2. Script | 5 hooks + two-column script (VO ⇄ visual) + numbered VO line list — or song lyrics + Suno kit | **Script gate** (scriptwriting.md) + reviewer verdict — kills are cheapest here | scriptwriting.md · swipe-file.md · review-gates.md |
| 3. Audio | VO take per line (ElevenLabs MCP preferred when connected, one voice per role) or generated song; durations noted; pronunciation QA'd | Takes approved | audio.md (tool routing) |
| 4. Storyboard + images | Shot manifest (P# · VO line · Type A/B/C · framing) → hero reference → all start frames (+ end frames for Type B) | Frames approved | image-prompting.md · styles.md |
| 5. Animation | Draft clips (cheap tier) → approved shots re-run on final tier | Motion approved on drafts first | video-prompting.md |
| 6. Assembly + finish | Assembled MP4 (server-side assembler or CapCut kit), captions, upscale, aspect variants | Ship gates below + reviewer SHIP verdict | higgsfield-pipeline.md · review-gates.md |
| S. Statics track | 2–4 statics per video concept + standalone static batches | Compliance gate | static-ads.md |
| U. Realistic-UGC track | Photoreal creator-style UGC: whole-reference segment adaptation → plate per segment → Omni clips with native dialogue → captioned assembly | THE THREE REVIEWS: strategy (mechanic availability + vault-verified SKUs) -> script (voice + AI-tells) -> edit (ugc-edit-reviewer on the cut), plus frame/transcript/voice gates | realistic-ugc.md |

**Stage 1 menu discipline:** show the style menu with visual references where they exist (paper styles: `![Paper styles](https://f.starpop.org/skill-refs/paper-animation-styles-v4.webp)` · skeleton looks: the style-guide image linked in formats.md §4), recommend the best fit in one line, and wait. Static-only requests skip to Stage S (statics still need Stages 0–2's brief, angle, and hook).

## Reference routing

- **formats.md** — the 8 formats, when each wins, script skeletons, in-library proof, skeleton character bibles
- **styles.md** — locked style blocks (3D feature/"Pixar-style", claymation, 5 paper lanes, crochet, flat 2D), per-style production rules, IP-safe phrasing, selection matrix, the 16-look menu + style-menu grid generator
- **material-styles.md** — full production kits for the other 13 material worlds (felt, plush, marionette, animatronic, plastic doll, action figure, wooden doll, cardboard, brick-built, miniature model, boxed diorama, porcelain doll, balloon); load when one is picked from the menu
- **scriptwriting.md** — research brief spec, angle/awareness, hooks, beat craft, banned words, compliance gate, script gate
- **swipe-file.md** — 11 proven scripts/structures + the Parker live-mining playbook (run at Stage 0–1); read the 2–3 entries matching the chosen format before writing
- **audio.md** — ElevenLabs direction + tags, voice archetypes, Suno kits + genre map, licensing, music/SFX policy
- **image-prompting.md** — prompt anatomy, 3-layer consistency system, model table, workflow discipline
- **video-prompting.md** — Type A/B/C director decisions, lip-sync vs VO-only doctrine, movement vocabulary, per-model playbooks (Kling 3.0 / Veo 3.1 / Seedance / Hailuo / Wan), cost ladder
- **realistic-ugc.md** — the photoreal UGC/talking-head lane: start-frame method (real reference → JSON extraction → fresh-context frame), frame-to-video over ingredients, Omni/Flow + veo3 execution routing, same-session voice consistency, likeness + testimonial-truth gates
- **static-ads.md** — 11 static archetypes, one-shot text generation rules, Meta specs/safe zones, compliance, testing cadence
- **higgsfield-pipeline.md** — exact tool-call sequences, job model, credit discipline, assembly, Kit Mode
- **review-gates.md** — the SHIP / FIX / KILL quality rubric (copy + visual + audio, kill questions, output format); run it via the `ad-creative-reviewer` agent when agents are available, inline otherwise

Load only what the current stage needs.

## Hard rules

1. **The skill executes autonomously; judgment lives in the gates, not in approval loops.** Run the full pipeline end to end — strategy, reference selection, copy, generation, review, iteration — and deliver finished gated work, never a menu of options awaiting a yes. Every judgment call a human approval used to cover must instead pass a written internal test: the reference-fit scorecard for reference choices, the compliance gates for copy, review-gates for output quality. Two guardrails remain: (a) budget — check `balance` before a batch; proceed autonomously up to ~10% of the current balance per batch, and pause to flag only beyond that or when credits would run dry; (b) lane changes — switching production lanes (statics ↔ video ↔ audio campaign) or spending on final-tier video before draft motion passed review still gets a heads-up. Report what was decided and why AFTER delivering, with receipts.
2. The style block and character bible are locked once chosen — verbatim in every prompt, never paraphrased.
3. No text baked into video frames (captions live in the edit). Statics have their own text rules.
4. Claymation/paper/crochet characters NEVER lip-sync; talking-character dialogue requires the exact line in the video prompt; never paste dialogue into a no-lip-sync prompt without the mouth-stays-closed constraint.
5. One action per clip; one idea per beat; one speaker per shot.
6. VO lines are plain speech — no em-dashes, no parentheticals; numbers spelled out; brand names phonetically respelled when models mispronounce ("AY-Gee-One").
7. Check `balance` and preflight `get_cost` before any generation run; state the estimated spend; draft tier before final tier. If credits can't cover the plan, say so and offer Kit Mode.
8. No franchise/studio names in prompts or scripts (trademark/trade-dress exposure — Disney/Universal v. Midjourney is live). Use the descriptive blocks; "in the style of [studio/show]" never ships.
9. Compliance gate on every script and static: no medical/cure claims, no personal-attribute callouts, no weight-loss before/afters (including implied), realistic timelines, real urgency only. Brand vault claims doc wins over everything.
10. Meta AI-disclosure is enforced (2026): flag AI-generated creative in Ads Manager for photorealistic content; obviously-animated creative carries the lighter label — one more reason this lane wins. Never strip C2PA metadata.
11. Every video concept ships with 2–4 statics from its hero frames.
12. Report costs and failures honestly — if a generation ran over budget or a clip won't animate after two rewrites, say so and propose the fallback.

## Quality bar & ship gates (Stage 6)

**The review runs twice — Stage 2 (script alone, where a KILL costs nothing) and Stage 6 (the assembled ad) — via the `ad-creative-reviewer` agent, or review-gates.md applied inline where agents don't exist. Only a SHIP verdict ships; FIX loops back to the named stage; statics batches get one pass per batch.** Beyond the reviewer, an ad ships only when: hook lands in ≤3s with verbal + visual + text hook designed together · character/world identical across every shot · style texture survived motion (no realism drift, no vector drift) · VO pronunciation clean, audio continuous, music ducked under VO · captions styled, final CTA frame clean · aspect + safe zones correct for placement · compliance + IP rules pass · (optional but recommended) `virality_predictor` run on the final file for a hook/retention read. Deliver: final file(s) + shot manifest + what to test next (hook variants, second style, statics batch).

## Failure playbook (fast lookups)

| Symptom | Fix |
|---|---|
| Character drifts across frames | Re-attach HERO reference (not last output) + verbatim bible + "identical facial features"; mint a fresh clean reference if drift persists |
| Palette/lighting breaks between scenes | Palette-continuity line in every prompt after P1 ("matching P1, NO [opposite] tones") |
| Style comes back too smooth/realistic/vector | Escalate texture defenses (thumbprints / paper grain / yarn stitches); name the stop-motion cadence in video prompts; swap image model family |
| Mouths move in a no-lip-sync format | Remove quoted dialogue; VO-as-context phrasing + "mouth stays closed, no lip-sync, no speaking on screen"; mute native audio |
| Every character's mouth flaps | Name the single speaker; others "mouths closed, listening" |
| Veo burns subtitles | Colon trick (no quotation marks) + "(no subtitles)" + negative line; crop or re-roll if it persists |
| Seedance adds unwanted music | `generate_audio: false` or "no music, only raw SFX" |
| Villain sounds timid / delivery flat | Direct the energy in the prompt ("assertive, menacing, taunting") and regenerate — delivery is promptable |
| Clip motion is chaotic | Simplify: one movement, drop background animation, shorten dialogue |
| Walking/locomotion jitters (clay/stop-motion) | Switch to in-place motion (shudder, slump, lean) |
| Set morph looks broken | Never prompt literal morphs; cut or dissolve in the edit; paper styles use their transition catalog |
| Text misspelled in a static | Surgical edit ("keep everything identical; correct the headline to spell '…' exactly"), not a re-roll |
| Song take wrong length/rhythm | Regenerate with tightened lyrics + `[Outro: 2 bars]`; generate long, cut the best 30s |
| Two identical failures on anything | The prompt is wrong, not the luck — rewrite it or change model |
