#!/usr/bin/env python3
"""Global exact-token replacement of the changed cities' old population numbers with the new ones, over a fixed file set:
Specs, the census, the pass folders (Datasheets, Pre-Trips, ledgers), Division of Industry 09 and 16. Not run over history
(Research_Logs, rulings log, audit reports, megasheets, culture files, scratch). usage: [--apply]"""
import glob, os, re, sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from esperanza_tokens import tokens, M, wf
CIT = HERE.parent
apply = "--apply" in sys.argv
tok, conf = tokens()
assert not conf, conf
# workforce tokens (round, floor, ceil variants)
for c, v in M.items():
    o, n = v["old"], v["new"]
    if o[0] is None: continue
    ow = o[0] + 0.5 * (o[1] or 0); nw = wf(n[0], n[1] or 0)
    if (o[1] or 0) == 0: continue  # robot-only: workforce equals robots, already mapped
    for cand in {int(ow), int(ow + 0.5), int(ow) + 1}:
        k = f"{cand:,}"
        if k not in tok: tok[k] = f"{nw:,}"
files = []
files += sorted(glob.glob(str(CIT / "Specs" / "*" / "*.md")))
files += [str(CIT / "Official_Population_Census.md")]
for d in glob.glob(str(CIT / "City_Development_Passes" / "*" / "*")):
    files += glob.glob(d + "/Datasheets/*.md") + glob.glob(d + "/00.0_Pre-Trip_Inspection.md") + glob.glob(d + "/00.2_Position_Coverage_Ledger.md")
files += [str(CIT / "Division_of_Industry" / "09_Per_City_Baseline_Run.md"), str(CIT / "Division_of_Industry" / "16_Per_City_Three_Tier_Run.md")]
files = [f for f in files if "Zhongshan_Opus" not in f and "Zhongshan_Sonnet" not in f]
pat = re.compile(r"(?<![\d,.])(" + "|".join(re.escape(k) for k in sorted(tok, key=len, reverse=True)) + r")(?![\d,]|\.\d)")
total = 0; per = {}
for f in files:
    t = open(f, encoding="utf-8").read()
    n = [0]
    def sub(m):
        n[0] += 1; return tok[m.group(1)]
    nt = pat.sub(sub, t)
    if n[0]:
        per[os.path.relpath(f, CIT)] = n[0]; total += n[0]
        if apply: open(f, "w", encoding="utf-8").write(nt)
print(("APPLIED" if apply else "dry run"), total, "replacements in", len(per), "files; tokens", len(tok))
for k, v in sorted(per.items(), key=lambda kv: -kv[1])[:25]: print(f"  {v:4d} {k}")
