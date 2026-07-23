# Process — AI Video Ad Build

The default process for any ad-shaped video ask: a full ad designed first, then broken into multiple AI generations stitched in the edit. One 8-second clip is never the silent default for an ad — `video-single-shot` is chosen only when the user explicitly wants one clip (a hook test, a single moment, an image animation), and the output names that choice.

The craft source is `parker-system/creative-strategy-context/ai-video-ad-structure.md` — runtime selection, the beat skeleton, the architectures, the natural product handoff, the pacing laws, clip-length derivation, the audio spine, and continuity. Load it and `veo3-video-prompting.md` (per-clip prompt formula) before executing; the architectures and their pacing signatures live there, not here.

One posture note before anything: this format is Disney-style storytelling. Invent characters, worlds, and scenarios freely and specifically — imagination is the engine, not a compliance risk. The wall is the fact layer only: numbers, claims, prices, mechanisms, and anything presented as a real customer or result stay verified or flagged, even out of a cartoon character's mouth.

## Required inputs

- The message: what the ad must make the viewer believe, and the offer.
- A script, if one exists (from the scriptwriting skill or the user). Scripts are a first-class input — beats and line lengths set the shot list. If the ad is dialogue-driven and no script exists, write the lines first, in the brand's voice.
- Brand context — strategy frame, voice, compliance, ICP, visual identity, visual vocabulary if it exists.
- Format: AI Animation, AI UGC, or another named format.
- Platform, audience, and aspect ratio — the delivery pacing read.

## Execution

1. **Pick architecture and runtime from the knowledge doc.** Read the story shape and message weight against the architectures and runtime guidance in `ai-video-ad-structure.md`, and choose — including deliberate hybrids. Name the choice and the reason in one line each. AI Animation is always a multi-clip build or a held-world relay; a single continuous take is only on the table for AI UGC one-take grammar.

2. **Invent the story and map the beats.** Characters, world, conflict — invented specifically and vividly, translated to this brand's message. Walk the skeleton: hook (a character in a charged moment), escalation, the turn, proof, payoff, end card. For long form, chapter the escalation as scheduled reveals — each chapter opens or pays off a question.

3. **Find the natural product handoff.** Not a timestamp — a story event. The problem must be earned first; a character the story trusts does the handing (helper, authority, insider, discovery, or the mascot-as-protagonist inversion); the story keeps moving through it. Test: cover the product beat and ask what the character would reach for next. If it isn't the product, the escalation is thin — fix the story, not the schedule.

4. **Decide the audio spine before any prompt.** Continuous narrator VO laid over the cut, or per-clip character dialogue with delivery direction — plus music (or deliberately none), SFX, register moves. This decision changes what every clip prompt directs.

5. **Build the shot list with the pacing laws.** Fast–slow–fast; no metronome; one proof hold (short form) or a proof chapter (long form); layer-two churn specified per shot (captions per line, expression shifts, inserts, prop entrances); pattern interrupts at act boundaries.

6. **Derive each shot's used length.** From the line it carries (~2.5–3 words/second), the beat's job, AI drift (generate long, use short — money action mid-window, trim both ends), and the delivery read.

7. **Lock continuity and map shots to generations.** Verbatim character and world anchors repeated in every prompt; one world per scene; title cards for time jumps; first/last-frame chaining where a moment must read continuous. One generation per proof hold and per held scene; several sub-2s shots can share one generation via timestamp notation and get separated in the edit.

8. **Write each clip's prompt.** Full five-part formula per clip, anchors verbatim, subject and camera motion separated, audio directed per the spine, descriptive negation only.

9. **Self-check, then deliver the ad.** Run `python3 scripts/voice-lint.py` on every line a viewer will read or hear and fix real flags per `ai-writing-tells.md` (spoken lines also against `spoken-script-voice.md`); fact-trace every number, claim, and price; confirm used lengths vary and anchors match across prompts. Then hand over the ad itself, lean (see Output). When a connected generation tool is available — Higgsfield or similar — offer to run the generations and deliver the actual clips, not just the prompt text.

## Output

Lean. The user wants the ad, not paperwork.

- **THE PLAN** — a short header: architecture and runtime with the one-line reason, audio spine, and the continuity anchor block (the verbatim character/world descriptions the prompts repeat).
- **THE CLIPS** — in stitch order, one block per generation: the beat it carries, its used length (with generation length when they differ, e.g. "use ~3s of the 8s gen"), the line or action, and the complete paste-ready prompt in a code block.
- **EDIT NOTES** — a few lines: trims, caption cadence, title cards, compliance overlay if the category needs one, and the end card (product, offer, URL).

Skip long rationale sections. If something needs explaining — a compliance swap, a conflict with the committed strategy, why single-clip was deliberate — say it in a sentence where it applies.

## What never to do

- Deliver one 8-second clip for an ad ask without naming why single-clip was deliberate.
- Cut on a metronome or hand over uniform used lengths.
- Interrupt the story with the product instead of letting a trusted character hand it over once the problem is earned.
- Run long form without scheduled reveals.
- Write clip prompts before the audio spine is decided.
- Drop character or world anchors between generations, or change world mid-scene.
- Lock the fact layer and the story layer together: story invention is the craft; invented numbers, claims, prices, or fake-real customers are fabrication.
- Bury the ad in paperwork — the deliverable is the clips and the few notes needed to stitch them.
