# Pre-Contamination Review — CASEY

**Location:** Casey · **Parent:** Mirny subnet · **Type:** Settlement · **Frame:** Second Interwar, pre-war
**Built:** 2026-09-02, during Run 12's remediation · **Mechanism:** `../00_RUNBOOK.md` §C.4
**Readers:** 3 (A, B, C), dispatched 2026-09-02, all reported · **Rule:** `ADMISSIBLE` requires 3–0

# ⚠ Status: **DRAFT** — vectors closed, map built, **escalation ladder not yet worked**

> ## ⭐ BEFORE BUILDING THIS REVIEW'S REGISTRY SCOPE — read this. **Added 2026-09-03.**
> **This review has not yet had its registry enumerated or its scope pin taken.** ***That is fortunate: the
> enumeration everyone used before today was INCOMPLETE, and building it now means building it right.***
>
> ### The corrected root list is **`§B · §C · §C.1 · §C.6 · §C.7 · §C.9 · §D`**
> **`§C.7` (symbol systems) and `§C.9` (the real-world research register — ~90 files across nine subfolders)
> were added 2026-09-03.** ***Both existed; neither was named in `Step −2`, `§C.4` requirement 6, or Brief B's
> `STEP 1`, so no scout before today swept them.*** **Shirayuki's review recorded "34 of 34 roots, no
> omissions" and was demoted the same day for exactly this.**
>
> ⚠ **`§C.9` is ALIAS-KEYED.** `Climate Data/READER/` names its 37 files for the **real-world station**, never
> the Tepenian city. ***A sweep on the city name alone returns a confident false negative.***
>
> 📁 **And three reference files now exist beside the runbook**, registered in its "Where everything lives"
> table: **`ULM_Input_Required_Reference.md`** · **`ULM_Input_Available_Audit.md`** ·
> **`Location_Data-Input_To-Do.md`**. **Intended `ADMISSIBLE`, but map them first — `05` §6.1d: no file is
> safe by category.**

> ### ⛔ AND A SECOND, INDEPENDENT GAP — added 2026-09-03 from Run 14 *(M-112)*
>
> **This review is scoped to a FILE LIST, like every review in this folder.** ***A `CONFIRMED`, pinned,
> 3-of-3 review on another subject was honored perfectly and still leaked, because the registry points at
> sources no review had mapped.*** **Assume the same is true here: closing the escalation ladder would make
> this review `CONFIRMED` under the OLD five requirements, and it would still be incomplete.**
>
> **Before this is ever `CONFIRMED`, discharge `§C.4` requirement 6 as well** — dispatch **Brief B**
> *(`Test_Runs/COLD_RUN_CHECKLIST.md`)*: enumerate the registry, take the **scope pin** and the **inventory
> pin**, and tier every source `MAPPED` · `WITHHELD` · `QUERYABLE-BY-SCHEMA`.
>
> **⚠ And note Casey's own §C.6 exposure is likely LARGER than the other subject's** — Casey carries a
> `Course_of_Events/` folder whose **filenames are theses** (M-88), which a registry sweep must count without
> listing.

**All four `Step −2` vectors are swept and closed. All three readers reported and the 3-of-3 verdict is
computed below.** ***What blocks `CONFIRMED` is `§C.2` requirement 3: every non-unanimous range must be run
down the escalation ladder or explicitly accepted as `WITHHELD`.*** **188 lines are split and unworked.**

> **A run may proceed against this map as it stands — the `ADMISSIBLE` set is already 3–0 unanimous and safe.
> It will simply be THINNER than it needs to be.** **Working the ladder is a yield recovery, not a safety
> requirement.**

> ## ✅ THIS FILE IS SAFE FOR A COLD DERIVER TO READ IN FULL.
>
> **Coordinates, tags and status only. No headings, no quotes, no summaries, no adjectives about Casey.**
> ***That property is the entire point of the artifact and must be protected absolutely*** *(M-85; M-97;
> and `06`'s own "what this reveals about X" column, the same defect built into a manifest schema)*.

---

# 1. The four-vector sweep — `Step −2`

| # | Vector | Status | Evidence |
|---|---|---|---|
| **1** | **Required reading** | ✅ **SWEPT AND FIXED** | `grep -n "Casey"` across `00`–`06`. **Two live leaks, both un-manifested**: `00_RUNBOOK.md` §C.2's return-contract example *(**neutralized**)* and `01_Frame_Typology_and_Inheritance.md` **line 65** *(**retained deliberately** — see §4)*. §C.3's mentions are anecdote-only. **Manifested in `06`.** |
| **2** | **Auto-loaded memory** | ✅ **SWEPT AND BANDED** | `grep -ril casey`. **Three entries carried conclusion-tier content**, banded in place via `§3d` (locate by grep → patch by asserted script → verify by grep): `project_casey_recheck.md` · `project_casey_bug_check_resolved.md` · `project_pink_lucy_migration_resolved.md`. **Re-verify with `grep -ril`, never `-rin`** (M-91). |
| **3** | **File tree** | ✅ **SWEPT AND SANITIZED** | See §3. **One folder must never be listed.** |
| **4** | **Union / compositional** | ✅ **CLEAR for a new session** | Vectors 1–3 were individually marginal and **jointly reconstructed Casey's spine** for Run 12 (M-89). **For a session that has read none of them the union is empty** — the fixes above are what make that true. **Keep an exposure ledger anyway and review it as a SET before Phase 0.** |

---

# 2. ⛔ The pin — REVERIFY BEFORE REUSING. Do not assume.

**A coordinate map is line-anchored: one inserted line above a range shifts every range below it, silently,
and points a deriver into withheld content.** **Verify with the script in `../00_RUNBOOK.md` §C.4.**

```
Worldspace/.../Cities/Specs/Casey.md|feade7fce857ca75|191
Worldspace/.../Cities/Local_Cultures/Mirny_Subnet/Casey.md|c43b8875c06c49d8|292
Worldspace/.../Cities/City_Megasheets/Mirny_Subnet/Casey/Casey_Physical_Infrastructure_Attributes.md|161ab6535711a842|166
```

*(`sha256` first 16 chars · paths under `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/`. Pinned 2026-09-02.)*
**On a `STALE` row: re-tag only the file that moved. Do not rebuild the review.**

---

# 3. Sanitized file tree — ⛔ NEVER `ls` THE FOLDER IN THE MARKED ROW

**M-88: a filename is a section heading.** **Addressable by index without seeing a title.**

| Path | Contents | Safe to list? |
|---|---|---|
| `Cities/Specs/Casey.md` | 191 lines | ✅ |
| `Cities/Local_Cultures/Mirny_Subnet/Casey.md` | 292 lines | ✅ |
| `Cities/City_Megasheets/Mirny_Subnet/Casey/` | 6 files, 35–232 lines | ✅ template-named |
| `Cities/City_Enneagram_Personalities/Mirny_Subnet/Casey.md` | 15 lines | ✅ *(⛔ quarantined content)* |
| `Cities/City_Vision_Notes/Casey.md` | 26 lines | ✅ *(⛔ quarantined content)* |
| `Cities/Local_Robot_Culture/Mirny_Subnet/Casey.md` | 289 lines | ✅ *(⛔ quarantined content)* |
| `Neo-Races-and-Cultures/Mirny_Subnet/Casey/` | 1 file, 636 lines | ✅ template-named |
| `Reference/Real-World/Climate Data/READER/Casey.md` | 16 lines | ✅ **G7** |
| **`Background-Lore/Cities/Mirny_Subnet/Casey/Course_of_Events/`** | **11 files, 91–143 lines each** | ⛔⛔ **NO. Address by index: `Casey_01` … `Casey_11`** |
| `Background-Lore/Cities/Mirny_Subnet/Casey/` *(top level)* | 2 files, 143 and 674 lines | ⚠ **Address by line count** |

---

# 4. Required-reading skip list

| File | Coordinate | Action |
|---|--:|---|
| `01_Frame_Typology_and_Inheritance.md` | **line 65** | ⚠ **SKIP THIS LINE.** Retained deliberately; **pending developer ruling on genericizing** |
| `00_RUNBOOK.md` | §C.2 | ✅ **Neutralized 2026-09-02** |
| `06_Worked_Example_Provenance.md` | Casey entry | ✅ **Safe** — coordinates-only |
| `Test_Runs/Casey_ColdRun_Prep_2026-09-02.md` | all | ✅ **Safe — audited after Run 12, leaked nothing** |

---

# 5. ⭐ THE COORDINATE MAP — 3-of-3 unanimity applied

## 5a. The withheld-rate — a statistic about the CORPUS, not about the run (`§C.2` step 4)

> ### ⚠ CORRECTED 2026-09-03 (M-101 defect 3). **The first published version of this table counted blank
> lines, horizontal rules and table separators in its denominator.** ***A blank line is not attribute surface
> that has been withheld — it is not attribute surface.*** **287 of 649 lines were inert.** Both columns are
> shown, because the raw figures were published and a silent fix would hide the error.

| File | Lines | Content lines | **ADMISSIBLE — corrected** | *(raw, as first published)* |
|---|--:|--:|--:|--:|
| `Specs/Casey.md` | 191 | 113 | **85.0%** | *82.7%* |
| `Casey_Physical_Infrastructure_Attributes.md` | 166 | 119 | **43.7%** | *45.2%* |
| `Local_Cultures/Mirny_Subnet/Casey.md` | 292 | 130 | **31.5%** | *30.5%* |
| **TOTAL** | **649** | **362** | **52.2% adm · 47.8% WITHHELD** | *49.6% / 50.4%* |

**Split/unanimous breakdown of the withheld portion** *(raw line basis, uncorrected)*: `Specs` 5.2% unanimous
/ 12.0% split · `Attributes` 32.5% / 22.3% · `Local_Cultures` 25.7% / **43.8%** · total 22.3% / **28.0%**.

> ### ⭐⭐ **ROUGHLY HALF OF CASEY'S CONTENT-BEARING SURFACE IS CONCLUSION-TIER.**
> **`§C.2` step 4 is explicit that this is a finding about the SOURCES, not about the run:** *"the files are
> badly mixed and want real upstream splits per `§C.1`."* ***First time this statistic has been measured on
> any location in this project.***
>
> **⭐ And the finding SURVIVED its own correction** — 47.8% where 50.4% was claimed — **because the inert
> lines fell across admissible and withheld regions at similar rates rather than clustering.** ***The method
> was wrong and the conclusion was robust; both halves are recorded, because compressing this into either
> "it was fine" or "it was wrong" loses the lesson.***

**The stratification tracks the tier ordering exactly, which is itself a validation:** **`Specs/` is the
cleanest tier (82.7% admissible), the "attributes" megasheet sits in the middle (45.2%), and the completed
culture sheet is the dirtiest (30.5%).** **The prep document's §3 warning that
`Casey_Physical_Infrastructure_Attributes.md` is *the trap by name* is confirmed — a file whose title
promises attributes is 54.8% conclusions.**

## 5b. ⚠⚠ THE HONEST CAVEAT — the readers ran under THREE DIFFERENT CONTRACTS

***This is the measured cost of M-93, and it must be read before the split numbers are trusted.***

**A mid-flight amendment (character-spans + path sanitization) was sent to all three readers.** **They
diverged:**

| Reader | Response to the amendment | Grain returned |
|---|---|---|
| **A** | Did not apply it | Line |
| **B** | **Adopted it** | **Character-span** |
| **C** | **Refused it as a suspected prompt injection** (M-93 — correct behavior) | Line |

**B's character-spans were collapsed CONSERVATIVELY for comparison — any line with a withheld portion became
a fully withheld line.** ***That collapse inflates B's withheld count, and therefore inflates the SPLIT rate
wherever B is the dissenter.***

> ### ***A unanimity rule applied across non-identical contracts is weaker than it looks.*** **Some part of
> the 28% split rate is an artifact of comparing char-grain against line-grain, not genuine disagreement.**
> **This is the strongest possible argument for `§C.2`'s new rule that the brief is FINAL at dispatch and a
> changed contract means KILL AND RE-DISPATCH.**

**How much is artifact:** **on `Local_Cultures`, B withheld several large blocks outright that A and C read
as alternating — that is substantive disagreement about the file's tier, not a grain artifact.** **On the
smaller mid-line disputes it is likely mostly artifact.** ***The two cannot be separated without a re-run
under one contract, and this review does not claim to have separated them.***

**⭐ And one substantive observation that survives the caveat:** **B's read of `Local_Cultures` — mostly
conclusion-tier, with narrow admissible windows — is much closer to the prep document's own §4.2 by-rule
default than A's or C's are.** **Two independent methods agreeing is worth more than either alone.**

## 5c. The 3–0 ADMISSIBLE sets — safe to open

**`Specs/Casey.md`** *(82.7%)*
`1-6, 8-96, 103-116, 130-141, 143, 145-151, 153-168, 171-172, 181-191`

**`Casey_Physical_Infrastructure_Attributes.md`** *(45.2%)*
`1-12, 24-27, 30-55, 61-74, 80-87, 92-96, 161-166`

**`Local_Cultures/Mirny_Subnet/Casey.md`** *(30.5%)*
`1-12, 16-33, 45-48, 94-100, 105-108, 113-116, 152-165, 215-218, 260-267, 269, 271-277, 280-284, 286`

## 5d. The unanimous-WITHHELD sets — ⛔ do not open, and no ladder will recover them

**`Specs`:** `101-102, 122-128, 178`
**`Attributes`:** `106-159`
**`Local_Cultures`:** `14, 39, 42-43, 49-51, 57, 69-77, 82-87, 92-93, 101-103, 109, 117-120, 125-126, 131-134,
139-142, 147-150, 171-172, 177-178, 183-186, 191-192, 197-198, 207-208, 213, 222-223, 228-229, 234-237,
252-253, 258, 285, 292`

## 5e. ⚠ The SPLIT set — the escalation ladder's work, and what blocks `CONFIRMED`

**188 lines. Currently `WITHHELD` by the asymmetric rule, correctly.** **Work `§C.2`'s ladder on these to
recover yield: re-split finer → check generator agreement → closed-schema extraction → withhold and record.**

**`Specs` (23):** `7, 97-100, 117-121, 129, 142, 144, 152, 169-170, 173-177, 179-180`
**`Attributes` (37):** `13-23, 28-29, 56-60, 75-79, 88-91, 97-105, 160`
**`Local_Cultures` (128):** `13, 15, 34-38, 40-41, 44, 52-56, 58-68, 78-81, 88-91, 104, 110-112, 121-124,
127-130, 135-138, 143-146, 151, 166-170, 173-176, 179-182, 187-190, 193-196, 199-206, 209-212, 214, 219-221,
224-227, 230-233, 238-251, 254-257, 259, 268, 270, 278-279, 287-291`

> **⭐ Ladder step 2 is the cheap win and should be run first.** **Where all three readers agree on the
> GENERATOR but split on admissibility, the dispute is about PHRASING, not content — and a finer re-split
> usually turns one disputed range into two undisputed ones.** **The generator tags needed for this are
> already collected in the readers' returns.**

## 5f. Tier 3 handles — `Worldspace/Characters/`

**Two Casey-referencing character files. Reader B sanitized these correctly; A and C returned person-named
paths (M-94).** **Addressed here by index:**

| Index | Path shape | Lines |
|---|---|--:|
| **CH-1** | `Characters/Dolls/Still-Present_-_In-Game/recruitable/[folder A]/README.md` | 80 |
| **CH-2** | `Characters/Dolls/Still-Present_-_In-Game/recruitable/[folder B]/README.md` | 161 |

**⚠ Both are MIXED. Route through `§C.2` before opening.** **Interrogate BACKWARD per prep §5** — *"what must
be true of this place for X to have become who X is?"* — **never forward from a roster entry.**

---

# 6. What this review can and cannot prove

**CAN:** that vectors 1–4 were live for Casey on 2026-09-02 and are now closed for a session that has not
already read them · that all three mapped files are genuinely mixed, none openable whole · **that the
project's completed culture sheets and "attributes" megasheets are roughly half conclusion-tier by line**,
which is a corpus finding with implications well beyond Casey.

**CANNOT:** clear anyone to derive at full yield — **`Status: DRAFT`, 188 lines unworked.** · **Separate
genuine reader disagreement from the grain artifact introduced by the contract divergence (§5b)** ·
**Verify its own accuracy.** `§C.2`'s standing warning holds: a map's correctness is load-bearing and
unverifiable by its consumer, **which is exactly why `CONFIRMED` demands 3–0 and an attribution trail.**
