#!/usr/bin/env python3
"""Verify the 2026-11-03 Davis amendment note against the live source files (read-only).

Each check: (file, line number, [substrings that must all appear on that line]).
Prints one result per check and a total. Prints only OK/DIFF and the address, never another
location's text. Run:  python3 -I verify_davis_note.py  (from the repo root).
"""
import os, sys

REPO = os.getcwd()
LOC = "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations"
CIT = LOC + "/Cities"
ULM = "Worldspace/Locations-and-Levels/Universal_Location_Methodology"
SPEC = CIT + "/Specs/Mirny subnet/Davis.md"
CEN = CIT + "/Official_Population_Census.md"
REG = CIT + "/Founding_Register.md"
DOI = CIT + "/Division_of_Industry"
LOG = ULM + "/DEVELOPER_RULINGS_LOG.md"
INF = LOC + "/Infrastructure"
LANG = CIT + "/Research_Logs/Language_Blocs_By_City_2026-11-03.md"
CONN = CIT + "/City_National_Connections.md"
SYM = CIT + "/City_Symbolic_Substrate/City_Symbol_Assignments.md"
EXT = ULM + "/Extent_and_Density_Per_City.md"
STP = "Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/TBN [STP-06 thicc Chinese Hao]/README.md"

CHECKS = [
 (CEN, 506, ["590,668", "619,764", "1,210,432"]),
 (CEN, 650, ["454,101", "363,374", "817,475"]),
 (CEN, 394, ["Japan, Sinian Federation, United Kingdom, Germany, Korea"]),
 (CEN, 395, ["Indonesia, Australia", "founding wave"]),
 (SPEC, 15, ["590,668", "619,764", "1,210,432"]),
 (SPEC, 16, ["454,101", "363,374", "817,475"]),
 (SPEC, 20, ["Japan, Sinian Federation, United Kingdom, Germany, Korea"]),
 (SPEC, 21, ["Indonesia, Australia", "founding wave"]),
 (SPEC, 32, ["Japan", "10.42%", "64,576", "61,547"]),
 (SPEC, 33, ["Sinian Federation", "9.72%"]),
 (SPEC, 37, ["Indonesia", "5.74%"]),
 (SPEC, 38, ["Australia", "founding wave", "5.74%", "35,573", "33,902"]),
 (SPEC, 49, ["Idelsk-Uralia", "1.67%"]),
 (SPEC, 76, ["Tuva", "0.013%"]),
 (SPEC, 99, ["Jun 4", "~37 days"]),
 (SPEC, 100, ["Nov 25", "~55 days"]),
 (SPEC, 107, ["ICE-FREE OASIS"]),
 (SPEC, 108, ["~73 mm"]),
 (SPEC, 109, ["~28 mm", "~38% retention"]),
 (REG, 59, ["Davis", "Australia", "extremely close", "DR-19"]),
 (DOI + "/09_Per_City_Baseline_Run.md", 79, ["Davis", "590,668", "1,210,432", "323,548", "915,098", "35.4%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 262, ["Davis", "915,098", "41.9%", "20.3%", "37.8%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2006, ["19.", "DAVIS", "Option B"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2010, ["383,295", "41.9%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2011, ["252,606", "27.6%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2012, ["279,197", "30.5%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2014, ["531,803", "58.1%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2022, ["186,131"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2074, ["Mandate 28.2% / free 31.1%"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 2076, ["27.6%", "30.5%", "252,606", "279,197"]),
 (DOI + "/16_Per_City_Three_Tier_Run.md", 3568, ["Davis", "27.6%", "30.5%"]),
 (DOI + "/19_National_Balance_Refresh_2026-11-02.md", 62, ["Davis", "186,131"]),
 (DOI + "/19_National_Balance_Refresh_2026-11-02.md", 81, ["Davis", "44.2%"]),
 (INF + "/Highways.md", 199, ["Zhongshan", "Davis"]),
 (INF + "/Ports.md", 559, ["Davis", "Prydz Bay"]),
 (INF + "/Airports.md", 50, ["Davis"]),
 (INF + "/Airports.md", 55, ["Davis"]),
 (INF + "/Airports.md", 57, ["highway network only"]),
 (CONN, 303, ["### Davis"]),
 (CONN, 304, ["Australia is among the founders"]),
 (CONN, 307, ["Hwy 110"]),
 (CONN, 308, ["Relay Vaults"]),
 (LANG, 916, ["### Davis"]),
 (LANG, 922, ["English", "17.02", "25.78"]),
 (LANG, 923, ["Mandarin", "13.29", "14.08"]),
 (LANG, 925, ["Japanese", "10.42"]),
 (LANG, 926, ["German", "9.93"]),
 (LANG, 927, ["Korean", "8.35"]),
 (EXT, 617, ["Davis", "1,210,432", "410"]),
 (EXT, 636, ["2,952"]),
 (SYM, 112, ["Davis", "BLANK"]),
 (LOG, 1555, ["founding wave", "Founding Register"]),
 (LOG, 1660, ["founding wave"]),
 (LOG, 1698, ["DR-104"]),
 (STP, 22, ["Davis"]),
]

cache = {}
def lines(path):
    if path not in cache:
        full = os.path.join(REPO, path)
        if not os.path.exists(full):
            cache[path] = None
        else:
            with open(full, encoding="utf-8") as f:
                cache[path] = f.read().split("\n")
    return cache[path]

ok = diff = 0
for path, n, subs in CHECKS:
    L = lines(path)
    name = os.path.basename(path)
    if L is None:
        print("MISSING  %s L%d" % (name, n)); diff += 1; continue
    line = L[n-1] if n-1 < len(L) else ""
    miss = [s for s in subs if s not in line]
    if miss:
        print("DIFF     %s L%d  missing: %s" % (name, n, miss)); diff += 1
    else:
        print("OK       %s L%d" % (name, n)); ok += 1
print("TOTAL line checks: %d   OK: %d   DIFF: %d" % (len(CHECKS), ok, diff))

# ---- derived figures, recomputed ----
spec = lines(SPEC)
rows = []
for i in range(31, 76):
    cells = [c.strip() for c in spec[i].strip().strip("|").split("|")]
    if len(cells) >= 7 and cells[0] in ("Primary", "Significant", "Notable"):
        rows.append((cells[0], cells[1], float(cells[2].rstrip("%")), int(cells[3].replace(",", "")), int(cells[4].replace(",", ""))))
tiers = {}
for r in rows: tiers[r[0]] = tiers.get(r[0], 0) + 1
print("composition table rows parsed (L32-L76): %d; by tier: %s" % (len(rows), tiers))
print("share sum: %.3f%%" % sum(r[2] for r in rows))
print("rows under 1%%: %d; under 0.5%%: %d; under 0.1%%: %d" % (sum(r[2] < 1 for r in rows), sum(r[2] < .5 for r in rows), sum(r[2] < .1 for r in rows)))
print("Census I sum over rows: %d" % sum(r[3] + r[4] for r in rows))
small = sorted(rows, key=lambda r: r[3] + r[4])[:4]
print("four smallest rows at Census I: %s" % [(s[1], s[3] + s[4]) for s in small])
H1, R1, H2, R2 = 590668, 619764, 454101, 363374
print("Census I %d, Census II %d" % (H1 + R1, H2 + R2))
print("retention combined %.2f%%, humans %.2f%%, robots %.2f%%, spread %.2f pp" % (100*(H2+R2)/(H1+R1), 100*H2/H1, 100*R2/R1, 100*(H2/H1 - R2/R1)))
print("robots share of Census I %.2f%%, of Census II %.2f%%" % (100*R1/(H1+R1), 100*R2/(H2+R2)))
print("humans departed %d = %.2f%%; robots departed %d = %.2f%%; people gone %d" % (H1-H2, 100*(H1-H2)/H1, R1-R2, 100*(R1-R2)/R1, (H1+R1)-(H2+R2)))
print("density on 410 km2: Census I %.2f, Census II %.2f" % ((H1+R1)/410, (H2+R2)/410))
print("workforce %.0f (robots + humans/2); required 323,548 / 915,098 = %.2f%%" % (R1 + H1/2, 100*323548/915098))
print("file 16 section 19: 383,295 + 252,606 + 279,197 = %d; mandated %.2f%%, free %.2f%%" % (383295+252606+279197, 100*252606/915098, 100*279197/915098))
print("agriculture 35%% of 531,803 = %.2f; technical half 12.5%% = %.2f" % (531803*.35, 531803*.125))
print("retention in climate: 28/72.8 = %.2f%%; 28/73 = %.2f%%" % (100*28/72.8, 100*28/73))
sys.exit(1 if diff else 0)
