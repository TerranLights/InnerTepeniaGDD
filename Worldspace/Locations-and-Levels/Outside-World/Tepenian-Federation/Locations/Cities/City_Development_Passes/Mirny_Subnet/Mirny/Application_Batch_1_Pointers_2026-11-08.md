# Mirny · Application Batch 1 · End-of-file pointer lines · 2026-11-08

> **UPDATE 2026-11-08 (later the same day): APPLIED.** The developer approved all 11 pointers and the orchestrator applied them after a second reader passed the batch (`DR-123`); the early-step pointers also carry the added relay and live-extent sentence. The status text below is the text as first written.

> **STATUS: PREPARED, NOT APPLIED.** No pass file was edited. Each line below is applied only when the dockets are
> applied (`DR-116` item 2; `DR-122` item 2), and only after a second reader has read it against the whole finding it
> touches (`Amendment_Layer_Rules.md` rule 4). `DR-101` is reconciled at that moment (`DR-116` item 2).

## Summary

On 2026-11-08 the developer approved one pointer line at the very end of ten Mirny files named in `DR-122` item 2, plus the symbol review through DEC-203's marks, which the developer is asked to confirm before it is applied (`DR-122`, the last entry
of `DEVELOPER_RULINGS_LOG.md`; DEC-140, DEC-160, DEC-180 and DEC-203 in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`).
This file holds the exact line for each file, the file's current last line, where the line's text comes from, and
what was changed from the piece's text. Six texts serve eleven files: one shared by the five early step files, one for
Phase 3, one shared by Phases 4 and 5, and one each for Phase 10, Step 5 and the symbol review of 2026-10-13.

The pieces' texts were updated only where the developer's answers in `DR-122` settled them: Air is confirmed with its
one-word label still provisional, and Wood is reserved (DEC-201). The Planet is Neptune, provisional, with Uranus
reserved, Saturn not confirmed, and the Planet hold lifted (DEC-200, DEC-202). The word warning keeps both of its uses
(DEC-162). Two plainness edits were also made: abbreviations that the target files do not define are spelled out. Every
change is listed in the entry for its file.

**Folder.** `M` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/`.

**How each line goes in.** Append only: one blank line, then the pointer line, after the file's current last line,
which ends with a newline in all eleven files. Nothing else changes, so no cited line moves (rule 3). The blank line
is needed because five files end inside a table (the input contract, Phases 3, 4 and 5, Step 5), three inside a
list (the Frame, Phase 10, the symbol review) and three in a paragraph (Inherited, the Spine, Research). Without it,
Markdown would read the pointer as a table row, a list continuation or the same paragraph.

## Notes for the second reader

1. **DK16-2 belongs to Step 5, not Phase 10:** its lines are `05_Reconciliation.md` L519 to L527 (ST16 L405). So the
   Phase 10 line carries DK16-1, DK16-3 and DK16-4, and the Step 5 line carries DK16-2 and DK16-5 to DK16-7.
2. **DEC-203's eleven marks:** DK16-1 to DK16-7 and DK16-10 are carried by three lines here. DK16-8 and DK16-9 are
   registry cells, not pointers, and are applied after a second reader reads Mirny's registry row (`DR-122` item 1).
   DK16-11 is "no edit".
3. **DEC-202's answer leaves the Planet cell showing the hold only, but `DR-122` item 1 lifts the hold** with Neptune
   decided. These pointers state the decided fact. The registry cell text is outside this batch and needs
   reconciling before DK16-9 is applied.
4. **The census row cited by the early-step line (L500) carries a revision note that names another location** (not
   named here). ST16 took the same figures from `ST14` L9 instead. The anchor is kept as approved. The alternative is
   "per piece ST12, section 2", the form the Phase 3 and Phases 4 and 5 lines use.
5. **The symbol review's line (DK16-10) is covered by DEC-203's eleven marks**, although `DR-122` item 2's list does not
   name that file.
6. **The Phases 4 and 5 line names Phase 4's lines in its warning clause, and Phase 5 never uses the word.** The text
   is kept identical in both files because one text was approved for both (AS14-54; DEC-180). The clause has no effect
   in Phase 5.
7. **Anchors checked live on 2026-11-08:** `Founding_Register.md` L57 is Mirny's row. `Official_Population_Census.md`
   L500 is Mirny's Census I row (692,971 / 710,578 / 1,403,549). `Specs/Mirny subnet/Mirny.md` (252 lines) L20 to L22
   are the three stock tiers. Every line the Phase 10 and Step 5 marks name (`P10` L421, L425, L426, L538, L539, L575,
   L588; `S5` L301, L519, L523 to L525, L657, L709, L766) holds the text the marks describe.

## Apply script (NOT RUN)

This script appends each line safely. Run it only when the dockets are applied and the second reader has passed every
line. It first checks all eleven files and writes nothing if any check fails. For each file it checks the line count,
the exact last line, the final newline, and that the pointer is not already present. It then appends, and confirms
that each file is its old bytes plus exactly the appended text.

```python
#!/usr/bin/env python3
# Mirny Application Batch 1: append one end-of-file pointer line to each of eleven files.
# NOT RUN. Apply only with the dockets (DR-116 item 2; DR-122 item 2), after the second reader (ALR rule 4).
import os
import sys

M = ("/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/"
     "Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/"
     "Mirny_Subnet/Mirny")

P_ST12 = """*Addenda proposed 2026-11-05 beside this file (piece ST12, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`); this file is not reworded (`DR-102`). Read its statements of no teacher, no inherited judgment, an unread cue or a private reading as the first generation's (Act 1); founders per the Founding Register (`Founding_Register.md` L57); live census and composition per the census (`Official_Population_Census.md` L500) and Mirny's spec (`Specs/Mirny subnet/Mirny.md` L20 to L22); the relay carries the weather warnings (`DR-76`); the extent at Census I is 140.35 km² at 10,000 per km² and 200.51 km² at 7,000 per km², computed from `Official_Population_Census.md` L500.*"""

P_ST13 = """*Addenda proposed 2026-11-05 beside this file (piece ST13, `Amendment_Rederivation_ST13_Phase3_2026-11-05.md`); this file is not reworded (`DR-102`). The weather warnings travel on the relay (`DR-76`). Read its statements of unread or unlearned cues, a reader that does not exist, blame or carelessness as the first generation's (Act 1) and the not-yet-taught's; warning in this file names the wind's own first sign, and the word keeps both uses, this one and the weather warning on the relay, with context deciding (`DR-122`); spec line numbers are the 230-line spec's (+22 from old L46); live census, founders and extent per piece ST13, section 2.*"""

P_ST14 = """*Addenda proposed 2026-11-05 beside this file (piece ST14, `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md`); this file is not reworded (`DR-102`). The weather warnings travel on the relay (`DR-76`). Read its statements of unread cues, no teacher, no public wind call, blame or carelessness, and a relay restored by position or kept invisibly, as the first generation's (Act 1) and the not-yet-taught's; warning in Phase 4 at L122 and L269 names the wind's own first sign, and the word keeps both uses, that one and the weather warning on the relay, with context deciding (`DR-122`); the lived middle is deferred to the cultural synthesis pass (CST, `DR-108`); spec line numbers are the 230-line spec's (+22 from old L46); live census, founders, tiers and extent per piece ST14, section 2.*"""

P_P10 = """*Piece ST16 (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`), beside this file, re-tests §13 B3's Planet and Element on the corrected wind account (AS16-23; marks DK16-1, DK16-3 and DK16-4); this file is not reworded (`DR-102`). Current fact (`DR-122`): the Element is Air, confirmed on re-test on its physics and on the open carriage of the protocol and the warnings, not on L426's Social Contract clause, which rests on the retired premise; its one-word label is still provisional; Wood reserved; the Planet is Neptune, provisional, decided within Mirny's own ULM, Uranus reserved; Saturn, the provisional Planet of §13 B3, was not confirmed on re-test; the Planet hold is lifted. RF-1's Neptune (L538) now rests on the taught, public knowledge and the wind known by what it lifts, not on the relay; RF-2's Wood (L539) now reaches the knowledge, not only the record. By these facts Q-91 (L575) is answered and PA-66 (L588) is overturned on its Planet half.*"""

P_S5 = """*Piece ST16 (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`), beside this file, re-tests the §10 backstop on the corrected wind account (AS16-23; marks DK16-2 and DK16-5 to DK16-7); this file is not reworded (`DR-102`). Current fact (`DR-122`): the Element is Air, confirmed on re-test on its physics and on the open carriage of the protocol and the warnings, its one-word label still provisional, Wood reserved; the Planet is Neptune, provisional, decided within Mirny's own ULM, Uranus reserved; Saturn was not confirmed on re-test; the Planet hold is lifted. Of §10's grounds for Saturn, the private reading is retired because the protocol is public (`DR-56`, `DR-57`), the fragments ground stood on the old composition frame and the station's run of operators, and the tilt is the planet's description, not one of its fields; the Element's Social Contract clause rests on the retired premise and was not counted. R-132 (L766) and C-6 (L301) are answered: rebuilt Earth was tested 2026-11-05 and does not fit. The word guard (L657) also covers the words contact, ring, winds, storm, warning and light: none of them is evidence for a symbol (AS16-15). The swap-test row for B3 (L709) is stale on both halves.*"""

P_SR = """*Superseded in part, as a proposal, by piece ST16 (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`, AS16-21), which re-tested all eight Elements and all eleven Planets on the corrected wind account with three readers; this file is not reworded (`DR-102`). Current fact (`DR-122`): the Element is Air, now confirmed, its one-word label still provisional, and Wood is reserved, as this review proposed; the Planet is Neptune, provisional, decided within Mirny's own ULM, Uranus reserved, Saturn not confirmed on re-test. Superseded here: Earth as the main alternative (rebuilt Earth does not fit), the Planet verdict, the proposed Planet cell, and a Planet test that read only two of the eleven.*"""

# (file name, recorded line count, recorded last line, pointer line)
TARGETS = [
    ("00.1_Step_MINUS-1_Input_Contract.md", 656,
     """| U-16 | The Megasheet folder count in PTI L281 / L406 ("3 files", four names) | A, C | B | Q-16 |""", P_ST12),
    ("00_Frame.md", 653,
     """7. **All three readers carried `RB` L1961's "Band 6" at first**; only A tested it against the census.""", P_ST12),
    ("01_Inherited.md", 49,
     """**Verdict:** ☑ step complete.""", P_ST12),
    ("02_Spine.md", 176,
     """L176) and were built from admitted text only.""", P_ST12),
    ("03_Research.md", 144,
     """of the nightless weeks · the web-search cap cut every reader short — each reader lists its unspent picks.""", P_ST12),
    ("04_Phase_03_Surface_and_Texture.md", 541,
     """| Type variance: Corridor and Network locus reach one feature each; Structure and Band 0 do not | A, B, C | all three |""", P_ST13),
    ("04_Phase_04_Ordinary_Life.md", 402,
     """| Spec L82 chars 423–500 drafted and killed | A, B, C, C2 | all |""", P_ST14),
    ("04_Phase_05_Relation_and_Geometry.md", 587,
     """| 5b deferred; three attempts not adopted | A, B, C | all three |""", P_ST14),
    ("04_Phase_10_Catalog.md", 629,
     """- *Round 3 prose slips not carried:* reader B's count of 34 admitted spec spans (the admitted range is 29 spans; 34 was its count of Read calls); reader C's quoted strings in its Zodiac cells (the Pre-Trip form rule takes bare pointers in lens cells — §12 was rewritten to pointers); reader A's stale reading-log counts (its PROOF blocks were correct).""", P_P10),
    ("05_Reconciliation.md", 840,
     """| Step-local numbers renumbered; sign names removed from citation tags | — | all | applied |""", P_S5),
    ("Symbol_Review_2026-10-13.md", 59,
     """- **Proposed registry edits (not applied):** Mirny's Element cell: Air (provisional); Planet cell: Saturn (provisional, contested by Neptune). Both are the developer's to change.""", P_SR),
]


def check(name, count, last, pointer):
    with open(os.path.join(M, name), "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    if "\r" in text:
        return name + ": carriage return present"
    if not text.endswith("\n"):
        return name + ": no final newline"
    lines = text[:-1].split("\n")
    if len(lines) != count:
        return "%s: %d lines, recorded %d" % (name, len(lines), count)
    if lines[-1] != last:
        return name + ": last line differs from the recorded one"
    if pointer in text:
        return name + ": pointer already present"
    return None


errors = [e for e in (check(*t) for t in TARGETS) if e]
if errors:
    print("ABORT, nothing written:")
    for e in errors:
        print("  " + e)
    sys.exit(1)

for name, count, last, pointer in TARGETS:
    path = os.path.join(M, name)
    with open(path, "rb") as f:
        before = f.read()
    addition = ("\n" + pointer + "\n").encode("utf-8")
    with open(path, "ab") as f:  # append only
        f.write(addition)
    with open(path, "rb") as f:
        after = f.read()
    if after != before + addition:
        print("STOP: " + name + " is not its old bytes plus the pointer; inspect it before anything else.")
        sys.exit(2)
    print("appended: %s (now %d lines)" % (name, count + 2))
```

## The eleven files

### 1 · `M/00.1_Step_MINUS-1_Input_Contract.md` (the input contract)

**Current last line, L656** (ends with a newline; the file ends inside a table):

```text
| U-16 | The Megasheet folder count in PTI L281 / L406 ("3 files", four names) | A, C | B | Q-16 |
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST12, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`); this file is not reworded (`DR-102`). Read its statements of no teacher, no inherited judgment, an unread cue or a private reading as the first generation's (Act 1); founders per the Founding Register (`Founding_Register.md` L57); live census and composition per the census (`Official_Population_Census.md` L500) and Mirny's spec (`Specs/Mirny subnet/Mirny.md` L20 to L22); the relay carries the weather warnings (`DR-76`); the extent at Census I is 140.35 km² at 10,000 per km² and 200.51 km² at 7,000 per km², computed from `Official_Population_Census.md` L500.*
```

**Source:** AS12-52, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L822 (the finding begins at L817); docket DK12-52 at L888; DEC-140.

**Changed:** only `REG`, `CEN` and `SPEC` are spelled out as file names, because none of the five files defines `REG` or `SPEC` and only the Frame defines `CEN`. Nothing in this text was settled by `DR-122` (DEC-141 and DEC-142 concern datasheets and research, not this line).

### 2 · `M/00_Frame.md` (the Frame)

**Current last line, L653** (ends with a newline; the file ends inside a numbered list):

```text
7. **All three readers carried `RB` L1961's "Band 6" at first**; only A tested it against the census.
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST12, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`); this file is not reworded (`DR-102`). Read its statements of no teacher, no inherited judgment, an unread cue or a private reading as the first generation's (Act 1); founders per the Founding Register (`Founding_Register.md` L57); live census and composition per the census (`Official_Population_Census.md` L500) and Mirny's spec (`Specs/Mirny subnet/Mirny.md` L20 to L22); the relay carries the weather warnings (`DR-76`); the extent at Census I is 140.35 km² at 10,000 per km² and 200.51 km² at 7,000 per km², computed from `Official_Population_Census.md` L500.*
```

**Source:** AS12-52, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L822; DK12-52 at L888; DEC-140.

**Changed:** as entry 1. The five files take one identical text (AS12-52: "the same in the five files").

### 3 · `M/01_Inherited.md` (Inherited)

**Current last line, L49** (ends with a newline; L48 is blank, so the file ends in a one-line paragraph):

```text
**Verdict:** ☑ step complete.
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST12, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`); this file is not reworded (`DR-102`). Read its statements of no teacher, no inherited judgment, an unread cue or a private reading as the first generation's (Act 1); founders per the Founding Register (`Founding_Register.md` L57); live census and composition per the census (`Official_Population_Census.md` L500) and Mirny's spec (`Specs/Mirny subnet/Mirny.md` L20 to L22); the relay carries the weather warnings (`DR-76`); the extent at Census I is 140.35 km² at 10,000 per km² and 200.51 km² at 7,000 per km², computed from `Official_Population_Census.md` L500.*
```

**Source:** AS12-52, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L822; DK12-52 at L888; DEC-140.

**Changed:** as entry 1.

### 4 · `M/02_Spine.md` (the Spine)

**Current last line, L176** (ends with a newline; the last line of a wrapped paragraph that begins at L173):

```text
L176) and were built from admitted text only.
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST12, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`); this file is not reworded (`DR-102`). Read its statements of no teacher, no inherited judgment, an unread cue or a private reading as the first generation's (Act 1); founders per the Founding Register (`Founding_Register.md` L57); live census and composition per the census (`Official_Population_Census.md` L500) and Mirny's spec (`Specs/Mirny subnet/Mirny.md` L20 to L22); the relay carries the weather warnings (`DR-76`); the extent at Census I is 140.35 km² at 10,000 per km² and 200.51 km² at 7,000 per km², computed from `Official_Population_Census.md` L500.*
```

**Source:** AS12-52, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L822; DK12-52 at L888; DEC-140.

**Changed:** as entry 1.

### 5 · `M/03_Research.md` (Research)

**Current last line, L144** (ends with a newline; the last line of a wrapped paragraph that begins at L142):

```text
of the nightless weeks · the web-search cap cut every reader short — each reader lists its unspent picks.
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST12, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md`); this file is not reworded (`DR-102`). Read its statements of no teacher, no inherited judgment, an unread cue or a private reading as the first generation's (Act 1); founders per the Founding Register (`Founding_Register.md` L57); live census and composition per the census (`Official_Population_Census.md` L500) and Mirny's spec (`Specs/Mirny subnet/Mirny.md` L20 to L22); the relay carries the weather warnings (`DR-76`); the extent at Census I is 140.35 km² at 10,000 per km² and 200.51 km² at 7,000 per km², computed from `Official_Population_Census.md` L500.*
```

**Source:** AS12-52, `Amendment_Rederivation_ST12_EarlySteps_2026-11-05.md` L822; DK12-52 at L888; DEC-140.

**Changed:** as entry 1.

### 6 · `M/04_Phase_03_Surface_and_Texture.md` (Phase 3)

**Current last line, L541** (ends with a newline; the file ends inside a table):

```text
| Type variance: Corridor and Network locus reach one feature each; Structure and Band 0 do not | A, B, C | all three |
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST13, `Amendment_Rederivation_ST13_Phase3_2026-11-05.md`); this file is not reworded (`DR-102`). The weather warnings travel on the relay (`DR-76`). Read its statements of unread or unlearned cues, a reader that does not exist, blame or carelessness as the first generation's (Act 1) and the not-yet-taught's; warning in this file names the wind's own first sign, and the word keeps both uses, this one and the weather warning on the relay, with context deciding (`DR-122`); spec line numbers are the 230-line spec's (+22 from old L46); live census, founders and extent per piece ST13, section 2.*
```

**Source:** AS13-33, `Amendment_Rederivation_ST13_Phase3_2026-11-05.md` L462 (the finding begins at L457); DK13-33 at L504; DEC-160.

**Changed:** "warning in this file means the physical onset" now follows DEC-162 (keep both uses; context decides). The file's own uses (L168, L387, L417, L521; AS13-14) are the first sign, so that is still stated. DEC-161 (no label) changes AS13-25's addendum in the piece, not this line, which names no role.

### 7 · `M/04_Phase_04_Ordinary_Life.md` (Phase 4)

**Current last line, L402** (ends with a newline; the file ends inside a table):

```text
| Spec L82 chars 423–500 drafted and killed | A, B, C, C2 | all |
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST14, `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md`); this file is not reworded (`DR-102`). The weather warnings travel on the relay (`DR-76`). Read its statements of unread cues, no teacher, no public wind call, blame or carelessness, and a relay restored by position or kept invisibly, as the first generation's (Act 1) and the not-yet-taught's; warning in Phase 4 at L122 and L269 names the wind's own first sign, and the word keeps both uses, that one and the weather warning on the relay, with context deciding (`DR-122`); the lived middle is deferred to the cultural synthesis pass (CST, `DR-108`); spec line numbers are the 230-line spec's (+22 from old L46); live census, founders, tiers and extent per piece ST14, section 2.*
```

**Source:** AS14-54, `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L721 (the finding begins at L716); DK14-54 at L784; DEC-180.

**Changed:** the warning clause now follows DEC-162. Phase 4 has both uses (L122 and L269 are the first sign; L246's early warning is the relay's), so context decides. "the CST" is spelled out once, because Phase 4 never names it. DEC-181 (keep four) needs nothing here: Band 5's four common items stand as written.

### 8 · `M/04_Phase_05_Relation_and_Geometry.md` (Phase 5)

**Current last line, L587** (ends with a newline; the file ends inside a table):

```text
| 5b deferred; three attempts not adopted | A, B, C | all three |
```

**Line to append** (after one blank line):

```text
*Addenda proposed 2026-11-05 beside this file (piece ST14, `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md`); this file is not reworded (`DR-102`). The weather warnings travel on the relay (`DR-76`). Read its statements of unread cues, no teacher, no public wind call, blame or carelessness, and a relay restored by position or kept invisibly, as the first generation's (Act 1) and the not-yet-taught's; warning in Phase 4 at L122 and L269 names the wind's own first sign, and the word keeps both uses, that one and the weather warning on the relay, with context deciding (`DR-122`); the lived middle is deferred to the cultural synthesis pass (CST, `DR-108`); spec line numbers are the 230-line spec's (+22 from old L46); live census, founders, tiers and extent per piece ST14, section 2.*
```

**Source:** AS14-54, `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L721; DK14-54 at L784; DEC-180.

**Changed:** as entry 7, with an identical text because one text was approved for both phases. Phase 5 never uses the word warning, so that clause has no effect here (note 6).

### 9 · `M/04_Phase_10_Catalog.md` (Phase 10)

**Current last line, L629** (ends with a newline; the file ends inside a list):

```text
- *Round 3 prose slips not carried:* reader B's count of 34 admitted spec spans (the admitted range is 29 spans; 34 was its count of Read calls); reader C's quoted strings in its Zodiac cells (the Pre-Trip form rule takes bare pointers in lens cells — §12 was rewritten to pointers); reader A's stale reading-log counts (its PROOF blocks were correct).
```

**Line to append** (after one blank line):

```text
*Piece ST16 (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`), beside this file, re-tests §13 B3's Planet and Element on the corrected wind account (AS16-23; marks DK16-1, DK16-3 and DK16-4); this file is not reworded (`DR-102`). Current fact (`DR-122`): the Element is Air, confirmed on re-test on its physics and on the open carriage of the protocol and the warnings, not on L426's Social Contract clause, which rests on the retired premise; its one-word label is still provisional; Wood reserved; the Planet is Neptune, provisional, decided within Mirny's own ULM, Uranus reserved; Saturn, the provisional Planet of §13 B3, was not confirmed on re-test; the Planet hold is lifted. RF-1's Neptune (L538) now rests on the taught, public knowledge and the wind known by what it lifts, not on the relay; RF-2's Wood (L539) now reaches the knowledge, not only the record. By these facts Q-91 (L575) is answered and PA-66 (L588) is overturned on its Planet half.*
```

**Source:** AS16-23, `Amendment_Rederivation_ST16_Symbols_2026-11-05.md` L368 (its Phase 10 addendum is at L369 to L374); DK16-1 L404, DK16-3 L406, DK16-4 L407 (section 8); DEC-203.

**Changed:** the piece's addendum and DK16-1 said the Planet was held, with Saturn provisional and Neptune contested, and the hold blocking "complete". DK16-4 said "Element re-tested (Air)". These now read as `DR-122` decided: Air confirmed and Wood reserved, Neptune provisional and Uranus reserved, Saturn not confirmed, the hold lifted. The three marks are condensed into one line. The Phase 10 piece's own status marks of 2026-11-04 are not repeated (ST16 section 8).

### 10 · `M/05_Reconciliation.md` (Step 5)

**Current last line, L840** (ends with a newline; the file ends inside a table):

```text
| Step-local numbers renumbered; sign names removed from citation tags | — | all | applied |
```

**Line to append** (after one blank line):

```text
*Piece ST16 (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`), beside this file, re-tests the §10 backstop on the corrected wind account (AS16-23; marks DK16-2 and DK16-5 to DK16-7); this file is not reworded (`DR-102`). Current fact (`DR-122`): the Element is Air, confirmed on re-test on its physics and on the open carriage of the protocol and the warnings, its one-word label still provisional, Wood reserved; the Planet is Neptune, provisional, decided within Mirny's own ULM, Uranus reserved; Saturn was not confirmed on re-test; the Planet hold is lifted. Of §10's grounds for Saturn, the private reading is retired because the protocol is public (`DR-56`, `DR-57`), the fragments ground stood on the old composition frame and the station's run of operators, and the tilt is the planet's description, not one of its fields; the Element's Social Contract clause rests on the retired premise and was not counted. R-132 (L766) and C-6 (L301) are answered: rebuilt Earth was tested 2026-11-05 and does not fit. The word guard (L657) also covers the words contact, ring, winds, storm, warning and light: none of them is evidence for a symbol (AS16-15). The swap-test row for B3 (L709) is stale on both halves.*
```

**Source:** AS16-23, `Amendment_Rederivation_ST16_Symbols_2026-11-05.md` L368 (its Step 5 addendum is at L376 to L380); DK16-2 L405, DK16-5 L408, DK16-6 L409, DK16-7 L410 (section 8); DEC-203.

**Changed:** the addendum's "Re-test (ST16): Saturn not confirmed; the Planet held by the developer" now gives the decided Planet and the lifted hold. Its Element line, which stood as Air, now says confirmed (DEC-201). DK16-7's "Element accepted" now reads confirmed. DK16-2 is carried here, where its lines are (note 1). The word list is unquoted, to add no new quotation.

### 11 · `M/Symbol_Review_2026-10-13.md` (the symbol review of 2026-10-13)

**Current last line, L59** (ends with a newline; the file ends inside a list):

```text
- **Proposed registry edits (not applied):** Mirny's Element cell: Air (provisional); Planet cell: Saturn (provisional, contested by Neptune). Both are the developer's to change.
```

**Line to append** (after one blank line):

```text
*Superseded in part, as a proposal, by piece ST16 (`Amendment_Rederivation_ST16_Symbols_2026-11-05.md`, AS16-21), which re-tested all eight Elements and all eleven Planets on the corrected wind account with three readers; this file is not reworded (`DR-102`). Current fact (`DR-122`): the Element is Air, now confirmed, its one-word label still provisional, and Wood is reserved, as this review proposed; the Planet is Neptune, provisional, decided within Mirny's own ULM, Uranus reserved, Saturn not confirmed on re-test. Superseded here: Earth as the main alternative (rebuilt Earth does not fit), the Planet verdict, the proposed Planet cell, and a Planet test that read only two of the eleven.*
```

**Source:** DK16-10, `Amendment_Rederivation_ST16_Symbols_2026-11-05.md` L413; AS16-21 at L325 to L355; DEC-203.

**Changed:** DK16-10's mark ("Superseded in part as a proposal by piece ST16: Earth as second, the Planet verdict and cell, coverage") is written out in full. It now gives the decided fact (`DR-122`): the review's "leave open" Planet verdict and its proposed Saturn cell are superseded by Neptune, provisional. The review's Air and Wood conclusions stand, Air now confirmed. Only the Planet cell is named as superseded, as in DK16-10, because the review's Element cell (Air) still names the right member.
