"""A one-line museum placard for a stapler as an ancient artifact.

The program drops a single 133-character placard into
/output/entry.txt. Standard library only, no network access, no
secrets, and the same bytes come out on every run.
"""

import os

# Split across lines only for readability; the value is one line.
PLACARD = (
    "Stapler, bronze, c. 2140 BCE. Ritual binding tool of the "
    "Paperwork Cult; donor's note reads only: 'It jammed on the "
    "third sacrifice.'"
)

LIMIT = 180
ENDERS = (".", "!", "?")


def reject(message):
    """Abort the run with a plain-language reason."""
    raise SystemExit(message)


def check_shape(text):
    """Reject the placard if its shape breaks the bounty gate.

    Shape: not blank, a single line, within LIMIT characters, ending
    in sentence punctuation.
    """
    if not text:
        reject("placard is empty or only whitespace")
    if "\n" in text or "\r" in text:
        reject("placard must fit on one line")
    if len(text) > LIMIT:
        reject(f"placard is {len(text)} characters, over the {LIMIT} limit")
    core = text.rstrip("'\"")
    if not core or core[-1] not in ENDERS:
        reject("placard must end with sentence-ending punctuation")


def validate_placard(raw):
    """Run the bounty gate over the placard; return the cleaned text."""
    text = raw.strip()
    check_shape(text)
    return text


def main():
    placard = validate_placard(PLACARD)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(placard + "\n")


if __name__ == "__main__":
    main()
