# AI Ad Generation — Strategy

This document picks which generation process to run based on what the user is asking for. The skill spans video (Veo 3) and static (AI image generation) and recreation of existing statics. All processes share the same discipline: be forensically specific, ground every detail in brand context, never fabricate claims.

## What to load before deciding

- The user's intended use case — paid ad, organic social, product showcase, narrative, recreation of inspo.
- The brand's voice, compliance constraints, visual identity, ICP.
- Any source materials the user provided — images, storyboard frames, reference videos, competitor static screenshots, prior generations to iterate on.
- The intended placement and aspect ratio.

## Which process

### Video processes (Veo 3)

#### video-single-shot
User wants one Veo prompt for a single 8-second clip. Single moment, single camera setup. Most common video ask.

#### video-multi-shot-sequence
User wants a sequence of distinct shots within a longer composition, with character consistency or narrative flow across cuts. Uses timestamp notation.

#### video-image-to-video
User has a static image they want animated into motion.

#### video-first-last-frame
User has two static images and wants Veo to interpolate the camera move or transformation between them.

#### video-dialogue-scene
User wants a scene where spoken dialogue is the primary content — testimonial, founder note, character speaking to camera. Special constraints: one speaker per shot, short lines, delivery direction in every line.

### Static processes (AI image)

#### static-generation
User wants an AI-generated static ad from scratch, picking from the brand-grounded format library. Picks one or more proven format structures and fills the bracketed fields with brand-specific content.

#### static-recreation
User shares a competitor or inspo static and wants to recreate it for their brand. Preserves the original's story while rewriting every word and adapting every brand-specific visual. Different discipline from generation — fidelity to the source structure is the constraint.

## How to choose

Run through these decisions in order. Stop at the first match.

1. **User shared a competitor or inspo static and wants the brand's version?** → static-recreation.
2. **User wants a static and has not shared a reference?** → static-generation.
3. **User has an image as input for video?** → video-image-to-video (one image) or video-first-last-frame (two images).
4. **User describes dialogue as the primary content of the scene?** → video-dialogue-scene.
5. **User asks for a sequence, story, or multiple shots?** → video-multi-shot-sequence.
6. **Default for video asks** → video-single-shot.

A multi-shot sequence is also correct when the user describes a single scene that obviously cannot fit in 8 seconds.

## Shared discipline across all processes

These principles apply universally and govern every process.

### Brand context grounding
Every prompt is built from the brand's actual ICP, voice, compliance, and visual identity. If brand context is not loaded, do not generate output. The discipline that makes AI-generated assets usable rather than generic is the discipline of always grounding in brand context.

### Visual vocabulary grounding
When `sub-context-docs/visual-vocabulary.md` exists, the brand's in-play shots ground the generation prompt — its filmed settings, talent situations, and product moves are the brand's visual language, per the method at `parker-system/creative-strategy-context/visual-vocabulary-method.md`. Build the prompt from that language. A visual the prompt invents outside the vocabulary is out-of-play; flag it so the user knows the prompt asks for something the brand has not shot.

### Specificity
Every detail the prompt omits, the model fills in arbitrarily. The discipline of the skill is forensic specificity — what is in the frame, what is said, what is on the soundtrack, what aesthetic governs the composition, what the brand's visual identity actually looks like.

### Compliance walls
Forbidden terms are forbidden, even if the user asks for them. Push back, explain, offer a compliant alternative that achieves the same strategic intent.

### Data integrity
Every factual claim — stat, percentage, clinical result, case study, quote — must trace to a verified source. If no source exists, the line gets marked `[STAT NEEDED — verify before publishing]` and left unfilled. Never fabricate.

### Customer voice over marketing voice
Where copy is in the prompt — dialogue, headlines, supporting copy — it must sound like the brand's actual customers, not like ad voice. Source from reviews, comments, surveys.

## Video-specific decisions

The source of truth for everything in this section is `parker-system/creative-strategy-context/veo3-video-prompting.md` — the canonical Veo method, with the full camera-language reference, the worked prompt examples by use case, and the iteration process. What follows is the working recap for picking and running a process; when the two ever diverge, the canonical doc wins, and the deeper craft references live there.

### The five-part formula
Every Veo prompt is built from these five components:
- **Cinematography.** Shot type, camera movement, lens, angle. Open with this to anchor mood and composition.
- **Subject.** Who or what is the focus, with detail matched to shot distance.
- **Action.** What the subject is doing, in precise verbs.
- **Context.** Environment and background. What is visible in the frame.
- **Style & ambiance.** Unifying aesthetic — film references, color palette, lighting, mood.

### Subject motion vs camera motion
Always written as separate clauses. Conflating them confuses the model. "She walks slowly toward the window as the camera tracks alongside her at eye level, maintaining a medium shot."

### Audio direction
- **Dialogue.** Quotation marks around exact spoken lines with delivery direction.
- **SFX.** `SFX: [specific named sound]`
- **Ambient.** `Ambient noise: [soundscape description]`
- **Music.** Mood or style direction.

If sound matters to the scene and the prompt omits audio direction, the model improvises and that improvisation will not match intent.

### Multi-shot timestamp notation
```
[00:00-00:02] [Complete first shot]
[00:02-00:04] [Complete second shot — character anchors repeated]
[00:04-00:06] [Complete third shot — character anchors repeated]
[00:06-00:08] [Complete fourth shot — character anchors repeated]
```
The model carries no memory between timestamps. Character details must be repeated verbatim in every shot featuring that character.

### Negative prompts as descriptions
"A desolate landscape without any man-made structures" works. "No buildings" does not. Frame exclusions as positive descriptions, not instructions.

### Aspect ratio
- **16:9** — landscape, YouTube, TV, desktop.
- **9:16** — TikTok, Reels, Shorts, mobile-first.
- **1:1** — feed, in-grid social.
- **4:5** — feed-optimized portrait for Instagram and Facebook.

## Static-specific decisions

### Format library reference
The static-generation process draws from a library of proven format structures, organized by category. The source library is at `parker-system/creative-strategy-context/ai-static-ad-generation.md`, which is the source of truth for the format set — it holds 40 named formats across these categories:

- **Social proof & testimonials.** Customer voices, review data, star ratings, verified badges. Best for brands with strong review data or high-consideration categories.
- **Comparison & competition.** Brand vs competitor or generic category. Best for crowded markets or products with measurable advantages.
- **Product hero & benefits.** Product as the visual focus, with benefit-led copy. Best for visually striking products or new launches.
- **Editorial & press.** Editorial styling and press logos. Best for brands with real press coverage to leverage.
- **UGC & native.** Organic-feeling images that mimic user-generated content. Best for trust-sensitive categories where ad-style imagery underperforms.
- **Copy-led & curiosity.** Bold typography-led layouts driven by headline strength. Best when the message is the asset.
- **Lifestyle & flavor.** Scene-driven imagery showing the product in context. Best for lifestyle brands and category-defining moments.
- **Offer & promotion.** Discount, urgency, and seasonal callouts. Best during promotional periods.

The static-generation process picks one or more formats based on the brand's situation and fills the bracketed fields.

### Recreation discipline
The recreation method is canonical at `parker-system/creative-strategy-context/static-ad-recreation.md`. The recreation process preserves the original's story while rewriting every word for the brand. Hard constraints:
- Every word gets rewritten. Nothing carries over.
- Word count matches the original at every level.
- Copy mechanics are preserved — number stays a number, question stays a question, quote stays a quote.
- Layout, composition, and hierarchy stay the same.
- No new elements added. If the original has no CTA, the recreation has no CTA.

## Common mistakes the strategy must avoid

- Vague action verbs that produce generic motion.
- Mixing subject motion and camera motion in one description.
- Describing details outside the frame for the shot type.
- Forgetting audio direction when sound matters.
- Inconsistent character details across multi-shot sequences.
- Using marketing voice instead of customer voice in dialogue or copy.
- Generating static prompts without brand reference images when they exist.
- Bloating recreated copy past the original's word count.
- Adding new elements to recreations.
- Fabricating any stat, percentage, or claim.

## Final quality audit before output

- For video: all five formula parts present, subject and camera motion separated, audio direction included if relevant, multi-shot character anchors repeated, aspect ratio matches placement.
- For static generation: format chosen matches the brand's situation, bracketed fields filled with brand-specific values, customer voice sourced from real reviews where copy appears, brand reference images instructed.
- For recreation: every word rewritten, word count matches original, copy mechanics preserved, no new elements added, layout intact.
- Across all: brand context applied, compliance respected, no fabricated claims, marketing voice avoided. Where a visual vocabulary doc exists, the prompt grounds in the brand's in-play shots and any out-of-play visual invention is flagged.

## Reasoning log

Past prompts the user has accepted or rejected, with the reasoning behind each pick, accumulate here as the loop runs. Over time this trains Parker on the brand's specific visual taste — what cinematography lands, what dialogue patterns the brand voice supports, what format families convert for this brand's audience.

*(No entries yet — populated by the fine-tuning loop.)*
