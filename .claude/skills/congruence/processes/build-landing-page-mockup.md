# Build the Congruence landing-page mockup

Run this process only after a completed Congruence audit triggers it or the user explicitly asks for the mockup. The deliverable is working local code plus verified mobile and desktop views. It is not a live-site edit.

## 1. Lock the repair brief

Carry forward:

- the exact ad, audience assumption, delivery read, promotion, product, offer, proof, and call to action;
- the two landing-page seam scores and the evidence that lowered them;
- the smallest first-screen and page changes that would repair those seams;
- every legal, factual, and brand constraint already observed.

Do not turn a focused repair into a wholesale rebrand. Do not invent claims, discounts, scarcity, reviews, certifications, product capabilities, or customer quotes.

## 2. Study the company's real design language

Inspect the rendered destination, homepage, exact product page, and one or two representative current pages. When a Parker Brain exists, also read its brand identity, website and product, visual vocabulary, voice, and current strategy surfaces. Capture receipts for:

- official logo and wordmark treatment;
- served font families, weights, type scale, line height, and letter spacing;
- colors and semantic use, including backgrounds, text, borders, actions, and sale states;
- grid, container width, spacing rhythm, density, radius, border, shadow, and image cropping;
- header, announcement bar, navigation, footer, buttons, forms, product cards, accordions, and other repeated components;
- photography, illustration, product imagery, people, art direction, and mobile behavior.

Use browser evidence and computed styles when available. A screenshot shows the result; computed styles and source assets show how it was made. If the site has inconsistent patterns, copy the page family closest to the destination rather than averaging the whole brand.

## 3. Build a brand asset packet

Use official, company-owned assets already served on its site or supplied by the user. Download or reference the correct logo, product imagery, campaign imagery, icons, and fonts when their use is permitted. Preserve proportions and image quality. Record every asset's source URL.

Do not take imagery, layouts, or copy from competitors. Do not hotlink an asset when a local copy is allowed and more reliable. If a required brand asset cannot be used, say so and use a clearly marked neutral placeholder rather than generating a fake product or fake customer.

## 4. Resolve the design tools

Discover the design and frontend skills available in the user's environment. Prefer user-owned and company-specific design skills over generic taste. When `ui-ux-pro-max` or an equivalent design-system skill is available, use its design-system and UX checks, but treat extracted brand evidence as the source of truth for colors, fonts, spacing, radius, shadows, and visual style.

If 21st.dev, shadcn/ui, or another component source is connected, use it to find a strong interaction or accessible component only when it helps. Restyle it to the brand's tokens. Never let a component library make the page look like the library instead of the company.

## 5. Implement the smallest convincing page

Use the site's existing codebase, framework, tokens, and components when available. Otherwise create a self-contained local web mockup in:

- a Parker brand brain: `audits/congruence/[YYYY-MM-DD]-[ad-id]/mockup/`;
- another workspace: `congruence-output/[YYYY-MM-DD]-[ad-id]/mockup/`.

Build mobile first, then desktop. Preserve the recognizable shell and design system. Repair the ad handoff above the fold first, then add only the sections needed to continue the promise, handle the delivered audience's real questions, and support the action.

Interactive elements must work in the mockup. Keep checkout, lead submission, tracking, and other production side effects disconnected. Use a safe demo state for calls to action and forms.

## 6. Remove the design tells

Read `references/mockup-standard.md` and review the page against it. Brand evidence overrides generic design recommendations. A polished page that looks like an AI template is a failed result.

## 7. Run and visually verify

Install only the dependencies the chosen stack actually needs. Run the mockup locally and inspect it in a browser at a minimum of 375 pixels wide and 1440 pixels wide. Also check an intermediate tablet width when layout changes.

Verify:

- the first screen immediately continues the ad's audience, product, promise, promotion, and action;
- real fonts, colors, assets, and component behavior match the reference site;
- body copy is at least 16 pixels on mobile, contrast is readable, focus states are visible, touch targets are at least 44 by 44 pixels, and no horizontal scroll appears;
- images reserve space and keep the intended crop;
- overlays do not block the main action;
- buttons, accordions, galleries, selectors, and demo forms work;
- the browser console shows no implementation errors.

At every required viewport, measure `document.documentElement.scrollWidth` against `document.documentElement.clientWidth`. They must be equal. Also inspect long announcement-bar copy, offer lines, button groups, navigation, product selectors, and dialog content; these are common sources of mobile overflow. A screenshot that clips text or a page that scrolls sideways fails the mockup gate. Do not hide the evidence with `overflow-x: hidden` or `clip`; repair the element causing it.

Save full-page mobile and desktop screenshots beside the code. Do not call the mockup complete until the screenshots have been opened and visually inspected. Check for an installed browser, connected browser tool, Playwright, or another renderer before declaring screenshots unavailable. If no renderer exists after that check, report the mockup as blocked at visual verification rather than complete. Compare the captures with the reference-site captures and repair visible drift before delivery.

## 8. Deliver the artifact

Return:

- the mockup folder and the simplest command to run it;
- a local preview URL when one is active;
- mobile and desktop screenshot paths;
- the exact Congruence seams repaired;
- the brand pages, fonts, colors, components, and assets carried forward;
- anything left as a placeholder and why;
- the explicit note that the live site was not changed.
