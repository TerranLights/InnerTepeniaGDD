# Cape Adare — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (286 lines), the whole Pre-Trip (564 lines; standard text compared line for line with earlier cities, only differing lines re-read), all 19 datasheets (this city's are the longer 2026-09-30 hand-built set, with partial updates since), the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `CA-…`). Pass folder: `City_Development_Passes/Janbogo_Subnet/Cape_Adare/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run as a whole, but **Cape Adare is the subject of the Run 7 cold test run**, which is why `06_Worked_Example_Provenance.md` carries a skip manifest for it.

**Verdict.** **Nothing blocks a run.** The Pre-Trip is the refreshed version (its "19 files, all present" and zero "not built" count are right), and the census values in the sheets' main rows are current. What is left: **(1)** the sheets mix **old and new** census figures — `Step_0` retention has a new combined figure over old human and robot figures; `Step_1_and_2` and `Phase_7` give the `16` workforce as 1,126,670 where the live row is 1,144,518; `Phase_4` contradicts itself on the same number; **(2)** the Run 7 manifest cites in `Step_10`, `Phase_3` and `Phase_8` are one line off, and the extent row is cited at L611 (it is L607); **(3)** the founding "TBD" is described as an undeveloped field, but the Register (`DR-44`) has since ruled it an empty slot — a result; **(4)** the Pre-Trip still calls the climate file a stub; **(5)** the spec's monthly table has the Avg Low column below the record low in nine months, and its density tables carry pre-change census numbers and peer comparisons.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Janbogo subnet/Cape_Adare.md` (286 lines; the Step −1 sheet says 286, exact). Later-era headings **L256** (Connection to Concordia), **L264** (Current Status / Destruction), **L270** (Legacy) = the Step −1 list; spec L3–L9, L15–16, L18–22, L28–45, L51–57, L66–68, L100–101, L109–113, L118–123, L133–137, L144–151, L155–158, L161, L164–167, L173–184, L192, L197–199, L211–215, L219–229, L239–245, L249–252, L281 land on what the sheets say | ✅ |
| Census Section A heading **L260**, entry L262–266 (annotation lines L265–266), Census I row **L484**, Census II row **L607**; other lines L588 (→ L589), L801–802, L804 | ✅ (one shift, **A-01**) |
| Census I **758,107 H / 765,465 R / 1,523,572**; Census II **434,451 / 631,447 / 1,065,898** | ✅ |
| `09` row **L66** (header L52): Required **409,472** · Workforce **1,144,519** · **35.8%**; `11` rows **L97** (header L95: 177,732 · 44.4 Mt · 13.7×), **L109–111** (the provider-contradiction resolution), **L265**; `15_Open_Items…` L117 (Resolution 2), L121, L133, L141, L159; Sweep **L153** (2/6), L7, L13–15, L141, L232; `01` **L286**; `08` **L654**; Theoretical **L982–990** (Christchurch/Lyttelton at L986); `16` §26 content (466,136 / 247,701 / 412,834 = 41.4 / 22.0 / 36.6%) | ✅ (the `16` §26 line numbers are +5, **D-03**) |
| `READER/Cape_Adare.md` (rebuilt 2026-10-28; "READER station: none"; Possession Island AWS proxy, `DR-70`; annual −11.4): the spec's Mean column equals it; the `Step_1_and_2` sheet says so | ✅ |
| `Precipitation_Falls_vs_Lands.md` **L154** (350 / 133 / 217); Topics **L295–297**; Founding Register row **L68**; `05` §6.1d and the `06` Run 7 manifest content; Falkland Treaty QR L40, L49, L110–113, L128, L130–131; Robot Physiology QR L48, L81, L95–99; Zodiac Full Attributes 267 lines; substrate folder 22 files | ✅ |
| Zero-hit claims re-run: Stations, Energy grid, Geothermal, Arcanet, NMCI, Robot Physiology, Holidays (St. Carsten absent, as the spec says), Robot_Religions, Ice-Cold folder, Meme Machine, True Believer, Robot_Universals (33), Enneagram index; Characters canon: **0** files name the city, Carsten or Borchgrevink | ✅ |
| Pass README: the four source pointers (spec, local culture, vision notes, research log) are right for this city | ✅ |
| Pre-Trip §C intro "19 files, all present" and §I `DATASHEET-NOT-YET-BUILT(N-5)=0` | ✅ (this Pre-Trip was refreshed) |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip vs live). Highways L226, 231 → **L227, 232**. Airports L41, 47 → **L44, 50**. Ports L195 same; L521, 716, 790–791 → **L544, 739, 813–814**. RelDB L30, 34, 50 same; L130–131, 148, 249, 307, 501 → **L141–142, 159, 260, 318, 512**. NatConn L222–223 same; L438, 445, 448, 456 → **L443, 450, 453, 461**. Census L588 → **L589**. `16`: row L268 → **L269**; L66, 163 same; L349, 376–377 → **L352, 379–380**; L2696, 2715, 2798, 3046, 3086, 3149, 3568 → **L2701, 2720, 2803, 3051, 3091, 3154, 3573**. Add `Precipitation_Falls_vs_Lands.md` **L154**. CrossSub, `09`, `11`, Extent, Topics, Register unchanged. | live greps | Re-read each list live (SH-010) |
| **A-02** | WRONG | **§D Phase 1 climate row:** "⚠ The file is an 8-line STUB, not a dataset". `READER/Cape_Adare.md` was **rebuilt on 2026-10-28** as a 16-line dataset (Possession Island AWS proxy, `DR-70`); the spec's Mean column was replaced the same day. | READER file | Reword; cite the rebuilt file and the proxy |
| **A-03** | GAP | **Alias set is "Cape Adare" only.** Names the spec and shared files use: **Ridley Beach** (Borchgrevink's hut site; `Ports.md` L544 "Ridley Beach — a LANDING, not a harbor"), **Adare Peninsula**, **Possession Island** (the climate proxy, `AYM00089879`) and **Adare Hallett** (`AYW00087701`, the July proxy), **St. Carsten** / **Carsten Borchgrevink** (the civic association; a naming fact only), **Cape Roget**. | spec L3, L55, L148, L215; Ports L544 | Add; re-run the name search |
| **A-04** | GAP | **Founding Register is not an address.** Row **L68** (`DR-44`, 2026-10-03: "Mixed; no single dominant national community. An empty slot by ruling, not a gap") and **L90**. The Pre-Trip mentions it only in a §J note. | Register L68, L90 | Add to §D Phase 2; reword the sheets (**D-10**) |
| **A-05** | NOTE | No `Cape_Adare_Inspiration_Place_Research` files yet. Shared items SH-001 … SH-007; megasheet folder "7 files" = 6 files + 1 subfolder (this folder also holds `Questline_Asset_Concept_Art/`). | | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ (the Pre-Trip row is stale, **A-02**) · G3 `16` Half B ✅ (cited at the wrong line, **D-03**) · G4 Register row ✅ (not an address, **A-04**) · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ (`Inspirational-Influences.md` L41–44 is right for this city: the Janbogo subnet's section sits before the Relung Panen insert, so XS-15 does not apply) · G8 census tier table ✅ · T2-8 extent ✅ (cited at the wrong line, **D-04**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals; the 12 per-nation shares sum to **100.00%**; all four count columns sum **exactly** (Census I robots **765,465**, humans **758,107**; Census II robots **631,447**, humans **434,451**); tier lists equal the table (2 / 6 / 4); monthly means average **−11.38 °C** (stated −11.4); polar night May 19 → Jul 26 = **69 days**, midnight sun Nov 14 → Jan 30 = **78 days**; the temperature-range line (L149) matches the means; retention 133 ÷ 350 = 38%, lost 217.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | STALE | **The density tables (L73–78, L127–131) carry pre-change census numbers and compare other cities:** Cape Adare Census II "1,050,051" (now **1,065,898**; 2.94 km² → about 362,550 per km²), Davis "781,596" (now 797,443), Sinheung "888,292" (now 815,309), Lazar "1,803,977" (now 1,639,426); the whole frame is explicitly superseded at L83–98. The tables are a dated derivation, not a live claim; the Step −1 sheet correctly does not transcribe them (L73–78, L127–131). | spec L73–78, L127–131 |
| **S-02** | WRONG | **In nine months Avg Low (night) is lower than Rec Low** (an average cannot be below the record): Jan −9 vs −2.8, Feb −15 vs −4.6, Mar −22 vs −18.4, May −31 vs −17.2, Jun −33 vs −12.3, Aug −30 vs −17.9, Sep −26 vs −20.6, Oct −20 vs −18.8, Dec −9 vs −3.1. The Rec Low column is itself mixed (April −31.5 but June −12.3; the July value −42.2 comes from a different proxy station). L192 admits that Avg High / Avg Low "still the earlier derived figures"; it does not mention the Rec Low column. | spec L173–184, L148, L192 |
| **S-03** | NOTE | Precipitation: the monthly column sums to **289 mm**, the header says "approximately 200–350" (L151), and the regime box says falls ~350 (L156). | spec L151, L156, L173–184 |
| **S-04** | NOTE | L281 (Open Questions) cites a Background-Lore vignette and a withheld megasheet file as the source of the adopted observance; the sheets correctly do not carry it (`Phase_6` records the line as not pre-staged). | spec L281 |
| **S-05** | NOTE | The timeline repo's `Worldspace/Locations/` folder now holds 4 `.md` files; the sheets' "10 files" is out of date (**D-11**). | `find` |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings L256, L264, L270; census (exact match); extent facts; ❌ **D-04**, **D-11** |
| `Step_0` | ❌ **D-01** (retention), **D-04** (extent line) |
| `Step_1_and_2` | ✅ climate rows incl. the 2026-10-28 proxy, READER row, Precip L154 cross-check; ❌ **D-02**, **D-03**, **D-10** |
| `Step_3` | ✅ picks L41–44 (the Janbogo section is unaffected by the insert) |
| `Step_5` | ✅ stub |
| `Step_6` | ✅ ten sections; ❌ **D-12** (no Subnet column) |
| `Step_7`, `Step_8` | ✅ |
| `Step_9` | ❌ **D-12** (item 5 missing) |
| `Step_10` | ❌ **D-06** (manifest lines), **D-12** |
| `Phase_2` | ❌ **D-01**, **D-05**, **D-10** |
| `Phase_3` | ✅ spec lines; ❌ **D-06** (`06` L237) |
| `Phase_4` | ✅ `09`, `11` rows; ❌ **D-02** (contradicts itself), **D-03** |
| `Phase_5` | ❌ **D-07** |
| `Phase_6` | ✅ |
| `Phase_7` | ✅ `15`, Sweep, `01`, `08`; ❌ **D-02**, **D-03** |
| `Phase_8` | ❌ **D-06** (`06` L237) |
| `Phase_9` | ❌ **D-08** |
| `Phase_10` | ✅ zodiac counts; ❌ **D-09** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Step_0` rows 18–21; `Phase_2` row 20 | **Old and new census figures mixed.** `Step_0`: combined 1,065,898 ÷ 1,523,572 = **69.96%** (new, right), but human "426,343 ÷ 745,967 = 57.15%" and robot "623,708 ÷ 753,687 = 82.75%" and spread "25.60 pp" are pre-`DR-68`. `Phase_2`: combined **70.02%** (old) · human 57.15% · robot 82.75% · 25.60. By hand with the live values: **69.96% · 57.31% · 82.49% · spread 25.18 pp** (434,451 ÷ 758,107; 631,447 ÷ 765,465). | Replace in both |
| **D-02** | WRONG | `Step_1_and_2` `16` row; `Phase_4` rows 20 and 22; `Phase_7` row 29 | `16` Half B workforce quoted as **1,126,670** (pre-`DR-68`); live row L269: **1,144,518** (= 765,465 + 0.5 × 758,107), and `09` has **1,144,519**. `Phase_4` row 20 already says 1,144,519, so row 22 ("`09` states 1,126,671; `16` states 1,126,670 — one-worker discrepancy") contradicts the row above it; `Phase_7` row 29 says §26's tiers "sum to 1,126,671, matching `09`'s workforce" — no longer true: `09` and Half B agree at 1,144,519 / 1,144,518, and §26's counts (466,136 + 247,701 + 412,834) are the pre-`DR-68` set (`16` L1). | Replace; label §26 pre-`DR-68` |
| **D-03** | STALE | `Step_1_and_2` row 34; `Phase_4` rows 22, 32; `Phase_7` | `16` Half B row **L268 → L269**; `16` §26 **L2657–2738 → L2662–2743**, hut line L2727–2729 → **L2732–2734**, L2798 → **L2803**, L2693–2707 → **L2698–2712**, L2702–2704 → **L2707–2709**, L2734–2735 → **L2739–2740**; L376–379 → **L379–382**. | Re-point (`Tools/remap_line_citations.py` exists for this) |
| **D-04** | WRONG | `Step_-1` / `Step_0` · extent row | Cites the extent row at **L611** ("table header L607, section L605"). Cape Adare's row is **L607**; the table header is L603–604. The values quoted (1,499,654 · 150 · 214; on the live 1,523,572: 152 / 218) are right. | Re-point |
| **D-05** | STALE | `Phase_2` row 27 | Runbook §C.9b **L2088 → L2090**, §C.9d **L2147 → L2150**. | Re-point |
| **D-06** | STALE | `Step_10` rows 1–6 and range; `Phase_3` row 27; `Phase_8` row 15 | The Run 7 manifest in `06` is now **L229–L251** (sheet L228–250); table rows **L238–243** (sheet L237–242); the re-run note **L232–234** (sheet L232–233); the file has **431** lines (sheet "428"). Every row is one line later; nothing was added to the manifest. | Re-point |
| **D-07** | STALE | `Phase_5` | Highways **L227, 232** (section L223); Airports **L44, 47–48, 50** (+3); Ports **L544, 739, 598, 397, 399, 813–814** (+23); RelDB entry "L130–137" → **L141–148**, other-city entries L243/L249 → **L254/L260**, L301/L307 → **L312/L318**, L148/L30 → **L159/L30**, L501 → **L512**; NatConn Cape Adare section heading **L440 → L450**, others' sections L216–217, L433, L451 → **L222–223, L443, L453, L461**. | Re-point |
| **D-08** | STALE | `Phase_9` · robot share | "**50.26%** — 765,465 ÷ 1,523,572 = 50.2415%": the calculation shown gives **50.24%**; 50.26% is the pre-`DR-68` value. | 50.24% |
| **D-09** | STALE | `Phase_10` · "No invented person names" | `00_RUNBOOK.md` **L1980 → L1982** (Phase 10 row); `03_The_Phase_Spine.md` **L219 → L220**. | Re-point |
| **D-10** | STALE | `Step_1_and_2` row 38; `Phase_2` row 21 | The founding population is described as "TBD — an undeveloped field, not a finding". The Register row **L68** (`DR-44`, 2026-10-03) rules it "**Mixed; no single dominant national community. An empty slot by ruling, not a gap**" — a result under the No Forced Fit law. The sheets pre-date the ruling and do not cite the Register. | Add Register L68; reword |
| **D-11** | STALE | `Step_-1` row "U Location canon"; `Step_1_and_2` row 41; `Phase_5` row 33 | "**10** files enumerated" in the universe repo's `Worldspace/Locations/` (2026-09-30): the folder now holds **4** `.md` files; `Earth/Antarctica/` is still empty. The roster line is README **L18**, right. | Update the count |
| **D-12** | GAP | `Step_6`, `Step_9`, `Step_10` | `Step_6` section 1 lacks the **Subnet** column; `Step_9` lacks item 5; `Step_10`'s lines are in D-06. | As Casey (CASEY-048/049) |
| **D-13** | NOTE | `Step_1_and_2` row 20 | Says the READER file "had been a 7-line stub"; the file's own note says 8-line. | Match the file |

### 2d. DECIDE items (collected)
1. **S-02** Re-derive the Avg High / Avg Low / Rec Low columns (or mark them as design-grade estimates that do not fit).
2. **S-01** Update or drop the superseded density tables (L73–78, L127–131).
3. **A-03** Confirm the alias set.
