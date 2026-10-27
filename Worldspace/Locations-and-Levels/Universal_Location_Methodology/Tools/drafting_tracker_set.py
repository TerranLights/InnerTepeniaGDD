#!/usr/bin/env python3
"""usage: python3 drafting_tracker_set.py <key> <status> [note]   (status: ☐ ◐ ✅ ⚠). Sets one row in candidates/_DRAFTING_TRACKER.md.
python3 drafting_tracker_set.py --next   prints the key, spec path and input file of the first row that is not done."""
import sys
T = "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Real-World/Inspiration_Place_Research/candidates/_DRAFTING_TRACKER.md"
L = open(T, encoding="utf-8").read().split("\n")
def cells(l): return [x.strip() for x in l.strip().strip("|").split("|")]
if sys.argv[1] == "--next":
    for l in L:
        if l.startswith("| ") and l[2:3].isdigit():
            c = cells(l)
            if not (c[-1].startswith("✅") or c[-1].startswith("⏸") or c[-1].startswith("◐")):
                print(c[1].strip("`"), "|", c[2], "|", c[3].strip("`"), "|", c[4].strip("`")); break
    else: print("ALL DONE")
    sys.exit()
key, st = sys.argv[1], sys.argv[2]
note = sys.argv[3] if len(sys.argv) > 3 else ""
for i, l in enumerate(L):
    if l.startswith("| ") and l[2:3].isdigit():
        c = cells(l)
        if c[1].strip("`") == key:
            c[5] = (st + (" " + note if note else "")).strip()
            L[i] = "| " + " | ".join(c) + " |"
            open(T, "w", encoding="utf-8").write("\n".join(L)); print(L[i][:120]); break
else: sys.exit("key not found: " + key)
