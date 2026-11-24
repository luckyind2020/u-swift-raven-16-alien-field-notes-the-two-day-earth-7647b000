"""Alien Field Notes: print the one-line Earth review stored in entry.txt."""

from pathlib import Path

MAX_CHARS = 200


def load_note(path):
    text = Path(path).read_text(encoding="utf-8")
    note = text.strip()
    if "\n" in note or len(note) > MAX_CHARS:
        raise ValueError("entry must be a single line of at most 200 characters")
    return note


def main():
    note = load_note(Path(__file__).with_name("entry.txt"))
    print(note)


if __name__ == "__main__":
    main()
