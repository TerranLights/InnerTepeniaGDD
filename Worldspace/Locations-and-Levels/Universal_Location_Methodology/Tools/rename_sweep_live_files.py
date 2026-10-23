#!/usr/bin/env python3
"""
RENAME SWEEP, LIVE FILES  —  line-aware version of the old-name sweep (2026-10-23, developer request:
"find all the mentions of their old names, mark down their new names, and add a brief note 'New (formerly Old)'").

  usage:  python3 rename_sweep_live_files.py            # DRY RUN: prints every line that would change
          python3 rename_sweep_live_files.py --apply    # applies (git is the backup)

SCOPE (live files only; everything else is listed in the report and NOT touched):
  the cities' own files (Specs, Local_Cultures, Local_Robot_Culture, City_Vision_Notes, City_Enneagram_Personalities, the city catalogs,
  Neo-Races catalogs, the Relung Panen folder), Infrastructure (Highways, Ports, Airports), and the research-topic / book indexes.
NEVER TOUCHED: megasheets, the Background-Lore vignettes (standing rules), graphify-out (regenerated), frozen records and audits, the rulings
  log and method trackers, test runs, archives, Concordia district work, real-station data (inventory CSVs, BAS READER files), and the six
  held Mirny input files (they wait for the Mirny pass, per the developer's 2026-10-03 ruling).
WHAT IT SKIPS WITHIN A LIVE FILE: a line that is a rename notice, tells the story of the old name (etymology, fusion, placeholder), or is about
  the real site or station (heritage base, Operation Tabarin, King Sejong, King Juan Carlos), so the old name stays there on purpose.
THE NOTE: in a live file that has no rename notice of its own, the FIRST replaced mention becomes "New (formerly Old)".
"""
import os, re, sys, glob, collections
sys.argv_save = list(sys.argv)
APPLY = "--apply" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.argv = ["x"]
import rename_sweep_held_files as R          # the token rules (what counts as the city name vs the real site)
sys.argv = sys.argv_save
GDD = R.GDD
C = GDD + "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/"
NEW_OLD = {"Santa Luce": "Abowasa", "Temirötkel": "Sayowa", "Utstein": "Princess Elisabeth", "Relung Panen": "Bunger Hills City",
           "Puerto Abrigo": "Port Lockroy", "Pergamino": "Juan Carlos", "Contrapunto": "Sejong", "Ariun Nuur": "Vostok"}
SKIP = re.compile(r"RENAMED|[Ff]ormerly|[Ff]ormer name|[Ff]ormerly named|renamed|Renamed|\bplaceholder|\{\{|DR-3[6-9]|DR-4[0-3]|etymolog|Shōwa|Syowa|Showa|Aboa \+ Wasa|Aboa and Wasa|"
                  r"fusion|real base|real station|real Spanish|real Soviet|Operation Tabarin|Heritage Trust|King Sejong|King Juan Carlos|Hangul|Lockroy, French|"
                  r"Turku|naming connection|the real|real-world|Lake Vostok|district|Vostok Station|Wasa Research|Aboa Station|"
                  r"Vostok/Ariun Nuur|Vostok genetics|Vostok Genetics|naming it after|In the pre-exile era|founded by Korean exiles and both named|(?:Abowasa|Sayowa|Princess Elisabeth|Bunger Hills City|Port Lockroy|Juan Carlos|Sejong|Vostok)\s*(?:→|->|=>)")
CITY_OWN = ("/Specs/", "/Local_Cultures/", "/Local_Robot_Culture/", "/City_Vision_Notes/", "/City_Enneagram_Personalities/", "/Relung_Panen/")


def live_files():
    out = []
    for sub in ("Specs", "Local_Cultures", "Local_Robot_Culture", "City_Vision_Notes", "City_Enneagram_Personalities"):
        out += glob.glob(C + sub + "/**/*.md", recursive=True)
    out += [f for f in glob.glob(C + "*.md") if os.path.basename(f) in (
        "Santa_Luce.md", "Utstein.md", "Temirotkel.md", "Puerto_Abrigo.md", "Pergamino.md", "Contrapunto.md", "Ariun_Nuur.md")]
    out += glob.glob(C + "Relung_Panen/*.md") + [C + "Relung_Panen_Dossier_2026-10-03.md"]
    out += glob.glob(GDD + "Neo-Races-and-Cultures/*_Subnet/*/*_Catalog.md")
    out += [GDD + "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/" + f for f in ("Highways.md", "Ports.md", "Airports.md")]
    out += [GDD + "Reference/Real-World/Book_to_City_Map.md", GDD + "Reference/Real-World/City_and_District_Research_Topics.md",
            GDD + "Reference/Real-World/Book_Extraction_Index.md", GDD + "Reference/Real-World/Book_TOC_Master_Reference.md"]
    return sorted(set(f for f in out if os.path.exists(f)))


def new_for(text_match):
    for new, old in NEW_OLD.items():
        if text_match == new:
            return old
    return None


def process(path):
    t = open(path, encoding="utf-8").read()
    has_notice = "RENAMED 2026-10-03" in t or any(k in path for k in CITY_OWN)
    out, changed, noted = [], [], set()
    for n, line in enumerate(t.split("\n"), 1):
        if SKIP.search(line):
            out.append(line)
            continue
        nl, st = R.transform(line)
        if nl != line:
            if not has_notice:
                # first replaced mention of each new name in this file gets the note
                for new, old in NEW_OLD.items():
                    if new in nl and new not in noted and old in line:
                        nl = nl.replace(new, "%s (formerly %s)" % (new, old), 1)
                        noted.add(new)
                        break
            changed.append((n, line, nl))
        out.append(nl)
    return t, "\n".join(out), changed


def main():
    tot = 0
    fl = 0
    for f in live_files():
        t, nt, ch = process(f)
        if not ch:
            continue
        fl += 1
        tot += len(ch)
        print("\n### %s  (%d line(s))" % (f.replace(GDD, ""), len(ch)))
        for n, a, b in ch[:40]:
            i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), 0)
            print("  L%-5d - %s" % (n, a[max(0, i - 45):i + 70]))
            print("         + %s" % b[max(0, i - 45):i + 85])
        if APPLY and nt != t:
            open(f, "w", encoding="utf-8").write(nt)
    print("\n%s: %d line(s) in %d file(s)" % ("APPLIED" if APPLY else "DRY RUN", tot, fl))


if __name__ == "__main__":
    main()
