# Marambio — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (232 lines), the whole Pre-Trip (565 lines; the standard text compared line for line with Esperanza's — same subnet, same builder form — and only the differing lines re-read), all 19 datasheets, the pass README and coverage ledger; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `MB-…`). Pass folder: `City_Development_Passes/Palmer_Subnet/Marambio/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. No rename pending.

**Verdict.** **Nothing blocks a run.** The spec's census rows, per-nation table (shares sum 100.01%), tier model and climate table are clean, the city's own `09`, `16`, census, Register and extent rows are current (the city was not touched by the 2026-10-28 scenario), and `Step_0` and `Phase_2` retention agree and are right. What is left: **(1)** `Step_3` cites the picks 31 lines early (XS-15); **(2)** the sheets cite `16` Half B (mandate 35.2 / free 23.5) and never mention the city's own determination **§12 (L1458–1521: 41.1 / 17.6, counts current)** or the 2026-09-02 Sejong / Marambio split ruling (L375–445), whose headings the name search misses because they are upper case (SH-013); **(3)** the Pre-Trip's extent list misses the city's own extent section (**§8, L397**, upper-case heading); **(4)** "datasheets not yet built" in three places, stale lists for eight shared files, a pass README whose spec pointer is dead; **(5)** the sheets withhold the highway, significance, climate-type and wind lines whole (peer clauses), so they give no description of the causeway chain, the winds or the site; **(6)** the founding-population and settled lines are excluded as "later-era" though they are founding-era text; **(7)** the spec says the city is "~415 km north of the Antarctic Circle" (it is ~260 km) and gives two daylight figures.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Palmer subnet/Marambio.md` (232 lines; `Step_-1` says 233, builder's convention SH-009). Spec L1, L3–9, L15–16, L79–81, L85, L106, L114–133, L168, L170, L176, L186, L205, L213, later-era headings **L218, L223** all land on what the sheets say | ✅ |
| Census Section A heading **L78**, entry L80–84 (tier lines L82–84); Census I row **L504** (283,442 / 286,827 / **570,269**, "island cap; revised 2026-07-04"); Census II row **L626** (195,623 / 234,522 / **430,145**, "island cap"); the destroyed-city notes **L795–796, L804**; none carries a `DR-68` note | ✅ unchanged |
| Spec arithmetic by hand: 283,442 + 286,827 = 570,269 ✓; 195,623 + 234,522 = 430,145 ✓; the 10 per-nation shares sum **100.01%** (rounding); tier lists equal the table (1 / 6 / 3) and the census entry (identical); tier totals are exactly the 8 : 3 : 1 model (Primary 27.59 = 8/29; Significant 62.07 = 18/29; Notable 10.35 = 3/29); the four count columns sum **286,829 · 283,444 · 234,522 · 195,622** against 286,827 · 283,442 · 234,522 · 195,623 (+2, +2, 0, −1 — rounding) | ✅ |
| Retention by hand: 430,145 ÷ 570,269 = **75.43%**, 195,623 ÷ 283,442 = **69.02%**, 234,522 ÷ 286,827 = **81.76%** — `Step_0` and `Phase_2` agree and are right; robots' share of Census I 286,827 ÷ 570,269 = **50.30%** (`Phase_9`) | ✅ |
| The city's own rows: `09` header L52, row **L68** (D 1.25 · 283,442 · 570,269 · required **153,217** · workforce **428,548** · **35.8%**; required recomputed: 283,442 × 0.15185 + 570,269 × 0.1932 = 43,041 + 110,176 = 153,217 ✓; workforce = 286,827 + 0.5 × 283,442 = 428,548 ✓; 153,217 ÷ 428,548 = 35.75%); `16` Half B header L247, row **L251** (428,548 · 41.3 / 35.2 / 23.5 · src C); Register row **L41** (Argentina; "almost immediately accessible"; `DR-19`, `DR-22`); `11`: no hit; NMCI: no hit; Extent row **L60** ("Seymour I. · ~78 · 570,269 · 7,311 · plausible" — 570,269 ÷ 78 = 7,311 ✓, current) | ✅ |
| Spec climate by hand: the twelve monthly means equal `READER/Marambio.md` and sum −96.1 (÷ 12 = −8.01); Avg High > Mean > Avg Low in all twelve months; Avg Low > Rec Low and Avg High < Rec High in all twelve; record high +17.4 (Mar; 23 March 2015) and record low −38.3 (Aug) are the table's extremes; precipitation column sums **362.8** exactly; falls 363 / lands 290 (80%) / lost 73 ✓; `Precipitation_Falls_vs_Lands.md` L176; solstice daylight recomputed at 64°14'S with refraction: **4.07 h** and **21.2 h** (L124–125 right; L121 differs, **S-02**) | ✅ |
| Lines found to be unchanged: Highways L75, 79, 81, 84; Airports L3, 16, 19; Ports L122, 128, 133–135, 154–155, 169, 178, 182, 184, 244, 272; CrossSub L36, 83, 93, 201; RelDB L20, 36, 46; NatConn L77, 184, 186, 207; census; Extent L14, 60, 78, 85, 410, 432, 435, 458, 468, 470, 512, 524, 576, 583, 635, 637–638, 701; Register L39, 41; Topics L214, 218; Precip L176; Stations L32; Sweep L128, 173, 188, 220; Factions (`Second_Interwar` L239, 242, 244, 246–248; `Cross_City_Cultural_Patterns` L26) | ✅ |
| COMNAP catalogue (86 pages): Marambio on pages **8** (index), **16** (the entry, 10 hits), **17** and **42** — the sheet is right. READER `Marambio.md` equals the sheet's rows | ✅ |
| Zero-hit claims re-run: Energy grid, Meme Machine, True Believer, Weapons, Arcanet, Geothermal, Holidays, NMCI, `11`, `Theoretical-Calculations`, Robot Religions (6 files), Ice-Cold folder (7), jobs folder (4), `Robot_Universals` (33), Enneagram Character Index (35), `06`. Timeline-repo `Worldspace/Characters/`: 1 file (Calethina README L60) = the sheet. Concept-art folder: `.gitkeep` only ✓. Megasheet folder: 8 items ✓ (not opened). Culture, robot-culture, Enneagram and vision-note files exist ✓ (not opened). No research log exists ✓. No `ULM/Test_Runs` file names the city ✓ | ✅ |
| Picks (live): heading **L263**, picks **L264–265** (Duisburg [PRIMARY], Gander [SECONDARY]) and the struck-Drumheller note **L266**; text equals the sheet's. `Step_5` … `Step_10` equal Esperanza's | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip §C Step 2, §D, §E, `Phase_5`, `Phase_7`, vs live). Highways L311, 312, 316, 347 → **L326, L327, L331, L362** (L75, 79, 81, 84 same). Airports L96 → **L99** (L3, 16, 19 same). Ports L360, 710, 769, 774, 825, 836 → **L383, L733, L792, L797, L848, L859** (the other 13 same). CrossSub L209 → **L210**. RelDB L123, 213–215, 224, 259–260, 290–291, 293, 295, 350, 405, 416–417, 501 → **L134, L224–226, L235, L270–271, L301–302, L304, L306, L361, L416, L427–428, L512** (L20, 36, 46 same); the city's entry L290–300 → **L301–311**, its lines L291–297 → **L302–308**. NatConn L550 → **L555** (the other 4 same). `16`: row L251 same; the other 23 lines L315, 327, 391, 394, 398, 401, 404, 409–410, 422, 570, 1481, 1488, 1495, 1500, 1506–1508, 1511, 1731, 1745, 2703, 2799 → **L318, 330, 394, 397, 401, 404, 407, 412–413, 425, 575, 1486, 1493, 1500, 1505, 1511–1513, 1516, 1736, 1750, 2708, 2804**; **add the upper-case headings L375, L392 (the Sejong / Marambio split ruling) and L1458 (§12)**. Unchanged: `09`, census, Register, Topics, Precip, Stations. | greps | Re-point per `MB-001` |
| **A-02** | WRONG | **"Datasheets not yet built" in three places** (2026-10-21 builder text): §C intro (Pre-Trip L53), §I `DATASHEET-NOT-YET-BUILT(N-5)=20` (L483, with `RESOLVE=119`), and a §J row (L528). All 19 files exist. | `Datasheets/` | Reword all three |
| **A-03** | STALE | **Extent.** The Pre-Trip's "Marambio's row **60**" is right (the first table already shows 570,269 on ~78 km² = 7,311/km², "plausible") but the city's own extent section — **Extent §8, heading L397 "# 8 · ✅ MARAMBIO — EXTENT SETTLED 2026-09-05"** (upper-case, missed by the name search), running to the next section — is not listed, nor is the open bridgehead question (the ~110 km² extent: Seymour + a ~32 km² bridgehead on Snow Hill, "a choice, not a requirement"). **No sheet carries an extent row** (D-08). | Extent L60, L397–499 | Add; label (SH-011) |
| **A-04** | NOTE | **The pass `README.md`'s spec pointer is dead:** `../../../Specs/Marambio.md` (the file is `Specs/Palmer subnet/Marambio.md`). The other pointers resolve. | `README.md` | Re-point |
| **A-05** | NOTE | **Alias set** (mechanical draft: Marambio Base · Seymour Island · Weddell Sea · Antarctic Peninsula). Not listed: **Isla Marambio**, **Picnic Passage**, **Snow Hill Island**, **James Ross Island**, **Prince Gustav Channel** (the causeway chain, spec L7, L208), **Marambio Airport** (Airports L16, Stations L32), **the shipyards**, **Vicecomodoro Gustavo Marambio** (naming), the demonym **"Marambian / marambiano"** (spec L231), and `Station_to_City_Map.md` **L35, L135** (in no phase list). | live | Add to §A; DECIDE the set |
| **A-06** | NOTE | **Characters.** The Pre-Trip's `Phase 10` row and `Phase_10.md` use the timeline-repo tree (correct, see 1a). The GDD `Worldspace/Characters/` tree names the city in 2 files (Calethina's README and `Founding_Construction_Chain_Play-by-Play.md`). | grep | Register (XS-17) |
| **A-07** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011, SH-013. | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ (§12 and the split ruling not listed, **D-02**) · G4 Register row ✅ (L41) · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` (cited at the wrong lines, **D-01**) · G8 census tier table ✅ (spec and census identical) · T2-8 extent ✅ in the Pre-Trip (row L60; §8 not listed, **A-03**), ❌ not in the sheets (**D-08**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: see 1a (census, tiers, per-nation table, climate, extent arithmetic, founding line vs Register). What is left:

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **L122 "at 64°14'S the city lies roughly ~415 km north of the Antarctic Circle"**: (66.56° − 64.23°) × 111 km = **~260 km** (Contrapunto's equivalent line, 62°13'S, says ~475 km, which is right). | spec L122 |
| **S-02** | WRONG | **Two solstice daylight figures.** L121: "winter minimum daylight ~4–5 hours; summer maximum ~19–20 hours"; L124–125: "approximately 4.1 hours" / "21.2 hours" (the monthly table agrees: Jun 4.2, Dec 21.0; hand recompute 4.07 / 21.2). | spec L121, L124–125 |
| **S-03** | NOTE | **L120 "coldest months avg −17 °C; warmest month avg 0 °C"** matches no column: the coldest means are Jul −14.9 / Jun −14.8 (the July Avg Low is −19.3); the warmest mean is January −0.8 (Avg High +1.7). | spec L120 vs L142–153 |
| **S-04** | NOTE | **Wet or dry?** L116: "colder and drier than the western coast; similar to Esperanza"; L130: "MARITIME — genuinely wet; precipitation behaves temperately" (363 mm, about half Esperanza's). | spec L116, L130 |
| **S-05** | NOTE | **`(island cap)` on both census lines** (L15–16, census L504 / L626) while the extent file's §8 says "this city was never island-confined. It is on a chain". Three cities where the roads answered (Dumont d'Urville, Denison, Temirötkel) had the label removed; this one keeps it. | spec L15–16; Extent L408–412 |
| **S-06** | STALE | **Working notes inside the spec.** L18–75 is a pasted extent working record; it carries "Esperanza carries 1,878,287 people" (the old Census I; now 1,902,205) at L58 and "MARAMBIO IS ONE OF ONLY TWO TEPENIAN CITIES THAT NEVER HAD TO BUILD ON ICE" (L30, corrected the same day from "the one") — the extent file still says **"THE ONE TEPENIAN CITY THAT NEVER HAD TO BUILD ON ICE"** at **Extent L421**. | spec L30–37, L58; Extent L421 |
| **S-07** | NOTE | **Founders.** The Register says Argentina; L170 says "Primarily Argentine exiles"; the per-nation table has Argentina as the smallest Notable nation (0.74%, against Chile 4.87%, Uruguay 4.74%). The 2026-10-13 cleanup did not touch this spec's founding line. Population claim vs founders — recorded so the 0.74% is not read as a mistake. | spec L170, L98–100; Register L41 |
| **S-08** | STALE | **Peer-relative lines:** L8 (the Palmer-subnet gateway framework), L110 ("distinct from Rothera's paved runway"), L116 ("similar to Esperanza"), L136 ("29 of the 37 are colder"), L162 ("more developed than Rothera's"), L198–201 (Esperanza as "complementary, not competing"), L229. The sheets withhold L7, L8, L116, L118 whole. | spec |
| **S-09** | NOTE | **The international gateway is named differently.** L8 and L190: "Machu Picchu **Base** (King George Island, the dedicated Upper Earth customs/immigration gateway established for **Palmer City**)"; `Airports.md` L17: "Machu Picchu **Airport**, near Contrapunto"; `16` L392 ff.: the Border & Customs Authority is "seated at Sejong" (Contrapunto). | spec L8, L190; Airports L17; `16` L392 |
| **S-10** | NOTE | L47–48 contain "food" (the national food deficit, Relung Panen's food role) — not cuisine; the term-check count (**D-09**) says 0. L8 is cut off mid-sentence in the file ("Named after Vicecomodoro Gustavo Marambio" with no closing). | spec L8, L47–48 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, header fields, census, later-era headings L218 / 223; length 233 (SH-009); ❌ **D-05** (L7, L8 withheld whole) |
| `Step_0` | ✅ census, retention; ❌ **D-08** (extent) |
| `Step_1_and_2` | ✅ climate rows (READER, Register, composition, COMNAP); ❌ **D-02** (`16` row), **D-05**, **D-06**, **D-07**, **D-08** |
| `Step_3` | ❌ **D-01** (picks +31) |
| `Step_5`–`Step_10` | ✅ (`Step_10`: **D-09**) |
| `Phase_2` | ✅ composition, retention; NOTE **D-10** (duplicate rows) |
| `Phase_3` | ✅ spec ranges, folders |
| `Phase_4` | ✅ `09` L52 / L68, NMCI; ❌ **D-02** |
| `Phase_5` | ❌ **D-03** (lines) |
| `Phase_6` | ✅ zero-hit claims |
| `Phase_7` | ❌ **D-02**, **D-04** (list; §12 and the split ruling missing); NOTE **D-12** |
| `Phase_8` | NOTE **D-11** |
| `Phase_9` | ✅ robot share 50.30% |
| `Phase_10` | ✅ spec L213–217; NOTE **A-06** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | WRONG | `Step_3` · picks rows | "section at **L232–L236**, picks L233–235": those lines are Utstein's and Signy's sections. The city's heading is **L263**, picks **L264–265**, struck-pick note **L266**. (XS-15.) | Re-point |
| **D-02** | STALE | `Step_1_and_2` row 37; `Phase_4` row 3; `Phase_7` row 1 | All quote `16` Half B (mandated **35.2%**, free **23.5%**, src C). The city's own determination **§12 (L1458–1521)** is in no sheet: baseline 177,203 (**41.3%**) · mandated **175,942 (41.1%)** · FREE **75,404 (17.6%)** · distinctive tier 251,345 (58.7%); mandate = maritime/port 30% (75,404) + aviation/logistics (domestic) 30% (75,404) + half of technical/maintenance 10% (25,134); the counts sum to 428,549 = the **current** workforce (the city was not changed by `DR-68`). The preamble ruling **L375–445** (the Sejong / Marambio split: Marambio = cargo by sea in and people by air around the country; Contrapunto = where people enter and the Border & Customs seat) is canon about this city that no sheet carries. (SH-013.) | Quote §12 and the ruling beside Half B |
| **D-03** | STALE | `Phase_5` | Line numbers per **A-01** (Highways ×4, Airports ×1, Ports ×6, CrossSub, RelDB entry and lines, NatConn). | Re-point |
| **D-04** | STALE | `Phase_7` · `16` "other lines" row | 23 lines → live numbers per **A-01**; add L375, L392, L1458. | Re-point and add |
| **D-05** | GAP | `Step_-1` rows 14–15; `Step_1_and_2` rows 16, 18 | The Highway access (L7), Significance (L8), climate-type (L116) and prevailing-winds (L118) lines are withheld whole ("compares the city with other places"), so the sheets give **no description of the causeway chain, the winds or the site's role**. The non-peer parts: the Picnic Passage → Snow Hill → James Ross → Prince Gustav Channel chain to the Trinity Peninsula (also Highways L81, L316); winds "NW and SW, monthly mean vector near 270°; storms on the southwesterlies; gusts to 220 km/h; föhn from the mountain spine and cold southerly barrier winds off the Weddell Sea Low"; "eastern Peninsula continental — Weddell Sea influence". | Add the trimmed values |
| **D-06** | WRONG | `Step_1_and_2` row 21 (polar night) | Carries spec L122 verbatim, "roughly ~415 km north of the Antarctic Circle" (should be ~260 km, **S-01**). Row 19 carries "The mainland record belongs to Esperanza's 18.3 °C" (a cross-city line). | Correct; trim |
| **D-07** | STALE | `Step_1_and_2` rows 40–41 | `Settled:` (L168) and `Founding population:` (L170) are both "excluded: later-era content". L170 ("Primarily Argentine exiles, who independently developed their own operational culture and discipline around running the airfield … Marambio and Esperanza together gave the Argentine exile community a strong northern Peninsula presence") is founding-era text, not later-era; L168 mixes First Interwar upkeep with the post-2564 rebuild. The Register governs the founders either way. (Defect pattern 6.) | Copy L170 (and rule L168) |
| **D-08** | GAP | `Step_0`, `Step_1_and_2` | No extent row. Extent **L60** (7,311/km², plausible) and **§8 (L397 ff.)**: 570,269 on ~78 km² of snow-free ground; the ~110 km² bridgehead option; James Ross reserved for Esperanza. Label (SH-011). | Add |
| **D-09** | STALE | counts | `Step_10` "(430 lines)" → **431** (`wc -l`; builder convention 432). The other "N-line" counts follow the builder convention (spec 233 / 232, Holidays 166 / 165, Meme 293 / 292, True Believer 378 / 377, Geothermal 199 / 198, Arcanet 28 / 27, Weapons 74 / 73, Enneagram 36 / 35, Energy 146 / 145, NMCI 246 / 245) — SH-009. | per SH-009 |
| **D-10** | NOTE | `Phase_2` · rows 4–7 | The two annotation rows (spec `(founding wave)` at L81, census at L84) each appear twice. | Delete the duplicates |
| **D-11** | NOTE | `Phase_8` · term check | "cuisine / food / dish / drink — 0": the spec has "food" at L47–48 (the national food deficit; not cuisine) — the count method and the file disagree. The city's making content is the shipyards and the airfield maintenance (L196, L207). | Mention |
| **D-12** | NOTE | `Phase_7` · header "13 of 13" vs last row "11 of 11" | disagree (SH-008). | per SH-008 |

### 2d. DECIDE items (collected)
1. **D-02** Whether the sheets must carry §12 and the split ruling and say Half B is superseded (SH-013).
2. **A-03** Whether the extent section (§8) and the bridgehead question are listed and carried.
3. **S-05** Whether the `(island cap)` label stays given the extent file's "never island-confined".
4. **S-01 / S-02** Whether spec L121–122 are corrected.
5. **D-07** Whether L168 / L170 are admitted.
6. **A-05** The alias set.
