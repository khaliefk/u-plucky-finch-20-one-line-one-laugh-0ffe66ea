#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (83 characters) to /output/entry.txt.
Standard library only; no network, no input.
"""

import os

LINE = "My GPS took me past my ex's house and whispered, 'Closure is only 400 metres away.'"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
