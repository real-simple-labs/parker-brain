# Design the test — triangulate the full picture, don't build a study

The test is how the prediction gets settled. Two failure modes sit on either side of it, and the job is to land between them: a single pull that only sees one angle, and a six-step research study that over-engineers every angle. The right test is **a few complementary sources that together see the full picture** — each adding a *different* angle — and none of them over-built.

The promoted loop arrives with a validation approach the roll-up sketched. Sharpen it into the few pulls that decide; don't expand any one into a sub-study, and don't shrink it to a single source that can't see the whole thing.

## Triangulate — no one source sees the full picture

A real read usually needs a few angles, because each source answers a different part of "is this true, and is it a good opportunity":

- **The ad account** (`search_facebook_ads_sql`) — what the brand has actually run, and how it performed. The pattern's history.
- **Customer reviews and the brand's own corpus** (`search_customer_reviews_sql` / `search_customer_reviews_semantic`) — whether the demand is genuinely there, in the customer's own words and at real volume.
- **Competitors** (`search_competitor_facebook_ads`) — whether someone is already doing it and whether it works in market.
- **Post-purchase, organic, ad comments, a known web page** — as the specific question needs.

Pick the two, three, or four that each add a *different* angle on this prediction. The discipline is not "use one source"; it is "use the few that see the whole thing, and don't pile on a fifth that only repeats an angle you already have." Tools come from `parker-system/system/parker-tools.md`; Parker has no open-web search, so the competitor and open-web angles run through `search_competitor_facebook_ads` and known-URL fetches, not a search.

## The ad account is blind to what it has never tested

This is the trap that makes a single-source test wrong. The account can only tell you about what the brand has already run. If the prediction is about an *opportunity* the brand hasn't tested — a buyer it never named, an angle it never ran — the account literally cannot answer whether it is a good one; it has no data there. That is exactly when reviews and competitors carry the test: reviews show whether the demand exists for the untested thing, competitors show whether it works for someone else. A test that judges an opportunity off the account alone mistakes "never tested" for "no evidence," and misses real opportunity. Whenever the prediction reaches past what the brand has run, a demand source (reviews) and an in-market source (competitors) belong in the test.

## The cut is depth, not breadth

The thing to cut is over-engineering, not triangulation. Don't turn one source into a study — no confound-separations, no time-series-per-rung, no mechanism sub-cuts stacked on a single pull. Read each source at the depth that answers its angle, then stop. A test of three clean complementary pulls is sharp; a single pull split into eight analytical steps is the research-agenda failure the loop stage warns about.

## Size first when the loop is about an opportunity

If the prediction is about a market, segment, persona, or complaint worth acting on, the test checks it is big enough to matter before how to capture it — one sizing read, usually from reviews or the account, not a sub-study.

## Look for what would prove you wrong — in the same pulls

Across the few sources, read the evidence against the prediction as hard as the evidence for it: the named ad that came back expensive, the review demand that isn't actually there, the competitor who tried it and stopped. The disconfirming read rides the same pulls, not a separate study.

## Set the bar before you run

Name what would count as enough, in a line, across the sources: what convergence makes it validated, what split makes it inconclusive, what thinness makes it insufficient. Set it now so the validation step cannot move it to fit the finding.

## When the test cannot be built

If the only thing that would settle it is a real-world test Parker cannot run, or data the brand has never published, say so plainly — route to the user as brand-routed if brand data would unlock it. Do not fake a rigorous plan that closes nothing.
