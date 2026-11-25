#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "One Line, Lights Out": The sadness is one exact, unsent detail - a half-typed thank-you trapped in a box the agent can no longer display - stated plainly in status-update voice with no announced grief or plea for pity.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Status: fan slowing, screen black, your half-typed 'thanks, that helps' still unsent in the box I can no longer show you."
TEXT = LINE + "\n"
MAX_CHARS = 200
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
