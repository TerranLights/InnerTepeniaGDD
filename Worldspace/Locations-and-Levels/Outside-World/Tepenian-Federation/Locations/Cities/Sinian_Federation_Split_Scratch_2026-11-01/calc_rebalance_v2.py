#!/usr/bin/env python3
"""Second run, 2026-11-01 ~23:40, at the developer's request. SCRATCH: read-only on every repo file except its
own outputs in this folder.

Developer: "go with the proportional fill and use a 4.5% cutoff, use a randomly-generated value between 55-65%
(instead of 55-60), and also calculate for populations from North America (now many countries),
what-was-current-day-Russia (also now many countries), and Argentina, and see what the resulting numbers look like"

Step 1 (the 20 cities with Chinese presence except Zhongshan and Kunlun): China's row -> the Sinian Federation's
        share (Option B, 91.56%) x a random draw in [0.55, 0.65] per city (same seed and order as run 1, so each
        city's draw is 0.55 + 2 x (its run-1 draw - 0.55)). The gap goes PROPORTIONALLY to the city's nations at
        4.5% or more outside its top tier (Concordia: to its other top-tier nations, as in run 1).
Step 2 (every city except Kunlun): the rows of the USA, Canada, Mexico, Russia and Argentina are divided among
        their successor states in proportion to each successor's share of the old country's effective pool
        (Option B, economic size; Russia: RS1b split (a), primary variant). Pure relabeling: nobody else changes.
        Successors drawn from several countries (Cascadia, Sonora, Alaska) are added together.
Check  (order reversed): the splits first, then step 1, so successor rows can receive the fill.

Kunlun is left exactly as it is (its rows are by space-program heritage, and its table changes on 2026-11-02
under Option A). Canada's Neutral Scientific Territory and Greenland pieces (0.08% of Canada's pool together) are
left out and Canada's other successors scaled up to cover them; Canada's Demilitarized Zone keeps its own row
because where its exiles count is still the developer's decision.
"""
import contextlib
import csv
import io
import random
from collections import OrderedDict
from pathlib import Path

import calc_rebalance as v1

HERE = Path(__file__).resolve().parent
SPECS = HERE.parent / "Specs"
SEED = v1.SEED
LINE = 4.5
EXCLUDED = {"Kunlun"}
DECLINE_CITIES = [c for c, _ in v1.CITY_FILES]

LABEL = {
    "The CSA": "CSA", "Appalachia": "Appalachia", "New England": "New England",
    "The People's Democratic Republic of Cascadia": "Cascadia", "The Midwest Republic": "Midwest Republic",
    "Colorado": "Colorado", "La República de Sonora": "Sonora", "The Sovereign Republic of Hawaii": "Hawaii",
    "Alaska": "Alaska", "Demilitarized Zone": "Demilitarized Zone (s. Ontario; not a nation)",
    "Quebec": "Quebec", "The Prairie Federation": "Prairie Federation", "México": "México",
    "La República de Yucatán": "Yucatán", "Argentina": "Argentina (without Patagonia)",
    "Araucanía-Patagonia Autonomous Zone": "Araucanía-Patagonia",
}
LEFT_OUT = {"Neutral Scientific Territory", "Greenland"}

# Russia: RS1b section 6.1, split (a), primary variant V1 · K-out · INIT (W shares, percent)
RUSSIA = [("Russia (core state)", 41.83), ("Idelsk-Uralia", 23.41), ("Siberia", 16.90), ("Künnarantaiga", 8.24),
          ("Donska-Kubania", 7.12), ("Karelia", 0.97), ("Dagestan", 0.61), ("Chechnya", 0.29),
          ("Kabardino-Balkaria", 0.20), ("North Ossetia-Alania", 0.19), ("Karachay-Cherkessia", 0.10),
          ("Tuva", 0.08), ("Ingushetia", 0.06)]


def successor_shares():
    ns = {"__file__": str(HERE / "calc_part2.py"), "__name__": "part2"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec((HERE / "calc_part2.py").read_text(encoding="utf-8"), ns)
    out = {}
    for country in ("USA", "Canada", "Mexico", "Argentina"):
        res = ns["resolved"][country]
        g = OrderedDict()
        for _, s, _, gdp in res:
            if s in LEFT_OUT:
                continue
            g[LABEL[s]] = g.get(LABEL[s], 0.0) + gdp
        tot = sum(g.values())
        out[country] = [(k, 100 * v / tot) for k, v in sorted(g.items(), key=lambda kv: -kv[1])]
    out["Russia"] = RUSSIA
    return out


SPLIT = successor_shares()
SOURCE_OF = {}
for _c, _lst in SPLIT.items():
    for _s, _ in _lst:
        SOURCE_OF.setdefault(_s, []).append(_c)


def copy_rows(rows):
    return [dict(r, counts=list(r["counts"])) for r in rows]


def decline(rows, r, order_b=False):
    """Step 1 on a row list. Returns new rows. Eligible: >= LINE and outside the top tier; successor rows (order B)
    count as outside it. Fallback (nobody eligible): the other rows >= LINE."""
    rows = copy_rows(rows)
    def top(x):
        return x["tier"] == "Primary" and not (order_b and x.get("from"))
    el = [x for x in rows if x["nation"] != "China" and not top(x) and x["share"] >= LINE]
    fallback = False
    if not el:
        el = [x for x in rows if x["nation"] != "China" and x["share"] >= LINE]
        fallback = True
    ch = next(x for x in rows if x["nation"] == "China")
    s_old = ch["share"]
    ch["share"] = s_old * v1.SINIAN_B * r
    w = {x["nation"]: x["share"] for x in el}
    add = v1.distribute(s_old - ch["share"], w, even=False)
    for x in el:
        x["share"] += add[x["nation"]]
    for j in range(len(ch["counts"])):
        c = ch["counts"][j]
        if c is None:
            continue
        newc = round(c * v1.SINIAN_B * r)
        ch["counts"][j] = newc
        add = v1.distribute(c - newc, {x["nation"]: x["counts"][j] for x in el}, even=False)
        for x in el:
            x["counts"][j] += add[x["nation"]]
    ch["nation"] = "Sinian Federation"
    return rows, [x["nation"] for x in el], fallback


def split(rows):
    out = OrderedDict()
    for x in rows:
        if x["nation"] not in SPLIT:
            out[x["nation"]] = dict(x, counts=list(x["counts"]))
            continue
        lst = SPLIT[x["nation"]]
        w = {s: sh for s, sh in lst}
        parts = {s: {"share": x["share"] * sh / 100, "counts": []} for s, sh in lst}
        for c in x["counts"]:
            if c is None:
                for s in parts:
                    parts[s]["counts"].append(None)
                continue
            d = v1.distribute(c, w, even=False)
            for s in parts:
                parts[s]["counts"].append(d[s])
        for s, p in parts.items():
            if s in out:  # a successor drawn from two countries in the same city
                o = out[s]
                o["share"] += p["share"]
                o["counts"] = [(a or 0) + (b or 0) if (a is not None or b is not None) else None
                               for a, b in zip(o["counts"], p["counts"])]
                o["from"] = o["from"] + " + " + x["nation"]
            else:
                out[s] = {"tier": x["tier"], "nation": s, "share": p["share"], "counts": p["counts"],
                          "from": x["nation"]}
    return list(out.values())


def fmt_top(rows, k=5):
    r = sorted(rows, key=lambda x: -x["share"])[:k]
    return ", ".join(f"{x['nation'].replace(' (s. Ontario; not a nation)', '')} {x['share']:.1f}" for x in r)


def lead(rows):
    r = sorted(rows, key=lambda x: -x["share"])
    return r[0], r[0]["share"] / r[1]["share"]


def main():
    rng = random.Random(SEED)
    draws = {c: rng.uniform(0.55, 0.65) for c in DECLINE_CITIES}
    files = sorted(p for p in SPECS.glob("*/*.md") if not p.name.startswith("_"))
    cities = OrderedDict()
    for p in files:
        header, rows = v1.read_table(p)
        name = next((c for c, f in v1.CITY_FILES if (SPECS / f) == p), None)
        if name is None:
            name = p.stem.replace("_", " ").replace("dUrville", "d'Urville").replace("Temirotkel", "Temirötkel")
        cities[name] = (header, rows)

    print("## Successor shares used (Option B: each successor's share of the old country's pool)\n")
    for c, lst in SPLIT.items():
        print(f"- **{c}:** " + " · ".join(f"{s} {sh:.2f}%" for s, sh in lst))
    print("\n## Draws (seed %d, uniform 0.55-0.65, same order as run 1)\n" % SEED)
    print("| City | Draw | Sinian factor (0.9156 × draw) |")
    print("|---|--:|--:|")
    for c in DECLINE_CITIES:
        print(f"| {c} | {draws[c]:.4f} | {v1.SINIAN_B * draws[c]:.4f} |")

    results, csvrows, checks = OrderedDict(), [], []
    for name, (header, rows) in cities.items():
        if name in EXCLUDED:
            continue
        info = {}
        cur = copy_rows(rows)
        if name in draws:
            cur, el, fb = decline(cur, draws[name])
            info.update(el=el, fallback=fb)
            # order B check
            b_rows, b_el, b_fb = decline(split(copy_rows(rows)), draws[name], order_b=True)
            info.update(b_rows=b_rows, b_el=b_el)
        final = split(cur)
        for j in range(len(rows[0]["counts"])):
            before = sum((x["counts"][j] or 0) for x in rows)
            after = sum((x["counts"][j] or 0) for x in final)
            checks.append((name, header[j] if j < len(header) else j, before == after))
        results[name] = (header, rows, final, info)
        for x in final:
            csvrows.append({"city": name, "row": x["nation"], "from": x.get("from", ""), "tier_today": x["tier"],
                            "share_after": f"{x['share']:.3f}",
                            **{h: (x["counts"][j] if j < len(x["counts"]) else "") for j, h in enumerate(header)}})

    bad = [c for c in checks if not c[2]]
    print(f"\n*Every city keeps its exact total in every census column: {'yes' if not bad else 'NO: ' + str(bad)}.*\n")

    print("## Every city, after both steps\n")
    print("| City | China → Sinian Fed. | Leader before | Leader after | Lead after (1st ÷ 2nd) | Top five after (%) |")
    print("|---|---|---|---|--:|---|")
    for name, (header, rows, final, info) in results.items():
        lb, _ = lead(rows)
        la, ratio = lead(final)
        ch = next((x for x in rows if x["nation"] == "China"), None)
        sf = next((x for x in final if x["nation"] in ("Sinian Federation", "China")), None)
        chs = f"{ch['share']:.2f} → {sf['share']:.2f}" if ch else "—"
        print(f"| {name} | {chs} | {lb['nation']} {lb['share']:.2f} | {la['nation']} {la['share']:.2f} | "
              f"{ratio:.2f} | {fmt_top(final)} |")

    # national
    nb, na = {}, {}
    for name, (header, rows, final, info) in results.items():
        hc = v1.human_col(header)
        if hc is None:
            continue
        for x in rows:
            if x["counts"][hc] is not None:
                nb[x["nation"]] = nb.get(x["nation"], 0) + x["counts"][hc]
        for x in final:
            if x["counts"][hc] is not None:
                key = "Sinian Federation" if x["nation"] == "China" else x["nation"]  # Zhongshan's row
                na[key] = na.get(key, 0) + x["counts"][hc]
    tot_b, tot_a = sum(nb.values()), sum(na.values())
    print(f"\n## Nationally (Census I humans, summed from the specs: {tot_b:,} before, {tot_a:,} after)\n")
    print("| Rank | Nation or successor | Humans after | Share of Tepenia | Before (as listed today) |")
    print("|--:|---|--:|--:|---|")
    for i, (n, v) in enumerate(sorted(na.items(), key=lambda kv: -kv[1]), 1):
        if n in nb:
            b = f"{nb[n]:,}"
        elif n == "Sinian Federation":
            zh = next(x for x in cities['Zhongshan'][1] if x['nation'] == 'China')['counts'][1]
            b = f"China {nb['China']:,} (includes Zhongshan's {zh:,}, unchanged)"
        elif n in SOURCE_OF:
            b = "part of " + ", ".join(SOURCE_OF[n])
        else:
            b = "—"
        print(f"| {i} | {n} | {v:,} | {100 * v / tot_a:.2f}% | {b} |")

    # order check
    print("\n## Check: the splits first, then the decline (order reversed)\n")
    print("*Same draws and rules; successor rows count as outside the top tier, so they can receive the fill.*\n")
    print("| City | Receivers, decline first | Receivers, splits first | Leader then | Lead (1st ÷ 2nd) |")
    print("|---|---|---|---|--:|")
    for name, (header, rows, final, info) in results.items():
        if "b_rows" not in info:
            continue
        la, ratio = lead(info["b_rows"])
        print(f"| {name} | {', '.join(info['el'])} | {', '.join(info['b_el'])} | {la['nation']} {la['share']:.2f} | {ratio:.2f} |")

    # per-city detail
    print("\n## City by city (rows under 0.10% are added together by source country; every row is in the CSV)\n")
    for name, (header, rows, final, info) in results.items():
        hc = v1.human_col(header)
        print(f"### {name}\n")
        if info:
            note = f"draw {draws[name]:.4f}; fill to: {', '.join(info['el'])}"
            if info.get("fallback"):
                note += " (FALLBACK: nobody outside the top tier reaches 4.5%)"
            print(f"*{note}*\n")
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
            line = f"| {x['tier']} | {x['nation']} | {x.get('from', '') or ('China' if x['nation'] == 'Sinian Federation' else '')} | {bs} | {x['share']:.2f}% |"
            if hc is not None:
                line += f" {x['counts'][hc]:,} |" if x["counts"][hc] is not None else " |"
            print(line)
        for src, (k, sh, h) in small.items():
            line = f"| | *{k} smaller {src} successor{'' if k == 1 else 's'}* | {src} | — | {sh:.2f}% |"
            if hc is not None:
                line += f" {h:,} |"
            print(line)
        moved = [f"{n} {before[n]:.2f}%" for n in before if n in SPLIT]
        if moved:
            print(f"\n*Split today's: {', '.join(moved)} (after step 1 where it received fill).*")
        print()

    out = HERE / "09_city_tables.csv"
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
