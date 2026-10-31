# Mawson — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (184 lines), the whole Pre-Trip (566 lines; the standard text compared line for line with Dome Fuji's — same subnet, same builder form — and only the differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `MW-…`). Pass folder: `City_Development_Passes/Mawson_Subnet/Mawson/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. **"Mawson" is also the name of the subnet and of the explorer (St. Douglas)**, so every name hit must be sorted into the city's own line and a line where the Subnet column says Mawson. The city is not yet run as a whole; `Research_Logs/Mawson_Research_Log.md` (170 lines, 3 sessions) holds an earlier warm run's Steps −1 → 3 (Session 1, 2026-09-04). Its Census I and II changed in the 2026-10-28 scenario.

**Verdict.** **Nothing blocks a run.** The spec is clean arithmetic; the city's own `09`, `16`, census and extent rows are current, and `Step_0` retention is right. What is left: **(1)** `Phase_2` retention is the pre-change set; **(2)** `Step_3` cites the picks 31 lines early (XS-15; they land at the end of Relung Panen's section); **(3)** the Pre-Trip says "datasheets not yet built" in three places, its lists are stale and — because the name is shared with the subnet — **mostly other cities' lines** (Sayowa's, Dome Fuji's and Sinheung's rows), while the city's own `16` determination (§33, upper-case heading) is in no list or sheet; **(4)** source: the spec gives no usable record-extreme conflict this time, but its precipitation column sums to 268 mm against "about 350", the Precip Prob column holds `~0%` in six months, and L79's "coldest months avg −20 °C" matches no column.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mawson subnet/Mawson.md` (184 lines; `Step_-1` says 185, builder's convention). Later-era headings **L167** (Connection to Concordia) and **L172** (Legacy) = the Step −1 list (there is no Current Status section); `## Notable Locations` **L152**, `## Notable Figures` **L161**; spec L3–9, L15–16, L20–22, L26–62, L63–124, L73–91, L129, L135–144, L145–151, L162–163 land on what the sheets say | ✅ |
| Census Section A heading **L328**, entry L330–334 (tier lines L332–334); Census I row **L487** (721,869 / 748,782 / 1,470,651; `DR-68` +12,140 H / +11,778 R); Census II row **L612** (435,429 / 532,864 / 968,293); the many "other lines" L319, L338, L493, L497, L514, L518, L530, L536, L634, L648, L654, L783, L787 | ✅ unchanged |
| Retention by hand: 968,293 ÷ 1,470,651 = **65.84%**, 435,429 ÷ 721,869 = **60.32%**, 532,864 ÷ 748,782 = **71.16%** — `Step_0` right | ✅ (`Phase_2` disagrees, **D-01**) |
| The city's own rows: `09` **L75** (header L52): D 1.25 · humans 721,869 · residents 1,470,651 · required **393,745** · workforce **1,109,717** · **35.5%** (393,745 ÷ 1,109,717 = 35.48%; `16` has 1,109,716 — 748,782 + 0.5 × 721,869 = 1,109,716.5, `09` rounds up); `16` Half B (now **L271**): D 1.25 · workforce **1,109,716** · base 41.0 · MAND 14.8 · FREE 44.3 · src C; `11`: no city row; Extent row **L610**; Register row **L54** ("Kazakhstan, Russia (the core state) and Australia, jointly"; `DR-33`, `DR-46`, `DR-53`; `DR-45` reversed) | ✅ |
| `READER/Mawson.md` (annual −11.2): the twelve monthly means equal the spec's Mean column and average −11.18; COMNAP pages **8** (index) and **25** (the entry); Stations L34, L35, L55; Precip **L155**; Topics L302, L326–327; Holidays **L42** ("St. Douglas"); NMCI L224; Sweep L24, L25, L76, L161; Theoretical L992; Factions `Second_Interwar` L31, L33, L43, L47, L53, L57, L143, L147, L151 and `Cross_City_Cultural_Patterns` L61, L68; Polydimensional Animism `Culture.md` L18, `README.md` L172–173, L217 (the Enfolded; the sheet carries all four); Highways L102, L104, L149; CrossSub; Ports L129–130, L154, L189, L203, L207, L224, L232, L240, L244 | ✅ unchanged |
| Zero-hit claims re-run: Energy grid, Meme Machine, True Believer, Weapons, Arcanet, Geothermal (198 lines), `Robot_Universals` (timeline repo), Ice-Cold folder (7), jobs folder, `06_Worked_Example_Provenance.md` (431 lines, 0 hits); timeline-repo `Worldspace/Characters/`: Calethina README L58, L60 and `Formative_History.md` L5 only | ✅ |
| Pass README pointers; `Step_5` … `Step_9` equal Janbogo's (Subnet column, item 5) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Highways L102, 104, 149 same; L344 → **L359**. Airports L48, 52, 60 → **L51, 55, 63**. Ports L129–130, 154, 189, 203, 207, 224, 232, 240, 244 same; L318, 362, 386, 528, 710, 770, 772, 837 → **L341, 385, 409, 551, 733, 793, 795, 860**. CrossSub L45–48, 51, 75, 95–97, 113, 118, 123, 130, 139–142, 146–147, 160–161, 168 same; L231 → **L232**. RelDB L22, 25, 36, 48–49, 55, 104–105 same; L124, 142, 148, 191, 312–313, 316–319, 436–439, 447, 449–450, 511 → **L135, 153, 159, 202, 323–324, 327–330, 447–450, 458, 460–461, 522** (the city's entry is L323–L333). NatConn L61–62, 95, 134, 137, 162, 174–175 same; L303, 305, 311, 317 → **L304, 306, 312, 318**; L341, 369–370, 374, 383–384, 392 → **L342, 370–371, 375, 384–385, 393**; L405, 411, 485–486, 488, 490, 495, 505, 510–511, 524–525, 555–556, 583 → **L410, 416, 490–491, 493, 495, 500, 510, 515–516, 529–530, 560–561, 588**. `09` L75, 82, 90 same. `16`: row **L270 → L271**; L253 same; the other 16 entries L282, 300, 1305, 1307, 1310–1311, 1571, 3249, 3284, 3288, 3292, 3299, 3316–3317, 3342, 3479, 3571 → **L283, 303, 1310, 1312, 1315–1316, 1576, 3254, 3289, 3293, 3297, 3304, 3321–3322, 3347, 3484, 3576**; **missing:** the city's own section heading **L3263** ("## 33. ✅ MAWSON — DETERMINED", upper-case). Unchanged: census, extent, Stations, Topics, Precip, Holidays, NMCI, Register. | live greps | Re-read each list live (SH-012) |
| **A-02** | WRONG | **The "names Mawson at" lists are mostly other cities' lines.** The Pre-Trip warns of the shared name; the effect is large. `09`: only **L75** is the city (L82 is **Sayowa**'s row, L90 **Dome Fuji**'s). `16`: only **L271** and §33 (**L3263–3340**) are the city's; L253 is Sayowa's row, L283 Dome Fuji's, L303 an earlier pilot table. Extent: **L610** is the city's, **L628** is Dome Fuji's row. Census: only **L328, L487, L612** are the city's; L493 / L497 (Shirayuki, Sinheung), L514 (Sayowa), L518 (Dome Fuji) and the totals are not. Register: **L54** is the city's row; **L55** is Sayowa's (Temirötkel), **L56** Dome Fuji's, and L82, L88, L89, L93, L94 are the change log. | live | Split each list: the city's own lines / lines where the Subnet column says Mawson |
| **A-03** | WRONG | **"Datasheets not yet built" in three places** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20` (with `RESOLVE=122`), and a §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-04** | NOTE | **An earlier warm run exists in part.** `Research_Logs/Mawson_Research_Log.md` (170 lines; Session 1, 2026-09-04, "Steps −1 → 3 of a warm ULM run on Mawson", plus two later sessions) is listed as "(exists)" and as Step 3's write target; no other file of that run is in the pass folder (it is empty by design) and no archive folder for it exists. Whether the log's content is an admissible input to the new pass is not stated. | live | DECIDE |
| **A-05** | NOTE | **Alias set** (mechanical draft: Mawson Station · Horseshoe Harbor · Holme Bay · Mac.Robertson Land). Not listed: **St. Douglas** / **Douglas Mawson** (a naming fact, Holidays L42), **Prince Charles Mountains** (spec L155), **Rumdoodle** and the Mawson skiways (Stations L34, L35, L55 are found by "Mawson"), **Temirötkel Junction** (Highways), the Hwy 4 name "Mawson-Sinheung Highway" (the road, not the city). The renamed neighbor **Sayowa → Temirötkel** is still "Sayowa" in `09` L82, `16` L253 and census L514, and in the timeline repo's `Worldspace/Locations/README.md` L19 ("Mawson subnet: Dome Fuji, Mawson, Sayowa") — flag only. | live | Confirm; add |
| **A-06** | NOTE | The GDD `Worldspace/Characters/` tree names the city in 10 files (Calethina's chain — "request work at Mawson" — and related); the sheet cites the timeline-repo tree (3 hits), which is the one the Pre-Trip names. | grep | Register |
| **A-07** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011, SH-013. | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ (cited at the wrong line, **D-03**; §33 not listed) · G4 Register row ✅ (row L54; the range is too wide, **A-02**) · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` (cited at the wrong lines, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip (row L610), ❌ not in the sheets (**D-06**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals (721,869 + 748,782 = 1,470,651; 435,429 + 532,864 = 968,293); the 26 per-nation shares sum to **99.98%** (rounding); all four count columns sum **exactly**; tier lists equal the table (1 / 7 / 18) and the census Section A entry; tier totals are exactly the 8 : 3 : 1 share model (17.02 / 44.7 / 38.3 against 8 / 21 / 18 of 47); monthly means average **−11.18 °C** (stated −11.2); in every month Avg High > Mean > Avg Low and **Avg Low > Rec Low**; the record extremes (+10.6 Jan; −36.0 Jul) equal the table; polar night Jun 14 → Jun 30 = 17 days and midnight sun Dec 1 → Jan 13 = 44 days (recomputed at 67°36′S: about 16 and 46 days); falls 350 − lands 133 = lost 217 (38.0%).

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | NOTE | **Precipitation.** The monthly column sums to **268 mm**; the header says "approximately 200–350 mm" (L84) and the regime box "falls ~350" (L89). The note under the table says Avg Precip is "derived — BoM's rainfall statistics … not yet retrieved". | spec L84, L89, L100–111, L116 |
| **S-02** | WRONG | **The Precip Prob column holds `~0%` in six months** (Feb, Mar, May, Jun, Sep, Oct) while those months carry 15–28 mm; the other six read 30–40%. The column is "derived"; the zeros cannot be probabilities. | spec L100–111 |
| **S-03** | NOTE | **L79 "coldest months avg −20 °C; warmest month avg −1 °C"** matches no column: the coldest mean is August **−18.1** (July −17.8); the −20 is nearer the Avg Low (−20.9 / −21.4). The warmest (January −0.3, December −0.8) is right to the degree. | spec L79 vs L100–111 |
| **S-04** | NOTE | **The de-stacking puts Germany (Significant) at 1.86%**, below nine of the eighteen Notable nations (Estonia 3.17, South Africa 3.09, Norway 3.05, Vietnam 2.99, Thailand 2.97, Belarus 2.93, Netherlands 2.92, Slovenia 2.71, Bulgaria 2.68). | spec L48 |
| **S-05** | STALE | Peer-relative lines, none carried by the sheets except one (D-05): L75 ("similar to Mirny (same latitude …)"), L94 ("19 of the 37 Tepenian cities are colder"), L181 (Fort McMurdo). | spec |
| **S-06** | NOTE | Founders (L129, the Register) are Kazakhstan, Russia and Australia, but **neither Kazakhstan nor Russia appears in the tier table** (China is the sole Primary); L183 records this as the developer's call. The Russia split is pending (memory). | spec L129, L183 |
| **S-07** | NOTE | The Daylight column shows Jun **0\*** and Dec **24\***; the daylight entries for May (5.2) and Jul (3.0) are monthly averages around a 17-day polar night. | spec |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, header fields, census; length 185 (SH-009) |
| `Step_0` | ✅ census, retention; ❌ **D-06** (extent) |
| `Step_1_and_2` | ✅ climate rows, READER, Stations, COMNAP, Register; ❌ **D-03** (`16` row), **D-05**, **D-06** |
| `Step_3` | ❌ **D-02** (picks +31) |
| `Step_5`–`Step_9` | ✅ |
| `Step_10` | ❌ **D-07** (430) |
| `Phase_2` | ❌ **D-01** (retention) |
| `Phase_3` | ✅ spec ranges |
| `Phase_4` | ✅ `09` L75, NMCI L224; ❌ **D-03** |
| `Phase_5` | ❌ **D-04** (lines) |
| `Phase_6` | ✅ Polydimensional Animism ×4, Holidays L42 |
| `Phase_7` | ❌ **D-03**, **D-04** (list, §33 missing) |
| `Phase_8` | NOTE **D-08** |
| `Phase_9` | ✅ robot share 50.92% (748,782 ÷ 1,470,651 = 50.916%) |
| `Phase_10` | ✅ spec L161–163; NOTE **A-06** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Phase_2` · "Computed retention %" | "combined 65.83% · human 60.21% · robot 71.25%" are the pre-`DR-68` set. `Step_0` (hand-checked): **65.84% · 60.32% · 71.16%**. | Replace |
| **D-02** | WRONG | `Step_3` · picks rows | "section at **L121–L126**, picks L122–125": those lines are the end of Relung Panen's section. Mawson's heading is **L152**, picks **L153–156** (Odessa [PRIMARY], Varna, Trogir, Jeju City). (XS-15.) | Re-point |
| **D-03** | STALE | `Step_1_and_2` row 40; `Phase_4` row 3; `Phase_7` | `16` Half B row **L270 → L271**. The city's own determination **§33 (L3263–3340)** is in no sheet: baseline 447,342 (**41.0%**) · mandated 225,584 (**20.7%**) · FREE 418,942 (**38.4%**) · distinctive tier 644,527 (59.0%); the counts sum to 1,091,868 — the **pre-`DR-68`** workforce (737,004 + 0.5 × 709,729), so only the shares are current. Half B's MAND 14.8 / FREE 44.3 is superseded (SH-013). | Re-point; add §33 shares |
| **D-04** | STALE | `Phase_5`; `Phase_7` | Highways **L344 → L359**; Airports **L48, L52, L60 → L51, L55, L63**; Ports **L318, L362, L386, L528, L710, L770, L772, L837 → L341, L385, L409, L551, L733, L793, L795, L860**; RelDB entry **L312–L322 → L323–L333**, lines **L313–L319 → L324–L330**; CrossSub "23 line(s)" **L231 → L232**; NatConn "34 line(s)" per A-01. `Phase_7` "18 line(s)" per A-01, most of which are other cities' rows (A-02). | Re-point |
| **D-05** | NOTE | `Step_1_and_2` · climate-type row | carries spec L75 verbatim, "similar to Mirny (same latitude …)" — a peer comparison. | Trim the clause |
| **D-06** | GAP | `Step_0`, `Step_1_and_2` | No extent row: Extent file **L610** (the city's row, a 2026-09-05 snapshot at the old Census I) — and **not L628** (Dome Fuji's). | Add, labelled the snapshot (SH-011) |
| **D-07** | STALE | counts | `Step_10` "(430 lines)" → **431**; "185-line" spec (184), "293 / 378" Meme / True Believer (292 / 377), "199-line" Geothermal (198), "28-line" Arcanet (27), "74-line" Weapons (73), "36" Enneagram (35), "146" Energy (145) — SH-009. | per SH-009 |
| **D-08** | NOTE | `Phase_8` · term check | "cuisine / food / dish / drink — 0" ✓, but the spec's food-and-drink-adjacent content is "hospitality and honeymoon tourism" (L146), the honeymoon traditions (L184) and the public libraries (L156), none of which the pattern catches. | Mention L146, L156, L184 |

### 2d. DECIDE items (collected)
1. **A-04** Whether the earlier warm run's research log is an input to the new pass.
2. **A-02** Whether the lists are split into the city's own lines and subnet-column lines.
3. **S-02 / S-01** Re-derive the Precip Prob (and Avg Precip) columns or label them design-grade.
4. **D-03** Whether the sheets must carry §33 and say Half B is superseded (SH-013).
