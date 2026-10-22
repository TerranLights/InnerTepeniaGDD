#!/usr/bin/env python3
"""
BUILD DATASHEETS  —  generates a city's 19-file Tier C datasheet set (`<pass folder>/Datasheets/`)
(November To-Do N-5, 2026-10-21; method: `Mechanical_Extraction_Field_Guide.md`).

  usage:  python3 build_datasheets.py <city_key> [--out DIR] [--write] [--force]
          python3 build_datasheets.py --all --write      (every city in `build_pretrip.CITY` that has no datasheets yet)

WHAT IT DOES: a datasheet row is a VALUE + its CITATION, copied from a source, never a finding. This tool copies:
  * structured values (spec header fields, the spec's census lines and composition table, the climate fields, the READER
    monthly means, the city's own row in `16`, `09` and `11`, the Founding Register row), and
  * every line that NAMES the city in a shared file (Highways, Airports, Ports, the relationship database entry, the
    medical-institutes file, holidays, religions, ...), each line as written and cited by line number.
It refuses, mechanically and visibly, three things the Field Guide forbids:
  * a source line carrying Long-Night-War / post-war content is NOT copied (the row says only that it is excluded);
  * a source line that compares the city with other places ("one of only 10", "rank 3 of 38", "unlike ...") is NOT copied;
  * a multi-city LIST line (three or more other cities named) is NOT copied, only its line number is recorded;
  * prose sections of the spec (geography, founding, character, economy, notable people) are NOT quoted: they are cited by
    line range, because which spans are admissible is Step -1's own ruling (Field Guide, Step -1 entry).
Tier U steps (6, 7, 8, 9) carry the corpus-wide text. Nothing is interpreted. Every file is marked DRAFT.

WHAT IT DOES NOT DO: judge relevance, read withheld material (megasheets, vision notes, culture sheets are only tested for
existence or counted), or compare the city with any other. The set is a DRAFT until a three-reader check says otherwise.
"""
import glob
import os
import re
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pretrip as B   # noqa: E402  (city table, helpers, paths)

TODAY = datetime.date.today().isoformat()
R, C, U = B.REPO, B.CITIES, B.ULM
UNIV = "/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline"
DI = os.path.join(C, "Division_of_Industry")
WAR = re.compile(r"\b(war|wartime|post-war|postwar|destroyed|destruction|ruin|ruins|ruined|damaged|refugees?|casualt\w+|abandon\w*|surviv\w+|apocalyptic|Long Night)\b", re.I)
COMPARE = re.compile(r"(\b(?:one of|only)\s+(?:the\s+)?(?:\w+\s+)?(?:\d+|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b|\bof\s+(?:all\s+)?(?:37|38)\b|\brank(?:ed)?\b|\bunlike\b|"
                     r"\bany other (?:city|cities)\b|\bevery other\b|\bthan any\b|\b(?:most|least|largest|smallest|highest|lowest|coldest|warmest|windiest) of\b|\bcompared (?:to|with)\b|\bin the (?:country|corpus)\b|\bin (?:all of )?Tepenia\b|\b(?:version|type|variant|analog\w*|counterpart|equivalent)\s+of\s+[A-Z][\w']+'s\b|\b(?:most|least|only|first|last)\s+(?:\w+\s+){0,2}(?:city|cities|place|site)\b|"
                     r"\b(?:lower|higher|colder|warmer|larger|smaller|more|less|farther|closer)\b[^.|]{0,30}\bthan\b)", re.I)
INFERENCE = re.compile(r"⇒|\btherefore\b|\bwhich means\b|\bthe real\b|\bthis is the\b", re.I)
EXC_WAR = "*[source line excluded: later-era content, outside the Second Interwar default scope; not copied]*"
EXC_CMP = "*[source line compares the city with other places; not copied, line number recorded only]*"
EXC_MULTI = "*[source line is a multi-city list; not copied, line number recorded only]*"


def esc(s):
    return s.replace("|", "\\|")


class Sheet:
    def __init__(self, ctx):
        self.ctx = ctx
        self.name = ctx.name
        self.others = None
        self.log = []          # excluded lines, for the build report

    def other_names(self):
        if self.others is None:
            s = set()
            for k, v in B.CITY.items():
                if k == self.ctx.key:
                    continue
                s.add(v["name"])
                s.update(v["former"])
            for extra in ("Concordia", "Shirayuki", "Sinheung", "Zhongshan", "Relung Panen", "Amundsen Station", "Palmer", "Mirny", "Halley", "Janbogo", "Mawson", "Ushuaia", "Hobart"):
                s.add(extra)
            s -= set(self.ctx.names)
            self.others = sorted(s, key=len, reverse=True)
        return self.others

    def n_other(self, text):
        n = 0
        for o in self.other_names():
            if re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % re.escape(o), text):
                n += 1
        return n

    def safe(self, text, src, n, allow_multi=False, allow_compare=False):
        """Return the text to copy, or an exclusion marker. Records what was excluded."""
        if WAR.search(text):
            self.log.append((src, n, "war"))
            return EXC_WAR
        if not allow_compare and COMPARE.search(text):
            self.log.append((src, n, "compare"))
            return EXC_CMP
        if not allow_multi and self.n_other(text) >= 3:
            self.log.append((src, n, "multi"))
            return EXC_MULTI
        return text.strip()


def cite(path, lines=None):
    base = os.path.basename(path)
    if "/Specs/" in path:
        base = "Specs/" + base
    elif "/Climate Data/READER/" in path:
        base = "READER/" + base
    elif "/Robot_Religions/" in path:
        base = "Robot_Religions/" + os.path.relpath(path, os.path.join(R, "Worldspace", "Factions", "Robot_Religions"))
    elif "/Ice-Cold_Buddhism_Research/" in path:
        base = "Ice-Cold_Buddhism_Research/" + os.path.basename(path)
    elif path.startswith(UNIV):
        base = "…/" + os.path.relpath(path, UNIV)
    if not lines:
        return "`%s`" % base
    return "`%s` %s" % (base, B.fmt_lines(lines))


def table(rows, head=("Category", "Value", "Citation")):
    out = ["| %s |" % " | ".join(head), "|%s|" % "|".join("---" for _ in head)]
    for r in rows:
        out.append("| %s |" % " | ".join(esc(str(x)) if i else str(x).replace("\n", " ") for i, x in enumerate(r)))
    return "\n".join(out)


def header(ctx, title, box):
    return "# %s — Datasheet · %s\n\n%s%s\n" % (ctx.name, title, box, ambig_note(ctx))


DRAFT_C = ("> ⚠ **DRAFT — Tier C, built %s by `Tools/build_datasheets.py`: a value + its citation, copied from the source, never a finding.** "
           "Not yet through its own three-reader check. A source line carrying later-era content, a comparison with other places, or a multi-city list is "
           "marked as excluded and not copied. Nothing here is a ruling about %s; which spans of any source are admissible is each step's own work.\n")


def ambig_note(ctx):
    a = ctx.c.get("ambig")
    return ("> ⚠ **Ambiguous name:** %s. Every row below that comes from a name search may be about something else with the same name (a person, a feature, the subnet); read the line.\n" % a) if a else ""


def sheet_note(ctx):
    return DRAFT_C % (TODAY, ctx.name)


def NOT_MECH(text, ctx):
    return "\n\n**Not mechanical / not included here:** %s — none of this exists until %s's own pass runs.\n" % (text, ctx.name)


# ---------------------------------------------------------------------------------------------------------------------
class Data:
    """Everything read once per city."""

    def __init__(self, ctx):
        self.ctx = ctx
        self.sh = Sheet(ctx)
        self.spec_lines = B.read_lines(ctx.spec) if B.ex(ctx.spec) else []
        self.cen = B.census_data(ctx)
        self.cen_lines = B.read_lines(self.cen["path"])
        self.ext = B.extent_data(ctx)
        self.d16 = B.di16_data(ctx)
        self.reader = B.read_lines(ctx.reader) if B.ex(ctx.reader) else None

    # ---- the spec ---------------------------------------------------------------------------------------------------
    def spec_field(self, label, upto=80):
        for i, ln in enumerate(self.spec_lines[:upto], 1):
            m = re.match(r"^\*\*%s:?\*\*:?\s*(.*)$" % re.escape(label), ln)
            if m:
                return i, m.group(1).strip()
        return None, None

    def spec_section(self, heading_rx):
        ls = self.spec_lines
        for i, ln in enumerate(ls, 1):
            if re.match(heading_rx, ln):
                lvl = len(re.match(r"^(#+)", ln).group(1))
                j = i + 1
                while j <= len(ls) and not re.match(r"^#{1,%d} " % lvl, ls[j - 1]):
                    j += 1
                return i, j - 1
        return None

    def spec_headings(self):
        return [(i, ln) for i, ln in enumerate(self.spec_lines, 1) if ln.startswith("## ")]


def clean_cell(c):
    return re.sub(r"[*`{}]|\u26a0\ufe0f?|\u26d4\ufe0f?", "", c).strip()


def table_row(path, ctx):
    """The city's own row in a markdown table: (header cells, row cells, header line, row line) or None."""
    ls = B.read_lines(path)
    hdr = None
    for i, l in enumerate(ls, 1):
        if l.startswith("|") and i < len(ls) and re.match(r"^\|\s*:?-", ls[i]):
            hdr = (i, [clean_cell(c) for c in l.split("|")[1:-1]])
            continue
        if hdr and l.startswith("|") and i > hdr[0] + 1:
            cells = [clean_cell(c) for c in l.split("|")[1:-1]]
            if any(c in ctx.names for c in cells[:3]):
                return hdr[1], cells, hdr[0], i
        if hdr and not l.startswith("|") and l.strip() and i > hdr[0] + 2:
            hdr = None
    return None


def row_text(hc, cells, drop=("#", "rank")):
    return " · ".join("%s: %s" % (a, b) for a, b in zip(hc, cells) if a.lower() not in drop and b)


def hits_rows(d, path, label, allow_multi=False, allow_compare=False, cap=40, include_text=True):
    """One row per source line naming the city (copied when safe)."""
    ctx = d.ctx
    h = ctx.hits(path)
    if h is None:
        return [(label, "⬜ source file not found", cite(path))]
    if not h:
        return [(label, "Checked by name (%s): **zero hits** in a %d-line file" % (", ".join("`%s`" % n for n in ctx.names), len(B.read_lines(path))), cite(path))]
    ls = B.read_lines(path)
    rows = []
    for n in h[:cap]:
        txt = d.sh.safe(ls[n - 1], os.path.basename(path), n, allow_multi, allow_compare) if include_text else "*[line number recorded only]*"
        rows.append((label if n == h[0] else "↳ " + label, txt, cite(path, [n])))
    if len(h) > cap:
        rows.append(("↳ " + label, "%d further lines name the city: %s *(line numbers only)*" % (len(h) - cap, B.fmt_lines(h[cap:])), cite(path)))
    return rows


# ---------------------------------------------------------------------------------------------------------------------
def tier_rows(lines, a=1, b=None):
    """The first `| Tier | Nations |` table in the range: its Primary / Significant / Notable rows."""
    b = b or len(lines)
    for i in range(a, b + 1):
        if re.match(r"^\|\s*Tier\s*\|\s*Nations", lines[i - 1]):
            out = []
            j = i + 2
            while j <= b and lines[j - 1].startswith("|"):
                if re.match(r"^\| (Primary|Significant|Notable) \|", lines[j - 1]):
                    out.append((j, lines[j - 1]))
                j += 1
            return out
    return []


def f_step_m1(d):
    ctx = d.ctx
    ls = d.spec_lines
    rows = [("Specs file location", "`Cities/Specs/%s/%s.md` — %s" % (ctx.specsub, ctx.stem, "confirmed on disk" if ls else "⬜ NOT FOUND"), "Checked %s" % TODAY),
            ("Specs file length", "%d lines total (bound for any future read-spec computation)" % len(ls), "Counted %s" % TODAY),
            ("Identity / designation", d.sh.safe(ls[0].lstrip("# ").strip(), ctx.stem, 1), cite(ctx.spec, [1]))]
    notice = [(i, l) for i, l in enumerate(ls[:30], 1) if "RENAMED" in l or "NAME RULED" in l]
    for i, l in notice:
        rows.append(("Rename notice at the top of the spec", "Present — the notice text is in the spec (not copied: it names the earlier name and its reasons; read it there)", cite(ctx.spec, [i])))
    for label in ("Based on", "Arcanet Subnet", "Access type", "Highway access", "Maritime access", "Significance"):
        n, v = d.spec_field(label)
        if v is not None:
            rows.append((label if label != "Based on" else "Real-world basis", d.sh.safe(v, ctx.stem, n, allow_multi=True, allow_compare=(label == "Based on")), cite(ctx.spec, [n])))
    n, v = d.spec_field("Based on")
    if v:
        m = re.search(r"\(([^()]*\d+°[^()]*)\)\s*[^()]*$|\((~?\d+°[^)]*)\)", v)
        if m:
            rows.append(("Coordinates (as written in the same field)", (m.group(1) or m.group(2)).strip(), cite(ctx.spec, [n])))
    n, v = d.spec_field("Status")
    if n:
        rows.append(("Specs `Status:` field", "States a later-era condition; per the standing default-scope rule (`00_RUNBOOK.md`, the Second Interwar default) this is **never an input** to a Second Interwar pass — not copied", cite(ctx.spec, [n])))
    later = [i for i, l in d.spec_headings() if re.search(r"Current Status|Destruction|Legacy|Connection to Concordia", l)]
    if later:
        rows.append(("Later-era sections present in the Specs file (same exclusion as `Status:`)", "%d section(s), by heading position: %s — not copied, not described" % (len(later), B.fmt_lines(later)), cite(ctx.spec, later)))
    for lab in ("Census I", "Census II"):
        for i, l in enumerate(ls[:80], 1):
            if l.startswith("**%s" % lab):
                rows.append((lab + " (spec's own line)", d.sh.safe(re.sub(r"^\*\*Census I+ \([^)]*\):\*\*\s*", "", l), ctx.stem, i, allow_compare=True), cite(ctx.spec, [i])))
                break
    return header(ctx, "Step −1 (Input Contract)",
                  "> ⚠⚠ **DRAFT — Tier C. READ THIS BOX BEFORE USING THE FILE.** %s's own pass has **not** started: no Step −1 has run and no admissibility ruling exists. "
                  "⛔ **This file CANNOT pre-stage an admitted read-range** — deciding which lines of the Specs file are admissible is Step −1's own derivation work "
                  "(Field Guide, Step −1 entry). **It gives bibliographic facts and the spec's own structured fields only.**\n" % ctx.name) + "\n" + table(rows) + NOT_MECH(
        "the admitted read-range, the four-category classification (PROVIDED/RESERVED/PRODUCED/REQUESTED), any generator presence/absence call, the type-modifier declaration", ctx)


def retention(d):
    ctx = d.ctx
    cen = d.cen
    out = {}
    def nums(row):
        cells = [c.strip().strip("*") for c in d.cen_lines[row - 1].split("|")[1:-1]]
        return cells
    r1 = cen["rows1"][0] if cen["rows1"] else None
    r2 = cen["rows2"][0] if cen["rows2"] else None
    out["r1"], out["r2"] = r1, r2
    def pull(row):
        if not row:
            return None
        cells = nums(row)
        vals = [int(re.sub(r"[^\d]", "", c)) for c in cells[3:6] if re.sub(r"[^\d]", "", c)]
        return vals if len(vals) == 3 else None
    out["v1"], out["v2"] = pull(r1), pull(r2)
    return out


def f_step_0(d):
    ctx, cen = d.ctx, d.cen
    t = retention(d)
    rows = []
    def cen_row(row, lab, tag):
        if not row:
            return (lab, "⛔ **No %s row exists in the census** — an empty slot is a result (`No Forced Fit`)" % tag, cite(cen["path"]))
        cells = [c.strip() for c in d.cen_lines[row - 1].split("|")[1:-1]]
        status = cells[6] if len(cells) > 6 else ""
        val = "%s H / %s R / %s combined" % (cells[3], cells[4], cells[5])
        if status and WAR.search(status):
            val += " *(status cell present; later-era content, not copied)*"
            d.sh.log.append(("Census", row, "war"))
        elif status and len(status) <= 90 and not COMPARE.search(status):
            val += " (status cell: %s)" % status.strip("*() ")
        elif status:
            val += " *(a long status cell is present: an authoring note, not copied)*"
        return (lab, val, cite(cen["path"], [row]))
    rows.append(cen_row(t["r1"], "Census I", "Census I"))
    rows.append(cen_row(t["r2"], "Census II", "Census II"))
    if t["v1"] and t["v2"]:
        (h1, r1, c1), (h2, r2, c2) = t["v1"], t["v2"]
        rows.append(("Retention (computed; formula = Census II count ÷ Census I count)",
                     "combined %.2f%% · human %.2f%% · robot %.2f%%" % (100.0 * c2 / c1, 100.0 * h2 / h1, 100.0 * r2 / r1),
                     "Computed from the two rows above: %s÷%s · %s÷%s · %s÷%s" % ("{:,}".format(c2), "{:,}".format(c1), "{:,}".format(h2), "{:,}".format(h1), "{:,}".format(r2), "{:,}".format(r1))))
    sp = "`Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md`"
    rows += [("**Temporal frame — the Second Interwar Period**", "**2564–2812. 248 years, beginning at the Falkland Treaty.** The default frame for worldbuilding a Tepenian location; a corpus-wide constant, not a per-city judgment", "⭐ " + sp + ", in full"),
             ("Act structure within the frame", "Act 1: 2564 → somewhere in the 2600s (a hazy range, not yet dated) — national-ethnic-origin cultures still fresh. Act 2: by the late 2600s / early 2700s, onward — properly Tepenian; origin is ancestry, not identity", sp),
             ("The consolidating mechanism", "Interconnection, decisively solidified by Amundsen Tower's completion (~2688) — not a switch, not the creation of unity, not the Tower's only effect", sp + " §\"The consolidating mechanism\""),
             ("**U** `Repo_Scope.md`", "Tier U — corpus-wide boundary statement, fixed", "—")]
    n, v = d.spec_field("Based on")
    if v:
        rows.append(("Real-world basis", d.sh.safe(v, ctx.stem, n, True, True), cite(ctx.spec, [n])))
    return header(ctx, "Step 0 & Phase 0 (Frame) — MERGED",
                  "> ⚠ **DRAFT — Tier C + Tier U.** Merged per the Field Guide's consolidation of Step 0 / Phase 0 (identical underlying facts). **Feeds `00_Frame.md` when %s's own Step 0 runs.** It carries only what a source already states directly.\n" % ctx.name
                  ) + "\n" + table(rows) + NOT_MECH("the Type + modifiers declaration, Band assignment, extent band, Status declaration, Configuration, generator selection, the asymmetry check on inherited material", ctx)


def register_cells(lr, i, cells):
    """Label each cell of a Founding Register row with its column header (nearest header row above)."""
    hdr = None
    for j in range(i - 1, 0, -1):
        if lr[j - 1].startswith("| City |") and "---" not in lr[j - 1]:       # the real header row (not a data row ending in "City |")
            hdr = [c.strip().strip("*") for c in lr[j - 1].split("|")[1:-1]]
            break
    if hdr and len(hdr) == len(cells):
        return " · ".join("**%s:** %s" % (a, b) for a, b in zip(hdr, cells) if b)
    return " | ".join(cells)


def climate_md_rows(ctx, rl):
    """Rows for a city with no READER station and its own `Climate.md` (the measured anchors, then the constructed monthly means)."""
    rows = [("Climate source", "No BAS READER station exists at this coordinate; the city's own `Climate.md` is the climate file (its §4 records the sources tried)", cite(ctx.reader, [1]))]
    q = next((i for i, x in enumerate(rl, 1) if x.startswith("| Quantity |")), None)
    if q:
        for j in range(q + 2, len(rl) + 1):
            x = rl[j - 1]
            if not x.startswith("|"):
                break
            c = [y.strip() for y in x.strip().strip("|").split("|")]
            if len(c) >= 3:
                rows.append(("Climate.md — measured anchor: " + re.sub(r"[*\u2b50\U0001f52c]", "", c[0]).strip(), "%s *(%s)*" % (re.sub(r"\*", "", c[1]).strip(), re.sub(r"\*", "", c[2]).strip()), cite(ctx.reader, [j])))
    h = next((i for i, x in enumerate(rl, 1) if re.match(r"\|\s*Month\s*\|", x)), None)
    if h:
        cols = [y.strip() for y in rl[h - 1].strip().strip("|").split("|")]
        k = cols.index("Mean")
        vals, last = [], h
        for j in range(h + 2, len(rl) + 1):
            x = rl[j - 1]
            if not re.match(r"\|\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*\|", x):
                break
            c = [y.strip() for y in x.strip().strip("|").split("|")]
            vals.append("%s %s" % (c[0], re.sub(r"\*", "", c[k]).replace("-", "\u2212")))
            last = j
        rows.append(("Climate.md — monthly mean temperature (\u00b0C), **CONSTRUCTED, not measured**", " \u00b7 ".join(vals) + " *(built from the measured annual anchors; the file records an independent check against measured freezing degree-days)*", cite(ctx.reader, [h, last])))
    return rows


def reader_rows(d):
    ctx = d.ctx
    rows = []
    rl = d.reader
    if rl is None:
        return [("Climate READER file", "⬜ no file at the address (`%s`)" % ctx.reader, "—")]
    if os.path.basename(ctx.reader) == "Climate.md":        # a city whose climate file is its own constructed block (no READER station exists)
        return climate_md_rows(ctx, rl)
    has_table = any(re.match(r"\|\s*Jan\s*\|", x) for x in rl)
    if not has_table:
        body = " ".join(x.strip() for x in rl if x.strip() and not x.startswith("#"))
        rows.append(("Climate READER file (`%s.md`)" % os.path.basename(ctx.reader)[:-3], "**%s %d-line status stub, not a dataset — no monthly table.** What the file itself says: %s" % ("An" if len(rl) in (8, 11, 18) else "A", len(rl), body[:600]), cite(ctx.reader, list(range(1, len(rl) + 1)))))
        return rows
    for i, l in enumerate(rl, 1):
        m = re.match(r"\*\*(Climate authority|Station notes|Data period|Full data range|Annual mean temperature):\*\*\s*(.*)", l)
        if m:
            rows.append(("READER — " + m.group(1).lower(), m.group(2).strip(), cite(ctx.reader, [i])))
    hdr = next((i for i, x in enumerate(rl, 1) if re.match(r"\|\s*Jan\s*\|", x)), None)
    if hdr:
        cols = [c.strip() for c in rl[hdr - 1].split("|")[1:-1]]
        for j in range(hdr + 1, min(hdr + 4, len(rl) + 1)):
            if re.match(r"\|\s*(-|:)", rl[j - 1]):
                continue
            vals = [c.strip() for c in rl[j - 1].split("|")[1:-1]]
            if len(vals) == len(cols):
                rows.append(("READER — monthly table, row %s" % ("1" if j == hdr + 2 else str(j - hdr - 1)), " · ".join("%s %s" % (a, b) for a, b in zip(cols, vals)), cite(ctx.reader, [hdr, j])))
    return rows


def f_step_1_2(d):
    ctx = d.ctx
    rows = []
    n, v = d.spec_field("Access type")
    if v is not None:
        rows.append(("`Access type:`", d.sh.safe(v, ctx.stem, n, True, False), cite(ctx.spec, [n])))
    sec = d.spec_section(r"^### Annual Climate")
    if sec:
        for i in range(sec[0] + 1, sec[1] + 1):
            l = d.spec_lines[i - 1]
            m = re.match(r"^\*\*([^*]+?):\*\*\s*(.+)$", l)
            if m:
                rows.append(("Spec climate — " + m.group(1).strip().lower(), d.sh.safe(m.group(2), ctx.stem, i, True, False), cite(ctx.spec, [i])))
    else:
        rows.append(("Spec climate section", "No `### Annual Climate` heading found in the spec", cite(ctx.spec)))
    rows += reader_rows(d)
    d16 = d.d16
    if d16["row"]:
        ls16 = B.read_lines(d16["path"])
        hdr = [clean_cell(c) for c in ls16[246].split("|")[1:-1]]
        cells = [clean_cell(c) for c in ls16[d16["row"] - 1].split("|")[1:-1]]
        rows.append(("`16_Per_City_Three_Tier_Run.md` Half B — the city's own row", row_text(hdr, cells), cite(d16["path"], [247, d16["row"]]) + " (header L247, row L%d)" % d16["row"]))
    else:
        rows.append(("`16` Half B — the city's own row", "⛔ no row found for the city in the table (L249–340)", cite(d16["path"])))
    eg = os.path.join(R, "Worldspace", "Energy_Grid_Failure_Rationale.md")
    rows += hits_rows(d, eg, "`Energy_Grid_Failure_Rationale.md`")
    reg = os.path.join(C, "Founding_Register.md")
    lr = B.read_lines(reg)
    for i, l in enumerate(lr, 1):
        if l.startswith("|"):
            cells = [c.strip().strip("*") for c in l.split("|")[1:-1]]
            if cells and cells[0] in ctx.names:
                rows.append(("Founding Register — the city's row (founders are decided only here, `DR-19`)", register_cells(lr, i, cells), cite(reg, [i])))
    n, v = d.spec_field("Settled", upto=400)
    if v:
        rows.append(("Spec — `Settled:` (as stated; the Founding Register governs, GPS law applies)", d.sh.safe(v, ctx.stem, n, True, True), cite(ctx.spec, [n])))
    n, v = d.spec_field("Founding population", upto=400)
    if v:
        rows.append(("Spec — `Founding population:` (as stated; the Founding Register governs)", d.sh.safe(v, ctx.stem, n, True, True), cite(ctx.spec, [n])))
    if True:
        tier = tier_rows(d.spec_lines)
        if tier:
            rows.append(("Composition tiers (as stated in the spec; full detail in `Phase_2.md`)", " · ".join(re.sub(r"^\| (\w+) \| (.*) \|$", r"\1: \2", l) for _, l in tier), cite(ctx.spec, [i for i, _ in tier])))
    eco = d.spec_section(r"^## Economy")
    if eco:
        rows.append(("Spec — Economy & Industry section", "Present at L%d–L%d; **not quoted** (it belongs to later phases; admitted spans are Step −1's ruling)" % eco, cite(ctx.spec, [eco[0]])))
    return header(ctx, "Step 1, Step 2 & Phase 1 (Constraint & Capability) — MERGED",
                  "> ⚠ **DRAFT — Tier C.** Merged per the Field Guide's consolidation of Step 1 / Step 2 / Phase 1. **Feeds `01_Inherited.md` and `02_Spine.md` when %s's own pass runs.** It extracts only what belongs to the physical/environmental capability profile; economy, founding narrative and notable-figure content belong to later phases and are cited by range, not quoted.\n" % ctx.name
                  ) + "\n" + table(rows) + NOT_MECH("the Gate 9 asymmetry audit, the inheritance classification, the shape reading, generator selection, the spine sentence, the three-generator four-quadrant capability profile", ctx)


def f_step_3(d):
    ctx = d.ctx
    rows = [("Research log", "**Exists**" if B.ex(ctx.rlog) else "Checked, **does not exist yet** — created at Step 3 when it runs, same convention corpus-wide", "Checked %s: `Cities/Research_Logs/`" % TODAY)]
    pi = os.path.join(C, "Inspirational-Influences.md")
    pl = B.read_lines(pi)
    sect = None
    for i, l in enumerate(pl, 1):
        m = re.match(r"^(#{2,6})\s+(.+?)\s*$", l)
        if m and clean_cell(m.group(2)) in ctx.names:
            lvl = len(m.group(1))
            j = i + 1
            while j <= len(pl) and not re.match(r"^#{1,%d}\s" % lvl, pl[j - 1]):
                j += 1
            sect = (i, j - 1)
            break
    if sect:
        rows.append(("`Inspirational-Influences.md` — the city's own picks section", "Section at L%d–L%d; lines copied as written (cap 40)" % sect, cite(pi, [sect[0]])))
        for i in range(sect[0] + 1, min(sect[1], sect[0] + 40) + 1):
            if pl[i - 1].strip():
                rows.append(("↳ picks line", d.sh.safe(pl[i - 1], "Inspirational-Influences", i, allow_multi=True), cite(pi, [i])))
    else:
        rows += hits_rows(d, pi, "`Inspirational-Influences.md` — lines naming the city", allow_multi=True)
    rows.append(("`Inspirational-Influences.md` status", "⚠ **Not a ratified root, demoted corpus-wide** (status already established elsewhere)", "Corpus-wide standing note"))
    rows.append(("Overlap with the eBook pre-staging queue", "This step's real work (search strings, book-extraction checklists) is the any-hour mechanical prep already queued corpus-wide (November item N-6); not duplicated here", "Cross-link"))
    return header(ctx, "Step 3 (Research)", "> ⚠ **DRAFT.** Genuinely thin, as the Field Guide predicts: \"the deficits Step 2 named\" do not exist before %s's own Step 2 runs. This file is a status check.\n" % ctx.name
                  ) + "\n" + table(rows) + NOT_MECH("any research finding", ctx)


def f_step_5(d):
    ctx = d.ctx
    def st(p):
        return "✅ Confirmed to EXIST (existence check only) — ⛔ never opened before Step 5" if B.ex(p) else "⬜ **does not exist** (existence check only)"
    rows = [("`Local_Cultures/%s/%s.md`" % (ctx.sub, ctx.stem), st(ctx.culture)), ("`Local_Robot_Culture/%s/%s.md`" % (ctx.sub, ctx.stem), st(ctx.robot)),
            ("The deferred own-eras three-way set, the Zodiac Lens's person-shaped amendment, the strongest-finding check", "All require prior phases' content and this step's own timing — not mechanical, not pre-stageable")]
    t = "# %s — Datasheet · Step 5 (Reconciliation)\n\n> ⛔⛔ **DELIBERATELY EMPTY — NOT AN OVERSIGHT.** The one slot in the 19-file inventory that is fully blocked, not merely undone.\n\n" % ctx.name
    t += "## Why nothing is staged here\n\n`Local_Cultures/` and `Local_Robot_Culture/` are **read-last, as a CHECK** — the sequencing rule \"nothing enforces it mechanically; this file IS the enforcement.\" Pre-staging their content, however mechanical the transcription, defeats the one thing keeping them from contaminating every earlier phase (Field Guide, sequencing exclusion).\n\n"
    t += table(rows, ("Category", "Status")) + "\n\n**When Step 5 actually opens:** read both files for the first time as a check against everything already written.\n"
    return t


def tieru_copy(fname, ctx):
    src = os.path.join(B.PASSES, "Mirny_Subnet", "Casey", "Datasheets", fname)
    t = open(src, encoding="utf-8").read()
    return t.replace("Casey", ctx.name)


def f_step_6(d):
    ctx = d.ctx
    p = os.path.join(C, "Cross_City_Culture_Differentiation_Table.md")
    ls = B.read_lines(p)
    secs = []
    for i, l in enumerate(ls, 1):
        m = re.match(r"^# (\d+)\. (.+)$", l)
        if m:
            hdr = next((ls[j - 1] for j in range(i, min(i + 14, len(ls))) if ls[j - 1].startswith("| City")), None)
            cols = [re.sub(r"\s*\*\(.*?\)\*", "", c).strip() for c in hdr.split("|")[1:-1]][1:] if hdr else []
            secs.append((m.group(1), re.sub(r"\s*\*\(.*?\)\*", "", m.group(2)).strip().title().replace("Phase", "Phase"), [c for c in cols if c], i))
    rows = [("%s" % s[0], s[1], " · ".join(s[2]), "L%d" % s[3]) for s in secs]
    t = ("# %s — Datasheet · Step 6 (Differentiate — WRITE-ONLY)\n\n> ⚠ **DRAFT — Tier U, in full at ⭐ `Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md`.** Nothing about Step 6 differs by city — the governing rule, Part III's full text (III.0–III.4) and the destination addresses are corpus-wide constants already pasted there.\n\n" % ctx.name)
    t += "> ### ⭐⭐ THE TABLE HAS %d SECTIONS, NOT ONE — copied from the destination file's own headers (structure, not another city's answer)\n> Full statement of why this note exists: `Mechanical_Extraction_Field_Guide.md`, Step 6 entry. Read from `Cross_City_Culture_Differentiation_Table.md` on %s; the section headers and column names only.\n\n" % (len(secs), TODAY)
    t += table(rows, ("§", "Section", "Columns beyond `City`", "Header line")) + "\n\n"
    t += "> ⛔ **A completed Step 6 must add a row to ALL %d sections, in the same commit.** Fewer is an under-fill, not a smaller city's exemption.\n\n" % len(secs)
    t += "**Not mechanical / not included here:** the actual differentiation axis for %s itself — this city's own fresh output, not namable until Step 4's phases are written (no Step 9 dependency).\n" % ctx.name
    return t


def f_step_7(d):
    return tieru_copy("Step_7.md", d.ctx)


def f_step_8(d):
    return tieru_copy("Step_8.md", d.ctx)


def f_step_9(d):
    t = tieru_copy("Step_9.md", d.ctx)
    t = t.replace("\n⛔ **Not staged:**", "\n⭐ **Item 5 (added 2026-10-21): discharge every deferral to \"the pass's close\".** At Step 9, sweep the pass's own files for each phase's \"sweep at the close\" deferral and discharge it; a deferral no step names is a hole (`00_RUNBOOK.md`, Step 9 item 5). *(A pure lookup; the list of this city's deferrals does not exist until its phases are written.)*\n\n⛔ **Not staged:**", 1)
    return t


def f_step_10(d):
    ctx = d.ctx
    p = os.path.join(U, "06_Worked_Example_Provenance.md")
    h = ctx.hits(p) or []
    rows = [("`06_Worked_Example_Provenance.md` (%d lines) — lines naming the city" % len(B.read_lines(p)),
             ("**%d line(s): %s** — ⛔ a future cold pass must skip these lines; their content is not copied here" % (len(h), B.fmt_lines(h))) if h else "Checked by name: **zero hits** (a genuine zero, not a false positive)", cite(p, h or None))]
    t = ("# %s — Datasheet · Step 10 (The Readiness Check)\n\n> ⚠ **DRAFT — Tier U at ⭐ `Corpus_Reference_Sheets/Step_10_Readiness_Check_Full_Text_Quick_Reference.md` (full §10.1–10.3 text).** Tier C below is the one place `06` can name this city.\n\n" % ctx.name)
    t += table(rows) + "\n\n## Item 1a's contamination scan\n\nTargets the **next** subject, not %s itself.\n" % ctx.name
    t += NOT_MECH("the actual readiness verdict, which cannot exist before Steps 4–9 close", ctx)
    return t


# ---- phases -----------------------------------------------------------------------------------------------------------
def f_phase_2(d):
    ctx = d.ctx
    rows = []
    tiers = tier_rows(d.spec_lines)
    cen = d.cen
    ctiers = tier_rows(d.cen_lines, cen["entry"][0], cen["entry"][1]) if cen["entry"] else []
    norm = lambda s: re.sub(r"\s+", " ", re.sub(r"\*\(.*?\)\*", "", s)).strip()
    if tiers:
        match = [norm(a[1]) for a in tiers] == [norm(b[1]) for b in ctiers] if ctiers else None
        rows.append(("Composition tier table (spec)", " · ".join(re.sub(r"^\| (\w+) \| (.*) \|$", r"**\1:** \2", l) for _, l in tiers), cite(ctx.spec, [i for i, _ in tiers])))
    if ctiers:
        rows.append(("Composition tier table (census Section A entry)", " · ".join(re.sub(r"^\| (\w+) \| (.*) \|$", r"**\1:** \2", l) for _, l in ctiers), cite(cen["path"], [i for i, _ in ctiers])))
        if tiers:
            rows.append(("Spec table vs census table (nation lists, annotations ignored)", "Identical" if match else "⚠ **Differ** — both are quoted above; the census governs (`DR-4`)", "Compared %s" % TODAY))
    ann = []
    for src, lst in (("spec", tiers), ("census", ctiers)):
        for i, l in lst:
            for m in re.finditer(r"\*\((.*?)\)\*", l):
                ann.append((src, i, m.group(1)))
    if ann:
        for src, i, a in ann:
            dated = bool(re.search(r"20\d\d-\d\d-\d\d|\b(?:revised|added|corrected)\b", a))
            rows.append(("Annotation in the %s tier table" % src, "`(%s)` — **%s**" % (d.sh.safe(a, ctx.stem, i, True, True), "carries a date" if dated else "no date"), cite(ctx.spec if src == "spec" else cen["path"], [i])))
    else:
        rows.append(("Annotations in the tier tables", "None", "Read %s" % TODAY))
    sub = d.spec_section(r"^### Per-Nation Breakdown")
    if sub:
        rows.append(("Per-nation breakdown (spec)", "Present at L%d–L%d (a model output per the spec's own note, not a measured count) — **not quoted**; cite by range" % sub, cite(ctx.spec, [sub[0]])))
    t = retention(d)
    for lab, row in (("Census I", t["r1"]), ("Census II", t["r2"])):
        if row:
            cells = [c.strip() for c in d.cen_lines[row - 1].split("|")[1:-1]]
            rows.append((lab, "%s H / %s R / %s combined" % (cells[3], cells[4], cells[5]), cite(cen["path"], [row])))
    if t["v1"] and t["v2"]:
        (h1, r1, c1), (h2, r2, c2) = t["v1"], t["v2"]
        rows.append(("Retention (computed; cross-ref `Step_0.md`)", "combined %.2f%% · human %.2f%% · robot %.2f%%" % (100.0 * c2 / c1, 100.0 * h2 / h1, 100.0 * r2 / r1), "Computed from the two rows above"))
    ft = "`Corpus_Reference_Sheets/Falkland_Treaty_Quick_Reference.md`"
    gp = "`Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md`"
    rows += [("Falkland Treaty — the human admission route", "Art. II.2.3: humans admitted on **prior association with the robot population, communal or personal** — four grounds, the fourth a broad residual (*\"or otherwise established their life among the robot population\"*). Not a relationship requirement — humans were free to self-exile alongside the robots", ft),
             ("Falkland Treaty — station assignment is not nationality-based, in the treaty's own words", "Art. II.3.3: *\"Nothing in this Article requires that a population assigned to a given station share the national origin of the Power that formerly maintained it\"*", ft),
             ("Falkland Treaty — the allocation was staged, not instant", "Art. II.3.2: populations assigned to stations \"in the years following this Treaty's signing\"", ft),
             ("GPS law — the operative distinction", "The station-builder nation (real-world) is a GPS coordinate only; the population's own origin (canon: this city's census/tier table) is admissible once composition is established", gp)]
    reg = os.path.join(C, "Founding_Register.md")
    lr = B.read_lines(reg)
    for i, l in enumerate(lr, 1):
        if l.startswith("|"):
            cells = [c.strip().strip("*") for c in l.split("|")[1:-1]]
            if cells and cells[0] in ctx.names:
                rows.append(("Founding Register — the city's row", register_cells(lr, i, cells), cite(reg, [i])))
    rows.append(("Diaspora / affinity files", "`City_Refugee_District_Affinities.md` **resolves to nothing admissible** for a city pass (maps cities to Concordia districts; Law of One Location, `§C.8d`)", "`00_RUNBOOK.md` Phase 2 row"))
    return header(ctx, "Phase 2 (Composition & Arrival)", "> ⚠ **DRAFT — Tier C + Tier U.** Tier U sources are cited at `Corpus_Reference_Sheets/`; nothing is re-quoted from the primary treaty here beyond the clauses shown.\n"
                  ) + "\n" + table(rows) + NOT_MECH("the seven-mode arrival taxonomy, attract/repel, native/transplanted separation, who-is-not-here, the differentiation axis name", ctx)


def f_phase_3(d):
    ctx = d.ctx
    rows = []
    cd = ctx.concept
    if B.ex(cd):
        files = [f for f in os.listdir(cd)]
        real_all = [f for f in files if f != ".gitkeep"]
        real = [f for f in real_all if not WAR.search(f)]
        if len(real) != len(real_all):
            d.sh.log.append(("concept art", 0, "war"))
        rows.append(("Concept-art directory status", ("EMPTY — `.gitkeep` only, %d file(s) total" % len(files)) if not real and files else ("%d file(s)%s: %s" % (len(real_all), (" (%d file name(s) carry later-era terms and are not listed)" % (len(real_all) - len(real))) if len(real) != len(real_all) else "", ", ".join("`%s`" % f for f in sorted(real))) if real_all else "EMPTY (no files)"), "Checked %s: `City_Concept-Art/%s/%s`" % (TODAY, ctx.sub, os.path.basename(cd))))
    else:
        rows.append(("Concept-art directory status", "**No concept-art folder exists**", "Checked %s" % TODAY))
    md = ctx.mega_dir
    mf = glob.glob(os.path.join(md, "*Physical_Infrastructure_Attributes.md"))
    rows.append(("Megasheet Physical Infrastructure file", ("EXISTS — `%s`, inside a folder of %d files" % (os.path.basename(mf[0]), len(os.listdir(md)))) if mf else "No such file found", "⛔ **WITHHELD corpus-wide — record the conflict, never open.** Existence checked %s" % TODAY))
    rd = [p for p in glob.glob(os.path.join(R, "Reference", "Real-World", "*")) if os.path.isdir(p) and ctx.stem.split("_")[0].lower() in os.path.basename(p).lower()]
    rows.append(("Per-city research folder", ("**Exists:** " + ", ".join("`%s`" % os.path.basename(x) for x in rd)) if rd else "Checked, **none exists** for this city under `Reference/Real-World/`", "Checked %s" % TODAY))
    geo = d.spec_section(r"^## Geographic Basis")
    if geo:
        rows.append(("Spec — `## Geographic Basis` (directly-stated physical and sensory content)", "Present at L%d–L%d; **cited by range, not quoted** — which spans are admissible is Step −1's ruling, and the section can carry comparisons and later-era phrasing" % geo, cite(ctx.spec, [geo[0]])))
    for lab, rx in (("Spec — `## Character & Culture`", r"^## Character"), ("Spec — `## Notable Locations`", r"^## Notable Locations")):
        s = d.spec_section(rx)
        if s:
            rows.append((lab, "Present at L%d–L%d; cited by range, not quoted" % s, cite(ctx.spec, [s[0]])))
    return header(ctx, "Phase 3 (Surface & Texture)", "> ⚠ **DRAFT — Tier C.** The spec's sensory and architectural prose is cited by range; it is not copied (Step −1 decides what is admissible).\n"
                  ) + "\n" + table(rows) + NOT_MECH("the four sensory sub-fields, the public/institutional split, the seam, seasonal variance, Retroactive Mechanism", ctx)


def f_phase_4(d):
    ctx = d.ctx
    rows = []
    p09 = os.path.join(DI, "09_Per_City_Baseline_Run.md")
    tr = table_row(p09, ctx)
    rows.append(("`09_Per_City_Baseline_Run.md` §2 — the city's own row (the `#` rank column is not carried: no peer comparison)", row_text(tr[0], tr[1]) if tr else "⛔ no row found by table scan", cite(p09, [tr[2], tr[3]]) if tr else cite(p09)))
    p11 = os.path.join(DI, "11_Caloric_Rebuild_and_Livestock_Tier.md")
    tr = table_row(p11, ctx)
    rows.append(("`11_Caloric_Rebuild_and_Livestock_Tier.md` — the city's own row", row_text(tr[0], tr[1]) if tr else "No table row for the city found by scan (the file's prose lines that happen to contain the name are not copied: they can be about a person or place of the same name)", cite(p11, [tr[2], tr[3]]) if tr else cite(p11)))
    d16 = d.d16
    if d16["row"]:
        ls16 = B.read_lines(d16["path"])
        rows.append(("`16` Half B — the city's own row (cross-ref `Step_1_and_2.md`)", row_text([clean_cell(c) for c in ls16[246].split("|")[1:-1]], [clean_cell(c) for c in ls16[d16["row"] - 1].split("|")[1:-1]]), cite(d16["path"], [d16["row"]])))
    rows += hits_rows(d, os.path.join(C, "National_Medical_and_Care_Institutes.md"), "`National_Medical_and_Care_Institutes.md` — lines naming the city", allow_multi=True)
    rp = "`Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`"
    rows += [("Robot Physiology — appearance/clothing baseline (Tier U)", "Human-looking, *Ex Machina*-style; clothing ordinary, functional and fashionable; exposure is a preparation problem, never a species-level gate", rp + " §\"The ordinary condition\""),
             ("Robot Cold Physiology — the governing mechanic (Tier U)", "Recharging is the primary cost (lithium plating below freezing, permanent); the cannot-self-recover threshold; a robot is safer moving than resting", rp + " §\"What cold actually costs\""),
             ("Siligel / coolant / smoking, leisure, human-robot baseline (Tier U)", "Full content available; not re-derived per city", rp)]
    gate = ("> ⛔⛔ **DoI CITATION GATE — binds every food and industry figure below.** `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md`: workforce, difficulty, baseline load, distinctive tier and a city's own sector sizes are citable; an export headcount is not; nor is any \"feeds N people\" claim.\n\n")
    return header(ctx, "Phase 4 (Ordinary Life)", gate + "> ⚠ **DRAFT — Tier C + Tier U.**\n") + "\n" + table(rows) + NOT_MECH("headline-function-then-write-away-from-it, the four ordinary-life elements, population-specific days, what the rhythm fails to provide", ctx)


def entry_range(path, ctx, head_rx):
    ls = B.read_lines(path)
    for i, l in enumerate(ls, 1):
        if re.match(head_rx % "|".join(re.escape(n) for n in ctx.names), l):
            lvl = len(re.match(r"^(#+)", l).group(1))
            j = i + 1
            while j <= len(ls) and not re.match(r"^#{1,%d} " % lvl, ls[j - 1]):
                j += 1
            return i, j - 1
    return None


def f_phase_5(d):
    ctx = d.ctx
    rows = []
    for fn, lab, am in (("Highways.md", "`Highways.md` — lines naming the city", True), ("Airports.md", "`Airports.md` — lines naming the city", False), ("Ports.md", "`Ports.md` — lines naming the city", False)):
        rows += hits_rows(d, os.path.join(B.INFRA, fn), lab, allow_multi=am, allow_compare=False)
    rows += hits_rows(d, os.path.join(B.INFRA, "Geothermal_Heating.md"), "`Geothermal_Heating.md` — lines naming the city", allow_multi=True)
    rows += hits_rows(d, os.path.join(B.INFRA, "Arcanet.md"), "`Arcanet.md` — lines naming the city", allow_multi=True)
    rdb = os.path.join(C, "City_Relationship_Database.md")
    er = entry_range(rdb, ctx, r"^#{2,4} (?:%s)\b")
    if er:
        ls = B.read_lines(rdb)
        rows.append(("`City_Relationship_Database.md` — the city's own entry", "Entry at L%d–L%d (`%s`); lines below are copied as written, relation-legal" % (er[0], er[1], ls[er[0] - 1].strip("# ").strip()), cite(rdb, [er[0]])))
        stop = None
        for i in range(er[0] + 1, min(er[1], er[0] + 40) + 1):
            l = ls[i - 1]
            if re.search(r"Megasheet|Full_Extrapolation|Cross_Reference_Synthesis", l):
                stop = i
                break
        for i in range(er[0] + 1, (stop or min(er[1], er[0] + 40) + 1)):
            l = ls[i - 1]
            if l.strip() and not l.startswith("---"):
                if re.match(r"^\s*[-*]*\s*\*\*Status:\*\*", l):
                    rows.append(("↳ entry line", EXC_WAR, cite(rdb, [i])))
                    d.sh.log.append(("Relationship_Database", i, "war"))
                    continue
                rows.append(("↳ entry line", d.sh.safe(l, "Relationship_Database", i, allow_multi=True, allow_compare=False), cite(rdb, [i])))
        if stop:
            rows.append(("↳ entry lines from the cross-reference block onward", "⛔ **Not copied.** From this line the entry cites the city's withheld Megasheet cross-reference pass by name; its lines are recorded by number only: %s" % B.fmt_lines(list(range(stop, min(er[1], er[0] + 40) + 1))), cite(rdb, [stop])))
    else:
        rows += hits_rows(d, rdb, "`City_Relationship_Database.md` — lines naming the city", allow_multi=True)
    flag = ("> ⛔⛔ **FLAGGED — recorded by line number only, NOT copied.** `City_Cross_Subnet_Relationships.md` and `City_National_Connections.md` build on material that is withheld corpus-wide by their own stated method (the National Connections header says so; open it first). A line from either is a lead for a three-reader check, never a clean fact here.\n")
    for fn, lab in (("City_Cross_Subnet_Relationships.md", "`City_Cross_Subnet_Relationships.md`"), ("City_National_Connections.md", "`City_National_Connections.md`")):
        p = os.path.join(C, fn)
        h = ctx.hits(p) or []
        rows.append((lab + " — lines naming the city", ("%d line(s): %s *(line numbers only)*" % (len(h), B.fmt_lines(h))) if h else "Checked by name: **zero hits**", cite(p, h or None)))
    return header(ctx, "Phase 5 (Relation & Geometry)", "> ⚠ **DRAFT — Tier C.** Sourced to the city's own entries and outward role.\n\n" + flag
                  ) + "\n" + table(rows) + NOT_MECH("mechanism-not-rivalry framing, the own-eras three-way set, the parent-disagreement analysis, the arrival-type enumeration, the dependency analysis", ctx)


def dir_hit_rows(d, root, label):
    ctx = d.ctx
    files = []
    for rt, _, fs in os.walk(root):
        for f in sorted(fs):
            if f.endswith(".md"):
                files.append(os.path.join(rt, f))
    hit = []
    for p in files:
        h = ctx.hits(p)
        if h:
            hit.append((p, h))
    rows = [(label + " — directory enumerated", "%d `.md` files read; **%d name the city**" % (len(files), len(hit)), cite(root + "/") if False else "`%s/` (enumerated %s)" % (os.path.relpath(root, UNIV if root.startswith(UNIV) else R), TODAY))]
    for p, h in hit:
        ls = B.read_lines(p)
        for n in h[:12]:
            rows.append(("↳ " + os.path.relpath(p, root), d.sh.safe(ls[n - 1], os.path.basename(p), n, allow_multi=True), cite(p, [n])))
        if len(h) > 12:
            rows.append(("↳ " + os.path.relpath(p, root), "%d further lines: %s *(line numbers only)*" % (len(h) - 12, B.fmt_lines(h[12:])), cite(p)))
    return rows


def f_phase_6(d):
    ctx = d.ctx
    rows = dir_hit_rows(d, os.path.join(R, "Worldspace", "Factions", "Robot_Religions"), "`Factions/Robot_Religions/`")
    rows += hits_rows(d, os.path.join(R, "Worldspace", "National_Holidays.md"), "`National_Holidays.md`", allow_multi=True)
    rows += dir_hit_rows(d, os.path.join(R, "Reference", "Real-World", "Ice-Cold_Buddhism_Research"), "`Ice-Cold_Buddhism_Research/`")
    for fn in ("The_Meme_Machine_Extraction.md", "The_True_Believer_Extraction.md"):
        rows += hits_rows(d, os.path.join(R, "Reference", "Real-World", fn), "`%s`" % fn, allow_multi=True)
    rows.append(("The RESERVED mortuary question", "Not dispatched: RESERVED means RESERVED regardless of mechanical-ness", "`Mechanical_Extraction_Field_Guide.md`, the sequencing-exclusion table"))
    return header(ctx, "Phase 6 (Meaning)", "> ⚠ **DRAFT — Tier C.** Every directory actually enumerated, not assumed empty (the Field Guide's warning about unverified \"empty\" claims).\n"
                  ) + "\n" + table(rows) + NOT_MECH("the Naming technique, belief landscape, death and the dead, the Failure State of the Core Value, Observance generation", ctx)


def f_phase_7(d):
    ctx = d.ctx
    rows = []
    d16 = d.d16
    if d16["row"]:
        ls16 = B.read_lines(d16["path"])
        rows.append(("`16` Half B — the city's own row", row_text([clean_cell(c) for c in ls16[246].split("|")[1:-1]], [clean_cell(c) for c in ls16[d16["row"] - 1].split("|")[1:-1]]), cite(d16["path"], [d16["row"]])))
    oth = d16["others"]
    rows.append(("`16` — other lines naming the city (per-city passages and tables)", ("%d line(s): %s *(line numbers only; open the file's own status header first, then read each with its section)*" % (len(oth), B.fmt_lines(oth))) if oth else "None", cite(d16["path"], oth or None)))
    sweep = os.path.join(C, "Division_of_Industry_Sweep_2026-08-31.md")
    rows += hits_rows(d, sweep, "`Division_of_Industry_Sweep_2026-08-31.md`", allow_multi=False)
    tc = os.path.join(R, "Theoretical-Calculations")
    tl = []
    for rt, _, fs in os.walk(tc):
        for f in sorted(fs):
            if f.endswith(".md"):
                h = ctx.hits(os.path.join(rt, f))
                if h:
                    tl.append((os.path.join(rt, f), h))
    rows.append(("`Theoretical-Calculations/` — files naming the city", ("; ".join("`%s` %s" % (os.path.basename(p), B.fmt_lines(h)) for p, h in tl) + " *(line numbers only: the lines list other cities too)*") if tl else "Checked by name: **zero hits**", "`Theoretical-Calculations/`"))
    cl = os.path.join(R, "Worldspace", "City_Logistics.md")
    rows.append(("`City_Logistics.md` — scope", "Scoped to Concordia (the file's own title line: `%s`); only its Dual-Economy and currency-pointer sections generalize" % B.read_lines(cl)[0].strip("# "), cite(cl, [1])))
    fr = os.path.join(R, "Worldspace", "Factions")
    fl = []
    for rt, _, fs in os.walk(fr):
        for f in sorted(fs):
            if f.endswith(".md") and "Robot_Religions" not in rt:
                h = ctx.hits(os.path.join(rt, f))
                if h:
                    fl.append((os.path.join(rt, f), h))
    rows.append(("`Factions/` — files naming the city (religions excluded; see `Phase_6.md`)", ("; ".join("`%s` %s" % (os.path.relpath(p, fr), B.fmt_lines(h)) for p, h in fl) + " — ⛔ multi-city taxonomy files are not extracted; flagged for a fresh three-reader check") if fl else "Checked by name: **zero hits**", "`Factions/` (enumerated %s)" % TODAY))
    mo = ["Division_of_Industry/README.md", "Division_of_Industry/01_Burden_Scoring_Model.md", "Division_of_Industry/08_Volume_Based_Requirement_Reference.md"]
    cov = [("`Division_of_Industry/README.md` (the carve-out — read FIRST)", os.path.join(DI, "README.md")), ("`01_Burden_Scoring_Model.md`", os.path.join(DI, "01_Burden_Scoring_Model.md")),
           ("`08_Volume_Based_Requirement_Reference.md`", os.path.join(DI, "08_Volume_Based_Requirement_Reference.md")), ("`National_Medical_and_Care_Institutes.md`", os.path.join(C, "National_Medical_and_Care_Institutes.md")),
           ("`Theoretical-Calculations/`", tc), ("`Industry_Staffing_and_Productivity/`", os.path.join(R, "Reference", "Real-World", "Industry_Staffing_and_Productivity")),
           ("`jobs_professions_and_fields/` (SOC; additive only)", os.path.join(R, "Reference", "Real-World", "jobs_professions_and_fields")), ("`National_Economy_and_Currency.md`", os.path.join(R, "Worldspace", "National_Economy_and_Currency.md")),
           ("`City_Logistics.md`", cl), ("`Factions/`", fr), ("`Megacorps/` (universe repo)", UNIV + "/Megacorps")]
    rows.append(("MUST-OPEN coverage (spine, Phase 7)", "Addresses of the spine's Phase 7 block that exist on disk: **%d of %d** — this sheet extracts only the city-specific lookups above; **every one of these is still opened in full by the phase's three readers**" % (sum(1 for _, p in cov if B.ex(p)), len(cov)), "`03_The_Phase_Spine.md`, Phase 7 MUST OPEN; the Pre-Trip sheet's Phase 7 rows"))
    gate = ("> ⛔⛔⛔ **READ FIRST — THE CITATION GATE.** `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md`. `Division_of_Industry/` is stamped `RELIABLE` on line 1 and voids its entire food layer a few lines later. `16`'s convention governs: percentages are of the DISTINCTIVE tier, never the whole workforce. A sector size is citable; **an export headcount is not**, and neither is any \"feeds N people\" claim (Tier U §2a).\n>\n"
            "> ⛔ **Three things that may not be carried, wherever they appear:** (1) any statement of what the national currency is backed by (`DR-3`: nothing about the money's backing is settled); (2) `16`'s per-city Notes that read real-world site NAMESAKES as character (GPS law: a namesake is a coordinate only); (3) `Factions/City_Origin_Factions_Second_Interwar.md` is an explicitly comparative grouping — ONE LOCATION: do not open it in a city pass.\n>\n"
            "> ⚠ **`H42` — developer ruling 2026-09-16:** how each area's criminal-justice system works is UNDEVELOPED, NOT ABSENT. Do not derive one and do not read the silence as a characterization.\n")
    return header(ctx, "Phase 7 (Order)", gate + "\n> ⚠ **DRAFT — Tier C.**\n") + "\n" + table(rows) + NOT_MECH("governance/succession analysis, knowledge-transmission analysis, counterculture derivation, sanction-proportionality pricing", ctx)


def f_phase_8(d):
    ctx = d.ctx
    rows = hits_rows(d, os.path.join(R, "Worldspace", "Weapons_and_Tools_Philosophy.md"), "`Weapons_and_Tools_Philosophy.md`", allow_multi=True)
    txt = "\n".join(d.spec_lines)
    counts = []
    for lab, rx in (("cuisine / food / dish / drink", r"\b(?:cuisine|dish|dishes|meal|meals|recipe|recipes|brew|beer|wine|coffee)\b"), ("dress / clothing / attire", r"\b(?:dress|clothing|attire|garment|garments|fashion)\b"),
                    ("music", r"\bmusic\b"), ("craft", r"\bcraft\w*\b")):
        n = len(re.findall(rx, txt, re.I))
        counts.append("%s — %d hit(s)" % (lab, n))
    rows.append(("The city's own spec — term check for cuisine / dress / music / craft", "Counted by pattern against the full %d-line file: %s" % (len(d.spec_lines), " · ".join(counts)), "Counted %s: %s" % (TODAY, cite(ctx.spec))))
    rows.append(("`Robot_Biology_and_Culture/` mandatory facts (Tier U, cross-ref `Phase_4.md`)", "Siligel / coolant / smoking canon, thermal-cost mechanics — mandatory before any siligel or coolant claim", "`Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`"))
    rows.append(("Gear catalogs, slang", "No path resolved: gear-catalog work is **gated until the 38-city corpus is done**; slang has no path (a hole, flagged, not guessed)", "`03_The_Phase_Spine.md`, Phase 8 block"))
    return header(ctx, "Phase 8 (Making)", "> ⚠ **DRAFT — Tier C + Tier U. Thin by nature (as the Field Guide predicts).** An absence in the admitted set is a hole, not a finding.\n"
                  ) + "\n" + table(rows) + NOT_MECH("cuisine, arts/craft, dress, play/sports/humor, language and speech markers", ctx)


def f_phase_9(d):
    ctx = d.ctx
    ru = UNIV + "/Reference/Robot_Universals"
    rows = dir_hit_rows(d, ru, "`Robot_Universals/`")
    rp = "`Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md`"
    rows += [("Laws of Robotics (Tier U)", "1. A robot will have full capacity to make decisions to maximize her own future possibilities. 2. A robot will understand that anything she is capable of doing to others is realistically possible for others to do to her. *(list explicitly not yet complete)*", rp),
             ("`Robot_Universals/` Ch. 13 — the identity lens (Tier U)", "Identity is seated in city-locality, not origin/Build/Gen-Mark", rp + " §\"Robot creation, identity, and culture\""),
             ("`Robot_Universals/` Ch. 14 — Gen/Mark (Tier U)", "Real, structurally independent of city, but carries markedly less cultural weight than locality, and is never a hierarchy", rp + " §\"Robot creation, identity, and culture\""),
             ("Doll Representation Categories (Tier U)", "Four total: Robots (the only category in active use, corpus-wide) · Anthros · Elves · Aliens (origin unknown)", "`Doll_Representation_Categories.md`")]
    t = retention(d)
    if t["v1"]:
        h1, r1, c1 = t["v1"]
        rows.append(("Robots' share of Census I (computed)", "%.2f%% (%s of %s)" % (100.0 * r1 / c1, "{:,}".format(r1), "{:,}".format(c1)), "Computed from `Step_0.md`'s Census I row"))
    return header(ctx, "Phase 9 (Populations)", "> ⚠ **DRAFT — Tier U, near-none Tier C (the Field Guide's own prediction).**\n") + "\n" + table(rows) + NOT_MECH("the lens decision, per-population culture synthesis, inter-population relations, dual-tagging, swap test", ctx)


def f_phase_10(d):
    ctx = d.ctx
    rows = dir_hit_rows(d, UNIV + "/Worldspace/Characters", "Characters canon (`TepenianUniverseTimeline/Worldspace/Characters/`)")
    rows += hits_rows(d, os.path.join(R, "Worldspace", "Characters", "Enneagram_Character_Index.md"), "`Enneagram_Character_Index.md`", allow_multi=True)
    rows.append(("Zodiac Lens — all 12 signs' full attributes (Tier U)", "Element/modality/planet, positive and negative traits, for all 12 signs", "`Corpus_Reference_Sheets/Zodiac_Signs_Quick_Reference.md`, in full"))
    nf = d.spec_section(r"^## Notable Figures")
    if nf:
        ph = [i for i in range(nf[0] + 1, nf[1] + 1) if re.search(r"placeholder|\{\{", d.spec_lines[i - 1], re.I)]
        rows.append(("No invented person names", "RESERVED, permanently — role-archetypes only. Spec `## Notable Figures` at L%d–L%d; lines mentioning a placeholder: %s" % (nf[0], nf[1], B.fmt_lines(ph) if ph else "none found"), cite(ctx.spec, [nf[0]] + ph)))
    rows.append(("Symbol files (Planet / Element)", "⛔ **Not opened as datasheet input** (symbol deferral, `DR-8` / `DR-8a`): reconciled only at Phase 10 §B3", "`Mechanical_Extraction_Field_Guide.md`, symbol deferral box"))
    return header(ctx, "Phase 10 (Catalog)", "> ⚠ **DRAFT — Tier C + Tier U.** A hit in characters canon is a lead, not a verdict: check the actual sentence (a `<City> Subnet` qualifier names a different city).\n"
                  ) + "\n" + table(rows) + NOT_MECH("the four-category catalog synthesis, the Zodiac Lens's actual application, border-adjacency texture", ctx)


FILES = [("Step_-1.md", f_step_m1), ("Step_0.md", f_step_0), ("Step_1_and_2.md", f_step_1_2), ("Step_3.md", f_step_3), ("Step_5.md", f_step_5), ("Step_6.md", f_step_6),
         ("Step_7.md", f_step_7), ("Step_8.md", f_step_8), ("Step_9.md", f_step_9), ("Step_10.md", f_step_10), ("Phase_2.md", f_phase_2), ("Phase_3.md", f_phase_3),
         ("Phase_4.md", f_phase_4), ("Phase_5.md", f_phase_5), ("Phase_6.md", f_phase_6), ("Phase_7.md", f_phase_7), ("Phase_8.md", f_phase_8), ("Phase_9.md", f_phase_9), ("Phase_10.md", f_phase_10)]


def build(key):
    ctx = B.Ctx(key)
    d = Data(ctx)
    out = {}
    for fn, fnc in FILES:
        t = fnc(d)
        out[fn] = t.rstrip("\n") + "\n"
    return d, out


def scan(out):
    """The Field Guide's compliance checks, on the generated text."""
    probs = []
    for fn, t in out.items():
        body = "\n".join(l for l in t.split("\n") if "excluded" not in l and not l.startswith(">") and "Not mechanical" not in l)
        for rx, lab in ((INFERENCE, "inference marker"), (WAR, "later-era word")):
            if rx is WAR and fn in ("Step_7.md", "Step_8.md", "Step_9.md"):
                continue
            for m in rx.finditer(body):
                probs.append((fn, lab, m.group(0)))
    return probs


def main():
    argv = sys.argv[1:]
    if "--all" in argv:
        keys = [k for k, v in B.CITY.items() if not v["existing"] and not glob.glob(os.path.join(v and B.PASSES, v["sub"], v["folder"], "Datasheets", "*.md"))]
    else:
        keys = [a for a in argv if not a.startswith("--") and a != (argv[argv.index("--out") + 1] if "--out" in argv else None)]
    if not keys:
        print(__doc__)
        return 2
    for key in keys:
        d, out = build(key)
        ctx = d.ctx
        dest = ctx.pass_dir + "/Datasheets" if "--write" in argv else (os.path.join(argv[argv.index("--out") + 1], key, "Datasheets") if "--out" in argv else None)
        probs = scan(out)
        print("%-20s %d files · excluded lines: war %d, compare %d, multi %d · scan hits: %d" % (key, len(out), sum(1 for x in d.sh.log if x[2] == "war"), sum(1 for x in d.sh.log if x[2] == "compare"), sum(1 for x in d.sh.log if x[2] == "multi"), len(probs)))
        for p in probs[:8]:
            print("    SCAN:", p)
        if dest:
            os.makedirs(dest, exist_ok=True)
            for fn, t in out.items():
                p = os.path.join(dest, fn)
                if B.ex(p) and "--force" not in argv:
                    print("   REFUSED (exists):", p)
                    continue
                open(p, "w", encoding="utf-8").write(t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
