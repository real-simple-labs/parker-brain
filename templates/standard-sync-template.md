# Standard sync — the update ledger

> Status: `[~]` template. Seeded by the onboarding build when the method is mounted; owned by `/update-brain` from then on. This is the one file that says how this brain relates to the `parker-brain` factory: which release it runs, what posture it holds toward updates, and every offer the team has already answered. `/disconnect-factory` flips the posture; nothing else edits the header block.

## Where this brain stands

- **Factory remote:** {{FACTORY_REMOTE — the public parker-brain URL, or the team's own copy after a decoupling}}
- **Posture:** `follow` {{— or `own-factory` / `independent` after /disconnect-factory}}
- **Pinned release:** {{TAG — the vN tag parker-system/ is checked out at; matches parker_config.json's parker_brain_version}}
- **Migrations applied through:** {{TAG}}
- **Last compared:** {{DATE}} against {{NEWEST TAG SEEN}}

## Offer history

Append one line per offer, newest first: date — item — taken / declined (why, if given) / deferred. A declined item stays quiet until the factory version of that item moves again.

{{No offers yet — first /update-brain run fills this in.}}
