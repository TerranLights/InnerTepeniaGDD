#!/usr/bin/env python3
"""Items 3 and 4 of the 2026-11-02 open list (DR-94). Pure arithmetic on final_tables.json.
usage: python3 items25_data.py [--apply]

Item 3, Kunlun's heritage rows get today's names (shares and counts unchanged):
  USA -> CSA; Russia -> Russia (core state); Canada -> Quebec; UK -> United Kingdom; South Korea -> Korea;
  Argentina -> Argentina (without Patagonia); Italy -> Meridia + Magna Lombardia, equal halves;
  Germany -> Germany (without Bavaria) 70% + Austro-Bavaria 30% (Bavaria's share of German aerospace employment is
  about 30%: 38,000 of 130,000 jobs; Austria adds the IWF Graz instrument group, Austromir 1991, ESO membership).
Item 4, Manchuria declines like the Sinian Federation: in every city that lists it, its share is multiplied by a draw
  from 0.55-0.65 (seed 2026110215 fixed before any draw was seen; draw order = the order of final_tables.json),
  and the freed points go in proportion to size to the rows at 4.5% or more outside the top tier (decline_fill's rule).
Tiers are relabeled by apply_final.relabel in the Manchuria cities; Kunlun keeps its heritage tiers.
"""
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import calc_rebalance as v1  # noqa: E402
import calc_rebalance_v2 as v2  # noqa: E402
from apply_final import relabel  # noqa: E402

SEED = 2026110215
LINE = 4.5
apply = "--apply" in sys.argv
data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
C = data["cities"]
bk = HERE / "final_tables_before_items25.json"
if not bk.exists():
    bk.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
log = []

# ---------------------------------------------------------------- item 3: Kunlun
K = C["Kunlun"]["rows"]
TOT = [sum(x["counts"][0] for x in K), None, None, None]
RENAME = {"USA": "CSA", "Russia": "Russia (core state)", "Canada": "Quebec", "UK": "United Kingdom", "South Korea": "Korea",
          "Argentina": "Argentina (without Patagonia)"}
new = []
for x in K:
    n = x["nation"]
    c = x["counts"][0]
    if n in RENAME:
        new.append(dict(x, nation=RENAME[n], **{"from": n}))
    elif n == "Italy":
        a = c // 2
        new.append(dict(x, nation="Meridia", counts=[c - a, None, None, None], **{"from": "Italy"}))
        new.append(dict(x, nation="Magna Lombardia", counts=[a, None, None, None], **{"from": "Italy"}))
    elif n == "Germany":
        ab = round(c * 0.30)
        new.append(dict(x, nation="Germany", counts=[c - ab, None, None, None], **{"from": "Germany"}))
        new.append(dict(x, nation="Austro-Bavaria", counts=[ab, None, None, None], **{"from": "Germany"}))
    else:
        new.append(dict(x))
tot = TOT[0]
for x in new:
    if x["nation"] in ("Meridia", "Magna Lombardia", "Germany", "Austro-Bavaria"):
        x["share"] = round(100 * x["counts"][0] / tot, 3)
assert sum(x["counts"][0] for x in new) == tot
rank = {"Primary": 0, "Significant": 1, "Notable": 2}
new.sort(key=lambda x: (rank[x["tier"]], -x["counts"][0]))
C["Kunlun"]["rows"] = new
log.append("Kunlun: " + "; ".join(f"{x['nation']} {x['share']:.3f}% ({x['counts'][0]:,})" for x in new if x["tier"] != "Notable"))

# ---------------------------------------------------------------- item 4: Manchuria
rng = random.Random(SEED)
draws = {}
for name, d in C.items():
    if any(x["nation"] == "Manchuria" for x in d["rows"]):
        draws[name] = rng.uniform(0.55, 0.65)
for name, r in draws.items():
    rows = v2.copy_rows(C[name]["rows"])
    m = next(x for x in rows if x["nation"] == "Manchuria")
    el = [x for x in rows if x is not m and x["tier"] != "Primary" and x["share"] >= LINE]
    fb = False
    if not el:
        el = [x for x in rows if x is not m and x["share"] >= LINE]
        fb = True
    s_old = m["share"]
    m["share"] = s_old * r
    add = v1.distribute(s_old - m["share"], {x["nation"]: x["share"] for x in el}, even=False)
    for x in el:
        x["share"] += add[x["nation"]]
    for j in range(len(m["counts"])):
        c = m["counts"][j]
        if c is None:
            continue
        newc = round(c * r)
        m["counts"][j] = newc
        add = v1.distribute(c - newc, {x["nation"]: (x["counts"][j] or 0) for x in el}, even=False)
        for x in el:
            x["counts"][j] = (x["counts"][j] or 0) + add[x["nation"]]
    old = C[name]["rows"]
    for j in range(4):
        assert sum(x["counts"][j] or 0 for x in rows) == sum(x["counts"][j] or 0 for x in old), (name, j)
    assert all((q or 0) >= 0 for x in rows for q in x["counts"])
    before = next(x["tier"] for x in old if x["nation"] == "Manchuria")
    order = relabel(rows)
    for x in order:
        o = next(q for q in old if q["nation"] == x["nation"])
        if o["tier"] != x["tier"] and x["nation"] != "Manchuria":
            log.append(f"   {name}: {x['nation']} also changes tier {o['tier']} -> {x['tier']}")
    after = next(x["tier"] for x in order if x["nation"] == "Manchuria")
    C[name]["rows"] = order
    log.append(f"{name}: Manchuria {s_old:.3f}% -> {m['share']:.3f}% (draw {r:.4f}); freed {s_old - m['share']:.3f} points to "
               f"{', '.join(x['nation'] for x in el)}{' (FALLBACK)' if fb else ''}; Manchuria {before} -> {after}")
data["manchuria_draws"] = draws
for l in log:
    print(l)
if apply:
    (HERE / "final_tables.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print("APPLIED" if apply else "dry run")
