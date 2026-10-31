# Dumont d'Urville — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (255 lines), the whole Pre-Trip (567 lines; the standard text compared line for line with Denison's — same subnet, same hand-built-then-refreshed form — and only the differing lines re-read), all 19 datasheets, the pass README and coverage ledger; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `DD-…`). Pass folder: `City_Development_Passes/Janbogo_Subnet/Dumont_dUrville/` (the file and folder names drop the apostrophe: `Dumont_dUrville`). `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. **The developer ruled on 2026-10-13 that this city needs a new name (founders are Japan, not France); the name is not chosen and no sweep is to be done unprompted** — every finding below is written against the current name.

**Verdict.** **Nothing blocks a run.** The Pre-Trip's census, extent and `09` / `16` rows point at the right city's lines, and the census numbers in the sheets are current (this city's Census I and II did not change in the 2026-10-28 scenario). What is left: **(1)** a small arithmetic slip repeated in two sheets (robot retention 77.17% and spread 16.94 pp; the correct values are 77.19% and 16.96 pp); **(2)** `09` L60, `16` Half B L279 and `16` §24 still carry the **pre-trim** population (a 10% trim on 2026-09-05) — the sheets quote them faithfully and one flags it, but the two sheets that quote the Half B row do not agree on its mandate; **(3)** the Pre-Trip says "no rename flagged" while the spec records the 2026-10-13 ruling, cites a line (extent L718) beyond the end of the file, and never names the Founding Register, the picks or the new partial inspiration research (spelled `Dumont_d_Urville` — a third spelling); **(4)** `Phase_4` calls another city's `11` row "a subnet-level figure"; **(5)** the usual line shifts; **(6)** source: the spec contradicts itself on the record extremes, the coldest-month figure, the polar night, and the monthly precipitation (sums to 404 mm against about 655).

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Janbogo subnet/Dumont_dUrville.md` (255 lines; `Step_-1` says 256, the builder's convention). `## Notable Locations` **L190**, `## Notable Figures` **L215**, Connection to Concordia **L221**, Current Status **L229**, Legacy **L239**; spec L3–9, L15–16, L18–44, L46–50, L58–71, L79, L81, L83, L89–98, L102–105, L108, L111–114, L120–131, L142–144, L162, L164, L176, L180, L194, L196, L217, L249 land on what the sheets say | ✅ |
| Census Section A heading **L280**, entry L282–286 (a tier table); Census I row **L506**; Census II row **L630** (retention "68.8248% → 68.8246%"); others L502, L715–716, L728, L748 | ✅ unchanged |
| Census I **201,194 H / 206,807 R / 408,001**; Census II **121,170 H / 159,635 R / 280,805** (the spec, `Step_-1`, `Step_0`, `Phase_2` agree with the live rows); overflow rows L715–716 (22,355 / 22,978 / 45,333 and 13,464 / 17,737 / 31,201) | ✅ |
| Extent rows **L57** (the pre-trim snapshot: 453,334 on 0.33 km² = 1,373,739/km²), **L211** (408,001 · ~47 km² · 8,681/km² · "maintenance"), **L652** (pool row) and the other lines L14, L85, L93, L179, L189, L214, L217, L254, L274, L405, L448, L505, L704 | ✅ (L94, L164 not in the list, **A-01**; L718 does not exist, **A-02**) |
| `16` Half B row (D 1.67 · workforce 341,560 · base 48.0 · MAND 0.0 · FREE 52.0 · src –), `16` §24 (baseline 163,966 · mandated 14,799 · FREE 162,794 · distinctive 177,593; shares 48.0 / 4.3 / 47.7 / 52.0), `09` L60 (1.67 · 223,549 · 453,334 · 138,692 · 341,560 · 40.6%) — the sheets quote them exactly | ✅ (but the figures are pre-trim, **S-08**) |
| `READER/Dumont_dUrville.md` (16 lines; "READER station: Dumont_Durville"; annual −11.0): the twelve monthly means equal the spec's Mean column; the sheets' L8 and the Pre-Trip's "its own header spells the key `Dumont_Durville`" (L3) both land | ✅ |
| Stations L20 (D10 Skiway); COMNAP pages **8** (index) and **46** (the entry) — page 45 names the city only inside another station's neighbor sentence; Cymatics_reverence L158 (a "not yet cross-referenced" open question); zero hits re-run: Meme Machine, True Believer, NMCI, Holidays, Energy grid, Weapons, Weapon_Item_Catalog, National Economy, Ice-Cold folder (7 files), jobs folder, Test_Runs tree (0 files), `06_Worked_Example_Provenance.md` (0), `11` (no city row); Factions: `Second_Interwar` L31, L33, L51, L53, L57 and `Cross_City_Cultural_Patterns` L149 only | ✅ |
| Topics L305–306; CrossSub L42–43, L55, L94, L160–161; Highways L56, L65, L88–97 (L88 and L361 are the highway's own name, "Dumont Coast Highway", not the city); Theoretical `Amundsen_Tower_Space_Fountain_Design.md` L991–995; Sweep row L155; universe-repo README L18 | ✅ |
| Pass README: spec `../../../Specs/Janbogo subnet/Dumont_dUrville.md` ✓, local culture ✓, vision notes ✓ (34 lines), research log `Dumont_dUrville_Research_Log.md` (does not exist yet) ✓, picks file ✓; every Pre-Trip source path exists; megasheet folder 7 entries (5 files + `README.md` + `Questline_Asset_Concept_Art/`, empty) | ✅ |
| Pre-Trip §C intro "19 files, all present"; §I `DATASHEET-NOT-YET-BUILT(N-5)=0`; no stub claim (the climate file is a real dataset) | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Highways L56, 65, 90, 92, 96–97 same; L226, 228, 233, 279 → **L227, 229, 234, 294**. Airports L47, 52 → **L50, 55**. Ports L129, 149, 154, 189, 193, 207, 218, 224, 232, 240, 244, 247, 249, 262 same; L363, 714, 770 → **L386, 737, 793**. RelDB L21, 30, 50 same; L143, 147–148, 154, 158–159, 197–199, 204 → **L154, 158–159, 165, 169–170, 208–210, 215** (the city's own entry is **L208–215**; L36 and the other "Dumont Coast Highway" hits are the road's name). NatConn L291 same; L409, 434, 442, 457, 473 → **L414, 439, 447, 462, 478**. `09` L60 same; L201 → **L203**. `16`: row **L278 → L279**; L183 same; L2206, 2431, 2452, 2460, 2496, 2597, 3086, 3565, 3569 → **L2211, 2436, 2457, 2465, 2501, 2602, 3091, 3570, 3574**; **not in the list at all:** L2432 (the §24 heading "DUMONT D'URVILLE — DETERMINED") and L2474. Extent: add **L94** and **L164** (the §5 heading "DUMONT D'URVILLE — RESOLVED 2026-09-05"). Add `Precipitation_Falls_vs_Lands.md` **L151** (the `Dumont_dUrville` row: 655 / 249 / 406) and L213 (the radar-measurement citation). Unchanged: census, CrossSub, Topics, Stations. | live greps | Re-read each list live (SH-012) |
| **A-02** | WRONG | **§A alias row cites the extent file at "L57, L718".** The file has 709 lines; the island's row is **L704** (also in the list). | `wc -l`; Extent L704 | Re-point |
| **A-03** | GAP | **Founding Register is not an address.** Row **L71** (Japan; geography and access; `DR-20`, `DR-44`; the last column lists the former founders as "French"), the ruling line **L90**, and **L94** (the 2026-10-13 cleanup that rewrote this spec's founding line). The Pre-Trip never names the file; `Step_1_and_2` and `Phase_2` cite "`Founding_Register.md`" with no line. | Register L71, L90, L94 | Add to §D Phase 2; add the lines |
| **A-04** | WRONG | **"No rename flagged — no 'rename' note in the spec header region."** The spec records the 2026-10-13 ruling at **L166** ("a city not settled by the French would have a different name; the new name is to be set in line with its founders, and is not yet chosen"). The check looked only at the header and searched the words *formerly · renamed · …*; the note uses "a different name". Memory holds the ruling (no name chosen, no sweep unprompted). | spec L166 | Replace with a pending-rename care-note; widen the search words |
| **A-05** | GAP | **Picks and the new inspiration research are not addressed in the Pre-Trip.** `Inspirational-Influences.md` heading **L30**, picks **L31–33** (Singapore [PRIMARY], San Miguel de Allende, San Miguel de Tucumán) — `Step_3` cites them correctly. `Research_Logs/Dumont_d_Urville_Inspiration_Place_Research_R1.md` (173 lines, 2026-10-26; **partial — stopped at pick 1 by the search limit, no box ticked**) exists, with `Reference/Real-World/Inspiration_Place_Research/inputs/Dumont_d_Urville.md` and `candidates/Dumont_d_Urville.md` — **spelled with an underscore between "d" and "Urville"**, which none of the Pre-Trip's spellings (`Dumont_dUrville`, `Dumont_Durville`, apostrophe forms) finds. `Step_3` says "`Research_Logs/` has no Dumont_dUrville file" — true of the log, not of the folder. | live | Register with a tier (DECIDE); add the spelling |
| **A-06** | NOTE | **Characters.** Pink Lucy (TBN [FW-25]) names this city as her origin: GDD `…/recruitable/TBN [FW-25 Pink Lucy]/README.md` L12, L56, L79–80 and the timeline repo's copy; the Palmer City self-defense candidate (TBN [SE-031]) lists it among three candidate origins (timeline repo: README L61, `Formative_History.md` L6; GDD: `PreWar_History.md` L20); a quick-capture seed `00d_Quick_Capture_Seed_…txt` L180, L186. `Phase_10` carries Pink Lucy and Akina and the Enneagram Index row (L24) correctly. The Pre-Trip's Phase 10 row ("actually run the check") has no names to check against. | grep | Register |
| **A-07** | NOTE | **Alias set** (confirmed in part): Dumont d'Urville · D10 Skiway · DdU · Petrel Island / Île des Pétrels · Géologie Archipelago · Adélie Land. Not listed: **Pink Lucy** and **St. Jules** as naming facts only; the road's name "Dumont Coast Highway" is a false positive (Highways L88, L361; RelDB L36; `16` L2223). `Station_to_City_Map.md` L80–87 names the city and is in no phase list (shared). | grep | Care-note |
| **A-08** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011: `Upper_Earth_Immigration_Composition.md` (this city's section) is not in Phase 2; the extent table is the 2026-09-05 snapshot (L211, L652, L57). | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ (a real dataset) · G3 `16` Half B ✅ (cited at the wrong line, **D-06**; figures pre-trim, **S-08**) · G4 Register row ❌ not an address (**A-03**) · G5 `Access type: ON` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3`, ❌ not in the Pre-Trip (**A-05**) · G8 census tier table ✅ · T2-8 extent ✅ in the Pre-Trip (rows L57, L211, L652; heading L164 missing), ❌ not in the sheets (**D-09**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals (201,194 + 206,807 = 408,001; 121,170 + 159,635 = 280,805); the 12 per-nation shares sum to **100.01%** (rounding); all four count columns sum **exactly** (Census I robots **206,807**, humans **201,194**; Census II robots **159,635**, humans **121,170**); the tier lists equal the table (2 / 5 / 5) and the tier totals are exactly the 8 : 3 : 1 share model (44.44 / 41.67 / 13.90 against 16 / 15 / 5 of 36 shares); monthly means average **−10.96 °C** (stated −11.0) and in every month Avg High > Mean > Avg Low and **Avg Low > Rec Low**; the trim arithmetic (453,334 × 0.9 = 408,001; overflow 45,333 and 31,201; density 408,001 ÷ 47 = 8,681; 453,334 ÷ 0.33 = 1,373,739); falls 655 − lands 249 = lost **406** (249 ÷ 655 = 38.0%); no polar night — recomputed from the physics: at 66°40′S with the −0.833° convention the solstice day length is **1.96 h** (spec "~1.9"); midnight sun recomputed at **about 33 days** against the spec's ~31 (Dec 7 → Jan 6), inside the method's tolerance.

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | WRONG | **Record extremes and coldest month contradict the monthly table.** L95 "coldest months (July/August) avg −22 °C" — the table gives July **−16.9** (Avg Low −20). L96 "record low approximately −40 °C; record high approximately +9 °C" — the table (and the Rec columns) give **−37.4 (Aug)** and **+11 (Dec)**; Denison's L191 (same station) was re-derived from the table, this city's was not. `Step_1_and_2` carries L96. | spec L95–96 vs L120–131 |
| **S-02** | WRONG | **L145 "polar night and midnight sun in near-minimal form — roughly ten days of each"** against L111–113 (no polar night; ~31 days of midnight sun; corrected 2026-09-04). | spec L145 vs L111 |
| **S-03** | WRONG | **The monthly precipitation column sums to 404 mm** (42 + 40 + 37 + 32 + 28 + 25 + 25 + 27 + 31 + 35 + 40 + 42) against the annual "~655 mm" that falls. The column is "derived" (L136). Denison's same-station column sums 657. | spec L120–131, L98 |
| **S-04** | NOTE | Peer-relative statements, none carried by the sheets except one (D-16): L83 (Mirny, Casey, Denison), L108 "22 of the 37 Tepenian cities are colder" (38 now), L110 "37-city comparison", L81 and L207 (Denison). | spec |
| **S-05** | NOTE | The de-stacking breaks the claimed ordering inside the tiers: South Korea (Significant) at **1.48%** is below four of the five Notable nations (NZ 4.16, Vietnam 4.04, Philippines 3.40, Malaysia 2.16); Thailand (Notable) is **0.14%** (285 robots, 278 humans). The tier totals are right. | spec L56, L58–71 |
| **S-06** | NOTE | The composition still lists **France** as a Significant nation (11.80%) for a Japan-founded city — consistent with the GPS law (composition names the stock), but worth a care-note while the rename is pending. | spec L49, L62 |
| **S-07** | NOTE | L166 holds the rename ruling (A-04); L162 and L164 are rewritten to the Register; L249 and L217 carry Pink Lucy. | spec |
| **S-08** | STALE | **`09` L60, `16` Half B L279 and `16` §24 still carry the pre-trim population.** `09`: humans 223,549 · residents 453,334 · required 138,692 · workforce 341,560 · 40.6%; `16`: workforce 341,560 (= 229,785 + 0.5 × 223,549), §24 worker counts 163,966 / 14,799 / 162,794 / 177,593 on that workforce. The census rows say the trim was 2026-09-05; the 2026-10-28 refresh of `16` Half B covered only the cities `DR-68` changed (the file's own header), so this city's row was never refreshed. At the live census the workforce is **307,404** (= 206,807 + 0.5 × 201,194). (Shared source; for the sweep.) | `09` L60; `16` L1, L279, L2432–2441 |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ spec header fields, extent, census cross-check (L506, L630); ❌ **D-02** (no later-era section table / overflow rows), **D-03** (garbled trim sentence), **D-17** |
| `Step_0` | ✅ census, source-stated retention; ❌ **D-01** (robot retention, spread) |
| `Step_1_and_2` | ✅ climate rows 17–27, Stations, COMNAP, Energy, founding rows; ❌ **D-04** (census range), **D-05** (record extremes), **D-06** (`16` row), **D-16** (peer clause), **A-03** |
| `Step_3` | ❌ **D-13** (README L39) and the research-folder claim (A-05); ✅ picks L30–33 |
| `Step_5` | ✅ |
| `Step_6`, `Step_9` | ❌ **D-14** |
| `Step_7`, `Step_8` | ✅ |
| `Step_10` | ✅ zero hits re-run; ❌ **D-12** (429 → 431) |
| `Phase_2` | ❌ **D-01**, **D-04**, **A-03** |
| `Phase_3` | ✅ every spec line, megasheet 7 entries |
| `Phase_4` | ✅ `09` L60 flagged correctly; ❌ **D-07** (another city's `11` row), **D-08** (`16` line) |
| `Phase_5` | ❌ **D-09** (lines, gateway-port gap) |
| `Phase_6` | ✅ (builder-convention counts, **D-17**) |
| `Phase_7` | ✅ Sweep, Theoretical, Factions notes; ❌ **D-08** (`16` §24 cites) |
| `Phase_8` | ✅ |
| `Phase_9` | ❌ **D-10** |
| `Phase_10` | ❌ **D-11** |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | WRONG | `Step_0` robot-retention and spread rows; `Phase_2` retention row | **Robot retention 77.17% and spread 16.94 pp are an arithmetic slip.** 159,635 ÷ 206,807 = **77.19%** (47,172 lost ÷ 206,807 = 22.81%); human 121,170 ÷ 201,194 = **60.23%** (right); spread **16.96 pp** (77.1903 − 60.2254). Combined 68.8246% (source-stated) is right. | Replace in both |
| **D-02** | GAP | `Step_-1` | Unlike Denison's and Cape Adare's, no table of the later-era sections by line range only: Connection to Concordia **L221–225**, Current Status **L229–235**, Legacy **L239–243**; and none of this city's overflow rows (census **L715–716**) or the vision-notes path row (`City_Vision_Notes/Dumont_dUrville.md`, 34 lines). | Add |
| **D-03** | WRONG | `Step_-1` · "Population-trim note" | "was 223,549 H+R I / 453,334 combined" — 223,549 is the **humans**; the pre-trim set was **223,549 H / 229,785 R / 453,334** (spec L42). The sheet also says "256 lines" (255 by `wc -l`, SH-009). | Reword |
| **D-04** | STALE | `Step_1_and_2` row 34; `Phase_2` row 1 | "`Official_Population_Census.md` **L280–284**" — the heading is L280 and the tier table is **L282–286** (the Notable row is L286). | Re-point |
| **D-05** | WRONG | `Step_1_and_2` · record extremes | Carries spec L96 ("~−40 °C … ~+9 °C"). The table gives **−37.4 °C (Aug)** and **+11.0 °C (Dec)**. | Replace; note S-01 |
| **D-06** | STALE | `Step_1_and_2` · `16` Half B row; `Phase_4` · cross-check row | Row cited **L278 → L279**. The row says MAND 0.0% / FREE 52.0%; `Phase_7` (rows 1–2) says §24 **replaces** the 0.0% with **4.3%** and FREE **47.7%** — two sheets of the same city disagree on the same row. Workforce 341,560 is the pre-trim value (live 307,404, **S-08**). | Add the replacement note; flag the pre-trim basis |
| **D-07** | WRONG | `Phase_4` · "`11` … per-city row" | "only a subnet-level Janbogo figure exists (124,985 / 31.2 Mt / 9.6×) … `11` L98" — **that is the city Janbogo's own marine-workers row** (the table's other rows are cities too: Cape Adare, Belgrano, Princess Elisabeth), not a subnet figure. This city has no row. It also reads another city's row. | Delete the clause |
| **D-08** | STALE | `Phase_4` row 3; `Phase_7` rows 1–7 | `16` row **L278 → L279**. `16` §24 cites are all one shift (+5): **L2427–2436 → L2432–2441; L2438–2454 → L2443–2459; L2475–2479 → L2480–2484; L2463–2471 → L2468–2476; L2481–2488 → L2486–2493; L2492–2495 → L2497–2500; L2496–2497 → L2501–2502.** (Content at each live range is what the row quotes.) | Re-point |
| **D-09** | STALE + GAP | `Phase_5`; `Step_-1`, `Step_0` | Highways **L226–233 → L227–234**, **L279 → L294**; Airports **L44–54 → L47–57**; Ports **L363, L714, L770 → L386, L737, L793**; RelDB header **L197–201 → L208–212**, notes **L204 → L215**. **Gaps:** the Port row omits the gateway facts the Pre-Trip lists — Hobart is the primary port for the Adélie Land site (Ports L144, L149: **2,682 km**, 5–7 days by icebreaker), "the nearest Tepenian port to Hobart" (L193), Torquay / Jan Juc 3,161 km and Outer Harbor 3,548 km (L232), voyages of 1,915 nm / 1,711 nm (L218); and no sheet carries the extent file's rows (L57, L164 heading, L211, L652). | Re-point; add; label the snapshot (SH-011) |
| **D-10** | STALE | `Phase_9` · Doll Representation row | "read firsthand in full, **32 lines**" — the file is **35 lines**. | Re-count |
| **D-11** | STALE | `Phase_10` · SE-031 row | timeline-repo `…Akina]/README.md` **L59 → L61** (Formative_History L6 is right). | Re-point |
| **D-12** | STALE | `Step_10` | "429-line file" — `06_Worked_Example_Provenance.md` is **431** lines (zero hits for "dumont" re-run). | Re-count (SH-009) |
| **D-13** | STALE | `Step_3` row 1 | "`Dumont_dUrville/README.md` L39 … 'may not exist yet'" — it is **L40**. The research-folder claim: see A-05. | Re-point |
| **D-14** | ADD | `Step_6` section 1 columns; `Step_9` | The Subnet column; item 5 — as CASEY-048 / CASEY-049. | As Casey |
| **D-15** | NOTE | `Phase_9` · "Robot_Universals" row | "zero hits … across the whole reference" ✓ (the Robot Physiology file also names no Dumont); the robot share **50.69%** (206,807 ÷ 408,001 = 50.6879%) is right. | none |
| **D-16** | NOTE | `Step_1_and_2` row 28 | "slightly further south than Mirny" — names another city (spec L83). | Delete the clause |
| **D-17** | NOTE | counts | "256" (spec: 255), "378-line" True Believer (377), "293-line" Meme Machine (292) — builder convention, SH-009. | per SH-009 |

### 2d. DECIDE items (collected)
1. **S-08** Refresh `09` L60, `16` Half B L279 and `16` §24 to the live (trimmed) population as was done for the `DR-68` cities (workforce 307,404), or label them pre-trim.
2. **S-01 / S-02 / S-03** Approve source edits in the spec: coldest-month line (L95), record extremes (L96), the polar-night line (L145), the monthly precipitation column.
3. **A-04** Add the pending-rename care-note to the Pre-Trip (the new name is not chosen; no sweep unprompted).
4. **A-05** The tier of `Dumont_d_Urville_Inspiration_Place_Research_R1.md`.
