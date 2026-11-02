#!/usr/bin/env python3
"""Run 4, 2026-11-02 overnight, with the developer's decisions of ~00:00 (file 11). SCRATCH: read-only on every
repo file except its own outputs in this folder.

Decisions applied:
  * HEADCOUNT for every split (the pools already carry the income and inequality adjustment).
  * Every country name mapped to the latest period of the developer's atlas (file 11, section 2).
  * China's breakaway pieces placed by the time-zone window; Hong Kong, Macau, Taiwan, today's Mongolia and the
    other places never counted (Austria, Guatemala's Petén, North Korea, Luxembourg, Kosovo) get pools and are
    placed by the window too.
  * Then, as in run 3: the Sinian Federation's decline (same draws, 0.55-0.65), the gap filled in proportion to
    size by rows at 4.5% or more outside the top tier; the founder moves at Ariun Nuur and Utstein (same draws);
    Kunlun's Option A with Mongolia and Künnarantaiga in its middle tier.
  * Concordia, Dome Fuji, Relung Panen and Amundsen Station included (developer: commit their numbers).

Method choices (stated in 12_Rebalance_Run4.md; each is one place in this file):
  M1 Order: (1) splits and renames; (2) China's row -> the Sinian Federation plus the pieces inside their windows
     (a piece outside its window leaves its slice with the Sinian Federation); (3) new pools placed by window;
     (4) decline and fill; (5) founder moves; (6) Kunlun.
  M2 A successor keeps its source row's top-tier status only if it keeps at least half of that row (Korea from
     South Korea does; no USA successor does), for the fill's "outside the top tier" test.
  M3 A new pool's humans = 2% of its pool (the census's governing exile rate). They go to the cities in its window
     as one equal percentage of each city (every census column), the city's other rows scaling down to make room.
     A piece that belongs to an existing nation (Hong Kong and Macau to the Sinian Federation, North Korea to
     Korea, Luxembourg to France, Kosovo to Serbia, Austria to Austro-Bavaria, Petén to Yucatán) goes only to
     window cities where that nation already has a row. Taiwan and today's Mongolia may open new rows.
  M4 New pools are estimated from each place's people x the pool-per-person ratio of the three existing nations
     nearest to it in GDP per person (log scale) and Gini (k-nearest neighbors on the 43 nations).
  M5 Zhongshan and Kunlun: exempt from the decline and from new entrants; their China row is relabeled the Sinian
     Federation whole. Kunlun's rows are by space-program heritage and are not split (flagged).
"""
import contextlib
import unicodedata
import csv
import io
import math
import os
import random
import re
from collections import OrderedDict
from pathlib import Path

import calc_rebalance as v1
import calc_rebalance_v2 as v2
import calc_rebalance_v3 as v3

HERE = Path(__file__).resolve().parent
RES = Path(os.environ.get("RUN4_RESEARCH_DIR", str(HERE / "Run4_Research")))
SPECS = HERE.parent / "Specs"
COMP = HERE.parent / "Upper_Earth_Immigration_Composition.md"

LINE = 4.5
EXILE_RATE = 0.02
EXEMPT = {"Zhongshan", "Kunlun"}
POLE = {"Amundsen Station"}

# Solar UTC of each city, from Founding_Register.md (Amundsen Station: the Pole, every zone)
CITY_UTC = {"Palmer City": -4, "Rothera": -5, "Esperanza": -4, "Marambio": -4, "Pergamino": -4, "Puerto Abrigo": -4,
            "Contrapunto": -4, "Signy": -3, "Halley": -2, "Neumayer": -1, "Troll": 0, "Santa Luce": -1, "Sanay": 0,
            "Utstein": 2, "Lazar": 1, "Belgrano": -2, "Mawson": 4, "Temirötkel": 3, "Dome Fuji": 3, "Mirny": 6,
            "Casey": 7, "Davis": 5, "Zhongshan": 5, "Shirayuki": 5, "Sinheung": 5, "Ariun Nuur": 7, "Kunlun": 5,
            "Relung Panen": 7, "Janbogo": 11, "Zukelli": 11, "Cape Adare": 11, "Fort McMurdo": 11, "Scott": 11,
            "Dumont d'Urville": 9, "Denison": 10, "Concordia": 8, "Byrd": -8}


def in_window(city, zones):
    if city in POLE:
        return True
    u = CITY_UTC[city]
    return min(min(abs(u - z), 24 - abs(u - z)) for z in zones) <= 3


# ----------------------------------------------------------------------------------------------- splits
LABEL4 = dict(v2.LABEL)
LABEL4.update({"Sicilia (autonomous zone within Meridia)": "Sicilia (autonomous zone within Meridia)"})


def part2_headcount():
    ns = {"__file__": str(HERE / "calc_part2.py"), "__name__": "part2"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec((HERE / "calc_part2.py").read_text(encoding="utf-8"), ns)
    out = {}
    for country in ("USA", "Canada", "Mexico", "Argentina", "Italy", "Germany"):
        g = OrderedDict()
        for _, s, pop, _ in ns["resolved"][country]:
            if s in v2.LEFT_OUT:
                continue
            lab = LABEL4.get(s, s)
            g[lab] = g.get(lab, 0.0) + pop
        out[country] = g
    return out


def china_headcount():
    g = OrderedDict()
    for r in csv.DictReader(open(HERE / "02_unit_data.csv", encoding="utf-8")):
        if r["in_china_official_figures"] != "yes" or r["successor"] == "(not assigned)":
            continue
        g[r["successor"]] = g.get(r["successor"], 0.0) + float(r["pop_yearend_2024_10k"]) * 10_000
    return g


# RS1b section 5.1 populations (2021), latest map (C-15): Republic of Karelia to Finland, Murmansk to Idelsk-Uralia
RUSSIA_POP = OrderedDict([
    ("Russia (core state)", 45_053_162), ("Idelsk-Uralia", 44_387_883 + 667_744), ("Siberia", 17_909_856),
    ("Donska-Kubania", 17_171_585), ("Künnarantaiga", 10_345_864), ("Dagestan", 3_182_054),
    ("Chechnya", 1_510_824), ("Kabardino-Balkaria", 904_200), ("North Ossetia-Alania", 687_357),
    ("Finland", 533_121), ("Ingushetia", 509_541), ("Karachay-Cherkessia", 469_865), ("Tuva", 336_651)])

# Unit B: which units go to which successor (keywords matched case-insensitively against the CSV's unit names);
# whatever is left of the country total stays with the continuing state (the last element).
B_SPEC = {
    "Belgium": ([("flemish", "Netherlands"), ("flanders", "Netherlands"), ("walloon", "France"), ("wallonia", "France"),
                 ("brussels", "France")], None),
    "United Kingdom": ([("northern ireland", "Northern Ireland")], "United Kingdom"),
    "Spain": ([("catalonia", "Catalonia"), ("catalunya", "Catalonia"), ("cataluna", "Catalonia"),
               ("alava", "Basque Country"), ("araba", "Basque Country"), ("biscay", "Basque Country"),
               ("bizkaia", "Basque Country"), ("vizcaya", "Basque Country"), ("gipuzkoa", "Basque Country"),
               ("guipuzcoa", "Basque Country"), ("navarre", "Basque Country"), ("navarra", "Basque Country"),
               ("trevino", "Basque Country"), ("villaverde", "Basque Country")], "Spain"),
    "Brazil": ([("acre", "Amazonia"), ("amapa", "Amazonia"), ("amazonas", "Amazonia"), ("mato grosso", "Amazonia"),
                ("para", "Amazonia"), ("rondonia", "Amazonia"), ("roraima", "Amazonia")], "Brazil"),
    "Indonesia": ([("aceh", "Aceh"), ("papua", "West Papua")], "Indonesia"),
    "Thailand": ([("pattani", "Patani"), ("yala", "Patani"), ("narathiwat", "Patani")], "Thailand"),
    "Romania": ([("satu mare", "Hungary"), ("bihor", "Hungary"), ("salaj", "Hungary"), ("maramures", "Hungary"),
                 ("arad", "Hungary")], "Romania"),
    "South Korea": ([("jeju", "Jeju-do (neutral zone)")], "Korea"),
    "Chile": ([("araucania", "Araucanía-Patagonia"), ("los rios", "Araucanía-Patagonia"),
               ("los lagos", "Araucanía-Patagonia"), ("aysen", "Araucanía-Patagonia"), ("aisen", "Araucanía-Patagonia"),
               ("magallanes", "Araucanía-Patagonia")], "Chile"),
    "Ukraine": ([("luhansk", "Russia (core state)"), ("donetsk", "Russia (core state)"),
                 ("kharkiv", "Russia (core state)"), ("dnipropetrovsk", "Russia (core state)"),
                 ("zaporizhzhia", "Russia (core state)"), ("kherson", "Russia (core state)")], "Ukraine"),
}
# Kherson's left bank, when the research gives no figure: RS1b's 34.04% (the developer's area-weighted guess, 2001)
KHERSON_LEFT_BANK_SHARE = 0.3404


def norm(t):
    return "".join(ch for ch in unicodedata.normalize("NFKD", t) if not unicodedata.combining(ch)).lower()


B_COUNTRY_ALIASES = {"UK": "United Kingdom", "Korea": "South Korea"}
# Where Unit B gave two vintages, use one whole set (never mix): Brazil's latest official estimate; Thailand's
# 2025 census preliminary (the registration set lacks Yala's exact figure).
B_DATE = {"Brazil": "2026-07-01", "Thailand": "2025-04-01"}
# Gaps Unit B could not fill, filled by the orchestrator (logged as UNVERIFIED):
JEJU_FALLBACK = 672_252  # k-calc.com, "2024", claims MOIS resident registration; no official page reached
PETEN_FALLBACK = 640_151  # INE Guatemala 2023 projection via citypopulation.de (file 11, section 3)
TABLE_NAME = {"United Kingdom": "UK"}  # the name the city tables use, where it differs


def b_headcount(log):
    rows = list(csv.DictReader(open(RES / "B_split_headcounts.csv", encoding="utf-8")))
    by = {}
    for r in rows:
        c = B_COUNTRY_ALIASES.get(r["country"].strip(), r["country"].strip())
        by.setdefault(c, []).append(r)
    out = {}
    for country, (rules, cont) in B_SPEC.items():
        rs = by.get(country, [])
        if country in B_DATE:
            rs = [r for r in rs if r["date"].strip() == B_DATE[country]]
        if country == "South Korea":
            for r in rs:
                if "jeju" in norm(r["unit"]) and not r["population"].strip():
                    r["population"] = str(JEJU_FALLBACK)
                    log.append(f"Unit B South Korea: Jeju blank; used {JEJU_FALLBACK:,} (k-calc.com, UNVERIFIED)")
        total = next((float(r["population"]) for r in rs if r["is_country_total"].strip().lower() == "yes"), None)
        g = OrderedDict()
        used = []
        left_bank = [r for r in rs if "kherson" in norm(r["unit"]) and ("left" in norm(r["unit"]) or "east" in norm(r["unit"]))
                     and r["population"].strip()]
        for r in rs:
            if r["is_country_total"].strip().lower() == "yes" or not r["population"].strip():
                continue
            name = norm(r["unit"])
            if "mato grosso do sul" in name or "german-speaking" in name or "german speaking" in name:
                continue
            pop = float(r["population"])
            if country == "Ukraine" and "kherson" in name:
                if left_bank and r not in left_bank:
                    continue
                if not left_bank:
                    pop *= KHERSON_LEFT_BANK_SHARE
                    log.append(f"Unit B Ukraine: no left-bank Kherson figure; used {KHERSON_LEFT_BANK_SHARE:.2%} of "
                               f"{float(r['population']):,.0f} (RS1b, the developer's area-weighted guess)")
            for kw, succ in rules:
                if re.search(r"\b" + kw + r"\b", name):
                    g[succ] = g.get(succ, 0.0) + pop
                    used.append(r["unit"])
                    break
        if total is None:
            log.append(f"Unit B: no country total for {country}; split skipped")
            continue
        if cont is not None:
            g[cont] = total - sum(g.values())
        out[country] = g
        log.append(f"Unit B {country}: total {total:,.0f}; units used: {', '.join(used)}")
    return out


def all_splits(log):
    sp = {}
    for c, g in part2_headcount().items():
        sp[c] = g
    sp["Russia"] = RUSSIA_POP
    for c, g in b_headcount(log).items():
        sp[TABLE_NAME.get(c, c)] = g
    sp = {c: [(s, v / sum(g.values())) for s, v in g.items()] for c, g in sp.items()}
    sp["Czech Republic"] = [("Czechia", 1.0)]
    return sp


def apply_splits(rows, splits):
    """Every row of a split country divided among its successors (headcount), merged by name with any existing
    row. A successor keeps the source row's top tier only if it keeps at least half of it (M2)."""
    out = OrderedDict()

    def add(name, tier, share, counts, src):
        if name not in out:
            out[name] = {"tier": tier, "nation": name, "share": 0.0,
                         "counts": [None if c is None else 0 for c in counts], "from": src}
        o = out[name]
        o["share"] += share
        o["counts"] = [None if (a is None and b is None) else (a or 0) + (b or 0) for a, b in zip(o["counts"], counts)]
        if src and src not in (o.get("from") or ""):
            o["from"] = (o.get("from") + " + " if o.get("from") else "") + src
        if tier == "Primary":
            o["tier"] = "Primary"

    for x in rows:
        if x["nation"] not in splits:
            add(x["nation"], x["tier"], x["share"], x["counts"], "")
            continue
        lst = splits[x["nation"]]
        w = {s: f for s, f in lst}
        counts = {s: [] for s, _ in lst}
        for c in x["counts"]:
            d = v1.distribute(c, w, even=False) if c is not None else {s: None for s in w}
            for s in w:
                counts[s].append(d[s])
        for s, f in lst:
            tier = x["tier"] if (x["tier"] != "Primary" or f >= 0.5) else "Significant (successor)"
            add(s, tier, x["share"] * f, counts[s], x["nation"] if (s != x["nation"]) else "")
    return list(out.values())


# ----------------------------------------------------------------------------------------------- China's pieces
PIECE_ZONES = {"Manchuria": [8, 9], "Mongolia": [7, 8], "East Turkestan": [5, 6], "Tibet": [6]}


def split_china(city, rows, ch_shares):
    rows = v2.copy_rows(rows)
    ch = next((x for x in rows if x["nation"] == "China"), None)
    if ch is None:
        return rows, []
    if city in EXEMPT:
        ch["nation"] = "Sinian Federation"
        return rows, []
    inw = {p: f for p, f in ch_shares.items() if p in PIECE_ZONES and in_window(city, PIECE_ZONES[p])}
    w = {"Sinian Federation": 1.0 - sum(inw.values()), **inw}
    parts = {n: [] for n in w}
    for c in ch["counts"]:
        d = v1.distribute(c, w, even=False) if c is not None else {n: None for n in w}
        for n in w:
            parts[n].append(d[n])
    rows.remove(ch)
    by = {x["nation"]: x for x in rows}
    for n, f in w.items():
        if n in by:  # e.g. Mongolia's founder row at Ariun Nuur (no China row there, so not reached)
            o = by[n]
            o["share"] += ch["share"] * f
            o["counts"] = [(a or 0) + (b or 0) if (a is not None or b is not None) else None for a, b in zip(o["counts"], parts[n])]
        else:
            tier = ch["tier"] if n == "Sinian Federation" else "Notable (China piece)"
            rows.append({"tier": tier, "nation": n, "share": ch["share"] * f, "counts": parts[n],
                         "from": "China"})
    return rows, list(inw)


# ----------------------------------------------------------------------------------------------- new pools
NEW_PLACES = OrderedDict([
    # place in A_new_places.csv: (row it joins, zones, may open a new row)
    ("Hong Kong", ("Sinian Federation", [8], False)),
    ("Macau", ("Sinian Federation", [8], False)),
    ("Taiwan", ("Taiwan", [8], True)),
    ("Mongolia", ("Mongolia", [7], True)),
    ("North Korea", ("Korea", [8], False)),
    ("Luxembourg", ("France", [0], False)),
    ("Kosovo", ("Serbia", [1], False)),
    ("Austria", ("Austro-Bavaria", [1], False)),
    ("Petén", ("Yucatán", [-6], False)),
])


def read_pools_master():
    pools = {}
    for ln in COMP.read_text(encoding="utf-8").splitlines()[66:111]:
        m = re.match(r"^\|\s*([A-Za-z .]+?)\s*\|\s*~([0-9.]+)M\s*\|", ln)
        if m:
            pools[m.group(1)] = float(m.group(2)) * 1e6
    return pools


CAL_ALIAS = {"United States": "USA", "United Kingdom": "UK", "Czechia": "Czech Republic", "Korea, Rep.": "South Korea",
             "Russian Federation": "Russia", "Viet Nam": "Vietnam", "Slovak Republic": "Slovakia"}


def estimate_new_pools(log):
    master = read_pools_master()
    cal = []
    for r in csv.DictReader(open(RES / "A_calibration_43.csv", encoding="utf-8")):
        name = CAL_ALIAS.get(r["country"].strip(), r["country"].strip())
        if name not in master or not r["population"].strip() or not r["gdp_per_person_usd"].strip():
            log.append(f"calibration: skipped {r['country']} (no pool or missing figures)")
            continue
        gini = float(r["gini"]) if r["gini"].strip() else None
        cal.append({"name": name, "lg": math.log10(float(r["gdp_per_person_usd"])), "gini": gini,
                    "ratio": master[name] / float(r["population"])})
    lgs = [c["lg"] for c in cal]
    gs = [c["gini"] for c in cal if c["gini"] is not None]
    sd = lambda v: (sum((a - sum(v) / len(v)) ** 2 for a in v) / len(v)) ** 0.5
    s_lg, s_g = sd(lgs), sd(gs)
    gini_scale = 100.0 if max(gs) > 1 else 1.0
    est = OrderedDict()
    places = {r["place"].strip(): r for r in csv.DictReader(open(RES / "A_new_places.csv", encoding="utf-8"))}
    for place in NEW_PLACES:
        key = place
        r = places.get(place) or places.get(place.replace("é", "e"))
        src = r
        if place == "Petén":
            # Petén: its own people, at Guatemala's income and inequality (no department GDP figure assumed)
            g = places.get("Guatemala")
            pet = next((v for k, v in places.items() if "pet" in norm(k)), None)
            pop = float(pet["population"]) if pet and pet["population"].strip() else None
            if pop is None:
                pop = float(PETEN_FALLBACK)
                log.append(f"new pool: Petén population blank in Unit A; used {PETEN_FALLBACK:,} (INE 2023 projection)")
            src = g
        else:
            pop = float(r["population"]) if r and r["population"].strip() else None
        if src is None or pop is None or not src["gdp_per_person_usd"].strip():
            log.append(f"new pool: {place} skipped (missing population or GDP per person)")
            continue
        lg = math.log10(float(src["gdp_per_person_usd"]))
        gini = float(src["gini"]) if src["gini"].strip() else None
        if gini is not None and gini_scale == 100.0 and gini <= 1:
            gini *= 100
        if gini is not None and gini_scale == 1.0 and gini > 1:
            gini /= 100

        def dist(c):
            d = ((c["lg"] - lg) / s_lg) ** 2
            if gini is not None and c["gini"] is not None:
                d += ((c["gini"] - gini) / s_g) ** 2
            return d ** 0.5
        pool_set = [c for c in cal if gini is None or c['gini'] is not None]  # no Gini-less neighbor when the place has a Gini
        nn = sorted(pool_set, key=dist)[:3]
        ratio = sum(c["ratio"] for c in nn) / 3
        est[place] = {"population": pop, "ratio": ratio, "pool": pop * ratio, "neighbors": [c["name"] for c in nn],
                      "gdp": float(src["gdp_per_person_usd"]), "gini": gini}
    return est


def add_new_pool(cities, place, pool, log):
    target, zones, may_open = NEW_PLACES[place]
    humans = EXILE_RATE * pool
    cand = []
    for name, (header, rows) in cities.items():
        if name in EXEMPT or not in_window(name, zones):
            continue
        if not may_open and not any(x["nation"] == target for x in rows):
            continue
        cand.append(name)
    tot_h = 0
    for name in cand:
        header, rows = cities[name]
        hc = v1.human_col(header)
        tot_h += sum((x["counts"][hc] or 0) for x in rows) if hc is not None else 0
    if not cand or tot_h == 0:
        log.append(f"new pool {place}: no city to place it in")
        return {}
    p = humans / tot_h
    placed = {}
    for name in cand:
        header, rows = cities[name]
        rows = v2.copy_rows(rows)
        if not any(x["nation"] == target for x in rows):
            rows.append({"tier": "New (time-zone window)", "nation": target, "share": 0.0,
                         "counts": [None if c is None else 0 for c in rows[0]["counts"]], "from": place})
        for x in rows:
            x["share"] *= (1 - p)
        t = next(x for x in rows if x["nation"] == target)
        t["share"] += 100 * p
        if place not in (t.get("from") or "") and place != target:
            t["from"] = ((t.get("from") + " + ") if t.get("from") else "") + place
        for j in range(len(rows[0]["counts"])):
            if rows[0]["counts"][j] is None and all(x["counts"][j] is None for x in rows):
                continue
            total = sum((x["counts"][j] or 0) for x in rows)
            new = round(total * p)
            others = {x["nation"]: (x["counts"][j] or 0) for x in rows}
            kept = v1.distribute(total - new, others, even=False)
            for x in rows:
                if x["counts"][j] is None and x is not t:
                    continue
                x["counts"][j] = kept[x["nation"]] + (new if x is t else 0)
        cities[name] = (header, rows)
        placed[name] = 100 * p
    log.append(f"new pool {place}: {humans:,.0f} humans (2% of {pool:,.0f}) -> {len(cand)} cities at {100 * p:.3f}% each")
    return placed


# ----------------------------------------------------------------------------------------------- decline + fill
def decline_fill(rows, r):
    rows = v2.copy_rows(rows)
    sf = next(x for x in rows if x["nation"] == "Sinian Federation")
    el = [x for x in rows if x is not sf and x["tier"] != "Primary" and x["share"] >= LINE]
    fallback = False
    if not el:
        el = [x for x in rows if x is not sf and x["share"] >= LINE]
        fallback = True
    s_old = sf["share"]
    sf["share"] = s_old * r
    add = v1.distribute(s_old - sf["share"], {x["nation"]: x["share"] for x in el}, even=False)
    for x in el:
        x["share"] += add[x["nation"]]
    for j in range(len(sf["counts"])):
        c = sf["counts"][j]
        if c is None:
            continue
        newc = round(c * r)
        sf["counts"][j] = newc
        add = v1.distribute(c - newc, {x["nation"]: (x["counts"][j] or 0) for x in el}, even=False)
        for x in el:
            x["counts"][j] = (x["counts"][j] or 0) + add[x["nation"]]
    return rows, [x["nation"] for x in el], fallback


# ----------------------------------------------------------------------------------------------- Kunlun
def kunlun_option_a(rows):
    """China (Sinian Federation) alone in the top tier; USA and Russia to the middle tier; Mongolia and
    Künnarantaiga added to the middle tier as the founding wave. Primary 8 / Significant 3 / Notable 1 shares,
    each tier's existing relative weights kept; members new to a tier get that tier's mean weight."""
    rows = v2.copy_rows(rows)
    for x in rows:
        if x["nation"] == "China":
            x["nation"] = "Sinian Federation"
        if x["nation"] in ("USA", "Russia"):
            x["tier"] = "Significant"
            x["moved"] = True
    for n in ("Mongolia", "Künnarantaiga"):
        rows.append({"tier": "Significant", "nation": n, "share": None, "counts": [0], "from": "", "moved": True,
                     "founder": True})
    tiers = {"Primary": 8, "Significant": 3, "Notable": 1}
    total_w = sum(tiers[x["tier"]] for x in rows)
    for t, wt in tiers.items():
        mem = [x for x in rows if x["tier"] == t]
        keep = [x["share"] for x in mem if not x.get("moved")]
        mean = sum(keep) / len(keep) if keep else 1.0
        raw = {x["nation"]: (mean if x.get("moved") else x["share"]) for x in mem}
        tier_total = 100 * wt * len(mem) / total_w
        for x in mem:
            x["share"] = tier_total * raw[x["nation"]] / sum(raw.values())
    total = 135_226  # Census I robots (spec L33)
    d = v1.distribute(total, {x["nation"]: x["share"] for x in rows}, even=False)
    for x in rows:
        x["counts"] = [d[x["nation"]]]
        if x.get("founder"):
            x["tier"] = "Significant (founding wave)"
    return rows


# ----------------------------------------------------------------------------------------------- main
def main():
    log = []
    splits = all_splits(log)
    ch = china_headcount()
    ch_tot = sum(ch.values())
    ch_shares = {k: v / ch_tot for k, v in ch.items()}

    rng = random.Random(v1.SEED)
    draws = {c: rng.uniform(0.55, 0.65) for c in v2.DECLINE_CITIES}
    gifts = v3.founder_draws()

    files = sorted(p for p in SPECS.glob("*/*.md") if not p.name.startswith("_"))
    original, cities = OrderedDict(), OrderedDict()
    for p in files:
        header, rows = v1.read_table(p)
        name = next((c for c, f in v1.CITY_FILES if (SPECS / f) == p), None)
        if name is None:
            name = p.stem.replace("_", " ").replace("dUrville", "d'Urville").replace("Temirotkel", "Temirötkel")
        original[name] = (header, rows)

    pieces_placed = {}
    for name, (header, rows) in original.items():
        if name == "Kunlun":
            cities[name] = (header, kunlun_option_a(rows))
            continue
        cur = apply_splits(v2.copy_rows(rows), splits)
        cur, inw = split_china(name, cur, ch_shares)
        pieces_placed[name] = inw
        cities[name] = (header, cur)

    pools = estimate_new_pools(log)
    placed = OrderedDict()
    for place, est in pools.items():
        placed[place] = add_new_pool(cities, place, est["pool"], log)

    fills = {}
    for name in list(cities):
        header, rows = cities[name]
        if name in draws and name not in EXEMPT:
            rows, el, fb = decline_fill(rows, draws[name])
            fills[name] = (el, fb)
        if name in gifts:
            rows = v3.move_from(rows, "Japan", gifts[name])
            for x in rows:
                if x["nation"] in {n for n, _ in gifts[name]}:
                    x["tier"] = "Founder"
        cities[name] = (header, rows)

    bad = []
    for name, (header, rows) in cities.items():
        oh, orows = original[name]
        for j in range(len(orows[0]["counts"])):
            want = 135_226 if name == "Kunlun" else sum((x["counts"][j] or 0) for x in orows)
            if want != sum((x["counts"][j] or 0) for x in rows):
                bad.append((name, j))
        if any((c or 0) < 0 for x in rows for c in x["counts"]):
            bad.append((name, "negative"))
        if abs(sum(x["share"] for x in rows) - sum(x["share"] for x in orows)) > 0.05:
            bad.append((name, "share sum"))

    # ---------------- output
    print("## Inputs\n")
    print("**Successor headcount shares** (share of the old country's people):\n")
    for c, lst in splits.items():
        print(f"- **{c}:** " + " · ".join(f"{s} {100 * f:.2f}%" for s, f in lst))
    print("\n**China (2024 year-end, 31 provinces):** " + " · ".join(f"{k} {100 * v:.2f}%" for k, v in ch_shares.items()))
    print("\n**New pools (M4: 3 nearest existing nations by GDP per person and Gini):**\n")
    print("| Place | People | GDP per person (USD) | Gini | Nearest nations | Pool per person | Pool | Humans (2%) | Joins | Cities | Share added in each |")
    print("|---|--:|--:|--:|---|--:|--:|--:|---|--:|--:|")
    for place, e in pools.items():
        pl = placed.get(place, {})
        share = f"{next(iter(pl.values())):.3f}%" if pl else "—"
        gini = f"{e['gini']:.1f}" if e["gini"] is not None else "—"
        print(f"| {place} | {e['population']:,.0f} | {e['gdp']:,.0f} | {gini} | {', '.join(e['neighbors'])} | "
              f"{e['ratio']:.3f} | {e['pool'] / 1e6:,.2f}M | {EXILE_RATE * e['pool']:,.0f} | {NEW_PLACES[place][0]} | {len(pl)} | {share} |")
    print("\n**Log:**\n")
    for l in log:
        print(f"- {l}")
    print(f"\n*Every city keeps its exact total in every census column, no count is negative, and shares still sum as "
          f"before: {'yes' if not bad else 'NO: ' + str(bad)}.*\n")

    print("## Every city\n")
    print("| City | Leader after | Lead (1st ÷ 2nd) | Sinian Federation | Top five after (%) |")
    print("|---|---|--:|--:|---|")
    for name, (header, rows) in cities.items():
        la, ratio = v2.lead(rows)
        sf = next((x["share"] for x in rows if x["nation"] == "Sinian Federation"), None)
        print(f"| {name} | {la['nation']} {la['share']:.2f} | {ratio:.2f} | {f'{sf:.2f}' if sf is not None else '—'} | "
              f"{v2.fmt_top(rows)} |")

    nb, na = {}, {}
    for name, (header, rows) in cities.items():
        hc = v1.human_col(header)
        if hc is None:
            continue
        for x in original[name][1]:
            if x["counts"][hc] is not None:
                nb[x["nation"]] = nb.get(x["nation"], 0) + x["counts"][hc]
        for x in rows:
            if x["counts"][hc] is not None:
                na[x["nation"]] = na.get(x["nation"], 0) + x["counts"][hc]
    tot = sum(na.values())
    print(f"\n## Nationally (Census I humans, {tot:,})\n")
    print("| Rank | Nation | Humans | Share | Listed today as |")
    print("|--:|---|--:|--:|---|")
    for i, (n, v) in enumerate(sorted(na.items(), key=lambda kv: -kv[1]), 1):
        srcs = [c for c, lst in splits.items() if c != n and any(s2 == n for s2, _ in lst)]
        newp = [p for p, (t, _, _) in NEW_PLACES.items() if t == n and p != n]
        if n in nb:
            b = f"{nb[n]:,}" + ((" + part of " + ", ".join(srcs)) if srcs else "") + ((" + " + ", ".join(newp)) if newp else "")
        else:
            b = ("part of " + ", ".join(srcs)) if srcs else ("part of China" if n in PIECE_ZONES or n == "Sinian Federation" else "new")
            if n == "Sinian Federation":
                b = f"China {nb.get('China', 0):,} (with Zhongshan's, unchanged) + Hong Kong, Macau"
            elif newp:
                b += " + " + ", ".join(newp)
        print(f"| {i} | {n} | {v:,} | {100 * v / tot:.2f}% | {b} |")

    print("\n## City by city (rows under 0.10% added together by source; every row is in the CSV)\n")
    csvrows = []
    for name, (header, rows) in cities.items():
        hc = v1.human_col(header)
        print(f"### {name}\n")
        notes = []
        if pieces_placed.get(name):
            notes.append("China's pieces in window: " + ", ".join(pieces_placed[name]))
        newp = [f"{p} {v:.2f}%" for p, d in placed.items() for c, v in d.items() if c == name]
        if newp:
            notes.append("new pools: " + ", ".join(newp))
        if name in fills:
            el, fb = fills[name]
            notes.append(f"Sinian draw {draws[name]:.4f}; fill to: {', '.join(el)}" + (" (FALLBACK)" if fb else ""))
        if name in gifts:
            notes.append("from Japan: " + ", ".join(f"{n} {v:.2f}" for n, v in gifts[name]))
        if notes:
            print("*" + " · ".join(notes) + "*\n")
        before = {x["nation"]: x["share"] for x in original[name][1]}
        print("| Tier | Row | From | Before | After |" + (" Census I humans after |" if hc is not None else ""))
        print("|---|---|---|--:|--:|" + ("--:|" if hc is not None else ""))
        small = {}
        for x in sorted(rows, key=lambda x: -x["share"]):
            src = x.get("from") or ""
            if src and x["share"] < 0.10:
                s = small.setdefault(src, [0, 0.0, 0])
                s[0] += 1
                s[1] += x["share"]
                s[2] += (x["counts"][hc] or 0) if hc is not None else 0
            else:
                b = before.get(x["nation"])
                line = f"| {x['tier']} | {x['nation']} | {src} | {f'{b:.2f}%' if b is not None else '—'} | {x['share']:.2f}% |"
                if hc is not None:
                    line += f" {x['counts'][hc]:,} |" if x["counts"][hc] is not None else " |"
                print(line)
            csvrows.append({"city": name, "row": x["nation"], "from": src, "tier": x["tier"],
                            "share_after": f"{x['share']:.3f}",
                            **{h: (x["counts"][j] if j < len(x["counts"]) else "") for j, h in enumerate(header)}})
        for src, (k, sh, h) in small.items():
            line = f"| | *{k} smaller row{'' if k == 1 else 's'} from {src}* | {src} | — | {sh:.2f}% |"
            if hc is not None:
                line += f" {h:,} |"
            print(line)
        print()

    out = Path(os.environ.get("RUN4_OUT_DIR", str(HERE))) / "12_city_tables.csv"
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
