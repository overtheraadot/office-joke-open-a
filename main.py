"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
The angle: the office printer — the one machine in the office more
honest than the humans.
"""

import os

LINE = (
    "Our office printer only ever jams on documents marked urgent, "
    "which makes it the most honest performance review in the building."
)


def validate(line: str) -> str:
    """Enforce the gate: a single non-blank line of 1-200 characters."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
