#!/usr/bin/env python3
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re


class ReviewHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.href: str | None = None
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs = dict(attrs)
        if tag in {"style", "script", "head"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "h1":
            self.parts.append("\n# ")
        elif tag == "h2":
            self.parts.append("\n## ")
        elif tag == "h3":
            self.parts.append("\n### ")
        elif tag == "p":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "strong":
            self.parts.append("**")
        elif tag == "code":
            self.parts.append("`")
        elif tag == "a":
            self.href = attrs.get("href", "")
            self.parts.append("[")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"style", "script", "head"}:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag == "strong":
            self.parts.append("**")
        elif tag == "code":
            self.parts.append("`")
        elif tag == "a":
            self.parts.append(f"]({self.href or ''})")
            self.href = None
        elif tag in {"p", "ul", "ol", "section", "article", "div"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)


def convert_html(path: Path) -> str:
    parser = ReviewHtmlParser()
    parser.feed(path.read_text(encoding="utf-8"))
    text = "".join(parser.parts)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    return text.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html_file")
    args = parser.parse_args()
    print(convert_html(Path(args.html_file)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
