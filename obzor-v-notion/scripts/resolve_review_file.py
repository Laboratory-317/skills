#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def resolve_file(base_dir: Path, query: str | None) -> Path:
    files = sorted(base_dir.glob("*.html"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        raise FileNotFoundError(f"No HTML files found in {base_dir}")

    if not query:
        return files[0]

    candidate = Path(query)
    if candidate.exists():
        return candidate.resolve()

    query_norm = normalize(query)
    ranked: list[tuple[int, float, Path]] = []
    for path in files:
        stem_norm = normalize(path.stem)
        name_norm = normalize(path.name)
        score = 0
        if stem_norm == query_norm:
            score = 3
        elif query_norm in stem_norm:
            score = 2
        elif query_norm in name_norm:
            score = 1
        if score:
            ranked.append((score, path.stat().st_mtime, path))

    if not ranked:
        raise FileNotFoundError(f"No review HTML matched query: {query}")

    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return ranked[0][2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", default=None)
    parser.add_argument("--base-dir", default=r"F:\work\Actual")
    args = parser.parse_args()

    try:
        path = resolve_file(Path(args.base_dir), args.query)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
