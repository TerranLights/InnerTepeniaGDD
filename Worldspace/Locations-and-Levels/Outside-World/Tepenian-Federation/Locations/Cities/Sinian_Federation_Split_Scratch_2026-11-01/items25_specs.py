import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from apply_final import SPEC_PATH
from write_specs import tier_lines, table_rows
apply = "--apply" in sys.argv
D = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
C = D["cities"]; DR = D["manchuria_draws"]
NOTE = {}
for c, r in DR.items():
    NOTE[c] = (" Manchuria's share was reduced on 2026-11-02 (`DR-94`), as the Sinian Federation's was: multiplied by %.4f (a draw from 0.55 to 0.65, seed 2026110215), "
               "the freed points going in proportion to size to the rows at 4.5%% or more outside the top tier; tiers were relabeled from the new shares." % r)
NOTE["Kunlun"] = (" Kunlun's heritage rows were given today's names on 2026-11-02 (`DR-94`), shares and counts unchanged: USA is CSA, Russia is Russia (core state), "
                  "Canada is Quebec, UK is the United Kingdom, South Korea is Korea, Argentina is Argentina (without Patagonia), Italy is split equally between Meridia and "
                  "Magna Lombardia, and Germany is split 70% Germany and 30% Austro-Bavaria (Bavaria holds about 30% of German aerospace employment, and Austria adds its "
                  "space-instrument institute at Graz).")
delta = {}
for c in NOTE:
    p = HERE.parent / "Specs" / SPEC_PATH[c]
    L = p.read_text(encoding="utf-8").split("\n"); n0 = len(L)
    rows = C[c]["rows"]
    t = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nations *\|", l))
    L[t + 2:t + 5] = tier_lines(rows)
    h = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nation *\|", l))
    ncols = len(L[h].strip().strip("|").split("|")) - 3
    j = h + 2
    while L[j].startswith("|"): j += 1
    L[h + 2:j] = table_rows(rows, ncols)
    for i, l in enumerate(L):
        if l.startswith("*(Rebalanced 2026-11-02 in the population rework") and "DR-94" not in l:
            k = l.rindex(")*"); L[i] = l[:k] + NOTE[c] + l[k:]; break
    else:
        raise SystemExit("no pre-note in " + c)
    delta[c] = len(L) - n0
    if apply: p.write_text("\n".join(L), encoding="utf-8")
print(delta, "APPLIED" if apply else "dry run")
