import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from apply_final import SPEC_PATH
from write_specs import tier_lines, table_rows
apply = "--apply" in sys.argv
C = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
OLD = json.loads((HERE / "final_tables_before_founders.json").read_text(encoding="utf-8"))["cities"]
AFFECTED = ["Utstein", "Temirötkel", "Dome Fuji", "Mawson", "Davis", "Shirayuki", "Sinheung", "Mirny", "Casey", "Ariun Nuur", "Relung Panen", "Concordia", "Amundsen Station", "Pergamino"]
NOTE = {"Temirötkel": " Kazakhstan, the city's main founder, was added on 2026-11-02 (`DR-93`) at the 1.45% every city in its time-zone window receives, plus a founder boost of 3.67 points taken from the Sinian Federation.",
        "Mawson": " Kazakhstan and Russia (the core state), co-founders with Australia, were boosted on 2026-11-02 (`DR-93`) by 3.35 and 3.00 points taken from the United Kingdom; Kazakhstan also received the 1.45% every city in its window receives.",
        "Pergamino": " Uruguay, the city's first founder, was given a row on 2026-11-02 (`DR-93`) of 4.53 points taken from the United Kingdom."}
for c in AFFECTED:
    NOTE.setdefault(c, " Kazakhstan was added on 2026-11-02 (`DR-93`) at 1.45%, the share every city in its time-zone window receives; every other row shrank in proportion.")
delta = {}
for c in AFFECTED:
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
        if l.startswith("*(Rebalanced 2026-11-02 in the population rework") and "DR-93" not in l:
            k = l.rindex(")*"); L[i] = l[:k] + NOTE[c] + l[k:]; break
    else:
        raise SystemExit("no pre-note in " + c)
    delta[c] = len(L) - n0
    if apply: p.write_text("\n".join(L), encoding="utf-8")
print(delta, "APPLIED" if apply else "dry run")
