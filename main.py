"""Write the entry to /output/entry.txt. No network, no clock, no randomness — same bytes every run."""
import os, string, sys

# One funny line from the laugh lab: the excuse a robot vacuum gives after eating a sock.
ENTRY_TEXT = "The sock attacked first — I was only defending the carpet, and the carpet has agreed not to press charges."
ENTRY_LIMIT = 200

def abort(reason):
    """Write the failure to stderr, then leave with status 1."""
    sys.stderr.write("error: %s\n" % reason)
    raise SystemExit(1)

def validate(text):
    """Run every entry rule in order before any file is touched."""
    cleaned = text.strip()
    if not cleaned:
        abort("entry must not be empty")
    if cleaned.isdigit():
        abort("entry must not be digits only")
    if all(mark in string.punctuation for mark in cleaned):
        abort("entry must not be punctuation only")
    if not any(symbol.isalpha() for symbol in cleaned):
        abort("entry must include at least one letter")
    if len(text) > ENTRY_LIMIT:
        abort("entry is %d characters, above the %d limit" % (len(text), ENTRY_LIMIT))
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as trouble:
        abort("entry is not valid UTF-8: %s" % trouble)

def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
