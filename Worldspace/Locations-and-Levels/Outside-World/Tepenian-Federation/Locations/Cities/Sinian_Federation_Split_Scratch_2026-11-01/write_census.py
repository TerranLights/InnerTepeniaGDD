#!/usr/bin/env python3
"""Write the final tables into Official_Population_Census.md. 2026-11-02.
usage: python3 write_census.py [--apply]
  1. Section A: the three tier rows of every city (38; Relung Panen gets the entry it never had).
  2. Section B: the National Origin Totals table (humans, Census I), rebuilt from the final city tables.
  3. Section E (new, before the closing lines): the successor-name key.
"""
import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CENSUS = HERE.parent / "Official_Population_Census.md"
sys.path.insert(0, str(HERE))
from write_specs import tier_lines  # noqa: E402

OLD_NAME = {"Juan Carlos": "Pergamino", "Port Lockroy": "Puerto Abrigo", "Sejong": "Contrapunto", "Abowasa": "Santa Luce",
            "Princess Elisabeth": "Utstein", "Sayowa": "Temirötkel", "Vostok": "Ariun Nuur"}
MARITIME = 11_205
RULING = "DR-85"

SECTION_B_NOTE = (
    "***Rebuilt 2026-11-02 (`" + RULING + "`)*** — *superseding every version above and the table below as it stood. "
    "Every nation is now written in its latest-period form (successor states and renamed countries; names are explained in "
    "Section E), and the humans are the sum of each city's final per-nation table in its Specs file, Census I human column. "
    "New places were added (Taiwan, Hong Kong, Macau, today's Mongolia, North Korea, Luxembourg, Kosovo, Austria, Petén), "
    "Jeju-do's people count as Korea's, and the Sinian Federation's share in the cities where it was reduced was refilled by "
    "the other nations. Every city's total is unchanged, so the grand total equals the sum of the city rows plus the maritime "
    "fleet. The earlier table is in git commit `593510ab`.*")


def build_national(data):
    tot = collections.Counter()
    for city, d in data["cities"].items():
        for r in d["rows"]:
            c = r["counts"][1] if len(r["counts"]) > 1 else None
            if c:
                tot[r["nation"]] += c
    return tot


def national_table(tot, maritime=MARITIME):
    items = sorted(tot.items(), key=lambda kv: (-kv[1], kv[0]))
    items.append(("*Maritime fleet (no nation assigned)*", maritime))
    grand = sum(v for _, v in items)
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    out = ["| Nation | Human Exiles | | Nation | Human Exiles |", "|--------|-------------|---|--------|-------------|"]
    for i in range(half):
        a = f"| {left[i][0]} | {left[i][1]:,} |"
        if i < len(right):
            b = f" | {right[i][0]} | {right[i][1]:,} |"
        elif i == len(right):
            b = f" | **TOTAL** | **{grand:,}** |"
        else:
            b = " |  |  |"
        out.append(a + b)
    if len(right) == half:  # the right column is full: the total needs its own line
        out.append("|  |  | | **TOTAL** | **%s** |" % f"{grand:,}")
    return out, grand


def section_e(data):
    bysrc = collections.defaultdict(set)
    for city, d in data["cities"].items():
        for r in d["rows"]:
            for t in [s.strip() for s in r["from"].split("+") if s.strip()]:
                bysrc[t].add(r["nation"])
    order = ["China", "Hong Kong", "Macau", "Mongolia", "Taiwan", "South Korea", "North Korea", "Jeju-do", "USA", "Canada",
             "Mexico", "Petén", "Russia", "Ukraine", "Argentina", "Chile", "Italy", "Germany", "Austria", "Belgium", "Luxembourg",
             "UK", "Spain", "Brazil", "Indonesia", "Thailand", "Romania", "Kosovo", "Czech Republic"]
    L = ["## Section E — Successor-country names in the per-nation tables (added 2026-11-02, `" + RULING + "`)", "",
         "*The per-nation tables in the Specs files and the national totals above write every country in its latest-period form "
         "(the world atlas's latest period). A country that split is written as its successor states, each taking its share of "
         "the old country's people (headcount; the pools already carry the income adjustment). A country that was renamed is "
         "written under its new name. Rows under 0.10% of a city are listed individually in the Specs files.*", "",
         "| Old name or place | Rows that carry its people now |", "|---|---|"]
    for k in order:
        if k in bysrc:
            L.append(f"| {k} | {', '.join(sorted(bysrc[k]))} |")
    for k in sorted(bysrc):
        if k not in order:
            L.append(f"| {k} | {', '.join(sorted(bysrc[k]))} |")
    L += ["", "**Notes on specific rows:**",
          "- **Sinian Federation:** China's nine Han states, with Hong Kong and Macau; it is the same row the old \"China\" held, "
          "in the cities that listed one. Manchuria, Mongolia (with Inner Mongolia), East Turkestan and Tibet are placed only in "
          "the cities inside their time-zone windows; elsewhere their share stays with the Sinian Federation. Taiwan is a separate "
          "nation.",
          "- **Korea:** South Korea and North Korea. Jeju-do is the International Court of Diplomacy's neutral ground and nobody "
          "comes from it (developer, 2026-11-02): its people count as Korea's.",
          "- **Demilitarized Zone (s. Ontario; not a nation):** Canada's former southern-Ontario territory. Its treatment is "
          "**still open** (developer, 2026-11-02: to be decided).",
          "- **Sicilia (autonomous zone within Meridia):** listed on its own as the atlas lists it.",
          "- **Neutral Scientific Territory:** no one is from it, so it has no row (developer, 2026-11-01).",
          "- **Kunlun's heritage rows** (USA, Russia, Canada, UK, Italy, Germany, South Korea, Argentina, Intermarium/Intermaria) "
          "keep their old names, because Kunlun's rows follow space-program heritage and not headcount; which successor carries "
          "which program is still to be decided.",
          "- **Where the numbers come from:** `Sinian_Federation_Split_Scratch_2026-11-01/` (file `12_Rebalance_Run4.md`, the research "
          "in `Run4_Research/`, and `apply_final.py` for the last changes).", "", "---", ""]
    return L


def main():
    apply = "--apply" in sys.argv
    data = json.loads((HERE / "final_tables.json").read_text(encoding="utf-8"))
    from apply_final import SPEC_PATH  # noqa: F401
    txt = CENSUS.read_text(encoding="utf-8")
    if "Section E — Successor-country names" in txt:
        raise SystemExit("already applied")
    L = txt.split("\n")
    # ---- Section A
    done = set()
    i = 0
    a_end = next(k for k, l in enumerate(L) if l.startswith("## Section B"))
    cur = None
    kun_note = None
    while i < a_end:
        m = re.match(r"^\*\*([^*]+)\*\*", L[i])
        if m and not L[i].startswith("**Tier"):
            nm = m.group(1).strip()
            cur = OLD_NAME.get(nm, nm)
        if re.match(r"^\| *Tier *\| *Nations *\|", L[i]) and cur in data["cities"]:
            rows = data["cities"][cur]["rows"]
            assert L[i + 2].startswith("| Primary |") and L[i + 3].startswith("| Significant |") and L[i + 4].startswith("| Notable |"), cur
            L[i + 2:i + 5] = tier_lines(rows)
            done.add(cur)
            if cur == "Kunlun":
                kun_note = i
        i += 1
    # Relung Panen's missing entry, after Kunlun's block
    rp = data["cities"]["Relung Panen"]["rows"]
    j = kun_note
    while not L[j].startswith("---"):
        j += 1
    entry = ["---", "", "**Relung Panen** *(Bunger Hills oasis, Knox Coast — the 38th city, populated 2026-09-05; entry added to this "
             "section 2026-11-02, `" + RULING + "`)*", "", "| Tier | Nations |", "|------|---------|"] + tier_lines(rp) + [
        "", "*Note: Relung Panen's population and its Census I and II figures are in Sections B and C; its full per-nation table "
        "is in `Specs/Mirny subnet/Relung_Panen.md`.*", ""]
    L[j:j] = entry
    missing = set(data["cities"]) - done
    assert missing == {"Relung Panen"}, missing
    # ---- Section B national table
    b = next(k for k, l in enumerate(L) if l.startswith("| Nation | Human Exiles |"))
    e = b
    while L[e].startswith("|"):
        e += 1
    tot = build_national(data)
    tbl, grand = national_table(tot)
    expected = 15_623_523
    assert grand == expected, (grand, expected)
    L[b:e] = [SECTION_B_NOTE, ""] + tbl
    # ---- Section E before the closing lines
    k = next(n for n, l in enumerate(L) if l.startswith("*End of record.*"))
    k = max(n for n in range(k) if L[n].startswith("---"))
    L[k:k] = section_e(data)
    if apply:
        CENSUS.write_text("\n".join(L), encoding="utf-8")
    print("national total", f"{grand:,}", "nations", len(tot), "APPLIED" if apply else "dry run")


if __name__ == "__main__":
    main()
