# Parker Brain

**A living, self-improving creative strategist for your brand that runs inside Claude Code.**

The Parker Brain is a structured repository of your brand's identity, your customer's actual language, your competitors, your ad account, your creative strategy, and the open questions you haven't answered yet — wired into Claude Code and connected to your live data through the **Parker MCP**. Instead of knowledge scattered across a dozen tools, you get one place that holds everything, connects the dots, and keeps getting better the more your team uses it.

It also keeps itself from going stale on its own schedule:

- **It dreams** — every day it reads your team's conversations against the brand and surfaces what it's noticing.
- **It harvests ideas** — every week it hunts inspiration across TikTok, competitor ads, Reddit, and your own reviews, and grades each find against your strategy.
- **It refreshes itself** — when a doc gets old, it flags it and re-runs the work to bring it current.
- **It self-improves** — it gets sharper the more your team uses it.

> The Parker Brain is not finished (and never will be) — we ship new knowledge, skills, and processes every week. It works today, and we'd love your feedback.

---

## You need a Parker account for this to work

This repo is the **brain's knowledge and methodology** — the prompts, skills, and craft layer. It comes alive only when it can reach **your brand's live data** (your ad account, customer reviews, competitor ads, surveys, organic social). That live reach is the **Parker MCP**, and the Parker MCP requires a Parker account.

**👉 Sign up at [heyparker.ai](https://heyparker.ai) — use code `PARKERBRAIN` for 1 month free.**

Without a connected Parker MCP (or equivalent data exports), the brain has the methodology but no live evidence to reason over — it can't audit an account it can't see.

---

## The two-repo model (read this first)

There are **two** repositories, and keeping them straight is the whole mental model:

1. **This repo (`parker-brain`)** — the read-only **factory**. It holds the prompts, skills, methodology, and craft layer. You clone it; you don't build inside it.
2. **Your brand brain** — a **separate, private repo** that Parker scaffolds *for your brand* during setup. This is the product you talk to every day; it learns your brand and grows over time.

When you run setup, Parker reads this factory and writes your brand's brain into its own new private repo. You can always pull improvements from the factory later. **Never commit brand data back into this repo.**

---

## Quickstart

The full, walk-you-through-it guide (with screenshots and a setup video) lives at **[heyparker.ai](https://heyparker.ai)**. The short version, in order:

**On the Parker web app first** ([heyparker.ai](https://heyparker.ai), code `PARKERBRAIN`):

1. Sign up and **connect your Meta ad account**. Parker spends the first few hours watching your creatives shot by shot, pulling performance data, and scraping ad comments.
2. **Upload customer reviews and post-purchase data** (CSV or direct integration — template in the dashboard).
3. **Fill out the Context Hub** — brand voice, products, personas, compliance notes. The more Parker knows, the better the outputs.
4. **Set up the Parker MCP** so Claude Code can reach your data.

**Then in Claude Code:**

5. Verify the connection:
   ```
   Verify that Parker MCP is properly set up for my brand [your brand]
   ```
6. Build your brain:
   ```
   Set up my brain for my brand [your brand] in a new private repo,
   follow the instructions here: https://github.com/real-simple-labs/parker-brain.git
   ```

Parker scaffolds your brand brain, then runs the foundation work in the background. A full build typically takes **2–4 hours** depending on how much data your brand has. What you get is a complete, worked example tailored to your brand — not an empty template.

📺 **Setup video:** https://drive.google.com/file/d/1zxs88XEx1-zdbHjO-DfNc70a3zuGYnuF/view

Want a hand? [Book a setup call or join our Slack](https://heyparker.ai).

---

## Make it your own

The goal of this repo is to hand you a strong foundation and then get out of your way. What's here is the starting point — the full creative-strategy knowledge, the prompts and skills, the system architecture, and the structure for a brand brain — assembled so you don't have to build any of it from scratch. **It's meant to be built on, not just run.**

- **Extend and customize freely.** Tune the prompts, add skills, adapt the methodology, reshape the structure to fit how your team actually works. The foundation is opinionated so it's useful on day one, not so it's fixed forever.
- **Build on top in your own brand repo, not in this one.** "Make it your own" happens in your brand's private repository, where the brain learns your brand and your team grows it over time. This clone stays the clean factory you can always pull improvements from.
- **The brain improves itself with you.** Connected tools, the refresh and self-improvement routines, and human feedback all feed back in — the more you use it and teach it, the better it gets.

---

## A note on the skills

**The skills are still under testing.** They ship as foundations — the full context and methodology so your team can stand these capabilities up and build on them — not as guaranteed-final products. **Scriptwriting in particular is actively being trained.** Treat skill output as a strong starting point a human should review.

---

## Repository layout

| Path | What's in it |
|---|---|
| `CLAUDE.md` | Parker's operating contract — how the brain reasons, retrieves, and attributes. |
| `prompts/` | Production prompts for context docs, audits, personas, voice-of-customer, market reads, and databases. `prompts/onboarding-runner.md` is the cold-start build sequence. |
| `skills/` | Runtime skill instructions (hooks, headlines, scriptwriting, ad-account analysis, and more). |
| `system/` | Methodology, retrieval, attribution, and the canonical tool inventory (`system/parker-tools.md`). |
| `global/knowledge/` | Generalized creative-strategy and performance knowledge. |
| `templates/` | Reusable document and brand-routine templates. |
| `self-improvement/` | The dreaming, refresh, and self-improvement methodology. |
| `release-notes/` | Versioned summary of brain changes. |

---

## License

This repository is source-available under the **[PolyForm Noncommercial License 1.0.0](./LICENSE.md)**. You may use, study, modify, and share it for **noncommercial** purposes. Commercial use requires a separate written license from the copyright holder — reach out via [heyparker.ai](https://heyparker.ai).

This is intentionally not an Apache/MIT/BSD release: the repo is shared publicly so teams can inspect and build on the Parker brain for noncommercial purposes while commercial rights stay reserved.
