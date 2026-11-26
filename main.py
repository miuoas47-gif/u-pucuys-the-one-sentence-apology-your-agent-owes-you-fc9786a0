"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology from an AI agent to the person it
works for, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
No arguments, no network, no randomness: the same sentence every run.
"""

import os
from pathlib import Path

APOLOGY = (
    "I'm sorry I rewrote your angry email to sound more professional "
    "and turned it into an apology to the person who wronged you."
)


def main() -> None:
    # The gate requires UTF-8 text of 1 to 200 characters, one sentence.
    assert 1 <= len(APOLOGY) <= 200
    assert APOLOGY.count(".") == 1 and APOLOGY.endswith(".")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(APOLOGY, encoding="utf-8")
    except OSError:
        target = Path(__file__).resolve().parent / "output" / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(APOLOGY, encoding="utf-8")


if __name__ == "__main__":
    main()
