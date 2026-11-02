import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from apply_final import SPEC_PATH
apply = "--apply" in sys.argv
DATA = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
M = json.loads((HERE / "esperanza_map.json").read_text(encoding="utf-8"))
f = lambda n: f"{n:,}"
n_ok = 0
for city, v in M.items():
    p = HERE.parent / "Specs" / SPEC_PATH[city]
    L = p.read_text(encoding="utf-8").split("\n")
    n0 = len(L)
    o = v["old"]
    # header notes
    for i, l in enumerate(L):
        m = re.match(r"^(\*\*Census I \(Pre-Orbital Era\):\*\* [\d,]+ humans / [\d,]+ robots / \*\*[\d,]+\*\* combined)", l)
        if m and "DR-90" not in l:
            ot = f"{f(o[1] or 0)} humans / {f(o[0])} robots / {f(o[0] + (o[1] or 0))} combined"
            L[i] = m.group(1) + f" *(Esperanza relocation 2026-11-02, `DR-90`: was {ot})*" + l[len(m.group(1)):]
        m = re.match(r"^(\*\*Census II \(Orbital Era\):\*\* [\d,]+ humans / [\d,]+ robots / \*\*[\d,]+\*\* combined)", l)
        if m and "DR-90" not in l and len(o) > 3 and o[2] is not None:
            ot = f"{f(o[3] or 0)} humans / {f(o[2])} robots / {f(o[2] + (o[3] or 0))} combined"
            L[i] = m.group(1) + f" *(Esperanza relocation 2026-11-02, `DR-90`: was {ot})*" + l[len(m.group(1)):]
    # table counts
    h = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nation *\|", l))
    ncols = len(L[h].strip().strip("|").split("|")) - 3
    byn = {r["nation"]: r for r in DATA[city]["rows"]}
    j = h + 2
    while L[j].startswith("|"):
        c = [x.strip() for x in L[j].strip().strip("|").split("|")]
        base = re.sub(r"\s*\*\(.*\)\*$", "", c[1])
        r = byn[base]
        for k in range(ncols):
            old = c[3 + k]
            if re.fullmatch(r"[\d,]+", old):
                c[3 + k] = f(r["counts"][k])
        L[j] = "| " + " | ".join(c) + " |"
        j += 1
    assert len(L) == n0
    if apply: p.write_text("\n".join(L), encoding="utf-8")
    n_ok += 1
print(n_ok, "specs", "APPLIED" if apply else "dry run")
