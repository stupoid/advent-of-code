from __future__ import annotations

import argparse
import re
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Tuple

parser = argparse.ArgumentParser(description="Get Advent of Code puzzle.")
parser.add_argument("puzzle", nargs="+", help="enter path to puzzle. e.g. 2015/day/1")
args = parser.parse_args()

puzzle = args.puzzle[0]


if not re.fullmatch(r"20\d{2}\/day\/[1-9]\d?", puzzle):
    raise ValueError("Invalid puzzle argument format, use e.g. 2015/day/1")


class ArticleParser(HTMLParser):
    def __init__(self, *, target_tag: str = "article") -> None:
        super().__init__()
        self.target_tag = target_tag
        self.data: str = ""
        self.recording: bool = False
        self.list_numbering: int = 0
        self.tag_conversion = {
            "p": "\n",
            "b": "**",
            "strong": "**",
            "i": "*",
            "em": "*",
        }
        self.starttag_conversion = {
            "h1": "# ",
            "h2": "## ",
            "h3": "### ",
            "h4": "#### ",
            "h5": "##### ",
            "h6": "###### ",
        }

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str | None]]):
        if tag == self.target_tag:
            self.recording = True
        elif self.recording:
            if tag in self.starttag_conversion:
                self.data += self.starttag_conversion[tag]
            elif tag in self.tag_conversion:
                self.data += self.tag_conversion[tag]
            elif tag == "ol":
                self.list_numbering = 1
            elif tag == "li":
                if self.list_numbering > 0:
                    self.data += f"{self.list_numbering}. "
                    self.list_numbering += 1
                else:
                    self.data += f"- "

    def handle_endtag(self, tag: str):
        if tag == self.target_tag:
            self.recording = False
        elif self.recording:
            if tag in self.tag_conversion:
                self.data += self.tag_conversion[tag]
            elif tag == "ol":
                self.list_numbering = 0

    def handle_data(self, data: str):
        if self.recording:
            self.data += data


article_parser = ArticleParser()

p = Path(puzzle)
p.mkdir(parents=True, exist_ok=True)

with urllib.request.urlopen(f"https://adventofcode.com/{puzzle}") as res:
    article_parser.feed(res.read().decode("utf-8"))
    file = p / "puzzle.md"
    with file.open("w+") as puzzle_md:
        puzzle_md.write(article_parser.data)
        print(f"puzzle saved to ./{file}")

with urllib.request.urlopen(f"https://adventofcode.com/{puzzle}/input") as res:
    article_parser.feed(res.read().decode("utf-8"))
    file = p / "input.txt"
    with file.open("w+") as input_txt:
        input_txt.write(article_parser.data)
        print(f"puzzle input saved to ./{file}")
