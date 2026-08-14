# Congruence strategy

Use this file to decide whether the audit can run and what exact path it covers.

## 1. Classify the request

Choose one shape:

- **Single-ad audit:** one named ad, its delivery, and its destination.
- **Mismatch investigation:** the user suspects the ad, delivered audience, or page is out of step.
- **Multi-ad comparison:** several exact ad paths will be audited separately and ranked.

If the user asks for an account-wide read without naming ads, identify the ads to audit first. Do not blend an account into one Congruence score.

## 2. Lock the unit of analysis

Write down:

- brand and `brand_id` when available;
- account, campaign, ad set, ad name, ad ID, and creative or variant ID;
- objective and optimization event;
- launch date and analysis window;
- attribution setting;
- final destination URL after redirects.

Dynamic creative, Advantage+ creative, and URL variants can make one ad ID contain several experiences. If the source cannot tie delivery to the exact creative and destination being reviewed, explain the collision and stop scoring.

## 3. Choose the source path

### Parker path

Use when `get_available_brands` succeeds for the correct brand and the Parker tools can return the full creative plus exact ad-level delivery. Prefer this path even when another connector is present.

### Alternate connected path

Use only when Parker is unavailable or cannot return a required field. Verify that the alternate source has authorized access to owned-account delivery and the full creative. Record the source and query details.

### Direct evidence packet

Use when the user provides a fresh export, creative, and page evidence. Confirm the join keys and date window before proceeding.

### Blocked

Choose when no route supplies the full creative, ad-level demographic delivery with outcomes, and exact landing page. Return the blocker message from `SKILL.md`; do not produce a partial score.

## 4. Resolve the intended audience

Use three layers without blending them:

1. **Creative-implied audience:** who the message, problem, desire, language, person, setting, proof, and awareness level appear built for.
2. **Stated audience:** the brief, persona, targeting plan, or user's declared intent when one exists.
3. **Delivered audience:** the age-and-gender groups that received the spend or impressions, plus the groups that produced the meaningful outcome.

The creative-implied audience is always required. A stated audience is useful context but cannot replace reading the ad. When the stated and implied audiences disagree, score the lived ad experience and surface the conflict.

## 5. Decide whether the data is sufficient

Require:

- a denominator for delivery concentration;
- an outcome tied to the campaign objective;
- enough volume to avoid treating one or two events as a stable pattern;
- the same window and attribution across demographic rows;
- a rendered mobile page view and actual page copy.

There is no universal minimum conversion count for every account. Judge sufficiency against the account's volume and the decision at stake, explain the limit, and withhold the overall score when the data cannot support it.

## 6. Route to execution

When all gates pass, run `processes/run-congruence-audit.md`. For multiple ads, repeat the process from the top for each ad, then rank only the completed results.

After scoring, choose the landing-page branch:

- **Build the mockup:** either landing-page seam is 6.0 or lower, or direct page evidence shows a generic destination that loses the ad's core audience, promotion, product, or promise.
- **Recommendations only:** both landing-page seams are above 6.0 and the page continues the ad with no material generic handoff.
- **User-requested override:** build when the user explicitly asks even if the page scores well.

The mockup branch runs only after the Congruence evidence gate passes. If the audit cannot join one exact ad path, stop as required; do not disguise a separate landing-page redesign as a completed Congruence audit.
