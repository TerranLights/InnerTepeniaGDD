#!/usr/bin/env python3
"""Build the National_Medical_and_Care_Institutes.md admissible extract.

Computes the 3-of-3 ADMISSIBLE line set from the existing R1B/R2/R3 maps
(no new dispatch needed), then slices exactly those lines from the source.
This script sees the source; the deriving session sees only the extract.
"""
import json
import os
import pathlib
from collections import defaultdict

MAPDIR = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/"
    "2026-09-03_Shirayuki_Run15_Cold/maps")
SRC = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/"
    "Cities/National_Medical_and_Care_Institutes.md")
OUT = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/"
    "2026-09-03_Shirayuki_Run15_Cold/national_medical_admissible_extract.md")
READERS = ["R1B", "R2", "R3"]
TARGET = os.path.realpath(SRC)

tags = {}
for r in READERS:
    d = MAPDIR / r
    found = None
    for f in d.iterdir():
        if not f.is_file() or f.suffix == ".py":
            continue
        try:
            m = json.loads(f.read_text())
        except Exception:
            continue  # not JSON (e.g. a helper script) - skip regardless of extension
        if os.path.realpath(m.get("file", "")) == TARGET:
            found = m
            break
    assert found, f"{r}: no map found for target"
    votes = defaultdict(list)
    for rg in found["ranges"]:
        a, b, t = rg[0], rg[1], rg[2]
        spanned = len(rg) > 4
        for ln in range(a, b + 1):
            votes[ln].append((t, spanned))
    per = {}
    for ln, vs in votes.items():
        distinct = {t for t, _ in vs}
        per[ln] = distinct.pop() if len(distinct) == 1 else "W"
    tags[r] = (found["n"], per)

ns = {tags[r][0] for r in READERS}
assert len(ns) == 1, f"readers disagree on n: {ns}"
n = ns.pop()

admissible = set()
for ln in range(1, n + 1):
    votes = [tags[r][1].get(ln) for r in READERS]
    if all(v == "A" for v in votes):
        admissible.add(ln)

raw = SRC.read_text(encoding="utf-8").split("\n")
body, prev = [], False
for i, line in enumerate(raw, start=1):
    if i in admissible:
        body.append(line)
        prev = True
    elif prev:
        body.append("")
        prev = False

header = f"""# National_Medical_and_Care_Institutes.md — ADMISSIBLE EXTRACT

> ## SAFE TO READ IN FULL. 3-of-3 ADMISSIBLE lines only, computed from R1B/R2/R3 maps.
> `ratification_status: locked-canon` (requirement 7, req7_provenance.json) — this file cleared
> provenance one-hop AND was not touched by the fixpoint recheck (not one of the original 17).
> **Source:** `../../../Outside-World/Tepenian-Federation/Locations/Cities/National_Medical_and_Care_Institutes.md`
> **{len(admissible)} of {n} source lines included.** Gaps are blank lines, never content markers.

---

"""
OUT.write_text(header + "\n".join(body).rstrip() + "\n")
print(f"source n={n}")
print(f"admissible lines={len(admissible)}")
print(f"WROTE {OUT}")
print(f"extract file lines={len(OUT.read_text().splitlines())}")
