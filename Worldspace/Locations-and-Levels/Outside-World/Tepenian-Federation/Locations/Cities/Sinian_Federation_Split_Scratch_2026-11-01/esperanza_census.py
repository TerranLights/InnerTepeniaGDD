#!/usr/bin/env python3
"""Structured census edits for the Esperanza relocation (after the global number replacement): group rows, subnet totals,
row notes, and the Section B national-origin table. usage: [--apply]"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from write_census import OLD_NAME, build_national, national_table
CIT = HERE.parent
apply = "--apply" in sys.argv
P = json.loads((HERE / "esperanza_plan.json").read_text(encoding="utf-8"))
DATA = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
p = CIT / "Official_Population_Census.md"
L = p.read_text(encoding="utf-8").split("\n")
f = lambda n: f"{n:,}"
def cells(l): return [c.strip() for c in l.strip().strip("|").split("|")]
def num(s): return int(re.sub(r"[^\d]", "", s))
def city_key(name):
    n = name.replace("**", "").strip()
    return OLD_NAME.get(n, n)
# ---- 1. group rows
g = P["groups"]
for i, l in enumerate(L):
    if l.startswith("| — | **Maritime fleet** *(non-city)* | — | 11,205 |"):
        c = cells(l); H, R = 11205 + g["maritime"][1], 11777 + g["maritime"][0]
        c[3], c[4], c[5] = f(H), f(R), f"**{f(H+R)}**"
        c[6] += " **Updated 2026-11-02 (`DR-90`):** it also takes Amundsen Station's share of the Esperanza relocation (arithmetic, NOT a migration)."
        L[i] = "| " + " | ".join(c) + " |"; G_CI = (H, R)
    elif l.startswith("| — | **Space workforce** *(non-city)* | — | 4,054 |"):
        c = cells(l); H, R = 4054 + g["space"][3], 3869 + g["space"][2]
        c[3], c[4], c[5] = f(H), f(R), f"**{f(H+R)}**"
        c[6] += " **Updated 2026-11-02 (`DR-90`):** it also takes half of Amundsen Station's share of the Esperanza relocation (arithmetic, NOT a migration)."
        L[i] = "| " + " | ".join(c) + " |"; G_SP = (H, R)
    elif l.startswith("| — | **Maritime fleet** *(non-city)* | — | 4,053 |"):
        c = cells(l); H, R = 4053 + g["maritime"][3], 3869 + g["maritime"][2]
        c[3], c[4], c[5] = f(H), f(R), f"**{f(H+R)}**"
        c[6] += " **Updated 2026-11-02 (`DR-90`):** the other half of Amundsen Station's share of the Esperanza relocation."
        L[i] = "| " + " | ".join(c) + " |"; G_MA2 = (H, R)
# ---- 2. row notes for Esperanza and the recipients (city rows)
b = next(k for k, l in enumerate(L) if l.startswith("## Section B"))
c_ = next(k for k, l in enumerate(L) if l.startswith("## Section C"))
d_ = next(k for k, l in enumerate(L) if l.startswith("## §D-OVERFLOW"))
def note(i, census):
    c = cells(L[i])
    key = city_key(c[1])
    if key == "Esperanza":
        o = P["esperanza_old"]
        if census == 1:
            t = f"⭐ **Relocation `DR-90`, 2026-11-02:** reduced to 1,200,000 (was {f(o[1]+o[0])}); the {f(P['removed'][1]+P['removed'][0])} difference is divided evenly across the other non-island cities (Santa Luce's method). Arithmetic, NOT a migration."
        else:
            t = f"⭐ **Relocation `DR-90`, 2026-11-02:** scaled by the same factor ({P['factor']:.5f}) to {f(P['esperanza_new'][2]+P['esperanza_new'][3])}; the difference is divided across the cities that have a Census II row. Arithmetic, NOT a migration."
    elif key in P["add"] and any(P["add"][key]):
        a = P["add"][key]
        h, r = (a[1], a[0]) if census == 1 else (a[3], a[2])
        if not (h or r): return
        t = f"⭐ **`DR-90`, 2026-11-02:** +{f(h)} H / +{f(r)} R from the Esperanza relocation. Arithmetic, NOT a migration."
    else:
        return
    c[6] += " " + t
    L[i] = "| " + " | ".join(c) + " |"
for i in range(b, c_):
    if re.match(r"^\| (\d+|—) \| [^|]+ \| (Halley|Janbogo|Mawson|Palmer|Mirny|Byrd|Amundsen) \|", L[i]): note(i, 1)
for i in range(c_, d_):
    if re.match(r"^\| (\d+|—) \| [^|]+ \| (Halley|Janbogo|Mawson|Palmer|Mirny|Byrd|Amundsen) \|", L[i]): note(i, 2)
# ---- 3. subnet totals (recomputed from the city rows plus groups)
LABEL = {"Halley": "Halley / Queen Maud Land", "Janbogo": "Janbogo / Ross Sea", "Mawson": "Mawson / Indian Ocean", "Palmer": "Palmer / Antarctic Peninsula",
         "Mirny": "Mirny / Wilkes Land + Plateau", "Byrd": "Byrd / West Antarctic Ice Sheet", "Amundsen": "Amundsen / South Pole"}
def recompute(lo, hi, grp_rows):
    s = {k: [0, 0] for k in LABEL}
    for i in range(lo, hi):
        m = re.match(r"^\| (\d+|—) \| [^|]+ \| (Halley|Janbogo|Mawson|Palmer|Mirny|Byrd|Amundsen) \| \**([\d,]+)\** \| \**([\d,]+)\** \|", L[i])
        if m: s[m.group(2)][0] += num(m.group(3)); s[m.group(2)][1] += num(m.group(4))
    j = next(k for k in range(lo, hi + 40) if L[k].startswith("| Subnet | Humans"))
    tot = [0, 0]
    for k in range(j + 2, j + 12):
        l = L[k]
        for key, lab in LABEL.items():
            if l.startswith(f"| {lab} |"):
                H, R = s[key]; L[k] = f"| {lab} | {f(H)} | {f(R)} | **{f(H+R)}** |"; tot[0] += H; tot[1] += R
        if l.startswith("| *Non-city"):
            for name, (H, R) in grp_rows.items():
                if name in l: L[k] = f"| *Non-city: {name}* | {f(H)} | {f(R)} | **{f(H+R)}** |"; tot[0] += H; tot[1] += R
        if l.startswith("| **TOTAL"):
            assert [num(x) for x in cells(l)[1:3]] == tot, (l, tot)
            return tot
tot1 = recompute(b, c_, {"maritime fleet": G_CI})
tot2 = recompute(c_, d_, {"space workforce": G_SP, "maritime fleet": G_MA2})
# ---- 4. national origin table (Section B)
tb = next(k for k, l in enumerate(L) if l.startswith("| Nation | Human Exiles |"))
te = tb
while L[te].startswith("|"): te += 1
tbl, grand = national_table(build_national(DATA), G_CI[0])
L[tb:te] = tbl
for k, l in enumerate(L):
    if l.startswith("***Rebuilt 2026-11-02 (`DR-85`)***"):
        L[k] = l[:-1] + " **Rebuilt again 2026-11-02 (`DR-90`)** after the Esperanza relocation (Esperanza 1,200,000; the difference spread across the other cities; the totals are unchanged).*"
print("subnet sums CI", tot1, "CII", tot2, "national humans", grand, "APPLIED" if apply else "dry run")
assert grand == 15_623_523, grand
if apply: p.write_text("\n".join(L), encoding="utf-8")
