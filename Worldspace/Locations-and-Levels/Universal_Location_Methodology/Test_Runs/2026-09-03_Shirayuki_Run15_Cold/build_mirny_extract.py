#!/usr/bin/env python3
"""Build the Mirny subnet split extract from three independent coordinate maps.

Prints STATISTICS ONLY. Never emits source content to stdout — the whole point
of C.1/C.2 is that no session reads the source (00_RUNBOOK.md §C.1).

A line enters the extract only on 3-0 ADMISSIBLE unanimity. Lines any reader
split into character spans with differing tags collapse conservatively to
WITHHELD at line grain (M-101).
"""
import hashlib
import json
import pathlib
import sys
from collections import Counter, defaultdict

RUN = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/"
    "2026-09-03_Shirayuki_Run15_Cold/cmr_maps")
SRC = pathlib.Path(
    "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
    "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/"
    "Cities/City_Master_Reference/Mirny_Subnet_Reference.md")
OUT = SRC.parent / "Split_Extracts" / "Mirny_Subnet_Reference_EXTRACT.md"
READERS = ["R1", "R2", "R3"]

tags = {}
problems = []
for r in READERS:
    p = RUN / f"{r}_Mirny_Subnet_Reference.json"
    m = json.loads(p.read_text())
    votes = defaultdict(list)
    for rg in m["ranges"]:
        a, b, t = rg[0], rg[1], rg[2]
        for ln in range(a, b + 1):
            votes[ln].append(t)
    per = {}
    for ln, vs in votes.items():
        d = set(vs)
        per[ln] = d.pop() if len(d) == 1 else "W"   # mixed span -> conservative
    missing = set(range(1, m["n"] + 1)) - set(votes)
    if missing:
        problems.append(f"{r}: {len(missing)} uncovered lines")
    tags[r] = per
    print(f"{r}: n={m['n']} ranges={len(m['ranges'])} tag-mix={dict(Counter(per.values()))}")

n = 344
verdict = {}
for ln in range(1, n + 1):
    vs = [tags[r].get(ln) for r in READERS]
    if all(v == "I" for v in vs):
        verdict[ln] = "INERT"
    elif all(v == "A" for v in vs):
        verdict[ln] = "ADMISSIBLE"
    elif all(v == "W" for v in vs):
        verdict[ln] = "WITHHELD"
    else:
        verdict[ln] = "SPLIT"

c = Counter(verdict.values())
content = n - c["INERT"]
adm_pct = c["ADMISSIBLE"] / content * 100 if content else 0
print(f"\nn={n} INERT={c['INERT']} content={content}")
print(f"ADMISSIBLE 3-0={c['ADMISSIBLE']} ({adm_pct:.1f}% of content) "
      f"WITHHELD 3-0={c['WITHHELD']} SPLIT={c['SPLIT']}")
print("PROBLEMS:", problems if problems else "none")

if problems:
    print("\nREFUSING TO WRITE — coverage incomplete.")
    sys.exit(1)

raw = SRC.read_bytes()
pin = hashlib.sha256(raw).hexdigest()[:16]
lines = raw.decode("utf-8").split("\n")

header = f"""# Mirny Subnet Reference — SPLIT EXTRACT

> ## ✅ SAFE FOR A COLD DERIVER TO READ IN FULL.
> **Attribute-tier lines only.** Built 2026-09-03 by three isolated readers plus this script,
> per `00_RUNBOOK.md` §C.1 / §C.2. ***No session read the source.***

**Source:** `../Mirny_Subnet_Reference.md` · **PIN** `sha256:{pin}` · `{n}` lines
**Readers:** R1 · R2 · R3, independent. **A line appears below only on 3-0 `ADMISSIBLE` unanimity.**
**Verdict:** {c['ADMISSIBLE']} admissible · {c['WITHHELD']} withheld · {c['SPLIT']} split (accepted as withheld) · {c['INERT']} inert.
**{adm_pct:.1f}% of content-bearing lines.**

> ### ⚠ THIS EXTRACT IS THIN BY RULE. **Do not read thinness as evidence the source is clean.**
> A line is dropped on any dissent, and on any mid-line seam. **Recover yield by working the escalation
> ladder on the seam lines — never by lowering the threshold** (`00_RUNBOOK.md` §C.2).

> ### ⚠ Standing tagging obligation (§C.1)
> **Division-of-industry mandate/free figures are `G3` and admissible, but are project-internal derivation
> — `05` §6.1 Column 3.** ***Tag every finding that rests on one: corroboration, not independent
> confirmation.***

---

"""

body = []
for ln in range(1, n + 1):
    if verdict[ln] == "ADMISSIBLE":
        body.append(lines[ln - 1])
    elif body and body[-1] != "":
        body.append("")  # elide gaps as a blank line; never a marker carrying content

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(header + "\n".join(body).rstrip() + "\n")
print(f"\nWROTE {OUT}")
print(f"extract lines={len(OUT.read_text().splitlines())} (header {len(header.splitlines())} + body)")
