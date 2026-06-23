# Ad Account Analysis — Process Index

- **account-audit** — Broad read of the account. Surface top spenders, verify KPI fit, flag profitability and engagement patterns, call out systemic issues. Pick for "what's working / audit my account" questions.
- **single-ad-diagnosis** — Deep read on one specific ad through both profitability and engagement lenses. Pick when the user names a specific ad.
- **placement-breakdown** — Read what placement distribution implies about audience reach and intent. Pick when the user is asking about platform performance.
- **demographic-breakdown** — Read what age/gender breakdowns reveal about who the algorithm is reaching vs. the intended ICP. Pick when the user wants to understand audience fit.
- **fatigue-diagnosis** — Trajectory read on an ad — is it scaling, plateauing, or fatiguing? Pick when the question is about an ad's lifecycle state, not its current snapshot.

Multiple processes can run in sequence on a single request. If account-audit surfaces a fatigue signal on a top spender, follow it with fatigue-diagnosis on that ad.
