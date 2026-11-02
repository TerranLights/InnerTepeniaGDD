import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
C = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
def hr(c):
    r = C[c]["rows"]; return sum(x["counts"][1] or 0 for x in r), sum(x["counts"][0] or 0 for x in r)
RATE = 0.1207 * 1.20  # food rate per human at the mild-coast difficulty, as in 17
NAT_H = 15_623_523
def tier(c, D, f=1.0):
    H, R = hr(c); res = H + R; W = R + 0.5 * H
    base = H * (120.7 * D * f + 85.6) / 1000 + res * (64 * D + 113.2) / 1000
    return dict(H=H, R=R, W=W, base=base, base_pct=100 * base / W, dist=W - base)
d = tier("Davis", 1.25); e = tier("Esperanza", 1.11); r = tier("Relung Panen", 1.43)
ag_d, ag_e, ag_r = 0.35 * d["dist"], 0.15 * e["dist"], 0.25 * r["dist"]
belt, marine = 36_000, 15_600
imp_H = sum(hr(c)[0] for c in ("Halley", "Neumayer", "Ariun Nuur", "Byrd", "Amundsen Station"))
need = imp_H * RATE
for label, rp in (("with Relung Panen", ag_r), ("without Relung Panen", 0)):
    sup = ag_d + ag_e + belt + marine + rp
    cap = sup / RATE
    print(f"{label}: supply {sup:,.0f}  balance {sup-need:+,.0f} ({100*(sup-need)/need:+.0f}%)  capacity {cap:,.0f}  slack {cap-imp_H:,.0f} = {100*(cap-imp_H)/NAT_H:.1f}% of national humans")
    print(f"   shares: Davis {100*ag_d/sup:.1f}%  Esperanza {100*ag_e/sup:.1f}%  Davis+Esperanza {100*(ag_d+ag_e)/sup:.1f}%  Relung {100*rp/sup:.1f}%")
print("forced importers' humans", imp_H, "import need", round(need))
for n, t, ag in (("Davis", d, ag_d), ("Esperanza", e, ag_e), ("Relung Panen", r, ag_r)):
    print(n, {k: round(v, 1) if isinstance(v, float) else v for k, v in t.items()}, "agri", round(ag))
print("people fed beyond themselves (agri/rate): Davis", round(ag_d/RATE), "Esperanza", round(ag_e/RATE), "Relung", round(ag_r/RATE))
