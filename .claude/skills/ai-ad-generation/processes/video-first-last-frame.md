# Process — Video First and Last Frame

Direct Veo to interpolate the camera move or transformation between two static images. The user provides both a starting frame and an ending frame; the prompt describes the transition between them.

## Required inputs

- The starting image and a description of what is in it — composition, subject, mood.
- The ending image and a description of what is in it.
- The intended transformation — camera move, environmental change, subject movement, time-of-day shift.
- Audio direction if sound is part of the transition.
- Brand context.

## Execution

1. **Read both frames.** State what is in the starting frame and what is in the ending frame in plain language. The transition has to make sense as a path from one to the other.

2. **Identify the transition type.** Is it a camera arc, a dolly, an environmental morph, a time-of-day change, a subject transformation? Each requires different language.

3. **Describe the path, not just the endpoints.** The model needs to know how to move between the frames — at what speed, with what camera behavior, with what motion arc.

4. **Direct audio across the transition.** Music often carries across; SFX punctuates moments within the move; dialogue (if any) belongs to a specific moment.

5. **Keep the transition single-arc.** One transformation per 8-second clip. Multiple simultaneous transitions produce jumbled output. First/last-frame chaining is also the continuity tool inside ai-video-ad-build when consecutive clips must read as one continuous take.

## Output

- **SHOT BRIEF.** Starting frame, ending frame, transition type, camera behavior, audio direction.
- **THE PROMPT.** Text the user pastes into Veo alongside both image uploads.
- **WHY THIS PROMPT WORKS.** Two-to-four-sentence rationale on the transition design and the audio choreography.
- **Brand Context Applied.**

## What never to do

- Propose transitions that contradict the two source images.
- Stack multiple simultaneous transformations.
- Forget to direct audio across the transition.
- Request camera moves that would require seeing space outside both source frames.
