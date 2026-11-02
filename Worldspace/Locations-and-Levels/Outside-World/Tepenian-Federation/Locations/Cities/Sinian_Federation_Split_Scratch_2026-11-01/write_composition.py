#!/usr/bin/env python3
"""Bring Upper_Earth_Immigration_Composition.md into line with the final tables. 2026-11-02.
usage: python3 write_composition.py [--apply]
Adds (1) a banner after the title paragraph and (2) one 'final composition' line at the end of each city section the
file has (32 city sections + Amundsen Station). The pool-based derivation tables are kept as the derivation record."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
COMP = HERE.parent / "Upper_Earth_Immigration_Composition.md"
RULING = "DR-85"
BANNER = ("> ⚠ **Update 2026-11-02 (`" + RULING + "`) — READ BEFORE USING ANY CITY TABLE BELOW.** The pool-based derivation in this file "
          "(each nation's Gini-adjusted effective pool and the 8 / 3 / 1 tier shares) is the **starting derivation**. The population "
          "rework of 2026-11-02 wrote every country in its latest-period form (successor states and renamed countries, split by "
          "headcount), reduced and refilled the Sinian Federation's share in the cities it dominated, added places never counted "
          "before, moved founder shares at Ariun Nuur, Utstein and Neumayer, and relabeled tiers from the final shares. **The final "
          "composition of each city is its Specs file's per-nation table and `Official_Population_Census.md` Section A** (names "
          "explained in its Section E). The tier tables below show the derivation as it stood before the rework, old nation names "
          "included, and are kept as the derivation record; each city section ends with a line giving its final composition. "
          "Method and every run: `Sinian_Federation_Split_Scratch_2026-11-01/12_Rebalance_Run4.md`.")


def final_line(city, rows):
    t = {"Primary": [], "Significant": [], "Notable": []}
    for x in rows:
        t[x["tier"]].append(x["nation"])
    return ("**Final composition after the 2026-11-02 rework (`" + RULING + "`):** Primary — " + ", ".join(t["Primary"]) +
            "; Significant — " + ", ".join(t["Significant"]) + "; Notable — " + str(len(t["Notable"])) +
            " nations and smaller successor rows (all of them, with shares and counts, in the city's Specs file). "
            "The pool-based table above is the derivation before the rework.")


def main():
    apply = "--apply" in sys.argv
    data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))["cities"]
    L = COMP.read_text(encoding="utf-8").split("\n")
    if any("Update 2026-11-02" in l for l in L):
        raise SystemExit("already applied")
    heads = [(i, l) for i, l in enumerate(L) if l.startswith("### ") or l.startswith("## ")]
    ins, done = [], set()
    for n, (i, l) in enumerate(heads):
        if not (i < 700):
            continue
        name = None
        for c in data:
            if re.match(r"^#{2,3} " + re.escape(c) + r"( |\*|$)", l) or (c == "Amundsen Station" and l.startswith("## AMUNDSEN STATION")):
                name = c
        if name is None:
            continue
        end = heads[n + 1][0] if n + 1 < len(heads) else len(L)
        k = end
        while k > i and not L[k - 1].strip():
            k -= 1
        if L[k - 1].strip() == "---":
            k -= 1
            while k > i and not L[k - 1].strip():
                k -= 1
        ins.append((k, name))
        done.add(name)
    for k, name in sorted(ins, reverse=True):
        L[k:k] = ["", final_line(name, data[name]["rows"])]
    L[4:4] = ["", BANNER]
    print("sections updated:", len(done), "| without a section in this file:", sorted(set(data) - done))
    if apply:
        COMP.write_text("\n".join(L), encoding="utf-8")
        print("APPLIED")
    else:
        print("dry run")

if __name__ == "__main__":
    main()
