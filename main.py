"""Write one debugging haiku to /output/entry.txt.

The bounty asks for a program that writes one text to /output/entry.txt:
three lines in the 5-7-5 syllable shape, at most 200 characters.
"""

import os

HAIKU = (
    "Three a.m. cursor\n"
    "on the line I swore was fine\u2014\n"
    "my name in git blame"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # The grader collects /output as another user: keep the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
