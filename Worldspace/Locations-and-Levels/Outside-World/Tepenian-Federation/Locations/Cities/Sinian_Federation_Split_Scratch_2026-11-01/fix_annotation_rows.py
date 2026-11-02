import re, json, glob, os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from apply_final import SPEC_PATH
CHG = ["Temirötkel","Mawson","Pergamino"]
from write_census import OLD_NAME
from write_datasheet_tiers import DIRKEY, PASSES
apply = "--apply" in sys.argv
CIT = HERE.parent
C = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
# census tier rows line numbers
cl = (CIT / "Official_Population_Census.md").read_text(encoding="utf-8").split("\n")
a_end = next(k for k, l in enumerate(cl) if l.startswith("## Section B"))
cur, cen = None, {}
for i in range(a_end):
    m = re.match(r"^\*\*([^*]+)\*\*", cl[i])
    if m and not cl[i].startswith("**Tier"):
        cur = OLD_NAME.get(m.group(1).strip(), m.group(1).strip())
    if re.match(r"^\| *Tier *\| *Nations *\|", cl[i]) and cur:
        cen[cur] = (i + 3, i + 5)
n = 0
for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
    key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
    if key not in CHG:
        continue
    f = os.path.join(d, "Phase_2.md")
    L = open(f, encoding="utf-8").read().split("\n")
    sp = (CIT / "Specs" / SPEC_PATH[key]).read_text(encoding="utf-8").split("\n")
    t = next(i for i, l in enumerate(sp) if re.match(r"^\| *Tier *\| *Nations *\|", l))
    tagged = [r["nation"] for r in C[key]["rows"] if r["anno"] and "founding" in r["anno"]]
    txt = (f"`(founding wave)` on {', '.join(tagged)} — the Founding Register's founder(s); **no date**; the tag was narrowed to Register founders 2026-11-02 (`DR-88`)"
           if tagged else "none since 2026-11-02 (`DR-88`): the tag now means a Founding Register founder, and none of this city's founders carries it here")
    # drop old founding-wave annotation rows
    keep = [l for l in L if not (re.match(r"^\| Annotation", l) and "founding wave" in l)]
    ci = next((k for k, l in enumerate(keep) if l.startswith("| Composition tier")), None)
    if ci is None:
        print("no anchor", key); continue
    j = ci
    while j + 1 < len(keep) and keep[j + 1].startswith("|") and keep[j + 1].startswith("| Composition tier"):
        j += 1
    rows = [f"| Annotation in the spec tier table | {txt} | `Specs/{os.path.basename(SPEC_PATH[key])}` L{t+3}–L{t+5} |",
            f"| Annotation in the census tier table | {txt} | `Official_Population_Census.md` L{cen[key][0]}–L{cen[key][1]} |"]
    keep[j + 1:j + 1] = rows
    n += 1
    if apply:
        open(f, "w", encoding="utf-8").write("\n".join(keep))
print(n, "sheets", "APPLIED" if apply else "dry run")
