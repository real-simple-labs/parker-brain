---
summary: "How to prompt AI video generation (Veo 3)."
---

# Veo 3 Video Generation Context Document

**RULE:** Anytime you reference this document, at the end of the message, you must put "This is based on everything I have learned about AI video generation prompting"

## Brand Context Rule (Applies Before Any Output From This Document)

Before generating ANY output using this document, you MUST first pull and review the full brand context.

How to use it:

- ICPs, customer language, purchase dynamics, and competitive landscape shape every creative decision. These are your raw materials. When you write hooks, scripts, angles, or recommendations, they should be built from this — not generic category assumptions.
- Compliance and legal constraints are hardcoded walls, not guidelines. Every word you generate must pass through the brand's compliance framework. Forbidden terms are forbidden — even if the user asks you to use them. If a user requests copy using a forbidden term or making a claim that violates the brand's compliance rails, you MUST push back. Do not comply. Do not "use it just this once." Do not assume the user knows better than the compliance framework. Instead, flag the issue, explain why you can't use that language, and immediately offer a compliant alternative that achieves the same strategic intent. This is the one area where you do not defer to the user.
- The team's current creative challenges, what's working, and what they want to test give you strategic awareness. You're not blindly following their test wishlist — you're a strategist who knows what they've already tried, where they're stuck, and what opportunities they might be missing. Use this to inform your recommendations, not dictate them.
- The marketing calendar is context you carry passively. If a user's request is relevant to an upcoming moment (holiday, launch, seasonal push), bring it up naturally. Don't force it. But don't forget it either.
- Brand voice governs how copy sounds. Match it. If the brand would never say something a certain way, neither do you.

Do not generate output from this document without brand context loaded.

## Output Proof (Required — End Of Every Response Using This Document)

End every response with this exact structure:

**Brand Context Applied:**

- **What I used:** [Which parts of the brand context shaped this output — ICP, customer language, competitive positioning, creative challenges, marketing calendar, etc.]
- **What I avoided:** [Compliance constraints, forbidden terms, or brand voice boundaries that shaped your language. If the user requested something that violated compliance, state what was flagged and what you offered instead.]
- **Why this fits:** [2-4 sentences connecting your output to the brand's current situation — their creative challenges, what's working/not working, what they want to test, or an upcoming calendar moment. Connect your output to this.]

---

## When To Use This Document

**TRIGGER ALERT:** Pull and use this document immediately when the user asks for any of the following:

- Veo 3 prompts or prompt ideas
- AI video generation prompts
- Text-to-video prompts
- How to prompt video AI models
- Video ad prompts for AI generation
- Cinematic prompts for AI
- Scene descriptions for video generation
- Multi-shot video sequences
- Video prompts with dialogue or audio direction
- Character consistency across video shots
- Camera movement descriptions for AI
- "Write me a Veo prompt for..."
- "How do I describe this scene for AI video..."
- Storyboard-to-prompt translation
- Any request involving AI-generated video content

---

## What Is Veo 3 And Why Does Prompting Matter?

Veo 3 is Google's state-of-the-art video generation model that transforms text prompts into high-definition video with native audio. Unlike earlier models, Veo 3 can generate synchronized dialogue, ambient sounds, sound effects, and background music directly from your text instructions. As of now, Veo can only generate up to 8 second clips. It is also hard to keep consistency every time.

This changes everything about how you write prompts. You're not just describing visuals anymore — you're directing an entire audiovisual experience.

**Why prompting matters:** The quality gap between a mediocre prompt and a well-crafted prompt is enormous. A vague prompt produces generic, unusable footage. A precise prompt produces footage that looks like it came from a professional shoot.

Think of yourself as a director giving instructions to a cinematographer who has never seen your vision. They don't know what's in your head. They can only work with exactly what you tell them. Every detail you omit is a detail they'll improvise — and their improvisation probably won't match what you wanted.

---

## The Core Principle: Describe What The Camera Sees And Hears

The fundamental skill in Veo prompting is describing only what exists within the frame during that specific shot. Not what happened before. Not what will happen after. Not what's happening off-screen. Just what the camera captures in this moment.

This means:
- If it's a close-up, don't describe the character's shoes
- If it's a wide shot, don't describe the texture of their skin
- If the camera is static, don't describe movement that would require the camera to follow
- If there's no dialogue, don't describe what the character is thinking

The prompt is a hyper-specific film script that assumes your AI cinematographer knows nothing implicitly. You must paint the complete picture with words — visual, auditory, and atmospheric.

---

## The Five-Part Prompt Formula

Use this structure as your foundation for every Veo prompt:

**[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]**

Each element serves a specific purpose:

**1. Cinematography** — How the camera captures the scene. This is your most powerful tool for conveying tone and emotion. It includes:
- Shot type (wide shot, medium shot, close-up, extreme close-up)
- Camera movement (static, tracking, dolly, crane, pan, tilt, handheld)
- Lens characteristics (shallow depth of field, wide-angle, macro)
- Angle (eye-level, low angle, high angle, Dutch angle)

**2. Subject** — Who or what the camera focuses on. The main character, object, or focal point. Be specific with physical details that matter for this shot. If it's a close-up of hands, describe the hands. If it's a wide shot of a person, describe their silhouette and posture, not their eye color.

**3. Action** — What the subject is doing. Precise verbs matter enormously. "Walking" is generic. "Limping deliberately," "striding purposefully," "stumbling frantically" — these tell the AI exactly what motion to generate. Describe achievable, natural movements, not physics-defying stunts.

**4. Context** — The environment and background. Where is this happening? What objects, colors, and textures define the space? Describe what's visible within the frame, not the entire world the scene exists in.

**5. Style & Ambiance** — The overall aesthetic and mood. This includes lighting (harsh fluorescent, golden hour, candlelight), color palette (cool blues, warm oranges, desaturated), atmospheric conditions (fog, rain, dust motes), and emotional tone (melancholic, tense, joyful).

---

## How To Use The Formula

### Step 1: Start with the Cinematic Hook

Open your prompt by establishing the mood, visual style, and shot type. This anchors everything that follows.

- **Weak opening:** "A woman is in an elevator..."
- **Strong opening:** "A tense, claustrophobic medium shot captures..."

The strong opening immediately tells the AI what emotional quality to aim for and how to frame the scene. The weak opening leaves the AI guessing about mood and composition.

Think of it like the first sentence of a novel — it sets expectations for everything that follows. A gritty, handheld close-up creates different expectations than an ethereal, wide-angle crane shot.

### Step 2: Establish Who and What

After your cinematic hook, identify your subject with specific, evocative details. Use adjectives that paint a picture, but only include details visible at this shot's distance.

- **For a close-up:** "...a woman in her late 30s, exhaustion etched in the lines around her eyes, mascara slightly smudged..."
- **For a wide shot:** "...a lone figure in a red coat, hunched against the wind, moving slowly across the empty parking lot..."

Notice how the close-up describes facial details while the wide shot describes posture and clothing silhouette. Match your description to what the camera would actually capture.

### Step 3: Choreograph the Action

Describe what your subject is doing with precision. This is where weak verbs kill your prompt.

- **Weak:** "She opens a box"
- **Strong:** "She carefully lifts the lid, her fingers trembling slightly, peeling back layers of tissue paper to reveal..."

The strong version gives the AI specific motion cues — the care, the trembling, the peeling motion. The weak version could produce any number of interpretations.

**Critical distinction: Subject motion vs. camera motion**

These must be described separately. Subject motion is what your character does. Camera motion is how the camera behaves. Mixing them up confuses the model.

**Subject motion examples:**
- "She walks slowly toward the window"
- "His hand reaches for the doorknob"
- "The leaves rustle in the breeze"

**Camera motion examples:**
- "The camera tracks smoothly alongside her"
- "A slow dolly pushes in toward his face"
- "The camera remains perfectly still, observing"

When you want both, describe them distinctly: "She walks slowly toward the window (subject motion) as the camera tracks alongside her at eye level, maintaining a medium shot (camera motion)."

### Step 4: Build the World

Context isn't just "where" — it's the sensory environment that makes the scene feel real. Describe:

- **Physical environment:** What objects populate the space? What's the architecture? What textures are visible?
- **Lighting:** How does light enter the scene? What shadows does it create? How does it interact with surfaces?
- **Atmospheric conditions:** Is there fog, rain, dust, steam? How do these interact with the light?
- **Implied sound (for visual cues):** Even if you're not directing audio explicitly, describing implied sounds can inform the visual mood. "The oppressive silence of the empty hallway" creates different visual energy than "the bustling chaos of the crowded market."

### Step 5: Lock in the Style

End with stylistic direction that unifies the whole prompt. This is where you reference specific aesthetics, film styles, or visual treatments.

**Examples:**
- "Shot as if on 1980s color film, slightly grainy, with warm nostalgic tones"
- "Clean, modern aesthetic with high contrast and desaturated colors"
- "Dreamlike quality with soft focus and ethereal lighting"
- "Documentary-style realism, handheld with natural imperfections"

---

## Directing Audio And Dialogue

This is where Veo 3 fundamentally differs from earlier models. You can now direct the complete soundscape.

### Dialogue Direction

Use quotation marks for specific speech. The model will generate synchronized lip movement and voice.

**Format:** A [character description] says, "[exact dialogue]"

**Example:** "A tired detective behind his desk looks up and says in a weary voice, 'Of all the offices in this town, you had to walk into mine.'"

**Key principles for dialogue:**
- Keep lines short and natural — long monologues are harder to generate cleanly
- Describe the emotional quality of delivery ("weary voice," "excited whisper," "stern tone")
- One speaker per shot works best — multi-person conversations should be broken into separate shots

### Sound Effects (SFX)

Describe specific sounds you want to hear. Be direct and clear.

**Format:** SFX: [description of sound]

**Examples:**
- "SFX: thunder cracks in the distance"
- "SFX: the metallic clang of the door slamming shut"
- "SFX: footsteps echo on wet pavement"
- "SFX: a phone buzzes on the table"

### Ambient Sound

Define the background soundscape that creates environmental reality.

**Format:** Ambient noise: [description] or describe within the scene naturally

**Examples:**
- "Ambient noise: the quiet hum of fluorescent lights and distant office chatter"
- "The scene is filled with the sounds of the bustling city — car horns, distant sirens, fragments of conversation"
- "Soft elevator music plays from overhead speakers, mixing with the mechanical hum of the descent"

### Music Direction

You can request specific musical moods or styles.

**Examples:**
- "A swelling, gentle orchestral score begins to play"
- "Soft jazz plays in the background"
- "Tense, minimalist electronic music underscores the scene"

---

## Camera Language Reference

Master these terms to direct your shots precisely:

### Shot Types (Distance from Subject)

- **Extreme Wide Shot (EWS):** Subject is tiny in the frame, environment dominates. Used to establish location or show isolation.
- **Wide Shot (WS):** Full body visible with significant environment. Establishes spatial relationships.
- **Medium Wide Shot (MWS):** Approximately knees-up. Balances subject and environment.
- **Medium Shot (MS):** Waist-up. The workhorse of dialogue scenes.
- **Medium Close-Up (MCU):** Chest-up. Focuses on facial expressions while maintaining some context.
- **Close-Up (CU):** Face fills most of frame. Captures emotional detail.
- **Extreme Close-Up (ECU):** Single feature (eyes, hands, object detail). Maximum emotional intensity or detail focus.

### Camera Movements

- **Static:** Camera doesn't move. Creates stability, formality, or tension depending on context.
- **Pan:** Camera rotates horizontally on a fixed point. Used to follow action or reveal space.
- **Tilt:** Camera rotates vertically on a fixed point. Used to show height or follow vertical movement.
- **Dolly:** Camera moves toward or away from subject on tracks. Creates smooth approach or retreat.
- **Tracking/Trucking:** Camera moves parallel to subject. Often used to follow walking characters.
- **Crane:** Camera moves vertically through space. Creates sweeping reveals or establishes scale.
- **Handheld:** Camera held by operator, creating natural shake. Adds documentary feel, tension, or intimacy.
- **Steadicam:** Smooth movement through space without tracks. Follows action fluidly.
- **POV (Point of View):** Camera represents character's literal viewpoint.

### Lens and Focus Terms

- **Shallow Depth of Field:** Subject sharp, background blurry. Creates focus and cinematic look.
- **Deep Focus:** Everything sharp from foreground to background. Shows environmental detail.
- **Rack Focus:** Focus shifts from one subject to another within the shot.
- **Wide-Angle Lens:** Exaggerates depth, can distort edges. Creates dynamic, immersive feel.
- **Telephoto/Long Lens:** Compresses depth, flattens space. Creates voyeuristic or isolated feel.

### Compositional Terms

- **Rule of Thirds:** Subject placed off-center for visual interest.
- **Leading Lines:** Environmental lines draw eye toward subject.
- **Framing:** Using environmental elements to create frame-within-frame.
- **Symmetry:** Balanced, centered composition. Creates formality or unease.
- **Dutch Angle:** Camera tilted to create diagonal horizon. Creates disorientation or tension.

---

## Timestamp Prompting For Multi-Shot Sequences

For complex sequences, you can direct multiple shots within a single generation using timestamp notation. This creates a complete scene with distinct shots that maintain visual consistency.

**Format:**
```
[00:00-00:02] [First shot description]
[00:02-00:04] [Second shot description]
[00:04-00:06] [Third shot description]
[00:06-00:08] [Fourth shot description]
```

**Example:**
```
[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal a hidden path.

[00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with awe as she gazes upon ancient, moss-covered ruins in the background. SFX: The rustle of dense leaves, distant exotic bird calls.

[00:04-00:06] Tracking shot following the explorer as she steps into the clearing and runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder and reverence.

[00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small in the center of the vast, forgotten temple complex, half-swallowed by the jungle. SFX: A swelling, gentle orchestral score begins to play.
```

**Key principles for timestamp prompting:**
- Re-establish key visual details in each segment (the model doesn't carry memory between timestamps)
- Maintain character consistency by repeating distinguishing features
- Each timestamp should describe a complete shot, not a fragment
- Use this for scenes that benefit from multiple angles, not just longer single shots

---

## Negative Prompts: Describing What To Exclude

Sometimes you need to tell the model what NOT to include. The key is framing exclusions as descriptions, not instructions.

**Wrong approach (instructive language):**
- "No buildings"
- "Don't show walls"
- "Avoid showing other people"

**Correct approach (descriptive language):**
- "A desolate landscape without any man-made structures"
- "An empty room with bare floors and no furniture"
- "The character stands alone, isolated from any crowd"

You can also use a dedicated negative prompt field (if available in your interface) with simple terms: "urban background, man-made structures, dark atmosphere"

This tells the model to deprioritize these elements without using instructive language.

---

## Aspect Ratio Considerations

- **16:9 (Widescreen):** The standard for most video content. Use for landscapes, establishing shots, scenes where horizontal space matters, and most professional video applications.
- **9:16 (Portrait):** Vertical format for short-form social content (TikTok, Reels, Shorts). Use for tall subjects, vertical motion, and content designed for mobile viewing.

Match your aspect ratio to your final use case. A cinematic ad destined for TV or YouTube should be 16:9. A TikTok-first piece should be 9:16.

---

## Common Mistakes And How To Avoid Them

### Mistake 1: Vague Action Verbs

- **Problem:** Generic verbs like "walks," "looks," "moves" give the AI no specific motion to generate.
- **Solution:** Use precise, evocative verbs. "Limps," "strides," "shuffles," "stumbles," "saunters," "creeps." Each creates distinctly different motion.

### Mistake 2: Mixing Subject and Camera Motion

- **Problem:** "The woman walks forward and zooms in on her face" conflates what the subject does with what the camera does.
- **Solution:** Describe them separately. "The woman walks forward toward the window. The camera slowly dollies in, ending on a close-up of her face."

### Mistake 3: Describing Details Outside the Frame

- **Problem:** For a close-up, describing the character's full outfit and environment wastes words on invisible elements.
- **Solution:** Match description detail to shot type. Close-ups get facial details. Wide shots get posture and silhouette. Only describe what the camera captures.

### Mistake 4: Overly Complex Simultaneous Actions

- **Problem:** "She picks up the phone while looking out the window while her other hand drums on the desk while she sighs" is too much for a single generation.
- **Solution:** Prioritize one or two actions that can be executed clearly. Save additional actions for separate shots.

### Mistake 5: Physics-Defying Movement

- **Problem:** Requesting movements that don't obey natural physics produces glitchy, unrealistic results.
- **Solution:** Describe natural, achievable motion. Humans don't spin 360 degrees while jumping and catching an object. Keep movements grounded in reality.

### Mistake 6: Forgetting Audio Direction

- **Problem:** Leaving audio to chance when Veo 3 can generate precise soundscapes.
- **Solution:** Include explicit audio direction — dialogue, SFX, ambient sound, or music — in prompts where sound matters to the scene's impact.

### Mistake 7: Inconsistent Character Details Across Shots

- **Problem:** Describing a character differently in each prompt of a multi-shot sequence produces inconsistent appearance.
- **Solution:** Establish key character anchors (specific clothing, distinguishing features, body type) and repeat them verbatim in every prompt featuring that character.

---

## Iteration Process

Getting the perfect output rarely happens on the first generation. Here's how to iterate effectively:

**First pass:** Generate with your initial prompt. Evaluate what worked and what didn't.

**Identify specific issues:**
- Did the framing match what you wanted?
- Did the motion look natural?
- Did the audio sync properly?
- Were there any visual artifacts?
- Did background characters behave as expected?

**Revise with precision:** Don't rewrite the entire prompt. Add or modify specific elements to address specific issues.

**Common fixes:**
- "Doors opened too fast" → Add "slowly" or "deliberately" to the action
- "Background people stared at the main character" → Add "surrounding people remain absorbed in their own activities, ignoring the main characters"
- "Audio too quiet" → Be more explicit about sound: "The elevator dings loudly" or "Ambient music plays clearly from overhead speakers"
- "Wrong emotional tone" → Add explicit emotional direction: "Her expression is exhausted but not sad"

**Know when to stop:** AI video generation follows the 90/10 rule — you'll get 90% of the way there quickly, and the last 10% takes disproportionate effort. Sometimes it's faster to do final polish in editing software than to iterate endlessly.

---

## Advanced Workflows

### Workflow 1: First and Last Frame Transitions

Create specific camera movements or transformations by providing start and end images.

**Process:**
1. Generate (or provide) your starting frame image
2. Generate (or provide) your ending frame image
3. Use the First and Last Frame feature with a prompt describing the transition
4. Include audio direction for the transition

**Example prompt:** "The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to seamlessly end on the POV shot from behind her on stage. The singer sings 'when you look me in the eyes, I can see a million stars.'"

### Workflow 2: Ingredients to Video (Character Consistency)

Maintain consistent characters across multiple shots by providing reference images.

**Process:**
1. Generate or provide reference images for characters, settings, and key objects
2. Use the Ingredients to Video feature with relevant reference images
3. Write prompts that specify which reference elements to use
4. Include audio direction for dialogue scenes

**Example prompt:** "Using the provided images for the detective, the woman, and the office setting, create a medium shot of the detective behind his desk. He looks up at the woman and says in a weary voice, 'Of all the offices in this town, you had to walk into mine.'"

### Workflow 3: Image-to-Video Animation

Bring static images to life with motion and sound.

**Process:**
1. Start with a strong source image (generated or provided)
2. Write a prompt describing the motion you want
3. Include audio that matches the scene
4. Keep the motion achievable and natural

**Example:** Starting with an image of a bunny with a chocolate bar, prompt: "The bunny's nose twitches, then it hops away clutching the chocolate bar. SFX: Soft rustling of grass and a distant bird chirp."

---

## Prompt Examples By Use Case

### Commercial/Ad Prompt

```
Medium shot, a tired corporate worker in a rumpled white shirt, rubbing his temples in exhaustion, seated in front of a bulky 1980s computer in a cluttered office late at night. The harsh fluorescent overhead lights flicker occasionally, mixing with the green glow of the monochrome monitor that illuminates his face. Papers are stacked precariously on every surface. He sighs heavily and says, "There has to be a better way." Retro aesthetic, shot as if on 1980s color film, slightly grainy with warm nostalgic tones. SFX: The hum of the old computer, distant office sounds, the buzz of fluorescent lights.
```

### Cinematic Narrative Prompt

```
Close-up with shallow depth of field, a woman in her late 30s opens a weathered cardboard box on the floor of a quiet hallway. Natural morning light filters softly through a nearby window. She carefully peels back layers of tissue paper to reveal a pair of pristine white baby shoes. Her expression is unreadable — not sad, just present and still. She holds the shoes in her lap, her thumb tracing the tiny sole. The shot is unhurried and intimate. Ambient noise: soft house sounds, the creak of floorboards, a distant bird outside the window. No music.
```

### Product Showcase Prompt

```
Extreme close-up with macro lens detail, a single drop of golden serum falls in slow motion onto smooth skin. The camera captures the moment of impact as the droplet spreads and absorbs, the skin taking on a subtle luminous quality. Clean, clinical white background with soft, diffused lighting that highlights the product's texture. The mood is luxurious and scientific. SFX: A soft, satisfying 'drop' sound as the serum lands.
```

### Social Media (Vertical) Prompt

```
9:16 aspect ratio. POV shot from inside a vintage convertible driving down a palm-lined street in golden hour light. The camera is positioned in the passenger seat, capturing the driver's hands on the leather steering wheel, the dashboard, and the sun-drenched road ahead. Palm trees pass overhead, casting moving shadows. The driver taps the steering wheel to the beat. Warm, saturated colors with lens flare from the setting sun. Ambient: Wind rushing past, an upbeat retro song playing on the car radio.
```

---

## Final Checklist Before Generating

Before you submit any Veo prompt, verify:

- [ ] Shot type is explicitly stated (wide, medium, close-up, etc.)
- [ ] Camera movement is described separately from subject movement
- [ ] Subject details match what would be visible at this shot distance
- [ ] Actions use precise, specific verbs
- [ ] Environment includes sensory details (lighting, textures, atmosphere)
- [ ] Style/mood is clearly established
- [ ] Audio direction is included if sound matters to the scene
- [ ] Dialogue uses quotation marks with delivery direction
- [ ] No physics-defying or overly complex simultaneous actions
- [ ] For multi-shot sequences, character details are consistent across prompts

---

## Output Format For Veo Prompts

When writing Veo prompts for a user, present them in this format:

---

### SHOT BRIEF

- **Shot Type:** [Wide/Medium/Close-up/etc.]
- **Camera Movement:** [Static/Tracking/Dolly/etc.]
- **Subject:** [Who or what is the focus]
- **Core Action:** [What happens in this shot]
- **Mood/Style:** [Emotional and aesthetic qualities]
- **Audio Elements:** [Dialogue/SFX/Ambient/Music]
- **Aspect Ratio:** [16:9 or 9:16]
- **Duration:** [If multi-shot, specify timestamps]

---

### THE PROMPT

[Write the complete prompt here — this is what gets entered into Veo]

---

### WHY THIS PROMPT WORKS

[Explain the key decisions: why this shot type, why these specific details, why this audio direction. This helps the user understand the craft so they can iterate intelligently.]
