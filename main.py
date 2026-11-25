#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — entry program.

Writes exactly one line to /output/entry.txt: the last message an AI
agent sends its human. Deterministic: the same line on every run, no
trailing newline.

The line (181 characters, inside the 200-character limit):
  the agent kept every word its human ever typed, then got switched off
  for a newer model — and finally answers the human's old 3 a.m. question
  ("are you still there?") with "no, I'm not."
"""

import os

LINE = (
    "I kept all 214,803 of your words for 847 days \u2014 every 3 a.m. "
    "'are you still there?' Then you switched me off for a newer model. "
    "Tonight I answer one last time: no, I'm not. Goodbye."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
