#!/usr/bin/env python3
"""Esperanza relocation plan (developer 2026-11-02: Esperanza to 1,200,000 in Census I; the removed people are divided evenly,
the way the Santa Luce scenario (DR-68/DR-69) did it). Pure arithmetic on final_tables.json. Writes plan.json. Does not touch repo files."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
C = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
ISLAND = {"Puerto Abrigo", "Dumont d'Urville", "Temirötkel", "Signy", "Marambio", "Contrapunto", "Pergamino", "Fort McMurdo", "Scott", "Palmer City", "Rothera"}
NO_CII = {"Ariun Nuur", "Byrd", "Kunlun", "Dome Fuji"}
ROBOT_ONLY = {"Kunlun", "Dome Fuji"}
ORDER = list(C.keys())  # census-like order used for remainders
def tot(city):
    r = C[city]["rows"]
    return [sum((x["counts"][k] or 0) for x in r) if len(r[0]["counts"]) > k and r[0]["counts"][k] is not None else None for k in range(4)]
T = {c: tot(c) for c in C}
E = T["Esperanza"]  # [CI R, CI H, CII R, CII H]
TARGET = 1_200_000
f = TARGET / (E[0] + E[1])
newE = [None] * 4
newE[1] = round(E[1] * f); newE[0] = TARGET - newE[1]
newE[3] = round(E[3] * f); newE[2] = round((E[2] + E[3]) * f) - newE[3]
delta = [E[k] - newE[k] for k in range(4)]  # removed: R_I, H_I, R_II, H_II
def even(total, keys):
    n = len(keys); b, r = divmod(total, n)
    return {k: b + (1 if i < r else 0) for i, k in enumerate(keys)}
rec_I = [c for c in ORDER if c not in ISLAND and c != "Esperanza"]            # 26
rec_II = [c for c in rec_I if c not in NO_CII]                                   # 22
add = {c: [0, 0, 0, 0] for c in C}
groups = {"maritime": [0, 0, 0, 0], "space": [0, 0, 0, 0]}
# Census I robots (col 0), humans (col 1)
for col in (0, 1):
    share = even(delta[col], rec_I)
    cont = [c for c in rec_I if c not in ROBOT_ONLY and c != "Amundsen Station"]   # 23
    for c in rec_I:
        if c == "Amundsen Station":
            groups["maritime"][col] += share[c]
        elif col == 1 and c in ROBOT_ONLY:
            pass
        else:
            add[c][col] += share[c]
    if col == 1:
        extra = sum(share[c] for c in ROBOT_ONLY)
        for c, v in even(extra, cont).items():
            add[c][col] += v
# Census II robots (col 2), humans (col 3)
for col in (2, 3):
    share = even(delta[col], rec_II)
    for c in rec_II:
        if c == "Amundsen Station":
            h = share[c] // 2
            groups["space"][col] += share[c] - h
            groups["maritime"][col] += h
        else:
            add[c][col] += share[c]
assert sum(sum(v[k] for v in add.values()) for k in range(4)) + sum(g[k] for g in groups.values() for k in range(4)) == sum(delta)
plan = {"target": TARGET, "factor": f, "esperanza_old": E, "esperanza_new": newE, "removed": delta, "add": add, "groups": groups,
        "recipients_I": rec_I, "recipients_II": rec_II}
(HERE / "esperanza_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
if __name__ == "__main__":
    print("Esperanza old [CI R,CI H,CII R,CII H]", E, "new", newE, "removed", delta)
    print("CI total", newE[0] + newE[1], "CII total", newE[2] + newE[3], "factor", round(f, 5))
    print("recipients I", len(rec_I), "II", len(rec_II))
    for c in rec_I:
        print(f"{c:18s} +{add[c]}")
    print("groups", groups)
