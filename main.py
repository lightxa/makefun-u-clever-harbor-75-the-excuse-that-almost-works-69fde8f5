#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the single line a gamer texts the boss to skip work during
GTA 6 launch week to /output/entry.txt.

The excuse: a boring, specific, almost believable workplace detail
(the engineer is coming Thursday to fix the line) fused with the one
counted GTA 6 detail that gives the game away (the download froze at
97%). Deadpan, hurried, no setup, no signature, no cliche excuse.
"""

import os

ENTRY = (
    "sorry boss, the engineer is coming thursday to fix my line "
    "and my GTA 6 download froze at 97%"
)

OUTPUT_PATH = "/output/entry.txt"
MAX_WORDS = 20
MAX_CHARS = 140


def validate(text: str) -> None:
    """Gate check mirroring the competition gate: 1-140 chars, <= 20 words."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 140 cap")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(f"entry is {len(words)} words, over the 20 cap")


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Validate the entry, then write it as one line of UTF-8 plain text."""
    validate(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    return ENTRY


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {len(written)} chars, {len(written.split())} words")
    print(written)
