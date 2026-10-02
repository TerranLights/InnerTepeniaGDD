#!/usr/bin/env python3
"""Compute the 3-of-3 coordinate-map verdict for Run 15.

Keyed on each map's internal "file" field, canonicalized against the filesystem,
so a reader that named its output differently (M-122) still joins the
intersection instead of dropping out of it silently (M-106).

Verdict is computed from the range data on disk, never from the receipt lines
(M-133).
"""
import json
import os
import pathlib
import sys
from collections import defaultdict

RUN = ("/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
       "Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/"
       "2026-09-03_Shirayuki_Run15_Cold/maps")
READERS = ["R1B", "R2", "R3"]

# reader -> canonical source path -> (n, {line: tag})
maps = defaultdict(dict)
problems = []

for reader in READERS:
    d = pathlib.Path(RUN) / reader
    if not d.is_dir():
        problems.append(f"{reader}: directory missing")
        continue
    for f in sorted(d.iterdir()):
        # A reader's own helper file lives here by contract 2026-09-03-b; it is
        # not a map. Skip anything that is not JSON rather than calling it a fault.
        if not f.is_file() or f.suffix == ".py":
            continue
        try:
            m = json.loads(f.read_text())
        except Exception as e:
            problems.append(f"{reader}/{f.name}: unparseable ({e})")
            continue
        src = os.path.realpath(m["file"])
        n = m["n"]
        # Collect every tag asserted for each line. A line may legitimately carry
        # more than one when the reader split it into character spans (a 6-element
        # range). Per M-101 / C.4 §6, a line whose spans disagree collapses
        # CONSERVATIVELY to WITHHELD at line grain.
        votes = defaultdict(list)
        for r in m["ranges"]:
            a, b, tag = r[0], r[1], r[2]
            spanned = len(r) > 4
            for ln in range(a, b + 1):
                votes[ln].append((tag, spanned))
        tags = {}
        for ln, vs in votes.items():
            distinct = {t for t, _ in vs}
            if len(distinct) == 1:
                tags[ln] = distinct.pop()
            else:
                tags[ln] = "W"  # mixed-content line, collapsed conservatively
                if not any(spanned for _, spanned in vs):
                    problems.append(
                        f"{reader}/{os.path.basename(src)}: line {ln} double-tagged "
                        "with NO char spans (true overlap)")
        missing = set(range(1, n + 1)) - set(votes)
        if missing:
            problems.append(f"{reader}/{os.path.basename(src)}: {len(missing)} uncovered lines")
        maps[reader][src] = (n, tags)

# Which sources did every reader assert on?
keysets = [set(maps[r]) for r in READERS if maps[r]]
common = set.intersection(*keysets) if keysets else set()
for r in READERS:
    extra = set(maps[r]) - common
    for e in extra:
        problems.append(f"{r}: asserted on {os.path.basename(e)} which is not in all 3")

print(f"sources asserted on by all {len(READERS)} readers: {len(common)}\n")
hdr = f"{'source':<46}{'n':>5}{'INERT':>7}{'content':>9}{'A 3-0':>7}{'W 3-0':>7}{'SPLIT':>7}{'adm%':>8}"
print(hdr)
print("-" * len(hdr))

tot = defaultdict(int)
rows = []
for src in sorted(common, key=lambda p: os.path.basename(p)):
    ns = {maps[r][src][0] for r in READERS}
    if len(ns) != 1:
        problems.append(f"{os.path.basename(src)}: readers disagree on n {ns}")
    n = max(ns)
    inert = a3 = w3 = split = 0
    for ln in range(1, n + 1):
        votes = [maps[r][src][1].get(ln) for r in READERS]
        if all(v == "I" for v in votes):
            inert += 1
        elif all(v == "A" for v in votes):
            a3 += 1
        elif all(v == "W" for v in votes):
            w3 += 1
        else:
            split += 1
    content = n - inert
    pct = (a3 / content * 100) if content else 0.0
    rows.append((os.path.basename(src), n, inert, content, a3, w3, split, pct))
    for k, v in (("n", n), ("inert", inert), ("content", content),
                 ("a3", a3), ("w3", w3), ("split", split)):
        tot[k] += v

for name, n, inert, content, a3, w3, split, pct in rows:
    print(f"{name[:45]:<46}{n:>5}{inert:>7}{content:>9}{a3:>7}{w3:>7}{split:>7}{pct:>7.1f}%")

tp = (tot["a3"] / tot["content"] * 100) if tot["content"] else 0
print("-" * len(hdr))
print(f"{'TOTAL':<46}{tot['n']:>5}{tot['inert']:>7}{tot['content']:>9}"
      f"{tot['a3']:>7}{tot['w3']:>7}{tot['split']:>7}{tp:>7.1f}%")
sr = (tot["split"] / tot["content"] * 100) if tot["content"] else 0
print(f"\nSPLIT rate (accepted as WITHHELD, per C.4 req 3): {sr:.1f}%")

print("\nPROBLEMS:" if problems else "\nPROBLEMS: none")
for p in problems:
    print(f"  - {p}")
sys.exit(0)
