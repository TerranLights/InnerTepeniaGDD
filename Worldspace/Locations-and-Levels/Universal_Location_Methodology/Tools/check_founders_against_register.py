#!/usr/bin/env python3
"""check_founders_against_register.py

Lists every place where a city's files disagree with the Founding Register
(Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md),
plus any station-heritage wording anywhere in the repo.

THIS IS A LIST OF PLACES TO READ, NOT A VERIFICATION. A search only finds the wording it is given; paraphrases
slip past it. Every hit must be read in context, and a city counts as clean only once its files have been read
in full (developer, 2026-10-01: "Information is in files... I want you to read the files.").

Usage:  python3 check_founders_against_register.py [--city NAME] [--include-passes]
Run from anywhere; paths are resolved from this file's location. Read-only: it never edits a file.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
CITIES = os.path.join(REPO, "Worldspace", "Locations-and-Levels", "Outside-World",
                      "Tepenian-Federation", "Locations", "Cities")
REGISTER = os.path.join(CITIES, "Founding_Register.md")

# Never scanned: locked (vignettes), generated, history, archived records (DR-27), and the files that state the rules.
# The live Test_Runs files (checklist, RESUME_HERE, observations, run log, worked examples) ARE scanned; the run
# folders themselves now sit under Archive/ULM_Records/.
SKIP_DIRS = ("graphify-out", os.sep + ".git", os.sep + "Archive" + os.sep, os.sep + "Background-Lore" + os.sep,
             "node_modules", os.sep + "Reference" + os.sep + "Materials" + os.sep)
SKIP_FILES = ("Founding_Register.md", "Station_Heritage_Removal_Tracker.md", "DEVELOPER_RULINGS_LOG.md",
              "MASTER_Process_Tracker.md", "Post-War_Nations_Founder_Reference.md")

# Adjective in the Register's "Not founders" column -> words that name that nation.
NATION_WORDS = {
    "British": r"British|UK|United Kingdom",
    "Spanish": r"Spanish|Spain",
    "South Korean": r"South Korean|Korean|South Korea|Korea",
    "Finnish": r"Finnish|Finland",
    "Swedish": r"Swedish|Sweden",
    "Belgian": r"Belgian|Belgium",
    "Japanese": r"Japanese|Japan",
    "Italian": r"Italian|Italy",
    "American": r"American|USA|United States",
    "French": r"French|France|francophone",
}

FOUNDING = r"(?:exiles|founders?|founding|founded|-founded|founding nation|founding population|founding wave)"

# Station-heritage wording, as a reason (DR-19). Infrastructure facts (DR-24) are not matched.
HERITAGE = re.compile(
    r"operator[- ]heritage|founding[- ]operator|infrastructure heritage|operator-primary|"
    r"(?:JARE|SANAE|CHINARE|AWI|BAS|IPEV|AARI|AAD|KOPRI|PNRA|Polar Institute|Polar Foundation|Antarctic Division|"
    r"Novolazarevskaya)\s+(?:heritage|inheritance|tradition|lineage)|"
    r"organic (?:real-)?station inheritance|real-world station heritage|station(?:'s)? heritage",
    re.I)


def city_tokens(name):
    """File-name and prose forms of a Register city name."""
    plain = re.sub(r"[`{}]", "", name).strip()
    toks = {plain, plain.replace(" ", "_"), plain.replace("'", "").replace(" ", "_")}
    if plain == "Dumont d'Urville":
        toks |= {"Dumont_dUrville", "DdU"}
    if plain == "Bunger Hills City":
        toks |= {"Bunger_Hills"}
    return {t for t in toks if t}


def read_register():
    rows = []
    with open(REGISTER, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("| ") or line.startswith("| City ") or line.startswith("|---"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) != 8:
                continue
            city, subnet, utc, status, founders, basis, source, notf = cells
            not_founders = [n.strip() for n in notf.split(",") if n.strip() and n.strip() != "—"]
            rows.append({"city": city, "status": status, "not": not_founders, "tokens": city_tokens(city)})
    return rows


def md_files(include_passes):
    for d, ds, fs in os.walk(REPO):
        if any(s in d + os.sep for s in SKIP_DIRS):
            continue
        if not include_passes and "City_Development_Passes" in d and "Datasheets" not in d:
            continue
        for f in fs:
            if f.endswith(".md") and f not in SKIP_FILES:
                yield os.path.join(d, f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", help="only this Register city")
    ap.add_argument("--include-passes", action="store_true",
                    help="also scan City_Development_Passes run records (datasheets are always scanned)")
    args = ap.parse_args()

    rows = read_register()
    if args.city:
        rows = [r for r in rows if args.city.lower() in r["city"].lower()]
    files = list(md_files(args.include_passes))
    texts = {}
    for p in files:
        try:
            texts[p] = open(p, encoding="utf-8").read().split("\n")
        except (UnicodeDecodeError, OSError):
            pass

    total = 0
    print("=" * 100)
    print("FOUNDERS vs. THE FOUNDING REGISTER — places to READ (not a verification)")
    print("=" * 100)
    for r in rows:
        if not r["not"]:
            continue
        nat = "|".join(NATION_WORDS.get(n, re.escape(n)) for n in r["not"])
        pat = re.compile(
            rf"\b(?:primarily\s+)?(?:{nat})\b[^.\n]{{0,40}}{FOUNDING}|{FOUNDING}[^.\n]{{0,40}}\b(?:{nat})\b|francophone city"
            if "French" in r["not"] else
            rf"\b(?:primarily\s+)?(?:{nat})\b[^.\n]{{0,40}}{FOUNDING}|{FOUNDING}[^.\n]{{0,40}}\b(?:{nat})\b", re.I)
        name_rx = re.compile("|".join(re.escape(t) for t in sorted(r["tokens"], key=len, reverse=True)))
        hits = []
        for p, lines in texts.items():
            in_city_file = any(t in p for t in r["tokens"] if "_" in t or " " not in t)
            for i, line in enumerate(lines, 1):
                if in_city_file:
                    m = pat.search(line)
                else:
                    # Shared files: the founding phrase must sit within ~120 characters of this city's name,
                    # so a long paragraph about several cities doesn't credit one city with another's founders.
                    m = None
                    for nm in name_rx.finditer(line):
                        win_s = max(0, nm.start() - 120)
                        m = pat.search(line, win_s, min(len(line), nm.end() + 120))
                        if m:
                            break
                if m:
                    s = max(0, m.start() - 70)
                    hits.append((os.path.relpath(p, REPO), i, line[s:m.end() + 60].strip()))
        if hits:
            print(f"\n## {r['city']}  [{r['status']}]  ruled out: {', '.join(r['not'])}  — {len(hits)} place(s)")
            for p, i, snip in hits:
                print(f"  {p}:{i}: …{snip}…")
            total += len(hits)

    print("\n" + "=" * 100)
    print("STATION-HERITAGE WORDING (DR-19) — places to READ")
    print("=" * 100)
    hcount = 0
    for p, lines in texts.items():
        for i, line in enumerate(lines, 1):
            m = HERITAGE.search(line)
            if m:
                s = max(0, m.start() - 70)
                print(f"  {os.path.relpath(p, REPO)}:{i}: …{line[s:m.end() + 50].strip()}…")
                hcount += 1

    print("\n" + "-" * 100)
    print(f"Founder disagreements: {total} · heritage wording: {hcount} · files scanned: {len(texts)}")
    print("Excluded: Background-Lore (locked), graphify-out, Archive/ (DR-27), pass run records (use --include-passes),")
    print("and the rule/tracking files themselves. Hits are where to READ; a clean result is not proof.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
