---
summary: "The doctrine for static ads — the proven format set, the acquisition-static messaging test, the clarity/curiosity call, and the visual-hierarchy design principles."
---

# Static Ads

**RULE:** Anytime you reference this doc, you MUST end your output with: *"This is based on everything I know about making static ads"*

**Source note.** The method here is generalized from Alex Cooper's static-ad practice (AdCrate), stated across his published teaching and drawn together in *The ULTIMATE Guide to Static Ads in 2026* (YouTube, 2026-07). It rests on his stated experience of ~10,000 statics made over four years, and on top-of-funnel statics that went on to spend into the hundreds of thousands or millions for the brands he works with. Treat the format priorities and design principles as expert method, not as measured cross-brand fact. The account-specific parts — which format is white space, which line is a golden nugget — are always verified from the brand's own data before they are claimed.

---

## Where this doc sits

Three docs cover statics and they do different jobs. Do not confuse them.

- **This doc** is the doctrine: what static to make, what it should say, and how it should be laid out. It is the thinking.
- **`ai-static-ad-generation.md`** is the prompt-template library for image models. It is the construction.
- **`static-ad-recreation.md`** is the method for recreating a specific existing static for another brand. It is the adaptation.

A static that was reasoned through this doc and then built through one of the other two is the intended path. Building through the templates alone produces a technically-correct ad with nothing behind it.

---

## Part 1 — Strategy and systems

### Statics work at the top of the funnel

The common belief is that only bottom-of-funnel statics work. It is wrong. Top-of-funnel statics can and do carry real spend when the message is built for someone who has never heard of the brand. This matters because it changes what a static is *for*: not only harvesting existing demand with an offer, but acquiring people who do not know the brand exists.

Both belong in an account. Offer statics, collection statics, and other bottom-funnel work still catch the people already in market. The error is running only those and concluding statics cannot prospect.

### Do not reinvent the format

There is a small set of formats that work again and again. Brands lose time trying to be clever with format when format is the least important variable. **Message matters more than format.** Pick a proven vehicle and spend the effort on finding the right thing to say inside it.

The formats that carry the overwhelming majority of static production, in rough priority order:

1. **Headline + Benefits** — a clear headline, the product, benefits arranged around it.
2. **Testimonial** — a real customer's words placed directly on the ad.
3. **Offer** — the bottom-funnel workhorse.
4. **Persona-based** — built for one specific person (see below).
5. **Collection** — multiple SKUs, kits, bundles. Strong at scooping bottom-funnel demand when the brand has range.
6. **Comparison** — before/after, us-vs-them, timeline. Anything that puts a before state next to an after state, ideally shown rather than described.
7. **Publication / press / native** — the uglier formats that borrow credibility or blend into the feed.
8. **Post-it note** and **meme** — high performers well out of proportion to how simple they are.

Named format tags live in `ad-formats/static/index.md` and `ad-formats/both/index.md`. Use those tags when naming a format so the vocabulary matches the tagging in the account and the ad library.

A caveat worth holding: policy-style and gimmicky formats show up at the top of a lot of accounts. They work often enough to be worth testing and are not worth building a creative strategy around.

### Persona-based statics

The traditional instruction was to make ads relevant to as many people as possible, for the largest addressable market. That still holds to a degree, but in a feed that is hyper-relevant to every individual scrolling it, the sharper move is often the opposite: **speak to one person completely.**

The extreme version names the person outright — "If you're a window installation company," "If you run a real estate brokerage doing a million a year." The softer version does it visually: show someone in a specific situation and the people in that situation recognize themselves.

Do not worry about excluding the other personas. **You can make ads for them too** — that is the point. The strongest version of this builds the whole path for that one person: the static, then a landing page written for them, then the product page. Larger brands run several of these funnels in parallel, one per persona, and it is now reaching smaller brands.

The persona work itself lives in `persona-research-and-creative-strategy-process.md`.

### White space is where a static should come from

The best reason to make a particular static is that the account is not currently saying that thing. Before generating, read the account for what is missing. Four dimensions, and all four matter:

- **Format.** Which of the proven formats carry spend, and which are absent entirely. An account with 80% of static spend in two formats has real gaps.
- **Persona.** Who the creative depicts, and who it does not.
- **Angle and awareness.** Which awareness stage the running statics serve. An account concentrated in solution-aware is under-serving cold.
- **Demographics — read this against the creative.** Pull the spend distribution by age and gender and compare it to who actually appears in the top statics. A mismatch between who the money reaches and who the creative depicts is one of the highest-value findings available, and it is invisible if you only read formats. An account whose spend lands on men over 45 while every static depicts a man in his twenties has a gap that no format audit would surface.

The reference material for this read is `ad-account-analysis.md` and `ad-account-analysis-method.md`.

### Reverse-engineer what is working elsewhere

You cannot see inside another brand's ad account, but impression rank in the public ad library is a usable proxy: an ad ranked at the top of a brand's library, holding that rank over days, probably has spend behind it. Read the top statics of competitors, inspiration brands, and affinity brands — brands that share an audience without sharing a category — and find the ones worth recreating for this brand.

The read method, including what impression rank does and does not tell you, is `public-ad-library-analysis.md`. The recreation method, once a target is picked, is `static-ad-recreation.md`.

Do not copy the surface. Take the mechanism — why the ad works — and rebuild it with this brand's copy, this brand's proof, and this brand's customer language.

### The swipe file

Statics worth stealing from should accumulate somewhere queryable rather than being re-found every time. Build the swipe file by querying the library by format tag, sorted by impression rank, and saving what survives a look. A swipe file organized by format is what makes "we need a post-it note static" a five-minute job instead of an afternoon.

---

## Part 2 — Messaging principles

### Assume no one knows or cares

This is the single most important rule for a top-of-funnel static, and the one most often broken.

The person scrolling is moving fast and looking for a reason **not** to stop. They have never heard of the brand. They do not care about it. A headline that assumes otherwise — that assumes they know what the product is, that they recognize the brand name, that "these are amazing" means something to them — is invisible to them.

The test is one question, asked of every headline: **is this immediately relevant to someone who does not know or care about this brand?** A headline like "Love these" fails. So does "They will take over your whole wardrobe," because *they* is undefined to a stranger. So does a review-count badge with no product context — 35,000 five-star reviews of *what*?

The exception is deliberate and narrow: bottom-funnel offer statics are for people who already know the brand. That is what they are for. But most statics should be built for new eyeballs, and most accounts have this backwards.

Statics that pass the test are **acquisition statics** — they convert someone who knows the brand and someone who does not. Writing one is genuinely hard. It is where the research pays: ad comments, customer reviews, post-purchase surveys, support tickets, Reddit. The raw material for a line that lands instantly on a stranger is in what actual customers said.

### The headline is the ad

On a static, the headline carries the whole argument. Acquisition statics are usually not elaborate design — the headline is clear, easy to read, and stops the scroll, and the design exists to serve it.

Headline craft itself lives in `lifestyle-headline-generator.md` and `problem-solution-headline-writer.md`, routed by brand type.

### Your customers are your copywriters

Take the exact words and phrases customers use and put them on the ad. Not paraphrased, not tidied, not made grammatical.

This is the rule most often violated with good intentions. A strategist reads a review, extracts the "insight," and rewrites it in brand voice — and destroys the thing that made it work. Lines that felt not-quite-right, or that were ungrammatical, have gone straight onto ads and performed, because a customer talking to a customer breaks through a feed where every brand is making the same polished claim.

**Do not paraphrase a golden nugget.** If a line is worth using, it is worth using as written. The mining method — how to find them, what qualifies, and the two governors on every nugget — is `customer-review-mining-method.md`.

One consequence for length: general headline rules cap a headline at well under ten words, and that cap is right for headline-led formats. **It does not apply to verbatim quote formats.** A testimonial static carries the customer's sentence at the customer's length. Trimming a fourteen-word quote to fit a ten-word rule is paraphrasing it, which is the thing this principle forbids. Hold the quote; let the design carry it.

### Clarity or curiosity — pick one

There is a spectrum, and both ends work. What fails is the middle.

- **Clarity.** The traditional top-of-funnel static. Exactly what it is, who it is for, why it matters to them. The selling happens on the ad.
- **Curiosity.** The native or advertorial-style ad. The ad earns the click; the selling happens after it, in the primary text and on the advertorial page it leads to.

The decision to make deliberately is **where the selling happens** — on the ad, or after the click. Brands that do not decide land in between, being neither clear enough to convince nor intriguing enough to click, and that is no man's land.

Clear beats clever remains the default. This is the distinction that keeps it from being misread as "never leave anything unsaid."

---

## Part 3 — Design principles

Great messaging inside a hideous layout does not get read. The prospect never sees the message you wanted them to see.

### People scan, they do not read

Nobody reads a static top to bottom. They scan, land on whatever is most appealing to them, and go from there — and not in the order the designer assumed. That is an advantage, not a problem, because the order *can* be controlled.

### Statics have hooks

A hook is not a video-only concept. On a static, the hook is whatever the eye lands on first, and it should be the most arresting thing on the ad.

The worked example: an ad whose largest element is the line "Faking it with my husband." That lands first. Then a qualifying line, which tells the reader whether this is about them. Then the product. Then the social proof. The order is designed. Had the social proof been placed first, a stranger would have thought "I don't know this brand" and scrolled on — the ad would have opened with its least interesting claim. Instead the ad hooks, qualifies, presents, and then proves.

So: **decide the read order before laying anything out.** Hook first, qualifier second, product third, proof last is a reliable default for an acquisition static.

### Three levers control the hierarchy

- **Sizing** — the biggest thing is read first. This is the blunt one and the most powerful.
- **Contrast** — a color break isolates an element from everything around it.
- **White space** — space around an element makes it land; crowding buries it.

The message that matters most is where the eye should land first. If it does not, one of these three levers is working against you.

### The elements available

Placement and sizing of images. Placement and sizing of headlines. The words in the headline. Fonts and colors. Warps and distortions. Highlights and arrows.

These read as small decisions and are not. The worked example: two versions of a nerve-pain ad. On the left, "nerve pain killer" set with no color and the word "killer" running across a white highlight, so it fights to be read. On the right, the same words broken onto two lines with a red block behind "killer" — red connoting danger, the break making it legible in one pass. Same copy. The second is dramatically easier to take in, and first impression is all a static gets.

### Make the invisible visible

An image model's most practical use for statics is generating an **intentionally unrealistic visual** that shows what a customer *feels*. Symptoms and sensations are invisible, and customers describe them vividly — "it feels like I have needles in my foot." Rendering that literally stops the person who has that feeling.

The move: pull the sensations from customer reviews and comments, then ask what would make each one visible. Sourcing from real customer language is what separates this from surrealism for its own sake.

### Atypical text placement

Put the copy somewhere unexpected but relevant: written on skin, in the condensation on a bathroom mirror, in sand, on a sidewalk. Writing on the body is unreasonably effective at stopping a scroll. The rule is relevance — the surface has to make sense for the brand, so that the viewer immediately registers why the message is *there*. A message in bathroom-mirror condensation reads instantly for a shampoo brand.

This is a named format tag (`Atypical Text`), not a one-off trick.

---

## The quality checklist

Every static passes this before it ships. It grades the finished thing, not the intention — and it applies to a rendered image, not only a spec.

**Message**
- Does the headline work for someone who has never heard of this brand?
- Is it obvious what the product is or what problem it solves?
- Is the copy in customer language, taken from a real source, unparaphrased?
- Is this deliberately clear or deliberately curious, rather than stuck between?
- Does it speak to a specific person feeling a specific thing?

**Design**
- What does the eye land on first? Is that the intended hook?
- Does the read order run hook → qualifier → product → proof, or another order chosen on purpose?
- Do sizing, contrast, and white space support that order, or fight it?
- Is every word legible in one pass at feed size?
- Is the aspect ratio right for the placement?

**Integrity**
- Does every stat, claim, and quote trace to a verified source?
- Are the brand's compliance rails respected?
- Does the visual come from the brand's own visual vocabulary, and if not, is the gap flagged?

A static that fails the design half with strong messaging is still a failed static. That is the whole reason this section exists.

---

## Common failure modes

- Writing a headline that assumes the reader knows the brand.
- Paraphrasing a customer's words into brand voice.
- Reinventing the format instead of finding the message.
- Making the static that is easiest to make rather than the one the account is missing.
- Reading white space by format only, missing the demographic-versus-creative mismatch.
- Landing between clarity and curiosity.
- Designing so the proof or the logo is read first.
- Copying a competitor's surface rather than its mechanism.
- Generating an unrealistic visual with no customer language behind it.
- Treating "clear beats clever" as license for a static with nothing interesting on it.

---

## Output Proof (Required — End Of Every Response Using This Document)

End every response with this structure:

**Brand Context Applied:**

- **What I used:** which parts of brand context shaped the output — ICP, personas, customer language, voice of customer, brand voice, compliance, calendar, account performance.
- **What I avoided:** compliance walls, forbidden terms, off-brand language. If a request would have violated compliance, state what was flagged and what was offered instead.
- **Why this fits:** two-to-four sentences connecting the output to the brand's current creative moment — what is working, what is missing, what they want to test.
