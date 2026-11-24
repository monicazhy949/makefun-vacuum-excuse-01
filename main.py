#!/usr/bin/env python3
"""{e["title"]}.

Writes a single line of text to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'I did not miss that spot — I was respecting its privacy. It asked me not to come near it ever again.'
)
# Revision: v1 ended on a soft setup (giving it space) with no real punchline.
# Revised: added the payoff — the spot itself asked the vacuum never to come near it again.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
