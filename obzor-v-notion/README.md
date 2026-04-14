# obzor-v-notion

Skill для Codex, который импортирует локальный HTML-обзор в рабочую базу Notion по фиксированному шаблону.

## Что делает

- выбирает HTML-файл обзора по имени или берет самый новый файл из `F:\work\Actual`;
- преобразует HTML в Markdown, пригодный для Notion;
- определяет тип обзора: `Weekly Survey` или `Тематический обзор`;
- создает страницу в базе `📰 Обзоры`;
- заполняет свойства страницы по фиксированной схеме и проверяет результат.

## Зависимости

- доступ к Notion workspace с целевой базой и шаблоном;
- локальные HTML-файлы обзоров в `F:\work\Actual`.

## Состав

- `SKILL.md` — основной сценарий работы;
- `agents/openai.yaml` — UI-метаданные skill;
- `references/notion-review-template.md` — привязка к базе, шаблону и свойствам;
- `scripts/resolve_review_file.py` — детерминированный выбор HTML-файла;
- `scripts/html_to_notion_markdown.py` — конвертация HTML в Markdown для Notion.
