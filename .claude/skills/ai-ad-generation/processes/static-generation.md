# Process — AI Static Generation

Generate a brand-grounded prompt for an AI image model. Pulls from the proven format library, picks the right format(s) for the brand's situation, and fills the bracketed fields with brand-specific values sourced from real data.

The output is prompt text that gets pasted into an image model alongside brand reference images. The model handles the visual generation; the prompt's job is to direct it precisely so the output reads as on-brand rather than as generic category styling.

## Required inputs

- The brand's situation — what objective the ad serves, what audience it targets, what creative challenge it addresses.
- Brand context — ICP, voice, visual identity, compliance, customer language pulled from reviews.
- Brand reference images if available. The image model uses these to match colors, typography, and brand tone.
- Customer review data with verifiable quotes if any of the chosen formats require testimonials, social proof, or quoted copy.
- Format preference if the user has one. Otherwise, the strategy picks based on the brand situation.

## Format library reference

The full library lives at `parker-system/creative-strategy-context/ai-static-ad-generation.md`. Eight categories cover the proven format families:

- **Social proof & testimonials.** Customer voices, review data, star ratings, verified badges. Pick for trust-sensitive categories, high-consideration purchases, or retargeting where one more trust signal closes the deal.
- **Comparison & competition.** Side-by-side against competitors or generic category. Pick for crowded markets, products with measurable advantages, or audiences who frequently mention switching from competitors.
- **Product hero & benefits.** Product as visual focus with benefit-led copy. Pick for visually striking products, new launches, or category-defining hero shots.
- **Editorial & press.** Editorial styling and earned press logos. Pick for brands with real press coverage. Only use logos and mentions the brand has actually earned — never fabricate.
- **UGC & native.** Organic-feeling images that mimic user-generated content. Pick for trust-sensitive categories or when ad-style imagery is underperforming because it reads as too polished.
- **Copy-led & curiosity.** Bold typography-led layouts driven by headline strength. Pick when the message is the asset, when the brand has a strong customer-language headline, or when product visuals are not yet hero-worthy.
- **Lifestyle & flavor.** Scene-driven imagery showing the product in context. Pick for lifestyle brands, food and drink, anything where the experience is the sell.
- **Offer & promotion.** Discount, urgency, and seasonal callouts. Pick during promotional periods, around holidays, or when a real time-sensitive offer is in market.

Within each category are multiple specific formats (Format 1, Format 3, etc. in the source library). The strategy picks the category first based on the brand's situation, then picks the specific format based on what is being tested and what bracketed fields the brand can credibly fill.

## Execution

1. **Pick the format category.** Based on the brand's situation, ICP, current creative challenges, and what the brand has not yet tested. Reference the category-level descriptions above.

2. **Pick the specific format within the category.** Each format inside the library has its own template with a specific structure (headline-only, testimonial card, social proof stack, etc.) and tests something specific (text rendering, composition depth, organic feel). Pick the format that matches the brand's situation and the bracketed fields it can fill with verified data.

3. **Source the bracketed values from real data.**
   - **Headlines and supporting copy.** From customer language in reviews, comments, or surveys. Apply the headlines skill's discipline if needed.
   - **Customer quotes.** Verbatim from real reviews. Never invented.
   - **Stats, ratings, member counts.** From verified brand data. Never invented.
   - **Press logos.** Only earned ones.
   - **Product details.** From actual product specs and packaging.

4. **Fill the template.** Replace every bracketed field with the brand-specific value. Keep the non-bracketed structural language exactly as-is — that scaffolding has been tested to produce clean output from image models.

5. **Instruct the model to use brand reference images.** Every prompt should open with language directing the model to match the brand's product colors, typography style, and brand tone precisely using the attached reference images.

6. **Match aspect ratio to placement.** 1:1, 4:5, 9:16, or 16:9. State explicitly in the prompt.

7. **Check compliance one more time.** Every claim, every stat, every quote passes through compliance before output.

## Output

- **FORMAT BRIEF.** Format name (from the library), what it tests, aspect ratio, why this format fits the brand's situation.
- **THE PROMPT.** The complete prompt with all brackets filled. Self-contained — the user pastes it into the image model alongside brand reference images.
- **WHY THIS FORMAT FITS.** Two-to-four-sentence rationale on the format choice, the customer language used, and the brand alignment.
- **Brand Context Applied.**

## What never to do

- Pick a format whose bracketed fields the brand cannot fill with verified data. Picking a testimonial format and then inventing the testimonial defeats the entire process.
- Use marketing voice in headlines or quotes. Customer language only.
- Fabricate press logos, stats, ratings, or member counts.
- Generate a prompt that ignores the brand's actual visual identity. Reference images are not optional when they exist.
- Use a forbidden term in any visible copy.
- Skip the aspect ratio specification.
