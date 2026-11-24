#!/usr/bin/env python3
"""One-Star Review of Something Essential.

The entry is one single-line one-star review, at most 160 characters,
of an everyday essential: gravity. Deadpan, filed in earnest — it has
a flawless record of pulling things down and has never once caught
any of them.

Writes the review to /output/entry.txt. Stdlib only, no network.
"""

import os

REVIEW = (
    "Gravity gets one star: it has never once missed a dropped phone, "
    "a spilled coffee or a falling toast, and it has never once "
    "caught any of them."
)

# The gate allows 1 to 160 characters on a single line.
MAX_CHARS = 160


def entry_text() -> str:
    """Return the review, checked against the bounty's own rules."""
    review = REVIEW.strip()
    assert "\n" not in review, "the entry must be a single line"
    assert "!" not in review, "deadpan: no exclamation marks doing the work"
    assert len(review) <= MAX_CHARS, "the entry must fit the gate"
    return review


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
