# Parameter Template

Use this compact block when the user wants a repeatable digest format or when an automation prompt should pass explicit inputs.

```text
keywords: RSMA; 6G; PHY
count: 7
period: last 14 days
scope: papers only | papers + standards
language: original source language
```

Interpretation notes:

- `keywords`: split on commas or semicolons; preserve quoted phrases.
- `count`: treat as target maximum, not a guarantee if strong results are scarce.
- `period`: support relative windows and absolute start dates.
- `scope`: default to `papers only` unless the query clearly asks for standards, specs, RFCs, or technical reports.
- `language`: keep source titles as published; summaries may follow the user's language.
