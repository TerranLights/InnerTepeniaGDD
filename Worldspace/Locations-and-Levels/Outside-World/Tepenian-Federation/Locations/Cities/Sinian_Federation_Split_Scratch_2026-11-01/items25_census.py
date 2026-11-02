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
AFFECTED = set(DATA["manchuria_draws"]) | {"Kunlun"}
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
    if l.startswith("***Rebuilt 2026-11-02 (`DR-85`)***") and "DR-94" not in l:
        L[k] = l[:-1] + " **Rebuilt a fourth time 2026-11-02 (`DR-94`)** after Manchuria's share was reduced in the 15 cities that list it (as the Sinian Federation's was); the totals are unchanged.*"
# Section E table
hs = next(k for k, l in enumerate(L) if l.startswith("| Old name or place |"))
he = hs
while L[he].startswith("|"): he += 1
new_e = section_e(DATA)
ns = next(k for k, l in enumerate(new_e) if l.startswith("| Old name or place |"))
ne = ns
while new_e[ne].startswith("|"): ne += 1
L[hs:he] = new_e[ns:ne]
for k, l in enumerate(L):
    if l.startswith("- **Sinian Federation:** China's nine Han states"):
        L[k] = l.replace("Manchuria, Mongolia (with Inner Mongolia), East Turkestan and Tibet are placed only in the cities inside their time-zone windows; elsewhere their share stays with the Sinian Federation.",
                         "Manchuria, Mongolia (with Inner Mongolia), East Turkestan and Tibet are placed only in the cities inside their time-zone windows; elsewhere their share stays with the Sinian Federation. Manchuria's share was then reduced the same way the Sinian Federation's was (a draw from 0.55 to 0.65 in each of its 15 cities, `DR-94`); Mongolia, East Turkestan, Tibet and Taiwan were not reduced.")
        assert "DR-94" in L[k]
    if l.startswith("- **Kunlun's heritage rows**"):
        L[k] = ("- **Kunlun's heritage rows** (given today's names 2026-11-02, `DR-94`; shares and counts unchanged): USA is CSA, Russia is Russia (core state), "
                "Canada is Quebec, UK is the United Kingdom, South Korea is Korea, Argentina is Argentina (without Patagonia), Italy is split equally between Meridia and "
                "Magna Lombardia, and Germany is split 70% Germany and 30% Austro-Bavaria. The rows follow space-program heritage and not headcount: the Italian space agency "
                "is in Rome (Meridia) and its industry in Turin and Milan (Magna Lombardia); Germany's astronaut corps, agency headquarters and module builders are in Cologne and Bremen, "
                "while Bavaria holds the mission-control center at Oberpfaffenhofen, the European Southern Observatory's headquarters at Garching and Airbus's satellite works at "
                "Ottobrunn (about 30% of German aerospace employment), and Austria adds its space-instrument institute at Graz. Intermarium/Intermaria is unchanged.")
print(n, "census tier rows;", "lines", len(L) - n0, "APPLIED" if apply else "dry run")
if apply: p.write_text("\n".join(L), encoding="utf-8")
cp = HERE.parent / "Upper_Earth_Immigration_Composition.md"
CL = cp.read_text(encoding="utf-8").split("\n"); c0 = len(CL)
heads = [(i, l) for i, l in enumerate(CL) if l.startswith("### ") or l.startswith("## ")]
cnt = 0
for idx, (i, l) in enumerate(heads):
    name = None
    for c in AFFECTED:
        if re.match(r"^#{2,3} " + re.escape(c) + r"( |\*|$)", l) or (c == "Amundsen Station" and l.startswith("## AMUNDSEN STATION")): name = c
    if not name: continue
    end = heads[idx + 1][0] if idx + 1 < len(heads) else len(CL)
    for k in range(i, end):
        if CL[k].startswith("**Final composition after the 2026-11-02 rework"):
            CL[k] = final_line(name, C[name]["rows"]); cnt += 1
print("composition lines", cnt, "lines", len(CL) - c0)
if apply: cp.write_text("\n".join(CL), encoding="utf-8")
