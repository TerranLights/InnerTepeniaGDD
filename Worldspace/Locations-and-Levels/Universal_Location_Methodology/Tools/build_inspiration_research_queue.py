#!/usr/bin/env python3
"""
BUILD INSPIRATION RESEARCH QUEUE  (2026-10-26; developer: do the deep research for every city's real-world inspiration places, two rounds, full depth)

  usage:  python3 build_inspiration_research_queue.py [--write]

Reads Cities/Inspirational-Influences.md and splits it into WORK UNITS, one per city (a city with more than 7 picks is split into two units, a and b).
For each unit it writes inputs/<unit>.md containing ONLY that city's own picks, so an agent assigned to the unit never reads another city's picks
(the project's one-location-on-its-own-terms rule). It also writes _TRACKER.md (one row per unit, Round 1 and Round 2 status).
The status columns are edited by hand (or by the orchestrator) as rounds finish; re-running this script KEEPS existing statuses.
Real-world facts only. No conclusion about any fictional city is produced or stored.
"""
import os, re, sys
GDD = "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
PICKS = GDD + "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Inspirational-Influences.md"
OUT = GDD + "Reference/Real-World/Inspiration_Place_Research/"
PRIORITY = "Mirny"      # developer, 2026-10-26: start with the Mirny subnet (it holds cities whose passes are already done), then the rest in file order
SKIP = {"Relung Panen"}          # researched separately (26 candidate places, 2026-10-26)


def parse():
    sub = city = None
    data = []   # (subnet, city, [bullets])
    for ln in open(PICKS, encoding="utf-8").read().split("\n"):
        if ln.startswith("### "):
            sub = ln[4:].strip()
        elif ln.startswith("##### "):
            city = ln[6:].strip()
            data.append([sub, city, []])
        elif ln.startswith("- ") and data and city:
            data[-1][2].append(ln[2:].strip())
    return [(s, c, b) for s, c, b in data if b and c not in SKIP]


def key(name):
    return re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")


def main():
    write = "--write" in sys.argv
    units = []
    for sub, city, bullets in parse():
        if len(bullets) > 7:
            h = (len(bullets) + 1) // 2
            units.append((sub, city, key(city) + "_a", bullets[:h]))
            units.append((sub, city, key(city) + "_b", bullets[h:]))
        else:
            units.append((sub, city, key(city), bullets))
    units.sort(key=lambda u: 0 if PRIORITY in u[0] else 1)   # stable: the rest keep file order
    old = {}
    tp = OUT + "_TRACKER.md"
    if os.path.exists(tp):
        for ln in open(tp, encoding="utf-8").read().split("\n"):
            m = re.match(r"\| `([^`]+)` \|.*\| (.*?) \| (.*?) \| (.*?) \|$", ln)
            if m:
                old[m.group(1)] = (m.group(2), m.group(3), m.group(4))
    rows = []
    for sub, city, u, bl in units:
        r1, r2, note = old.get(u, ("☐", "☐", ""))
        rows.append("| `%s` | %s | %s | %d | %s | %s | %s |" % (u, city, sub, len(bl), r1, r2, note))
        if write:
            body = "# Research unit `%s`: %s (%s)\n\nThis file holds ONLY this city's own inspiration picks. Do not read any other city's picks.\nEach line is `place [TIER] // the developer's reason note` as written in the picks file.\n\n" % (u, city, sub)
            body += "\n".join("- " + b for b in bl) + "\n"
            open(OUT + "inputs/%s.md" % u, "w", encoding="utf-8").write(body)
    head = ("# Inspiration place research: tracker (all cities except Relung Panen)\n\n"
            "**Built %s by `Tools/build_inspiration_research_queue.py`.** One row per work unit. Round 1 = basics (what else exists there, the cultural locations, how the defining feature shaped them). "
            "Round 2 = deeper (other settings, subcultures, leisure industries, places of meeting, cultural activities and civic life). "
            "Status: ☐ not started · ◐ in progress · ✅ finished (every place ticked FINAL in its file).\n\n"
            "Developer, 2026-10-26: two rounds at full depth for every city; accuracy and depth over cost; patience for the window limits. **Run order: the Mirny subnet first (8 units: Casey, Mirny, Davis, Ariun Nuur, Kunlun, Zhongshan, Sinheung, Shirayuki), then every other subnet in file order.** Relung Panen is separate.\n\n"
            "| Unit | City | Subnet | Picks | Round 1 | Round 2 | Note |\n|---|---|---|--:|---|---|---|\n") % "2026-10-26"
    txt = head + "\n".join(rows) + "\n"
    print("units:", len(units), "| cities:", len(set(c for _, c, _, _ in units)), "| picks:", sum(len(b) for _, _, _, b in units))
    if write:
        open(tp, "w", encoding="utf-8").write(txt)
        print("wrote", tp)


if __name__ == "__main__":
    main()
