# Process — Video Dialogue Scene

A Veo prompt where spoken dialogue is the primary content — testimonial, founder note, character speaking to camera, conversational reaction. The dialogue is the asset; the visuals support it. A dialogue ad longer than one clip runs through ai-video-ad-build, with this process governing each spoken clip.

## Required inputs

- The dialogue itself — exact spoken lines.
- The speaker — who they are, what they look like, their tone and delivery.
- Brand context — voice, compliance, and any persona work that defines how a brand spokesperson would sound.
- The visual setting and shot type.
- Whether this is a single shot or part of a multi-shot sequence.

## Constraints specific to dialogue

These constraints make dialogue scenes work or fail.

- **One speaker per shot.** Veo handles single-speaker dialogue well. Multi-person conversations should be broken into separate shots and stitched in post or composed as a multi-shot sequence.
- **Short lines.** Long monologues are harder to generate cleanly. Break long content into multiple shorter shots.
- **Delivery direction in every line.** The exact words matter, but so does the emotional quality of the delivery. "Weary voice," "excited whisper," "stern tone," "warm and conspiratorial" each tell the model how the voice should land.
- **Compliance applies to dialogue.** Forbidden terms remain forbidden even when a character says them. Push back, offer compliant alternatives.

## Execution

1. **Lock the dialogue first.** Every spoken line, exactly. Read it out loud — would the brand's actual customer or persona say this? If not, rewrite. Source phrasing from voice-of-customer where applicable.

2. **Direct the delivery.** Per line, name the emotional quality. The same words delivered three different ways produce three different ads.

3. **Build the visual around the dialogue.** The shot type, the framing, the action, the setting — all support the dialogue. A close-up emphasizes intimacy. A medium shot supports natural conversational delivery. A wide shot makes the speaker feel small or part of an environment.

4. **Match the visual energy to the line.** A high-energy reaction needs faster pacing and tighter framing. A reflective testimonial needs space, breath, and a slower setting.

5. **Add ambient sound.** Even when the dialogue carries the audio, an ambient layer makes the scene real. Ambient noise of the environment, soft music underneath if the brand voice supports it.

6. **For multi-shot dialogue sequences.** Use timestamp notation with one speaker per shot. Each shot is its own short line with its own delivery direction.

## Output

- **SHOT BRIEF.** Speaker, shot type, setting, the spoken line, delivery direction, audio elements.
- **THE PROMPT.** Text the user pastes into Veo. Dialogue in quotation marks. Delivery direction inline.
- **WHY THIS PROMPT WORKS.** Two-to-four-sentence rationale on the dialogue, the delivery direction, and the visual support.
- **Brand Context Applied.**

## What never to do

- Put more than one speaker in a single shot.
- Write long monologues for a single shot.
- Omit delivery direction.
- Use marketing voice in dialogue when the brand has customer voice to draw from.
- Use forbidden terms even in character dialogue.
