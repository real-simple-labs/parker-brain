---
summary: "The design psychology of static ads — statics have hooks too. How the eye scans a static in milliseconds and the default Z path it takes when nothing directs it, the visual-hierarchy call (what's seen first, second, third), the formatting devices that stop the scroll down to single-word emphasis and where the line breaks, why a static has to be sufficient as well as short, message-image congruency, product money-shots, where social proof goes, and the layouts that lose the eye."
doc: static-ad-design
status: drafted
source: internal creative-strategy doc; extended 2026-08-07 from an internal team statics training
last_updated: 2026-08-07
---

# Static ad design

The rule to start from: **statics have hooks too.** A static ad has an opener just like a video does — it's just spatial instead of sequential. Nobody reads an ad top to bottom. People scan in milliseconds and decide in that scan whether to stop. So a static isn't "laid out," it's *directed* — you decide what the eye sees first, second, and third, and you build the design to enforce that order.

This is the static-specific application of the visual principles in `visuals.md` — the half-second read, hierarchy, pattern interruption, and cognitive ease, worked out for a single designed frame. Read that doc for the why; this one is how it lands on a static. The prompt templates that execute these choices live in `ai-static-ad-generation.md`.

## Visual hierarchy is the whole game

Hierarchy — not copy quality — decides whether the message is even seen. Two moves carry most of it:

- **Size first.** The most important element — the hook — should be the largest thing on the ad, so it's the first thing the eye lands on. One real example ran "FAKING IT WITH MY HUSBAND" as the biggest text on the frame; that line *was* the scroll-stop. Everything supporting it steps down in size from there, so the scan has an obvious order instead of a wall of equal weights.
- **Placement follows the eye.** Put the hook where the eye naturally goes first, and arrange the supporting elements in the order you want them read. You're laying a path, not filling a canvas.

Know where the eye goes when you *don't* direct it. On an English-language feed the untreated default is a Z — top-left, across to top-right, down and back to bottom-left, out to bottom-right. That's the path you get for free, and it's the path you're overriding every time you reach for a device in the next section. So either put the hook on the Z and let the default carry it, or make something loud enough to break the default. What loses is the ad that does neither: a headline sitting mid-frame at the same weight as everything else, hoping to be found. `iterations.md` carries the same read from the iteration side, where a layout restructure alone can move a static without a word of copy changing.

If every element is the same size and weight, nothing leads, and the viewer bounces before the message resolves.

The stack that works most often, largest to smallest: **hook, supporting statement, product, social proof.** The hook takes the scroll-stop, the supporting statement resolves what the hook opened, the product shows what's being sold, and the proof closes. That same "FAKING IT WITH MY HUSBAND" ad runs the whole ladder — the hook enormous, a stepped-down line beneath it naming perimenopause as the cause and the supplement as the fix, the bottle small in the corner, and the star rating and review count smaller still. It is a default, not a law: an offer ad puts the deal at the top, and a product whose payoff is visual puts the money shot first. But when there's no reason to depart from it, that order is the one to build.

## Devices that stop the scroll

These earn the extra half-second. Use them on purpose, not for decoration:

- **Text emphasis** — bold, italic, underline, and colored highlights behind a key phrase pull the eye to the line that matters. Emphasis works at the level of the phrase, but it's sharper at the level of the *word*: pick the one word the headline turns on and hit that, rather than lighting up half the line, which just moves the wall of equal weights up a level. Where the color can carry meaning, let it — a nerve-pain supplement static put its headline's single hardest word, "KILLER," in red, so the color did double duty as emphasis and as connotation.
- **Where the line breaks** is a design decision, not typesetting left over from the copy. The same words set over two lines instead of three read materially faster, because each break is a stop the eye has to pay for. Set the break where the sense breaks — that nerve-pain static went from three lines to two and got easier to take in without losing a word.
- **Lowercase** reads as more organic and less "ad-like," which helps a static blend into the feed.
- **Warped or distorted text** is a small but real pattern-break — the slight wrongness buys a beat of extra attention as the brain resolves it.
- **Arrows** point the eye straight at the thing you want seen.
- **Color contrast** makes the important element pop off everything around it.
- **Font variation** creates visual interest and separates hierarchy levels.
- **White space** keeps the frame from clutter, so the hook has room to land — and it steers, it doesn't only tidy. Emptiness around an element reads as importance, so clearing space is a way of pointing without drawing an arrow. Sizing, contrast, and white space are the three levers that actually move the eye; everything else on this list is a way of working one of them. (White space is also the counterweight to all the devices above — using every trick at once just recreates the wall of noise.)

## Everything it needs, and nothing it doesn't

The concision rule everywhere else in the craft — cut the filler, keep it under ten words, if you can say it shorter say it shorter — is only half the instruction, and on a static the missing half bites harder than anywhere else. A video can withhold something in the first second and pay it off in the fourth. A static has no second beat. Whatever the frame doesn't carry, the viewer never gets.

So the frame has to be *sufficient*: someone who has never heard of this brand should come away knowing what it is, who it's for, and why it should matter to them. Trim to that line and then stop. Cut past it and the ad stops being short and starts being empty — a headline reading "Improvement I can see" has been cut so far that it has no subject left, and the reader has to reconstruct what improved, for whom, from what. They won't; they'll scroll.

Read a draft both ways. Is there a word doing no work? Cut it. Is there a question the frame raises and never answers? That's the thing to add back, even at the cost of a longer line.

## Congruency: the image has to match the promise

The imagery must deliver on what the headline says. If the headline is about *stretch*, show someone stretching the product. If it's about *comfort*, show someone who looks comfortable. If it's about *style*, show someone who looks stylish. A gap between what you say and what you show costs you the half-second read — the viewer's brain stalls reconciling the mismatch, and stalls lose.

The common failure: reusing one image under several different headlines aimed at different audiences. When the picture doesn't move with the message, most of those variants are incongruent by definition, and they underperform the ones where message and image were built together.

## Show the product, and show the payoff

- Use clear, high-quality product shots. Show the product **in use** when it's relevant.
- Reach for the **money shot** — the image that communicates the benefit instantly, with no reading required. A clean before/after skin result is a money shot; the picture *is* the argument.

## Social proof, placed to be scanned

- Put review counts where they're easy to catch — "3,600+ reviews" prominently, not buried.
- Position proof so it's scannable in the same pass as the hook, and keep it from cluttering the layout. It should add credibility, not compete with the message.

## How to test statics

The instinct to change one variable at a time works against congruency here. Because message and image have to match, the stronger approach is **congruent variations** — change the message *and* the imagery together so each variant is internally consistent and aimed at a specific audience segment. You're not isolating a single element; you're testing whole, coherent expressions against each other.

## What to avoid

- **Over-complication** — too many elements competing, so nothing leads.
- **Generic layouts** — designs that look like every other ad in the feed and give the eye no reason to stop.
- **Poor hierarchy** — everything the same size and importance.
- **Mismatched imagery** — visuals that don't support the main message.
- **The decorative split screen** — a frame divided evenly with a photo on one side and a copy block on the other. The eye gets two entry points of equal weight and commits to neither, and at 9:16 both halves are shrunk to where neither reads. The distinction that matters is whether the split *is* the message: in a before-and-after or an us-versus-them, the two panels are the argument, the comparison is the reason to look, and the format earns its place. When the split is only a container for an image and some words, it's costing hierarchy and buying nothing.
- **The stacked composite** — a headline block, then a testimonial block, then a feature row, then a product shot, each self-contained and none subordinate. It reads as two or three ads sharing one frame, and the viewer has to pick which ad they're looking at before they can read any of it. One ad, one argument, one entry point.

The whole philosophy in one line: be intentional with every choice. Know what you want the viewer to see first, second, and third — then design it so they do.

## Related

- `visuals.md` — the cross-cutting visual principles this applies to statics (the half-second read, hierarchy, pattern interruption, cognitive ease).
- `ai-static-ad-generation.md` — the prompt-template library that executes these design choices in AI image tools.
- `hooks.md` and `hook-psychology.md` — the hook is a hook whether it's the first frame of a video or the biggest text on a static.
- `ad-formats/static/index.md` — the taxonomy of static ad formats.

This is everything I know about static ad design.
