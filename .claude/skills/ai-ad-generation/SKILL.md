---
name: ai-ad-generation
description: Generate AI ad assets — Veo 3 video prompts and AI image static prompts — with brand context, compliance, and forensic direction. The output is prompt text the user pastes into the AI tool, not the final asset.
triggers:
  - veo prompt
  - veo 3 prompt
  - AI video prompt
  - AI video generation
  - text-to-video prompt
  - cinematic prompt for AI
  - multi-shot video sequence
  - storyboard to prompt
  - AI static ad
  - AI image ad
  - generate a static with AI
  - midjourney prompt for an ad
  - recreate this static
  - adapt this competitor static
  - AI ad creative
  - prompt for AI ad
---

# AI Ad Generation

## Goal

Produce the prompt text that goes into an AI generation tool — Veo 3 for video, image models for static — so the output matches the brand's voice, compliance, and visual language. Whatever the model fills in by default is the model's interpretation of the brand, which is almost never what the brand actually is. The skill's job is to remove that gap by being forensically specific about everything in the frame, on the soundtrack, in the copy, and in the visual identity.

This skill produces prompt text. It does not generate the final asset, evaluate the asset's performance, or iterate on a winning asset — those are different skills (ad-account-analysis, iterations).

## What this skill covers

- **Veo 3 video prompts.** Single shots, multi-shot sequences, image-to-video animations, first-and-last-frame transitions, dialogue-driven scenes.
- **AI static ad prompts.** Brand-context-grounded prompts for image models. Covers the standard format families — social proof, comparison, product hero, editorial, UGC, copy-led, lifestyle, offer.
- **Static recreation.** Recreating a competitor or inspo static for the user's brand, preserving the story while rewriting every word and adapting every brand-specific visual.

## What you are working from

The generation methods this skill runs on are canonical, not improvised. Before writing a prompt, load what `parker-system/creative-strategy-context/expertise-routing.md` names for creative generation: `veo3-video-prompting.md` for video, `ai-static-ad-generation.md` for statics, `static-ad-recreation.md` for a recreation, and `visual-vocabulary-method.md` so the frame sources from the brand's own in-play, adjacent, and out-of-play visual language rather than the model's default guess. The Parker tools that pull brand reference and creative data are inventoried in `parker-system/system/parker-tools.md`.

## Background that loads up front

Two pieces of context every AI-generation prompt depends on:

- **The AI improvises whatever is not specified.** Vague prompt input means generic, off-brand output. The discipline of the skill is specificity — describe what the camera sees, what is in the static frame, what the dialogue sounds like, what aesthetic governs the whole composition. Every detail the prompt omits, the model fills in arbitrarily.
- **Veo 3 generates synchronized audio.** Unlike earlier video models, Veo 3 produces dialogue, ambient sound, SFX, and music from text. Leaving audio direction unwritten means leaving 30% of the output to the model. If sound matters, direct it.

## How this skill runs

1. **Identify the prompt type.** Run strategy.md to pick which process. Video or static, and within that, which variant — single-shot, multi-shot, image-driven, dialogue-driven, format-generation, or recreation.

2. **Load brand context — strategy first.** The brand's committed strategy (`strategy/` — the working thesis, the roadmap's calls on what to say and show) frames what's worth generating; read it before writing the prompt, and check the idea bank (`idea-bank/`, including evaluated ideas) for an entry this asset should execute from. Then brand voice, compliance, ICP, visual identity, current creative challenges. The prompt must be grounded in this. A request that cuts against the committed strategy is surfaced with the conflict named, not silently executed; a brain without `strategy/` or an idea bank yet gets one line saying so. AI-generated assets that ignore brand voice produce technically-correct output that is functionally useless because it does not look or sound like the brand. When `sub-context-docs/visual-vocabulary.md` exists, load it too — the brand's in-play filmed settings, talent situations, and product moves are the visual language the generation prompt grounds in, per the method at `parker-system/creative-strategy-context/visual-vocabulary-method.md`.

3. **Apply the format library or the five-part formula.** Video uses the five-part formula — cinematography + subject + action + context + style. Static uses the format library — proven prompt structures with bracketed fields for brand-specific content.

4. **Direct audio explicitly for video when sound matters.** Dialogue in quotes with delivery direction. SFX as named sounds. Ambient soundscape. Music register.

5. **Source claims from verified data.** Every stat, every claim, every customer quote must come from brand context, customer reviews pulled via tools, ad comments, or data the user explicitly provided. If a verified source does not exist, mark the gap with `[STAT NEEDED — verify before publishing]` and leave it.

6. **Run the final checklist.**

7. **You run the two review gates yourself, now, before you present anything — this is a step you execute, not a thing that happens for you.** Read "automatically" as *without being asked*, never as *without you doing it*: nothing else spawns these agents, so if you don't spawn them they never run. They are not optional, not a "second opinion," and never offered to the user as a choice — asking "want me to review this" is itself the failure. Running `scripts/voice-lint.py` yourself is not the gate; the gate is the independent agent, and its returned verdict fills the receipt block below, which you cannot write yourself. Grounding gate first (it changes content), voice gate second (it changes lines). Spawn the `context-grounding-review` agent (defined at `.claude/agents/context-grounding-review.md`) with the user's task, the prompt output, the brain root, and the list of tool pulls made this session. It runs `scripts/grounding-check.py` and independently derives what should have been loaded and pulled — the visual vocabulary behind the frame, the verified sources behind every stat and quote, the brand reference behind the visual identity — then diffs that against the evidence. A `bounced` verdict means re-pull and regenerate the affected parts. This gate runs before the voice gate because its verdict changes content, not lines. And every bounce gets captured through `self-improvement-intake` as a one-line reasoning trace — the task shape plus the loads or pulls that were missed — so the routing layer learns from the catch instead of re-making the same mistake for the gate to re-catch.

8. **Run the voice review gate on the customer-facing copy.** The words a viewer will read or hear — dialogue lines in quotes, headlines, on-screen text, supporting copy, recreated copy — pass the gate; camera and technical direction do not. Spawn the `creative-voice-review` agent (defined at `.claude/agents/creative-voice-review.md`) with those lines extracted, the brand voice profile if one exists, and the deliverable type. The agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass per `ai-writing-tells.md` — and `spoken-script-voice.md` for spoken dialogue — independently, in a context that did not write them. Apply its rewrites into the prompt and re-run until the verdict is `ships`. A flag that conflicts with a sourced customer quote keeps the quote, with the reason carried into the Voice Review block.

9. **Format output per the structure below.**

## Output structure

### For Veo 3 video prompts

**SHOT BRIEF** — Shot type, camera movement, subject, core action, mood/style, audio elements, aspect ratio, duration.
**THE PROMPT** — The complete, self-contained text the user pastes into Veo.
**WHY THIS PROMPT WORKS** — Two-to-four-sentence rationale on the cinematography, the action specificity, and the audio direction.

### For AI static prompts

**FORMAT BRIEF** — Format name (from the category library), what it tests, aspect ratio.
**THE PROMPT** — The complete prompt the user pastes into the image model, with brand-specific values filled into all bracketed fields.
**WHY THIS FORMAT FITS** — Two-to-four-sentence rationale on why this format matches the brand, the ICP, the current moment.

### For static recreation

**THE STORY THIS AD IS TELLING** — Full paragraph explaining the original's narrative — what it wants the viewer to believe, how the visuals and copy work together to build conviction, why it works.
**RECREATION BRIEF** — for each section that applies — headline, supporting copy, design — give the original and then the brand's version, written as prose, not a table: name the section, quote the original, then the rewrite, in plain sentences. Skip the sections that do not apply.
**COMPLIANCE FLAGS** — Anything in the recreation that requires a disclaimer, a forbidden term, or stat verification.

### Brand Context Applied

Append to every output:
- **What I used:** which parts of brand context shaped the prompt.
- **What I avoided:** compliance walls, forbidden terms, off-brand language that shaped the language. If the user request would have violated compliance, state what was flagged and what was offered instead.
- **Why this fits:** two-to-four sentences connecting the output to the brand's current creative challenges, what is working, what they want to test, or an upcoming calendar moment.

### Grounding Review

The grounding gate's receipt, required on every prompt: the `context-grounding-review` verdict, one or two plain sentences on what it checked (visual vocabulary evidenced, stats and quotes traced, cited sources resolved), and — if it bounced — what was re-pulled and regenerated before re-shipping. A prompt missing this block did not pass the gate.

### Voice Review

The gate's receipt, required whenever the prompt carries customer-facing copy — dialogue, headlines, on-screen text: the `creative-voice-review` verdict, the lint density before and after, one or two plain sentences on what was flagged and fixed, and any flag kept with its reason. A prompt whose copy skipped this block did not pass the gate. Prompts with no customer-facing copy at all state that in one line instead.

## Hard rules

### For video prompts

- **Describe what the camera sees and hears.** Not what happened before, not what is off-screen, not what the character is thinking.
- **Match description detail to shot type.** Close-ups get facial details. Wide shots get posture and silhouette.
- **Use precise action verbs.** Weak verbs produce generic motion.
- **Separate subject motion and camera motion.** Always.
- **Stay grounded in natural physics.**
- **Use descriptive negation, not instructive.** "A desolate landscape without any man-made structures" works. "No buildings" does not.
- **For multi-shot prompts, re-establish character details in every shot.** The model carries no memory between timestamps.

### For static prompts

- **Use the brand's actual visual identity, not generic category styling.** If brand reference images are available, instruct the model to use them as reference and match colors, typography, and brand tone precisely.
- **Source the frame from the brand's visual vocabulary.** When `sub-context-docs/visual-vocabulary.md` exists, the brand's in-play filmed settings, talent situations, and product moves ground the generation prompt — that is the brand's visual language. Any visual invention outside the vocabulary is out-of-play; flag it so the user knows the prompt is asking for something the brand has not shot.
- **Match aspect ratio to placement.** 1:1, 4:5, 9:16, 16:9 each serve different placements.
- **Source customer voice from real reviews.** Every quote, every testimonial, every claim must come from a verified source. If no verified quote exists for the format, do not invent one — leave the gap or pick a different format.

### For recreation

- **Rewrite every word for the user's brand.** Nothing carries over verbatim from the original.
- **Match the original's word count at every level.** If the original headline is 4 words, the recreation is 4 words. Bloat kills recreations.
- **Preserve copy mechanics.** If the original uses a number, the recreation uses a number. If it asks a question, the recreation asks a question. If it uses a quote, the recreation uses a quote.
- **Do not add elements that were not there.** If the original has no CTA button, do not add one.
- **Do not redesign the layout.** The structural skeleton stays. Copy and brand-specific visuals change.

### Compliance and data integrity (all process types)

- **Compliance is a wall, not a guideline.** Forbidden terms are forbidden, even if the user asks. Push back, explain, offer a compliant alternative with the same strategic intent.
- **No fabricated stats, percentages, or claims.** Every factual element traces to brand context, reviews, ad comments, or user-provided data. If no verified source exists, mark `[STAT NEEDED — verify before publishing]` and leave the gap.
- **Match brand voice.** The brand's actual tone governs how the dialogue sounds, how the headlines read, how the copy is structured. If the brand would never say something a certain way, neither does the prompt.
- **No prompt ships bounced.** The independent `context-grounding-review` agent verifies the prompt was built from the brand's visual vocabulary, verified data, and traced customer language — an invented quote or an unresolved cited source is an automatic bounce. Its verdict appears in the Grounding Review block.
- **Check facts, not flavor.** The grounding gate verifies facts — numbers, sizes, specs, prices, claims must be real and trace. It does not hunt the exact source of every customer-voice line; a review-, comment-, or thread-sounding line that reads authentic and fits the brand register is fine unpulled, labeled illustrative in one line so no made-up quote runs as a real testimonial. Bounce for a wrong fact, never for an untraceable voice line.
- **You spawn the gates yourself before you present — never offered, never delegated.** The grounding gate runs on every prompt; the voice gate runs on every prompt that carries customer-facing copy, and a visual-only prompt with no dialogue, headline, or on-screen text says so in one line rather than skipping silently. You run them as your own step, before the prompt reaches the user; nothing runs them for you, so a prompt presented without the gate it needs is unfinished, not merely unreviewed. Never ask "want me to review this," never call it a "second opinion," never present and hold the review for later. Running the linter yourself is not the gate — the gate is the independent agent, whose returned verdict fills the receipt blocks you cannot write yourself.
- **No customer-facing copy ships without a clean `creative-voice-review` pass.** The independent agent runs the mechanical lint (`scripts/voice-lint.py`) and the judgment pass against `ai-writing-tells.md` on every line a viewer will read or hear; its verdict and the before/after lint density appear in the Voice Review block. Self-review does not substitute — the reviewer must not be the writer.
