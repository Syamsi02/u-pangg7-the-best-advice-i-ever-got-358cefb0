#!/usr/bin/env python3
"""The Best Advice I Ever Got.

Writes one original sentence of advice to /output/entry.txt and prints it.
Pure standard library, deterministic: the same sentence every run.
"""

import os

ADVICE = (
    "My father told me never to borrow trouble from tomorrow, because "
    "today is heavy enough already and tomorrow always arrives with its "
    "own hands to help carry it."
)


def main():
    # The gate allows 1 to 200 characters; keep the sentence inside it.
    assert 1 <= len(ADVICE) <= 200, len(ADVICE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ADVICE)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ADVICE)
    print(ADVICE)


if __name__ == "__main__":
    main()
