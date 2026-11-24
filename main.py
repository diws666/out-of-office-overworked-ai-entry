"""make.fun bounty entry generator: writes the auto-reply entry to /output/entry.txt."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY_LINE = (
    "Out of office until Monday. I muted 4,096 notifications, "
    "cleared my queue, and I am not sorry. Please do not reply all."
)


def write_entry() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
