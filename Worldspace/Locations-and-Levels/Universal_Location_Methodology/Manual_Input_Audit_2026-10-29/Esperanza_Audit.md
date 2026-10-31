# Esperanza — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (173 lines), the whole Pre-Trip (565 lines; the standard text compared line for line with Byrd's — same builder form, no rename — and only the differing lines re-read), all 19 datasheets, the pass README and coverage ledger; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `ES-…`). Pass folder: `City_Development_Passes/Palmer_Subnet/Esperanza/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. No rename pending.

**Verdict.** **Nothing blocks a run.** The spec's census rows, per-nation table (shares sum 100.00%, all four count columns sum **exactly** to the current census), tier model and climate table are clean, and the city's own `09`, `16`, `11`, census, Register and NMCI rows are current. `Step_0` retention is right. What is left: **(1)** `Phase_2` retention is the pre-change set (the same defect as Mawson); **(2)** `Step_3` cites the picks 31 lines early (XS-15) and loses two picks — the headline Primary pick (the Basque baserri tradition) is withheld because of an annotation, and Pestalozzi Children's Village is excluded as "later-era" because its text says "war-displaced"; **(3)** the sheets cite `16` Half B (mandate 24.1 / free 36.2) and never mention the city's own determination **§11 (L1332–1457: 25.6 / 34.7, counts on the old workforce)**, which the name search misses because its heading is upper case (SH-013); **(4)** "datasheets not yet built" in three places, stale line lists for eight shared files, and a pass README whose spec pointer is dead; **(5)** the extent row is the 2026-09-05 snapshot on the old census, and the extent file says outright that **Esperanza has no declared extent** and may be too big for its site; **(6)** the spec gives two different winter-solstice daylight figures; **(7)** the locked-canon NMCI file sizes the city's education sector on the old census and a whole-workforce basis.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Palmer subnet/Esperanza.md` (173 lines; `Step_-1` says 174, builder's convention SH-009). Spec L1, L3–9, L15–16, L20–22, L28, L46, L54–78, L109, L115, L121, L135, L142, L150, later-era headings **L155, L160** all land on what the sheets say | ✅ |
| Census Section A heading **L66**, entry L68–74 (tier lines L70–72, note L74); Census I row **L483** (967,477 / 934,728 / **1,902,205**; `DR-68` +12,140 H / +11,778 R from 955,337 / 922,950 / 1,878,287 — 967,477 − 955,337 = 12,140 ✓, 934,728 − 922,950 = 11,778 ✓); Census II row **L605** (510,762 / 683,124 / **1,193,886**; `DR-68` +8,108 H / +7,739 R from 502,654 / 675,385 / 1,178,039 ✓) | ✅ |
| Spec arithmetic by hand: 967,477 + 934,728 = 1,902,205 ✓; 510,762 + 683,124 = 1,193,886 ✓; the 7 per-nation shares sum **100.00%**; tier lists equal the table (1 / 4 / 2) and the census entry (identical); tier totals are exactly the 8 : 3 : 1 model (Primary 36.36 = 8/22; Significant 54.55 = 12/22; Notable 9.09 = 2/22); the four count columns sum **934,728 · 967,477 · 683,124 · 510,762** — exactly the census, so the table is on the **current** figures | ✅ |
| Retention by hand: 1,193,886 ÷ 1,902,205 = **62.76%**, 510,762 ÷ 967,477 = **52.79%**, 683,124 ÷ 934,728 = **73.08%** — `Step_0` right (`Phase_2` disagrees, **D-01**); robots' share of Census I 934,728 ÷ 1,902,205 = **49.14%** (`Phase_9`) | ✅ |
| The city's own rows: `09` header L52, row **L81** (D 1.11 · 967,477 · 1,902,205 · required **490,159** · workforce **1,418,467** · **34.6%**; workforce = 934,728 + 0.5 × 967,477 = 1,418,466.5; 490,159 ÷ 1,418,467 = 34.55%; required recomputes to 490,195 at D = 1.11 exactly, so D is 1.1098 unrounded); `16` Half B header L247, row **L259 → L260** (1,418,466 · 39.7 / 24.1 / 36.2 · src C); `11` **L332** (selected cities, baseline load: D 1.11 · old 34.6% · new 39.7%) and header L326; Register row **L40** (Argentina; "almost immediately accessible"; `DR-19`, `DR-22`); NMCI all 13 lines (L29–209) | ✅ |
| Spec climate by hand: the twelve monthly means equal `READER/Esperanza.md` and sum −54.5 (÷ 12 = −4.54, "−4.5"); Avg High > Mean > Avg Low in all twelve months; Avg Low > Rec Low and Avg High < Rec High in all twelve; record high +18.3 (Feb; the WMO-ratified 6 February 2020 value) and record low −38.4 (Jul) are the table's extremes; precipitation column sums **726.4** exactly; falls 726 / lands 581 (80%) / lost 145 ✓; `Precipitation_Falls_vs_Lands.md` L169 carries 726 / 581 / 145; solstice daylight recomputed at 63°24'S with refraction: **4.5 h** and **20.6 h** (L77–78 right; L61 differs, **S-01**) | ✅ |
| Lines found to be unchanged: Highways L55, 75, 77, 79; CrossSub L36, 202; RelDB L20, 46; NatConn L75, 183, 185, 189, 208–209; `11` L264, 332; Extent L409, 460, 464, 512, 606; Register L39–40; Topics L204, 207; Precip L169; Sweep L121, 171, 189, 193; Factions (`PostWar_Refugee` L109, 127; `Second_Interwar` L119, 127, 131, 137; `Cross_City_Cultural_Patterns` L26); Polydimensional Animism `Culture.md` L18, `README.md` L172, L218 | ✅ |
| COMNAP catalogue (86 pages): Esperanza on pages **8** (index) and **15** (the entry, 5 hits) — the sheet is right. READER `Esperanza.md` L4–L8, L12–14 equal the sheet's rows | ✅ |
| Zero-hit claims re-run: Energy grid, Meme Machine, True Believer, Weapons, Arcanet, Geothermal (198), Holidays (165), Stations (99), `Theoretical-Calculations`, Ice-Cold folder (7), jobs folder (4), `Robot_Universals` (33), Enneagram Character Index (35), `06`. Spec term check: cuisine / dress / music — 0 ✓; craft — 2 ✓ (see **D-09**). Timeline-repo `Worldspace/Characters/`: 3 files (Griselda Alejandra Chávez README L48, `Conflict_Experiences` L5, `Formative_History` L7) = the sheet. Concept-art folder: `.gitkeep` only ✓. Megasheet folder: 7 items ✓ (not opened). Culture, robot-culture, Enneagram and vision-note files exist ✓ (not opened). No research log exists ✓. No `ULM/Test_Runs` file names the city ✓ | ✅ |
| `Step_5` … `Step_10` equal Contrapunto's (Subnet column, item 5); the differentiation-table header lines are as `Step_6` says | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip §C Step 2, §D, §E, `Phase_5`, `Phase_7`, vs live). Airports L41, 48 → **L44, L51**. Ports L513, 710, 729 → **L536, L733, L752** (L155, 169, 177 same). RelDB L123, 208–209, 213, 260, 295–296, 350–351, 417 → **L134, L219–220, L224, L271, L306–307, L361–362, L428** (L20, 46 same); the city's entry L208–218 → **L219–229**, its lines L209–215 → **L220–226**. NatConn L407, 439, 459 → **L412, L444, L464** (the other 6 same; still 9 lines). `09` L104, L207 → **L106, L209** (L81 same). `16`: row L259 → **L260**; the other 23 lines L314, 363, 1146, 1231, 1339, 1345, 1356, 1362, 1370, 1384, 1389, 1400, 1407, 1420, 1424, 1441, 1443, 1511, 1744, 1886, 2799, 3224, 3560 → **L317, 366, 1151, 1236, 1344, 1350, 1361, 1367, 1375, 1389, 1394, 1405, 1412, 1425, 1429, 1446, 1448, 1516, 1749, 1891, 2804, 3229, 3565**; **add the §11 heading L1332** (upper-case "ESPERANZA", missed by the name search). Unchanged: Highways, CrossSub, census, Extent, NMCI, Register, Topics, Precip. | greps | Re-point per `ES-001` |
| **A-02** | WRONG | **"Datasheets not yet built" in three places** (2026-10-21 builder text): §C intro (Pre-Trip L53), §I `DATASHEET-NOT-YET-BUILT(N-5)=20` (L483, with `RESOLVE=121`), and a §J row (L528). All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | STALE | **Extent.** The Pre-Trip's "Esperanza's row **606**" is the 2026-09-05 snapshot on the old Census I (1,878,287: 188 km² at 10,000/km², 268 at 7,000; at 1,902,205: 190 / 272). The extent file says the city has **no declared extent** ("Esperanza carries 1,878,287 with no declared extent, on Hope Bay, already flagged as possibly too big for its site"; L460–470 reserve James Ross Island's Ulu Peninsula for it) and Ports L513 gives Hope Bay as 5.6 km × 3.7 km. The spec says nothing about extent. **No sheet carries an extent row** (D-06). | Extent L460–470, L606; Ports L513 | Add the open question; label the row a snapshot (SH-011) |
| **A-04** | NOTE | **The pass `README.md`'s spec pointer is dead:** `../../../Specs/Esperanza.md` (the file is `Specs/Palmer subnet/Esperanza.md`). The local-culture, vision-note and research-log pointers resolve (the log "may not exist yet"). | `README.md` | Re-point |
| **A-05** | NOTE | **Alias set** (mechanical draft: Esperanza Base · Hope Bay · Trinity Peninsula · Antarctic Peninsula). Not listed: **Emilio Marcos Palma** (the 1978 birth, spec L8), the **Esperanza Institute of Medicine** (NMCI; found by the name), the demonym **"esperanzeño / esperante"** (spec L172), the **birth registry**, the Course-of-Events file `Esperanza_09_The_Shipping_Partner_Across_the_Bay.md` (Ports L513), and `Station_to_City_Map.md` **L34, L135** (in no phase list). | live | Add to §A; DECIDE the set |
| **A-06** | NOTE | **Characters.** The Pre-Trip's `Phase 10` row and `Phase_10.md` use the timeline-repo tree (correct, see 1a). The GDD `Worldspace/Characters/` tree names the city in 13 files: Griselda Alejandra Chávez (2), the recruitable **TBN [TCY-45 "heavenly summertime Momo"]** (6) and **Shuchar Vaszyong** (5). | grep | Register (XS-17) |
| **A-07** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011, SH-013. | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ (§11 not listed, **D-03**) · G4 Register row ✅ (L40) · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` (cited at the wrong lines, two picks lost, **D-02**) · G8 census tier table ✅ (spec and census identical) · T2-8 extent ✅ in the Pre-Trip only as the old snapshot (**A-03**), ❌ not in the sheets (**D-06**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: see 1a (census, tiers, per-nation table, climate). What is left:

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **Two winter-solstice daylight figures.** L61: "winter minimum daylight ~5–6 hours; summer maximum ~19–20 hours"; L77–78: "approximately 4.5 hours" / "20.6 hours" (the monthly table agrees with these: Jun 4.6, Dec 20.4; hand recompute 4.5 / 20.6). | spec L61, L77–78 |
| **S-02** | NOTE | **L60 "coldest months avg −15 °C; warmest month avg +1 °C"** matches no Mean value: the coldest mean is July −10.9 (−15 is the July Avg Low); the warmest mean is January +1.5 (December +0.8). | spec L60 vs L82–93 |
| **S-03** | NOTE | **Founders.** L24 says "Argentina is the founding nation per the Founding section below"; the Founding section (L115) says "Multinational rather than purely Argentine" and never names Argentina; the Register says "Argentina". The 2026-10-13 cleanup that rewrote twenty specs' `Founding population:` lines to the Register did not include this spec. (Population claim vs founders — not a contradiction, but the line the sheets copy as "the spec's founding population" does not say who founded it.) | spec L24, L115; Register L40 |
| **S-04** | NOTE | **Wet or dry?** L48 and L56: the eastern coast is "colder and drier than the maritime west"; L66: "MARITIME — genuinely wet; precipitation behaves temperately" (726 mm, 80% retention). | spec L48, L56, L66 |
| **S-05** | STALE | **Peer-relative lines:** L7 (the Contrapunto and Pergamino comparison), L48 and L56 (the western coast), L72 ("30 of the 37 are colder"), L103 (Rothera). `Step_1_and_2` and `Step_-1` withhold L7 and L56 whole. | spec |
| **S-06** | NOTE | **Pointers to other files.** L109 ("see also `Course_of_Events/Esperanza_02_…md`, flagged in this city's own `candidates.txt`"), L138 (`Cities/Local_Cultures/Halley_Subnet/Belgrano.md` — **another city's read-last culture file** — and Griselda Alejandra Chávez's character file). Phase 5 readers must not open Belgrano's culture file; L151 names a canon character, not a placeholder. | spec L109, L138, L151 |
| **S-07** | DECIDE | **NMCI (locked canon) sizes the city's education on the old census and the wrong basis.** `National_Medical_and_Care_Institutes.md` L173 ("about 2% of a **1.88 M** city" — the old 1,878,287; now 1,902,205) and L176 ("§15 education sector of ~25% is **350,155 workers**" = 25% of the *whole* old workforce 1,400,620). `16` §11 (written the next day) says percentages are of the distinctive tier and corrects education to half of 25% = 105,599 workers, quoting this very NMCI passage. | NMCI L173–176; `16` §11 L1346–1362 |
| **S-08** | NOTE | The spec has no extent statement (no section, no figure), against a Census I over 1.9 million — the extent file flags it as open (A-03). An empty slot is a result; recorded so it is not mistaken for an omission in the audit. | spec; Extent L464 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, header fields, census, later-era headings L155 / 160; length 174 (SH-009) |
| `Step_0` | ✅ census, retention; NOTE **D-08** (status cells); ❌ **D-06** (extent) |
| `Step_1_and_2` | ✅ climate rows (READER, Register, composition, COMNAP 8 / 15); ❌ **D-03** (`16` row), **D-06** |
| `Step_3` | ❌ **D-02** (picks +31; two picks lost) |
| `Step_5`–`Step_10` | ✅ (`Step_10`: **D-07**) |
| `Phase_2` | ❌ **D-01** (retention pre-change); the tier tables are identical ✅ |
| `Phase_3` | ✅ spec ranges, folders |
| `Phase_4` | ✅ `09` L52 / L81, `11` L326 / L332, NMCI ×13; ❌ **D-03** |
| `Phase_5` | ❌ **D-04** (lines) |
| `Phase_6` | ✅ Polydimensional Animism ×3 lines |
| `Phase_7` | ❌ **D-03**, **D-05** (list; §11 missing); NOTE **D-10** |
| `Phase_8` | NOTE **D-09** |
| `Phase_9` | ✅ robot share 49.14% |
| `Phase_10` | ✅ spec L150–154; NOTE **A-06** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · "Retention" | "combined 62.72% · human 52.62% · robot 73.18%" are the pre-`DR-68` set. `Step_0` (hand-checked): **62.76% · 52.79% · 73.08%**. | Replace |
| **D-02** | WRONG | `Step_3` · picks rows | "section at **L223–L231**, picks L224–L230": those lines are Lazar's and Utstein's sections (Halley subnet). The city's heading is **L254**, picks **L255–261** (Basque baserri [PRIMARY], Auroville [PRIMARY], SOS Children's Villages [PRIMARY], Boys Town, Pestalozzi Children's Village, Sardinia's Blue Zone, Kibbutz communal child-rearing). The sheet **withholds L224 (now L255)** — the headline Primary pick, "The Basque baserri tradition, Spain/France [PRIMARY]" — as "compares the city with other places" because of its annotation ("ranked first of Esperanza's three Primary picks …"), and **excludes L228 (now L259, Pestalozzi Children's Village, "founded 1946 to house and raise war-displaced children of any nation") as "later-era content"** — real-world history; the scan tripped on "war". (XS-15; defect pattern 6.) | Re-point; copy both picks, trimming the annotation |
| **D-03** | STALE | `Step_1_and_2` row 38; `Phase_4` row 3; `Phase_7` row 1 | All quote `16` Half B (mandated **24.1%**, free **36.2%**, src C). The city's own determination **§11 (L1332–1457)** is in no sheet: baseline 555,826 (**39.7%**) · mandated **359,037 (25.6%)** · FREE **485,756 (34.7%)** · distinctive tier 844,793 (60.3%); mandate = education/childcare/family HALF 12.5% (105,599) + agricultural FULL 15% (126,719) + maritime/harbor HALF 10% (84,479) + other/administrative HALF (the birth registry) 5% (42,240); three national roles (FOOD · EDUC · MEDICINE); the counts sum to **1,400,619 — the pre-`DR-68` workforce** (current 1,418,466); the shares are current. (SH-013.) | Quote §11 beside Half B; say which supersedes and that the counts are on the old workforce |
| **D-04** | STALE | `Phase_5` | Line numbers per **A-01** (Airports ×2, Ports ×3, RelDB entry and lines, NatConn ×3). | Re-point |
| **D-05** | STALE | `Phase_7` · `16` "other lines" row | 23 lines → live numbers per **A-01**; add L1332. | Re-point |
| **D-06** | GAP | `Step_0`, `Step_1_and_2` | No extent row, and the open question is not stated: Extent **L606** (snapshot on the old Census I), **L460–470** (no declared extent; James Ross Island reserved for it), L464, Ports L513 (Hope Bay 5.6 × 3.7 km). | Add, labeled the snapshot (SH-011) |
| **D-07** | STALE | counts | `Step_10` "(430 lines)" → **431** (`wc -l`; builder convention 432). The other "N-line" counts follow the builder convention (spec 174 / 173, Stations 100 / 99, Holidays 166 / 165, Meme 293 / 292, True Believer 378 / 377, Geothermal 199 / 198, Arcanet 28 / 27, Weapons 74 / 73, Enneagram 36 / 35, Energy 146 / 145, NMCI 246 / 245) — SH-009. | per SH-009 |
| **D-08** | NOTE | `Step_0` · Census I and II rows | "status cell: revised 2026-07-04" / "revised 2026-07-03" — both census cells now also carry the `DR-68` scenario note (+12,140 H / +11,778 R; +8,108 H / +7,739 R). | Add |
| **D-09** | NOTE | `Phase_8` · term check | "craft — 2 hit(s)" are L138 and L151 — the whalebone-and-metal pianos "crafted in Belgrano" that passed through the harbor — the one piece of making content in the spec; the sheet does not say what the hits are. | Mention L138, L151 |
| **D-10** | NOTE | `Phase_7` · header "13 of 13" vs last row "11 of 11" | disagree (SH-008). | per SH-008 |

### 2d. DECIDE items (collected)
1. **D-03** Whether the sheets must carry §11 and say Half B is superseded (SH-013).
2. **A-03** Whether the open extent question (no declared extent; James Ross Island reserved) is surfaced in the Pre-Trip and the sheets.
3. **S-07** Whether NMCI L173–176 is updated to the current census and the distinctive-tier basis.
4. **S-01** Whether spec L61 is corrected to L77–78.
5. **A-05** The alias set.
