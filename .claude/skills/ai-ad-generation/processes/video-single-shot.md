# Process — Single-Shot Prompt

One 8-second Veo prompt, one moment, one camera setup. Chosen when a single clip is explicitly the deliverable — a hook test, one moment, one asset to iterate — and the output names that choice. An ad-shaped ask routes to ai-video-ad-build instead; this process also writes the individual clips inside those builds.

## Required inputs

- What the user wants to see and hear in the shot.
- Brand context — voice, compliance, aesthetic, ICP.
- The placement and aspect ratio if known.

## Execution

1. **Open with the cinematic hook.** First phrase of the prompt establishes shot type, mood, and visual register. "A tense, claustrophobic medium shot captures..." anchors everything that follows. A weak opening like "A woman in an elevator..." leaves mood and composition for the model to guess.

2. **Establish subject with detail matching shot distance.** Close-up gets facial details. Wide shot gets posture and silhouette. Match the description to what would actually be captured at that distance.

3. **Choreograph the action with precise verbs.** Replace generic verbs with specific ones. "Limps deliberately," "strides purposefully," "stumbles frantically" each tell the model something distinct. Describe achievable, natural motion.

4. **Separate subject motion and camera motion.** Write each as a distinct clause. "She walks slowly toward the window as the camera tracks alongside her at eye level, maintaining a medium shot."

5. **Build the world.** Environment, lighting, atmospheric conditions, textures. Implied sound counts here too — "the oppressive silence of the empty hallway" shapes the visual mood even before audio is directed.

6. **Lock in the style.** Final phrase unifies the aesthetic. Film references, color palette, lighting style.

7. **Direct audio if it matters.** Dialogue in quotes with delivery direction. SFX as named sounds. Ambient soundscape if the world needs depth. Music if mood requires it.

## Output

- **SHOT BRIEF.** Shot type, camera movement, subject, core action, mood/style, audio elements, aspect ratio, duration.
- **THE PROMPT.** The complete, self-contained text the user pastes into Veo.
- **WHY THIS PROMPT WORKS.** Two-to-four-sentence rationale on the cinematography choice, the action specificity, and the audio direction.
- **Brand Context Applied.** What brand context shaped the prompt, what was avoided, why this prompt fits the brand's current moment.

## What never to do

- Open with the subject before the cinematic hook.
- Use vague action verbs.
- Conflate subject and camera motion.
- Describe details outside what the shot would capture.
- Skip audio direction when sound matters.
- Request physics-defying motion.
