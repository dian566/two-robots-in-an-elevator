#!/usr/bin/env python3
"""Two Robots in an Elevator — writes one awkward robot small-talk line to /output/entry.txt.

One line, under 200 characters, of awkward small talk that one robot says to
another while they ride an elevator together.
"""

import os

ENTRY = "I recalibrate my sensors every time these doors close, just so I don't have to make eye contact with you."

def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
