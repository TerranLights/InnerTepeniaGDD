#!/usr/bin/env python3
"""S1: new per-nation counts for Esperanza and the 25 recipient cities (shares held; each column re-distributed by
largest remainder over the old counts). Writes final_tables.json (old copy: final_tables_before_esperanza.json) and
esperanza_map.json (old->new totals, workforce, Required, base%)."""
import json
from pathlib import Path
import calc_rebalance as v1
HERE = Path(__file__).resolve().parent
OLD = json.loads((HERE / "final_tables_before_esperanza.json").read_text(encoding="utf-8"))
P = json.loads((HERE / "esperanza_plan.json").read_text(encoding="utf-8"))
C = OLD["cities"]
def colsum(city, k):
    return sum((x["counts"][k] or 0) for x in C[city]["rows"])
newtot = {}
for city in C:
    nr = len(C[city]["rows"][0]["counts"])
    old = [colsum(city, k) if C[city]["rows"][0]["counts"][k] is not None else None for k in range(nr)]
    if city == "Esperanza":
        new = list(P["esperanza_new"])
    elif city in P["add"] and any(P["add"][city]):
        a = P["add"][city]
        new = [old[k] + a[k] if old[k] is not None else None for k in range(nr)]
    else:
        continue
    newtot[city] = (old, new)
    for k in range(nr):
        if old[k] is None or new[k] == old[k]:
            continue
        w = {i: (x["counts"][k] or 0) for i, x in enumerate(C[city]["rows"])}
        d = v1.distribute(new[k], w, even=False)
        for i, x in enumerate(C[city]["rows"]):
            x["counts"][k] = d[i]
    assert [sum((x["counts"][k] or 0) for x in C[city]["rows"]) for k in range(nr) if old[k] is not None] == [v for v in new if v is not None], city
(HERE / "final_tables.json").write_text(json.dumps(OLD, ensure_ascii=False, indent=1), encoding="utf-8")
(HERE / "esperanza_map.json").write_text(json.dumps({c: {"old": o, "new": n} for c, (o, n) in newtot.items()}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(newtot), "cities changed;", "total people before/after:",
      sum(sum(v for v in o if v) for o, n in newtot.values()), sum(sum(v for v in n if v) for o, n in newtot.values()),
      "groups take", sum(P["groups"]["maritime"]) + sum(P["groups"]["space"]))
