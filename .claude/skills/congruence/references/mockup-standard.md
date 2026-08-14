# Congruence mockup quality standard

The mockup should look like the company's team made a more relevant version of its own page. It should not look like an outside designer imposed a new system, and it should not look AI generated.

## Brand fidelity test

A teammate should recognize the company before reading the logo. Match the real site's:

- font files, type scale, weight, line height, and headline behavior;
- exact color roles, not merely similar colors;
- container width, grid, whitespace, density, and section rhythm;
- corner radius, borders, shadows, dividers, and image crops;
- button shapes, labels, interaction states, and action hierarchy;
- header, announcement bar, footer, product treatment, photography, and icon style.

When the current site does something unusual, preserve it unless it causes the Congruence break or a serious usability problem.

## Ad handoff test

Without being told, a reviewer should be able to match the mockup to the source ad. The mobile first screen must carry the important combination of:

- person or primary subject;
- problem, desire, or use moment;
- product or SKU;
- promise and promotion;
- proof appropriate to the claim;
- next action.

Do not repeat every ad line. Continue the expectation the click created.

## Common AI design tells to remove

Unless the source site already uses them consistently, avoid:

- purple or blue gradients, glows, blobs, glass panels, and decorative grids;
- a pill label above every headline;
- every section centered and every idea inside a rounded card;
- generic bento layouts, three-column feature grids, and alternating text-image blocks used without a content reason;
- random Lucide icons, emoji, fake logos, fake awards, fake review avatars, and invented star ratings;
- oversized empty heroes, vague copy, symmetrical marketing triads, and sections added only to fill space;
- one font, radius, shadow, or spacing value that drifts from the source site;
- excessive scroll animation, parallax, or hover movement that the source site does not use;
- component-library defaults that were never translated into the brand.

## Interface floor

- Start mobile first and test at 375, 768, 1024, and 1440 pixels when the layout changes.
- At each tested width, require page `scrollWidth` to equal `clientWidth`; a single clipped offer line, announcement, control, or dialog is a failure. Do not mask overflow with `hidden` or `clip` on the page.
- Use semantic HTML, logical headings, alt text, keyboard navigation, visible focus, and reduced-motion support.
- Keep mobile body text at least 16 pixels, normal text contrast at least 4.5 to 1, and touch targets at least 44 by 44 pixels.
- Use one clear primary action per screen state.
- Reserve image dimensions, avoid layout shift, and load below-fold media lazily.
- Use consistent design tokens rather than scattered raw values.
- Make every visible control work; do not ship dead buttons or decorative form fields.

## Final comparison

Open the actual full-page screenshots and place the reference-site mobile capture, broken-page capture, and mockup capture side by side. Ask:

1. Does this still look unmistakably like the brand?
2. Does it now feel unmistakably connected to the ad?
3. Does it make more sense for the people Meta actually reaches without stereotyping them?
4. Did the mockup repair the failed seam instead of redesigning unrelated parts?

If any answer is no, revise before delivery.
