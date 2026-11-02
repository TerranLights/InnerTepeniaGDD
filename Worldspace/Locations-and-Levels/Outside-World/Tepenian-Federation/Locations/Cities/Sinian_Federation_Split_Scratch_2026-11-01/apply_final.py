#!/usr/bin/env python3
"""Final tables for the official files (2026-11-02, ~09:30). Reads ONLY the frozen run 4 output
(`12_city_tables.csv`) and the old specs as they stand in git commit 593510ab (for annotations). Writes
`final_tables.json` and prints a report. Does not touch any official file.

Developer's rulings applied here (2026-11-02 morning):
  1. Run 4's numbers are applied ("the population numbers are actually supported and realistic").
  2. Neumayer is handled like Ariun Nuur and Utstein: shares move from the leader (France) to the two Register
     founders (the Netherlands, Austro-Bavaria). Range chosen by Claude: [1.5, 3.5] points each, the Nordic range,
     because the founders already hold about 3% (Ariun Nuur's and Utstein's founders started near zero). The seed is
     fixed BEFORE the draw is seen (date + hour): 2026110209.
  3. Jeju-do's people count as Korea's ("nobody would actually come from Jeju-Do").
  4. Tiers are relabeled mechanically (rule below). Kunlun keeps its Option A tiers (8 / 3 / 1 shares).
  5. Kunlun's heritage rows (old names) stay as run 4 left them, pending the developer's approval of a list.
  6. NOT applied: any decline to China's four pieces or to Taiwan (the developer's answer did not settle it).

TIER RULE (the composition file's own rule, "boundaries fall at the largest ratio gaps", adapted to final shares):
  Primary = the first i rows (by share), i from 1 to the number of rows at 4.5% or more (the developer's line) but
  never more than 6 (the most any city had before: Concordia), chosen where the ratio between row i and row i+1 is
  largest (ties: the smaller i).
  Significant = the next rows, through the LATER of (a) the last row at 4.5% or more and (b) the largest ratio gap
  among the rows at 1% or more. So no community at 4.5% or more is ever Notable.
  Notable = everything else.
"""
import csv
import json
import random
import re
import subprocess
from collections import OrderedDict, defaultdict
from pathlib import Path

import calc_rebalance_v2 as v2
import calc_rebalance_v3 as v3

HERE = Path(__file__).resolve().parent
CITIES_DIR = HERE.parent
REPO = Path(subprocess.run(["git", "-C", str(HERE), "rev-parse", "--show-toplevel"], capture_output=True).stdout.decode().strip())
NEUMAYER_SEED = 2026110209
BASE_REF = "593510ab"
LINE = 4.5
FOUNDERS = {
    "Ariun Nuur": ["Mongolia", "Künnarantaiga"],
    "Utstein": ["Iceland", "Norway", "Sweden", "Finland", "Denmark"],
    "Neumayer": ["Netherlands", "Austro-Bavaria"],
    "Kunlun": ["Mongolia", "Künnarantaiga", "Sinian Federation"],
}
SPEC_PATH = {  # city -> spec path under Specs/
    "Amundsen Station": "Amundsen-Scott subnet/Amundsen_Station.md", "Byrd": "Byrd subnet/Byrd.md",
    "Belgrano": "Halley subnet/Belgrano.md", "Halley": "Halley subnet/Halley.md", "Lazar": "Halley subnet/Lazar.md",
    "Neumayer": "Halley subnet/Neumayer.md", "Sanay": "Halley subnet/Sanay.md", "Santa Luce": "Halley subnet/Santa_Luce.md",
    "Troll": "Halley subnet/Troll.md", "Utstein": "Halley subnet/Utstein.md", "Cape Adare": "Janbogo subnet/Cape_Adare.md",
    "Concordia": "Janbogo subnet/Concordia.md", "Denison": "Janbogo subnet/Denison.md",
    "Dumont d'Urville": "Janbogo subnet/Dumont_dUrville.md", "Fort McMurdo": "Janbogo subnet/Fort_McMurdo.md",
    "Janbogo": "Janbogo subnet/Janbogo.md", "Scott": "Janbogo subnet/Scott.md", "Zukelli": "Janbogo subnet/Zukelli.md",
    "Dome Fuji": "Mawson subnet/Dome_Fuji.md", "Mawson": "Mawson subnet/Mawson.md", "Temirötkel": "Mawson subnet/Temirotkel.md",
    "Ariun Nuur": "Mirny subnet/Ariun_Nuur.md", "Casey": "Mirny subnet/Casey.md", "Davis": "Mirny subnet/Davis.md",
    "Kunlun": "Mirny subnet/Kunlun.md", "Mirny": "Mirny subnet/Mirny.md", "Relung Panen": "Mirny subnet/Relung_Panen.md",
    "Shirayuki": "Mirny subnet/Shirayuki.md", "Sinheung": "Mirny subnet/Sinheung.md", "Zhongshan": "Mirny subnet/Zhongshan.md",
    "Contrapunto": "Palmer subnet/Contrapunto.md", "Esperanza": "Palmer subnet/Esperanza.md", "Marambio": "Palmer subnet/Marambio.md",
    "Palmer City": "Palmer subnet/Palmer_City.md", "Pergamino": "Palmer subnet/Pergamino.md",
    "Puerto Abrigo": "Palmer subnet/Puerto_Abrigo.md", "Rothera": "Palmer subnet/Rothera.md", "Signy": "Palmer subnet/Signy.md",
}
ANNO_RENAME = {"China": "Sinian Federation", "South Korea": "Korea", "Argentina": "Argentina (without Patagonia)",
               "Mexico": "México"}
ANNO_KEEP = re.compile(r"founding wave|heritage|route advantage|gateway|Hobart|diplomatic allocation|earliest", re.I)
JEJU = "Jeju-do (neutral zone)"


def load_csv():
    cities = OrderedDict()
    cols = {}
    for r in csv.DictReader(open(HERE / "12_city_tables.csv", encoding="utf-8")):
        names = [k for k in r if k.startswith("Census")]
        cols[r["city"]] = names
        counts = [int(r[k]) if r[k] != "" else None for k in names]
        cities.setdefault(r["city"], []).append({"tier": r["tier"], "nation": r["row"], "share": float(r["share_after"]),
                                                  "counts": counts, "from": r["from"]})
    return cities, cols


def merge_jeju(rows):
    j = next((x for x in rows if x["nation"] == JEJU), None)
    if j is None:
        return rows
    k = next(x for x in rows if x["nation"] == "Korea")
    k["share"] += j["share"]
    k["counts"] = [(a or 0) + (b or 0) if (a is not None or b is not None) else None for a, b in zip(k["counts"], j["counts"])]
    k["from"] = (k["from"] + " + Jeju-do").strip(" +")
    return [x for x in rows if x is not j]


def split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def old_annotations(city):
    txt = subprocess.run(["git", "-C", str(REPO), "show", f"{BASE_REF}:Worldspace/Locations-and-Levels/Outside-World/"
                          f"Tepenian-Federation/Locations/Cities/Specs/{SPEC_PATH[city]}"], capture_output=True).stdout.decode("utf-8")
    anno = {}
    for ln in txt.split("\n"):
        m = re.match(r"^\| (Primary|Significant|Notable) \| (.*?) \|$", ln)
        if m and "%" not in ln:
            for item in split_top(m.group(2)):
                mm = re.match(r"^(.*?)\s*\*\((.*)\)\*\.?$", item, re.S)
                if mm:
                    anno[mm.group(1).strip()] = mm.group(2).strip()
        m = re.match(r"^\| (Primary|Significant|Notable) \| ([^|]*?)\s*\*\((.*?)\)\* \| [0-9.]+% \|", ln)
        if m:
            anno[m.group(2).strip()] = m.group(3).strip()
    out = {}
    for n, t in anno.items():
        if "diplomatic allocation" in t:
            t = "founding population — Jeju-do diplomatic allocation"
        elif not ANNO_KEEP.search(t):
            continue
        out[ANNO_RENAME.get(n, n)] = t
    return out


def header_targets(city):
    """The city's own census numbers from its spec header, as [CI robots, CI humans, CII robots, CII humans] (None where absent)."""
    txt = subprocess.run(["git", "-C", str(REPO), "show", f"{BASE_REF}:Worldspace/Locations-and-Levels/Outside-World/"
                          f"Tepenian-Federation/Locations/Cities/Specs/{SPEC_PATH[city]}"], capture_output=True).stdout.decode("utf-8")
    m = re.search(r"\*\*Census I[^:]*:\*\* ([\d,]+) humans / ([\d,]+) robots", txt)
    m2 = re.search(r"\*\*Census II[^:]*:\*\* ([\d,]+) humans / ([\d,]+) robots", txt)
    f = lambda g: int(g.replace(",", ""))
    return [f(m.group(2)) if m else None, f(m.group(1)) if m else None,
            f(m2.group(2)) if m2 else None, f(m2.group(1)) if m2 else None]


def make_exact(city, order, log):
    """The old tables carried a few individuals of rounding drift against the spec header (documented tolerance).
    Make each column sum EXACTLY to the header: the difference is spread one person at a time over the largest rows."""
    tg = header_targets(city)
    if city == "Kunlun":
        tg = [135_226, None, None, None]
    for j, t in enumerate(tg):
        if t is None or j >= len(order[0]["counts"]) or order[0]["counts"][j] is None:
            continue
        diff = t - sum((x["counts"][j] or 0) for x in order)
        if diff == 0:
            continue
        log.append((city, j, diff))
        step = 1 if diff > 0 else -1
        k = 0
        big = [x for x in order if x["counts"][j] and x["counts"][j] > 50]
        for _ in range(abs(diff)):
            big[k % len(big)]["counts"][j] += step
            k += 1


def relabel(rows):
    order = sorted(rows, key=lambda x: -x["share"])
    n = len(order)
    k1 = max(1, sum(1 for x in order if x["share"] >= LINE))
    best_i, best = 1, -1.0
    for i in range(1, min(k1, 6, n - 1) + 1):
        r = order[i - 1]["share"] / order[i]["share"]
        if r > best + 1e-12:
            best, best_i = r, i
    k2 = sum(1 for x in order if x["share"] >= 1.0)
    end_gap, best2 = best_i, -1.0
    for e in range(best_i + 1, min(k2, n - 1) + 1):  # e = number of rows through the end of Significant
        r = order[e - 1]["share"] / order[e]["share"]
        if r > best2 + 1e-12:
            best2, end_gap = r, e
    end_sig = max(end_gap, min(k1, n), best_i)
    for idx, x in enumerate(order):
        x["tier"] = "Primary" if idx < best_i else ("Significant" if idx < end_sig else "Notable")
    return order


def main():
    cities, cols = load_csv()
    out = OrderedDict()
    report = []
    exact_log = []
    # Neumayer draws
    rng = random.Random(NEUMAYER_SEED)
    neu = [("Netherlands", rng.uniform(1.5, 3.5)), ("Austro-Bavaria", rng.uniform(1.5, 3.5))]
    for city, rows in cities.items():
        rows = [dict(x, counts=list(x["counts"])) for x in rows]
        rows = merge_jeju(rows)
        if city == "Neumayer":
            rows = v3.move_from(rows, "France", neu)
        if city == "Kunlun":
            order = sorted(rows, key=lambda x: -x["share"])
            for x in order:
                x["tier"] = x["tier"].replace(" (founding wave)", "")
        else:
            order = relabel(rows)
        make_exact(city, order, exact_log)
        anno = old_annotations(city)
        for n in FOUNDERS.get(city, []):
            anno.setdefault(n, "founding wave")
        for x in order:
            x["anno"] = anno.get(x["nation"], "")
        out[city] = {"cols": cols[city], "rows": order}
        tiers = defaultdict(list)
        for x in order:
            tiers[x["tier"]].append(x["nation"])
        report.append((city, len(order), {t: len(v) for t, v in tiers.items()}, order[0], order[1], tiers))
    # checks against run 4's totals
    for city, d in out.items():
        orig = cities[city]
        tg = [135_226, None, None, None] if city == "Kunlun" else header_targets(city)
        for j in range(len(d["cols"])):
            a = sum((x["counts"][j] or 0) for x in d["rows"])
            b = sum((x["counts"][j] or 0) for x in orig)
            if tg[j] is not None and orig[0]["counts"][j] is not None:
                assert a == tg[j], (city, j, a, tg[j])
            else:
                assert a == b, (city, j, a, b)
        assert abs(sum(x["share"] for x in d["rows"]) - sum(x["share"] for x in orig)) < 0.02, city
        assert all((c or 0) >= 0 for x in d["rows"] for c in x["counts"]), city
    (HERE / "final_tables.json").write_text(json.dumps({"neumayer_draws": neu, "cities": out}, ensure_ascii=False, indent=1),
                                            encoding="utf-8")
    print("Neumayer draws (points moved from France):", [(n, round(v, 4)) for n, v in neu])
    print("Made exact against the spec header (city, column 0=CI robots 1=CI humans 2=CII robots 3=CII humans, difference in people):", exact_log)
    print("All totals check against the spec headers. Rows per city, tier sizes, leader and runner-up:\n")
    for city, n, sizes, a, b, tiers in report:
        print(f"{city:18s} rows {n:3d}  P/S/N {sizes.get('Primary', 0)}/{sizes.get('Significant', 0)}/{sizes.get('Notable', 0)}"
              f"  lead {a['nation']} {a['share']:.2f} / {b['nation']} {b['share']:.2f}")
    print()
    for city, d in out.items():
        print(city, {x["nation"]: x["anno"] for x in d["rows"] if x["anno"]})


if __name__ == "__main__":
    main()
