# Davis — manual input audit (2026-10-29) — a FINISHED city: the sheets, plus drift since the pass

Method: `README.md` in this folder. **Davis's ULM pass was run and closed on 2026-09-16** (24 pass files; last substantive change 2026-10-01). So this audit has two parts: **(A) the Pre-Trip sheet and the 19 datasheets**, read by hand and checked against the live sources like any other city; and **(B) drift**: *has anything the finished pass rested on changed since?* **Finished pass files are never edited**: each drift item is an `AMEND` entry in `FIX_LEDGER.md` (entries `DV-…`). **Limit, stated plainly:** the 24 pass files (about 700 KB) were *not* re-read line by line; drift was found by comparing what the pass recorded (numbers, claims) with the live sources, and by `git` history of the spec. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`.

**Verdict.** The pass is **not harmed in its method**, but **it carries values and claims that are now out of date**, and the datasheets cite live lines whose content has since changed without saying "as recorded at the pass." The one claim that is **wrong, not just old**: the pass's Phase 5 says *"Davis holds a confirmed airport marker"*; `Airports.md` lists Davis among the cities with **no air access**. Everything else is census-driven (the 2026-10-28 scenario) or a line-number shift.

---

## PART A — SHEETS

### A1. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mirny subnet/Davis.md` exists, **236 lines** (same length at the pass commit and now, so every spec line citation still lands) | ✅ |
| Census I row **L494** (Davis) and Section A heading L390, tier table L390–396 | ✅ lines live |
| `09` row **L79** and header L52; `NMCI` L23–24; `Sweep` L164 (Davis, 5/6); Theoretical-Calculations L992–994; `06`'s other lines | ✅ lines live |
| `Cross_Subnet` L53–54, L123–131, L139–142 (the Davis–Mawson passage and the namesake detail) | ✅ lines live; both correctly flagged and not extracted |
| NatConn L65–67 (the Davis–Neumayer link) | ✅ |
| Local culture / robot culture files exist (read-last); megasheet folder exists (withheld); concept-art folder empty; `READER/Davis.md` keyed by the city's own name | ✅ |
| Phase 6, 8, 9, 10 zero-hit claims (religions: **6 files across 2 developed religions**, 4 further roster folders are empty; holidays; Buddhism; Weapons file; Enneagram index; Characters: the two "davis" hits are Bette Davis and Sammy Davis Jr.) | ✅ re-run |
| Research log `Research_Logs/Davis_Research_Log.md` exists | ✅ (3,427 lines; the sheet says 1,953) |
| Step 6–9 Tier U sheets | ✅ headers match the live table except the missing Subnet column and Step 9's item 5 (same as Casey) |

### A2. Findings — the Pre-Trip (older trial-format sheet, kept as a record; refreshed 2026-10-21)
| ID | Sev | Finding | Fix |
|---|---|---|---|
| **A-01** | STALE | Says Davis's datasheets are "a full **22-file** set (11 step + 11 phase)"; the set is **19 files** (Step 0/Phase 0 and Steps 1–2/Phase 1 were merged 2026-09-22). | "19 files" |
| **A-02** | STALE | `City_Relationship_Database.md` "L175–176" (header and §…): Davis's entry is now **L186–187** (+11 after the 10-21 edit). | Re-point |
| **A-03** | NOTE | Quotes a "`Highways.md` L318" note ("`Ports.md` called EMPTY (0 bytes)") as a dated record; **live L318 is a different passage**. The refresh note says it is a record, not a live pointer. | Say "historic (line no longer exists)" |
| **A-04** | NOTE | `City_Symbol_Assignments.md` L92 cited as Davis's row: Davis is at **L71, L112 (BLANK), L335–338**; L92 does not name it. (The refresh block itself gives L112 and L335 correctly.) | Re-point |
| **A-05** | NOTE | Being a record, it carries no "Names Davis at" lists and no `T8` ranges of the newer generated sheets; it cites no runbook line numbers (so none can be stale). If Davis is ever re-run or re-derived (the developer's end-of-pass Division-of-Industry re-run does touch it), a rebuilt Pre-Trip is needed. | |

### A3. Findings — the datasheets
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Step_-1`, `Step_0`, `Phase_2` · census rows | Census II cited at **L611 and L613 and L496** (three different numbers in two files); the live row is **L617** (Census I **L494** is right). | Re-point to L617 |
| **D-02** | **STALE** | `Step_-1`, `Step_0`, `Phase_2`, `Phase_4`, `Step_1_and_2` · every population-derived value | **Pre-`DR-68` values, with no "as recorded at the pass" label** although the commit of 2026-10-28 said such rows would be annotated: Census I 563,599 H / 594,715 R / 1,158,314 → **575,738 / 606,493 / 1,182,231**; Census II 437,423 / 344,173 / 781,596 → **445,531 / 351,912 / 797,443**; retention 67.48 / 77.61 / 57.87 / 19.74 pp → **≈ 67.45 / 77.38 / 58.02 / 19.36 pp** (DERIVED by hand); robots' share 51.34% → **≈ 51.30%**; density 1,158,314 ÷ 410 = 2,825.16/km² → **≈ 2,883/km²**; `09` row (309,368 required; 876,515 workforce) → **315,832; 894,362** (35.3% unchanged); `16` Half B row workforce 876,514 · base 40.7% → **894,362 · 40.8%** (MAND 20.7% and FREE 38.5% unchanged). | Add "as recorded at the pass (2026-09-16); census since changed by `DR-68`" to each, or re-copy live (decision) |
| **D-03** | STALE | `Step_1_and_2`, `Phase_4` · `16` citations | Half B header "L245/L246" → **L247**; Davis row "L261" → **L262**; §19 ranges (L2028–2073, L2065–2069, L2043–2077, L2056–2062, L2068, L2077–2078, L2086–2092) are all **+5** now (§19 heading L2006; the developer's 2026-09-16 ruling "Mandate 28.2% / free 31.1%" at **L2074–2076**); L3563 → **L3568**; "L2122–2123" (the Vestfold Hills sentence) could not be matched (the live lines there belong to another city's section) | Re-read each live |
| **D-04** | **WRONG** | `Phase_5` · Airports row | "**Davis holds a confirmed airport marker** — `Airports.md` L47, L52". `Airports.md` lists Davis in the **"Everything Else Has No Air Access"** list (live **L50**) and the note that real stations have airstrips today but none exists in Tepenia (**L55**). (Identical to the Casey error corrected 2026-10-29.) | Correct as Casey's row was |
| **D-05** | STALE | `Phase_5` · RelDB; NatConn | RelDB "L175–176" → **L186–187**; NatConn Davis section "L296–308" → **L303–315**; the Davis–Mawson passage "L302–305" → **L304–306** | Re-point |
| **D-06** | WRONG | `Step_-1`, `Step_0` · symbol pair | "Earth / Earth, column-anchored" (`City_Symbol_Assignments.md` **L92**) and "Planet half RATIFIED, Element half RESERVED": Davis's row has been **BLANK since the developer ruling of 2026-09-16** (live **L112**; the earlier pair is recorded as superseded at L335). L92 does not name Davis. | Update row; re-point |
| **D-07** | STALE | `Step_10` | "`06` (406 lines) … **ZERO hits**": the file is **431 lines** and the word *Davis* appears **three times** (L317, L319, L320, the "orchestrator exposure" note, which names the session that ran Davis's Steps 4–10). | Re-count, re-word |
| **D-08** | STALE | `Phase_3` header | "`Specs/Mirny subnet/Davis.md` (181 lines)": 236 lines. And **`Step_-1`'s read-spec and exclusion ranges stop at L181**, so **L182–236** (the rest of Economy & Industry L182–206, Notable Locations L207, Notable Figures L215, Connection to Concordia L220, Legacy L225, Open Questions L230) are classified nowhere; the contract dates from before the 2026-09-16 port-ruling additions. | Note on the sheet; amendment (DV-005) |
| **D-09** | STALE | `Step_3` | "Davis_Research_Log.md (1,953 lines)": now **3,427**; two inspiration-place files for Davis exist (`Davis_Inspiration_Place_Research_R1/R2`, 2026-10-xx) and are not mentioned. | Re-count; register |
| **D-10** | NOTE | all | Counts one above `wc -l` in some sheets, equal in others (`Weapons` 73, `Laws` 54, `Doll` 35 follow `wc`; holidays 166 does not) (SH-009). | |
| **D-11** | NOTE | `Step_6`, `Step_9` | Section 1 columns lack "Subnet"; `Step_9` lacks item 5 (as Casey). | add |
| **D-12** | NOTE | many rows | **Conclusions inside value-and-citation sheets** (Field Guide Rule 1b): "TESTED AND ADOPTED", "THE TRAP", "⇒ …", the Option B reasoning, framing of the Round 3 finds. These were hand-built before Rule 1b and are a *record of the pass*; they would have to be stripped before reuse as input to any re-run. | decision |

---

## PART B — DRIFT SINCE THE PASS (2026-09-16)

What changed in Davis's own sources, from `git` history and live comparison:

| ID | Change | Where the pass or its sheets rest on it | Needed (as an amendment note; the pass files are not edited) |
|---|---|---|---|
| **DV-001** | **Census scenario `DR-68` (2026-10-28):** Census I 1,182,231 (+23,917), Census II 797,443, every per-nation count in the spec rescaled (shares unchanged). | Old **Census I total 1,158,314** appears in `00.1` (3×), `00_Frame` (5×), `02_Spine` (2×; and the density 2,825/km² against the 410 km² extent, 3 more times), `03_Research` (1×), `04_Phase_02` (2×), `04_Phase_04` (2×), `07_QA` (1×), `README` (2×), the Pre-Trip (1×); old **Census II total 781,596** in `00.1` (2×), `00_Frame` (2×), `01_Inherited` (1×), `02_Spine` (1×), `04_Phase_02` (3×), `07_QA` (1×), the Pre-Trip (1×); the old human and robot components (563,599 / 594,715 / 437,423 / 344,173) in `00.1`, `00_Frame`, `04_Phase_02`, `04_Phase_04`, `04_Phase_09`; the old workforce 876,51x in `04_Phase_04`, `04_Phase_07`, `04_Phase_08`, `04_Phase_10`, `07_QA`. | Amendment: restate the figures; the findings that rest on ratios (retention, density, share of robots) move by 0.03–0.4 percentage points or 2%; **none of the shares changed** |
| **DV-002** | **`Phase 5`'s air claim is wrong** (D-04): the pass says Davis "holds a confirmed airport marker" (`04_Phase_05` L23, L203). | The "By air" access row of Phase 5 and anything built on it. | Amendment note: Davis has **no air access** (`Airports.md` L50, L55); `DR-82` keeps the Mirny onward-flight service at Mirny, not Davis |
| **DV-003** | **Symbol pair blanked 2026-09-16** (developer: *"for now … we can just make that blank"*). | "Earth / Earth" in `00.1`, `00_Frame`, `02_Spine`, the Pre-Trip (twice) | Amendment: the pair is BLANK; the Planet-half/Element-half standing statements fall away (the Pre-Trip carries a dated update already) |
| **DV-004** | **Station-heritage and namesake rulings** (`DR-19`, `DR-24`, `DR-25`, `DR-32`, 2026-10-01): the spec's Significance line lost "Australian Antarctic Division heritage" and the vision line lost "genuine … heritage". The pass files were "audit-fixed" 2026-10-01 and no longer contain the removed phrase; `City_National_Connections.md` L303–305 and `City_Cross_Subnet_Relationships.md` L123–131 still rest on the withheld megasheet and a real-world namesake story (both flagged by the pass, correctly). | `00_Frame` §0.5 reserved item 1 (the namesake) | none beyond keeping the flags; confirm the 10-01 fixes covered every file (the sample greps found none left) |
| **DV-005** | **Spec grew to 236 lines before the contract was closed**; the contract's admitted/excluded ranges stop at L181 (D-08). | `00.1` §4.1 and §4.3 | Amendment: classify L182–236 (most of it is the Economy & Industry text added with the port ruling) |
| **DV-006** | **`16` Half B row refreshed** (workforce 894,362; base 40.8%), while §19 keeps the pre-`DR-68` worker counts (labelled "not recomputed", `16` L1). | `04_Phase_07` and `Datasheets/Phase_4` quote §19 and Half B | Amendment: say which row governs; the **28.2% / 31.1%** ruling lives only in §19, not in Half B (Half B still shows 20.7% / 38.5%) |
| **DV-007** | **`DR-75` (Relung Panen):** Davis is named as the holder of the **national agricultural research half** and a partner in the joint research project with Ariun Nuur and Zhongshan (file 18 §3), and "Davis 39.6% of export supply" appears in file 18 §4 (not citable as an export headcount). | Davis's Phase 7 (research as a co-equal pillar) | Amendment: cross-reference only; no change to Davis's own figures |
| **DV-008** | **Highways / Ports / Airports edited after the pass:** `Ports.md` Davis row now L559, L736 (and others); `Airports.md` L3, L23, L50, L55; Davis is also named in the new Winter Intake Airport row (L23). | Phase 5 | Amendment: re-point; add the Winter Intake mention if relevant (it names Davis? to be read at the sweep) |
| **DV-009** | **Research:** `Davis_Research_Log.md` grew (3,427 lines) and `Davis_Inspiration_Place_Research_R1/R2` were added (2026-10). | Step 3 | Register |

### Items I did not check (for honesty)
The 24 pass files themselves (their reasoning, T8 records, Gate 11 arithmetic beyond the density), the Davis Local Culture / Robot Culture sheets (read-last), and whether the 2026-10-01 audit-fix commit removed every station-heritage phrase from every pass file (sampled by search only).

## Source corrections needed (the developer decides)
DV-S01 `16` Half B Davis row MAND/FREE (20.7% / 38.5%) vs the §19 ruling (28.2% / 31.1%) · DV-S02 `City_Cross_Subnet_Relationships.md` L123–131 and `City_National_Connections.md` L303–305 (withheld-source claim; `DR-19` "Australian-heritage" wording) · DV-S03 Davis's `16` §19 worker counts (not recomputed) · DV-S04 `City_Symbol_Assignments.md` L335–338 (superseded record, fine) — no action.
