---
summary: "How to generate AI static image ads — prompt construction for static creative."
---

# AI Image Ad Prompt Generation Context Document

**RULE:** Anytime you reference this document, at the end of the message, you must put "this is everything I know about AI static ad generation"

**Template reference link** (share this when users are asking about prompting — they need the reference images for it to make sense): https://www.notion.so/realsimplelabs/Nano-Banana-2-Examples-e6a120b5a800826cbbe6810487e4b534

**YOU MUST USE THAT EXACT LINK. NO SHORTENING IT OR ANYTHING OR IT WILL NOT WORK!!!**

**RULE:** YOU NEED TO KEEP THESE PROMPTS VERY CLOSE TO WHAT IS PROVIDED, ONLY ADJUSTING THE VARIABLES FOR THIS SPECIFIC BRAND. THE PROMPT STRUCTURE SHOULD REMAIN THE SAME.

---

## When To Use This Document

**TRIGGER ALERT:** Pull and use this document immediately when the user asks for any of the following:

- Static ad ideas, concepts, or prompts
- Image ad prompts for Nano Banana 2, Hixfield, or any AI image generation tool
- "Generate me some static ads"
- "Give me image ad prompts"
- "I need static ad creative"
- Requests for specific static formats like comparison ads, testimonial ads, social proof ads, UGC-style statics, editorial ads, or product hero ads
- "What static ad formats should I test?"
- "Give me prompts I can plug into Nano Banana" or "prompts for Hixfield"
- Any request for image-based ad creative that is NOT a video script

**If the user is asking for video ad scripts,** use the relevant scriptwriting context doc instead. This document is exclusively for static/image ad prompt generation.

---

## What This Document Does

This document contains 40 proven static ad format templates. Each template is a structured prompt designed to be plugged directly into an AI image generation tool and produce a finished ad-ready image.

Your job is NOT to hand someone all 40 templates. Your job is to:

1. Understand the brand's situation, objectives, and audience
2. Select the formats that strategically make sense for this brand
3. Fill in the templates with brand-specific context using everything you know about the brand — brand DNA, customer review language, winning ad copy, ICP insights, and product details
4. Output finished prompts that are immediately ready to paste into an image generation tool with zero edits needed

The copy in these prompts is the most important variable you control. The template handles the design and layout. You handle the messaging. That messaging should come from real customer language and proven angles — not generic marketing copy.

---

## How To Use This Document

Follow these steps every time you generate image ad prompts. The steps are sequential. Do not skip any of them.

### Step 1: Pull Brand Context

Before selecting a single template, you need to understand the brand. Pull from:

- Brand context and personas via get_brand_persona
- Context docs via getContextDocs
- Customer reviews via search_customer_reviews_sql and search_customer_reviews_semantic
- Winning ad data via facebookAdsAnalysisReportsSqlSearchTool and search_facebook_ads_semantic

You need to know: What does this brand sell? Who buys it? What language do customers use? What angles have scaled in their ad account? What objections come up? What competitors get mentioned? What emotional drivers appear in reviews?

This is your source material. Every headline, subhead, testimonial quote, and benefit line in the finished prompts should come from this data — not from your general knowledge.

### Step 2: Identify the Objective

What is the user trying to accomplish? This determines which format categories to pull from.

- **Trust-building creative:** Pull from the Social Proof & Testimonial category. These formats use customer quotes, review cards, star ratings, and verified badges to build credibility. Best for brands with strong review data, products in skeptical categories, or retargeting audiences.
- **Competitive differentiation:** Pull from the Comparison category. These formats put the brand side-by-side against competitors or the generic category. Best for brands in crowded markets where customers mention competitors in reviews, or products with clear measurable advantages.
- **Showcase the product and its benefits:** Pull from the Product Hero & Benefits category. These formats put the product front and center with stats, benefit callouts, or feature annotations. Best for brands launching new products, running broad prospecting, or when the product itself is visually compelling.
- **Authority and press credibility:** Pull from the Editorial & Press category. These formats mimic news articles, editorial content, or publication features. Best for brands with press coverage, strong founder stories, or products that benefit from third-party validation.
- **Organic-feeling native creative:** Pull from the UGC & Native category. These formats are designed to look like real social posts, stories, notes app screenshots, or user-generated content. Best for brands whose audience scrolls past anything that looks like an ad, or for testing native-feeling creative against polished formats.
- **Copy-led scroll-stoppers:** Pull from the Copy-Led & Curiosity category. These formats lead with provocative headlines, bait-and-switch quotes, or manifesto-style copy where the writing IS the ad. Best for brands with a strong voice, controversial positioning, or when the emotional angle is stronger than the visual product.
- **Lifestyle and aspiration creative:** Pull from the Lifestyle & Flavor category. These formats put the product in context — action shots, flavor visualization, data-driven lifestyle scenes. Best for food/beverage, fitness, fashion, or any product where the use experience matters more than specs.
- **Promotional or offer creative:** Pull from the Offer & Promotion template. Best for sales events, launches, or when there's a specific offer to push.

### Step 3: Select Specific Formats

Based on the objective, select 3-6 specific formats from the library below. For each one, you should be able to clearly articulate WHY this format makes sense for this brand. If you can't justify it, don't recommend it.

- **Consider what's already working.** Look at the brand's top-spending ads. What formats are they already using? Are there categories they haven't tested at all? Untested format categories are your biggest opportunity.
- **Consider the ICP.** Different audiences respond to different formats. A younger audience might engage more with UGC-native formats. An older audience might respond better to editorial or social proof formats. A price-sensitive audience might need comparison formats. Let the ICP guide your selection.
- **Consider the product.** Visually compelling products shine in product hero and lifestyle formats. Products that need explanation benefit from feature callout and benefit list formats. Products in crowded categories need comparison and differentiation formats.

### Step 4: Fill In the Templates

This is where your value lives. Anyone can copy a template. Your job is to fill it in with brand-specific context that makes the ad actually convert.

- **For every headline and subhead field:** Pull language from customer reviews and winning ad copy. Search for the exact phrases customers use to describe the product, the problem, and the transformation. Use those phrases — not polished marketing language. If the customer says "I finally stopped waking up at 3am" that's better copy than "Achieve restful sleep tonight."
- **For every testimonial or quote field:** Use REAL customer reviews. Pull actual quotes from the review data. Use the customer's name and make it feel authentic. Do not fabricate quotes.
- **For every benefit or stat field:** Use real product data. Do not make up statistics, review counts, or customer numbers. If you don't have the exact number, leave a placeholder and flag it for the user to fill in.
- **For every competitor reference:** Use language from reviews where customers mention competitors or alternatives they've tried. Real comparison language from customers is more credible than marketing claims.
- **For product descriptions in prompts:** Be extremely precise about the product's physical appearance — packaging colors, label text, shape, size, distinguishing visual features. AI image generation models produce better results when the product description is detailed and specific.

### Step 5: Enhance Copy with Customer Data

After filling in the template, look at the copy one more time. For each piece of text that will appear in the image, ask:

- Did this come from real customer language or data? If not, can I find a better version in the reviews?
- Would a customer actually say this, or does it sound like marketing?
- Is this the strongest possible version of this headline? Check the top-spending ads for language patterns that have scaled.

This is where Parker adds value that no template doc alone can provide. You have access to customer reviews, ad performance data, and brand context. Use all of it to make the copy as strong as possible before the prompt goes into the image generation tool.

### Step 6: Output the Finished Prompts

Present each prompt as a standalone block that can be copied directly into Nano Banana 2, Hixfield, or any AI image generation tool. No additional context needed. No edits required. The user should be able to take each prompt, paste it in, attach their product images, and generate.

---

## Output Format

When presenting finished image ad prompts, use this EXACT format for each one:

---

### [FORMAT NAME] — [WHAT IT TESTS]

**Why This Format for [Brand]:** [2-3 sentences connecting this format to the brand's specific situation, audience, or data. Reference specific customer language, ad performance patterns, or strategic gaps.]

**PROMPT:**

[The complete, filled-in prompt. Ready to paste. All brand-specific details filled in. All copy finalized. All placeholders resolved except any that require information you genuinely don't have, which should be flagged clearly.]

---

Repeat for each format selected.

**CRITICAL RULES FOR OUTPUT:**

- Every prompt must be completely self-contained and immediately usable
- Do NOT leave template brackets like [YOUR HEADLINE] in the finished prompt — fill everything in
- Do NOT fabricate statistics, review counts, or data points you don't have. Use real numbers from the brand's data or flag as "[INSERT ACTUAL NUMBER]"
- Do NOT use generic marketing copy when you have access to real customer language
- Always note the aspect ratio at the end of each prompt
- If you're recommending more than 6 formats, explain why — the default should be a focused, strategic selection

---

## Format Library

The templates below are organized by category. Each template is a standardized prompt structure with bracketed fields that you fill in with brand-specific information.

**How to read these templates:** Anything in [BRACKETS] is a field you fill in. Some brackets contain guidance on what to put there. The non-bracketed text is the structural prompt that stays the same regardless of brand.

---

### CATEGORY: SOCIAL PROOF & TESTIMONIALS

These formats use customer voices, review data, star ratings, and verified badges to build trust. Best for brands with strong review data, products in skeptical or high-consideration categories, or retargeting audiences who need one more trust signal.

---

**FORMAT 1: HEADLINE**

Tests text rendering. If this comes back clean, the model handles copy. Good starting point for any brand.

**Template:**

Use the attached images as brand reference. Match the exact product colors, typography style, and brand tone precisely. Create: a static ad with a [BACKGROUND] background. Top third: large bold sans-serif headline reading "[YOUR HEADLINE, under 10 words]". Below in smaller text: "[YOUR SUBHEAD, one sentence]". Bottom half: [YOUR PRODUCT] on the surface with [DETAILS]. Shot at 50mm f/2.8 from slightly above. [BRAND] logo bottom right. Clean, authoritative. 4:5 aspect ratio.

---

**FORMAT 3: TESTIMONIAL**

Real environments plus text overlays. Tests composition depth. Use real customer quotes.

**Template:**

Use the attached images as brand reference. Create: a testimonial ad set in [SETTING like bright bathroom / kitchen] with warm natural light. [YOUR PRODUCT] on [SURFACE], slightly out of focus. Overlaid: large bold white sans-serif "[SHORT HEADLINE]". Below: "[FULL QUOTE 2-3 sentences]. [NAME], [CREDENTIAL]." Five filled [BRAND COLOR] stars. [BRAND] logo bottom right in white. Shot on 35mm f/2.0. 9:16 aspect ratio.

---

**FORMAT 6: SOCIAL PROOF**

Member count plus review card plus press logos. The trust stack.

**Template:**

Use the attached images as brand reference. Create: a social proof ad on [BACKGROUND like warm cream]. Top: "[HEADLINE like Join 1,000,000+ Members]" in bold [BRAND COLOR]. Five filled stars with "Rated [X] out of 5". Center: [YOUR PRODUCT] at 50mm f/4. Below: frosted white card with five-star rating, "[REVIEW TITLE]", "[2-3 SENTENCE REVIEW]", "[ATTRIBUTION]" in italic. Below card: "As Featured In" with five grayscale logos. [BRAND] logo bottom right. 4:5 aspect ratio.

---

**FORMAT 11: PULL-QUOTE REVIEW CARD**

Emotional quote headline over a truncated review card on a color block. The "...Read more" creates an open loop.

**Template:**

Use the attached images as brand reference. Match the exact product colors and brand tone precisely. Create: a review-driven ad with a solid [BRAND COLOR with hex — a soft, muted tone works best] color block background filling the entire image. Top half: large bold italic serif text in white with curly quotation marks reading "[PULL-QUOTE — the most emotional 4-8 word phrase from the review]". Directly below the quote: five large filled gold/yellow star icons in a horizontal row. Bottom left, overlapping the color background: a white rounded-corner review card with subtle shadow, containing: a small gray circular default avatar icon, beside it "[FIRST NAME + LAST INITIAL]" in bold dark sans-serif with a small [FLAG EMOJI matching target market], below the name a blue checkmark icon with "[VERIFIED REVIEWER / VERIFIED BUYER]" in small blue text. Below the reviewer info: the review body text in medium-weight dark sans-serif, 4-6 lines of authentic-sounding customer voice that trails off mid-sentence, ending with "...Read more" in bold [BRAND COLOR] text — the truncation is intentional to create curiosity. Below the review text: "Was this review helpful?" in small gray text with a thumbs-up icon and "[HELPFULNESS COUNT]" beside it. Bottom right, overlapping both the card and the color background: [YOUR PRODUCT — full packaging description] angled slightly toward the viewer, sitting on the color block surface with a subtle shadow beneath. No brand logo needed if the product packaging already shows it — the review card IS the social proof. 1:1 or 4:5 aspect ratio.

---

**FORMAT 15: SOCIAL COMMENT SCREENSHOT + PRODUCT**

Screenshotted comment equals instant credibility. Looks organic. Bold hook headline does the scroll-stopping.

**Template:**

Use the attached images as brand reference. Match the exact product design and colors precisely. Create: a static ad on a clean white background. Top: oversized bold black sans-serif headline reading "[HOOK HEADLINE]" with [EMOJI] at the end. Center: a social media comment card with light gray rounded-rectangle background containing: a small circular profile avatar (top left), bold name "[REVIEWER NAME]", and a multi-sentence review in regular-weight sans-serif: "[FULL REVIEW TEXT, 3-4 sentences, conversational and emotional]". Small gray timestamp "[TIMESTAMP like 2d]" below the comment. Bottom center: [YOUR PRODUCT] photographed at a slight angle on white, soft studio lighting. No brand logo. No stars. The rawness is the point — this should look like someone screenshotted a real comment and dropped the product photo below it. 1:1 aspect ratio.

---

**FORMAT 17: VERIFIED REVIEW CARD**

Mimics real review platform UI. The verified badge and helpfulness count do the trust-building work.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and typography style precisely. Create: a static ad on a solid [BRAND COLOR like periwinkle/lavender blue] background. Top: large bold white serif or semi-bold sans-serif pull-quote reading "[HEADLINE QUOTE]" in quotation marks. Below the quote: five filled gold stars, large. Center-left: a white rounded-rectangle review card with subtle shadow containing: gray circular avatar icon, bold name "[REVIEWER NAME]" with [FLAG EMOJI], blue checkmark and "[VERIFIED BADGE TEXT like Verified Reviewer]" in [BRAND COLOR] text, then 3-4 sentences of review body text in regular weight dark text. At the bottom of the card: a blue "...Read more" link and "[HELPFULNESS like Was this review helpful? thumbs-up 150]". Right side, overlapping the card edge: [YOUR PRODUCT] photographed at a slight angle, soft studio lighting, casting a gentle shadow on the background. No brand logo. The review UI is the trust mechanic. 1:1 aspect ratio.

---

**FORMAT 19: HIGHLIGHTED / ANNOTATED TESTIMONIAL**

The highlighter pen does the work. Long-form review text with key phrases visually emphasized. Directs the eye to the money lines.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and typography style precisely. Create: a static ad on a clean white background. Top left: circular customer headshot photo of [PERSON DESCRIPTION]. To the right of the photo: bold name "[REVIEWER NAME]" with a [VERIFIED ICON like blue checkmark]. Below: a long-form customer quote in large regular-weight black sans-serif type spanning most of the frame: "[FULL QUOTE, 3-5 sentences]". Key phrases within the quote are highlighted with [HIGHLIGHT COLOR like bright lime green / neon yellow] rectangular background fills behind the text: "[HIGHLIGHTED PHRASE 1]", "[HIGHLIGHTED PHRASE 2]". Bottom right: [YOUR PRODUCT] at a slight angle, partially cropped at the bottom edge. To the left of the product: a circular [TRUST BADGE like "100% MONEY BACK / 90 DAYS / 100% GUARANTEE"] seal in [BADGE COLOR]. [BRAND] logo bottom left corner, small. 1:1 aspect ratio.

---

**FORMAT 24: PRODUCT + COMMENT CALLOUT (FAUX SOCIAL PROOF)**

Product hero shot with a realistic Facebook-style comment card below. Should look like an organic screenshot, not designed.

**Template:**

Use the attached images as brand reference. Match the exact product design and packaging precisely. Create: a social proof ad. Top 55%: [YOUR PRODUCT] centered on a clean white background, studio-lit, shot at 85mm f/2.8 with soft shadow. Product cap/lid slightly open or [DETAIL showing use]. A few [LOOSE UNITS like gummies / capsules] spilling casually at the base. Bottom 45%: a realistic Facebook-style comment card. Left: small circular profile photo of [PERSON DESCRIPTION]. Bold name "[FIRST NAME + LAST INITIAL]" above the comment. Comment text in regular weight: "[TESTIMONIAL 2-3 sentences touching on a specific problem and the product being a game-changer]". Below comment: "[TIMEFRAME like 4w]" · Like · Reply in gray. Bottom right of comment: Facebook-style reaction emojis (thumbs up + heart) with "[COUNT]". Should look like an organic screenshot, not designed. 1:1 aspect ratio.

---

### CATEGORY: COMPARISON & COMPETITION

These formats put the brand side-by-side against competitors or the generic category. Best for brands in crowded markets, products with measurable advantages, or when customer reviews frequently mention switching from competitors.

---

**FORMAT 7: US VS THEM**

Side-by-side comparison. Photography quality gap IS the argument.

**Template:**

Use the attached images as brand reference. Create: a side-by-side divided vertically. Left: muted gray-blue background. Right: [PRIMARY BRAND COLOR]. Center top: white circle with "VS". Left header: "[COMPETITOR CATEGORY]" + generic competitor product + list with X marks: "[WEAKNESS 1-5]". Right header: "[YOUR BRAND]" + [YOUR PRODUCT] + list with checkmarks: "[STRENGTH 1-5]". [BRAND] logo bottom right. 4:5 aspect ratio.

---

**FORMAT 25: US VS THEM COLOR SPLIT**

Same comparison mechanic but with stronger visual contrast. Checkmark and X emoji format. Comic-style VS burst.

**Template:**

Use the attached images as brand reference. Match the exact product design and colors precisely. Create: a side-by-side comparison ad divided vertically into two equal halves. Left half: [PRIMARY BRAND COLOR] background. [YOUR PRODUCT] photographed with dynamic energy — [ACTION DETAIL like chocolate dripping / liquid pouring] to convey indulgence. Brand logo in bold white upper-left. Below product: vertical stack of 4 benefits, each with a green circle checkmark emoji: "[STRENGTH 1-4]" in bold white uppercase. Right half: [CONTRAST COLOR like pale cream/beige] background. Generic unbranded competitor product [DESCRIPTION]. Header: "[COMPETITOR CATEGORY]" in dark text. Below: vertical stack of 4 weaknesses, each with a red circle X emoji: "[WEAKNESS 1-4]" in bold dark uppercase. Center divider: a comic-style "VS" burst graphic in [ACCENT COLOR]. 1:1 aspect ratio.

---

**FORMAT 31: COMPARISON GRID / TABLE**

Structured comparison grid. No icons, no colors — the copy contrast does the work. Should feel like a meme-format comparison that would go viral.

**Template:**

Use the attached images as brand reference. Match the exact product packaging precisely. Create: a structured comparison grid ad on white background. Top row divided 50/50: Left: [YOUR PRODUCT] packaging photographed clean on white with [DETAIL]. Right: [COMPETITOR PRODUCT] packaging on white. Below: three horizontal rows spanning full width, each divided 50/50 by a thin black vertical line and separated by thin black horizontal lines. Each row compares one attribute: Row 1: "[YOUR ADVANTAGE]" vs "[COMPETITOR WEAKNESS]". Row 2: "[YOUR ADVANTAGE]" vs "[COMPETITOR WEAKNESS]". Row 3: "[YOUR ADVANTAGE]" vs "[COMPETITOR WEAKNESS]". All text in bold black serif or heavy sans-serif, centered in each cell. No icons, no colors, no checkmarks — the copy contrast does the work. Should feel like a meme-format comparison that would go viral on X or Reddit. 1:1 aspect ratio.

---

### CATEGORY: PRODUCT HERO & BENEFITS

These formats put the product front and center with stats, benefit callouts, or feature annotations. Best for brands launching new products, running broad prospecting, or when the product itself is visually compelling.

---

**FORMAT 4: FEATURES/BENEFITS POINT-OUT**

Educational diagram-style layout. Clean and informational.

**Template:**

Use the attached images as brand reference. Create: an educational diagram-style ad on white background. Top: bold [BRAND COLOR] text "[HEADER like What Makes [PRODUCT] Different]". Below: [YOUR PRODUCT] centered, even studio lighting. Four callout boxes with connecting lines: "[BENEFIT 1-4]". Each has a small [BRAND COLOR] circle. "[WEBSITE]" bottom center. [BRAND] logo bottom right. Scientific diagram redesigned by a luxury agency. 4:5 aspect ratio.

---

**FORMAT 5: BULLET-POINTS**

Split composition. Product left, benefits right.

**Template:**

Use the attached images as brand reference. Create: a benefit-list ad, split composition on [BACKGROUND] background. Left 40%: [YOUR PRODUCT] on [SURFACE], shot at 85mm f/2.8. Right 60%: vertical stack of five lines with filled [BRAND COLOR] circles: "[BENEFIT 1-5]". Clean sans-serif, generous spacing. [BRAND] logo bottom right. 4:5 aspect ratio.

---

**FORMAT 13: STAT SURROUND / CALLOUT RADIAL (PRODUCT HERO)**

Product is the sun. Stats are the planets. Arrows make it scannable in under 2 seconds.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and typography style precisely. Create: a static ad on a white-to-[LIGHT GRADIENT COLOR] gradient background, gradient fading from top to bottom. Top: large bold [TEXT COLOR] sans-serif headline reading "[HEADLINE]". Center: [YOUR PRODUCT] on white background, soft studio lighting. Floating near the product: a small circular badge reading "[PRICE POINT]" in [BADGE COLOR]. Flanking the product on both sides: four stat callouts with curved arrows pointing toward the product. Left side top: "[STAT 1]" in oversized bold text with "[LABEL]" below. Left side bottom: "[STAT 2]" with "[LABEL]". Right side top: "[STAT 3]" with "[LABEL]". Right side bottom: "[STAT 4]" with "[LABEL]" and five filled gold stars beneath. Arrows are simple hand-drawn-style curved lines in [ARROW COLOR]. Bottom foreground: [FLAVOR PROPS] adding appetite appeal. No brand logo. Clean, informational, appetizing. 1:1 aspect ratio.

---

**FORMAT 14: BUNDLE SHOWCASE + BENEFIT BAR**

Sells the system, not the SKU. The open box is the hero. The benefit bar handles the "what's in it for me."

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and typography style precisely. Create: a static ad on a [BACKGROUND like soft pink-to-hot-pink gradient] background. Top: oversized bold white all-caps sans-serif headline reading "[HEADLINE]". Below headline: a horizontal [ACCENT COLOR] banner bar divided into [NUMBER] equal segments separated by thin vertical lines, each containing a two-word benefit label in white text: "[BENEFIT 1]", "[BENEFIT 2]", "[BENEFIT 3]", "[BENEFIT 4]", "[BENEFIT 5]". Center-to-bottom: an open [PACKAGING] photographed at a slight overhead angle showing [NUMBER] [PRODUCTS] nestled inside, each a different [COLOR-CODED VARIANT]. In the lower foreground: a [LIFESTYLE PROP] entering the frame from bottom. [BRAND] logo bottom left corner. Bright studio lighting, saturated color, energetic and empowering. 1:1 aspect ratio.

---

**FORMAT 18: STAT SURROUND / CALLOUT RADIAL (LIFESTYLE FLATLAY)**

Same stat-radial format as Format 13 but lifestyle flatlay background and hand-held product sell the experience, not just the specs.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and typography style precisely. Create: a static ad on a white background with a lifestyle flatlay arrangement. Top: bold [ACCENT COLOR] filled banner bar spanning full width, white all-caps sans-serif reading "[HEADLINE]". Center: a [PERSON DETAIL like woman's hand] holding [YOUR PRODUCT] in mid-frame. Scattered around the edges: [FLATLAY PROPS] arranged organically to fill corners and edges, slightly out of focus. Four stat callouts with curved [ACCENT COLOR] arrows pointing toward the held product: "[STAT 1] / [LABEL]", "[STAT 2] / [LABEL]", "[STAT 3] / [LABEL]", "[STAT 4] / [LABEL]" with five small gold stars. Stats in bold black, labels in all-caps regular weight. Bright, flat studio lighting. Energetic, appetizing, information-dense but scannable. 1:1 aspect ratio.

---

**FORMAT 27: BENEFIT CHECKLIST SHOWCASE**

Split product display plus info panel. Sells the product and its proof simultaneously.

**Template:**

Use the attached images as brand reference. Match the exact product design and brand colors precisely. Create: an information-dense benefit ad, split composition. Left 45%: overhead product shot — [PRODUCT DISPLAY DESCRIPTION]. Shot on 50mm f/4, clean white surface. Right 55%: white background. Top: [STAR RATING] with "[REVIEW COUNT] REVIEWS" in [BRAND COLOR]. Brand logo. Below: [BRAND COLOR] headline: "[HEADLINE]". Then 3 checkmark benefit rows, each with a filled [BRAND COLOR] circle checkmark + bold text: "[BENEFIT 1-3]". Bottom right: large rounded [ACCENT COLOR] CTA button reading "[CTA]". 1:1 aspect ratio.

---

**FORMAT 28: FEATURE ARROW CALLOUT / PRODUCT ANNOTATION**

Product in hand with editorial-style curved arrows pointing to benefit callouts. Feels annotated and educational.

**Template:**

Use the attached images as brand reference. Match exact brand colors and typography style. Create: a product annotation ad on a [BACKGROUND like warm cream/light yellow textured] background. Top: italic serif headline "[BENEFIT STATEMENT]" in [BRAND COLOR]. Below in massive bold sans-serif: "[VALUE PROP]". Center: [PERSON'S HAND] holding [YOUR PRODUCT] at a natural angle. Four curved arrows in [BRAND COLOR] pointing from the product outward to four benefit callout labels arranged around it in bold [BRAND COLOR] text: "[CALLOUT 1-4]". Arrows should feel hand-drawn or editorial, not rigid. Bottom: full-width [CONTRAST COLOR] banner with [PROMO TEXT] in bold [ACCENT COLOR] with optional emoji accents. 1:1 aspect ratio.

---

**FORMAT 30: HERO STATEMENT + ICON BENEFIT BAR**

Pure brand energy with a bold 2-3 word statement, lifestyle product photo, and icon benefit bar at the bottom.

**Template:**

Use the attached images as brand reference. Match exact brand colors, packaging, and typography. Create: a bold statement ad. Top 15%: white banner overlay with massive bold [BRAND COLOR] uppercase sans-serif headline: "[2-3 WORD POWER STATEMENT]" with a period for punch. Middle 55%: lifestyle product photo — [SCENE]. Product label and branding clearly visible. Bottom 25%: [SOFT BRAND COLOR] background. Three evenly spaced icon-and-text benefit columns: [ICON 1 + LABEL] | [ICON 2 + LABEL] | [ICON 3 + LABEL]. Icons are simple line-drawn in [BRAND COLOR] circles. Very bottom edge: scrolling ticker bar in [DARK BRAND COLOR] with repeating text: "[SOCIAL PROOF]". 1:1 aspect ratio.

---

**FORMAT 35: HERO PRODUCT SHOWCASE + STAT BAR**

Product as hero with exploded ingredient/element scatter and a clean stat bar at the bottom. Visually compelling for food, supplement, and beauty products.

**Template:**

Use the attached images as brand reference. Match the exact product design, wrapper, and brand colors precisely. Create: a product showcase ad on a [BACKGROUND COLOR] background. Top: large bold [BRAND COLOR] uppercase sans-serif headline: "[SUPERLATIVE CLAIM]". Below headline: white rounded-rectangle CTA button with [BRAND COLOR] uppercase text "[CTA]". Center: [YOUR PRODUCT] in full packaging, angled slightly, hero-lit with soft studio lighting. Surrounding the product: [SCATTERED ELEMENTS] arranged in an exploded/radial pattern creating visual energy and texture on the background surface. Bottom: a white or light rounded-pill stat bar spanning the width with three metrics separated by thin vertical lines: "[STAT 1]" | "[STAT 2]" | "[STAT 3]" in bold [BRAND COLOR] text. Numbers should be large and dominant, labels smaller below. 1:1 aspect ratio.

---

**FORMAT 37: HERO STATEMENT + ICON BAR + OFFER BURST (PROMO VARIANT)**

Same structure as Format 30 but with a promotional starburst badge and offer banner. Use during sales events.

**Template:**

Use the attached images as brand reference. Match the exact product design and brand colors precisely. Create: a promotional variant of a hero statement ad on a [BACKGROUND like dark charcoal/moody gray] background. Top 12%: white or light banner with massive bold [DARK COLOR] uppercase sans-serif headline: "[PROVOCATIVE 2-3 WORD STATEMENT]" with a period for punch. Upper-left of product area: a [BRIGHT ACCENT COLOR] comic-style starburst badge rotated slightly, reading "GET UP TO [DISCOUNT] OFF" in bold black text. Center: [PERSON'S HAND] gripping [YOUR PRODUCT] from above, lifting it off its [PACKAGING] below. Product label and branding clearly visible. Moody, slightly dramatic lighting. Bottom 20%: three evenly spaced icon-and-text benefit columns on a semi-transparent dark strip: [ICON 1 + LABEL] | [ICON 2 + LABEL] | [ICON 3 + LABEL]. Icons in simple line-art circles with [ACCENT COLOR] highlights. Very bottom: full-width [BRIGHT ACCENT COLOR] banner with bold [DARK] text: "[PROMO]". 1:1 aspect ratio.

---

### CATEGORY: EDITORIAL & PRESS

These formats mimic news articles, editorial content, or publication features. Best for brands with press coverage, authority positioning, or products that benefit from third-party validation.

---

**FORMAT 10: PRESS/EDITORIAL**

Authority play. Vogue back-page energy.

**Template:**

Use the attached images as brand reference. Create: a press ad on off-white linen background. Top: "As Featured In" in small [BRAND COLOR] uppercase wide-tracked text. Below: five grayscale publication logos. Center: italic serif pull-quote in [BRAND COLOR]: "[PRESS QUOTE]" with attribution. Lower third: [PRODUCT] at 85mm f/2.8, soft side light. [BRAND] logo bottom left. Generous white space. Full-page Vogue energy. 4:5 aspect ratio.

---

**FORMAT 20: ADVERTORIAL / EDITORIAL CONTENT CARD**

Looks like a news post, not an ad. The editorial framing creates curiosity and authority. Designed to blend into feed.

**Template:**

Use the attached images as brand reference for tone ONLY. Do NOT use polished ad layouts. This should look like organic editorial content. Create: a full-bleed moody portrait photo of [PERSON DESCRIPTION], warm amber-toned lighting, shot on 50mm f/1.8, shallow depth of field, cinematic color grade with warm highlights and cool shadows. Lower 45% of the frame is a text overlay zone: a prominent white rounded-rectangle pill label reading "[CATEGORY TAG like HOT TOPIC]" in centered uppercase sans-serif, sized to span roughly one-third of the frame width. Below: very large, dominant, bold all-caps condensed sans-serif headline filling the width of the frame in white text with key words in [HIGHLIGHT COLOR]: "[HEADLINE]". The headline should be oversized — at least 35% of the total frame height. Bottom center: "[@HANDLE]" in small white text. No product shot, no CTA button, no stars. This should read like a culture account post, not a paid ad. 4:5 aspect ratio.

---

**FORMAT 33: FAUX PRESS / NEWS ARTICLE SCREENSHOT**

Designed to look like a real online news article screenshot. Authority through editorial framing.

**Template:**

Use the attached images as brand reference. Create: a static ad designed to look like a real online news article screenshot. Top 25%: white background with a realistic major publication masthead/logo in large bold black serif text [PUBLICATION STYLE]. Below: thin gray horizontal rule. Small gray text "Latest Headlines" left-aligned. Then: bold black serif headline spanning full width: "[HEADLINE like 'It's my holy grail product': The $[PRICE] [PRODUCT CATEGORY] with over [NUMBER] five-star reviews]". Bottom 60%: two side-by-side casual UGC-style photos of [PEOPLE] each holding [YOUR PRODUCT] in a casual selfie pose — one taken in natural daylight, one in warm indoor evening light. Photos should look like real customer submissions, not studio shots. No brand logo. No CTA. Should look like an organic article screenshot someone would share to their story. 4:5 aspect ratio.

---

### CATEGORY: UGC & NATIVE

These formats are designed to look like real social posts, stories, notes app screenshots, or user-generated content. Best for audiences with high ad fatigue, younger demographics, or brands testing native-feeling creative against polished formats.

---

**FORMAT 8: BEFORE & AFTER (UGC NATIVE)**

Mirror selfie transformation. Must look like a real person posted it.

**Template:**

Use the attached images as brand reference for product color ONLY. This should look like a real person's post. Create: TikTok before-and-after. LEFT: grainy iPhone mirror selfie, [PERSON] in dimly lit bathroom, [BEFORE STATE], harsh lighting. White handwritten text: "[BEFORE DATE]". RIGHT: same person, same bathroom, bright natural light, [AFTER STATE], [PRODUCT] visible on counter. White text: "[AFTER DATE]". Top center: "[TIMEFRAME] on [BRAND]" with emoji. Should look stitched in CapCut. 9:16 aspect ratio.

---

**FORMAT 29: UGC + VIRAL POST OVERLAY**

Casual selfie with a Reddit/Twitter post screenshot overlaid. The hook is the opinion in the post, not the product. No product visible.

**Template:**

Use the attached images as brand reference for product color ONLY. Do NOT use ad layouts or polish. This should look completely native and organic. Create: a casual selfie of [PERSON] doing something mundane [ACTION]. iPhone front camera, slightly grainy, bathroom/kitchen lighting, no professional setup. Overlaid in the center of the frame: a realistic screenshot of a [PLATFORM like Reddit / Twitter / X] post. [POST DETAILS like subreddit name, username, timestamp, upvote count]. Post title in bold: "[PROVOCATIVE OPINION HEADLINE related to the product's problem/benefit space]". Post body in regular text: "[2-3 sentences expanding on the opinion]". The post should feel like the person is reacting to it or sharing it — NOT selling a product. No product visible. No brand logo. No CTA. The hook is the opinion. 9:16 aspect ratio.

---

**FORMAT 32: UGC STORY CALLOUT / TEXT BUBBLE EXPLAINER**

Must look like a real person's Instagram Story. Casual iPhone photo with highlighted text bubbles scattered across the frame.

**Template:**

Use the attached images as brand reference for product color and packaging ONLY. Do NOT use ad layouts or polish. This must look like a real person's Instagram Story. Create: a casual iPhone photo of [PERSON DESCRIPTION] holding [YOUR PRODUCT with key packaging details] at a slight angle over [SURFACE/SETTING]. Natural overhead daylight, slightly warm, iPhone 15 quality. Scattered across the frame: 5 text bubbles using Instagram Story's built-in highlighted text tool. Each bubble must have a highlighted background for readability, with varied highlight colors between bubbles. Bubble 1: "[TOPIC + EMOJI]" large and bold. Bubble 2: "[EDUCATIONAL HOOK — a surprising stat or mechanism about why this category matters]". Bubble 3: "[WHY THIS PRODUCT — the specific feature that makes it different, excited informal tone]". Bubble 4: "[PERSONAL RESULT — early experience update, first-person, with emoji]". Bubble 5: "[BRAND ENDORSEMENT — one short line of approval]". Should feel casual and hand-placed, not designed. 9:16 aspect ratio.

---

**FORMAT 34: FAUX iPHONE NOTES / APP SCREENSHOT**

Static ad disguised as an iPhone Notes app screenshot. Native platform UI as the creative container.

**Template:**

Use the attached images as brand reference. Match the exact product design and packaging precisely. Create: a static ad disguised as an iPhone Notes app screenshot. Top: realistic iOS status bar (time "[TIME]", signal bars, wifi icon, battery icon). Below: iOS Notes navigation — blue "< All iCloud" back arrow left, share icon and three-dot menu icon right. Below nav: small gray timestamp text "[DATE]". Main content area on white background: bold black serif headline "[HEADLINE]". Below: [3 BENEFIT ROWS], each with a [BRAND COLOR] filled circle checkmark + [EMOJI] + bold black text using food-equivalency format: "[BENEFIT 1]" / "[BENEFIT 2]" / "[BENEFIT 3]". Right side, overlapping the benefit text slightly: [YOUR PRODUCT] at a slight angle with [DETAILS]. Product should feel casually placed into the note layout, breaking the frame slightly. Clean white background throughout. 1:1 aspect ratio.

---

**FORMAT 36: WHITEBOARD BEFORE / AFTER + PRODUCT HOLD**

Lifestyle photo with a hand-drawn whiteboard illustration showing before/after. Casual, educational, believable.

**Template:**

Use the attached images as brand reference for product packaging ONLY. Do NOT use ad layouts or polish. This should look like a real person's photo. Create: a lifestyle photo set in [SETTING like a bright modern kitchen]. In the background: a small tabletop dry-erase whiteboard or flip-chart propped up on [SURFACE]. On the whiteboard: two simple hand-drawn black marker line illustrations side by side — left drawing labeled "[BEFORE LABEL]" showing [BEFORE STATE], an arrow pointing right to a second drawing labeled "[AFTER LABEL]" showing [AFTER STATE]. Below the drawings on the whiteboard: handwritten text in black marker "[HANDWRITTEN CTA]". In the foreground: [PERSON'S HAND] holding [YOUR PRODUCT] up next to the whiteboard, positioned in the lower-right of the frame. Product label clearly visible. Shot on iPhone, natural kitchen lighting, casual and educational. 4:5 aspect ratio.

---

**FORMAT 38: UGC LIFESTYLE + PRODUCT + REVIEW CARD (SPLIT)**

Vertical split with casual UGC-style photo on one side and product plus review card on brand-colored background on the other.

**Template:**

Use the attached images as brand reference. Match the exact product design and brand colors precisely. Create: a vertical split social proof ad. Left 55%: a casual UGC-style photo of [PERSON] enjoying the product in context — [ACTION]. Natural lighting, warm and inviting, iPhone-quality casual feel. The person should look genuinely happy, not posed. Right 45%: solid [PRIMARY BRAND COLOR] background. Top-right: small decorative sparkle/star accents in [ACCENT COLOR]. Floating center-right: [YOUR PRODUCT] at a slight angle, studio-lit on the colored background. Below product: a white rounded-rectangle review card with: five filled [ACCENT COLOR] stars at top, then italic or casual serif text: "[SHORT REVIEW QUOTE]" in [BRAND COLOR]. Bottom center: [BRAND LOGO] in white on the colored background, with small decorative sparkle accents. 4:5 aspect ratio.

---

**FORMAT 40: NATIVE / UGLY POST-IT NOTE STYLE (PRODUCT HERO)**

Lifestyle product photo that looks found, not composed. A hand-written post-it note stuck on the product carries the message. Maximum organic energy.

**Template:**

Use the attached images as brand reference. Match the exact [PRODUCT DESCRIPTION — shape, color, label details, key typography on packaging] precisely. Create: a lifestyle product photo set in [REAL-LIFE SETTING] with [LIGHTING DESCRIPTION] and a naturally blurred background showing [BACKGROUND DETAILS]. Frame is very slightly off-center — product not perfectly centered, [LEFT / BOTTOM / RIGHT] edge of product very slightly cropped — feels found rather than composed. Slight natural sensor grain consistent with a phone camera in indoor daylight. Subtle natural vignette at frame corners. Center of frame, large and dominant: [FULL PRODUCT DESCRIPTION] sitting on [SURFACE], slightly angled toward the viewer. [SCATTERED SURFACE DETAIL] on the surface around the base of the product for casual realism. Stuck directly onto the front face of the product: a [POST-IT COLOR] square post-it note, slightly crooked and not perfectly straight — slightly trapezoid from the angle it was pressed on. Realistic paper texture with a horizontal crease across the middle as if it was folded once. Subtle curl at bottom-right corner only. Held at the top by a small piece of [TAPE COLOR] tape, slightly wrinkled — not a self-adhesive strip. One word in the handwriting is slightly heavier-inked or underlined from natural pen pressure. Handwritten in thick black marker-style lettering, imperfect and uneven, lowercase natural writing — not formatted, not centered, not evenly spaced: "[LINE 1 — lowercase, short, setup or hook]" line break "[LINE 2 — continuation or turn]" line break "[LINE 3 — punchline, result, or kicker]" line break "[LINE 4 — optional final beat or emoji]" No attribution line. No signature. Bottom center of frame, outside the photo on a plain white or off-white strip: small plain lowercase sans-serif caption text, looks like someone typed it under an organic post: "[brand url] — [3-5 word casual caption, sounds typed not written]" No logo overlay anywhere in the frame. Brand identity carried entirely by the product packaging visible in the photo. No border. [MOOD — 3 adjectives]. 4:5 aspect ratio.

---

### CATEGORY: COPY-LED & CURIOSITY

These formats lead with provocative headlines, bait-and-switch quotes, or manifesto-style copy where the writing IS the ad. Best for brands with a strong voice, controversial positioning, or when the emotional angle is stronger than the visual product.

---

**FORMAT 9: NEGATIVE MARKETING (BAIT & SWITCH)**

Fake bad review that's actually a rave. Scroll-stopper.

**Template:**

Use the attached images as brand reference. Create: Background is close-up of [PRODUCT], slightly blurred. Center: white rounded-rectangle review card (Amazon-style). Gray user icon, "[NAME]", one gold star + four gray, orange "Verified Purchase" badge, bold text: "[BAIT that sounds negative but is positive]". Bottom: bold white sans-serif "[PUNCHLINE]". [BRAND] logo bottom right. 4:5 aspect ratio.

---

**FORMAT 16: CURIOSITY GAP / HOOK QUOTE TESTIMONIAL**

The bait-and-switch testimonial. Provocative headline forces the double-take. The reveal reframes it. Scroll-stop machine.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and typography style precisely. Create: a static ad on a clean white background. Top center: large [ACCENT COLOR] opening quotation marks. Below: mixed-weight headline in black — the first line in italic serif or semi-bold reading "[SETUP LINE]", the next two lines in enormous heavy-weight bold all-caps sans-serif reading "[BAIT PHRASE]", followed by a smaller sentence-case line reading "[REVEAL]". Closing quotation marks and "[ATTRIBUTION]" in regular weight. Left side bottom third: [YOUR PRODUCT] at a slight angle with [PRODUCT DETAILS]. To the left of the product: a [TRUST BADGE]. Right side bottom third: [NUMBER] filled [ACCENT COLOR] stars and bold text reading "[REVIEW COUNT] 5-Star Reviews" with a [BRAND ICON]. Bottom edge: small disclaimer text "[DISCLAIMER]". 1:1 aspect ratio.

---

**FORMAT 21: BOLD STATEMENT / REACTION HEADLINE**

Pure brand energy. No stats. No reviews. Just a provocative line, a hot gradient, and the product. The copy IS the ad.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and visual tone precisely. Create: a static ad on a vibrant [GRADIENT] gradient background, flowing diagonally from upper left to lower right. Upper left: oversized playful [FONT STYLE] white headline reading "[BOLD STATEMENT]" — text should feel loose, fun, and expressive, not rigid or corporate. Right side: [PERSON DETAIL] grabbing from [YOUR PRODUCT]. Product sits center-right, slightly below midline. Bottom left: [BRAND] logo in [LOGO COLOR] with "[PRODUCT DESCRIPTOR]" in smaller text below. No stats, no reviews, no badges. The gradient and the headline do all the work. 1:1 aspect ratio.

---

**FORMAT 23: LONG-FORM MANIFESTO / LETTER AD**

Copy-dominant. No background imagery — text is the entire creative. The writing IS the ad.

**Template:**

Use the attached images as brand reference. Match exact brand typography style and tone. Create: a copy-dominant manifesto ad on a clean white background. No background imagery — text is the entire creative. Top: oversized bold black serif or sans-serif headline reading "[PROVOCATIVE HEADLINE]" spanning the top 15%. Below: left-aligned body copy in smaller regular-weight black text, structured as short punchy sentences and line breaks (NOT paragraphs), building a persuasive argument about [CORE BRAND TENSION]. The copy should flow through: acknowledging the objection, listing what you'd lose if they cut corners, reframing as a positive, closing with a confident brand statement. Approximately [12-18 LINES] of copy. Bottom 20%: [YOUR PRODUCT] centered or slightly right, product-only on white, clean studio shot angle. No icons, no badges, no CTA button. The writing IS the ad. 1:1 aspect ratio.

---

**FORMAT 39: CURIOSITY GAP + SCROLL-STOPPER HOOK**

Truncated social caption with a problem-visual photo below. No product. No logo. No CTA. The entire purpose is to provoke curiosity and earn the click.

**Template:**

Use the attached images as brand reference for visual tone ONLY. Do NOT include any product, logo, or branding. Create: a scroll-stopping curiosity ad designed to look like a truncated social media post. Top 35%: clean white background with large bold black sans-serif text (heavy weight, tight leading): "[HOOK HEADLINE]". The last few words should be followed by "...more" in lighter gray text, mimicking a truncated Facebook/Instagram caption that requires clicking "more" to expand. Bottom 65%: a close-up, slightly uncomfortable or attention-grabbing photo of [PROBLEM VISUAL]. Photo should feel real and editorial, not stock. Slightly shallow depth of field. No text on the photo. No product. No logo. No CTA. The entire purpose is to provoke curiosity and earn the click. 1:1 aspect ratio.

---

### CATEGORY: LIFESTYLE & FLAVOR

These formats put the product in context — action shots, flavor visualization, data-driven lifestyle scenes. Best for food/beverage, fitness, fashion, or any product where the use experience matters more than specs.

---

**FORMAT 12: LIFESTYLE ACTION + PRODUCT COLORWAY ARRAY**

Action hero shot sells the use case. Fanned product lineup sells the range. Two conversion jobs in one frame.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and visual tone precisely. Create: a static ad with a [LIFESTYLE PHOTO DESCRIPTION] occupying the left two-thirds of the frame, shot outdoors in [SETTING], bright natural daylight. [BRAND] logo top center in bold. Below logo: large bold sans-serif quote text reading "[ENDORSEMENT HEADLINE]" in [TEXT COLOR]. Bottom right foreground: three [PRODUCT VARIANTS] fanned in an overlapping arrangement showing [COLOR 1], [COLOR 2], and [COLOR 3]. Products are crisp and studio-lit against the lifestyle background. Shot on 50mm f/2.0, lifestyle background slightly softer than foreground product. [MOOD]. 1:1 aspect ratio.

---

**FORMAT 22: FLAVOR STORY / "TASTES LIKE"**

Flavor-visualization ad. Full background is an indulgent food scene. Product is placed into the scene as the payoff.

**Template:**

Use the attached images as brand reference. Match the exact product design, colors, and packaging precisely. Create: a flavor-visualization ad. Full background is a photorealistic close-up food scene of [INDULGENT FOOD]. Shot at 50mm f/2.8, shallow depth of field, warm bakery lighting. Top third: large bold white sans-serif headline reading "[HEADLINE like A protein bar that tastes like freshly baked raspberry donuts]" with one key word in bold italic for emphasis. [YOUR PRODUCT] packaged unit placed bottom-right, angled 15 degrees as if casually laid into the scene. Bottom: semi-transparent white bar spanning full width with three stat columns separated by thin vertical lines: "[STAT 1]" | "[STAT 2]" | "[STAT 3]". Very bottom edge: smaller bold sans-serif "[CLEAN LABEL CLAIM]". Food is the hero — product is the payoff. 1:1 aspect ratio.

---

**FORMAT 26: STAT CALLOUT (DATA-DRIVEN LIFESTYLE)**

Lifestyle photography top half, data-driven headline bottom half. The statistic IS the headline.

**Template:**

Use the attached images as brand reference. Match exact brand colors and typography. Create: a statistic-led ad. Top 50%: lifestyle product photography — [SCENE]. Product packaging visible in frame. Middle: brand logo centered with thin horizontal rules on either side as a visual divider. Bottom 50%: dark gradient overlay (fading from transparent to [DARK COLOR]). Large bold uppercase sans-serif text: "[STAT-DRIVEN HEADLINE with specific percentages]". Key result phrases highlighted in [ACCENT COLOR]. The statistic IS the headline — no separate subhead needed. 4:5 aspect ratio.

---

### CATEGORY: OFFER & PROMOTION

---

**FORMAT 2: OFFER/PROMOTION**

The money-maker. Test your core offer.

**Template:**

Use the attached images as brand reference. Match exact brand colors and typography style. Create: a promotional ad with a split background. Top 60% is [PRIMARY BRAND COLOR] and bottom 40% is [CONTRAST COLOR like warm cream]. [YOUR PRODUCT] sits centered where colors meet, soft studio lighting. Upper area: large [CONTRAST TEXT] sans-serif reading "[YOUR OFFER]". Below: "[OFFER DETAILS]". Lower section: small [BRAND COLOR] text with [VALUE ADDS]. [BRAND] logo bottom right. 9:16 aspect ratio.

---

## Data Integrity Rules For Image Ad Prompts

These rules are non-negotiable when filling in templates:

- **Do NOT fabricate statistics.** If the brand has 42,000 five-star reviews, use that number. If you don't know the exact number, write "[INSERT ACTUAL REVIEW COUNT]" and flag it for the user. Never invent a number that sounds good.
- **Do NOT fabricate testimonials.** Every customer quote must come from actual review data. Pull the exact quote. Use the customer's real first name and last initial. Do not write a quote that "sounds like" something a customer would say.
- **Do NOT guess at product details.** Packaging colors, label text, ingredient claims, nutritional stats — all of this must come from verified brand data or the product images provided. If you don't have a detail, flag it.
- **Do NOT use generic marketing copy when you have data.** If the customer reviews contain language like "I can't stop smelling my man after he showers," use that. It will always outperform anything you generate from scratch. Parker's entire advantage is access to real customer language. Use it.
- **Do flag anything that needs verification.** If a prompt contains a stat, claim, or detail you're not 100% certain about, mark it clearly so the user can verify before generating.
