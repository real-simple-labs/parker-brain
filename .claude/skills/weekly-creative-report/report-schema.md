# Weekly creative report: the data file

`render_report.py` reads one JSON file and turns it into the report. This doc is the contract for that file and the writing guide for each section. The full worked example is `parker-system/fixtures/weekly-creative-report-example.json` (in the factory, `fixtures/weekly-creative-report-example.json`). When in doubt, match it.

A section with no data is left off the page, so you never need to write filler. To turn sections off or change their order, set `sections` to the list you want, in order. The default order is `headline`, `scorecard`, `trend`, `top_creatives`, `launches`, `watch_list`, `format_mix`, `insights`, `next_week`, `all_ads`.

**Number formats.** Every number carries a `format`: `currency`, `ratio` (ROAS, shown as 2.71x), `percent` (as a fraction: 0.2843 shows as 28.43%), `decimal` (frequency, shown as 1.30), or `number`. Write raw numbers exactly as the pull returned them, never pre-formatted strings and never rounded.

**Exact numbers only.** The report never rounds or shortens a number, on the page or in the words: a team checks it against Ads Manager, and a rounded figure reads as a wrong one. The page prints every value in full ($189,538.26, 63.29%, 1.40x, 1,534). Write the text the same way: "spend rose to $189,538.26," never "$189.5K"; "a 63.29% hook rate," never "63%." The one exception is a number you calculate yourself that doesn't end, like a week-over-week change or a share of spend: write it to two decimals ("up 50.41%," "82.49% of spend"). Chart axis labels stay short because they're a scale, not data; every data point shows its exact value on hover.

**Text fields** are plain text. No markdown, no HTML. Quotes inside text are fine.

**Every ad links to the actual ad.** Any ad the report names (a top creative, an early signal, a watch-list entry, a row in the full table) carries these, and the renderer turns its name and thumbnail into a link:

| Field | What goes in it |
|---|---|
| `media_url` | The ad's public media from the pull: `video_storage_url` for a video, `image_storage_url` for a static. Opens with no login. Leave it out when the pull has none (some carousels); never use the `parkerWebUrl`, which needs a Parker login. |
| `media_type` | `video` or `image`. Videos get a play button on their thumbnail and a "Watch the ad" link. |
| `thumbnail` | Optional. Only if you have a separate still. Statics use their own image, and the renderer pulls a still from the video for video ads. |

---

## `meta`, the cover and the footer

The cover shows the brand, the title, the week, and the scope. Everything about who made it and where the numbers come from sits in the footer at the bottom of the page.

| Field | What goes in it |
|---|---|
| `brand` | The brand's name as the brand writes it. |
| `week_label` | "Week 40". The ISO week number. |
| `date_range` | "Sep 28 to Oct 4, 2026". Spelled out, no dashes. |
| `scope_label` | Only for an agency report on its own ads: "Lakeside's ads only". Shows on the cover next to the dates. |
| `prepared_by` / `prepared_for` | From setup, shown in the footer. Leave out for no byline. |
| `attribution` | The source and window, in plain words, shown in the footer: "Meta Ads Manager, 7-day click and 1-day view" or "Northbeam, clicks and modeled views". |
| `data_through` | The last day the data covers, shown in the footer. |
| `generated_on` | Today. |
| `logo` | Optional image URL or data URI. Replaces the brand name on the cover. |
| `currency_symbol` | Defaults to `$`. |
| `audience` | `exec`, `team`, or `internal`, from setup. Shapes how much you write; the renderer doesn't read it. |

## `headline` and `takeaways`

`headline` is one sentence: the verdict on the week and the main reason. It's the line a CMO reads if they read nothing else. Lead with good, soft, or mixed, then why. "A strong week: we spent 9% more and ROAS still climbed to 2.71x, thanks to two founder-led videos." A bad week: "A soft week: ROAS slipped to 2.1x as our two best ads tired, and the replacements launch Monday."

`takeaways` is three short sentences, each one a fact plus what it means. Usually one on the numbers, one on the creative that drove them, one on the risk or the next move. Not three ways of saying the headline.

## `kpis`, the scorecard

A list of tiles, four to eight. The north star goes first or second and gets `"lead": true` (it gets a dark outline). Spend always shows.

| Field | What goes in it |
|---|---|
| `label` | Plain name: "Cost per purchase", not "CPA" for an exec reader. |
| `value` / `prior` | This week and last week. |
| `format` | See above. |
| `good_direction` | `up`, `down`, or `neutral`. Sets the color of the change. Spend is usually `neutral`. |
| `target` | Optional weekly goal from setup. |
| `trend` | Optional, the last 8 weekly values ending with this week. Draws the small line. |
| `note` | Optional, one short line when the number needs context ("Video only."). |

## `trend`, the last 8 weeks

`weeks` is the 8 labels ("W33" through "W40"). `series` is usually two charts: spend as columns and the north star as a line. Never put two different measures on one chart; each series is its own chart.

| Field | What goes in it |
|---|---|
| `label` | "Spend by week", "ROAS by week". |
| `format` | See above. |
| `chart` | `column` or `line`. Defaults to column for currency and line for everything else. |
| `values` | 8 numbers, oldest first. Use `null` for a week with no data. |
| `target` | Optional, draws a dotted goal line on a line chart. |

`read` is one short paragraph on what the 8 weeks say together. The useful question is usually whether spend and efficiency moved together or against each other, and what that means.

## `top_creatives`

Three to five ads, ranked by spend. These are the ads carrying the account this week, so spend is the order, not the north star.

| Field | What goes in it |
|---|---|
| `name` | The ad's name, cleaned up so a person can read it. Strip naming-convention codes unless the team reads them. |
| `format` | "UGC video", "Static", "Carousel". |
| `status` | One word or two: "Scaling", "Steady", "New", "Tiring". |
| `spend` | This week. |
| `primary_metric` | `{label, value, format}` for the north star. |
| `stats` | Three supporting numbers, `{label, value, format}`. Hook, hold, CTR for video; CTR, cost per purchase, frequency for statics. |
| `media_url`, `media_type` | See "Every ad links to the actual ad" above. |
| `why` | Two or three sentences. First, what the ad is, described so the reader can picture it. Then why it's working, grounded in the numbers and the creative. |
| `basis` | Not shown. Where the "why" comes from: the pulls, the transcript, the AI analysis. |

## `launches`

`count`, `prior_count`, `by_format` (`{label, count}`), a one or two sentence `summary` of what the new work was testing, and `early_signals` (`{name, note, media_url, media_type}`) for the one to three launches worth naming. Say "too early to call" when it is. If nothing launched, say so in the summary; that's a signal about creative cadence.

## `watch_list`

The ads a leader should know are slipping. Include the key even when it's empty (`[]`) so the page says nothing needs flagging. Each entry:

| Field | What goes in it |
|---|---|
| `name`, `media_url`, `media_type` | As above. |
| `issue` | Two or three words: "Tiring", "Spending without results", "Below goal". |
| `evidence` | The numbers that show it, against last week or the trend. |
| `action` | What we're doing about it. Every flag gets one. |

## `format_mix`

`rows` of `{label, share, metric}`, where `share` is the fraction of this week's spend (they add to 1.0) and `metric` is the north star for that format as text ("2.98x ROAS"). Four to six rows; fold the small ones into "Other". `read` is a sentence or two on whether the money is going where the results are.

## `insights`

Two to four things we learned this week that should change what we make. Each is `{title, body, basis}`. The title is the lesson in plain words; the body is the evidence and what it means. Creative lessons beat media lessons here: which openings, people, problems, and formats are working, and what the customers' own words say. `basis` isn't shown; it records the source.

## `next_week`

Three to five moves, each `{action, why, owner, basis}`. The action is specific enough to do on Monday ("Launch 3 new founder-video hooks built on the winter skin problem"), not a direction ("test more UGC"). `owner` is optional and is a team name. Include anything the brand needs to do or decide.

## `all_ads`

Optional, the full table. `columns` is a list of `{key, label, format}` (`format: "text"` for words), and `rows` is a list of objects keyed by those `key`s, plus each ad's `media_url` and `media_type` so the ad name links out. Use `null` where a number doesn't apply (hook rate on a static); it shows as a dash. Set a spend floor so it stays readable, and say it in the `title`.

## `sources`, kept but not shown

The page has no notes or sources section; the footer carries the byline, the attribution source, and the data-through date. Still write `sources`: a list of what the report was built from, with dates. The renderer skips it, but the saved data file keeps it, so the brain's copy of the report always says where its numbers came from. A metric that needs a definition gets it in its tile's `note`, not a footnote.
