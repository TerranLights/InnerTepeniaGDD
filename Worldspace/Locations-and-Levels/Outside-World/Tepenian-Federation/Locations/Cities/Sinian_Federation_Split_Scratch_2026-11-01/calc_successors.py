#!/usr/bin/env python3
"""Add present-day units up into the Interwar successor countries and split China's
effective pool two ways. Reads only 02_unit_data.csv next to this file. Prints Markdown.

Option A: split by headcount (2024 year-end population).
Option B: split by economic size (2024 gross regional product = population x GDP per person).
Both keep China's single inequality adjustment for every piece (no provincial Gini used).
"""
import csv
import os
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
CHINA_EFFECTIVE_POOL = 210_000_000  # Upper_Earth_Immigration_Composition.md L68 ("~210M")
NATIONAL_CENSUS_2020 = 1_411_778_724  # P1
NATIONAL_YEAREND_2024 = 140828 * 10_000  # P4
ORDER = ["Sinian Federation", "Manchuria", "Mongolia", "East Turkestan", "Tibet", "Taiwan"]


def num(s):
    s = (s or "").strip()
    return float(s) if s else None


rows = list(csv.DictReader(open(os.path.join(HERE, "02_unit_data.csv"), newline="")))
provinces = [r for r in rows if r["in_china_official_figures"] == "yes" and r["successor"] != "(not assigned)"]

# --- checks against the national totals -------------------------------------------------
c2020 = sum(num(r["pop_census_2020_persons"]) for r in provinces)
p2024 = sum(num(r["pop_yearend_2024_10k"]) for r in provinces) * 10_000
grp = sum(num(r["grp_2024_100m_yuan"]) for r in provinces)
print("## Checks\n")
print(f"- 31 provinces, 2020 census: {c2020:,.0f}; plus 2,000,000 servicemen = {c2020 + 2_000_000:,.0f}; "
      f"national total {NATIONAL_CENSUS_2020:,} (difference {NATIONAL_CENSUS_2020 - c2020 - 2_000_000:,.0f})")
print(f"- 31 provinces, 2024 year-end: {p2024:,.0f}; national total {NATIONAL_YEAREND_2024:,}; "
      f"gap {NATIONAL_YEAREND_2024 - p2024:,.0f} (servicemen are in the national total only, plus rounding "
      f"of 31 figures given to the nearest 10,000)")
print(f"- 31 provinces, 2024 gross regional product: {grp:,.1f} hundred million yuan "
      f"(provinces are summed as published; the national GDP is a separate account and is not expected to match)\n")

# --- per successor ------------------------------------------------------------------------
agg = OrderedDict((s, {"c2020": 0.0, "p2024": 0.0, "grp": 0.0, "other": 0.0, "units": []}) for s in ORDER)
for r in rows:
    s = r["successor"]
    if s not in agg:
        continue
    a = agg[s]
    a["units"].append(r["unit"])
    if r["in_china_official_figures"] == "yes":
        a["c2020"] += num(r["pop_census_2020_persons"]) or 0
        a["p2024"] += (num(r["pop_yearend_2024_10k"]) or 0) * 10_000
        a["grp"] += num(r["grp_2024_100m_yuan"]) or 0
    else:
        a["other"] += num(r["other_population"]) or 0

print("## Raw populations of the successors\n")
print("| Successor | Present-day units | 2020 census (mainland part) | Share of the 31 provinces, 2020 | "
      "2024 year-end (mainland part) | Share of the 31 provinces, 2024 | Outside China's official figures "
      "(latest) | Total, 2024 basis |")
print("|---|---|--:|--:|--:|--:|--:|--:|")
for s, a in agg.items():
    print(f"| **{s}** | {', '.join(a['units'])} | {a['c2020']:,.0f} | {100 * a['c2020'] / c2020:.2f}% | "
          f"{a['p2024']:,.0f} | {100 * a['p2024'] / p2024:.2f}% | {a['other']:,.0f} | "
          f"{a['p2024'] + a['other']:,.0f} |")
print()

print("## GDP per person of each successor's mainland part (DERIVED: summed GRP / summed 2024 year-end "
      "population)\n")
print("| Successor | 2024 GRP, hundred million yuan | Share of the 31 provinces' GRP | GDP per person, yuan |")
print("|---|--:|--:|--:|")
for s, a in agg.items():
    if a["p2024"]:
        print(f"| {s} | {a['grp']:,.1f} | {100 * a['grp'] / grp:.2f}% | {a['grp'] * 1e8 / a['p2024']:,.0f} |")
print(f"| *All 31 provinces* | {grp:,.1f} | 100.00% | {grp * 1e8 / p2024:,.0f} |\n")

print(f"## Splitting China's effective pool of ~{CHINA_EFFECTIVE_POOL / 1e6:.0f}M (mainland parts only)\n")
print("| Successor | Option A: by headcount | Option B: by economic size (GRP) |")
print("|---|--:|--:|")
for s, a in agg.items():
    if not a["p2024"]:
        continue
    A = CHINA_EFFECTIVE_POOL * a["p2024"] / p2024
    B = CHINA_EFFECTIVE_POOL * a["grp"] / grp
    print(f"| {s} | {A / 1e6:,.1f}M ({100 * a['p2024'] / p2024:.1f}%) | {B / 1e6:,.1f}M ({100 * a['grp'] / grp:.1f}%) |")
print()
