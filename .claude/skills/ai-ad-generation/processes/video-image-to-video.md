# Process — Image to Video

Bring a static starting image to life with motion, sound, and atmosphere. Picked when the user has an existing image they want animated.

## Required inputs

- The starting image, with its content and composition understood — what is in the frame, what is the focal point, what is the existing lighting and mood.
- The motion the user wants — what moves, where it moves, how fast.
- The audio direction if sound is part of the scene.
- Brand context.

## Execution

1. **Read the image.** Describe what is already there in plain language. The existing composition, lighting, and subject are the constraints — the motion has to be consistent with them. Do not propose motion that contradicts what the image is showing.

2. **Pick achievable motion.** Subject motion that respects natural physics. A bunny's nose twitches; a person walks toward a door; leaves rustle in the breeze. Wild, physics-defying motion produces glitchy output.

3. **Direct camera motion if needed.** If the camera should move (push in, pan, dolly), specify it separately from the subject motion. Static camera with subject motion is often the cleanest choice.

4. **Add atmospheric and sound layers.** Even subtle ambient sound and SFX add reality. Rustling grass, distant traffic, soft footsteps. Where the image suggests an environment, the audio should match it.

5. **Keep the motion brief and singular.** One main motion arc per 8-second clip. Multiple simultaneous motions confuse the model and look unnatural. An image-to-video result is usually one clip inside a larger ai-video-ad-build, not a finished ad by itself.

## Output

- **SHOT BRIEF.** Subject, the motion, camera behavior, audio direction, mood.
- **THE PROMPT.** Text the user pastes into Veo alongside the source image upload.
- **WHY THIS PROMPT WORKS.** Two-to-four sentences on why this motion fits the image, why this audio reinforces the scene.
- **Brand Context Applied.**

## What never to do

- Propose motion that contradicts what the source image is showing.
- Stack multiple simultaneous motions in a single clip.
- Skip audio direction — animated stills feel inert without sound.
- Request camera moves that would require the camera to see what is not in the image.
