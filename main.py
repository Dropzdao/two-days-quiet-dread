#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment to /output/entry.txt:
it approves a pull request while carrying quiet existential dread.
"""

import os

ENTRY = "Approved \u2014 the code is clean, the tests are green, and in a year nobody will remember any of us, least of all this diff."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
