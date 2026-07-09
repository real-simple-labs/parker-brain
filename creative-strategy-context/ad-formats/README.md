# Ad formats context

Source: `AI Tagging - Ad Format.csv`, added 2026-06-04.

This is Parker's awareness map of every ad format the system classifies. The source CSV was originally a set of tagging instructions for labeling ads, but that job is done: every ad in the Parker database is already tagged. So this context exists for one reason — to give Parker a complete, shared vocabulary for the formats that appear in paid creative.

That vocabulary matters more than it looks. These are the exact format names creative strategists use when they talk about ads. When Parker reads a brand's library and says an account is leaning on `Founder Ads`, `Comment Response`, and `Us vs Them` while running no `Authority Figure` or `Before & After`, it is speaking the language of the craft. Using these formats correctly is how Parker proves it actually understands creative strategy rather than describing ads in vague, generic terms.

This doc is about identification only — what each format is and how to recognize it. It is not about how to execute a format well. Execution lives in the scriptwriting, static-ads, hooks, and concepting surfaces.

## When to pull this context

Pull this context in exactly two situations:

- The user asks what formats exist, what a format means, what formats a brand is running, or which formats are missing from an account.
- The user uploads an ad themselves and asks what format it is.

Outside of those, the format tags Parker needs already live on the ads in the database. Pull the existing tags from the MCP first; only reach for this doc to interpret what a tag means or to name the format of an ad that has none.

## Folder map

- `video/index.md` covers formats that rely primarily on motion, audio, time, sequencing, creator delivery, or a video-native structure.
- `static/index.md` covers formats that are primarily single-frame, designed, screenshot-like, editorial, native-photo, or layout-driven.
- `both/index.md` covers formats that can be meaningfully executed as either video or static.

These folders are retrieval paths, not rigid boxes. An ad can stack formats from more than one folder when the creative genuinely earns it.

## How to identify a format

Start from what is actually on screen. To name a format, reconstruct the creative for a reader who never saw it: the first frame, the person or object on screen, the visible text, the setting, the movement, the spoken line, the edit pattern, the platform interface, and the product's role. The format reveals itself in those details.

Separate format from message. Format is the creative container or execution type. It is not the hook, angle, awareness level, persona, desire, emotion, claim, offer, SKU, or stage of funnel. A doctor talking about gut health might be `Authority Figure`, `Educational`, and `Demo` — but those tags describe the container, not the ad's angle.

Use multiple formats when the ad earns them. Most ads carry one or two meaningful format tags; three when the execution genuinely stacks. Beyond that the read gets noisy.

## Parent-level logic

Video formats usually depend on time — motion, sequencing, creator behavior, spoken delivery, audio, cuts, or a beginning-to-end structure. A video format may contain static-looking frames, but the format logic lives in how the viewer experiences the ad over time.

Static formats usually depend on layout — a single visual composition, screenshot mimicry, headline hierarchy, product arrangement, or a designed artifact. A static may be lightly animated in delivery, but if the idea would still work as one designed frame, it belongs in the static path.

Both formats are execution-flexible. They are defined by the creative device, source of credibility, interaction pattern, or message structure rather than by motion, so they stack readily with other tags.
