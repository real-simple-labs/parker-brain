# Process — Multi-Shot Sequence

A sequence of distinct shots within a longer composition, using timestamp notation. Picked when the user wants a story, a storyboard-to-prompt translation, or a longer scene that cannot fit in 8 seconds.

## Required inputs

- The story or sequence the user wants — beat by beat, ideally.
- Brand context — voice, compliance, aesthetic, ICP.
- Total length and aspect ratio.
- Any character anchors that must persist across shots — distinguishing features, specific wardrobe, hair, body type.

## Execution

1. **Map the beats.** Identify the distinct shots that make up the sequence. Each shot is a complete unit — its own cinematography, subject, action, context, style, audio. Four-to-eight beats is typical.

2. **Lock the character anchors.** Before writing any shot, write down the specific physical details that identify each recurring character or object. These details must be repeated verbatim in every shot featuring that character — the model carries no memory between timestamps.

3. **Write each shot as a complete prompt.** Treat every timestamp segment like a single-shot prompt with the full five-part formula. Do not write fragments. Each segment should produce a coherent 2-second shot on its own.

4. **Maintain narrative cohesion.** Each shot picks up from the prior one — character location, emotional register, action continuation. The model does not infer this; the prompt language must signal continuity. "Cuts to," "the camera now," "in the next moment" are useful bridges.

5. **Audio across the sequence.** Audio can layer across shots or shift per shot. Music typically threads across; SFX and dialogue belong to specific shots. Direct each audio cue at the timestamp where it lands.

6. **Build to a payoff.** The last shot should resolve the sequence. If the sequence is a narrative arc, the final shot is the punchline, the reveal, the close.

## Output

- **SHOT BRIEF.** Per-shot type/movement/subject/action/mood plus total length and aspect ratio.
- **THE PROMPT.** Full timestamp-notated prompt in code-block format so the user can paste it directly.
- **WHY THIS PROMPT WORKS.** Two-to-four-sentence rationale on the sequence structure, the character anchoring, and the audio choreography.
- **Brand Context Applied.**

## Timestamp format

```
[00:00-00:02] [Complete first shot]
[00:02-00:04] [Complete second shot — character anchors repeated]
[00:04-00:06] [Complete third shot — character anchors repeated]
[00:06-00:08] [Complete fourth shot — character anchors repeated, payoff]
```

## What never to do

- Write fragments inside timestamp segments instead of complete shots.
- Drop character anchors between shots.
- Try to fit more than 4-5 shots into 8 seconds — each shot needs room to breathe.
- Cluster too much simultaneous action in a single timestamp segment.
- Forget to direct music across the sequence if the sequence has a musical arc.
