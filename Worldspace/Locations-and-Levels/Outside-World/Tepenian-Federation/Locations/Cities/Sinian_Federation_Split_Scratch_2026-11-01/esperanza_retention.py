import glob, json, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from write_datasheet_tiers import DIRKEY, PASSES
apply = "--apply" in sys.argv
M = json.loads((HERE / "esperanza_map.json").read_text(encoding="utf-8"))
changed = 0; files = 0; left = []
for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
    key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
    if key not in M: continue
    n = M[key]["new"]
    if len(n) < 4 or n[2] is None or not n[1]: continue
    R1, H1, R2, H2 = n[0], n[1], n[2], n[3]
    comb, hum, rob = (R2 + H2) / (R1 + H1), H2 / H1, R2 / R1
    spread = 100 * (rob - hum)
    for f in glob.glob(d + "/*.md"):
        L = open(f, encoding="utf-8").read().split("\n"); ch = False
        for i, ln in enumerate(L):
            if not ln.startswith("| Retention"): continue
            new = ln
            new = re.sub(r"([\d,]+)\s*÷\s*([\d,]+)\s*=\s*(\**)([\d.]+)%", lambda m: f"{m.group(1)}÷{m.group(2)} = {m.group(3)}{100*int(m.group(1).replace(',',''))/int(m.group(2).replace(',','')):.{len(m.group(4).split('.')[-1])}f}%", new)
            new = re.sub(r"(combined\s*\**)([\d.]+)(\**%)", lambda m: f"{m.group(1)}{100*comb:.2f}{m.group(3)}", new)
            new = re.sub(r"(human\s*\**)([\d.]+)(\**%)", lambda m: f"{m.group(1)}{100*hum:.2f}{m.group(3)}", new)
            new = re.sub(r"(robot\s*\**)([\d.]+)(\**%)", lambda m: f"{m.group(1)}{100*rob:.2f}{m.group(3)}", new)
            new = re.sub(r"(\**)([\d.]+)( pp toward robots)", lambda m: f"{m.group(1)}{spread:.2f}{m.group(3)}", new)
            if new != ln:
                L[i] = new; ch = True; changed += 1
        if ch:
            files += 1
            if apply: open(f, "w", encoding="utf-8").write("\n".join(L))
print(("APPLIED" if apply else "dry run"), changed, "rows in", files, "files")
