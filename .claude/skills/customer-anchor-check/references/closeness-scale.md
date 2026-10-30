# The closeness scale: tagging each line

Every non-functional line in the concept gets one of four tags. The tag comes from a pull, never from a feel. Keep the record or the count that earned it; it shows up in the full read if the user asks for it.

## The four tags

**Verbatim.** Customers say this, in close to these words. At least one record carries the load-bearing phrase or a near-exact form ("worth every penny" vs "worth every single penny"). One record makes it verbatim; three or more independent customers make it a pattern.

**Echo.** Customers say this idea, in different words. The meaning shows up in the data; the phrasing doesn't. The customer's own wording is the swap candidate. An echo line isn't wrong; the question is whether the customer's version does the job better.

**Composed.** No customer record says this, in these words or this idea. A marketer or creator wrote it. Most hooks built on a pattern interrupt, a visual, or a setup line land here, and that's fine. If nothing closer exists, it gets no swap.

**Off-customer.** The line leans on language the customer doesn't use, or actively pushes back on. Signs: zero or near-zero hits in a large corpus for the brand's own phrase, the phrase only appearing in hostile or mocking comments, or customers describing the same moment in clearly different terms. This is the tag most worth a swap, because the ad is saying something about the customer that the customer doesn't say about themselves.

**Functional** (not counted). CTA, offer, price, product mechanics, shipping, legal. Left out of the percentage, never tagged as a miss.

## How to test a line

1. **Find the load-bearing phrase.** The two to five words doing the work. In "My kids are impossible to shop for, so I got them this," it's "impossible to shop for," not "I got them this."
2. **Translate before you search.** Search the way a customer would say it, not the way the ad says it. Run the ad's phrase too: the gap between the two pulls is the finding.
3. **Two pulls per line, in parallel across lines.** One semantic pull on reviews (and comments where the line is objection- or reaction-shaped). One keyword count on the exact phrase plus one or two variants (`search_customer_reviews_sql`, `returnData=false`), so the tag rests on a number.
4. **Read the hits.** A keyword hit isn't a match until you've read it: "hard to shop for" inside "not hard to shop for at all" is a miss.
5. **Tag it.** Verbatim and Echo keep the record (quote, date, surface). Composed and Off-customer keep the count that came back ("0 of 4,200 reviews," "3 hits, all in comments mocking the phrase").

## How the percentage works

Verbatim lines count 1, Echo lines count 0.5, Composed and Off-customer lines count 0. Functional lines are left out. Add up, divide by the number of non-functional lines, round to a whole percentage. Six lines with three Verbatim and two Echo: (3 + 1) ÷ 6 = 67%.

The percentage measures how much of the wording already sounds like the customer. It isn't a performance prediction or a quality grade, and the sentence under it should never imply either. A composed hook over a verbatim body is often a strong build, and it'll score lower than a script that's verbatim end to end; that's fine.

## Budget

A 30-60 second script runs six to twelve lines. Test every hook and every non-functional body line; skip functional lines. For a concept with no script yet, test the hooks and the angle statement. If the user only wants the hook checked, test only the hook; the percentage is then the hook's alone, and the sentence under it says so.
