#!/usr/bin/env python3
"""Overnight scratch run, 2026-11-01 ~23:00, at the developer's request. READ-ONLY on every repo file except
its own outputs in this scratch folder.

Developer's instruction (verbatim in 08_Sinian_Decline_Rebalance.md):
  1. Start from the Sinian Federation's share of China after the territorial split (file 03).
  2. For every city with Chinese presence except Zhongshan and Kunlun, the Sinian figure becomes a random
     55-60% of that.
  3. The difference is filled by the city's nations that are less represented but above 5%, so the city keeps
     its previous total.
  4. Then judge whether each adjustment can reasonably be justified.

Choices made here (each stated in file 08):
  * Territorial step: Option B (economic size, the Sinian Federation's share of China's 2024 regional product,
    91.56%); Option A (headcount, 89.42%) is printed as a check.
  * The 55-60% draw is made once per city (seeded, so the run is repeatable).
  * "Less represented" = not in the city's top (Primary) tier. ALT: the literal "below China's share".
  * The fill is split EVENLY among the eligible nations (headline); PROPORTIONAL to their present size is the
    alternative. Integer counts use largest-remainder rounding so every column keeps its exact total.
"""
import csv
import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
CITIES_DIR = HERE.parent
SPECS = CITIES_DIR / "Specs"
CENSUS = CITIES_DIR / "Official_Population_Census.md"
COMP = CITIES_DIR / "Upper_Earth_Immigration_Composition.md"

SEED = 20261101
SINIAN_B = 1227248.4 / 1340312.8      # file 03: Sinian share of the 31 provinces' 2024 GRP
SINIAN_A = 1257460000 / 1406280000    # file 03: Sinian share of the 31 provinces' 2024 year-end population
THRESHOLD = 5.00

# Order fixes the random draws; do not reorder.
CITY_FILES = [
    ("Dumont d'Urville", "Janbogo subnet/Dumont_dUrville.md"),
    ("Mirny", "Mirny subnet/Mirny.md"),
    ("Zukelli", "Janbogo subnet/Zukelli.md"),
    ("Relung Panen", "Mirny subnet/Relung_Panen.md"),
    ("Janbogo", "Janbogo subnet/Janbogo.md"),
    ("Davis", "Mirny subnet/Davis.md"),
    ("Temirötkel", "Mawson subnet/Temirotkel.md"),
    ("Mawson", "Mawson subnet/Mawson.md"),
    ("Denison", "Janbogo subnet/Denison.md"),
    ("Cape Adare", "Janbogo subnet/Cape_Adare.md"),
    ("Scott", "Janbogo subnet/Scott.md"),
    ("Fort McMurdo", "Janbogo subnet/Fort_McMurdo.md"),
    ("Amundsen Station", "Amundsen-Scott subnet/Amundsen_Station.md"),
    ("Casey", "Mirny subnet/Casey.md"),
    ("Dome Fuji", "Mawson subnet/Dome_Fuji.md"),
    ("Sinheung", "Mirny subnet/Sinheung.md"),
    ("Concordia", "Janbogo subnet/Concordia.md"),
    ("Shirayuki", "Mirny subnet/Shirayuki.md"),
    ("Byrd", "Byrd subnet/Byrd.md"),
    ("Palmer City", "Palmer subnet/Palmer_City.md"),
]

# Founders from Founding_Register.md (nations that have a row in the city's table, or are named there)
FOUNDERS = {
    "Dumont d'Urville": ["Japan"], "Mirny": ["(Idelsk-Uralia, no row)"], "Zukelli": ["Australia"],
    "Relung Panen": ["Indonesia", "Malaysia"], "Janbogo": ["South Korea"], "Davis": ["Australia"],
    "Temirötkel": ["(Kazakhstan, no row)", "(the CIN members, all Notable)"],
    "Mawson": ["Australia", "(Kazakhstan, no row)", "(Russia, no row)"], "Denison": ["Australia"],
    "Cape Adare": [], "Scott": ["New Zealand"], "Fort McMurdo": [], "Amundsen Station": [],
    "Casey": ["Australia"], "Dome Fuji": [], "Sinheung": ["South Korea"], "Concordia": [],
    "Shirayuki": ["Japan"], "Byrd": [], "Palmer City": [],
}

ROW = re.compile(r"^\|\s*(Primary|Significant|Notable)[^|]*\|\s*([^|]+?)\s*\|\s*([0-9]+\.[0-9]+)\s*%\s*\|(.*)$")


def read_table(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks, cur, header = [], [], None
    for i, ln in enumerate(lines):
        m = ROW.match(ln)
        if m:
            if not cur:
                header = [c.strip() for c in lines[i - 2].strip().strip("|").split("|")][3:]
            tier, nation, share, rest = m.groups()
            nation = re.sub(r"\*.*?\*|\(.*?\)", "", nation).strip()
            cells = [c.strip().replace(",", "") for c in rest.strip().strip("|").split("|")]
            counts = [int(c) if c.isdigit() else None for c in cells]
            cur.append({"tier": tier, "nation": nation, "share": float(share), "counts": counts})
        elif cur:
            blocks.append((header, cur))
            cur = []
    if cur:
        blocks.append((header, cur))
    for header, b in blocks:
        if abs(sum(r["share"] for r in b) - 100) < 1.5:
            return header, b
    raise ValueError(path)


def distribute(total, weights, even):
    """Split an integer (or float) total among keys. even=True: equal parts; else proportional to weights.
    Integers use largest remainder (ties to the larger weight)."""
    keys = list(weights)
    if not keys:
        return {}
    raw = {k: (total / len(keys) if even else total * weights[k] / sum(weights.values())) for k in keys}
    if isinstance(total, float):
        return raw
    base = {k: int(raw[k] // 1) for k in keys}
    left = total - sum(base.values())
    order = sorted(keys, key=lambda k: (-(raw[k] - base[k]), -weights[k]))
    for k in order[:left]:
        base[k] += 1
    return base


def eligible(rows, rule, threshold=THRESHOLD):
    china = next(r for r in rows if r["nation"] == "China")
    if rule == "not-top-tier":
        el = [r for r in rows if r["nation"] != "China" and r["tier"] != "Primary" and r["share"] >= threshold]
    else:  # literal
        el = [r for r in rows if r["nation"] != "China" and threshold <= r["share"] < china["share"]]
    return [r["nation"] for r in el]


def run_city(rows, frac, r, el, even):
    """Returns new shares and new count columns."""
    shares = {x["nation"]: x["share"] for x in rows}
    s_c = shares["China"]
    s_new = s_c * frac * r
    out_sh = dict(shares)
    out_sh["China"] = s_new
    add = distribute(s_c - s_new, {n: shares[n] for n in el}, even)
    for n, v in add.items():
        out_sh[n] += v
    ncols = len(rows[0]["counts"])
    out_ct = {x["nation"]: list(x["counts"]) for x in rows}
    for j in range(ncols):
        c = out_ct["China"][j]
        if c is None:
            continue
        newc = round(c * frac * r)
        out_ct["China"][j] = newc
        add = distribute(c - newc, {n: next(x for x in rows if x["nation"] == n)["counts"][j] for n in el}, even)
        for n, v in add.items():
            out_ct[n][j] += v
    return out_sh, out_ct


def read_census_nations():
    txt = CENSUS.read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(txt) if l.startswith("| Nation | Human Exiles |"))
    nat = {}
    for l in txt[start + 2:start + 30]:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        for k in (0, 3):
            if k + 1 < len(cells) and re.fullmatch(r"[0-9,]+", cells[k + 1] or ""):
                nat[cells[k]] = int(cells[k + 1].replace(",", ""))
    return nat


def read_pools():
    pools = {}
    for ln in COMP.read_text(encoding="utf-8").splitlines()[66:111]:
        m = re.match(r"^\|\s*([A-Za-z .]+?)\s*\|\s*~([0-9.]+)M\s*\|", ln)
        if m:
            pools[m.group(1)] = float(m.group(2))
    return pools


def human_col(header):
    for j, h in enumerate(header):
        if h.lower().startswith("census i humans"):
            return j
    return None


def main():
    rng = random.Random(SEED)
    draws = {c: rng.uniform(0.55, 0.60) for c, _ in CITY_FILES}
    data = {c: read_table(SPECS / f) for c, f in CITY_FILES}

    print("## Random draws (seed %d, uniform 0.55-0.60, one per city, in table order)\n" % SEED)
    print("| City | Draw | Sinian factor (0.9156 x draw) | Option A check (0.8942 x draw) |")
    print("|---|--:|--:|--:|")
    for c, _ in CITY_FILES:
        print(f"| {c} | {draws[c]:.4f} | {SINIAN_B * draws[c]:.4f} | {SINIAN_A * draws[c]:.4f} |")

    summary, csv_rows = [], []
    nat_delta = {"even": {}, "prop": {}}
    for c, _ in CITY_FILES:
        header, rows = data[c]
        el = eligible(rows, "not-top-tier")
        fallback = False
        if not el:  # Concordia: no non-top-tier nation reaches 5%
            el = [r["nation"] for r in rows if r["nation"] != "China" and r["share"] >= THRESHOLD]
            fallback = True
        lit = eligible(rows, "literal")
        res = {}
        for mode in ("even", "prop"):
            res[mode] = run_city(rows, SINIAN_B, draws[c], el, mode == "even")
        hc = human_col(header)
        before = {x["nation"]: x["share"] for x in rows}
        for mode in ("even", "prop"):
            sh, ct = res[mode]
            if hc is not None:
                for x in rows:
                    n = x["nation"]
                    if x["counts"][hc] is not None:
                        nat_delta[mode][n] = nat_delta[mode].get(n, 0) + ct[n][hc] - x["counts"][hc]
        summary.append((c, header, rows, el, lit, fallback, res, before))
        for x in rows:
            n = x["nation"]
            for mode in ("even", "prop"):
                sh, ct = res[mode]
                csv_rows.append({"city": c, "fill": mode, "tier_today": x["tier"], "nation": n,
                                 "share_before": f"{x['share']:.2f}", "share_after": f"{sh[n]:.2f}",
                                 **{f"before:{h}": (x["counts"][j] if j < len(x["counts"]) else "")
                                    for j, h in enumerate(header)},
                                 **{f"after:{h}": (ct[n][j] if j < len(ct[n]) else "")
                                    for j, h in enumerate(header)}})

    # ---------- per-city tables ----------
    print("\n## City by city (shares; headline = even fill)\n")
    for c, header, rows, el, lit, fallback, res, before in summary:
        sh_e, ct_e = res["even"]
        sh_p, _ = res["prop"]
        hc = human_col(header)
        print(f"### {c}\n")
        notes = [f"draw {draws[c]:.4f}", f"Sinian factor {SINIAN_B * draws[c]:.4f}",
                 f"fill goes to: {', '.join(el)}" + (" (FALLBACK: no nation outside the top tier reaches 5%)" if fallback else "")]
        if set(lit) != set(el):
            notes.append(f"literal reading (below China and at least 5%) would give: {', '.join(lit) if lit else 'nobody'}")
        bord = [f"{x['nation']} {x['share']:.2f}%" for x in rows if 4.5 <= x["share"] < THRESHOLD and x["nation"] != "China"]
        if bord:
            notes.append("just under the line, so left as is: " + ", ".join(bord))
        print("*" + " · ".join(notes) + "*\n")
        cols = "| Tier today | Nation | Before | After (even) | Change | After (proportional) |"
        if hc is not None:
            cols += " Census I humans before | after (even) |"
        print(cols)
        print("|---|---|--:|--:|--:|--:|" + ("--:|--:|" if hc is not None else ""))
        order = sorted(rows, key=lambda x: -sh_e[x["nation"]])
        for x in order:
            n = x["nation"]
            label = "Sinian Federation (was China)" if n == "China" else n
            mark = " ★" if n in el else ""
            line = (f"| {x['tier']} | {label}{mark} | {before[n]:.2f}% | {sh_e[n]:.2f}% | {sh_e[n] - before[n]:+.2f} | "
                    f"{sh_p[n]:.2f}% |")
            if hc is not None:
                line += f" {x['counts'][hc]:,} | {ct_e[n][hc]:,} |" if x["counts"][hc] is not None else " | |"
            print(line)
        # column totals check
        ok = all(sum((ct_e[x['nation']][j] or 0) for x in rows) == sum((x['counts'][j] or 0) for x in rows)
                 for j in range(len(rows[0]["counts"])))
        print(f"\n*Column totals unchanged: {'yes' if ok else 'NO'}.  ★ = receives the fill.*\n")

    # ---------- summary ----------
    print("## Summary (even fill)\n")
    print("| City | China before | Sinian after | Leader before | Leader after | Lead after (1st ÷ 2nd) | Founders: before → after |")
    print("|---|--:|--:|---|---|--:|---|")
    for c, header, rows, el, lit, fallback, res, before in summary:
        sh_e, _ = res["even"]
        rb = sorted(before, key=lambda n: -before[n])
        ra = sorted(sh_e, key=lambda n: -sh_e[n])
        nm = lambda n: "Sinian Fed." if n == "China" else n
        f = []
        for fd in FOUNDERS[c]:
            if fd in before:
                f.append(f"{fd} {before[fd]:.2f} → {sh_e[fd]:.2f}")
            else:
                f.append(fd)
        print(f"| {c} | {before['China']:.2f}% | {sh_e['China']:.2f}% | {nm(rb[0])} {before[rb[0]]:.2f}% | "
              f"{nm(ra[0])} {sh_e[ra[0]]:.2f}% | {sh_e[ra[0]] / sh_e[ra[1]]:.2f} | {'; '.join(f) if f else '—'} |")

    # ---------- national ----------
    nat = read_census_nations()
    pools = read_pools()
    tot = 15_623_523
    print("\n## Nationally (Census I humans; the census table plus this run's changes)\n")
    print("| Nation | Before | After (even) | Change | After (proportional) | Before ÷ (2% of pool) | After (even) ÷ (2% of pool) |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    names = sorted(set(nat_delta["even"]) | set(nat_delta["prop"]), key=lambda n: -(nat_delta["even"].get(n, 0)))
    for n in names:
        if nat_delta["even"].get(n, 0) == 0 and nat_delta["prop"].get(n, 0) == 0:
            continue
        b = nat.get(n)
        if b is None:
            continue
        ae = b + nat_delta["even"].get(n, 0)
        ap = b + nat_delta["prop"].get(n, 0)
        p = pools.get(n)
        r1 = f"{b / (0.02 * p * 1e6):.2f}" if p else "—"
        r2 = f"{ae / (0.02 * p * 1e6):.2f}" if p else "—"
        label = "China → Sinian Federation (Zhongshan unchanged)" if n == "China" else n
        print(f"| {label} | {b:,} | {ae:,} | {ae - b:+,} | {ap:,} | {r1} | {r2} |")
    print(f"\n*Tepenia's human total is unchanged ({tot:,}): every city keeps its size.*")

    # ---------- variant: the line at 4.5% ("about 5%") ----------
    print("\n## Variant: the line at 4.5% (\"about 5%\"), even fill\n")
    print("*Only the cities where the 4.5% line adds a nation are listed; the Sinian figure is the same as above.*\n")
    print("| City | Added at 4.5% | Its share: before → after (5% line) → after (4.5% line) | Other recipients' gain: 5% line → 4.5% line |")
    print("|---|---|---|--:|")
    for c, header, rows, el, lit, fallback, res, before in summary:
        if fallback:
            continue
        el45 = eligible(rows, "not-top-tier", 4.5)
        extra = [n for n in el45 if n not in el]
        if not extra:
            continue
        sh45, _ = run_city(rows, SINIAN_B, draws[c], el45, True)
        sh5 = res["even"][0]
        g5 = sh5[el[0]] - before[el[0]]
        g45 = sh45[el[0]] - before[el[0]]
        cells = "; ".join(f"{n} {before[n]:.2f} → {sh5[n]:.2f} → {sh45[n]:.2f}" for n in extra)
        print(f"| {c} | {', '.join(extra)} | {cells} | +{g5:.2f} → +{g45:.2f} |")

    # ---------- illustration: the USA row split among its successors ----------
    # Option B shares of the USA's pool (06_Part2_Results.md, share of GDP). ILLUSTRATION ONLY: assumes every
    # successor reaches the city in proportion to its pool (no time-zone window applied; those rulings are open).
    usa_succ = [("CSA", 28.91), ("Appalachia", 19.64), ("New England", 19.51), ("Cascadia (US part)", 17.96),
                ("Midwest Republic", 6.14), ("Colorado", 4.75), ("Sonora (US part)", 2.45), ("Hawaii", 0.41),
                ("Alaska", 0.22)]
    print("\n## Illustration: the China-and-USA cities once the USA's row is also split (even fill)\n")
    print("*Assumes every American successor reaches the city in proportion to its share of the USA's pool "
          "(Option B); the time-zone window and the split rulings are not applied.*\n")
    print("| City | USA after this run | Largest American successor (CSA) | Leader then | Lead then (1st ÷ 2nd) |")
    print("|---|--:|--:|---|--:|")
    for c, header, rows, el, lit, fallback, res, before in summary:
        if c not in ("Dumont d'Urville", "Zukelli", "Janbogo", "Denison", "Cape Adare", "Scott",
                     "Fort McMurdo", "Amundsen Station", "Casey"):
            continue
        sh_e = dict(res["even"][0])
        usa = sh_e.pop("USA")
        for n, w in usa_succ:
            sh_e[n] = usa * w / 100
        ra = sorted(sh_e, key=lambda n: -sh_e[n])
        nm = lambda n: "Sinian Fed." if n == "China" else n
        print(f"| {c} | {usa:.2f}% | {usa * 0.2891:.2f}% | {nm(ra[0])} {sh_e[ra[0]]:.2f}% | {sh_e[ra[0]] / sh_e[ra[1]]:.2f} |")

    out = HERE / "08_rebalance_city_tables.csv"
    keys = []
    for r in csv_rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(csv_rows)
    print(f"\n*Full count tables (every column, both fills): `{out.name}`.*")


if __name__ == "__main__":
    main()
