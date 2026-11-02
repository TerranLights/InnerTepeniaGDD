#!/usr/bin/env python3
"""The '(founding wave)' tag now means 'named as a founder in the Founding Register' (developer 2026-11-02, DR-88).
Updates final_tables.json annotations, then the specs (tier rows + nation cells), census Section A tier rows, and the
datasheets' tier lists and annotation rows. usage: python3 apply_tag_change.py [--apply]"""
import json, re, sys, glob, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from apply_final import SPEC_PATH
from write_specs import tier_lines
from write_census import OLD_NAME
from write_datasheet_tiers import DIRKEY, PASSES, PAT, lists
CIT = HERE.parent
apply = "--apply" in sys.argv
CHG = {"Rothera": ([], ["CSA","Cascadia","Appalachia","México","New England","Quebec","Prairie Federation","Midwest Republic","Colorado","Sonora","Yucatán","Hawaii","Alaska"])}
data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
C = data["cities"]
for city, (rm, add) in CHG.items():
    rows = {r["nation"]: r for r in C[city]["rows"]}
    for n in rm:
        assert n in rows and rows[n]["anno"], (city, n, "no tag to remove")
        rows[n]["anno"] = ""
    for n in add:
        assert n in rows, (city, n, "not in table")
        rows[n]["anno"] = "founding wave"
if apply:
    (HERE / "final_tables.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
log = []
# ---- specs: tier rows + nation cells
for city in CHG:
    p = CIT / "Specs" / SPEC_PATH[city]
    L = p.read_text(encoding="utf-8").split("\n")
    t = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nations *\|", l))
    L[t + 2:t + 5] = tier_lines(C[city]["rows"])
    h = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nation *\|", l))
    byn = {r["nation"]: r for r in C[city]["rows"]}
    j = h + 2
    while L[j].startswith("|"):
        cells = [c.strip() for c in L[j].strip().strip("|").split("|")]
        base = re.sub(r"\s*\*\(.*\)\*$", "", cells[1])
        r = byn[base]
        cells[1] = base + (f" *({r['anno']})*" if r["anno"] else "")
        L[j] = "| " + " | ".join(cells) + " |"
        j += 1
    if apply:
        p.write_text("\n".join(L), encoding="utf-8")
    log.append(("spec", city))
# ---- census Section A tier rows
cp = CIT / "Official_Population_Census.md"
L = cp.read_text(encoding="utf-8").split("\n")
a_end = next(k for k, l in enumerate(L) if l.startswith("## Section B"))
cur = None
for i in range(a_end):
    m = re.match(r"^\*\*([^*]+)\*\*", L[i])
    if m and not L[i].startswith("**Tier"):
        cur = OLD_NAME.get(m.group(1).strip(), m.group(1).strip())
    if re.match(r"^\| *Tier *\| *Nations *\|", L[i]) and cur in CHG:
        L[i + 2:i + 5] = tier_lines(C[cur]["rows"]); log.append(("census", cur))
if apply:
    cp.write_text("\n".join(L), encoding="utf-8")
# ---- datasheets
for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
    key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
    if key not in CHG:
        continue
    rows = C[key]["rows"]
    for f in sorted(glob.glob(d + "/*.md")):
        L = open(f, encoding="utf-8").read().split("\n")
        ch = False
        for i, ln in enumerate(L):
            def sub(m):
                tail = re.sub(r"\*\((?:[^()]|\([^()]*\))*\)\*|\([^()]*\)", "", m.group(9))
                if re.search(r"[.;—]|\bplus\b|\(", tail.strip()):
                    log.append(("SKIPPED cell", key, os.path.basename(f), i + 1)); return m.group(0)
                annotate = "*(" in (m.group(3) + m.group(6) + m.group(9)) or True
                ls = lists(rows, annotate)
                trail = m.group(9)[len(m.group(9).rstrip()):]
                c = lambda g: g or ""
                return (f"{c(m.group(1))}Primary:{c(m.group(2))} {ls['Primary']} · {c(m.group(4))}Significant:{c(m.group(5))} "
                        f"{ls['Significant']} · {c(m.group(7))}Notable:{c(m.group(8))} {ls['Notable']}{trail}")
            new = PAT.sub(sub, ln)
            if new != ln:
                L[i] = new; ch = True
        if ch and apply:
            open(f, "w", encoding="utf-8").write("\n".join(L))
print(len([x for x in log if x[0] != "SKIPPED cell"]), "spec/census edits;", [x for x in log if x[0] == "SKIPPED cell"], "APPLIED" if apply else "dry run")
