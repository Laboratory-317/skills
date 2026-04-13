# research-digest-params

Параметризуемый skill для Codex, который готовит обзор свежих научных работ и технических материалов по заданным пользователем параметрам.

## Что умеет

- принимать ключевые слова или фразы;
- принимать желаемое количество работ в выдаче;
- принимать период обзора;
- отделять статьи от стандартов и технических документов, если это требуется запросом;
- отдавать краткий digest с приоритизацией и ссылками на источники.

## Какие параметры можно задавать

Минимальный набор:

```text
keywords: RIS; 6G; PHY
count: 5
period: last 14 days
```

Дополнительно можно указывать:

```text
scope: papers only | papers + standards
language: original source language
```

## Как установить

### Вариант 1. Установить вручную

Скопируйте содержимое репозитория в папку:

```text
C:\Users\<ваш_пользователь>\.codex\skills\research-digest-params
```

На PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills\research-digest-params" | Out-Null
Copy-Item -Recurse -Force ".\*" "$HOME\.codex\skills\research-digest-params"
```

После этого перезапустите сессию Codex, если skill не появился сразу.

### Вариант 2. Установить через git clone

```powershell
git clone <URL_репозитория> "$HOME\.codex\skills\research-digest-params"
```

## Как использовать

```text
@research-digest-params RIS, 5 работ, 26 год
```

## Состав репозитория

- `SKILL.md` — основная логика и правила работы skill;
- `agents/openai.yaml` — UI-метаданные skill;
- `references/parameter-template.md` — шаблон параметров для повторяемых запросов и автоматизаций.
