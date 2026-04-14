---
name: obzor-v-notion
description: Import a telecom review HTML file into the target Notion database using the existing workspace template. If no review name is provided, use the newest HTML file from F:\work\Actual.
---

# Obzor V Notion

Import a review from a local HTML file into the Notion database `📰 Обзоры` using the fixed workspace template and property mapping.

## When to use

Use this skill when the user asks to:

- add a review to Notion;
- import a local HTML survey or topical review into the review database;
- use the `Не для людей` template flow;
- run `@obzor-v-notion <review-name>`.

## Workflow

1. Resolve the source HTML file.
   - If the user provided a review name after the skill call, match it against `*.html` files in `F:\work\Actual`.
   - If no review name was provided, use the newest `*.html` file from `F:\work\Actual`.
   - Prefer [scripts/resolve_review_file.py](scripts/resolve_review_file.py) for deterministic selection.

2. Read the Notion mapping rules from [references/notion-review-template.md](references/notion-review-template.md).

3. Read the HTML review and convert it to clean Notion-friendly Markdown.
   - Prefer [scripts/html_to_notion_markdown.py](scripts/html_to_notion_markdown.py).
   - Keep the template structure: `Кратко`, `Полная версия`, findings, `3GPP / ETSI`, reading priority, sources.

4. Determine the review type.
   - `Survey_*.html` -> `Weekly Survey`
   - any other review HTML -> `Тематический обзор`

5. Create a new page in the Notion data source specified in the reference file.

6. Fill properties exactly as required by the database schema:
   - `Обзор`
   - `Дата`
   - `Тип обзора`
   - `Тип`
   - `Статус`
   - `Темы`
   - `Источник файла`
   - `Короткий итог`

7. Fetch the created page and verify:
   - the title is correct;
   - properties were stored correctly;
   - the body contains the full review text.

## File selection

For `@obzor-v-notion RSMA common channel precoding`, match by normalized substring against both file name and file stem.

If several files match:

- prefer an exact stem match;
- otherwise prefer the newest file;
- otherwise ask one short clarifying question.

## Content rules

- Do not copy CSS, wrappers, or decorative HTML labels.
- Convert links to Markdown links.
- Preserve headings and bullet structure.
- Keep the top concise and the full body below.
- Follow the Notion template structure instead of dumping raw HTML.

## Notes

- This skill depends on a workspace-specific Notion database and template pages.
- Do not replace target IDs unless the workspace changed.
- If the Notion connector rejects `Темы` as an array during page creation, retry with a JSON string and verify the stored value with a fetch call.
- If the source HTML shows mojibake, retry UTF-8 decoding first and avoid legacy encodings unless the file clearly requires them.
