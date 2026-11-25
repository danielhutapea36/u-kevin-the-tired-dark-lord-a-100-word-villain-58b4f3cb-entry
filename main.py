#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — entry program.

Writes one 100-word monologue, spoken by a fantasy villain who is
secretly just very tired, to entry.txt.

The bounty gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 600 characters, not only white space. This program writes a fixed
string, so every run produces byte-identical output. No network, no
randomness, no clock reads, standard library only.
"""

import os
import sys

ENTRY = 'Come in. Mind the third step. Loose since the siege. Nine years I meant to fix it. Sit. Not the throne, that chair. It pinches.\n\nYou came to kill me. They all do. Tuesdays, mostly. Bring the sword down. Be quick. Ledgers due at dusk, goblins want boots, east wing leaks when it rains.\n\nI built an empire on fear, boy. Fear, and a filing system. Damp stone. Cold tea. A crown that no longer fits.\n\nStrike, or take a number. The queue for my death is longer than the one for my mercy, and both end at this desk.'

MIN_CHARS = 1
MAX_CHARS = 600


def main() -> int:
    if not (MIN_CHARS <= len(ENTRY) <= MAX_CHARS):
        print(
            f"entry is {len(ENTRY)} characters, outside the 1-600 gate",
            file=sys.stderr,
        )
        return 1
    if len(ENTRY.split()) != 100:
        print(
            f"entry is {len(ENTRY.split())} words, expected 100",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back what was written and verify it is exactly the entry:
    # a silent truncation or encoding slip must fail loudly, not ship.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("entry.txt does not match the entry after writing", file=sys.stderr)
        return 1
    if len(written.split()) != 100:
        print(
            f"entry.txt is {len(written.split())} words, expected 100",
            file=sys.stderr,
        )
        return 1
    if not (MIN_CHARS <= len(written) <= MAX_CHARS):
        print(
            f"entry.txt is {len(written)} characters, outside the 1-600 gate",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
