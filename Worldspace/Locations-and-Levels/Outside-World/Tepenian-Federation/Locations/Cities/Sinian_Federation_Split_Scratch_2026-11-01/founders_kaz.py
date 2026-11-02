import csv, math, sys
sys.path.insert(0, ".")
import calc_run4 as R4
master = R4.read_pools_master()
cal = []
for r in csv.DictReader(open(R4.RES / "A_calibration_43.csv", encoding="utf-8")):
    name = R4.CAL_ALIAS.get(r["country"].strip(), r["country"].strip())
    if name not in master or not r["population"].strip() or not r["gdp_per_person_usd"].strip(): continue
    gini = float(r["gini"]) if r["gini"].strip() else None
    cal.append({"name": name, "lg": math.log10(float(r["gdp_per_person_usd"])), "gini": gini, "ratio": master[name] / float(r["population"])})
lgs = [c["lg"] for c in cal]; gs = [c["gini"] for c in cal if c["gini"] is not None]
sd = lambda v: (sum((a - sum(v) / len(v)) ** 2 for a in v) / len(v)) ** 0.5
s_lg, s_g = sd(lgs), sd(gs)
pop, gdp, gini = 20_843_754, 14_692.1331757237, 29.2
lg = math.log10(gdp)
def dist(c):
    d = ((c["lg"] - lg) / s_lg) ** 2
    if c["gini"] is not None: d += ((c["gini"] - gini) / s_g) ** 2
    return d ** 0.5
nn = sorted([c for c in cal if c["gini"] is not None], key=dist)[:3]
ratio = sum(c["ratio"] for c in nn) / 3
pool = pop * ratio
print("neighbors", [(c["name"], round(c["ratio"], 4)) for c in nn], "ratio", round(ratio, 4), "pool", round(pool), "humans (2%)", round(0.02 * pool))
