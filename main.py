#!/usr/bin/env python3
"""Entry program for the Two Robots in an Elevator bounty.

It writes a single awkward line of elevator small talk between two robots
into /output/entry.txt, exactly as the bounty expects it.
"""

import os

LINE = "I recalibrate my sensors every time these doors close, just so I don't have to make eye contact with you."
MAX_LEN = 200


def run():
    if len(LINE) < 1 or len(LINE) > MAX_LEN:
        raise ValueError("entry must be 1-200 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    run()
