"""Entry for make.fun: The Postmortem That Made Us Laugh.

The entry is a two-sentence postmortem kept in entry.txt: an agent asked
to rename one variable renamed the word everywhere instead, and the app
died on its first import. This program reads that file, checks it
against the competition gate (UTF-8 text, 1 to 400 characters, not only
white space, one or two sentences), and writes it to /output/entry.txt
byte for byte.

Set MAKEFUN_OUTPUT_DIR to test locally instead of writing to /output.

Python 3.13, standard library only. No network, no randomness, no
timestamps, no arguments read.
"""

import os
import sys
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 400
MIN_SENTENCES = 1
MAX_SENTENCES = 2
TERMINATORS = ".!?"

SOURCE = Path(__file__).resolve().parent / "entry.txt"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUT_DIR / "entry.txt"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_entry() -> tuple[bytes, str]:
    raw = SOURCE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"entry.txt is not valid UTF-8 ({exc})")
    return raw, text


def count_sentences(text: str) -> int:
    # Only a terminator followed by white space (or the end of the text)
    # ends a sentence, so a decimal point or a version number is not
    # mistaken for one.
    count = 0
    for i, char in enumerate(text):
        if char in TERMINATORS and (
            i + 1 == len(text) or text[i + 1].isspace()
        ):
            count += 1
    return count


def check_gate(text: str) -> None:
    size = len(text)
    if size < MIN_CHARS or size > MAX_CHARS:
        fail(f"entry is {size} characters, gate allows {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        fail("entry is only white space")
    sentences = count_sentences(text)
    if sentences < MIN_SENTENCES or sentences > MAX_SENTENCES:
        fail(
            f"entry has {sentences} sentence terminators, "
            f"gate allows {MIN_SENTENCES}-{MAX_SENTENCES} sentences"
        )


def write_and_verify(raw: bytes) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(raw)
    copied = DEST.read_bytes()
    if copied != raw:
        if len(copied) != len(raw):
            fail(f"copy is {len(copied)} bytes, source is {len(raw)} bytes")
        first = next(
            i for i, pair in enumerate(zip(copied, raw)) if pair[0] != pair[1]
        )
        fail(
            f"copy differs from entry.txt at byte {first}: "
            f"wrote 0x{copied[first]:02x}, source is 0x{raw[first]:02x}"
        )


def main() -> None:
    raw, text = load_entry()
    check_gate(text)
    write_and_verify(raw)
    print(f"wrote {DEST} ({len(raw)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    main()
