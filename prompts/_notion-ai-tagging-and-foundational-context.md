# Notion prompt library context — AI tagging and foundational analysis

Source checked: Notion Prompt Library shared page, 2026-06-02.

This note captures the parts of the Notion prompt library that should shape Parker v2 audits. It is not a full raw export. It is the working interpretation for audit prompts, especially monthly creative, hook, TikTok, competitor, and ad-account reads.

## Prompt library pages found

AI Tagging prompts:

- `Prompt for ad format` — Done.
- `Prompt for awareness level of the ad` — Testing.
- `Prompt for the emotion` — Testing.
- `Prompt for desire` — Testing.
- `Prompt for the occasion` — Testing.
- `Prompt for the persona` — Not started.
- `Prompt for the angle` — blank stub.

Foundational prompts:

- `Video Ad Analysis` — Done.
- `Static Ad Analysis` — Done.
- `Analyze Video From User Upload` — Done.
- `TikTok Video Analysis` — Testing.
- `Proactive Parker - suggesting which follow up questions within each report` — Testing.
- `Prompt to generate slack headline` — Testing.
- `Parker's personal swipe file` — sparse note.
- `Reasoning layer` — blank stub.

The AI-tagging prompts link to a Google Sheet taxonomy named `AI Tagging.xlsx`.

## Core analysis standard

The foundational analysis prompts set a high bar for source reads:

- A reader who has never seen the ad should be able to reconstruct it from the analysis.
- Video reads should move through the ad as the viewer experiences it, so the scene, spoken lines, visible text, transitions, pacing, and camera feel become part of a narrative description rather than a checklist.
- Spoken script must be quoted directly when available. Do not paraphrase a line that can be transcribed.
- On-screen text should be captured with exact wording, capitalization, symbols, and emojis when visible.
- Static reads must be reconstructable as design specs: layout, typography, hierarchy, copy, product placement, people, setting, color, and visual emphasis.
- TikTok or organic reads follow the same reconstruction standard, but should also capture native platform cues, pacing, sound, creator posture, and why the post feels organic rather than ad-like.
- The read should tell the research story and carry the evidence picture. A future LLM or strategist may only see Parker's written analysis, so the analysis needs to show what was reviewed, what source details mattered, how the classification was made, what evidence supports the read, and what uncertainty remains.

Audit implication: do not accept vague labels like "stretch demo," "UGC testimonial," or "creator explains product" as sufficient evidence. A hook, ad, or post should be described as an observable first frame and sequence: who is on screen, what the viewer sees first, what is said, what text appears, how the shot moves, and what emotional or strategic job that opening performs.

## AI-tagging principles

### Ad format

Format tags answer what formats are working. Tag every format with a genuinely strong argument, but wrong tags are worse than missing tags.

The detailed ad-format taxonomy now lives in `global/knowledge/creative-strategy/ad-formats/`. The Parker MCP already carries ad-format tags for the ads where that data is available, so this taxonomy is primarily context for Parker v2 to interpret, compare, audit, and reason from those tags. Read that folder when a prompt needs to classify, interpret, compare, or reason from ad formats. This section remains the short-form tagging principle layer; the folder is the deeper context source.

Separate two kinds of format:

- Visual or setting formats describe how the ad looks or where it was shot.
- Concept or messaging formats describe what the ad is about or how its narrative works.

An ad can legitimately have both. Most ads have one or two format tags, some have three, and more than three should be rare and pressure-tested.

Standardized format labels found in the sheet include:

`Aesthetic`, `AI Animation`, `ASMR`, `Authority Figure`, `Before & After`, `Billboard`, `Headline + Benefits`, `Carousel`, `Challenge`, `Social Interface`, `Comment Response`, `Demo`, `Educational`, `Employee Generated Content`, `Faceless`, `Founder Ads`, `Gifting`, `Green Screen`, `Handwritten`, `Atypical Text`, `High Production`, `How To`, `Humour`, `Infomercial / VSL`, `Meme`, `Motion Videos`, `Native`, `News`, `Notes App`, `Podcast`, `Post-It Note`, `Press`, `Sceptic Test`, `Skit`, `Slideshow`, `Stitch Hooks`, `Street Interview`, `Mashup`, `UGC Single`, `Unboxing`, `Us vs Them`, `Comparison`, `Warehouse`, `B-roll mashup + Voiceover`.

The taxonomy also contains deprecated or combined labels that should not be used as normal audit recommendations: `VSL (COMBINED WITH INFOMERCIAL)`, `Transformation (DO NOT INCLUDE)`, `Timeline (DO NOT INCLUDE)`, `Group (DO NOT INCLUDE)`.

### Awareness level

Awareness level classifies the ad's overall posture toward what the viewer already knows. It is not a sequence of the ad's beats.

Copy is the primary signal. Visuals are secondary. Almost every ad eventually mentions product and CTA; that does not mean it moves through multiple awareness levels.

Standardized labels:

- `Unaware`
- `Problem Aware`
- `Solution Aware`
- `Product Aware`
- `Most Aware`

Audit implication: when evaluating a hook, ask what knowledge state the hook assumes. "Sick of stiff jeans?" is Problem Aware. "Meet the jeans that fit perfectly" is Solution/Product Aware depending on the rest of the posture. "Most guys do not realize their jeans are aging them" can be Unaware if it teaches the viewer a problem they had not considered.

### Emotion

Emotion tagging classifies the whole ad's emotional center of gravity, not every moment in the ad.

Default to one primary emotion. Add a second only when the ad has a deliberate structural split or copy and visuals carry meaningfully different but co-equal emotional payloads. Three is the hard ceiling and should be rare.

Copy and visuals are both emotional signals. If one channel is neutral and the other is emotionally loaded, classify by the loaded channel.

Standardized emotion labels found in the sheet include:

`Hope`, `Confidence`, `Pride`, `Gratitude`, `Love`, `Relief`, `Contentment`, `Amusement`, `Inspiration`, `Empowerment`, `Belonging`, `Awe`, `Tenderness`, `Satisfaction`, `Fear`, `Anxiety`, `Frustration`, `Guilt`, `Shame`, `Sadness`, `Disgust`, `Envy`, `Loneliness`, `Overwhelm`, `Regret`, `Anger`, `Nostalgia`, `Curiosity`, `Surprise`, `Anticipation`, `FOMO (Fear of Missing Out)`, `Skepticism`, `Vulnerability`, `Determination`, `Bittersweet`, `Defiance`, `Calm`, `Trust`, `Desire`, `Urgency`, `Compassion`, `Playfulness`, `Wonder`, `Craving`, `Rebelliousness`, `Sentimentality`.

Audit implication: hook audits should note the likely emotional job of the opener when useful, but should not over-tag every observed cue. The question is the hook's dominant emotional pull.

### Desire

Desire tagging classifies the ad's primary motivational appeal, not isolated cues. It asks what core human motivation the ad is centrally activating.

Standardized labels:

- `Enjoyment of food and beverages`
- `Freedom from fear, pain, and danger`
- `Sexual companionship`
- `Comfortable living conditions`
- `To be superior, winning, keeping up with the Joneses`
- `Care and protection of loved ones`
- `Social approval`
- `None`

For TPJ, likely high-signal desire reads include:

- `Comfortable living conditions` when the hook explicitly promises fit, ease, comfort, friction reduction, stretch, or day-to-day wearability.
- `Social approval` only when the ad explicitly references how others perceive the viewer. Appearance-related apparel ads do not automatically qualify.
- `To be superior, winning, keeping up with the Joneses` when the hook frames TPJ as premium, best-in-class, superior, optimal, or better than alternatives.
- `Freedom from fear, pain, and danger` only when the hook centers physical discomfort or bodily relief as the promise.
- `Care and protection of loved ones` for true partner/family/gift-buyer care frames, not merely a woman appearing in the ad.

### Persona

Persona is who the ad is for, not who appears in the ad.

Select one persona only when the ad clearly speaks to a specific identity, worldview, situation, or life context. Do not force a persona for generic product shots, broad promos, simple motion graphics, or ads without a clear audience identity.

Audit implication: describe the likely target identity behind each hook. A 50+ creator does not automatically mean a 50+ persona unless the hook is written for that viewer. A female narrator can be speaking to a female gift buyer, the male recipient, or both; the ad's language decides.

### Occasion

Occasion classification is split across three independent dimensions:

- Seasonality: `Evergreen` vs `Seasonal`.
- Promotion: financial incentive present vs `No Promotions`.
- Product launch: newness present vs `No Product Launch`.

Seasonality must be core to the ad's message, not incidental background. A beach setting is not seasonal if the ad could run any month. Promo requires a monetary incentive; a CTA alone does not count. Product launch requires explicit or heavily implied newness.

Audit implication: promo-led hooks should generally be treated as account context, not inspiration, unless the first three seconds contain a reusable non-promo mechanic.

## How this should change audits

The audit prompt itself remains the source of truth for what information to look for in a given audit. Before running or rerunning an audit, read the specific prompt in `prompts/audits-*` and use its required inputs, sections, evidence standards, and output shape as the checklist. This Notion-derived context is a supporting layer that sharpens how to read ads and how to interpret AI tags; it does not override the audit prompt.

Monthly audits should look for more than the literal hook line. For every meaningful ad or post, describe the opening as a mini-scene first, then interpret it. The description should let the reader replay the opening in their head and understand how it earns attention. After that, name the mechanics, awareness posture, emotional pressure, and likely persona only where they clarify the read.
- Occasion context: evergreen, seasonal, promo, product launch.
- Whether the hook's useful mechanic is independent of promo or launch context.

The strategic read should still be plain English. These tags are not meant to turn the audit into a tag table. They are a lens for noticing what the ad is doing and what the brand is under- or over-testing.
