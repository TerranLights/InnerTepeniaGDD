# Dome Fuji — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (269 lines), the whole Pre-Trip (566 lines; the standard text compared line for line with Zukelli's and, through it, Janbogo's, and only the differing lines re-read), all 19 datasheets, the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `DF-…`). Pass folder: `City_Development_Passes/Mawson_Subnet/Dome_Fuji/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. It is robot-only (0 humans), has **no Census II row** (an empty slot is a result), and its official name is pending ("The Temple" is the interim colloquial name; the Pre-Trip correctly does not search it). Its Census I changed in the 2026-10-28 scenario (+11,777 R; 55,072 → 66,849).

**Verdict.** **Nothing blocks a run.** The Pre-Trip's census, `09`, `11`, `16` and the many shared-file lines point at the right places, and the sheets' numbers are current (the city has no humans, so the human/robot retention traps do not apply). What is left: **(1)** the **spec's per-nation table was never refreshed** — it still sums to 55,070 (the pre-change total) under a line saying it covers 66,849; **(2)** `Step_3` cites the picks 31 lines early (XS-15: they land in Relung Panen's section); **(3)** the Pre-Trip still says "datasheets not yet built" in three places and its lists are stale (Highways, Airports, Ports, RelDB, NatConn, `09`, `16`, Census L588), with the Precipitation row L118 and the city's own `16` section missing; **(4)** the spec's seed-vault ruling (L3–27) and `15_Open_Items…` Resolution 3 — the city's second most important identity fact — are in no Pre-Trip row and no sheet, and the Holidays entry "Deepest Cold" is carried as a heading only; **(5)** source: the spec still contradicts itself on whether humans can live here and on the annual mean (−54 vs −52.7), and says "10 coldest" ranks that are no longer true.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Mawson subnet/Dome_Fuji.md` (269 lines; `Step_-1` says 270, builder's convention). Header block L3–27 (the seed vault); fields L30–37; later-era headings **L242**, **L248**, **L254** = the Step −1 list; `## Notable Locations` **L227**, `## Notable Figures` **L235**; spec L43–44, L48–50, L54–108, L109–184, L123–144, L185–194, L205–218, L219–226 land on what the sheets say | ✅ |
| Census Section A heading **L354**, entry L356–362 (tier lines L360–362); Census I row **L518** (`0 / 66,849 / 66,849`; "+0 H / +11,777 R, was 0 / 55,072 / 55,072"); **no Census II row** (census L642, L644: "Kunlun, Dome Fuji, Byrd and Vostok still have no Census II rows") — the Pre-Trip and `Step_0` say so | ✅ |
| Extent file row **L628** and L249, L578, L588 | ✅ unchanged |
| `09` row **L90** (header L52): D **2.50** · humans 0 · residents 66,849 · required **18,264** · workforce **66,849** · **27.3%** (18,264 ÷ 66,849 = 27.32%); `11` row **L335** (2.50 · 27.3% · "27.3% — unchanged"; header L326); `16` Half B row (now **L283**): D 2.50 · workforce **66,849** · base 27.3 · MAND 14.5 · FREE 58.1 · src H; the city's own `16` §32 (**L3186**): baseline 15,046 (27.3%) · mandated 8,005 (14.5%) · FREE 32,021 (58.1%) — the shares equal Half B; the counts sum to 55,072, the pre-change workforce | ✅ (row line **D-03**; §32 not in any list, **A-01**) |
| `READER/Dome_Fuji.md` (AWS `Dome_F`, 1991–2025 record-period means; annual −52.7): the twelve monthly means equal the spec's Mean column and average −52.73; NMCI L231; Robot Physiology L379, L408–409, L432 and Cold Physiology L9, L181; Arcanet L26; Topics L330–331; Stations L24, L97; Founding Register row **L56** ("devout religious disciples, and not associated with any particular country"; `DR-20`; not founders: Japanese), L91, L94; Sweep L92, L128, L160 (row `Dome Fuji | . | . | . | . | . | . | 6/6`), L187, L249; Factions `Second_Interwar` L133, L173, L175, L179, L183, L187, `Hometown-based_Faction_Possibilities` L12, `basis collection - robot religions/Analysis_Notes.md` L28, L505, L590, L605, L609; Robot Religions: `Polydimensional_Animism/Culture.md` L26, `README.md` L143, L208, L230, L546, `Rituals.md` L45, `Cymatics_reverence.md` L27; Ice-Cold research `00_Extraction_Checklist.md` L7, L139; `Robot_Universals` (timeline repo): 2 files, `24_Worked_Example_Arcanet_Etiquette/README.md` L45, L48 and `14_Generational_Identity…/README.md` L30 | ✅ |
| Zero-hit claims re-run: COMNAP (no page), Energy grid, Meme Machine, True Believer, Weapons, Theoretical-Calculations, Geothermal (198 lines), jobs folder; timeline-repo `Worldspace/Characters/` (587 files): 0; `Enneagram_Character_Index.md`: 0; `06_Worked_Example_Provenance.md` (431 lines): 0; `Test_Runs` tree: 1 file | ✅ |
| Pass README pointers; concept-art folder: 5 images (the Pre-Trip and `Phase_3` list them all); megasheet 7 entries | ✅ |
| `Step_5` … `Step_9` equal Janbogo's (Subnet column, item 5) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Census L530, 552, 642 same; L588 → **L589**; add the note lines **L548, L644** (the Dome Fuji mentions in the census rebuild and scenario notes). Highways L156, 161, 163, 170 same; L281 → **L296**. Airports L18 same; L47, 52, 60, 63 → **L50, 55, 63, 66**. Ports L182, 205 same; L459, 717 → **L482, 740**. CrossSub L47, 75, 78, 97, 113–114, 118, 120 same; **add L121**. RelDB L26, 48 same; L124, 186–187, 192–193, 226, 272–273, 449, 472–473, 501, 520 → **L135, 197–198, 203–204, 237, 283–284, 460, 483–484, 512, 531** (the city's entry is L197–L207). NatConn L95, 99–100, 137 same; L311, 317–318, 341, 368, 370, 487–488, 498–499, 501, 503, 506–507, 511, 513, 518, 525, 593 → **L312, 318–319, 342, 369, 371, 492–493, 503–504, 506, 508, 511–512, 516, 518, 523, 530, 598**. `09`: L90 same; L109, 212, 219, 223 → **L111, 214, 221, 225**. `11` L335, L339 same. `16`: row **L282 → L283**; L114, 116, 138, 174, 222 same; the other 12 entries L333, 350, 439, 790, 2310, 3207, 3224, 3228, 3253, 3335, 3342, 3479, 3570 → **L336, 353, 442, 795, 2315, 3212, 3229, 3233, 3257–3258, 3340, 3347, 3484, 3575**; **missing:** the city's section heading **L3186** ("DOME FUJI — DETERMINED", upper-case). **Missing:** `Precipitation_Falls_vs_Lands.md` **L118** (the city's row). Unchanged: Extent, Stations, Topics, NMCI, Robot Physiology, Register, Religions. | live greps | Re-read each list live (SH-012) |
| **A-02** | WRONG | **"Datasheets not yet built" in three places** (2026-10-21 builder text): §C intro, §I `DATASHEET-NOT-YET-BUILT(N-5)=20` (with `RESOLVE=123`), and a §J row. All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | GAP | **The seed-vault block (spec L3–27) and the siting resolution are not addressed.** The spec opens with a developer-ruling block (`[CGRM 2026-09-02 · Path 6]`): Dome Fuji keeps one of Tepenia's two deep seed archives (the other is Kunlun), kept by the Ice Cold Buddhism devotees, "out of a sense of love and respect for the humans who sacrificed their pasts … so, just in case a catastrophe ever hit, Dome Fuji … would be able to return the favor"; human presence is forbidden. The same ruling is `Division_of_Industry/15_Open_Items_and_Three_Resolutions.md` **Resolution 3** (L164–~235; the vault "as a DEBT", L207–212). `Step_-1` starts at L30; no Pre-Trip row or sheet names L3–27 or `15`. (The block is admissible canon; admissibility is Step −1's call.) | spec L3–27; `15` L164, L187, L207 | Add the spec block to `Step_-1`; add `15` Resolution 3 as a named address (as the Cape Adare sheets carry `15`) |
| **A-04** | GAP | **Holidays: "Deepest Cold (Dome Fuji)" is the city's own established observance** (`National_Holidays.md` **L100–106**: the central communal observance of Ice-Cold Buddhism, the precise coldest point of polar night, first calm clear night after the winter solstice, a religious and mandatory observance whose date cannot be fixed in advance). `Phase_6` carries only the heading (L100). L103 names a **Background-Lore vignette** (`…/Dome_Fuji_06_Deepest_Cold.md`) — not canon, never an input. | Holidays L100–106 | Cite L100–106; say L103's path is not an input |
| **A-05** | NOTE | **Characters.** The timeline-repo tree names no Dome Fuji (as the sheet says); the **GDD** tree has one file: Calethina's `Personal_Background/Player_Chamber_Origin_Chain_DRAFT.md`. | grep | Register |
| **A-06** | NOTE | **Alias set** (mechanical draft: Dome Fuji Station · East Antarctic Plateau · Valkyrie Dome): also `Dome_F` (the READER AWS key), `AYM00089734` (the NOAA station), the pilgrimage names "Ice Cold Buddhism" (a placeholder) and "The Temple" (colloquial, deliberately not searched). Several other shared files name the city and are in no phase list (e.g. `Per-Subnet_Regional_Personality_Guide.md`, `Per-Subnet_Guides/Mawson.md`, `Parallel_Economies_Survey.md`, `Modern_Hawaiian_Language.md`) — outside the pass by design. | grep | Confirm; add |
| **A-07** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011, SH-013. | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ (a real dataset) · G3 `16` Half B ✅ (§32 not listed) · G4 Register row ✅ (named in §J) · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` (cited at the wrong lines, **D-02**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip (row L628), ❌ not in the sheets (**D-06**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I 0 + 66,849 = 66,849; the 43 per-nation **shares** sum to **99.99%** (rounding) and the tier totals are exactly the 8 : 3 : 1 share model (21.33 / 36.00 / 42.66 against 16 / 27 / 32 of 75 shares); tier lists equal the table (2 / 9 / 32) and the census Section A entry; monthly means average **−52.73 °C**; the record extremes are explicitly daily MEANS (−16.9 Dec, −79.1 Jul — the table and L126 agree) and every Rec High sits above, every Rec Low below, the Mean; monthly precipitation sums to **23.5 mm** against "~25"; falls 25 − lands 22 = lost 3 (88%, "~90%"); polar night Apr 27 → Aug 17 = **113 days**, midnight sun Oct 26 → Feb 18 = **116 days**; the coldest-month line (July −66.0 against "−65") and the warmest-month line (Jan −29.6 / Dec −29.7 against "−30") agree with the table; the Avg High / Avg Low columns are inverted in every month, exactly as L166 says ("not corrected here").

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **The per-nation table was never refreshed for the 2026-10-28 change.** The header says the breakdown is "applied to the Census I total of 66,849" (L56), but the 43 counts sum to **55,070** — the pre-change total (55,072) less 2; e.g. USA 11.20% is shown as 6,169 (= 11.20% × 55,072), where 11.20% of 66,849 is **7,487**. The shares are right; every count is on the old total. (Every other spec's per-nation table was refreshed.) | spec L56–102 |
| **S-02** | WRONG | **The annual mean is −54.0 °C in two places and −52.7 in the data.** L9 "~−54 °C annual mean" and the WIND vs COLD box L138 "At **−54.0 °C** it is the #3 coldest of the 37"; L124 says "approximately −53 °C"; the monthly means (and the READER file) average **−52.7**. The −54.0 predates the 2026-10-21 replacement of the Mean column. `15` L174 also says ~−54. | spec L9, L124, L138 |
| **S-03** | WRONG | **The spec contradicts itself on humans.** L21, L35, L207, L263 and the whole Founding block: robot-only, human presence forbidden, "no human has set foot since the pilgrimage". But L113 "It is not impossible to live at Dome Fuji as a human"; L171, L177, L180 (altitude debuffs for human characters, acclimatization); L230 "the altitude medical center — infrastructure developed to manage altitude effects for the human population". The spec's own L189 flags these as "revisit items". `Step_1_and_2` does not carry them; `Phase_4` carries NMCI L231 (the plateau problem). | spec |
| **S-04** | STALE | Peer-relative lines, none carried by the sheets except one (D-05): L123 ("nearly identical to Concordia and Ariun Nuur"), L124 ("comparable to Concordia's mean"), L127, L138 ("#3 coldest of the 37"), L141 ("shorter than Ariun Nuur and Concordia"), L172, L173; `Step_1_and_2` carries L123 and L127, L141 as written. | spec |
| **S-05** | NOTE | L30 "Dome Fuji Station (Japan / JARE) … near Valkyrie Dome (~77°19'S, 39°42'E)"; L35 "among the highest-elevation cities in Tepenia at approximately 3,810 m — higher than Concordia (3,233 m)" (peer); L111 "577 m higher than Concordia" (3,810 − 3,233 = 577 ✓). | spec |
| **S-06** | NOTE | The rename is pending ("The Temple" colloquially); the spec and the sheets carry no note. | memory; Pre-Trip |
| **S-07** | NOTE | "craft" in `Phase_8`'s term check: whole-word count 0 is right; the only substring hit is "aircraft" (L262). | spec L262 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, header fields, census (L43, L44 ✓); ❌ **A-03** (L3–27); length 270 (SH-009) |
| `Step_0` | ✅ census L518, "no Census II row"; ❌ **D-06** (extent) |
| `Step_1_and_2` | ✅ climate rows, READER row, Stations, Register; ❌ **D-03** (`16` row), **D-06** |
| `Step_3` | ❌ **D-02** (picks +31) |
| `Step_5`–`Step_9` | ✅ |
| `Step_10` | ❌ **D-07** (430) |
| `Phase_2` | ✅ census tier lines L360–362, Register L56 |
| `Phase_3` | ✅ every spec range, five images named |
| `Phase_4` | ✅ `09` L90, `11` L335; ❌ **D-03** (`16` row) |
| `Phase_5` | ❌ **D-04** (lines) |
| `Phase_6` | ✅ Polydimensional Animism ×6 lines (Culture L26, README ×4, Rituals L45), Cymatics L27; ❌ **A-04** |
| `Phase_7` | ❌ **D-03**, **D-04** (the `16` list), no §32 |
| `Phase_8` | ✅ (S-07) |
| `Phase_9` | ✅ |
| `Phase_10` | ✅ spec L235–238; NOTE **A-05** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | NOTE | all sheets | **There is no retention row** — correct (no Census II row, no humans); `Phase_9` robot share 100.00% right. | none |
| **D-02** | WRONG | `Step_3` · picks rows | "section at **L134–L138**, picks L135–137": those lines now fall inside Relung Panen's section (heading L119–149). Dome Fuji's heading is **L165**, picks **L166–168** (Paro Taktsang [PRIMARY], Potala Palace, Angkor Wat). (XS-15.) | Re-point |
| **D-03** | STALE | `Step_1_and_2`, `Phase_4`, `Phase_7` · `16` | row **L282 → L283**; the `Phase_7` "18 line(s)" list per A-01 (+3 / +5) and §32 (L3186) missing. | Re-point; add §32 shares (SH-013: consistent with Half B) |
| **D-04** | STALE | `Phase_5` | Highways **L281 → L296**; Airports **L47, L52, L60, L63 → L50, L55, L63, L66**; Ports **L459, L717 → L482, L740**; RelDB entry **L186–L196 → L197–L207**, lines **L187–L193 → L198–L204**; CrossSub "8 line(s)" + **L121**; NatConn "23 line(s)" per A-01. | Re-point |
| **D-05** | NOTE | `Step_1_and_2` rows 17, 21, 27 | carry L123 ("nearly identical to Concordia and Ariun Nuur"), L127 and L141 ("shorter than Ariun Nuur and Concordia") verbatim — peer comparisons; the row for L124 is correctly withheld. | Trim the comparison clauses |
| **D-06** | GAP | `Step_0`, `Step_1_and_2` | No extent row: Extent file **L628** (Dome Fuji's row, a 2026-09-05 snapshot at the old 55,072) and the lines L249, L578, L588. | Add, labelled the snapshot (SH-011) |
| **D-07** | STALE | counts | `Step_10` "(430 lines)" → **431**; "270-line" spec (269), "293 / 378" Meme / True Believer (292 / 377), "199-line" Geothermal (198), "74-line" Weapons (73), "36-line" Enneagram (35), "146" Energy (145) — SH-009. | per SH-009 |
| **D-08** | GAP | `Phase_6` · Holidays row | cites L100 (the heading only) — see A-04. | Re-cite L100–106 |

### 2d. DECIDE items (collected)
1. **S-01** Refresh the per-nation counts to 66,849 (shares stay).
2. **S-02** The annual mean: −52.7 (data) in L9 and the L138 box; the "#3 coldest" rank line.
3. **S-03** The human-presence remnants (L113, L171, L177, L180, L230) against the robot-only ruling.
4. **A-03** Whether the seed-vault block and `15` Resolution 3 become named inputs.
5. **S-06** The pending-rename care-note (with the Pre-Trip).
