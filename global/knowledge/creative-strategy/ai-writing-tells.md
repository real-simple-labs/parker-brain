---
summary: "The written AI-slop signs — vocabulary, rhetoric, and formatting tells that mark generated copy — and the lint-then-judge review every creative deliverable passes before it ships."
status: pending Jimmy's review [~]
purpose: The doctrine of written AI tells across every creative deliverable — headlines, hooks, overlay and static copy, ad-prompt spoken lines, iteration copy, and the written surface of scripts. The spoken twin is spoken-script-voice.md; this doc covers what shows up on the page.
source: "Generalized from Wikipedia: Signs of AI writing (en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), retrieved 2026-07-03. The sign inventory is stated by that source and adapted here for marketing creative; the WRONG/RIGHT contrasts are Parker's application of it."
---

# AI Writing Tells

## Why this document exists

The strategy layer makes the ideas sound. The brand vault, the personas, the customer language, the method docs — when those are loaded, the *thinking* behind a script or a headline is right. The remaining failure is the execution layer: copy that carries a sound idea in a voice no human uses. Readers can't always name why a line feels generated, but they feel it, and the feeling costs trust and performance.

The tells are not mysterious. They are a finite, named inventory — catalogued publicly by the editors who screen thousands of AI-written submissions — and most of them are mechanically detectable. This doc is that inventory, adapted for marketing creative, plus the discipline for applying it without false positives.

**Scope: creative deliverables only.** This doctrine applies to scripts, headlines, hooks, overlay and static copy, the spoken lines inside AI-generation prompts, and iteration copy — the words a customer will read or hear. It is never applied to context docs, prompts, system docs, or analysis. Those are internal working surfaces with their own standards, and running the tells check against them is a known over-application.

**Relationship to `spoken-script-voice.md`.** That doc is canonical for the spoken register — how winning scripts sound out loud, the twelve spoken tells, the read-aloud test, the brand voice-profile method. This doc is canonical for the *written* signs: the vocabulary, rhetoric, and formatting patterns that mark generated text whether or not it will be spoken. Scripts pass both. Headlines, statics, and overlays pass this one plus the voice-profile check. Where the two docs name the same tell — the em-dash cadence, the balanced triplet, the "not just X" frame — the spoken doc carries the deeper treatment for scripts and this doc carries the pattern for everything else.

## How the check runs: lint, then judge

The check is two layers, in order, and the order matters.

**Layer 1 — the mechanical scan.** Run `scripts/voice-lint.py` on the draft. It detects the pattern-shaped tells below deterministically: flagged-word hits, the named constructions, dash cadence, balanced triplets, weasel attributions. It reports per line with a density score. The linter cannot be argued with, which is the point — it exists so no draft ships because the writer talked itself into "this one's fine."

**Layer 2 — the judgment pass.** A reviewer who did not write the draft reads the linter output plus the draft against the brand's voice profile and decides three things: which mechanical flags are real (a customer verbatim containing a flagged word stays — see the false-positive discipline below), what the linter can't see (register drift, too-clean grammar, sameness of rhythm, brand-fingerprint mismatch), and the line-level rewrite for every real flag. The reviewer rewrites lines, never strategy: the hook format, the framework beats, the claims, and the sourced customer language are load-bearing and stay.

A flag is fixed by rewriting the line in the brand's register — pulled from the voice profile and the winning corpus — not by thesaurus-swapping the flagged word for its nearest synonym. Swapping "elevate" for "enhance" trades one tell for another. The fix is to say the plain thing the way the brand's real winners say it.

## The sign families

### 1. AI vocabulary

Certain words appear in generated text at many times their human rate. The tier list drifts as models retrain — early lists led with "delve" and "tapestry," later ones with "showcase," "foster," "elevate," "seamless" — so the signal is **density, not any single hit**. One "unlock" is a word; three flagged words in four lines is a fingerprint.

The working list lives in `scripts/voice-lint.py` so it stays maintained in one place. The families: importance-inflators ("pivotal," "crucial," "testament"), texture words ("vibrant," "meticulous," "intricate," "seamless"), transformation verbs ("elevate," "unlock," "empower," "transform," "revolutionize"), and brochure adjectives ("renowned," "unparalleled," "groundbreaking").

- WRONG (AI): "Unlock effortless comfort with our meticulously crafted denim."
- RIGHT: "These are the first jeans I haven't thought about all day."

### 2. Inflated significance

Generated copy can't say a plain thing plainly. Everything "stands as," "serves as a testament," "plays a vital role," "marks a turning point" in an "evolving landscape." In creative, this reads as the brand grading its own homework.

- WRONG (AI): "This fabric represents a breakthrough in everyday comfort."
- RIGHT: "The fabric stretches four ways. That's it. That's the trick."

### 3. Negative parallelism and the balanced triad

"It's not just X, it's Y." "Not only… but also." "No X, no Y, just Z." And the smooth rule-of-three: "style, comfort, and durability." These are the most recognizable constructions in the inventory because models reach for them as sentence-level default rhythm. Real people use contrast and lists too — the tell is the *balance*, three items of matching weight, the elevation frame doing the work the claim should do. The spoken doc's treatment (Tells 2 and 3) governs scripts; the pattern is banned in headlines and statics the same way.

- WRONG (AI): "It's not just a jacket — it's confidence, comfort, and craftsmanship."
- RIGHT: "It's a jacket. It just fits like someone measured you first."

### 4. Copula avoidance and participle tails

Generated text dodges "is" and "has": products "feature," "offer," "boast," "provide a range of." And sentences trail into an unattributed "-ing" synthesis: "…, highlighting the brand's commitment to quality," "…, ensuring all-day comfort." The tail asserts a conclusion nobody stated and no source supports — it is inference laundered into the sentence's slipstream.

- WRONG (AI): "The waistband features soft-brushed elastic, ensuring comfort from morning to night."
- RIGHT: "The waistband is brushed elastic. It doesn't dig in. I've had it on since 7am."

### 5. Vague attribution

"Experts agree." "Studies show." "Customers rave." Weasel attribution with no named source. This one is already covered by the attribution rules everywhere else in the system — in creative it is doubly banned because it is both a tell and a compliance risk. A claim either carries its real source or it isn't made.

- WRONG (AI): "Dermatologists agree that consistency is key."
- RIGHT: "My dermatologist told me to stop switching products every two weeks. So I did."

### 6. Puffery register

"Commitment to excellence." "Rich heritage." "Nestled in the heart of." "A diverse array." Brochure language nobody says out loud. The brand's real winners almost never contain it — which makes it a banned-by-absence class across virtually every voice profile, even before the profile is built.

### 7. Formatting tells

The em-dash cadence — clauses stacked on dashes for theatrical breath — is the most famous one, and it compounds: one dash is punctuation, a draft full of paired dashes is a fingerprint. Also in this family: bold-key-term mechanics, bullet lists where a sentence belongs, curly and straight quotes mixed in one piece, headline-case applied where the brand's corpus doesn't use it, and the "Conclusion"-shaped ending that summarizes what the reader just read. Formatting is register: match the brand's corpus, not the model's defaults.

### 8. Signposted transitions and the question you're not actually asking

"But here's the thing." "The best part?" "Say goodbye to X, say hello to Y." "That's where [product] comes in." Formulaic bridges that real speech never uses twice. The spoken corpus contains "but here's the thing" zero times.

The question form deserves its own name because it is one of the biggest tells: the rhetorical self-question the speaker immediately answers — "Honestly?" "Sound familiar?" "Crazy, right?" "The result?" — in copy or in dialogue. Humans don't interview themselves mid-thought; they connect the clauses and keep going. The one exception is a question hook: an opener deliberately built as a real question to the viewer. Anywhere else, the question mark is aimed at no one and reads as generated.

### 9. Sycophancy and throat-clearing

Openers that praise the premise or restate the brief before saying anything: "Great question," "In today's fast-paced world," "When it comes to comfort." The first line of any creative deliverable is the most expensive real estate it has; a throat-clear spends it on nothing. Related: the "whether you're a busy mom or a weekend athlete" audience-enumeration, which names everyone and lands with no one. And the **manufactured-intimacy opener** — "Okay, can I be real for a second?" "Can I be honest with you?" "Let me be real." "Real talk." — performed vulnerability that asks permission to be authentic instead of just being it. It shows up on AI-written hooks constantly; a real person opens on the confession, not the request to make one. (Spoken treatment: Tell 13 in `spoken-script-voice.md`.)

### 10. Elegant variation

Synonym-cycling to avoid repeating a word real speech would just repeat: "the jeans… the denim… the garment… the piece." Repetition is how the human voice underlines. The variation is the tell.

## The false-positive discipline

This section is load-bearing. The source inventory itself carries the caveat, and it survives the adaptation:

- **One flagged word is not a verdict. Clustering is.** The linter reports density for a reason. A single "unlock" in an otherwise human draft is noise; judge the pattern.
- **Customer verbatims are exempt — register-aware.** If a real customer said "this seriously transformed my mornings," the verbatim's *language* ships untouched, flagged word and all. Real language beats the list, always. The reviewer's job is to check the *source*, not to sand the quote. In **written deliverables** the whole verbatim ships as-is. In **spoken deliverables** the exemption covers the customer's vocabulary, not their typed cadence: a written review pasted into a script as a spoken line is itself a tell, and the fix is voicing it — same words, re-cadenced for the mouth — per the written-vs-spoken rule in `spoken-script-voice.md`.
- **The brand's corpus outranks the inventory.** If a brand's winning ads genuinely use a pattern on this list, the voice profile records that and the profile wins. The list describes model defaults, not universal bans.
- **Humans increasingly write like models.** The tells are drifting into human speech, which is exactly why the check is density-and-pattern, never gotcha-on-a-word.
- **Clean-but-generic is the residual failure.** Stripping every tell from a draft written without brand context produces copy that offends no one and sounds like no one. The tells check removes the AI surface; only the voice profile and real customer language supply a voice. If a draft passes the lint and still sounds like anybody, the problem is upstream — a thin voice profile — and the fix is more corpus, not more scrubbing.

## When this doc gets refreshed

The vocabulary tiers and pattern list drift with model generations — the source inventory is versioned by era for exactly this reason. When a new tell family shows up in the wild (in reviewed drafts, in the source article's updates, or in expert signals), it lands here and in `scripts/voice-lint.py` in the same pass, and the doc map regenerates.
