#!/usr/bin/env python3
"""Set one status cell in the inspiration-research tracker.
usage: python3 inspiration_tracker_set.py <unit> <1|2> <☐|◐|✅> [note]
Only call this after checking the unit's file: every pick and FINAL ticked in its PROGRESS block (never from an agent's report alone)."""
import sys, re
T = "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Inspiration_Place_Research/_TRACKER.md"
unit, rnd, st = sys.argv[1], sys.argv[2], sys.argv[3]
note = sys.argv[4] if len(sys.argv) > 4 else None
L = open(T, encoding="utf-8").read().split("\n")
for i, l in enumerate(L):
    if l.startswith("| `%s` |" % unit):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        c[4 if rnd == "1" else 5] = st
        if note is not None:
            c[6] = note
        L[i] = "| " + " | ".join(c) + " |"
        open(T, "w", encoding="utf-8").write("\n".join(L))
        print(L[i]); break
else:
    sys.exit("unit not found: " + unit)
