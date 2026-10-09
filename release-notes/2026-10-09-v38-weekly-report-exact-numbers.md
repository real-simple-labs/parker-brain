# v38 — the weekly creative report shows exact numbers (2026-10-09)

The weekly creative report skill shipped in v37, which bundled everything merged since v34 (v35 and v36 were never tagged on their own). Its first live run, on Reach International Outfitters for Week 40, showed the report rounding and shortening numbers: $189,538.26 on the page read as $190K, and cost per purchase lost its cents. Agencies check these reports against Ads Manager line by line, so v38 makes every number exact.

## What shipped

- **Exact numbers, never rounded.** Every number on the page is the exact value Parker pulled: $189,538.26, not $189.5K; 63.29%, not 63%; dollars always with cents. The report's own words follow the same rule, so the headline and takeaways quote exact figures too. The only numbers shown to two decimals are ones Parker calculates that don't end (a week-over-week change, a share of spend), and chart gridline labels stay short because they're a scale, not data. Agencies check these reports against Ads Manager line by line, and a rounded number reads as a wrong one. Long ad names in the full table wrap so the wider numbers fit.
- **Writing rule.** `SKILL.md` and `report-schema.md` tell Parker to write the headline, takeaways, and every line of text with exact figures too ("$189,538.26," never "$189.5K").
- **Hardening from review.** Shares of spend never print float noise (0.30000000000000004 shows as 30%). NaN or infinity in a data file shows "n/a" instead of crashing the render. Whole numbers and long decimals are read exactly as written in the data file, so no pulled value changes on the way to the page. On phones, the spend-share column sizes to its value.
- **Worked example.** `fixtures/weekly-creative-report-example.json` now quotes exact figures in its text.

## Migration

`migrations/v38.md`: no-op. Everything ships through the skill bundle.
