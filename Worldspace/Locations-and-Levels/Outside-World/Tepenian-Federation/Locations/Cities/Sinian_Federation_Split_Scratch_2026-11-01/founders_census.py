import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from write_specs import tier_lines
from write_census import OLD_NAME, build_national, national_table, section_e
from write_composition import final_line
apply = "--apply" in sys.argv
DATA = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
C = DATA["cities"]
AFFECTED = {"Utstein", "Temirötkel", "Dome Fuji", "Mawson", "Davis", "Shirayuki", "Sinheung", "Mirny", "Casey", "Ariun Nuur", "Relung Panen", "Concordia", "Amundsen Station", "Pergamino"}
p = HERE.parent / "Official_Population_Census.md"
L = p.read_text(encoding="utf-8").split("\n"); n0 = len(L)
a_end = next(k for k, l in enumerate(L) if l.startswith("## Section B"))
cur = None; n = 0
for i in range(a_end):
    m = re.match(r"^\*\*([^*]+)\*\*", L[i])
    if m and not L[i].startswith("**Tier"):
        cur = OLD_NAME.get(m.group(1).strip(), m.group(1).strip())
    if re.match(r"^\| *Tier *\| *Nations *\|", L[i]) and cur in AFFECTED:
        L[i + 2:i + 5] = tier_lines(C[cur]["rows"]); n += 1
tb = next(k for k, l in enumerate(L) if l.startswith("| Nation | Human Exiles |"))
te = tb
while L[te].startswith("|"): te += 1
maritime = int(re.search(r"\| — \| \*\*Maritime fleet\*\* \*\(non-city\)\* \| — \| ([\d,]+) \|", "\n".join(L)).group(1).replace(",", ""))
tbl, grand = national_table(build_national(DATA), maritime)
assert grand == 15_623_523, grand
L[tb:te] = tbl
for k, l in enumerate(L):
    if l.startswith("***Rebuilt 2026-11-02 (`DR-85`)***") and "DR-93" not in l:
        L[k] = l[:-1] + " **Rebuilt a third time 2026-11-02 (`DR-93`)** after Kazakhstan was added (82,544 humans placed at 1.45% in the 13 cities of its time-zone window) and the founder boosts at Temirötkel, Mawson and Pergamino; the totals are unchanged.*"
# Section E note about Kazakhstan
for k, l in enumerate(L):
    if l.startswith("- **Neutral Scientific Territory:**"):
        L.insert(k, "- **Kazakhstan** (added 2026-11-02, `DR-93`): a nation never counted before; its pool (4.13 million, estimated from Romania, Serbia and Russia on income and inequality) is placed at 1.45% in the 13 cities within three zones of UTC+5, and it is a founder at Temirötkel and Mawson (boosted there).")
        break
print(n, "census tier rows;", "national humans", grand, "lines", len(L) - n0, "APPLIED" if apply else "dry run")
if apply and '--comp-only' not in sys.argv: p.write_text("\n".join(L), encoding="utf-8")
# composition file: regenerate the final-composition lines of the affected cities
cp = HERE.parent / "Upper_Earth_Immigration_Composition.md"
CL = cp.read_text(encoding="utf-8").split("\n"); c0 = len(CL)
heads = [(i, l) for i, l in enumerate(CL) if l.startswith("### ") or l.startswith("## ")]
cnt = 0
for idx, (i, l) in enumerate(heads):
    if i > 800: continue
    name = None
    for c in AFFECTED:
        if re.match(r"^#{2,3} " + re.escape(c) + r"( |\*|$)", l) or (c == "Amundsen Station" and l.startswith("## AMUNDSEN STATION")): name = c
    if not name: continue
    end = heads[idx + 1][0] if idx + 1 < len(heads) else len(CL)
    for k in range(i, end):
        if CL[k].startswith("**Final composition after the 2026-11-02 rework"):
            CL[k] = final_line(name, C[name]["rows"]); cnt += 1
print("composition lines", cnt, "(of", len(AFFECTED) - 5, "cities that have a section) lines", len(CL) - c0)
if apply: cp.write_text("\n".join(CL), encoding="utf-8")
