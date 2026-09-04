#!/usr/bin/env python3
"""Build the Specs/Shirayuki.md admissible extract.

Ranges are the 3-of-3 ADMISSIBLE set from review §6b, MINUS the 7 lines
(215-216, 220-223, 225) demoted per §12a's ambiguous-citation finding.
This script sees the source; the deriving session sees only the extract.
"""
import pathlib

SRC = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/"
    "Cities/Specs/Shirayuki.md")
OUT = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/"
    "2026-09-03_Shirayuki_Run15_Cold/specs_admissible_extract.md")

# §6b's full admissible range string, MINUS 215-216, 220-223, 225 (§12a demotion)
RANGE_STR = ("3, 5-11, 17, 19-22, 24, 30, 32, 40-41, 45-47, 49, 53, 57-73, 75, 83, 85, "
             "91, 93, 97-98, 104, 106, 123-124, 126, 130, 134, 138-167, 172-175, "
             "178-186, 189-193, 196-200, 203-209")

def parse_ranges(s):
    lines = set()
    for tok in s.split(","):
        tok = tok.strip()
        if "-" in tok:
            a, b = tok.split("-")
            lines.update(range(int(a), int(b) + 1))
        else:
            lines.add(int(tok))
    return lines

admissible = parse_ranges(RANGE_STR)
raw = SRC.read_text(encoding="utf-8").split("\n")
n = len(raw) if raw[-1] != "" else len(raw) - 1  # wc -l convention

body = []
prev_included = False
for i, line in enumerate(raw, start=1):
    if i in admissible:
        body.append(line)
        prev_included = True
    elif prev_included:
        body.append("")  # mark a gap with one blank line, never a content marker
        prev_included = False

header = f"""# Specs/Shirayuki.md — ADMISSIBLE EXTRACT

> ## SAFE TO READ IN FULL. 3-of-3 ADMISSIBLE lines only (review §6b), minus the 7 lines
> demoted per §12a (ambiguous provenance citation, tail passage).
> **Source:** `../../../Outside-World/Tepenian-Federation/Locations/Cities/Specs/Shirayuki.md`
> **{len(admissible)} of {n} source lines included.** Gaps are blank lines, never content markers.

---

"""
OUT.write_text(header + "\n".join(body).rstrip() + "\n")
print(f"source n={n}")
print(f"admissible lines included={len(admissible)}")
print(f"WROTE {OUT}")
print(f"extract file lines={len(OUT.read_text().splitlines())}")
