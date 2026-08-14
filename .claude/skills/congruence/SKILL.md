---
name: congruence
description: Score how well one Meta ad's message, on-screen person, actual age-and-gender delivery, and landing-page experience align from click to conversion. Use for ad-to-page congruence audits, audience-message-match checks, creative-versus-delivery investigations, landing-page alignment reviews, or comparisons of which ad journeys feel most intentionally made for the people Meta reaches.
---

# Congruence

## Goal

Audit one exact path from ad impression to landing page and give it an evidence-backed score from 1 to 10. Find where the experience stops feeling as if it was made for the same person. When the landing page is the break, build a working local mockup that shows the repair in the company's own design language.

This is not a general ad critique, a full CRO audit, or an account-wide performance report. It joins three surfaces that are often reviewed separately:

1. the full ad and the audience it signals through its message, person, voice, and visuals;
2. the age-and-gender groups Meta actually reaches and the performance inside those groups;
3. the exact landing page those people reach after the click.

## Read the method first

Read these files completely before starting:

- `parker-system/creative-strategy-context/congruence.md`, or `creative-strategy-context/congruence.md` in a flat Parker Brain;
- `parker-system/creative-strategy-context/ad-account-analysis.md`, or its flat equivalent;
- `parker-system/creative-strategy-context/static-ad-design.md` for a static ad;
- `parker-system/creative-strategy-context/visuals.md` for any visual read;
- `parker-system/system/parker-tools.md`, or its flat equivalent.

Use the strategy file in this skill to lock the scope and data path. Then run `processes/run-congruence-audit.md`. When its landing-page trigger fires, also run `processes/build-landing-page-mockup.md` and use `references/mockup-standard.md`. Format the result with `references/report-template.md`.

## Hard evidence gate

Do not begin scoring until all three evidence groups are available for the same ad:

- **Full creative:** the static image, or the complete video with frames, spoken words, on-screen text, caption, and primary text. An ad name, thumbnail, tag, or campaign label is not a creative read.
- **Ad-level delivery:** age, gender, or combined age-and-gender delivery for the exact ad and one stated date window. Require a delivery measure such as spend or impressions and at least one meaningful outcome measure for the campaign objective. Use the same attribution setting across the comparison.
- **Exact destination:** the final landing-page URL after redirects plus a rendered mobile view and the page's actual copy. Source code, metadata, or a URL alone is not the page experience.

If the evidence cannot be joined to one ad ID and variant, stop. Do not substitute account-wide demographics, a similar ad, the brand homepage, or a different date window.

If volume is too low for a meaningful demographic outcome read, widen the date window when appropriate. If the evidence is still sparse or suppressed, do not issue an overall score.

## Data-source order

1. **Prefer Parker MCP.** Discover the available tools rather than guessing a server prefix. Confirm Parker by calling `get_available_brands`, lock the correct `brand_id`, and use the live Parker tools for owned Meta creative and performance. Use `get_current_time` when setting the window. Use `get_webpage` for the known destination's page content, while using an available browser or supplied capture for the rendered mobile experience.
2. **Try another authorized source if Parker cannot supply the required evidence.** Look for a connected Meta Ads source, measurement platform, data warehouse, or other tool that returns exact ad-level delivery and the complete creative. Keep source names, filters, IDs, dates, and attribution attached.
3. **Accept a direct evidence packet.** A fresh Meta export joined to the exact ad ID, the creative file or playable URL, and the exact landing-page capture can satisfy the gate.
4. **Stop when no path satisfies the gate.** Say: `I can't run the Congruence audit yet because I can't reach both the full creative and the exact ad-level delivery data. Parker MCP is the preferred connection. Connect it at https://app.heyparker.ai/dashboard/parker-brain, connect another source that carries both, or provide a fresh Meta export with the creative.` Name any landing-page evidence that is also missing.

Do not quietly downgrade this into a creative-only or page-only review. The joined read is the value of the skill.

## Run order

1. Lock one brand, one ad ID or variant, one destination, one objective, one date window, and one attribution setting.
2. Read the full creative and state the audience assumption from message, person, voice, visuals, product, awareness level, and desired action.
3. Read actual delivery and outcomes by age and gender. Keep delivery concentration separate from performance concentration.
4. Inspect the exact rendered landing page, mobile first. Read the first screen, message, person and imagery, product, offer, proof, objections, readability, and next action.
5. Score the four seams using the canonical anchors and evidence. Run the bundled scoring script for the weighted result.
6. Name the largest score leak and the smallest set of changes most likely to raise the score.
7. If either landing-page seam scores 6.0 or lower, or the page is generic enough that it drops the ad's core audience, promotion, product, or promise, build and visually verify a local landing-page mockup. Use the brand's real design language and owned assets. Never change the live site.
8. Close with sources and limitations.

## Scoring contract

Score each seam from 1.0 to 10.0:

- Ad message and person shown: 20%
- Intended audience and actual delivery: 30%
- Ad promise and landing page: 25%
- Delivered audience and landing-page experience: 25%

If no person appears, score the message against the ad's primary visual subject instead. Calculate the overall score with the bundled script:

```text
python3 <resolved-skill-directory>/scripts/score_congruence.py \
  --ad-message-person <score> \
  --audience-delivery <score> \
  --ad-page <score> \
  --delivery-page <score>
```

Never estimate the weighted result by eye. Never fill a missing seam with an average. If any seam is unscorable, withhold the overall score and say what evidence is missing.

The calculator also returns `landing_page_mockup_required`. Treat that as the normal trigger. A clearly generic or irrelevant page can also trigger the mockup even when a borderline score rounds above 6.0; explain the evidence for the override.

## Multiple ads

Audit each ad independently before ranking them. Do not let one ad borrow another ad's creative, demographics, destination, or score. Rank only completed audits by the weighted overall score, and show each ad's largest leak beside its rank.

## Guardrails

- Treat age and gender as platform delivery breakdowns, not the whole truth about identity or intent.
- Do not infer ethnicity, health, religion, sexuality, income, or other sensitive traits from appearance.
- Describe visible presentation cautiously. A person in an ad can be a customer, authority, founder, caregiver, spokesperson, or contrast character; do not assume they are the target without reading their role.
- Do not blame messaging alone for a delivery mismatch. Objective, auction conditions, budget, placements, offer, account structure, and Meta's breakdown effect can also shape delivery.
- Do not recommend excluding a profitable group just because it differs from the stated audience. Treat it as evidence to understand.
- The mockup is a local first pass, not permission to edit, publish, or deploy the company's live site. Keep live checkout, forms, tracking, and customer data disconnected.
- Preserve the existing brand before adding design ideas. Do not replace its typography, colors, spacing, radius, imagery style, header, footer, or interaction patterns with a generic component-library look.
- Keep observed facts, supplied claims, calculations, and inference separate.
- Do not invent hyphenated compounds. Write the sentence in plain English instead.

## Output requirements

Use `references/report-template.md`. The output must include:

- one weighted score out of 10 when all seams are scorable;
- all four seam scores, weights, and evidence;
- the audience assumption made from the ad;
- delivery and performance by age and gender;
- the landing-page experience for the people actually reached;
- the largest break in the path;
- prioritized changes tied to the score;
- a working local mockup, mobile and desktop screenshots, and its file path or preview URL whenever the landing-page trigger fires;
- source IDs, URLs, tools, windows, filters, attribution, calculations, and limitations.

Do not show hidden chain-of-thought. Show the evidence and concise scoring rationale a strategist can verify.
