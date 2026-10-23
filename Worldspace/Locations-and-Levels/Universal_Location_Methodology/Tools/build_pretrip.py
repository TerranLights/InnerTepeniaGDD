#!/usr/bin/env python3
"""
BUILD PRE-TRIP  —  generates a city's `00.0_Pre-Trip_Inspection.md` and `00.2_Position_Coverage_Ledger.md`
(November To-Do N-4, 2026-10-21).

  usage:  python3 build_pretrip.py <city_key> [--out DIR] [--write] [--force]
          python3 build_pretrip.py --all --write      (every city in the table; never overwrites without --force)
          python3 build_pretrip.py --list

  <city_key>   the pass-folder name (e.g. Cape_Adare, Santa_Luce, Utstein). `--list` prints all keys.
  --out DIR    write the two files into DIR (default: print a summary only; nothing is written)
  --write      write into the city's own pass folder (refuses to overwrite an existing file unless --force)

HOW IT WORKS
  The template is CASEY'S Pre-Trip sheet as of 2026-09-30 (the newest format), kept as a frozen copy beside this script. Every STANDARD line (the
  runbook's step and phase text, the laws, the carve-outs, the handoff sweep, the T8 procedure) is carried unchanged
  except for path substitution. Every CITY-SPECIFIC line is REGENERATED for the city:
    §A alias set (drafted mechanically from the spec header, the rename notice and the census heading; the developer confirms)
    §B / §C / §D / §F / §H / §K  paths (spec, culture, robot-culture, enneagram, vision notes, megasheet, concept art,
                                  neo-race catalog, research log, climate READER, datasheets, pass files)
    census / extent / Division-of-Industry `16` line ranges, and every "Names <city> at L…" row, from a live scan
    §E / §F rows, §I the verification block (raw output of the checks run by THIS script), §J rename rulings
  The generator never copies another city's line numbers: it refuses to run if an anchor in the template has moved.

  WHAT IT DOES NOT DO: judge. The alias set, a hit that is really about a different place, and any ruling that touches
  the city are flagged for the developer in §J; nothing is guessed. It does not read withheld material: megasheets,
  vision notes, culture sheets and enneagram sheets are only tested for existence (and the megasheet folder is only
  counted).
"""
import glob
import os
import re
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ULM = os.path.abspath(os.path.join(HERE, ".."))
REPO = os.path.abspath(os.path.join(ULM, "..", "..", ".."))
CITIES = os.path.join(REPO, "Worldspace", "Locations-and-Levels", "Outside-World", "Tepenian-Federation", "Locations", "Cities")
INFRA = os.path.join(REPO, "Worldspace", "Locations-and-Levels", "Outside-World", "Tepenian-Federation", "Locations", "Infrastructure")
PASSES = os.path.join(CITIES, "City_Development_Passes")
TEMPLATE_DIR = os.path.join(PASSES, "Mirny_Subnet", "Casey")
# FROZEN copies of Casey's hand-built sheet as it stood on 2026-09-30 (its line numbers are deliberately the OLD ones: the
# generator re-locates them). Casey's live sheet can now be refreshed or filled in without breaking the generator.
TEMPLATE = os.path.join(HERE, "pretrip_template_casey_2026-09-30.md")
TEMPLATE_LEDGER = os.path.join(HERE, "pretrip_ledger_template.md")
TODAY = datetime.date.today().isoformat()

# --------------------------------------------------------------------------------------------------------------------
# The city table.  key = pass-folder name.  Only what cannot be derived is written out.
#   sub       subnet folder name under City_Development_Passes
#   name      the city's CURRENT in-fiction name (as the spec and culture files use it)
#   stem      file stem used by Specs / Local_Cultures / Local_Robot_Culture / Enneagram / Vision Notes / Neo-Races
#   former    earlier names still present in the held (not yet swept) files and in records
#   extra     other strings that name the same place in files (real-station names), searched with the names
#   reader    stem of the climate READER file (keyed by the real station, which can differ from the city name)
#   mega      megasheet folder name; concept   concept-art folder name   (mega keeps the pre-rename names; the concept-art folders were renamed 2026-10-23)
#   pat       optional regex that replaces the default name search (for names that are also ordinary words)
#   ambig     a note printed in §A when the name is shared with a subnet or an ordinary word
# --------------------------------------------------------------------------------------------------------------------
def C(sub, name, stem=None, **kw):
    d = dict(sub=sub, name=name, stem=stem or name.replace(" ", "_"), former=[], extra=[], ambig=None, pat=None, existing=False)
    d.update(kw)
    return d


CITY = {
    "Amundsen_Station": C("Amundsen_Station", "Amundsen Station", extra=["Amundsen-Scott"], reader="Amundsen_Station",
                          specsub="Amundsen-Scott subnet", flat=True),
    "Byrd": C("Byrd_Subnet", "Byrd", reader="Byrd", pat=r"\bByrd\b",
              ambig="the name is shared with the subnet and with Richard Byrd; hits exclude `Byrd subnet` phrases only"),
    # Halley subnet
    "Santa_Luce": C("Halley_Subnet", "Santa Luce", stem="Santa_Luce", former=["Abowasa"], extra=["Aboa Station", "Wasa Research Station"], reader="Aboa", mega="Abowasa",
                 concept="Santa_Luce", renamed="`DR-36`: formerly Abowasa (the Aboa + Wasa fusion)"),
    "Belgrano": C("Halley_Subnet", "Belgrano", reader="Belgrano"),
    "Halley": C("Halley_Subnet", "Halley", reader="Halley",
                ambig="the city and its subnet share the name; hits exclude `Halley subnet` phrases, but a line may still be about the subnet"),
    "Lazar": C("Halley_Subnet", "Lazar", reader="Lazar", extra=["Novolazarevskaya"]),
    "Neumayer": C("Halley_Subnet", "Neumayer", reader="Neumayer"),
    "Utstein": C("Halley_Subnet", "Utstein", former=["Princess Elisabeth"], extra=["Utsteinen"],
                            reader="Princess_Elizabeth", mega="Princess_Elisabeth", concept="Utstein",
                            renamed="`DR-38`: formerly Princess Elisabeth"),
    "Sanay": C("Halley_Subnet", "Sanay", reader="Sanay", extra=["SANAE"]),
    "Troll": C("Halley_Subnet", "Troll", reader="Troll", pat=r"\bTroll\b",
               ambig="`Troll` is also an ordinary word; hits are case-sensitive and may include non-city uses"),
    # Janbogo subnet
    "Cape_Adare": C("Janbogo_Subnet", "Cape Adare", reader="Cape_Adare"),
    "Fort_McMurdo": C("Janbogo_Subnet", "Fort McMurdo", extra=["McMurdo Station"], reader="Fort_McMurdo"),
    "Janbogo": C("Janbogo_Subnet", "Janbogo", extra=["Jang Bogo"], reader="Janbogo",
                 ambig="the city and its subnet share the name; hits exclude `Janbogo subnet` phrases, but a line may still be about the subnet"),
    "Scott": C("Janbogo_Subnet", "Scott", extra=["Scott Base"], reader="Scott",
               pat=r"(?<!Amundsen-)(?<!Amundsen–)(?<!Amundsen—)(?<!Captain )(?<!Robert Falcon )\bScott\b(?! Polar)(?!'s [Hh]ut)",
               ambig="`Scott` is also a person's name and part of `Amundsen-Scott`; the search excludes those forms, but read each line"),
    "Zukelli": C("Janbogo_Subnet", "Zukelli", extra=["Zucchelli"], reader="Zukelli"),
    # Mawson subnet
    "Dome_Fuji": C("Mawson_Subnet", "Dome Fuji", reader="Dome_Fuji",
                   ambig="the developer's interim colloquial name `The Temple` is NOT searched (it is an ordinary phrase); the official name is pending"),
    "Mawson": C("Mawson_Subnet", "Mawson", reader="Mawson",
                ambig="the city and its subnet share the name; hits exclude `Mawson subnet` phrases, but a line may still be about the subnet"),
    "Temirotkel": C("Mawson_Subnet", "Temirotkel", stem="Temirotkel", former=["Sayowa"], extra=["Temirötkel", "Syowa"],
                reader="Sayowa", mega="Sayowa", concept="Temirotkel", renamed="`DR-37`: formerly Sayowa"),
    # Palmer subnet
    "Esperanza": C("Palmer_Subnet", "Esperanza", reader="Esperanza"),
    "Pergamino": C("Palmer_Subnet", "Pergamino", former=["Juan Carlos"], reader="Juan_Carlos", mega="Juan_Carlos",
                     concept="Pergamino", renamed="`DR-41`: formerly Juan Carlos"),
    "Marambio": C("Palmer_Subnet", "Marambio", reader="Marambio"),
    "Palmer_City": C("Palmer_Subnet", "Palmer City", extra=["Palmer Station"], reader="Palmer_City"),
    "Puerto_Abrigo": C("Palmer_Subnet", "Puerto Abrigo", former=["Port Lockroy"], reader="Port_Lockroy", mega="Port_Lockroy",
                      concept="Puerto_Abrigo", renamed="`DR-40`: formerly Port Lockroy"),
    "Rothera": C("Palmer_Subnet", "Rothera", reader="Rothera"),
    "Contrapunto": C("Palmer_Subnet", "Contrapunto", former=["Sejong"], reader="Sejong", mega="Sejong", concept="Contrapunto",
                renamed="`DR-43`: formerly Sejong"),
    "Signy": C("Palmer_Subnet", "Signy", reader="Signy"),
    # Mirny subnet, the 38th city (added 2026-10-21; official name confirmed the same day; its pass is not in the November run)
    "Relung_Panen": C("Mirny_Subnet", "Relung Panen", former=["Bunger Hills City", "Bunger Hills"], extra=["Bunger Hills oasis", "Knox Coast"],
                      reader="Relung_Panen", mega="Relung_Panen", concept="Relung_Panen",
                      reader_path=os.path.join(CITIES, "Relung_Panen", "Climate.md"),
                      renamed="`DR-39`: formerly the placeholder Bunger Hills City"),
    # ---- cities that already HAVE a hand-built sheet: listed so a side-by-side refresh can be generated into a scratch
    #      folder (`--out DIR`) and compared. `--all` skips them; `--write` refuses them.
    "Casey": C("Mirny_Subnet", "Casey", reader="Casey", existing=True),
    "Davis": C("Mirny_Subnet", "Davis", reader="Davis", existing=True),
    "Kunlun": C("Mirny_Subnet", "Kunlun", reader="Kunlun", existing=True,
                extra=["Kunlun Station", "Kunlun Skiway", "Dome A", "Dome Argus", "DOME PLATEAU DOME A", "AYM00089577"]),
    "Mirny": C("Mirny_Subnet", "Mirny", reader="Mirny", existing=True,
               ambig="the city and its subnet share the name; hits exclude `Mirny subnet` phrases"),
    "Denison": C("Janbogo_Subnet", "Denison", reader="Denison", existing=True, extra=["Commonwealth Bay"]),
    "Dumont_dUrville": C("Janbogo_Subnet", "Dumont d'Urville", stem="Dumont_dUrville", reader="Dumont_dUrville", existing=True,
                         extra=["Dumont d’Urville", "D10 Skiway", "DdU", "Petrel Island", "Île des Pétrels"]),
    "Ariun_Nuur": C("Mirny_Subnet", "Ariun Nuur", stem="Ariun_Nuur", former=["Vostok"], extra=["Vostok Skiway"], reader="Vostok", existing=True,
                renamed="`DR-42`: formerly Vostok"),
}
for _k, _v in CITY.items():
    _v["folder"] = _k
    _v.setdefault("specsub", _v["sub"].replace("_Subnet", " subnet").replace("_", " "))
    _v.setdefault("mega", _k)
    _v.setdefault("concept", _k)
    _v.setdefault("renamed", None)
    if _v["specsub"].endswith("subnet") is False and _k != "Amundsen_Station":
        _v["specsub"] += " subnet"

SKIP_NOTE = {
    "Concordia": "hub city; its 13 districts use the district methodology, not this one",
    "Shirayuki": "its ULM pass is complete (Tri-Cities)", "Sinheung": "its ULM pass is complete (Tri-Cities)",
}


# --------------------------------------------------------------------------------------------------------------------
def read_lines(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().split("\n")


def ex(path):
    return os.path.exists(path)


def fmt_lines(nums, prefix="L"):
    """[21, 28, 152, 153] -> 'L21, L28, L152–153' (Casey's style)."""
    nums = sorted(set(nums))
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append("%s%d" % (prefix, nums[i]) if i == j else "%s%d–%d" % (prefix, nums[i], nums[j]))
        i = j + 1
    return ", ".join(out)


def abbr_range(a, b):
    return "%d–%d" % (a, b) if a != b else "%d" % a


class Ctx:
    def __init__(self, key):
        c = CITY[key]
        self.key, self.c = key, c
        self.sub, self.folder, self.name, self.stem = c["sub"], c["folder"], c["name"], c["stem"]
        self.former, self.extra = c["former"], c["extra"]
        self.specsub = c["specsub"]
        self.pass_dir = os.path.join(PASSES, self.sub, self.folder)
        self.spec = os.path.join(CITIES, "Specs", self.specsub, self.stem + ".md")
        self.culture = os.path.join(CITIES, "Local_Cultures", self.sub, self.stem + ".md")
        self.robot = os.path.join(CITIES, "Local_Robot_Culture", self.sub, self.stem + ".md")
        self.enn = os.path.join(CITIES, "City_Enneagram_Personalities", self.sub, self.stem + ".md")
        self.vision = os.path.join(CITIES, "City_Vision_Notes", self.stem + ".md")
        self.mega_dir = os.path.join(CITIES, "City_Megasheets", self.sub, c["mega"])
        self.concept = os.path.join(CITIES, "City_Concept-Art", self.sub, c["concept"])
        if c.get("flat"):       # Amundsen Station: its files sit directly in the subnet-level folders
            self.mega_dir = os.path.join(CITIES, "City_Megasheets", self.sub)
            self.concept = os.path.join(CITIES, "City_Concept-Art", self.sub)
        self.neo = os.path.join(REPO, "Neo-Races-and-Cultures", self.sub, self.stem, self.stem + "_Catalog.md")
        self.neo_readme = os.path.join(REPO, "Neo-Races-and-Cultures", "README.md")
        self.rlog = os.path.join(CITIES, "Research_Logs", self.stem + "_Research_Log.md")
        self.reader = c.get("reader_path") or os.path.join(REPO, "Reference", "Real-World", "Climate Data", "READER", c["reader"] + ".md")
        self.names = [self.name] + self.former + self.extra
        self.rx = self._compile()
        self.claims = []          # (file, [line numbers], note) — re-read in the verification block
        self.flags = []           # things for the developer, printed in §J

    def _compile(self):
        if self.c["pat"]:
            return re.compile(self.c["pat"])
        alts = sorted({re.escape(n) for n in self.names}, key=len, reverse=True)
        return re.compile(r"(?<![A-Za-z])(?:%s)(?![A-Za-z])" % "|".join(alts))

    def strip_subnet(self, line):
        for n in [self.name] + self.former:
            line = re.sub(r"%s[ _-]?[Ss]ub-?net" % re.escape(n), "", line)
        return line

    def hits(self, path):
        if not ex(path) or os.path.isdir(path):
            return None
        out = []
        for i, ln in enumerate(read_lines(path), 1):
            if self.rx.search(self.strip_subnet(ln)):
                out.append(i)
        return out

    def claim(self, path, nums):
        self.claims.append((path, list(nums)))


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# Re-location of the STANDARD citations (method documents). Casey's sheet was verified against the files as they stood on
# 2026-09-30; the runbook and spine gained and lost lines afterwards. Every number is moved to where its line is NOW, by
# matching line text between the 2026-09-30 state and today (difflib). Governing step/phase ranges are instead recomputed
# from the live headings, which is stricter.
# --------------------------------------------------------------------------------------------------------------------
import subprocess
import difflib

METHOD_FILES = ("00_RUNBOOK.md", "03_The_Phase_Spine.md", "04_QA_Gates_and_Differentiation.md", "05_The_Input_Contract.md",
                "02_Generators_Capability_and_Symbols.md", "PRE-TRIP_INSPECTION_RECIPE_TRIAL.md", "PRE-TRIP_INSPECTION_RECIPE.md")
_TOK = re.compile(r"[A-Za-z0-9_.\-]+\.md")
_GRP = re.compile(r"(?:\blines?\s+|(?<![A-Za-z0-9§])L)(\d+(?:[–-]\d+)?(?:(?:,\s*|\s+and\s+|\s*\+\s*)(?:lines?\s+)?L?\d+(?:[–-]\d+)?)*)")
_maps, _base = {}, [None]
REMAP_LOG = []


def base_ref():
    if _base[0] is None:
        r = subprocess.run(["git", "-C", REPO, "rev-list", "-1", "--before=2026-10-01T00:00:00", "HEAD"], capture_output=True)
        _base[0] = r.stdout.decode().strip()
    return _base[0]


def method_map(fname):
    if fname in _maps:
        return _maps[fname]
    path = os.path.join(ULM, fname)
    rel = os.path.relpath(path, REPO)
    r = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (base_ref(), rel)], capture_output=True)
    if r.returncode != 0 or not ex(path):
        _maps[fname] = None
        return None
    old = r.stdout.decode("utf-8", "replace").split("\n")
    new = read_lines(path)
    sm = difflib.SequenceMatcher(None, [l.strip() for l in old], [l.strip() for l in new], autojunk=False)
    mp = {}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                mp[i1 + k + 1] = j1 + k + 1
    _maps[fname] = (mp, len(old))
    return _maps[fname]


def live_ranges():
    """(runbook step ranges, spine phase ranges) recomputed from today's headings: start = heading, end = line before the next."""
    rb = read_lines(os.path.join(ULM, "00_RUNBOOK.md"))
    heads = [(i, m.group(1)) for i, ln in enumerate(rb, 1) for m in [re.match(r"^# Step (−1|\d+) —", ln)] if m]
    steps = []
    for k, (i, nm) in enumerate(heads):
        end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len([l for l in rb if True]) - (1 if rb and rb[-1] == "" else 0)
        steps.append((nm, i, end))
    sp = read_lines(os.path.join(ULM, "03_The_Phase_Spine.md"))
    ph = [(i, int(m.group(1))) for i, ln in enumerate(sp, 1) for m in [re.match(r"^# PHASE (\d+) —", ln)] if m]
    top = [i for i, ln in enumerate(sp, 1) if ln.startswith("# ") and not ln.startswith("# PHASE")]
    phases = []
    for k, (i, n) in enumerate(ph):
        nxt = ph[k + 1][0] if k + 1 < len(ph) else next((t for t in top if t > i), len(sp) + 1)
        phases.append((n, i, nxt - 1))
    return steps, phases


def build_range_map(T):
    """Pair Casey's old governing ranges (in order) with the live ones. Returns {(file, a, b): (a2, b2)}."""
    steps, phases = live_ranges()
    old_rb, old_sp = set(), set()
    for ln in T:
        for m in re.finditer(r"00_RUNBOOK\.md`?\*{0,2} lines (\d+)[–-](\d+)", ln):
            a, b = int(m.group(1)), int(m.group(2))
            if a >= 2400:
                old_rb.add((a, b))
        for m in re.finditer(r"03_The_Phase_Spine\.md`?\*{0,2} lines (\d+)[–-](\d+)", ln):
            old_sp.add((int(m.group(1)), int(m.group(2))))
    old_rb, old_sp = sorted(old_rb), sorted(old_sp)
    if len(old_rb) != len(steps) or len(old_sp) != len(phases):
        sys.exit("RANGE COUNT MISMATCH: template has %d runbook step ranges / %d spine ranges; live file has %d steps / %d phases"
                 % (len(old_rb), len(old_sp), len(steps), len(phases)))
    rmap = {}
    for (a, b), (_, s, e) in zip(old_rb, steps):
        rmap[("00_RUNBOOK.md", a, b)] = (s, e)
    for (a, b), (_, s, e) in zip(old_sp, phases):
        rmap[("03_The_Phase_Spine.md", a, b)] = (s, e)
    return rmap, steps, phases


def remap_line(line, rmap, lineno=0):
    """Move every method-document citation in a STANDARD line to where its line is today."""
    def grp(m):
        pre = line[:m.start()]
        toks = _TOK.findall(pre)
        fname = os.path.basename(toks[-1]) if toks else None
        ctx_before = line[max(0, m.start() - 12):m.start()]
        if fname not in METHOD_FILES:
            if ctx_before.endswith("live ") or ctx_before.endswith("live lines ") or not toks:
                fname = "00_RUNBOOK.md" if (ctx_before.endswith("live ") or "runbook" in pre[-60:].lower()) else fname
            if fname not in METHOD_FILES:
                return m.group(0)
        text = m.group(1)
        pair = re.match(r"^(\d+)[–-](\d+)$", text)
        if pair and ctx_before.endswith("live ") and fname == "00_RUNBOOK.md":
            # the extract cards' "live lines A–B govern" note: take the step's own computed range (the nearest old start)
            near = [k for k in rmap if k[0] == fname and abs(k[1] - int(pair.group(1))) <= 3]
            if near:
                a2, b2 = rmap[min(near, key=lambda k: abs(k[1] - int(pair.group(1))))]
                new = "%d–%d" % (a2, b2)
                if new != text:
                    REMAP_LOG.append((lineno, fname, text, new))
                return m.group(0).replace(text, new, 1)
        if pair and (fname, int(pair.group(1)), int(pair.group(2))) in rmap:
            a2, b2 = rmap[(fname, int(pair.group(1)), int(pair.group(2)))]
            new = "%d–%d" % (a2, b2)
            if new != text:
                REMAP_LOG.append((lineno, fname, text, new))
            return m.group(0).replace(text, new, 1)
        if fname in ("00_RUNBOOK.md", "03_The_Phase_Spine.md"):
            return m.group(0)       # every other runbook/spine number is re-located by ANCHOR TEXT (method_fixes), never by position
        mm = method_map(fname)
        if mm is None:
            return m.group(0)
        mp, nold = mm

        def one(n):
            v = int(n.group(0))
            nv = mp.get(v) if v <= nold else v
            if nv is None:
                REMAP_LOG.append((lineno, fname, str(v), "NOT RE-LOCATABLE (line edited since)"))
                return n.group(0)
            if nv != v:
                REMAP_LOG.append((lineno, fname, str(v), str(nv)))
            return str(nv)
        return m.group(0).replace(text, re.sub(r"\d+", one, text), 1)
    return _GRP.sub(grp, line)


def method_fixes(T):
    """Runbook/spine citations that are not governing ranges, re-located by ANCHOR TEXT in today's files.
    Returns [(old, new)] to apply to the template; refuses to run if an old string is missing from the template."""
    rb = read_lines(os.path.join(ULM, "00_RUNBOOK.md"))
    sp = read_lines(os.path.join(ULM, "03_The_Phase_Spine.md"))

    def f(lines, rx, start=1, end=None):
        for i in range(start, (end or len(lines)) + 1):
            if re.search(rx, lines[i - 1]):
                return i
        sys.exit("ANCHOR NOT FOUND: %r (from line %d)" % (rx, start))
    t18 = f(rb, r"BINDING — \*\*`T1`–`T8` RUN ON EVERY STEP")
    law0 = f(rb, r"^# LAW 0 —")
    law0r_h = f(rb, r"LAW 0-R — RESEARCH FULLY")
    law0r = f(rb, r"GOVERNING\. Added 2026-09-06", law0r_h)
    nff = f(rb, r"^# ⛔⛔⛔ THE LAW OF NO FORCED FIT")
    one = f(rb, r"^# ⛔⛔⛔ THE LAW OF ONE LOCATION")
    div = f(rb, r"Refusing all ethnic material", 2000)
    c9b = f(rb, r"^## C\.9b ")
    c9d = f(rb, r"^## .*C\.9d ")
    c9tab = f(rb, r"^\|", f(rb, r"^## C\.9 "))
    lay = f(rb, r"THE LAYERING LAW")
    c8c = f(rb, r"^### C\.8c")
    hdr = f(rb, r"^\| Phase \| Address \|", c8c)
    row0 = f(rb, r"^\| \*\*0\*\* \|", hdr)
    row10 = f(rb, r"^\| \*\*10\*\* \|", hdr)
    geo = f(rb, r"Geothermal_Heating\.md", 600, 900)
    step3 = f(rb, r"^# Step 3 — ")
    s3ptr = f(rb, r"Real-World_Basis_Extrapolation_Method\.md", step3, step3 + 120)
    neo = f(rb, r"^\| `Neo-Races-and-Cultures/`")
    p06 = f(rb, r"06_Worked_Example_Provenance\.md` still applies in warm mode")
    reg = f(sp, r"location registries", 250)
    sp10 = f(sp, r"^\| \*\*10\*\* Catalog")
    pairs = [
        ("00_RUNBOOK.md` L2696–2698", "00_RUNBOOK.md` L%d–%d" % (t18, t18 + 2)),
        ("00_RUNBOOK.md` L307 ", "00_RUNBOOK.md` L%d " % law0),
        ("00_RUNBOOK.md` L2569 ", "00_RUNBOOK.md` L%d " % law0r),
        ("00_RUNBOOK.md` L376 ", "00_RUNBOOK.md` L%d " % nff),
        ("00_RUNBOOK.md` L428 ", "00_RUNBOOK.md` L%d " % one),
        ("00_RUNBOOK.md` L2177;", "00_RUNBOOK.md` L%d;" % div),
        ("`§C.9b` L2088", "`§C.9b` L%d" % c9b),
        ("`§C.9d` L2147", "`§C.9d` L%d" % c9d),
        ("00_RUNBOOK.md` L1980 (per-phase table, Phase 10)", "00_RUNBOOK.md` L%d (per-phase table, Phase 10)" % row10),
        ("03_The_Phase_Spine.md` L219 ", "03_The_Phase_Spine.md` L%d " % sp10),
        ("00_RUNBOOK.md` L215 ", "00_RUNBOOK.md` L%d " % lay),
        ("**L1968–1980**", "**L%d–%d**" % (c8c + 2, row10)),
        ("Phase 0 row (L1970)", "Phase 0 row (L%d)" % row0),
        ("(Phase 0 block, L285–286)", "(Phase 0 block, L%d–%d)" % (reg, reg + 1)),
        ("Runbook's table (L1980)", "Runbook's table (L%d)" % row10),
        ("registry row L745", "registry row L%d" % geo),
        ("per-phase table (L1970–1980)", "per-phase table (L%d–%d)" % (row0, row10)),
        ("table from L2056", "table from L%d" % c9tab),
        ("Step 3 (L2629)", "Step 3 (L%d)" % s3ptr),
        ("runbook lines 2508–2509", "runbook lines %d–%d" % (p06, p06 + 1)),
    ]
    joined = "\n".join(T)
    for old, _ in pairs:
        if old not in joined:
            sys.exit("TEMPLATE MOVED: expected %r in Casey's sheet" % old)
    return pairs, dict(neo=neo, hdr=hdr, row0=row0, row10=row10)


def spec_header(ctx):
    """Raw material for §A: the 'Based on' line, any rename notice, and rename/alias keyword hits — all in the spec only."""
    if not ex(ctx.spec):
        return None
    ls = read_lines(ctx.spec)
    based, based_n = None, None
    for i, ln in enumerate(ls[:60], 1):
        if ln.startswith("**Based on:**"):
            based, based_n = ln[len("**Based on:**"):].strip(), i
            break
    notice = [(i, ln) for i, ln in enumerate(ls[:30], 1) if "RENAMED" in ln or "NAME RULED" in ln]
    kw = re.compile(r"formerly|also known|a\.k\.a|renamed|working title|nickname|previously called|originally called|"
                    r"candidate name|alternative name|name considered|name dropped|name rejected", re.I)
    kwhits = [i for i, ln in enumerate(ls, 1) if kw.search(ln)]
    scripts = [i for i, ln in enumerate(ls[:25], 1) if re.search(r"[^\x00-ɏ‐-‧←-⯿\U0001F000-\U0001FAFF°′″]", ln)]
    return dict(based=based, based_n=based_n, notice=notice, kwhits=kwhits, scripts=scripts, n=len(ls))


def split_places(based):
    """Split a 'Based on' value into names, dropping parentheses and coordinates."""
    if not based:
        return []
    s = re.sub(r"\([^)]*\)", "", based)
    s = re.sub(r"~?\d+°[^,;]*", "", s)
    parts = [p.strip(" .—-") for p in re.split(r"[,;]", s)]
    return [p for p in parts if p and 2 < len(p) <= 45]


def census_data(ctx):
    path = os.path.join(CITIES, "Official_Population_Census.md")
    ls = read_lines(path)
    names = [ctx.name] + ctx.former
    entry = heading = None
    for i, ln in enumerate(ls[:473], 1):
        if i < 31:
            continue
        m = re.match(r"^\*\*(.+?)\*\*", ln)
        if m and any(re.sub(r"[{}\s]+", " ", m.group(1)).strip() == n or re.sub(r"[{}]", "", m.group(1)).strip() == n
                     for n in names):
            heading = i
            # the entry runs from two lines under the heading to the line before the next `---` separator (notes included)
            k = next((x for x in range(i + 1, len(ls) + 1) if ls[x - 1].strip() == "---"), len(ls) + 1)
            e = k - 1
            while e > i + 2 and not ls[e - 1].strip():
                e -= 1
            entry = (i + 2, e)
            break
    rows1, rows2 = [], []
    for i, ln in enumerate(ls, 1):
        if ln.startswith("|"):
            cells = [c.strip().strip("*`") for c in ln.split("|")[1:-1]]
            if len(cells) > 1 and any(re.sub(r"[{}]", "", cells[1]).strip() == n for n in names):
                if 474 <= i < 588:
                    rows1.append(i)
                elif 588 <= i < 679:
                    rows2.append(i)
    others = [i for i in ctx.hits(path) if i != heading and not (entry and entry[0] <= i <= entry[1]) and i not in rows1 + rows2]
    return dict(path=path, heading=heading, entry=entry, rows1=rows1, rows2=rows2, others=others)


def extent_data(ctx):
    path = os.path.join(ULM, "Extent_and_Density_Per_City.md")
    ls = read_lines(path)
    sec = tab = None
    for i, ln in enumerate(ls, 1):
        if ln.startswith("# 10 ·") and "THE OTHER 25" in ln:
            sec = i
        if ln.startswith("## ") and "THE DIFFERENT QUESTION" in ln and sec:
            sec_end = i - 2
        if ln.startswith("## ") and "THE TABLE" in ln:
            tab = i
    tab_end = tab + 3 if tab else None          # heading, blank, header row, separator row
    norm = lambda c: re.sub(r"[^A-Za-z0-9'. \-]+", "", c).strip()
    rows = [i for i in range(1, len(ls) + 1)
            if ls[i - 1].startswith("|") and norm(ls[i - 1].split("|")[1]) in [ctx.name] + ctx.former]
    allhits = ctx.hits(path)
    others = [i for i in allhits if i not in rows]
    return dict(path=path, sec=(sec, sec_end), tab=(tab, tab_end), rows=rows, others=others)


def di16_data(ctx):
    path = os.path.join(CITIES, "Division_of_Industry", "16_Per_City_Three_Tier_Run.md")
    ls = read_lines(path)
    row = None
    for i in range(249, 340):
        if ls[i - 1].startswith("|") and re.sub(r"[*`{}]", "", ls[i - 1].split("|")[1]).strip() in [ctx.name] + ctx.former:
            row = i
            break
    others = [i for i in ctx.hits(path) if i != row]
    return dict(path=path, row=row, others=others)


def names_at(ctx, path, zero_text="Checked by name: zero hits for %s"):
    """'Names X at L…' text for a row, or the zero-hit sentence."""
    h = ctx.hits(path)
    if h is None:
        return "⬜ file not found"
    if not h:
        return zero_text % ctx.name
    ctx.claim(path, h)
    return "Names %s at %s" % (ctx.name, fmt_lines(h))


def hits_in_dir(ctx, d):
    out = []
    for root, _, fs in os.walk(d):
        for f in sorted(fs):
            if f.endswith(".md"):
                p = os.path.join(root, f)
                h = ctx.hits(p)
                if h:
                    out.append((p, h))
    return out


# --------------------------------------------------------------------------------------------------------------------
def build(key):
    ctx = Ctx(key)
    c = ctx.c
    T = read_lines(TEMPLATE)
    R = REPO

    # ---- anchors: refuse to run if the template has moved -------------------------------------------------------
    def need(n, frag):
        if frag not in T[n - 1]:
            sys.exit("TEMPLATE MOVED: line %d of Casey's sheet no longer contains %r — update the generator anchors." % (n, frag))
    for n, frag in [(1, "# Casey — Pre-Trip Inspection"), (3, "**Generated per"), (11, "Every `T8` list"), (21, "| Alias | Status |"),
                    (23, "| **Casey** |"), (30, "Candidate names considered"), (51, "(19 files"), (96, "Official_Population_Census.md"),
                    (97, "Extent_and_Density_Per_City.md"), (124, "16_Per_City_Three_Tier_Run.md"), (138, "does not exist"),
                    (240, "**P** Census"), (252, "Climate READER"), (253, "| Stations |"), (254, "Div. of Industry `16` Half B"),
                    (255, "Physical infrastructure attributes"), (276, "Concept art"), (277, "Physical infrastructure attributes"),
                    (286, "Robot Physiology — GOVERNING"), (287, "Robot Cold Physiology"), (289, "`09` §3.5"),
                    (290, "`11` food layer"), (291, "National Medical and Care Institutes"), (301, "| Highways |"),
                    (302, "| Airports |"), (303, "| Arcanet |"), (304, "| Ports |"), (305, "City_Cross_Subnet_Relationships"),
                    (306, "City_Relationship_Database"), (307, "City_National_Connections"), (315, "Robot Religions"),
                    (316, "National Holidays"), (317, "Ice-Cold Buddhism research"), (318, "Meme Machine extraction"),
                    (319, "True Believer extraction"), (369, "Notable-figure and landmark canon"),
                    (372, "No invented person names"), (390, "is named inside rule/canon files"), (398, "WITHHELD corpus-wide"),
                    (404, "Test-run material"), (478, "```"), (515, "```"), (517, "Per-step and per-phase completeness"),
                    (534, "DR-3"), (542, "MANDATORY, EVERY CITY")]:
        need(n, frag)

    spec = ex(ctx.spec)
    sh = spec_header(ctx)
    cen = census_data(ctx)
    ext = extent_data(ctx)
    d16 = di16_data(ctx)

    # ---- generic path substitution for STANDARD lines ------------------------------------------------------------
    cas = "Casey"
    subs = [
        (os.path.join(PASSES, "Mirny_Subnet", cas) + "/", ctx.pass_dir + "/"),
        (os.path.join(CITIES, "Specs", "Mirny subnet", "Casey.md"), ctx.spec),
        (os.path.join(CITIES, "Local_Cultures", "Mirny_Subnet", "Casey.md"), ctx.culture),
        (os.path.join(CITIES, "Local_Robot_Culture", "Mirny_Subnet", "Casey.md"), ctx.robot),
        (os.path.join(CITIES, "City_Enneagram_Personalities", "Mirny_Subnet", "Casey.md"), ctx.enn),
        (os.path.join(CITIES, "City_Vision_Notes", "Casey.md"), ctx.vision),
        (os.path.join(CITIES, "City_Vision_Notes") + "/", os.path.join(CITIES, "City_Vision_Notes") + "/"),
        (os.path.join(CITIES, "City_Megasheets", "Mirny_Subnet", "Casey") + "/", ctx.mega_dir + "/"),
        (os.path.join(CITIES, "City_Concept-Art", "Mirny_Subnet", "Casey") + "/", ctx.concept + "/"),
        (os.path.join(R, "Neo-Races-and-Cultures", "Mirny_Subnet", "Casey", "Casey_Catalog.md"), ctx.neo),
        (os.path.join(CITIES, "Research_Logs", "Casey_Research_Log.md"), ctx.rlog),
        (os.path.join(R, "Reference", "Real-World", "Climate Data", "READER", "Casey.md"), ctx.reader),
        (os.path.join(R, "Archive", "ULM_Records", "Test_Runs", "Casey_ColdRun_Prep_2026-09-02.md"),
         os.path.join(R, "Archive", "ULM_Records", "Test_Runs", ctx.stem + "_ColdRun_Prep_2026-09-02.md")),
    ]

    del REMAP_LOG[:]
    rmap, steps_live, phases_live = build_range_map(T)
    fix_pairs, anch = method_fixes(T)
    ctx.known = set()
    for _o, _n in fix_pairs:
        ctx.known.update(re.findall(r"\d+(?:–\d+)?", _n))
    for (_f, _a, _b), (_a2, _b2) in rmap.items():
        ctx.known.add("%d–%d" % (_a2, _b2))

    def standard(line, n=0):
        for a, b in subs:
            line = line.replace(a, b)
        for old, new in fix_pairs:
            line = line.replace(old, new)
        line = remap_line(line, rmap, n)
        return line.replace("Casey", ctx.name)

    out = []
    skip = set()

    def put(n, text):
        out.append((n, text))
        skip.add(n)

    P_C, P_R = CITIES, REPO

    # ---- title, header, provenance -------------------------------------------------------------------------------
    put(1, "# %s — Pre-Trip Inspection" % ctx.name)
    put(3, "**Generated per `%s/PRE-TRIP_INSPECTION_RECIPE.md`, %s, by `Tools/build_pretrip.py`** — Casey's sheet is the template; "
           "every city-specific row was computed fresh for this city (see ⚙ below)." % (ULM, TODAY))
    put(11, "*(Developer, 2026-09-29/30.)* Every standard `T8` list in §C and §D below was resolved from the runbook's own step text and")
    put(12, "its REQUIRED READING boxes (on Casey's sheet, 2026-09-30) and is **carried unchanged** here; every city-specific row was computed "
            "for this city. ⛔ **Three measured failures of the copied-list")

    # ---- §A alias set --------------------------------------------------------------------------------------------
    A = ["| Alias | Status |", "|---|---|"]
    A.append("| **%s** | Current in-fiction name%s |" % (ctx.name, (" — renamed: " + c["renamed"]) if c["renamed"] else ""))
    for f in ctx.former:
        A.append("| %s | Earlier name — still present in the held (not yet swept) files and in frozen records; **searched under** |" % f)
    based_places = split_places(sh["based"]) if sh and sh["based"] else []
    if sh and sh["based"]:
        A.append("| **Real-world basis** | Spec header L%d, *\"Based on:\"* — raw text: `%s`. Station/place names drafted from it: %s — ⚠ **mechanical split; the developer confirms which are aliases and which are different places** |"
                 % (sh["based_n"], sh["based"].replace("|", "/"), " · ".join("**%s**" % p for p in based_places) or "none parsed"))
    else:
        A.append("| **Real-world basis** | ⚠ No `**Based on:**` line in the first 60 lines of the spec — not found, **not guessed** (developer supplies) |")
    A.append("| Climate READER key | the file is keyed `%s` — %s |" % (
        ctx.reader, "the same string as the city name, so it resolves directly" if os.path.basename(ctx.reader)[:-3] == ctx.stem
        else "⚠ **differs from the city's current name** (the real station or the pre-rename name); it is the file the spec's climate rows point to"))
    if ctx.extra:
        A.append("| Other strings searched | %s — real-station or variant spellings added to the name search (config, not derived) |" % " · ".join("`%s`" % e for e in ctx.extra))
    if sh:
        if sh["notice"]:
            A.append("| Rename notice | Spec L%s carries a rename notice — the text is in the spec; **not reproduced here** |" % ", L".join(str(i) for i, _ in sh["notice"]))
        else:
            A.append("| No rename flagged | Checked %s: no *RENAMED* / *NAME RULED* notice in the spec's first 30 lines |" % TODAY)
        A.append("| Other scripts / variant spellings | Checked %s: %s; a search of the whole spec for *formerly · also known · a.k.a. · renamed · working title · nickname · previously/originally called · candidate/alternative name · name considered/dropped/rejected* returned %s |"
                 % (TODAY, ("the spec's first 25 lines hold non-Latin script at L%s" % fmt_lines(sh["scripts"]).replace("L", "")) if sh["scripts"] else "the spec's first 25 lines hold no non-Latin script",
                    ("lines %s — read them for aliases" % fmt_lines(sh["kwhits"])) if sh["kwhits"] else "nothing"))
        A.append("| Candidate names considered and dropped | **Not checked:** the withheld megasheet and the vision notes (§F) are not opened in a pre-trip |")
    else:
        A.append("| ⚠ Spec | **No spec file at `%s`** — alias checks could not run |" % ctx.spec)
    if c["ambig"]:
        A.append("| ⚠ Ambiguous name | %s |" % c["ambig"])
    A.append("| ⚠ Draft alias set | **Mechanically drafted %s; unconfirmed.** Every \"Names %s at L…\" row below was found by searching the names above, so a line about a different place with the same name can appear — read each |" % (TODAY, ctx.name))
    # replace lines 21–30 with A
    for n in range(21, 31):
        skip.add(n)
    out.append((21, "\n".join(A)))

    # ---- datasheet status ----------------------------------------------------------------------------------------
    dsd = os.path.join(ctx.pass_dir, "Datasheets")
    nds = len(glob.glob(os.path.join(dsd, "*.md")))
    if nds >= 19:
        ds_line = "(19 files, all present)"
    elif nds:
        ds_line = "(%d of 19 files present)" % nds
    else:
        ds_line = "(**not yet built** — November item N-5; the addresses below are where the files will be created)"
    put(51, T[50].replace("(19 files, all present)", ds_line))
    # replace the pre-built "flat tables" remark on the next line
    put(52, "> consulted alongside `T8`, never instead of it.")
    put(51, standard(T[50].replace("(19 files, all present)", ds_line)))

    # ---- Step 0 census / extent bullets (L96–97) -----------------------------------------------------------------
    parts = ["lines 1–41 (tier definitions)"]
    if cen["entry"]:
        parts.append("**%s** (%s's Section A entry, under its heading at L%d)" % (abbr_range(*cen["entry"]), ctx.name, cen["heading"]))
    else:
        parts.append("⚠ **no Section A entry found for %s**" % ctx.name)
    for r in cen["rows1"]:
        parts.append("**%d** (Census I row)" % r)
    for r in cen["rows2"]:
        parts.append("**%d** (Census II row)" % r)
    if cen["others"]:
        parts.append("other lines naming %s: %s" % (ctx.name, fmt_lines(cen["others"])))
    if not cen["rows2"]:
        parts.append("⚠ **%s has no Census II row** — an empty slot is a result, `No Forced Fit`" % ctx.name)
    ctx.claim(cen["path"], ([cen["heading"]] if cen["heading"] else []) + cen["rows1"] + cen["rows2"] + cen["others"])
    put(96, "  - `%s` %s" % (cen["path"], ", ".join(parts)))
    ext_rows = ("%s's row%s %s" % (ctx.name, "s" if len(ext["rows"]) > 1 else "", ", ".join("**%d**" % r for r in ext["rows"]))) if ext["rows"] else "(no row for %s in the extent table of *the other 25*; a city outside that table has its extent declared elsewhere in the file)" % ctx.name
    put(97, "  - `%s` lines **%s**, **%s** and %s%s" % (
        ext["path"], abbr_range(*ext["sec"]), abbr_range(*ext["tab"]), ext_rows,
        ("; other lines naming %s: %s" % (ctx.name, fmt_lines(ext["others"]))) if ext["others"] else ""))
    ctx.claim(ext["path"], ext["rows"] + ext["others"])

    # ---- Step 2 line 124 (the `16` row) --------------------------------------------------------------------------
    put(124, T[123].replace("line 266", "line %s" % (d16["row"] or "⚠ not found")))
    put(124, standard(T[123]).replace("line 266", "line %s" % (d16["row"] or "⚠ not found")).replace(ctx.name + "'s row", ctx.name + "'s row"))

    # ---- Step 3 research log line (138) --------------------------------------------------------------------------
    t138 = standard(T[137])
    t138 = re.sub(r"\*\(does not exist — confirmed 2026-09-30 — created here, append-only\)\*",
                  ("*(exists)*" if ex(ctx.rlog) else "*(does not exist — confirmed %s — created here, append-only)*" % TODAY), t138)
    put(138, t138)

    # ---- Phase 0 census row (240) --------------------------------------------------------------------------------
    carve = "%s: Section A entry %s; " % (ctx.name, ("L" + abbr_range(*cen["entry"])) if cen["entry"] else "⚠ not found")
    carve += "; ".join(["Census I row L%d" % r for r in cen["rows1"]] + (["Census II row L%d" % r for r in cen["rows2"]]) or [])
    if not cen["rows2"]:
        carve += "; **no Census II row exists** (empty is a result)"
    put(240, standard(T[239]).rsplit("|", 2)[0] + "| %s |" % carve)
    need(240, "Casey: Section A entry")

    # ---- Phase 1 rows (252–255) ---------------------------------------------------------------------------------
    rl = read_lines(ctx.reader) if ex(ctx.reader) else None
    same = os.path.basename(ctx.reader)[:-3] == ctx.stem
    note = ("✅ **No station/city name divergence** — the file is `%s`, same as the city" % ctx.reader) if same else \
           ("⚠ **Station/city name divergence** — the file is keyed `%s.md`, not the city's current name `%s`" % (c["reader"], ctx.stem))
    if rl is not None and not any(re.match(r"\|\s*Jan\s*\|", x) for x in rl):      # no monthly table = a status stub, not data
        note += ". ⚠ **The file is %s %d-line STUB, not a dataset** — open it and record what it says it lacks" % ("an" if len(rl) in (8, 11, 18) else "a", len(rl))
    if rl is None:
        note = "⬜ **No READER file at that address** — the climate row cannot be resolved; record the gap"
    put(252, "| **1** | ⭐⭐ Climate READER | `%s` | %s | `MAPPED` | %s |" % (ctx.reader, "✅" if rl is not None else "⬜", note))
    st = os.path.join(R, "Reference", "Real-World", "Stations", "Antarctic_Stations_With_Airstrips.md")
    put(253, "| **1** | Stations | `%s` | ✅ | background only | %s`%s` also in the folder |" % (
        st, (names_at(ctx, st) + "; ") if True else "",
        os.path.join(R, "Reference", "Real-World", "Stations", "COMNAP_Antarctic_Station_Catalogue.pdf")))
    d16o = ("⚠ The file also names %s in other tables and per-city prose (%s) — read the file's own status header first" % (ctx.name, fmt_lines(d16["others"]))) if d16["others"] else "The file has no other line naming %s" % ctx.name
    ctx.claim(d16["path"], ([d16["row"]] if d16["row"] else []) + d16["others"])
    put(254, "| **1** | Div. of Industry `16` Half B | `%s` | ✅ | ⛔ `QUERYABLE-BY-SCHEMA` | Anchor to structure: table header L241–248, %s's row L%s. Never grep by name. %s |" % (
        d16["path"], ctx.name, d16["row"] or "⚠ not found", d16o))
    mega_f = glob.glob(os.path.join(ctx.mega_dir, "*Physical_Infrastructure_Attributes.md"))
    if not mega_f and ctx.key == "Amundsen_Station":
        mega_f = glob.glob(os.path.join(CITIES, "City_Megasheets", ctx.sub, "Amundsen_Station_Physical_Infrastructure_Attributes.md"))
    mega_p = mega_f[0] if mega_f else os.path.join(ctx.mega_dir, ctx.stem + "_Physical_Infrastructure_Attributes.md")
    put(255, "| **1** | Physical infrastructure attributes | `%s` | %s | ⛔ **WITHHELD corpus-wide** | Record; do not open (§F) |" % (mega_p, "✅" if ex(mega_p) else "⬜"))

    # ---- Phase 3 rows (276, 277) --------------------------------------------------------------------------------
    cdir = ctx.concept
    if ex(cdir):
        files = sorted(os.listdir(cdir))
        real = [f for f in files if f != ".gitkeep"]
        cstate = ("✅ dir exists", "✅ **EMPTY** (`.gitkeep` only) — opened-and-empty is a RESULT" if not real else "%d file(s) present: %s" % (len(real), ", ".join("`%s`" % f for f in real)))
    else:
        cstate = ("⬜ dir missing", "⬜ no concept-art folder for this city")
    put(276, "| **3** | Concept art | `%s/` | %s | — | %s |" % (cdir, cstate[0], cstate[1]))
    if ctx.key == "Amundsen_Station":
        nmega = len([f for f in os.listdir(os.path.join(CITIES, "City_Megasheets", ctx.sub)) if f.startswith("Amundsen_Station_")]) if ex(os.path.join(CITIES, "City_Megasheets", ctx.sub)) else 0
    else:
        nmega = len(os.listdir(ctx.mega_dir)) if ex(ctx.mega_dir) else 0
    put(277, "| **3** | ⛔ Physical infrastructure attributes | *(as Phase 1 — withheld)* | %s | ⛔ **WITHHELD** | The Megasheet folder holds **%d** files (counted with `ls | wc -l`, names not listed) — all withheld together |" % ("✅" if ex(mega_p) else "⬜", nmega))

    # ---- Phase 4 rows (286, 287, 289–291) ------------------------------------------------------------------------
    rp = os.path.join(R, "Worldspace", "Robot_Biology_and_Culture", "Robot_Physiology_and_Cultural_Practices.md")
    rc = os.path.join(R, "Worldspace", "Robot_Biology_and_Culture", "Robot_Cold_Physiology.md")
    di = os.path.join(CITIES, "Division_of_Industry")
    med = os.path.join(CITIES, "National_Medical_and_Care_Institutes.md")
    h_rp, h_rc = ctx.hits(rp), ctx.hits(rc)
    put(286, standard(T[285]).rsplit("|", 2)[0] + "| **Read FIRST.** %s |" % names_at(ctx, rp, "The file does not name %s"))
    put(287, standard(T[286]).rsplit("|", 2)[0] + "| Open the row above FIRST (`M-151`). %s |" % names_at(ctx, rc, "The file does not name %s"))
    put(289, standard(T[288]).rsplit("|", 2)[0] + "| %s |" % names_at(ctx, os.path.join(di, "09_Per_City_Baseline_Run.md"), "—"))
    put(290, standard(T[289]).rsplit("|", 2)[0] + "| §E — food-layer carve-out. %s |" % names_at(ctx, os.path.join(di, "11_Caloric_Rebuild_and_Livestock_Tier.md"), "Checked by name: zero hits for %s"))
    put(291, standard(T[290]).rsplit("|", 2)[0] + "| %s — admissible canon; open and read it |" % names_at(ctx, med))
    # (the row 289 text '—' for zero hits keeps Casey's form)

    # ---- Phase 5 rows (301–307) ---------------------------------------------------------------------------------
    def row(n, label, path, tier, extra_note=""):
        text = names_at(ctx, path)
        put(n, "| **5** | %s | `%s` | ✅ | %s | %s%s |" % (label, path, tier, extra_note, text + (" *(named in the runbook's Phase 5 row, which gives no other detail)*" if label == "Arcanet" else "")))
    row(301, "Highways", os.path.join(INFRA, "Highways.md"), "`MAPPED`")
    row(302, "Airports", os.path.join(INFRA, "Airports.md"), "`MAPPED`")
    row(303, "Arcanet", os.path.join(INFRA, "Arcanet.md"), "`MAPPED`")
    row(304, "Ports", os.path.join(INFRA, "Ports.md"), "`MAPPED`")
    row(305, "City_Cross_Subnet_Relationships", os.path.join(CITIES, "City_Cross_Subnet_Relationships.md"), "`MAPPED`")
    row(306, "City_Relationship_Database", os.path.join(CITIES, "City_Relationship_Database.md"), "`MAPPED`")
    row(307, "City_National_Connections", os.path.join(CITIES, "City_National_Connections.md"), "`MAPPED`",
        "⚠ **Draws on withheld/read-last material by its own stated method — open its header FIRST.** ")

    # ---- Phase 6 rows (315–319) ---------------------------------------------------------------------------------
    rel_hits = hits_in_dir(ctx, os.path.join(R, "Worldspace", "Factions", "Robot_Religions"))
    ice_hits = hits_in_dir(ctx, os.path.join(R, "Reference", "Real-World", "Ice-Cold_Buddhism_Research"))

    def named_in(lst):
        for p, h in lst:
            ctx.claim(p, h)
        return " · ".join("`%s` %s" % (p, fmt_lines(h)) for p, h in lst)
    t315 = standard(T[314]).rsplit("|", 2)[0] + "| A zero return is a RESULT. %s |" % (
        ("%s is named in: %s" % (ctx.name, named_in(rel_hits))) if rel_hits else "Checked by name: zero hits for %s in the folder" % ctx.name)
    put(315, t315)
    put(316, standard(T[315]).rsplit("|", 2)[0] + "| %s. Any observance a pass proposes is a CANDIDATE pending Step 5 |" % names_at(ctx, os.path.join(R, "Worldspace", "National_Holidays.md")))
    put(317, standard(T[316]).rsplit("|", 2)[0] + "| The faith's name is a placeholder. %s |" % (
        ("%s is named in: %s" % (ctx.name, named_in(ice_hits))) if ice_hits else "Checked by name: zero hits for %s in the folder" % ctx.name))
    mm = os.path.join(R, "Reference", "Real-World", "The_Meme_Machine_Extraction.md")
    tb = os.path.join(R, "Reference", "Real-World", "The_True_Believer_Extraction.md")
    put(318, standard(T[317]).rsplit("|", 2)[0] + "| %s |" % names_at(ctx, mm))
    put(319, standard(T[318]).rsplit("|", 2)[0] + "| %s *(named alongside the Meme Machine file in the runbook's Phase 6 row)* |" % names_at(ctx, tb))

    # ---- Phase 10 rows (369, 372) -------------------------------------------------------------------------------
    if spec:
        ls_ = read_lines(ctx.spec)
        nl = next((i for i, l in enumerate(ls_, 1) if l.startswith("## Notable Locations")), None)
        nf = next((i for i, l in enumerate(ls_, 1) if l.startswith("## Notable Figures")), None)
        ph = []
        if nf:
            end = next((i for i in range(nf + 1, len(ls_) + 1) if ls_[i - 1].startswith("## ")), len(ls_) + 1)
            ph = [i for i in range(nf + 1, end) if re.search(r"placeholder|\{\{", ls_[i - 1], re.I)]
    else:
        nl = nf = None
        ph = []
    put(369, "| **10** | Notable-figure and landmark canon | `%s` | %s | `MAPPED` | The runbook names a class, not a file; it resolves to this city's own spec sections `## Notable Locations` (%s) and `## Notable Figures` (%s). The Step −1 contract's line dispositions govern which spans are admitted |" % (
        ctx.spec, "✅" if spec else "⬜", ("L%d" % nl) if nl else "⚠ heading not found", ("L%d" % nf) if nf else "⚠ heading not found"))
    ctx.claim(ctx.spec, [x for x in (nl, nf) if x] + ph) if spec else None
    put(372, "| **10** | ⛔ No invented person names | — | n/a | **RESERVED — role-archetypes only** | %s |" % (
        ("Lines in the spec's `## Notable Figures` section that mention a placeholder or carry a `{{ }}` marker: %s (names only — re-flag each as a placeholder every time it is reused)" % fmt_lines(ph)) if ph else
        "No placeholder-marked person name found in the spec's `## Notable Figures` section by search; role-archetypes only"))

    # ---- §E row (390) -------------------------------------------------------------------------------------------
    rt = os.path.join(R, "Reference", "Real-World", "City_and_District_Research_Topics.md")
    pf = os.path.join(R, "Reference", "Real-World", "Climate Data", "Precipitation_Falls_vs_Lands.md")
    segs = []
    for p in (med, rt, pf):
        h = ctx.hits(p)
        if h:
            ctx.claim(p, h)
            segs.append("`%s` %s" % (p, fmt_lines(h)))
    if ext["others"]:
        segs.append("`%s` %s" % (ext["path"], fmt_lines(ext["others"])))
    if d16["others"] or d16["row"]:
        segs.append("`%s` L%s%s" % (d16["path"], d16["row"], (" and " + fmt_lines(d16["others"])) if d16["others"] else ""))
    put(390, "| ⚠ **%s is named inside rule/canon files other than its own** *(coordinates only)* | Phases 1, 4, 5, 6 | %s · plus the Phase 4–6 rows above. These are admissible canon; do not skip them. **The Robot Physiology file %s.** |" % (
        ctx.name, " · ".join(segs), ("names %s (see Phase 4 row)" % ctx.name) if h_rp else "does not name %s" % ctx.name))

    # ---- §F rows (398–404) --------------------------------------------------------------------------------------
    put(398, "| `%s/` (**%d** files) | ⛔ **WITHHELD corpus-wide** — address recorded so nobody re-derives it as a gap; do not open |" % (ctx.mega_dir, nmega))
    cul_state = lambda p: "" if ex(p) else " ⚠ **(file does not exist)**"
    put(399, "| `%s` and `%s` | ⏸️ **READ-LAST — open at Step 5, per §B.** Not inputs to Steps −1 through 4.%s%s |" % (
        ctx.culture, ctx.robot, cul_state(ctx.culture), cul_state(ctx.robot)))
    put(400, "| `%s` | ⏸️ **READ-LAST** — a prior personality read, conclusion-tier.%s |" % (ctx.enn, cul_state(ctx.enn)))
    put(401, "| `%s` | ⛔ **Not an input at any step** — the folder (`%s/`) is out of every step and phase, corpus-wide (developer ruling 2026-09-11; `DR-10`).%s |" % (
        ctx.vision, os.path.join(CITIES, "City_Vision_Notes"), cul_state(ctx.vision)))
    put(403, standard(T[402]).replace("(L740)", "(L%d)" % anch["neo"]).rstrip()[:-1].rstrip() + "%s |" % cul_state(ctx.neo))
    cold = os.path.join(R, "Archive", "ULM_Records", "Test_Runs", ctx.stem + "_ColdRun_Prep_2026-09-02.md")
    pre = os.path.join(ULM, "Pre-Contamination_Reviews", ctx.stem + "_Pre-Contamination_Review.md")
    tr_dir = os.path.join(ULM, "Test_Runs")
    nfiles = 0
    for root, _, fs in os.walk(tr_dir):
        for f in fs:
            if f.endswith((".md", ".txt")):
                try:
                    if ctx.rx.search(ctx.strip_subnet(open(os.path.join(root, f), encoding="utf-8", errors="replace").read())):
                        nfiles += 1
                except OSError:
                    pass
    own = [p for p in (cold, pre) if ex(p)]
    if own:
        own_t = "**%s has its own:** %s — artifacts of a cold-run preparation; a warm pass drops the pre-contamination review, and neither is an input." % (ctx.name, " and ".join("`%s`" % p for p in own))
    else:
        own_t = "**%s has no cold-run prep file and no pre-contamination review of its own** *(searched `%s` and `%s`)*." % (ctx.name, os.path.dirname(cold), os.path.dirname(pre))
    put(404, "| Test-run material | ⛔ **ZERO INTAKE for the whole pass** *(one exception: Step 9 reads the tail of the `%s` file for the next `M-` number — nothing else in the tree).* %s **%d further files** in the `%s/` tree name %s (counted by file, contents not read here) — that tree is zero-intake as a whole |" % (
        os.path.join(ULM, "Test_Runs", "OBSERVATIONS_and_Methodology_Findings.md"), own_t, nfiles, tr_dir, ctx.name))

    # ---- §J: add rename and developer items ----------------------------------------------------------------------
    extraJ = []
    if c["renamed"]:
        extraJ.append("| **Rename — %s** | ✅ Ruled 2026-10-03 | Files that still carry the old name are read through `%s/City_Renames_Alias_Table_2026-10-03.md`; the pass folder and megasheet/concept-art folders keep the old name by design (nothing was moved) |" % (c["renamed"], CITIES))
    reg = os.path.join(CITIES, "Founding_Register.md")
    rh = ctx.hits(reg) or []
    extraJ.append("| **Founding Register not in the Phase 2 table** — `%s` %s | ⏸️ Raised %s | ⛔ Does not block. Founders come only from the Register (`DR-19`), but the template's Phase 2 rows (resolved 2026-09-30, before the Register existed) do not list it. **Not added to any read list** — the developer decides whether Phase 2 should open it, and at which row |" % (
        reg, ("row L%s" % fmt_lines(rh).replace("L", "")) if rh else "(no row found for this city)", TODAY))
    ctx.claim(reg, rh)
    extraJ.append("| **Alias set and every \"Names %s at\" row are mechanical** (§A) | ⏸️ Raised %s | ⛔ Does not block. The developer or the first pass confirms the alias set before relying on the hit lists |" % (ctx.name, TODAY))
    if nds == 0:
        extraJ.append("| **Datasheets not yet built for this city** (November item N-5) | ⏸️ Raised %s | ⛔ The datasheet addresses in §C and §D are future outputs until N-5 runs |" % TODAY)

    # ---- assemble ------------------------------------------------------------------------------------------------
    outmap = {}
    for n, t in out:
        outmap[n] = t        # later put() calls for the same line override earlier ones
    body = []
    i = 1
    while i <= len(T):
        if i in outmap:
            body.append(outmap[i])
        elif i in skip:
            pass              # a line replaced by a multi-line block elsewhere
        else:
            body.append(standard(T[i - 1], i))
        i += 1
    text = "\n".join(body)

    # §J rows go right before the 'T1–T8 ARE MANDATORY' row
    anchor = "| ⛔⛔ **`T1`–`T8` ARE MANDATORY, EVERY CITY**"
    text = text.replace(anchor, "\n".join(extraJ) + "\n" + anchor, 1)

    # §I — replace the verification block with this run's own raw output
    i0 = text.index("## I · Verification block — raw output")
    i1 = text.index("**Per-step and per-phase completeness")
    ver = verify_block(ctx, text)
    text = text[:i0] + "## I · Verification block — raw output\n\n```\n" + ver + "\n```\n\n" + text[i1:]
    text = text.replace(
        "**Per-step and per-phase completeness (checked by script):**",
        "**Per-step and per-phase completeness (carried from Casey's sheet, where it was checked by script 2026-09-30; this generator re-checks the governing ranges and every path, above):**")
    # the ⚙ provenance block, after the banner
    prov = (
        "> ## ⚙ HOW THIS SHEET WAS BUILT — read before trusting a line number\n"
        "> **Generated %s by `Tools/build_pretrip.py`.** The standard rows (steps, phases, laws, carve-outs, handoff sweep, `T8` procedure) are "
        "**carried from Casey's sheet** (resolved from the runbook on 2026-09-30), **except that every runbook and spine line number was re-located in the files "
        "as they stand today**: governing ranges recomputed from the live headings, the law and table lines found by their own text, the other method-document "
        "lines moved by text match — all re-checked in §I. Every **city-specific** row — aliases, census, extent, `16` and every \"Names %s at L…\" list — was "
        "**computed fresh from the live files** for this city; no line number was copied from another city's sheet. **What the script cannot do:** decide whether a hit is "
        "about this place (§A is a mechanical draft), re-audit the standard rows against the runbook's per-phase table (hand-audited once, on Casey's "
        "sheet, 2026-09-30), or read any withheld file.\n" % (TODAY, ctx.name))
    marker = "---\n\n## A · Identity & alias set"
    text = text.replace(marker, prov + "\n" + marker, 1)
    # leftovers check
    return ctx, text


def verify_block(ctx, text):
    L = []
    L.append("$ build_pretrip.py %s  (%s) — template: Casey's sheet, %d lines" % (ctx.key, TODAY, len(read_lines(TEMPLATE))))
    # existence test over every backticked absolute address
    spans = re.findall(r"`(/home/[^`]+)`", text)
    seen, res, fut, dpend, missing, late = set(), 0, 0, 0, [], []
    pass_prefix = ctx.pass_dir.rstrip("/") + "/"
    for sp in spans:
        if sp in seen:
            continue
        seen.add(sp)
        p = sp.rstrip("/")
        if sp.startswith(pass_prefix) or sp == ctx.rlog:
            if "/Datasheets/" in sp and not ex(sp) and not ex(os.path.join(ctx.pass_dir, "Datasheets")):
                dpend += 1
            elif ex(p):
                res += 1
            else:
                fut += 1
        elif ex(p):
            res += 1
        elif any(m_ in sp for m_ in ("/Local_Cultures/", "/Local_Robot_Culture/", "/City_Enneagram_Personalities/", "/City_Vision_Notes/", "/Neo-Races-and-Cultures/", "/City_Megasheets/")):
            late.append(sp)
        else:
            missing.append(sp)
    L.append("existence test over every absolute address in this file (%s)" % TODAY)
    L.append("TOTAL=%d  RESOLVE=%d  FUTURE-OUTPUT(by design)=%d  DATASHEET-NOT-YET-BUILT(N-5)=%d  MISSING-INPUT=%d  MISSING-READ-LAST-OR-EXCLUDED=%d" % (len(seen), res, fut, dpend, len(missing), len(late)))
    for m in missing:
        L.append("  MISSING (an input a step opens): %s" % m)
    for m in late:
        L.append("  MISSING (read-last at Step 5, or an excluded file): %s" % m)
    # line claims re-read
    ok = bad = 0
    badl = []
    for path, nums in ctx.claims:
        if not ex(path):
            continue
        ls = read_lines(path)
        for n in nums:
            if n < 1 or n > len(ls):
                bad += 1
                badl.append("%s L%d (beyond end)" % (os.path.basename(path), n))
                continue
            line = ls[n - 1]
            if any(nm in line for nm in ctx.names) or (ctx.c["pat"] and ctx.rx.search(line)) or (os.path.basename(path) in ("Founding_Register.md",)):
                ok += 1
            elif os.path.basename(path).endswith("Official_Population_Census.md") and line.startswith("|"):
                ok += 1        # census entry rows (the entry's table rows do not repeat the name)
            elif os.path.basename(path) == ctx.stem + ".md":
                ok += 1        # the city's own spec: heading/placeholder lines
            else:
                bad += 1
                badl.append("%s L%d" % (os.path.basename(path), n))
    L.append("")
    L.append("$ line-number claims re-read from the live files (each cited line opened and tested for a name of this city)")
    L.append("%d claims · %d OK · %d FAIL%s" % (ok + bad, ok, bad, ("  — " + "; ".join(badl[:20])) if badl else ""))
    L.append("  (census Section A entry lines are table rows that do not repeat the city name; they are counted OK as table rows)")
    # governing ranges vs live headings (strict: start = heading, end = the line before the next heading)
    steps, phases = live_ranges()
    cards = re.findall(r"### Step (−1|\d+) — [^\n]*\n(?:[^\n]*\n){0,4}?- \*\*Governing rule:\*\* `[^`]*00_RUNBOOK.md` lines (\d+)–(\d+)", text)
    live = {nm.replace("−", "-"): (s_, e_) for nm, s_, e_ in steps}
    good = 0
    detail = []
    for st, a, b in cards:
        if live.get(st.replace("−", "-")) == (int(a), int(b)):
            good += 1
        else:
            detail.append("Step %s: cited %s–%s, live %s" % (st, a, b, live.get(st.replace("−", "-"))))
    L.append("")
    L.append("$ governing ranges vs live headings (strict: start = the heading line, end = the line before the next heading)")
    L.append("runbook steps: %d of %d cited ranges equal the live range%s" % (good, len(cards), ("  — OFF: " + "; ".join(detail)) if detail else ""))
    lp = {n_: (s_, e_) for n_, s_, e_ in phases}
    pr = re.findall(r"\*\*Phase (\d+) — governing:\*\* `[^`]*03_The_Phase_Spine.md` lines (\d+)–(\d+)", text)
    g2, d2 = 0, []
    for pn, a, b in pr:
        if lp.get(int(pn)) == (int(a), int(b)):
            g2 += 1
        else:
            d2.append("Phase %s: cited %s–%s, live %s" % (pn, a, b, lp.get(int(pn))))
    L.append("spine phases: %d of %d cited ranges equal the live range%s" % (g2, len(pr), ("  — OFF: " + "; ".join(d2)) if d2 else ""))
    # §G law rows: each cited line must contain the law's own anchor text
    anchors = [("LAW 0 — Depth over speed", "00_RUNBOOK.md", r"# LAW 0 —"), ("LAW 0-R", "00_RUNBOOK.md", r"LAW 0-R|GOVERNING\. Added"),
               ("No Forced Fit", "00_RUNBOOK.md", r"NO FORCED FIT"), ("Law of One Location", "00_RUNBOOK.md", r"LAW OF ONE LOCATION"),
               ("The Layering Law", "00_RUNBOOK.md", r"LAYERING LAW"), ("Divergence operator", "00_RUNBOOK.md", r"[Rr]efusing all ethnic"),
               ("`T1`–`T8` mandatory", "00_RUNBOOK.md", r"BINDING — \*\*`T1`")]
    law_ok = law_bad = 0
    law_detail = []
    rbl = read_lines(os.path.join(ULM, "00_RUNBOOK.md"))
    for label, fn, rx in anchors:
        row = next((l for l in text.split("\n") if l.startswith("| **%s" % label) or l.startswith("| %s" % label)), None)
        m = re.search(r"%s` L(\d+)" % re.escape(fn), row or "")
        if not m:
            law_bad += 1
            law_detail.append("%s: no cited line found" % label)
            continue
        n = int(m.group(1))
        if re.search(rx, rbl[n - 1]):
            law_ok += 1
        else:
            law_bad += 1
            law_detail.append("%s: L%d is %r" % (label, n, rbl[n - 1][:50]))
    L.append("§G law rows: %d of %d cited runbook lines contain the law's own text%s" % (law_ok, law_ok + law_bad, ("  — OFF: " + "; ".join(law_detail)) if law_detail else ""))
    moved = [r for r in REMAP_LOG if "NOT RE-LOCATABLE" not in r[3]]
    lost = [r for r in REMAP_LOG if "NOT RE-LOCATABLE" in r[3]]
    L.append("standard citations re-located from the 2026-09-30 state (base %s): %d numbers moved%s" % (
        base_ref()[:8], len(moved), ("; NOT RE-LOCATABLE: " + "; ".join("%s %s (template line %d)" % (r[1], r[2], r[0]) for r in lost)) if lost else "; none lost"))
    # any runbook/spine number that was neither an anchored fix nor a recomputed governing range
    unver = []
    for i, ln in enumerate(text.split("\n"), 1):
        for m in _GRP.finditer(ln):
            toks = _TOK.findall(ln[:m.start()])
            if toks and os.path.basename(toks[-1]) in ("00_RUNBOOK.md", "03_The_Phase_Spine.md"):
                for part in re.findall(r"\d+(?:[–-]\d+)?", m.group(1)):
                    part = part.replace("-", "–")
                    if part not in ctx.known:
                        unver.append("L%d: %s" % (i, part))
    L.append("runbook/spine citations that are neither an anchored fix nor a recomputed governing range: %s" % (", ".join(unver) if unver else "none"))
    # counts and placeholder/residue check
    L.append("")
    L.append("$ template-placeholder and carried-name check")
    body_chk = "\n".join(l for l in text.split("\n") if "Template-placeholder check" not in l and "survive in this" not in l)
    ph_tok = [t for t in ("<City>", "<Subnet>", "<STATION>", "<N>", "{{City}}") if t in body_chk]
    resid = []
    for w in ("Casey", "Mirny_Subnet", "Mirny subnet", "Wilkes", "Budd Coast", "Vincennes"):
        if ctx.name == "Casey":
            continue
        for i, ln in enumerate(text.split("\n"), 1):
            if w in ln and "Casey's sheet" not in ln and "carried unchanged from Casey" not in ln and "Casey's" not in ln and not (w in ("Mirny_Subnet", "Mirny subnet") and ctx.sub == "Mirny_Subnet"):
                resid.append("%s@L%d" % (w, i))
    L.append("placeholder tokens: %s" % (", ".join(ph_tok) or "none"))
    L.append("carried-over names (Casey / Mirny paths / Wilkes / Budd / Vincennes): %s" % (", ".join(resid[:30]) or "none"))
    return "\n".join(L)


def ledger_text(ctx):
    t = open(TEMPLATE_LEDGER, encoding="utf-8").read()
    t = t.replace("Casey", ctx.name)
    return t


def main():
    argv = sys.argv[1:]
    if "--list" in argv or (not [a for a in argv if not a.startswith("--")] and "--all" not in argv):
        for k, v in CITY.items():
            if v["existing"]:
                continue
            print("%-22s %-16s %s%s" % (k, v["sub"], v["name"], ("   (was: %s)" % ", ".join(v["former"])) if v["former"] else ""))
        print("\nNot built by this generator:")
        for k, v in SKIP_NOTE.items():
            print("  %-14s %s" % (k, v))
        return 0
    if "--all" in argv:
        rc = 0
        for k in CITY:
            if CITY[k]["existing"]:
                continue
            ctx_, text_ = build(k)
            d_ = ctx_.pass_dir if "--write" in argv else os.path.join(argv[argv.index("--out") + 1], k)
            os.makedirs(d_, exist_ok=True)
            for fn_, content_ in (("00.0_Pre-Trip_Inspection.md", text_), ("00.2_Position_Coverage_Ledger.md", ledger_text(ctx_))):
                p_ = os.path.join(d_, fn_)
                if ex(p_) and "--force" not in argv:
                    print("REFUSED (exists): %s" % p_)
                    rc = 1
                    continue
                open(p_, "w", encoding="utf-8").write(content_ + ("" if content_.endswith("\n") else "\n"))
                print("wrote %s" % p_.replace(REPO + "/", ""))
        return rc
    key = [a for a in argv if not a.startswith("--") and a not in ("--out",)][0]
    if "--out" in argv:
        key = [a for a in argv if not a.startswith("--") and a != argv[argv.index("--out") + 1]][0]
    if key not in CITY:
        sys.exit("unknown city key %r (see --list)" % key)
    if CITY[key]["existing"] and "--write" in argv:
        sys.exit("%s already has a hand-built sheet; use --out DIR to generate a comparison copy" % key)
    ctx, text = build(key)
    ledger = ledger_text(ctx)
    if "--write" in argv:
        d = ctx.pass_dir
        os.makedirs(d, exist_ok=True)
    elif "--out" in argv:
        d = os.path.join(argv[argv.index("--out") + 1], key)
        os.makedirs(d, exist_ok=True)
    else:
        d = None
    if d:
        for fn, content in (("00.0_Pre-Trip_Inspection.md", text), ("00.2_Position_Coverage_Ledger.md", ledger)):
            p = os.path.join(d, fn)
            if ex(p) and "--force" not in argv and "--write" in argv:
                print("REFUSED (exists, use --force): %s" % p)
                continue
            open(p, "w", encoding="utf-8").write(content + ("" if content.endswith("\n") else "\n"))
            print("wrote %s (%d bytes)" % (p, len(content.encode("utf-8"))))
    i0 = text.index("## I · Verification block")
    print(text[i0:i0 + 4000].split("**Per-step")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
