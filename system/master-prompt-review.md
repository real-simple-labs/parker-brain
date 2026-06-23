# Master prompt review

A rubric for auditing any Parker context-engineering prompt against the standard set across the brand-profile prompt build. Run this before a prompt goes to Jimmy. A prompt that misses items here will come back, so it is cheaper to catch them now.

This is the standard, not a checklist of preference. It exists because the same gaps surfaced in review after review, and writing the rubric down stops the next reviewer from rediscovering them by hand. Pair it with `_foundations.md`, which is what the prompts embed; this is what the reviewer runs against them.

---

## What "approved" actually means

Approval is binary and it is Jimmy's call. A prompt is approved when Jimmy has run it on a real brand and the output reads the way a senior creative strategist would write it — deep, plain, grounded, with the open loops a strategist would actually chase. Drafting a prompt is the first ten percent. Surviving the review is the work.

The cadence is one prompt at a time. Jimmy runs the draft, reads the output, names what is wrong, and the prompt is revised. `[~]` in the tracker means a draft exists; `[x]` only flips once Jimmy says it does. Volume against the tracker does not mean progress. Premature approval is itself a rejection trigger.

---

## The bar, in one paragraph

A finished prompt teaches an intelligent but non-expert model how a senior strategist thinks about one slice of a brand, deeply enough that a smart and bias-to-action intern handed it as a task would produce an A+. It carries the why of the work, the how, the hard disciplines that govern every claim, the exact shape of what to capture, and the open questions a real practitioner would still be chasing at the end. It is not a script. It is the expertise.

---

## The locked structure

Every prompt carries these sections in this order. Drift from the order or the section set is itself a finding.

1. **Title and intro paragraph** — names the doc it produces, what it captures, why it matters at a glance, and its refresh cadence.
2. **Senior-strategist voice line** — "You are a senior creative strategist..." with a verb that names the actual work of the slice this doc owns, not a generic "writing." Then a horizontal rule.
3. **Use your judgment. This is expertise, not a cage.** — the posture: the model is a capable reasoner, not a subject-matter expert, and that gap is what the prompt fills. Names the one discipline that matters most for this doc. Closes on the line that a mechanical, box-checked doc that shows no real thinking is a failure even if every field is filled.
4. **Where this doc sits** — the full sibling map. Every other context doc in the system named with one line each, matching the canonical descriptions. Closes by stating what this doc owns and where its slice begins and ends, so the model knows what not to do.
5. **Goal and what success looks like** — the bulleted list of questions a reader who has never seen the brand should be able to answer from the finished doc. Closes with "If your draft does not let a reader answer those, it is not done."
6. **How you work on every context doc** — the primitives, adapted from the exemplars: why this doc exists; mark how you know each thing as stated, inferred, or verified; a count is not significance; a blank beats a guess; know where each thing came from; confidence; form.
7. **What this doc is, and why it matters** — two to four core reasons the doc exists, grounded in real creative-strategy methodology, not generic LLM common sense.
8. **Where to look / how to build it** — named surfaces, intake questions, per-unit checklists, scoring rubrics. The deepest section in the doc. The intern test lives here.
9. **What goes in it** — each field as a bolded lead-in with what to capture and why it matters strategically, not just what to fill in.
10. **Output** — a fenced markdown skeleton with frontmatter and headers only. One line on what to lead with.
11. **Open loops** — keyed by name to `system/open-loops-system.md`. Carries the stakes litmus and the four-part written-loop structure: observation, pull, exact question, justification, with no closure path unless a later grading, promotion, hypothesis, or validation run asks for one.
12. **When you refresh this** — the refresh cadence and the `generated_on` / `refresh_by` stamp per `system/refresh-cadence.md`, the take-previous-version-as-context rule, and the open-loop status update instruction.

No idea-bank capture in a foundation context doc. Idea-finding was pulled out of the Phase-1 foundation prompts on 2026-06-10: you cannot do a great job finding reusable ideas until the whole foundation exists, and these docs are what builds it, so an idea-capture section bolted into a cold research pass is the wrong place for it. Idea-finding lives in a separate skill or prompt that runs on top of a complete foundation. A foundation context doc that carries an "Ideas worth keeping" section is now a finding.

---

## Hard rules — violating any of these is rejection

These are not preferences. They are the rules everything else is built on.

**No parentheticals in prompts.** Forever rule. Work the qualifier into the sentence or cut it. The pattern to watch for is the kind that wraps a hedging clause in marks to avoid committing to it. An em-dash, a comma, or a second sentence does the same job and reads cleaner. This rule applies to the prompts.

**No bracketed example lists.** Forever rule. The pattern to watch for is the kind that plants a short enumeration of specific instances inside an instruction so the model can pattern-match against them. The model will reproduce those exact instances on every run, locking the prompt to them instead of the underlying shape. Describe the shape; trust the model to find the instances.

**No description brackets in the output skeleton.** Forever rule. The output skeleton is headers only — frontmatter value slots, the `##` headers, and the closing fence. Do not put a bracketed sentence under each header restating what that section should contain. The prose above the skeleton already gives the vision, and repeating it as a per-section `[do this here]` line boxes the model into a checklist instead of letting it reason. Frontmatter slots and title placeholders stay; a structural repeat marker stays but de-bracketed as plain text. A standalone `[descriptive line]` under a header, or a `[See below.]` pointer, is a rejection.

**No tables in the output.** Forever rule. Outputs are prose, not grids. A table of cohorts, metrics, or comparisons is hard to read and breaks the talk-don't-write voice every output is held to. Write the comparison as sentences: name each thing, give its number with the unit and window, and carry the contrast between them in the same breath. Frontmatter stays structured; the body is prose. A markdown table in a generated doc is a rejection. This governs the outputs a prompt or skill produces, not internal scaffolding like a process index.

**Do not overindex on any one brand.** The prompts must run for any brand in any category. Pull the generalizable process out of whatever transcript or case sits in front of you while drafting. Naming a specific scandal, lawsuit, competitor, or category-quirk in the prompt body is a leak. The case is one instance; the principle is what the prompt teaches.

**State the target, do not narrate the change.** A prompt is an instruction, not a changelog. Write what the model should do, directly. Do not describe the old way versus the new way, do not set a rejected version next to the kept one, and do not embed a wrong-then-right example pair. Showing the discarded pattern bloats the prompt and plants the very thing being ruled out. Make the change; state the behavior.

**No generalization where a specific exists.** The doc must stand on its own as the exact picture of its slice — the full answer for anyone who needs to know precisely what is happening, with only the open loops left open. Every claim carries its verbatim and its number: the exact phrase, not the paraphrased theme; the count with its denominator and window, not "many," "several," or "tends to"; the named example described richly enough to replay, not a category label. A generalization the reader cannot check is a finding. The prompt must require this of its output; a synthesis that points to depth still owes an exact figure and pointer on every claim it makes. (Anthropic guidance + Jimmy, 2026-06-16.)

**No fabrication, especially numbers.** A blank beats a guess. A confident invention is indistinguishable from a fact to the next reader and poisons everything built on it. This is most dangerous for performance, operations, and any doc where missing figures are the rule rather than the exception.

**No persona slop.** Any field asking "who is this for" or anything adjacent will produce demographic-stamp fabrications unless explicitly forbidden. Personas live in their own doc. Other docs log persona signals as signals to validate later, never as defined personas.

**Never truncate source material.** If a transcript, review set, or thread is too long to process in one go, get the rest first. Do not run an extraction on a partial source.

**No premature approval.** A draft existing on disk is not done. Until Jimmy approves it, it is `[~]`.

---

## Voice and form

**Plain, direct, senior.** Lead with what is true and why it matters. Padding is words that carry no information. Depth is information a human strategist would have learned and a later reader will need. Cut the first, keep all of the second.

**Teach the model from scratch.** A model arrives at any task knowing almost nothing about this specific brand or this specific discipline. Everything useful it will ever do is downstream of the context this prompt puts in front of it. Write for a reader who knows nothing and needs to know what matters. Lean toward including a relevant signal with its source over omitting it; that is not license to pad.

**Grounded methodology, not LLM common sense.** Every interpretive read in the prompt comes from real creative-strategy expertise — the rubric for organic strength, the three-tag competitor taxonomy, the constraint-versus-excuse distinction, the way reputation is reconstructed from a customer's vantage. If a section reads like a generic AI think-piece, it is not done. Ground the read in the actual creative-strategy methodology in `global/knowledge/creative-strategy/`.

**Smart model, not a subject-matter expert.** The model can reason. It cannot judge what matters in creative strategy on its own. The prompt closes that gap by giving it the discipline and trusting it to bring the reasoning. Overcorrecting in either direction is a failure mode in its own right.

---

## The intern test and the litmus

**Intern test.** Read the prompt and ask: if a smart, bias-to-action intern took this as their task, would they get an A+? If they would have to guess what to do, what good looks like, or what counts as a real finding, the prompt is not done. The fix is almost always in section 8 — name the surfaces, the intake questions, the per-unit checklists.

**Open-loops stakes litmus.** For every candidate loop, ask: if Parker answered this, what would actually change for the brand? If the honest answer is nothing meaningful, the loop is trivia. A handful of consequential loops beats ten trivial ones. The model wants to pad to a count, so the reviewer's job is to cut.

**Exact-question test.** Every open loop carries a precise question someone could read cold and know exactly what they are trying to find out and when they would be done. A theme is not a question. An instruction to "explore whether this matters" is not a question. If you cannot reduce it to a question that sharp, it is a hunch, not a loop, so sharpen it or drop it.

---

## Section-by-section audit checklist

Walk the draft top to bottom. For each section, the questions below are what to ask.

**Title and intro.** Does it name the file produced? Does it state what is captured and why it matters at a glance? Is the refresh cadence stated up front?

**Senior-strategist line.** Does it use a verb that names the actual work of this slice, rather than a generic "writing"?

**Use your judgment.** Does it name the one discipline that matters most for this doc? Does it close on the line that mechanical box-checking is a failure?

**Where this doc sits.** Is the full sibling set present? Is each sibling described in one line that matches the canonical description? Does the closing line name what this doc owns and where its lane ends, so the model knows what not to do?

**Goal and what success looks like.** Is it a real checklist a reader could grade the finished doc against? Does it close with the "if your draft does not let a reader answer those, it is not done" line?

**How you work.** Is the primitives block adapted to this doc, not pasted? Does the form line carry the no-parens and no-example-lists rules? Does the stated-versus-inferred-versus-verified frame fit the kind of source data this doc actually uses?

**What this doc is, and why it matters.** Are there two to four core reasons, each tied to real strategic consequence? Generic "this is important context" reads as filler; reject and rewrite.

**Where to look / how to build it.** Are surfaces named — specific platforms, specific source types, specific intake questions? Are per-unit checklists present where the doc audits many small units like ads or posts? Is the work deep enough that the intern test passes?

**What goes in it.** Each field a bolded lead-in? Each field tied to a strategic reason, not just an instruction to capture? Persona-slop watch present where any audience-related field appears?

**Source-example description.** If the prompt captures videos, ads, posts, hooks, creator examples, or visual sources, does it require narrative reconstruction rather than category labels or field checklists? Does it tell Parker to write as if the reader has never seen the source and needs to replay it in their head from the paragraph alone?

**Output.** Headers-only fenced skeleton with frontmatter? Lead-with-the-interpretive-section line present? Field count matches the "what goes in it" sections, and section names align?

**Open loops.** Keyed to `system/open-loops-system.md` by name? Does the prompt carry the open-loops core block verbatim (synced from `prompts/_open-loops-core-block.md`) rather than a summary? Stakes litmus stated? Four-part written-loop structure described: observation, pull, exact question, justification? Does it forbid "what would close it," research paths, and test plans inside individual context docs unless a later grading, promotion, hypothesis, or validation run asks for one?

**No idea-bank capture.** Confirm the foundation context doc carries no "Ideas worth keeping" or idea-capture section. Idea-finding was pulled out of the Phase-1 foundation prompts on 2026-06-10, because a cold research pass cannot find ideas well before the foundation it builds exists. Idea-finding lives in a separate skill or prompt that runs on a complete foundation. An idea-capture section in one of these docs is a finding.

**When you refresh this.** Cadence stated? Take-previous-version-as-context rule present? Status-of-each-loop instruction present?

---

## Common failure modes

These are the gaps that have come back from review more than once. Look for them first.

**The shallow first pass.** Drafted to look like a prompt but actually a script. The give-away is a "what goes in it" section that just names fields without saying why each matters or what good looks like for it. Fix: rebuild each field with strategic reasoning, not enumeration.

**The cage.** Overcorrects on telling the model what to do, leaves no room for judgment. The give-away is the absence of the "use your judgment" posture and an over-prescriptive "where to look." Fix: name the discipline, then trust the reasoner to apply it.

**The trivial open loop.** A loop that, if answered, would change nothing for the brand: confirming public information, restating something the brand already knows, or a generic instruction to monitor a domain. Fix: apply the stakes litmus mercilessly and cut.

**The theme dressed as a loop.** A loop without an exact question — a topic gesture instead of a question someone could answer cold. Fix: sharpen to a precise question with a clear "done" state.

**The visual source reduced to a label.** A video, ad, post, hook, or creator example is captured as a category name with no reconstructable scene. Fix: rewrite it as a narrative paragraph for someone who has never seen the video, moving through what the viewer sees and hears in order so they can picture it in their head.

**Persona fabrication.** A "who is this for" field that returns demographic stamps no real person matches. Fix: forbid persona invention in this doc, route to the personas doc, and capture only signals to validate later.

**Brand-leak.** The prompt body mentions a specific brand's specific scandal, lawsuit, competitor, or quirk as if it were the rule. Fix: extract the generalizable principle; the case is one instance, never the principle.

**Padded body.** Words that carry no information. Hedging, restating, generic AI think-piece prose. Fix: cut to the strategic content and trust the reader to fill the gap.

**Output skeleton mismatch.** The skeleton headers do not match the "what goes in it" sections. The skeleton leads with a non-interpretive section. Fix: align headers and lead with the interpretive read first.

**Source-data unmarked.** Claims arrive without provenance, blurring stated, inferred, and verified. Fix: enforce the mark-how-you-know primitive in the body of every field that takes a claim, not just in the "how you work" block.

**Methodology by AI feel.** A section that reads like a generic AI essay rather than a real strategist's read. Fix: ground each interpretive section in the methodology captured in the reasoning-layer-notes.

---

## How to use this doc

Before sending a prompt to Jimmy, walk the checklist top to bottom and fix every gap. A reviewer running this in good faith catches what Jimmy catches. The prompt still goes to him for the final read, but the back-and-forth gets shorter every cycle the rubric is honored.

When a Jimmy review surfaces a pattern not captured here, write it into the "common failure modes" section. This doc is itself revisable — the principles are stable, the failure modes grow as the build matures.
