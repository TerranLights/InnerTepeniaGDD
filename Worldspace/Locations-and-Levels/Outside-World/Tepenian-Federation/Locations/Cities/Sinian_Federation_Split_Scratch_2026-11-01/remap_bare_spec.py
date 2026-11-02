#!/usr/bin/env python3
"""Remap bare 'Spec L123' / 'spec L123' citations in a city's Datasheets (the tool remap_line_citations.py needs a file name).
usage: python3 remap_bare_spec.py [--apply]. Base = git 593510ab."""
import glob, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "Universal_Location_Methodology" / "Tools"))
import remap_line_citations as R
from apply_final import SPEC_PATH
from write_datasheet_tiers import DIRKEY, PASSES
BASE = "593510ab"
PAT = re.compile(r"(\b[Ss]pec\s+)(L\d+(?:[–-]\d+)?(?:,\s*L?\d+(?:[–-]\d+)?)*)")
apply = "--apply" in sys.argv
moved, left = 0, []
for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
    key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
    if key not in SPEC_PATH:
        continue
    sp = HERE.parent / "Specs" / SPEC_PATH[key]
    mp, nold, nnew, edited = R.line_map(BASE, str(sp))
    for f in glob.glob(d + "/*.md"):
        t = open(f, encoding="utf-8").read()
        def fix(m):
            global moved
            def one(n):
                global moved
                a = int(n.group(2)); b = int(n.group(4)) if n.group(4) else None
                na = mp.get(a) if a <= nold else a
                nb = (mp.get(b) if b <= nold else b) if b else None
                if na is None or (b and nb is None):
                    left.append((os.path.basename(f), key, n.group(0))); return n.group(0)
                if na != a or (b and nb != b): moved += 1
                return "%s%d%s" % (n.group(1), na, ("%s%d" % (n.group(3), nb)) if b else "")
            return m.group(1) + R.NUM.sub(one, m.group(2))
        nt = PAT.sub(fix, t)
        if nt != t and apply:
            open(f, "w", encoding="utf-8").write(nt)
print("moved", moved, "left as written:", left, "APPLIED" if apply else "dry run")
