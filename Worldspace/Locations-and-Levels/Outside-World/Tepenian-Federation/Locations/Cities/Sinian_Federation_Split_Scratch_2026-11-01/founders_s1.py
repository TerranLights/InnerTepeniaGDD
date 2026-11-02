#!/usr/bin/env python3
"""Kazakhstan, Uruguay and the founder boosts (developer 2026-11-02, DR-93). Pure arithmetic on final_tables.json.
SEED 2026110214 fixed before any draw was seen; draw order: Temirötkel Kazakhstan, Mawson Kazakhstan, Mawson Russia (core state),
Pergamino Uruguay. Main founder (sole, or a row that does not exist yet): +3.5..5.0; co-founders: +1.5..3.5; taken from the
city's current leader. Kazakhstan's general placement first (13 cities in its window, p = humans / humans of those cities)."""
import json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import calc_rebalance as v1
import calc_rebalance_v3 as v3
import calc_rebalance_v2 as v2
from apply_final import relabel
SEED = 2026110214
KAZ_HUMANS = 82_544
WINDOW = ["Utstein", "Temirötkel", "Dome Fuji", "Mawson", "Davis", "Shirayuki", "Sinheung", "Mirny", "Casey", "Ariun Nuur", "Relung Panen", "Concordia", "Amundsen Station"]
data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
C = data["cities"]
bk = HERE / "final_tables_before_founders.json"
if not bk.exists(): bk.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
def hum(c): return sum(x["counts"][1] or 0 for x in C[c]["rows"])
tot_h = sum(hum(c) for c in WINDOW)
p = KAZ_HUMANS / tot_h
log = [f"Kazakhstan: {KAZ_HUMANS:,} humans over {len(WINDOW)} cities with {tot_h:,} humans -> {100*p:.4f}% each"]
def mk(rows): return v2.copy_rows(rows)
for c in WINDOW:
    rows = mk(C[c]["rows"])
    for x in rows: x["share"] *= (1 - p)
    ncol = len(rows[0]["counts"])
    k = {"tier": "New", "nation": "Kazakhstan", "share": 100 * p, "counts": [None] * ncol, "from": "Kazakhstan", "anno": ""}
    for j in range(ncol):
        if rows[0]["counts"][j] is None: continue
        total = sum(x["counts"][j] or 0 for x in rows)
        new = round(total * p)
        kept = v1.distribute(total - new, {i: (x["counts"][j] or 0) for i, x in enumerate(rows)}, even=False)
        for i, x in enumerate(rows): x["counts"][j] = kept[i]
        k["counts"][j] = new
    rows.append(k)
    C[c]["rows"] = rows
rng = random.Random(SEED)
LEADER = {c: max(C[c]["rows"], key=lambda x: x["share"])["nation"] for c in ("Temirötkel", "Mawson", "Pergamino")}  # before any boost
def boost(city, nation, lo, hi, anno="founding wave"):
    rows = mk(C[city]["rows"])
    leader = LEADER[city]
    g = rng.uniform(lo, hi)
    rows = v3.move_from(rows, leader, [(nation, g)])
    for x in rows:
        x.setdefault("from", ""); x.setdefault("anno", "")
        if x["nation"] == nation: x["anno"] = anno
    C[city]["rows"] = rows
    log.append(f"{city}: +{g:.4f} points to {nation} from {leader}")
boost("Temirötkel", "Kazakhstan", 3.5, 5.0)
boost("Mawson", "Kazakhstan", 1.5, 3.5)
boost("Mawson", "Russia (core state)", 1.5, 3.5)
boost("Pergamino", "Uruguay", 3.5, 5.0)
# relabel tiers in every touched city (the rule of apply_final), keeping annotations
for c in set(WINDOW) | {"Pergamino"}:
    order = relabel(C[c]["rows"])
    C[c]["rows"] = order
# totals check
old = json.loads(bk.read_text(encoding="utf-8"))["cities"]
for c in set(WINDOW) | {"Pergamino"}:
    for j in range(4):
        a = sum(x["counts"][j] or 0 for x in C[c]["rows"]); b = sum(x["counts"][j] or 0 for x in old[c]["rows"])
        assert a == b, (c, j, a, b)
    assert all((q or 0) >= 0 for x in C[c]["rows"] for q in x["counts"]), c
(HERE / "final_tables.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
for l in log: print(l)
for c in ("Temirötkel", "Mawson", "Pergamino"):
    print(c, [(x["nation"], round(x["share"], 2), x["tier"]) for x in C[c]["rows"] if x["nation"] in ("Kazakhstan", "Russia (core state)", "Uruguay")], "leader", C[c]["rows"][0]["nation"], round(C[c]["rows"][0]["share"], 2))
