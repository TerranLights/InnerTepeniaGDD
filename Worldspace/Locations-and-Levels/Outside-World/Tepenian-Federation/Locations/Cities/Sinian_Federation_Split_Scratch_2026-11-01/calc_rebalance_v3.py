#!/usr/bin/env python3
"""Run 3, 2026-11-01 ~23:40 onward, with the developer's answers to run 2. SCRATCH: read-only on every repo file
except its own outputs in this folder.

Developer's answers (verbatim in 10_Rebalance_Run3.md):
  1. Split each country "in proportion to its share of the old country" (the pool split; kept).
  2. Ariun Nuur: two random values in [3.5, 5.0] points come off Japan; the higher goes to Mongolia, the lower to
     Künnarantaiga.
     Utstein: from Japan, a random [0.5, 1.0] to Iceland and a random [1.5, 3.5] each to Norway, Sweden, Finland
     and Denmark.
     Esperanza: left as it is.
  3-4. Japan and South Korea as the largest communities, and Sanay: left as they are.
  5. Splits first, then the decline.

Order: (1) every city except Kunlun: the USA, Canada, Mexico, Russia and Argentina rows divided among their
successors (run 2's shares); (2) the 20 cities with Chinese presence except Zhongshan and Kunlun: China -> the
Sinian Federation x run 2's draw, the gap filled in proportion to size by rows at 4.5% or more outside the top
tier, successor rows included; (3) the founder adjustments at Ariun Nuur and Utstein, in points of the city's
population, applied to every census column (largest-remainder rounding keeps each column's total).
"""
import csv
import random
from collections import OrderedDict
from pathlib import Path

import calc_rebalance as v1
import calc_rebalance_v2 as v2

HERE = Path(__file__).resolve().parent
SPECS = HERE.parent / "Specs"
FOUNDER_SEED = 2026110123  # first founder stream (date + hour); Utstein's draws still come from it
# Ariun Nuur redrawn at the developer's request (~23:43): its first draw (3.5114 / 3.5107 from FOUNDER_SEED) left
# Mongolia and Künnarantaiga equal in effect. Its own seed, fixed BEFORE the redraw was seen (date + 23:43);
# Utstein's values are unchanged because its stream still skips the first two numbers of FOUNDER_SEED.
ARIUN_SEED = 202611012343

FOUNDER_TIER = "Founder (new row)"


def founder_draws():
    rng_a = random.Random(ARIUN_SEED)
    a, b = rng_a.uniform(3.5, 5.0), rng_a.uniform(3.5, 5.0)
    ariun = [("Mongolia", max(a, b)), ("Künnarantaiga", min(a, b))]
    rng = random.Random(FOUNDER_SEED)
    rng.random(), rng.random()  # the two numbers Ariun Nuur's first draw used
    utstein = [("Iceland", rng.uniform(0.5, 1.0))]
    for n in ("Norway", "Sweden", "Finland", "Denmark"):
        utstein.append((n, rng.uniform(1.5, 3.5)))
    return {"Ariun Nuur": ariun, "Utstein": utstein}


def move_from(rows, donor, gifts):
    """Move points of the city from the donor row to the named rows (created if missing), every column."""
    rows = v2.copy_rows(rows)
    by = {x["nation"]: x for x in rows}
    d = by[donor]
    ncols = len(d["counts"])
    for n, _ in gifts:
        if n not in by:
            by[n] = {"tier": FOUNDER_TIER, "nation": n, "share": 0.0, "counts": [0 if c is not None else None for c in d["counts"]]}
            rows.append(by[n])
    for n, v in gifts:
        d["share"] -= v
        by[n]["share"] += v
    for j in range(ncols):
        if d["counts"][j] is None:
            continue
        total = sum((x["counts"][j] or 0) for x in rows)
        want = {n: total * v / 100 for n, v in gifts}
        moved = v1.distribute(round(sum(want.values())), want, even=False)
        for n, _ in gifts:
            d["counts"][j] -= moved[n]
            by[n]["counts"][j] += moved[n]
    return rows


def main():
    rng = random.Random(v1.SEED)
    draws = {c: rng.uniform(0.55, 0.65) for c in v2.DECLINE_CITIES}
    gifts = founder_draws()

    files = sorted(p for p in SPECS.glob("*/*.md") if not p.name.startswith("_"))
    cities = OrderedDict()
    for p in files:
        header, rows = v1.read_table(p)
        name = next((c for c, f in v1.CITY_FILES if (SPECS / f) == p), None)
        if name is None:
            name = p.stem.replace("_", " ").replace("dUrville", "d'Urville").replace("Temirotkel", "Temirötkel")
        cities[name] = (header, rows)

    print("## The founder draws (seeds: Ariun Nuur %d, Utstein %d)\n" % (ARIUN_SEED, FOUNDER_SEED))
    print("| City | Row | Points moved from Japan |")
    print("|---|---|--:|")
    for c, lst in gifts.items():
        for n, v in lst:
            print(f"| {c} | {n} | {v:.2f} |")
        print(f"| {c} | **Japan, total moved** | **{sum(v for _, v in lst):.2f}** |")

    results, csvrows, bad = OrderedDict(), [], []
    for name, (header, rows) in cities.items():
        if name in v2.EXCLUDED:
            continue
        cur = v2.split(v2.copy_rows(rows))
        el = []
        if name in draws:
            cur, el, _ = v2.decline(cur, draws[name], order_b=True)
        if name in gifts:
            cur = move_from(cur, "Japan", gifts[name])
        for j in range(len(rows[0]["counts"])):
            if sum((x["counts"][j] or 0) for x in rows) != sum((x["counts"][j] or 0) for x in cur):
                bad.append((name, j))
        if any((c or 0) < 0 for x in cur for c in x["counts"]):
            bad.append((name, "negative"))
        results[name] = (header, rows, cur, el)
        for x in cur:
            csvrows.append({"city": name, "row": x["nation"], "from": x.get("from", ""), "tier_today": x["tier"],
                            "share_after": f"{x['share']:.3f}",
                            **{h: (x["counts"][j] if j < len(x["counts"]) else "") for j, h in enumerate(header)}})
    print(f"\n*Every city keeps its exact total in every census column, and no count is negative: "
          f"{'yes' if not bad else 'NO: ' + str(bad)}.*\n")

    print("## Every city, after all three steps\n")
    print("| City | China → Sinian Fed. | Leader before | Leader after | Lead after (1st ÷ 2nd) | Top five after (%) |")
    print("|---|---|---|---|--:|---|")
    for name, (header, rows, final, el) in results.items():
        lb, _ = v2.lead(rows)
        la, ratio = v2.lead(final)
        ch = next((x for x in rows if x["nation"] == "China"), None)
        sf = next((x for x in final if x["nation"] in ("Sinian Federation", "China")), None)
        chs = f"{ch['share']:.2f} → {sf['share']:.2f}" if ch else "—"
        print(f"| {name} | {chs} | {lb['nation']} {lb['share']:.2f} | {la['nation']} {la['share']:.2f} | "
              f"{ratio:.2f} | {v2.fmt_top(final)} |")

    # national
    nb, na = {}, {}
    for name, (header, rows, final, el) in results.items():
        hc = v1.human_col(header)
        if hc is None:
            continue
        for x in rows:
            if x["counts"][hc] is not None:
                nb[x["nation"]] = nb.get(x["nation"], 0) + x["counts"][hc]
        for x in final:
            if x["counts"][hc] is not None:
                key = "Sinian Federation" if x["nation"] == "China" else x["nation"]
                na[key] = na.get(key, 0) + x["counts"][hc]
    tot = sum(na.values())
    print(f"\n## Nationally (Census I humans, {tot:,} in the specs)\n")
    print("| Rank | Nation or successor | Humans after | Share | Before (as listed today) |")
    print("|--:|---|--:|--:|---|")
    for i, (n, v) in enumerate(sorted(na.items(), key=lambda kv: -kv[1]), 1):
        if n in nb:
            b = f"{nb[n]:,}"
        elif n == "Sinian Federation":
            b = f"China {nb['China']:,}"
        elif n in v2.SOURCE_OF:
            b = "part of " + ", ".join(v2.SOURCE_OF[n])
        else:
            b = "new row"
        print(f"| {i} | {n} | {v:,} | {100 * v / tot:.2f}% | {b} |")

    print("\n## City by city (rows under 0.10% added together by source country; every row is in the CSV)\n")
    for name, (header, rows, final, el) in results.items():
        hc = v1.human_col(header)
        print(f"### {name}\n")
        notes = []
        if name in draws:
            notes.append(f"Sinian draw {draws[name]:.4f}; fill to: {', '.join(el)}")
        if name in gifts:
            notes.append("from Japan: " + ", ".join(f"{n} {v:.2f}" for n, v in gifts[name]))
        if notes:
            print("*" + " · ".join(notes) + "*\n")
        before = {x["nation"]: x["share"] for x in rows}
        print("| Tier today | Row | From | Before | After |" + (" Census I humans after |" if hc is not None else ""))
        print("|---|---|---|--:|--:|" + ("--:|" if hc is not None else ""))
        small = {}
        for x in sorted(final, key=lambda x: -x["share"]):
            if x.get("from") and x["share"] < 0.10:
                s = small.setdefault(x["from"], [0, 0.0, 0])
                s[0] += 1
                s[1] += x["share"]
                s[2] += (x["counts"][hc] or 0) if hc is not None else 0
                continue
            b = before.get(x["nation"], before.get("China") if x["nation"] == "Sinian Federation" else None)
            bs = f"{b:.2f}%" if b is not None and not x.get("from") else "—"
            src = x.get("from", "") or ("China" if x["nation"] == "Sinian Federation" else "")
            line = f"| {x['tier']} | {x['nation']} | {src} | {bs} | {x['share']:.2f}% |"
            if hc is not None:
                line += f" {x['counts'][hc]:,} |" if x["counts"][hc] is not None else " |"
            print(line)
        for src, (k, sh, h) in small.items():
            line = f"| | *{k} smaller {src} successor{'' if k == 1 else 's'}* | {src} | — | {sh:.2f}% |"
            if hc is not None:
                line += f" {h:,} |"
            print(line)
        print()

    out = HERE / "10_city_tables.csv"
    keys = []
    for r in csvrows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(csvrows)
    print(f"*Every row, every census column: `{out.name}`.*")


if __name__ == "__main__":
    main()
