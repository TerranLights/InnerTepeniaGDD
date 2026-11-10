#!/usr/bin/env python3
"""Verify the 2026-11-03 Sinheung amendment note against the live files (read-only). Run from the repo root:
python3 -I verify_sinheung_note.py
Each check: (file, line or (first,last), [substrings that must all appear]). Prints OK/DIFF and addresses only."""
import os, sys, re
REPO = os.getcwd()
LOC = "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations"
CIT = LOC + "/Cities"
ULM = "Worldspace/Locations-and-Levels/Universal_Location_Methodology"
SPEC = CIT + "/Specs/Mirny subnet/Sinheung.md"
CEN = CIT + "/Official_Population_Census.md"
REG = CIT + "/Founding_Register.md"
D16 = CIT + "/Division_of_Industry/16_Per_City_Three_Tier_Run.md"
D09 = CIT + "/Division_of_Industry/09_Per_City_Baseline_Run.md"
EXT = ULM + "/Extent_and_Density_Per_City.md"
LOG = ULM + "/DEVELOPER_RULINGS_LOG.md"
PORTS = LOC + "/Infrastructure/Ports.md"
NTH = LOC + "/Infrastructure/Neutral_Transshipment_Hubs.md"
LANGB = CIT + "/Research_Logs/Language_Blocs_By_City_2026-11-03.md"
CULT = CIT + "/Local_Cultures/Mirny_Subnet/Sinheung.md"
SYM = CIT + "/City_Symbolic_Substrate/City_Symbol_Assignments.md"

CHECKS = [
 (CEN, 509, ["494,341", "520,192", "1,014,533"]),
 (CEN, 647, ["410,746", "424,595", "835,341"]),
 (CEN, 416, ["Primary", "Korea"]),
 (CEN, 417, ["Significant", "Japan, Germany, Sinian Federation"]),
 (CEN, 418, ["Notable", "Indonesia"]),
 (CEN, 33, ["founding wave", "says nothing about when people arrived"]),
 (SPEC, 4, ["Soyuz"]),
 (SPEC, 8, ["Temir"]),
 (SPEC, 71, ["494,341", "520,192", "1,014,533"]),
 (SPEC, 72, ["410,746", "424,595", "835,341"]),
 (SPEC, 76, ["Primary", "Korea"]),
 (SPEC, 77, ["Significant", "Japan, Germany, Sinian Federation"]),
 (SPEC, 92, ["Korea", "33.00%"]),
 (SPEC, 93, ["Japan", "9.40%"]),
 (SPEC, 94, ["Germany", "8.75%"]),
 (SPEC, 95, ["Sinian Federation", "5.45%"]),
 (SPEC, 96, ["Indonesia", "3.99%"]),
 (SPEC, 102, ["Taiwan", "2.86%"]),
 (SPEC, 104, ["Idelsk-Uralia", "2.03%"]),
 (SPEC, 105, ["Russia (core state)", "2.03%"]),
 (SPEC, 108, ["Kazakhstan", "1.45%"]),
 (SPEC, 154, ["Zhongshan"]),
 (SPEC, 211, ["Russian-built polar research infrastructure"]),
 (SPEC, 213, ["Founding population"]),
 (SPEC, 215, ["Soyuz"]),
 (REG, 62, ["Sinheung", "Korea", "Jeju-do", "geography", "DR-44"]),
 (REG, 61, ["Shirayuki"]),
 (REG, 60, ["Zhongshan"]),
 (D16, 257, ["Sinheung", "767,363", "41.8%", "26.2%", "32.0%"]),
 (D16, 1834, ["SINHEUNG", "DETERMINED"]),
 (D16, 1838, ["321,100"]),
 (D16, 1839, ["211,975"]),
 (D16, 1840, ["234,288"]),
 (D16, 1850, ["200,818"]),
 (D16, 1851, ["11,157"]),
 (D09, 80, ["Sinheung", "767,363", "271,073"]),
 (EXT, 620, ["Sinheung", "1,014,533"]),
 (PORTS, 130, ["Tri-Cities"]),
 (NTH, 60, ["Tri-Cities"]),
 (CULT, 90, ["33.00"]),
 (CULT, 135, ["dominant public language"]),
 (LOG, 538, ["DR-19"]),
 (LOG, 634, ["DR-25"]),
 (LOG, 654, ["DR-26"]),
 (LOG, 919, ["Shirayuki and Sinheung"]),
 (LOG, 930, ["Japan and Korea stay"]),
 (LANGB, (1104, 1116), ["Korean", "33.00"]),
 (LANGB, (1104, 1116), ["German", "10.06"]),
 (LANGB, (1104, 1116), ["Japanese", "9.40"]),
 (LANGB, (1104, 1116), ["Mandarin", "8.65"]),
 (SYM, (1, 400), ["Sinheung", "Uranus"]),
]
cache = {}
def lines(path):
    if path not in cache:
        fp = os.path.join(REPO, path)
        cache[path] = open(fp, encoding="utf-8").read().split("\n") if os.path.exists(fp) else None
    return cache[path]
ok = diff = 0
for path, where, subs in CHECKS:
    L = lines(path); name = os.path.basename(path)
    if L is None:
        print("MISSING  %s" % name); diff += 1; continue
    if isinstance(where, tuple):
        text = "\n".join(L[where[0] - 1:where[1]]); label = "L%d-L%d" % where
    else:
        text = L[where - 1] if where - 1 < len(L) else ""; label = "L%d" % where
    miss = [s for s in subs if s not in text]
    if miss:
        print("DIFF     %s %s  missing: %s" % (name, label, miss)); diff += 1
    else:
        print("OK       %s %s" % (name, label)); ok += 1
print("TOTAL line checks: %d   OK: %d   DIFF: %d" % (len(CHECKS), ok, diff))
for path, want in [(SPEC, 269), (CEN, 892)]:
    n = len(lines(path)) - 1
    print("file length %s: %d newline-lines (note says %d): %s" % (os.path.basename(path), n, want, "OK" if n == want else "DIFF"))

# ---- recomputed figures ----
S = lines(SPEC)
rows = []
for i in range(91, 130):  # L92..L130
    cells = [c.strip() for c in S[i].strip().strip("|").split("|")]
    if len(cells) >= 3 and cells[0] in ("Primary", "Significant", "Notable"):
        rows.append((cells[0], cells[1].replace("*(founding wave)*", "").strip(), float(cells[2].rstrip("%"))))
tiers = {}
for r in rows: tiers[r[0]] = tiers.get(r[0], 0) + 1
print("composition rows parsed (L92-L130): %d; by tier: %s; share sum %.3f%%; rows under 1%%: %d" % (len(rows), tiers, sum(r[2] for r in rows), sum(r[2] < 1 for r in rows)))
share = {r[1]: r[2] for r in rows}
print("East Asian cluster: Korea+Japan+Sinian Federation = %.2f; + Taiwan = %.2f; + Manchuria, Mongolia, East Turkestan, Tibet = %.3f" % (
    share["Korea"] + share["Japan"] + share["Sinian Federation"], share["Korea"] + share["Japan"] + share["Sinian Federation"] + share["Taiwan"],
    share["Korea"] + share["Japan"] + share["Sinian Federation"] + share["Taiwan"] + share["Manchuria"] + share["Mongolia"] + share["East Turkestan"] + share["Tibet"]))
russia13 = ["Idelsk-Uralia", "Russia (core state)", "Siberia", "Donska-Kubania", "Künnarantaiga", "Dagestan", "Chechnya", "Kabardino-Balkaria", "North Ossetia-Alania", "Finland", "Ingushetia", "Karachay-Cherkessia", "Tuva"]
print("the thirteen Russia rows together: %.2f%% (found %d of 13)" % (sum(share.get(n, 0) for n in russia13), sum(n in share for n in russia13)))
H1, R1, H2, R2 = 494341, 520192, 410746, 424595
print("Census I %d, Census II %d" % (H1 + R1, H2 + R2))
print("retention humans %.2f%%, robots %.2f%%, combined %.2f%%, gap %.2f points" % (100*H2/H1, 100*R2/R1, 100*(H2+R2)/(H1+R1), 100*(H2/H1 - R2/R1)))
print("robots share of Census I %.2f%%, humans %.2f%%" % (100*R1/(H1+R1), 100*H1/(H1+R1)))
print("workforce (robots + half the humans) = %.1f; required 271,073 / 767,363 = %.2f%%" % (R1 + H1/2, 100*271073/767363))
print("section 17: 321,100 + 211,975 + 234,288 = %d; shares %.3f%% / %.3f%% / %.3f%%; fabrication+Institute half = %d; distinctive %d" % (
    321100+211975+234288, 100*321100/767363, 100*211975/767363, 100*234288/767363, 200818+11157, 211975+234288))
print("land need at 10,000 and 7,000 per km2: %.2f and %.2f km2; density on 40 km2: %.0f per km2" % ((H1+R1)/10000, (H1+R1)/7000, (H1+R1)/40))
print("ratio check (Census I added humans/robots): %.3f; city ratio %.3f; (Census II added): %.3f; city ratio %.3f" % (14930/13271, H1/R1, 8570/11462, H2/R2))
sys.exit(1 if diff else 0)
