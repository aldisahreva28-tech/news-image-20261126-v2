#!/usr/bin/env python3
"""Entry program for the make.fun bounty news-image-20261126.

Copies the bundled front-page image ``entry.png`` (1024x1024, drawn with
Python Pillow) to ``$MAKEFUN_OUTPUT_DIR/entry.png``.  Standard library
only, no network.  The output bytes are exactly the bytes of ``entry.png``,
so two runs are byte-identical.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if target.read_bytes() != data:
        print("error: output does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
