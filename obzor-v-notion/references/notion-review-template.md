# Notion Review Import Reference

## Fixed Notion targets

- Folder page: `Не для людей`
  - page id: `33cc565d-c21c-80db-b42a-eb88cc28a920`
- Instruction page: `Шаблон внесения обзора в БД`
  - page id: `33cc565d-c21c-81a8-9ecc-ed0816221a5a`
- Body template page: `Шаблон полного weekly-обзора`
  - page id: `33cc565d-c21c-8127-8249-eeccd264d697`
- Database: `📰 Обзоры`
  - database id: `33cc565d-c21c-8007-9467-c14fec3d65cd`
  - data source id: `33cc565d-c21c-806e-8eda-000bcc35cd35`

## Database properties

- Title property: `Обзор`
- Date property: `Дата`
- Status property: `Статус`
  - allowed values: `Новый`, `Занесено`, `Нужно обновить`
- Review type properties:
  - `Тип обзора`
  - `Тип`
  - allowed values: `Weekly Survey`, `Тематический обзор`
- File property: `Источник файла`
- Short summary property: `Короткий итог`
- Tags property: `Темы`
  - allowed values: `RIS`, `RSMA`, `PHY`, `6G`, `Antennas`, `THz/mmWave`, `Polar Codes`, `LDPC`, `ISAC`, `AI-RAN`, `Wireless Trends`

## Expected body shape

Use this structure for imported pages:

```md
## Кратко
- Период отбора: ...
- Формат: ...
- Ключевые темы: ...
- Что главное на этой неделе: ...

## Полная версия
### Survey: самые интересные новые материалы за ...
...
#### 1. ...
- Источник: ...
- Дата: ...
- Ссылка: ...
- Summary: ...
- Почему важно: ...

#### 3GPP / ETSI
- Что нового за окно обзора: ...
- Что исключено и почему: ...
- Что важно держать в фоне: ...

#### Что читать в первую очередь
- ...

#### Источники
- ...
```

## Type mapping

- `Survey_*.html` -> `Weekly Survey`
- any topical review file such as `RSMA_common_channel_precoding_08042026.html` -> `Тематический обзор`

## Operational notes

- Source directory for local files: `F:\work\Actual`
- Default behavior when no review name is passed: use the newest `*.html`
- After creating the page, fetch it again and check that `Темы` became a real multi-select value
- If the HTML contains broken mojibake, retry reading it as UTF-8 first and avoid legacy encodings unless the file clearly requires them
