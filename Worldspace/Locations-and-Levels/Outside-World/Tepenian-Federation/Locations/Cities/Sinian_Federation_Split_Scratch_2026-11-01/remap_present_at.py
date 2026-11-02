#!/usr/bin/env python3
"""Remap the bare line numbers inside 'Present at Lx–Ly …' datasheet cells (the file is named in the NEXT cell, so
remap_line_citations.py skipped them). Per-nation rows are excluded (already rewritten to the new ranges).
usage: python3 remap_present_at.py [--apply]. Base = git 593510ab (the state the cell numbers describe)."""
import glob, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "Universal_Location_Methodology" / "Tools"))
import remap_line_citations as R
from apply_final import SPEC_PATH
from write_datasheet_tiers import DIRKEY, PASSES
BASE = "593510ab"
CIT = HERE.parent
apply = "--apply" in sys.argv
LTOK = re.compile(r"\bL(\d+)(?:([–-])L?(\d+))?")
changed, left, rows = 0, [], []
for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
    key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
    if key not in SPEC_PATH:
        continue
    for f in glob.glob(d + "/*.md"):
        L = open(f, encoding="utf-8").read().split("\n")
        ch = False
        for i, ln in enumerate(L):
            if not ln.startswith("|") or ln.startswith("| Per-nation") or "Present at L" not in ln:
                continue
            cells = ln.split(" | ")
            if len(cells) < 3:
                continue
            cite = cells[-1]
            if "Upper_Earth_Immigration_Composition" in cite:
                path = CIT / "Upper_Earth_Immigration_Composition.md"
            elif "Official_Population_Census" in cite:
                path = CIT / "Official_Population_Census.md"
            elif "Specs/" in cite:
                path = CIT / "Specs" / SPEC_PATH[key]
            else:
                left.append((os.path.basename(f), key, "unknown file")); continue
            lm = R.line_map(BASE, str(path))
            mp, nold = lm[0], lm[1]
            def one(m):
                global changed
                a = int(m.group(1)); b = int(m.group(3)) if m.group(3) else None
                na = mp.get(a) if a <= nold else a
                nb = (mp.get(b) if b <= nold else b) if b else None
                if na is None or (b and nb is None):
                    left.append((os.path.basename(f), key, m.group(0))); return m.group(0)
                if na != a or (b and nb != b): changed += 1
                return f"L{na}" + (f"{m.group(2)}L{nb}" if b else "")
            mid = " | ".join(cells[1:-1])
            # only the cell(s) between label and citation
            new_mid = LTOK.sub(one, mid)
            if new_mid != mid:
                L[i] = " | ".join([cells[0], new_mid, cite]); ch = True
                rows.append((key, os.path.basename(f), i + 1))
        if ch and apply:
            open(f, "w", encoding="utf-8").write("\n".join(L))
print("numbers changed", changed, "rows", len(rows), "left:", left[:10], "APPLIED" if apply else "dry run")
