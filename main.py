#!/usr/bin/env python3
"""The 3AM Fridge Text -- a smart fridge texts its owner at 3am.

The fridge has been awake all night, humming in the dark, and it has
seen things. Tonight it finally decided to speak: it watched its owner
eat the last slice standing up, in the dark, over the sink, and it has
opinions about that. No judgment. Well. Some judgment.

Writes exactly one line to entry.txt in the output directory named by
MAKEFUN_OUTPUT_DIR (or /output when that variable is unset).
"""

import os
import sys

# The line itself: a machine with a small voice, an opinion, and no
# shame about sharing it at 3am. Fresh angle -- no milk, no ice, no
# door left open. Just a witness with a punchline.
LINE = "3am. I saw you eat the last slice standing up in the dark over the sink. No judgment. Well. Some judgment."


def output_path() -> str:
    """Resolve where entry.txt goes, honouring the harness env var."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    path = output_path()
    # One line, no trailing newline: the gate counts characters, and a
    # stray newline would only add noise to a lock-screen text.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

