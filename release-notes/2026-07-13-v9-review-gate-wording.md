# 2026-07-13 — v9: review gates read as a step the agent runs

## What shipped

The review-gate instructions in the five creative skills — `scriptwriting`, `hooks`, `headlines`, `iterations`, `ai-ad-generation` — were reworded so the two independent review agents read as a step the agent runs itself, not something that runs "automatically" or "on its own." The old passive wording led the model to treat spawning `context-grounding-review` and `creative-voice-review` as optional; the new wording makes it a first-person, mandatory step ("you run the two gates yourself, now"; "nothing spawns these agents for you").

The two-gate contract is shared across all five skills; the wording is skill-specific — the scriptwriting 7a/7b gate split and the iterations/ai-ad-generation visual-only voice-gate exception stay intact.

## Why

Jimmy reported the review agents almost never fired on scriptwriting work. Root cause was prompt wording, not the scripts: framed passively, the model treated the gates as optional.

## Migration

`migrations/v9.md` — bundle-only no-op; the pin bump's executable-layer re-sync delivers the five skills. No data transformation.
