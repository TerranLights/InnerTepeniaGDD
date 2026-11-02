#!/usr/bin/env python3
"""Part 2: successors of the USA, Canada, Mexico, Italy, Germany and Argentina.
Reads only 05_part2_unit_data.csv next to this file. Prints Markdown.

Population column forms:  a number | SPLIT:<parent>:<fraction> | REMAINDER:<country total>
GDP column forms (per gdp_kind): total (any unit, consistent within a country) | share_pct |
per_capita (GDP = population x per capita) | SPLIT (parent GDP x the same fraction) |
REMAINDER[:<country total>] (country total minus the listed units; for share_pct, 100 minus them).

Option A splits a country's effective pool by headcount; Option B by economic size (GDP).
Every piece keeps its source country's single inequality adjustment.
"""
import csv
import os
from collections import OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

# Effective pools, Upper_Earth_Immigration_Composition.md L68-L86 ("~155M" etc.)
POOL = {"USA": 155e6, "Canada": 20e6, "Mexico": 18e6, "Italy": 27e6, "Germany": 46e6, "Argentina": 6e6}

# Parents of split rows: (population, GDP in the country's own GDP unit)
PARENT = {
    "Alaska": (737_270, 75_012),          # U1 July 1 2025; U2 2025, million USD
    "Ontario": (16_216_961, 1_197_020),   # C1 July 1 2025; C2 2024, million CAD
    "Nunavut": (42_108, 5_668),           # C1; C2
}

# Published totals to check the unit sums against
CHECK = {
    "USA": (341_784_857, 30_762_099, "July 1 2025 estimate, 50 states + DC (U1); 2025 GDP, million USD (U2)"),
    "Canada": (41_608_982, None, "July 1 2025, Table 17-10-0005-01 (C1)"),
    "Italy": (58_942_828, None, "1 Jan 2026 estimate (I1)"),
    "Argentina": (46_044_573, None, "2022 census, without Argentine Antarctica (A1)"),
}

rows = list(csv.DictReader(open(os.path.join(HERE, "05_part2_unit_data.csv"), newline="")))
by_country = OrderedDict()
for r in rows:
    by_country.setdefault(r["source_country"], []).append(r)


def resolve(country, units):
    """Return list of (unit, successor, population, gdp) with every form resolved."""
    out, known_pop, known_gdp = [], 0.0, 0.0
    remainder = None
    for r in units:
        pop, gdp, kind = r["population"], r["gdp_value"], r["gdp_kind"]
        if pop.startswith("REMAINDER"):
            remainder = r
            continue
        if pop.startswith("SPLIT:"):
            _, parent, frac = pop.split(":")
            frac = float(frac)
            p = PARENT[parent][0] * frac
            g = PARENT[parent][1] * frac if gdp == "SPLIT" else float(gdp)
        else:
            p = float(pop)
            g = p * float(gdp) if kind == "per_capita" else float(gdp)
        known_pop += p
        known_gdp += g
        out.append([r["unit"], r["successor"], p, g])
    if remainder is not None:
        total_pop = float(remainder["population"].split(":")[1])
        if remainder["gdp_kind"] == "share_pct":
            rem_gdp = 100.0 - known_gdp
        else:
            total_gdp = float(remainder["gdp_value"].split(":")[1])
            rem_gdp = total_gdp - known_gdp
        out.append([remainder["unit"], remainder["successor"], total_pop - known_pop, rem_gdp])
    # Fix the Alaska / Ontario / Nunavut whole-parent GDP rows (gdp given as the parent total)
    return out


print("## Checks\n")
resolved = OrderedDict()
for country, units in by_country.items():
    res = resolve(country, units)
    resolved[country] = res
    pop = sum(x[2] for x in res)
    gdp = sum(x[3] for x in res)
    line = f"- **{country}:** units sum to {pop:,.0f} people"
    if country in CHECK:
        tp, tg, note = CHECK[country]
        line += f"; published total {tp:,} ({note}); difference {pop - tp:,.0f}"
        if tg:
            line += f"; GDP units sum to {gdp:,.0f} against {tg:,} (difference {gdp - tg:,.0f})"
    print(line)
print()

combined = defaultdict(lambda: {"pop": 0.0, "A": 0.0, "B": 0.0, "parts": []})
for country, res in resolved.items():
    pop_t = sum(x[2] for x in res)
    gdp_t = sum(x[3] for x in res)
    succ = OrderedDict()
    for unit, s, p, g in res:
        d = succ.setdefault(s, {"pop": 0.0, "gdp": 0.0, "units": []})
        d["pop"] += p
        d["gdp"] += g
        d["units"].append(unit)
    print(f"## {country} (effective pool ~{POOL[country] / 1e6:.0f}M)\n")
    print("| Successor | Present-day units | Population | Share of people | Share of GDP | GDP per person vs the country | "
          "Option A: by headcount | Option B: by economic size |")
    print("|---|---|--:|--:|--:|--:|--:|--:|")
    for s, d in sorted(succ.items(), key=lambda kv: -kv[1]["pop"]):
        ps, gs = d["pop"] / pop_t, d["gdp"] / gdp_t
        rel = gs / ps if ps else 0
        A, B = POOL[country] * ps, POOL[country] * gs
        units = ", ".join(d["units"]) if len(d["units"]) <= 12 else f"{len(d['units'])} units (see the CSV)"
        print(f"| {s} | {units} | {d['pop']:,.0f} | {100 * ps:.2f}% | {100 * gs:.2f}% | {rel:.2f}x | "
              f"{A / 1e6:,.2f}M | {B / 1e6:,.2f}M |")
        c = combined[s]
        c["pop"] += d["pop"]
        c["A"] += A
        c["B"] += B
        c["parts"].append(country)
    print()

print("## Every successor, all source countries combined\n")
print("Successors that draw on more than one present-day country add their pieces' pools together. A successor's "
      "pool here counts only the source countries in this part (for example Cascadia's Alaska Panhandle comes "
      "from the USA's pool; Austria, Chile and Guatemala's Petén are not in this part).\n")
print("| Successor | From | Population (present day) | Option A pool | Option B pool |")
print("|---|---|--:|--:|--:|")
for s, c in sorted(combined.items(), key=lambda kv: -kv[1]["B"]):
    print(f"| {s} | {', '.join(c['parts'])} | {c['pop']:,.0f} | {c['A'] / 1e6:,.2f}M | {c['B'] / 1e6:,.2f}M |")
print()
