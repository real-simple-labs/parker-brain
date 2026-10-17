# Process — Find Reference Ads

Pull a handful of relevant reference ads from the sources Parker can reach, evaluate them, and pick the single best one to adapt. The chosen reference then feeds into adapt-existing-script.

This is the default first step of any scriptwriting request.

The method describes three ad databases in Parker, not on the filesystem: the **internal favorites DB** (team-curated, highest trust), **Parker's favorites DB** (Parker's own codified patterns, high confidence), and the **global AI-tagged ads DB** (continuous capture across all brands Parker has read, broadest pool). Every ad is tagged across multiple AI tag dimensions — format, hook type, angle, persona, behavioral signal, awareness stage, brand type, emotional driver. No tool available to users reaches them today, so all three are out of reach. Search the sources the skill names instead, in its source order: the brand's own account scripts (`search_facebook_ads_semantic`), the competitor and inspo scripts already captured in the brand's brain, the niche's top organic library (`search_tiktok_videos`), then the public ad library (`search_competitor_facebook_ads`) and the team's swipe file (`search_swipe_file`). Name the source each candidate came from; never call it a favorites or global-DB pick (see `parker-system/system/parker-tools.md`).

## Required inputs

- The user's request — what kind of script do they want, what format, what angle, what audience.
- Brand context — ICP, persona, brand type (lifestyle vs problem/solution), category.
- Brand baseline — the brand's existing scripts, so the references can be filtered to ones that match the brand's structural patterns where possible.

## When to pick

- **Always run as the first scripting step** unless the user has explicitly asked for net-new or has provided their own reference script. This is the default.

## Execution

1. **Build the tag query.** Translate the user's request and brand context into AI tag filters. Examples of dimensions to filter on:
   - Format (UGC, VSL, talking head, demo, listicle, podcast clip, founder note).
   - Hook type (comment response, investment, scam, POV, demographic, controversy, question, etc.).
   - Angle (the messaging angle — convenience, status, relief, identity, etc.).
   - Awareness stage (unaware, problem-aware, solution-aware, product-aware, most-aware).
   - Brand type (lifestyle vs problem/solution).
   - Persona or behavioral signal.
   - Emotional driver.

2. **Query Parker.** Run the tag-formatted query through the searches above and stop when their results together give enough strong matches. Typically the strongest references match on 3-5 tag dimensions, not all of them.

3. **Surface 3-5 candidates.** Of the matches, present the top few that:
   - Match the brand's audience and identity, not just the tags.
   - Have strong performance signal if available.
   - Match the brand baseline's pacing and length norms where possible.

4. **Pick the single best candidate.** Compare the candidates on:
   - Audience/identity match with the brand.
   - Performance signal strength.
   - Pacing and length alignment with the brand baseline.
   - Compliance fit — does the brand have a credible substitute for every claim and proof type in this reference?
   - Hook framework fit with what the brand's audience responds to.

   Pick one. Explain why this reference is the strongest choice over the others.

5. **Surface the chosen reference with full context for the adaptation step.** Provide:
   - The full script transcript with timing per beat.
   - The AI tags applied.
   - Performance signal if available.
   - The brand or category the reference came from (without exposing competitor confidentiality).
   - The rationale for picking this reference over the other candidates.

## Output content

- The 3-5 candidates considered, each with a one-line summary.
- The chosen reference with full transcript, tags, performance, and source category.
- The rationale for picking this one — what made it the best fit.
- Any compliance flags Parker should be aware of when adapting.

## What never to do

- Surface references that do not match the brand's category or audience.
- Pick a reference without comparing it against the other candidates. The pick has to be defensible.
- Skip the performance signal when it is available.
- Surface references in a vacuum. Always tie back to the user's request and what the chosen reference contributes.
- Replace this process with a competitor analysis. This is finding adaptation source material, not benchmarking competitors.
- Hand multiple references to the adaptation step. Pick one. Adaptation is 1:1.
