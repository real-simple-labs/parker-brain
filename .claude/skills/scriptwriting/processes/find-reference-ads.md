# Process — Find Reference Ads

Pull a handful of relevant reference ads from Parker's ad databases, evaluate them, and pick the single best one to adapt. The chosen reference then feeds into adapt-existing-script.

This is the default first step of any scriptwriting request.

The ad databases live in Parker, not on the filesystem. Three tiers are queryable: the **internal favorites DB** (team-curated, highest trust), **Parker's favorites DB** (Parker's own codified patterns, high confidence), and the **global AI-tagged ads DB** (continuous capture across all brands Parker has read, broadest pool). Every ad is tagged across multiple AI tag dimensions — format, hook type, angle, persona, behavioral signal, awareness stage, brand type, emotional driver. Access is through `ask_parker_agent` (Parker's ask-Parker MCP endpoint) with the active brand_id and a tag-formatted query. Through it, search in tier order: internal favorites first, then Parker favorites, then the global tagged DB if more breadth is needed. A brain's MCP doesn't carry that tool, so in Claude Code the three databases are out of reach. Fall back to the corpora the brain can search, `search_facebook_ads_semantic` (the brand's own ads), `search_competitor_facebook_ads` (the public ad library) and `search_swipe_file` (what the team saved), with no tier order, and name the corpus each candidate came from; never call it a favorites or global-DB pick (see "Chat-only tools" in `parker-system/system/parker-tools.md`).

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

2. **Query Parker.** Where `ask_parker_agent` is connected, run the tag-formatted query through it against each tier in order — internal favorites, Parker favorites, global AI-tagged DB — and stop at the first tier that returns enough strong matches. In Claude Code, run the fallback searches above instead and stop when their results together give enough strong matches. Typically the strongest references match on 3-5 tag dimensions, not all of them.

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
