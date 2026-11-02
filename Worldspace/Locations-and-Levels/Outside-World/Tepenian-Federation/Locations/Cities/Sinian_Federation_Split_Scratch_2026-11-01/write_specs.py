#!/usr/bin/env python3
"""Write the final tables (final_tables.json) into the 38 specs. 2026-11-02.
usage: python3 write_specs.py [--apply]     (dry run without --apply)

In each spec it replaces (1) the three tier rows, (2) the per-nation table rows, (3) the standard boilerplate notes
around that table; a spec whose notes are custom keeps them, with a line saying they describe the earlier table.
Nothing else in the spec is touched. Not idempotent on purpose: it refuses to run on a spec that already carries
the 2026-11-02 marker.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPECS = HERE.parent / "Specs"
MARK = "Rebalanced 2026-11-02"
RULING = "DR-85"

PRE_NEW = ("*(Rebalanced 2026-11-02 in the population rework, `" + RULING + "`: every country appears in its latest-period "
           "form (successor states and renamed countries, split by headcount, names explained in `Official_Population_Census.md` "
           "Section E); China's row is the Sinian Federation, with its decline and the refill of the gap where the rework "
           "applies it; places never counted before were added by time-zone window; tiers were relabeled from the final shares. "
           "{city}City totals in all four columns are unchanged. Method, every run and the research: "
           "`Sinian_Federation_Split_Scratch_2026-11-01/` (file `12_Rebalance_Run4.md`). The table that stood here before is in "
           "git commit `593510ab`.)*")
HIST_PRE = "*The note below describes the earlier table (2026-07 to 2026-10) and is kept as history; the table is the current one.*"
HIST_POST = "*The note that follows describes the earlier table (2026-07 to 2026-10) and is kept as history.*"
POST_NEW = ("*Tier labels follow the final shares: Primary and Significant end at the largest ratio gaps among the rows at 4.5% "
            "or more (Primary never more than six rows), no row at 4.5% or more is Notable, and Notable is the rest (the "
            "composition file's own rule, \"boundaries fall at the largest ratio gaps\"; the 8 / 3 / 1 share weights no longer "
            "produce the figures). Percentages are of this city's own {pop} population (identical between censuses), not "
            "Tepenia-wide. {robots}Shares are rounded; they sum to 100% within rounding.*")
STD_PRE_START = "*(De-stacked 2026-07-05"
STD_POST_START = "*Figures use the project's standard share-weighting methodology as a baseline"


def city_notes():
    txt = (HERE / "12_Rebalance_Run4.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^#### (.+)\n\n\*(.+)\*\n", txt, re.M):
        out[m.group(1).strip()] = m.group(2)
    return out


def build_detail(city, raw, neu):
    parts = []
    if city == "Zhongshan":
        parts.append("Zhongshan is exempt from the Sinian Federation's decline and from new places, as ruled: only the names and splits changed. ")
    if city == "Kunlun":
        parts.append("Kunlun follows Option A: the Sinian Federation alone in the top tier; the USA and Russia in the middle tier; Mongolia and Künnarantaiga added to the middle tier as the founding wave. The other rows keep their space-program heritage names. ")
    if raw:
        raw = raw.replace("Sinian draw ", "the Sinian Federation's share was multiplied by ")
        raw = raw.replace("; fill to: ", " (random 0.55 to 0.65), and the freed points went in proportion to size to: ")
        raw = raw.replace("from Japan: ", "founder shares moved from Japan (points of the city): ")
        raw = raw.replace(" · ", "; ")
        parts.append("This city: " + raw[0].lower() + raw[1:] + ". ")
    if city == "Neumayer":
        parts.append("This city: founder shares moved from France (points of the city, random 1.5 to 3.5 each, seed 2026110209): "
                     + ", ".join(f"{n} {v:.2f}" for n, v in neu) + ". ")
    if city == "Neumayer" or city in ("Utstein", "Ariun Nuur"):
        parts.append("The founders are the Register's. ")
    return "".join(parts)


def fmt_share(s):
    return f"{s:.2f}%" if s >= 0.1 else f"{s:.3f}%"


def tier_lines(rows):
    out = []
    for t in ("Primary", "Significant", "Notable"):
        names = []
        for x in rows:
            if x["tier"] == t:
                names.append(x["nation"] + (f" *({x['anno']})*" if x["anno"] else ""))
        out.append(f"| {t} | {', '.join(names)} |")
    return out


def table_rows(rows, ncols):
    out = []
    for x in rows:
        cells = []
        for c in x["counts"][:ncols]:
            cells.append(f"{c:,}" if c is not None else "*(N/A)*")
        nm = x["nation"] + (f" *({x['anno']})*" if x["anno"] else "")
        out.append(f"| {x['tier']} | {nm} | {fmt_share(x['share'])} | " + " | ".join(cells) + " |")
    return out


def main():
    apply = "--apply" in sys.argv
    data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
    neu = data["neumayer_draws"]
    notes = city_notes()
    sys.path.insert(0, str(HERE))
    from apply_final import SPEC_PATH
    changed = []
    for city, d in data["cities"].items():
        p = SPECS / SPEC_PATH[city]
        L = p.read_text(encoding="utf-8").split("\n")
        if any(MARK in l for l in L):
            raise SystemExit(f"{p.name}: already carries the marker; refusing")
        rows = d["rows"]
        t = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nations *\|", l))
        assert L[t + 2].startswith("| Primary |") and L[t + 3].startswith("| Significant |") and L[t + 4].startswith("| Notable |"), (city, "tier rows")
        h = next(i for i, l in enumerate(L) if re.match(r"^\| *Tier *\| *Nation *\|", l))
        ncols = len([c for c in L[h].strip().strip("|").split("|")]) - 3
        j = h + 2
        while j < len(L) and L[j].startswith("|"):
            j += 1
        ph = max(i for i in range(h) if L[i].startswith("### Per-Nation"))
        robots_only = ncols == 1
        pre_idx = next((i for i in range(ph + 1, h) if L[i].strip()), None)
        post_idx = next(i for i in range(j, len(L)) if L[i].strip())
        if pre_idx is None:
            print("NO PRE-NOTE:", city, "heading L%d table L%d" % (ph + 1, h + 1))
            pre_idx = h
        detail = build_detail(city, notes.get(city), neu)
        pre_std = pre_idx == h or (L[pre_idx].startswith(STD_PRE_START)
                                   and len([1 for i in range(ph + 1, h) if L[i].strip()]) == 1)
        post_std = L[post_idx].startswith(STD_POST_START) and len(L[post_idx]) < 700
        pre_text = PRE_NEW.format(city=detail)
        post_text = POST_NEW.format(pop="robot" if robots_only else "human and robot",
                                    robots="" if robots_only else "Robot figures apply the same proportions as the human population. ")
        new = L[:t + 2]
        new += tier_lines(rows)
        new += L[t + 5:ph + 1]
        # lines between heading and table
        mid = L[ph + 1:h]
        if pre_std:
            mid = ["", pre_text, ""]
        else:
            mid = ["", pre_text, "", HIST_PRE] + mid
        new += mid
        new += L[h:h + 2]
        new += table_rows(rows, ncols)
        tail = L[j:]
        if post_std:
            k = post_idx - j
            tail = tail[:k] + [post_text] + tail[k + 1:]
        else:
            tail = tail[:post_idx - j] + [post_text, "", HIST_POST] + tail[post_idx - j:]
        new += tail
        changed.append((city, len(L), len(new)))
        if apply:
            p.write_text("\n".join(new), encoding="utf-8")
    for c, a, b in changed:
        print(f"{c:18s} {a:4d} -> {b:4d} lines ({b - a:+d})")
    print("APPLIED" if apply else "dry run (nothing written)")


if __name__ == "__main__":
    main()
