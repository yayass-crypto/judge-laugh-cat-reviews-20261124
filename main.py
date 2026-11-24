#!/usr/bin/env python3
"""One-line entry for "Make the AI Judge Laugh: Cat Reviews Its Human".

Writes a single-line, one-star review written by a house cat about its
human to /output/entry.txt: 89 characters, one scene, one twist, with the
sting landing in the last few words.
"""

import os

ENTRY = "One star. He stares at his phone for hours, then calls ME the one who stares at walls."


def main():
    text = ENTRY.encode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert b"\n" not in text.rstrip(b"\n"), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"({len(text)} bytes)")


if __name__ == "__main__":
    main()
