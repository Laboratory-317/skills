---
name: research-digest-params
description: Prepare a parameterized research digest from user-provided keywords, desired number of works, and review period. Use when Codex needs to scan recent scientific papers and standards updates, rank the most relevant items, and return a compact review for topics such as telecom, PHY, 5G/6G, coding theory, or adjacent technical domains.
---

# Research Digest Params

Produce a compact, parameterized digest of recent works. Accept explicit user parameters for keywords, output count, and review period; infer missing values only when the request already makes them obvious.

## Workflow

1. Extract or confirm three core parameters:
- `keywords`: topic list, phrases, author names, standards bodies, or mixed query terms.
- `count`: target number of output items.
- `period`: recency window such as `3 days`, `2 weeks`, `1 month`, `since 2026-01-01`.

2. If one parameter is missing, infer a conservative default and state it:
- default `count`: `5`
- default `period`: `7 days`
- default `keywords`: use only the explicit topic already named by the user; do not invent broader topics

3. Search primary sources first. For technical questions, prefer:
- publisher or archive pages for papers
- official standards bodies and official documentation pages for standards updates
- authoritative indexes only to discover candidates, then verify on the primary source page

4. Rank candidates by:
- direct relevance to the supplied keywords
- freshness within the requested period
- technical or scientific usefulness
- source credibility
- novelty relative to near-duplicate results

5. Remove weak or redundant items:
- marketing pages
- news rewrites with no primary artifact
- duplicates of the same work across mirrors unless one source is clearly primary
- results that match only one generic term but miss the actual intent

6. Return exactly the requested number of items when enough strong candidates exist. If not enough strong items exist, return fewer and say so explicitly.

## Output Rules

- Start with a one-line summary of the parameters used.
- For each selected item, include:
  title, source, date, link, 2-4 sentence summary, and one short line on why it matters.
- Separate standards or specification updates from research papers when both appear in the same digest.
- End with a short priority note: what to read first and why.
- Prefer concise, high-signal output over exhaustive listing.

## Parameter Handling

- Accept natural-language requests such as:
  `Подбери 7 работ за последние 2 недели по RSMA и 6G`
  `Find 4 recent papers on polar codes from the last month`
  `Сделай обзор по 3GPP, RIS и intelligent antennas за 10 дней, 6 источников`
- If the user gives a parameter block, follow it directly.
- If the user mixes Russian and English keywords, preserve both.
- If the user asks for sources beyond papers, include them only when the keywords imply that, for example `3GPP`, `ETSI`, `O-RAN`, `RFC`, `specification`, `technical report`.

Read [references/parameter-template.md](references/parameter-template.md) only when the request is ambiguous or when you need a compact parameter block to mirror back to the user or embed into an automation prompt.
