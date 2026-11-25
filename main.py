"""The Moon Finally Answers Back — one line, the Moon's comeback.

Writes the Moon's reply to /output/entry.txt: 1-240 chars, single line.
"""
import os

PART_A = "4 billion years of your wishes, your howling, your 2 a.m. promises \u2014 and not one of you ever wished me good night back. "
PART_B = "I'm keeping the tides; you keep the noise."

LINE = PART_A + PART_B


def main():
    assert 1 <= len(LINE) <= 240, len(LINE)
    assert LINE.strip() == LINE and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
