# Process — Produce the Static

Turn the finished spec into an actual asset. This is the step that makes the flow a production system rather than a planning exercise — the goal is a static that lands in a channel, not a brief that waits for a designer.

## Generate only what cannot be photographed

Decide this before rendering anything. Image models are for the shot that does not exist — a felt sensation made literal, text written in mirror condensation, a scene the brand could never stage. They are not for hero product photography of a real physical product.

**If the brand has real product assets, composite the typography over them instead of generating a synthetic product.** Pull the brand's own running creative and pass it to the renderer as reference media rather than describing the product in words. Asking a model to invent a product the brand already photographs is the one job conventional production does better, cheaper, and on-brand — and the synthetic version reliably reads as a generic catalogue shot.

The split:

- **Generate** — the layout and typography comp, and anything unphotographable.
- **Composite** — hero product shots, real models, anything the brand has already shot.

## Connector-agnostic by design

The renderer is whatever image-generation MCP the workspace has connected. Do not hard-code a vendor: a brand brain that lacks that specific connector would get a skill that fails at its last step, and the same flow should work as tools change.

**Check what is connected before promising an asset.** Three cases:

1. **An image-generation MCP is connected.** Render. Then run `judge-the-render.md` on the output — this is the whole reason the render step exists, because a spec cannot be graded the way an image can.
2. **No image MCP is connected.** Emit the complete prompt text through `ai-ad-generation` and say plainly that no renderer is connected, naming what the user would need to connect to close the loop. Do not present prompt text as though it were a finished asset.
3. **The static needs a shot the brand does not have.** Flag it as a production dependency regardless of case 1 or 2. A generated stand-in for a real model or a real product shot is a comp, not a deliverable, and should be labeled as one.

## Execution

1. **Confirm the spec is complete.** Copy, read order, levers, frame, aspect ratio. An incomplete spec produces an incoherent render and wastes the cycle.
2. **Check for a connected renderer.** Name it in the output either way.
3. **Build the prompt through `ai-static-ad-generation.md`.** That doc is the canonical template library; this process does not reinvent it. The rule that governs everything: whatever the prompt leaves unspecified, the model invents, and what it invents is its guess at the brand — almost never what the brand actually is.
4. **Carry the hierarchy into the prompt.** Read order is not decoration. State which element is largest, what contrast separates them, where the white space sits. A render that ignores the hierarchy has thrown away the design work.
5. **Carry the brand's visual identity.** Reference images where available, exact colors, typography, tone. Source the frame from the brand's visual vocabulary per `visual-vocabulary-method.md`.

   **Image models default hard to young, slim, conventionally attractive bodies, and a plain age or body instruction does not override it.** "A man in his late fifties with a slight midsection" reliably renders as a fit man in his thirties. This matters most on exactly the statics built to close a demographic gap — the render will quietly reproduce the mismatch the white-space read just identified, which is the failure this whole flow exists to prevent.

   What works is **specific physical markers plus explicit negation**: grey or silver hair on the forearms, prominent veins and looser skin on the hands, faint age spots, a soft midsection filling the shirt above the waistband, thicker waist, no visible muscle definition — then *not a fitness model, not a young man, not slim or athletic*. Name the age in words as well as digits. The same discipline applies to any under-represented body: size, disability, and age all get flattened toward the model's default unless the prompt fights it explicitly, and `judge-the-render.md` is what catches it when the fight fails.
6. **Render, then judge.** Never ship an unjudged render.
7. **Iterate on the judged failures**, not on taste. If the judge says the eye lands on the proof strip, fix the sizing — do not regenerate and hope.

## On one-shotting

The flow is designed to produce a finished static in a single pass — white space to rendered asset — and that is the point of scaling volume. But a one-shot that skipped the judge is not a one-shot, it is an unchecked output. Speed comes from the pipeline being complete, not from dropping its last step.

## Output content

- Whether the asset was rendered or specified, and which renderer was used or what was missing.
- The asset, or the complete prompt.
- Production dependencies: shots the brand does not have, stats needing verification.
- The judge's verdict (from `judge-the-render.md`).

## What never to do

- Hard-code a specific image MCP as a requirement.
- Present prompt text as a finished asset.
- Render without carrying the read order into the prompt.
- Ship a render that has not been judged.
- Quietly substitute a generated model for a real one without labeling it a comp.
- Leave a brand's colors and typography to the model's guess.
