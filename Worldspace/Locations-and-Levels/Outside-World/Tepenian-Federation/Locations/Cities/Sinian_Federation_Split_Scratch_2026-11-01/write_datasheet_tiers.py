#!/usr/bin/env python3
"""Replace the 'Primary: A · Significant: B · Notable: C' strings in every city's Datasheets/*.md with the final tier lists.
usage: python3 write_datasheet_tiers.py [--apply]. Skips (and reports) cells with trailing prose after the Notable list."""
import json, re, sys, glob, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
PASSES = HERE.parent / "City_Development_Passes"
DIRKEY = {"Amundsen_Station": "Amundsen Station", "Byrd": "Byrd", "Belgrano": "Belgrano", "Halley": "Halley", "Lazar": "Lazar",
          "Neumayer": "Neumayer", "Sanay": "Sanay", "Santa_Luce": "Santa Luce", "Troll": "Troll", "Utstein": "Utstein",
          "Cape_Adare": "Cape Adare", "Concordia": "Concordia", "Denison": "Denison", "Dumont_dUrville": "Dumont d'Urville",
          "Fort_McMurdo": "Fort McMurdo", "Janbogo": "Janbogo", "Scott": "Scott", "Zukelli": "Zukelli", "Dome_Fuji": "Dome Fuji",
          "Mawson": "Mawson", "Temirotkel": "Temirötkel", "Ariun_Nuur": "Ariun Nuur", "Casey": "Casey", "Davis": "Davis",
          "Kunlun": "Kunlun", "Mirny": "Mirny", "Relung_Panen": "Relung Panen", "Shirayuki": "Shirayuki", "Sinheung": "Sinheung",
          "Zhongshan": "Zhongshan", "Contrapunto": "Contrapunto", "Esperanza": "Esperanza", "Marambio": "Marambio",
          "Palmer_City": "Palmer City", "Pergamino": "Pergamino", "Puerto_Abrigo": "Puerto Abrigo", "Rothera": "Rothera", "Signy": "Signy"}
PAT = re.compile(r"(\*\*)?Primary:(\*\*)? ?([^|\n]*?) · (\*\*)?Significant:(\*\*)? ([^|\n]*?) · (\*\*)?Notable:(\*\*)? ([^|\n]*)")


def lists(rows, annotate):
    out = {}
    for t in ("Primary", "Significant", "Notable"):
        names = []
        for x in rows:
            if x["tier"] == t:
                names.append(x["nation"] + (f" *({x['anno']})*" if (x["anno"] and annotate) else ""))
        out[t] = ", ".join(names)
    return out


def main():
    apply = "--apply" in sys.argv
    data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
    done, skipped, files = 0, [], 0
    for d in sorted(glob.glob(str(PASSES / "*" / "*" / "Datasheets"))):
        key = DIRKEY.get(os.path.basename(os.path.dirname(d)))
        if key is None:
            continue
        for f in sorted(glob.glob(d + "/*.md")):
            L = open(f, encoding="utf-8").read().split("\n")
            changed = False
            for i, ln in enumerate(L):
                def sub(m):
                    nonlocal done
                    tail = re.sub(r"\*\((?:[^()]|\([^()]*\))*\)\*|\([^()]*\)", "", m.group(9))
                    if re.search(r"[.;—]|\bplus\b|\(", tail.strip()):
                        skipped.append((f.split(str(PASSES))[1], i + 1))
                        return m.group(0)
                    annotate = True
                    ls = lists(data[key]["rows"], annotate)
                    trail = m.group(9)[len(m.group(9).rstrip()):]
                    done += 1
                    b = lambda g: g or ""
                    c = lambda g: b(g)
                    return (f"{c(m.group(1))}Primary:{c(m.group(2))} {ls['Primary']} · {c(m.group(4))}Significant:{c(m.group(5))} "
                            f"{ls['Significant']} · {c(m.group(7))}Notable:{c(m.group(8))} {ls['Notable']}{trail}")
                new = PAT.sub(sub, ln)
                if new != ln:
                    L[i] = new
                    changed = True
            if changed and apply:
                open(f, "w", encoding="utf-8").write("\n".join(L))
            files += changed
    print(("APPLIED" if apply else "dry run"), "replacements:", done, "in files:", files)
    print("skipped (hand-edit):", skipped)

if __name__ == "__main__":
    main()
