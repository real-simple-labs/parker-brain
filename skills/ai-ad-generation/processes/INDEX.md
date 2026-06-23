# AI Ad Generation — Process Index

## Video processes (Veo 3)

- **video-single-shot** — One 8-second clip, single moment, single camera setup. The default for video asks.
- **video-multi-shot-sequence** — Multiple distinct shots within a longer composition, with character consistency across cuts. Uses timestamp notation.
- **video-image-to-video** — Animate a static starting image into motion.
- **video-first-last-frame** — Interpolate camera move or transformation between two static images.
- **video-dialogue-scene** — Scene where spoken dialogue is the primary content. One speaker per shot, short lines, delivery direction.

## Static processes (AI image)

- **static-generation** — Generate an AI static ad from scratch using the format library. Picks one or more proven formats and fills brand-specific values.
- **static-recreation** — Recreate a competitor or inspo static for the brand. Preserves the story, rewrites every word, adapts brand-specific visuals.

---

The existing `single-shot-prompt.md`, `multi-shot-sequence.md`, and `image-to-video.md` files cover the video-single-shot, video-multi-shot-sequence, and video-image-to-video processes respectively. They were named without the `video-` prefix from an earlier version of this skill.
