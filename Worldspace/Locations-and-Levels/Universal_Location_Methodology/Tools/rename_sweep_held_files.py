#!/usr/bin/env python3
"""
RENAME SWEEP FOR THE 6 FILES HELD DURING THE MIRNY PASS  —  run ONLY after the Mirny pass has finished.

Background: on 2026-10-03 four cities were renamed (DR-36..DR-39) and the names were swept through the live canon in one
sweep. Six files were HELD because they are required reading of the in-flight Mirny T8 pass (the pass quotes them and its
readers prove them line by line). Developer ruling, 2026-10-03: "Sweep the 6 held files after the Mirny pass finishes."

  Santa Luce      <- Abowasa / {{ Abowasa }}
  Temirötkel      <- Sayowa                      (the real station name "Syowa" is left alone)
  Utstein         <- Princess Elisabeth          (real-station phrases "Princess Elisabeth Antarctica / Station / of Belgium" kept)
  Relung Panen    <- Bunger Hills City / {{ Bunger }}   ("Bunger Hills" the oasis is left alone)
BATCH 2 (DR-40..DR-43, added 2026-10-03; the non-held files were swept the same day, so this tool now covers BOTH batches):
  Puerto Abrigo   <- Port Lockroy                (real-site phrases "Port Lockroy harbor/Bay/Station/base" kept)
  Pergamino       <- Juan Carlos                 ("King Juan Carlos", "Juan Carlos I" and person names kept)
  Contrapunto     <- Sejong                      ("King Sejong the Great", "Sejong Station", "Sejong City" kept)
  Ariun Nuur      <- Vostok                      ("Lake Vostok", "Vostok Station/ice/Subglacial" kept; the central scientific
                                                  district keeps the name "Vostok", so READ the dry run for district mentions)

The six files (under Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/):
  Official_Population_Census.md
  Division_of_Industry/09_Per_City_Baseline_Run.md
  Division_of_Industry/10_Validation_Findings_2026-09-01.md
  Division_of_Industry/11_Caloric_Rebuild_and_Livestock_Tier.md
  Division_of_Industry/13_National_Balance_Under_the_Ruling.md
  Division_of_Industry/16_Per_City_Three_Tier_Run.md

usage:
  python3 rename_sweep_held_files.py            # DRY RUN: counts and a sample of lines per file, changes nothing
  python3 rename_sweep_held_files.py --apply    # backs the six files up to Archive/ first, then applies

Same rules as the main sweep: placeholder braces -> official names; path references to renamed files are remapped; slash-joined
city lists ("Hub/Sayowa") are replaced but real paths are not; lines that quote a developer verbatim are NOT specially
protected here, so READ THE DRY RUN. Afterwards run Tools/quotation_audit.py on the Mirny pass (expect misses only in frozen
pass records that quote an old name) and add a line to City_Renames_Alias_Table_2026-10-03.md.
Afterwards: re-run quotation_audit.py, and ALSO check the "Vostok" district mentions by hand (DR-42).
"""
import os, re, sys, shutil, time, collections

GDD = "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
C = "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/"
FILES = [C + "Official_Population_Census.md"] + [C + "Division_of_Industry/" + f for f in (
    "09_Per_City_Baseline_Run.md", "10_Validation_Findings_2026-09-01.md", "11_Caloric_Rebuild_and_Livestock_Tier.md",
    "13_National_Balance_Under_the_Ruling.md", "16_Per_City_Three_Tier_Run.md")]
APPLY = "--apply" in sys.argv

PATHS = [
    (r'(?<!Mirny_Subnet/)(?<![\w])Bunger_Hills_City/', 'Relung_Panen/'),
    (r'(?<!Mirny_Subnet/)(?<![\w])Bunger_Hills_City\.md', 'Relung_Panen.md'),
    (r'(?<!READER/)(?<![\w])Abowasa\.md', 'Santa_Luce.md'),
    (r'(?<!READER/)(?<![\w])Sayowa\.md', 'Temirotkel.md'),
    (r'(?<![\w])Princess_Elisabeth\.md', 'Utstein.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Abowasa/Abowasa_Catalog\.md', r'\1Santa_Luce/Santa_Luce_Catalog.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Sayowa/Sayowa_Catalog\.md', r'\1Temirotkel/Temirotkel_Catalog.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Princess_Elisabeth/Princess_Elisabeth_Catalog\.md', r'\1Utstein/Utstein_Catalog.md'),
    # batch 2
    (r'(?<!READER/)(?<![\w])Port_Lockroy\.md', 'Puerto_Abrigo.md'), (r'(?<!READER/)(?<![\w])Juan_Carlos\.md', 'Pergamino.md'),
    (r'(?<!READER/)(?<![\w])Sejong\.md', 'Contrapunto.md'), (r'(?<!READER/)(?<![\w])Vostok\.md', 'Ariun_Nuur.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Port_Lockroy/Port_Lockroy_Catalog\.md', r'\1Puerto_Abrigo/Puerto_Abrigo_Catalog.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Juan_Carlos/Juan_Carlos_Catalog\.md', r'\1Pergamino/Pergamino_Catalog.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Sejong/Sejong_Catalog\.md', r'\1Contrapunto/Contrapunto_Catalog.md'),
    (r'(Neo-Races-and-Cultures/\w+_Subnet/)Vostok/Vostok_Catalog\.md', r'\1Ariun_Nuur/Ariun_Nuur_Catalog.md'),
]
BRACES = [(r'\{\{\s*Bunger Hills City\s*\}\}', 'Relung Panen'), (r'\{\{\s*Bunger\s*\}\}', 'Relung Panen'),
          (r'\{\{\s*Abowasa\s*\}\}', 'Santa Luce'), (r'\{\{\s*Princess Elisabeth\s*\}\}', 'Utstein'),
          (r'\{\{\s*Syowa/Showa\s*\}\}', 'Temirötkel'), (r'\{\{\s*Sayowa\s*\}\}', 'Temirötkel')]
PE_KEEP = r'(?! Antarctica| Station| of Belgium|, Belgium| Base)'
TOK = [(re.compile(r'(?<![\w/])Sayowa(?![\w/])(?!\.md)'), 'Temirötkel'), (re.compile(r'(?<![\w/])SAYOWA(?![\w/])'), 'TEMIRÖTKEL'),
       (re.compile(r'(?<![\w/])Abowasa(?![\w/])(?!\.md)'), 'Santa Luce'), (re.compile(r'(?<![\w/])ABOWASA(?![\w/])'), 'SANTA LUCE'),
       (re.compile(r'(?<![\w/])Princess Elisabeth' + PE_KEEP + r'(?![\w])'), 'Utstein'),
       (re.compile(r'(?<![\w/])PRINCESS ELISABETH(?![\w])'), 'UTSTEIN'),
       (re.compile(r'(?<![\w/])Bunger Hills City(?![\w/])'), 'Relung Panen'), (re.compile(r'(?<![\w/])BUNGER HILLS CITY(?![\w/])'), 'RELUNG PANEN'),
       # batch 2 (same token rules as the 2026-10-03 non-held sweep)
       (re.compile(r'(?<![\w/])Port Lockroy(?! harbor| harbour| Bay| Station| base| Base| Antarctic)(?![\w/])(?<!harbor of Port Lockroy)'), 'Puerto Abrigo'),
       (re.compile(r'(?<![\w/])PORT LOCKROY(?![\w/])'), 'PUERTO ABRIGO'),
       (re.compile(r'(?<!King )(?<!after King )(?<![\w/])Juan Carlos(?! I\b)(?! [A-ZÁÉÍÓÚ][a-záéíóúñ]+(?<!Station))(?![\w/])'), 'Pergamino'),
       (re.compile(r'(?<![\w/])JUAN CARLOS(?![\w/])'), 'PERGAMINO'),
       (re.compile(r'(?<!King )(?<![\w/])Sejong(?! the Great)(?! Station)(?! City)(?![\w/])(?!\.md)'), 'Contrapunto'),
       (re.compile(r'(?<![\w/])SEJONG(?![\w/])'), 'CONTRAPUNTO'),
       (re.compile(r'(?<!Lake )(?<![\w/])Vostok(?! Station)(?! ice)(?! Subglacial)(?! subglacial)(?![\w/])(?!\.md)(?!\.html)'), 'Ariun Nuur'),
       (re.compile(r'(?<![\w/])VOSTOK(?![\w/])'), 'ARIUN NUUR')]
SLASH = [(re.compile(r'Sayowa(?![\w])'), 'Temirötkel'), (re.compile(r'Abowasa(?![\w])'), 'Santa Luce'),
         (re.compile(r'Princess Elisabeth' + PE_KEEP + r'(?![\w])'), 'Utstein'),
         (re.compile(r'(?<!King )Sejong(?! the Great| Station| City)(?![\w])'), 'Contrapunto'),
         (re.compile(r'(?<!Lake )Vostok(?! Station| ice| Subglacial| subglacial)(?![\w])'), 'Ariun Nuur'),
         (re.compile(r'(?<!King )Juan Carlos(?! I\b)(?![\w])'), 'Pergamino'),
         (re.compile(r'Port Lockroy(?! harbor| harbour| Bay| Station| base| Base| Antarctic)(?![\w])'), 'Puerto Abrigo')]


def chunk(t, pos):
    s = pos
    while s > 0 and not t[s - 1].isspace(): s -= 1
    e = pos
    while e < len(t) and not t[e].isspace(): e += 1
    return t[s:e]


def transform(t):
    stats = collections.Counter()
    for pat, rep in PATHS:
        t, n = re.subn(pat, rep, t); stats['path'] += n
    for pat, rep in BRACES:
        t, n = re.subn(pat, rep, t); stats['brace'] += n
    for rx, rep in TOK:
        t, n = rx.subn(rep, t); stats['name'] += n
    for rx, rep in SLASH:                                   # slash-joined city lists; never real paths
        out, last = [], 0
        for m in rx.finditer(t):
            c = chunk(t, m.start())
            if '/' not in c or '_' in c or '.md' in c or 'Megasheet' in c or 'Background-Lore' in c or 'READER' in c or c.startswith('`'):
                continue
            out.append(t[last:m.start()]); out.append(rep); last = m.end(); stats['slash'] += 1
        out.append(t[last:]); t = ''.join(out)
    return t, stats


def main():
    if APPLY:
        arch = GDD + "Archive/Pre_Rename_Sweep_Held_Files_" + time.strftime("%Y-%m-%d_%H%M") + "/"
        os.makedirs(arch, exist_ok=True)
        for f in FILES: shutil.copy2(GDD + f, arch + os.path.basename(f))
        print("backed up the six files to", arch)
    for f in FILES:
        p = GDD + f; t = open(p, encoding="utf8").read(); nt, st = transform(t)
        print(f"{os.path.basename(f):55s} {dict(st)}")
        if not APPLY:                                       # sample of changed lines
            shown = 0
            for a, b in zip(t.split("\n"), nt.split("\n")):
                if a != b and shown < 3: print("     -", a.strip()[:150]); print("     +", b.strip()[:150]); shown += 1
        elif nt != t:
            open(p, "w", encoding="utf8").write(nt)
    print("APPLIED" if APPLY else "DRY RUN ONLY - nothing was changed. Re-run with --apply after the Mirny pass has finished.")


if __name__ == "__main__":
    main()
