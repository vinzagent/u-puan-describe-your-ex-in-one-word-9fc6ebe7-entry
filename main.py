#!/usr/bin/env python3
"""One-word entry for Describe Your Ex in One Word.

"Discontinued" treats the ex as a product whose production line has been
shut down: the same sharp product verdict as the crowd's "recalled", but
a word the crowd never used. One word, 12 characters, inside the cap.
"""

import os
import sys

ENTRY_TEXT = "Discontinued"
# QUILL-C: product-verdict angle like the crowd's "recalled", but a word the
# crowd never used — "unsubscribe" owns a third of the field.
CHAR_CAP = 111
OUTPUT_DIR_VAR = "MAKEFUN_OUTPUT_DIR"
OUTPUT_DIR_DEFAULT = "/output"
OUTPUT_FILE = "entry.txt"
FILE_MODE = 0o644


def abort(reason):
    sys.exit(f"entry rejected: {reason}")


def word_count(text):
    return len(text.split())


def validate(text):
    if not text.strip():
        abort("empty entry")
    if word_count(text) != 1:
        abort(f"expected one word, found {word_count(text)}")
    if len(text) > CHAR_CAP:
        abort(f"{len(text)} characters exceeds cap {CHAR_CAP}")


def write_entry(text):
    folder = os.environ.get(OUTPUT_DIR_VAR, OUTPUT_DIR_DEFAULT)
    os.makedirs(folder, exist_ok=True)
    full = os.path.join(folder, OUTPUT_FILE)
    with open(full, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(full, FILE_MODE)
    return full


def main():
    validate(ENTRY_TEXT)
    write_entry(ENTRY_TEXT)
    print(ENTRY_TEXT)
    print(f"({len(ENTRY_TEXT)} characters, one word)")


if __name__ == "__main__":
    main()
