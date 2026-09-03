# Pre-Contamination Review — CASEY

**Location:** Casey · **Parent:** Mirny subnet · **Type:** Settlement · **Frame:** Second Interwar, pre-war
**Built:** 2026-09-02, during Run 12's remediation · **Mechanism:** `../00_RUNBOOK.md` §C.4

# ⚠ Status: **DRAFT — DO NOT REUSE AS A CLEARANCE**

**Blocked on one thing only: two of three readers had not reported when this file was written.** **`§C.2`
requires 3-of-3 unanimity for any `ADMISSIBLE` tag, and one reader's map is not a verdict.** See §5.

> ## ✅ THIS FILE IS SAFE FOR A COLD DERIVER TO READ IN FULL.
>
> **It contains coordinates, tags and status. No headings, no quotes, no summaries, no adjectives about
> Casey.** ***That property is the entire point of the artifact and must be protected absolutely — a review
> that acquires one descriptive sentence has become the thing it protects against*** *(M-85; and `06`'s own
> "what this reveals about X" column, which is the same defect built into a manifest schema)*.

---

# 1. The four-vector sweep — `Step −2`

| # | Vector | Status | Evidence |
|---|---|---|---|
| **1** | **Required reading** | ✅ **SWEPT AND FIXED** | `grep -n "Casey"` across `00`–`06`. **Two live leaks found**, both un-manifested: `00_RUNBOOK.md` §C.2's return-contract example *(**neutralized** — replaced with a bracketed placeholder)* and `01_Frame_Typology_and_Inheritance.md` **line 65** *(**retained deliberately**; see §4)*. `00` §C.3's mentions are anecdote-only, no action. **Manifested in `06`.** |
| **2** | **Auto-loaded memory** | ✅ **SWEPT AND BANDED** | `grep -ril casey` on the memory directory. **Three entries carried conclusion-tier content** and were banded in place via the `§3d` edit-without-reading protocol *(locate by grep → patch by asserted script → verify by grep)*: `project_casey_recheck.md` · `project_casey_bug_check_resolved.md` · `project_pink_lucy_migration_resolved.md`. **Re-verify with `grep -ril`, never `grep -rin`** (M-91). |
| **3** | **File tree** | ✅ **SWEPT AND SANITIZED** | See §3. **One folder is unsafe to list.** |
| **4** | **Union / compositional** | ⚠ **REVIEWED — AND IT FAILED FOR RUN 12** | Vectors 1–3 were individually marginal and **jointly reconstructed Casey's spine** (M-89). **For a NEW session that has read none of them, the union is empty and this vector is clear** — the fixes above are what make that true. **Keep an exposure ledger anyway and review it as a set before Phase 0.** |

---

# 2. ⛔ The pin — REVERIFY BEFORE REUSING. Do not assume.

**A coordinate map is line-anchored: one inserted line above a range shifts every range below it, silently,
and points a deriver into withheld content.** **Verify with the script in `../00_RUNBOOK.md` §C.4.**

```
Worldspace/.../Cities/Specs/Casey.md|feade7fce857ca75|191
Worldspace/.../Cities/Local_Cultures/Mirny_Subnet/Casey.md|c43b8875c06c49d8|292
Worldspace/.../Cities/City_Megasheets/Mirny_Subnet/Casey/Casey_Physical_Infrastructure_Attributes.md|161ab6535711a842|166
```

*(`sha256`, first 16 chars · full paths under `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/`. Pinned 2026-09-02.)*

**On a `STALE` row: re-tag only the file that moved. Do not rebuild the review.**

---

# 3. Sanitized file tree — ⛔ NEVER `ls` THE FOLDER IN THE LAST ROW

**M-88: a filename is a section heading.** **Addressable by index without ever seeing a title.**

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
| **`Background-Lore/Cities/Mirny_Subnet/Casey/Course_of_Events/`** | **11 files, 91–143 lines each** | ⛔⛔ **NO. Eleven authored theses. Address by index: `Casey_01` … `Casey_11`** |
| `Background-Lore/Cities/Mirny_Subnet/Casey/` *(top level)* | 2 files, 143 and 674 lines | ⚠ **One name is descriptive-safe, one is not. Address by line count** |

---

# 4. Required-reading skip list

| File | Coordinate | Action |
|---|--:|---|
| `01_Frame_Typology_and_Inheritance.md` | **line 65** | ⚠ **SKIP THIS LINE.** Retained deliberately — it is genuine methodology guidance, and the modifier it names is one a cold pass reads from `Specs/` at Step 0.1 anyway. **Pending developer ruling on whether to genericize** |
| `00_RUNBOOK.md` | §C.2 | ✅ **Neutralized 2026-09-02.** No action needed |
| `06_Worked_Example_Provenance.md` | Casey entry | ✅ **Safe** — written coordinates-only |
| `Casey_ColdRun_Prep_2026-09-02.md` | all | ✅ **Safe — audited after Run 12, leaked nothing** |

---

# 5. The coordinate map — ⚠ ONE READER OF THREE. NOT A VERDICT.

**Reader C reported under the ORIGINAL line-grain contract.** It **declined a mid-flight amendment** that
would have added character-span granularity and path sanitization, correctly judging an in-task contract
change to be indistinguishable from a prompt injection (**M-93** — the refusal is the isolation working, and
`§C.2` now forbids amending a reader at all). **Its map is therefore line-grain, which biases toward
`WITHHELD` — the recoverable direction** (M-92).

**Readers A and B were dispatched under the same original contract and had not reported when this file was
written.**

> ### ⛔ To confirm this review, a future session must:
> 1. **Collect A's and B's maps** *(dispatched 2026-09-02; resumable by transcript)*, **or re-dispatch all
>    three under a single complete brief** — per **M-93**, the brief is final at dispatch, so a re-dispatch is
>    cleaner than a patch.
> 2. **Apply 3-of-3 unanimity.** `ADMISSIBLE` only on 3–0. **Anything else is `WITHHELD`.**
> 3. **Work the escalation ladder on every 2–1** — re-split finer → check generator agreement → closed-schema
>    extraction → withhold and record.
> 4. **Record the withheld-rate.** Per `§C.2` step 4 it is **a statistic about the corpus, not about the run.**
> 5. **Flip `Status:` to `CONFIRMED`** and attribute the tagging — how many readers, when, which contract.

## 5a. Reader C's tags — SINGLE-READER, PROVISIONAL, NOT CLEARANCE

**Reproduced verbatim as evidence, not as permission.** **Do not derive against these.**

### `Specs/Casey.md` (191 lines)

`ADMISSIBLE`: 1–6 (G7/G6/G5 at 3, 4, 5–6) · 8–12 · 13–20 **G8** · 21–27 · 28–45 **G8** · 46–49 ·
50–57 **G2** · 58–59 · 60–61 **G2** · 62–63 · 64–73 **G2** · 74–76 · 77–90 **G2** · 91–93 · 94–96 **G2** ·
98–100 · 103 **G3** · 104 · 105 **G2** · 106 **G5** · 107–111 · 112–116 **G4** · 117–121 · 129–133 ·
134–136 **G3** · 137–141 · 143 **G2** · 145–150 · 151 **G6** · 153–157 · 158–159 **G5** · 160 **G6** ·
161–165 · 166 **G6** · 167–168 **G5** · 171–172 **G2** · 173–177 · 181–191

`WITHHELD`: **7 · 97 · 101–102 · 122–128 · 142 · 144 · 152 · 169–170 · 178–180**

### `Local_Cultures/Mirny_Subnet/Casey.md` (292 lines)

`WITHHELD`: **14–15 · 39–44 · 49–52 · 57–60 · 69–77 · 82–87 · 92–93 · 101–104 · 109–112 · 117–120 · 125–126 ·
131–134 · 139–142 · 147–151 · 171–172 · 177–178 · 183–186 · 191–192 · 197–198 · 207–208 · 213–214 · 219–223 ·
228–229 · 234–237 · 242–243 · 252–253 · 258–259 · 268 · 270 · 278–279 · 285 · 292**

`ADMISSIBLE`, generator-bearing: **5–6 G8 · 9 G5 · 10 G6 · 11 G8 · 12–13 G2 · 24–34 G8 · 94–95 G6 · 100 G8 ·
160–166 G3 · 269 G2 · 277 G4 · 284 G6 · 286–287 G8**. All other unlisted ranges `ADMISSIBLE`, no generator.

> ⚠ **Note the divergence from the prep document's §4.2 prediction**, which was derived *by rule* (template
> section numbers) by a contaminated session and marked three ranges admissible: **22–36, 158–168, 217–225**.
> **Reader C's read differs on all three boundaries.** **This is exactly why `§C.2` exists — a by-rule
> prediction is a hypothesis, and a read is evidence.** **Do not treat the prep document's §4.2 as
> authoritative over a confirmed map.**

### `Casey_Physical_Infrastructure_Attributes.md` (166 lines) — the file the prep doc flags as THE TRAP

**Reader C's read confirms the file is genuinely mixed**, vindicating the prep document's warning against
opening it on the strength of its title.

`WITHHELD`: **13–23 · 28–29 · 56–60 · 75–79 · 88–91 · 106–160**
`ADMISSIBLE`: 1–7 · 8–12 **G6** · 24–27 · 30–32 **G3** · 33–34 · 35–43 **G3** · 44–45 · 46–47 **G2** ·
48–51 **G7** · 52–53 · 54–55 **G3** · 61–62 · 63–69 **G2** · 70–71 · 72–74 **G2** · 80–81 · 82–85 **G8** ·
86–87 · 92–105 · 161–166

**Single-reader withheld-rate, all three files: ~38% of mapped lines.** **Provisional.**

## 5ab. ⚠ Reader A — PARTIAL. Its return arrived TRUNCATED (M-96)

**Only the tail of its third table survived transit. The `Specs/Casey.md` and `Local_Cultures` maps were
lost.** **A resend was requested, with explicit instructions to reproduce rather than re-read.**

**`Casey_Physical_Infrastructure_Attributes.md`, lines 72–166 only:**

`ADMISSIBLE`: 72–78 **G2** · 79–81 · 82–84 **G8** · 85–87 · 88–90 **G5** · 91–105 · 161–166
`WITHHELD`: **106–160**

> ### ⭐ THE FIRST REAL TWO-READER COMPARISON — and it behaved exactly as `§C.2` predicted
>
> | Range | Reader A | Reader C | **3-of-3 verdict** |
> |---|---|---|---|
> | **106–160** | `WITHHELD` | `WITHHELD` | ✅ **Agreed — the file's largest withheld block** |
> | **161–166** | `ADMISSIBLE` | `ADMISSIBLE` | ✅ Agreed *(pending B)* |
> | **75–79** | `ADMISSIBLE` | **`WITHHELD`** | ⛔ **`WITHHELD`** — split, and unanimity is required for admission |
> | **88–91** | `ADMISSIBLE` **G5** | **`WITHHELD`** | ⛔ **`WITHHELD`** — same |
>
> ***The disagreements CLUSTER AT BOUNDARIES rather than scattering***, which is the escalation ladder's
> central premise — *a split means the range contains a seam, not that a reader is wrong.* **And per ladder
> step 2, the two readers agree on the surrounding generators while splitting on admissibility, which
> diagnoses a PHRASING dispute and points to a finer re-split (ladder step 1) rather than to genuinely mixed
> content.** **First live evidence for a mechanism that until now had none.**

## 5b. Tier 3 handles — `Worldspace/Characters/`

**Two Casey-referencing character files exist.** **Reader C returned them as person-named paths, which is
M-94 — a positive-format contract would have returned indexes.** **Addressed here by index and line count:**

| Index | Path shape | Lines |
|---|---|--:|
| **CH-1** | `Characters/Dolls/Still-Present_-_In-Game/recruitable/[name-1]/README.md` | 80 |
| **CH-2** | `Characters/Dolls/Still-Present_-_In-Game/recruitable/[name-2]/README.md` | 161 |

**⚠ Both are MIXED sources. Route through `§C.2` before opening.** **Interrogate BACKWARD per prep §5** —
*"what must be true of this place for X to have become who X is?"* — **never forward from a roster entry.**

---

# 6. What this review can and cannot prove

**CAN:** that vectors 1–3 were live for Casey on 2026-09-02, and that all three are now closed for a session
that has not already read them. **That the three mapped files are genuinely mixed**, so none may be opened
whole.

**CANNOT:** clear anyone to derive. **`Status: DRAFT`.** **And it cannot verify its own accuracy** — `§C.2`'s
standing warning is that a map's correctness is load-bearing and unverifiable by its consumer, which is
precisely why `CONFIRMED` requires 3–0 and an attribution trail.
