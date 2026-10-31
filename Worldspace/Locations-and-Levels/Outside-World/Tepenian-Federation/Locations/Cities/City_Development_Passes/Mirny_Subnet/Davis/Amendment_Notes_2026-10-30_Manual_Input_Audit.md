# Davis — amendment notes, 2026-10-30 (manual input audit)

**What this file is.** Davis's pass was run and closed on 2026-09-16 (last substantive change 2026-10-01). **No pass file is edited by this note, and none was.** Each entry below says what has changed in one of Davis's sources since the pass, where the pass (or its sheets) rests on the old state, and the live figure as it stands on 2026-10-30. **Every figure or claim quoted from a pass file is as recorded at the pass; the source has since changed.** The pass stays the record of what it worked from.

**Limit, stated plainly.** The 24 pass files were not re-read line by line. The places listed below were found by searching the pass files for the old figures and phrases (counts are lines per file), so an occurrence worded differently may exist that this note does not list. Nothing here classifies, rules on or re-derives a finding; it only records the change and points to the live source.

**Not decided here.** Whether the datasheets should show the old values labeled as dated or the live values (`DV-011`), whether the conclusions inside the sheets are kept as a record (`DV-020`), and the two source corrections in the ledger (`DV-S01`, `DV-S02`) wait for the developer. Entries use the ledger's IDs; evidence is in `Manual_Input_Audit_2026-10-29/Davis_Audit.md` and `FIX_LEDGER.md`.

---

## DV-001 — The census scenario of 2026-10-28 (`DR-68`) rescaled Davis's population; shares did not change

**What changed.** The adopted Santa Luce population scenario raised Davis's Census I by +12,139 humans and +11,778 robots, and its Census II by +8,108 and +7,739 (`Official_Population_Census.md` L494 and L617; the spec `Specs/Mirny subnet/Davis.md` L15–16 carries the same counts). The spec's per-nation counts were rescaled to the new totals; the per-nation shares are unchanged (for example China stays at 19.04%, the figure `02_Spine.md` records as the largest).

**Live figures (2026-10-30), with the old figure as recorded at the pass.** Arithmetic below was done by hand and checked a second time.

| Figure | At the pass | Live | Source / working |
|---|---|---|---|
| Census I humans · robots · total | 563,599 · 594,715 · 1,158,314 | 575,738 · 606,493 · **1,182,231** | `Official_Population_Census.md` L494; 575,738 + 606,493 = 1,182,231 |
| Census II humans · robots · total | 437,423 · 344,173 · 781,596 | 445,531 · 351,912 · **797,443** | same file L617; 445,531 + 351,912 = 797,443 |
| Retention, combined | 67.48% | ≈ 67.45% | 797,443 ÷ 1,182,231 = 0.67452 |
| Retention, humans | 77.61% | ≈ 77.38% | 445,531 ÷ 575,738 = 0.77384 |
| Retention, robots | 57.87% | ≈ 58.02% | 351,912 ÷ 606,493 = 0.58024 |
| Spread (humans − robots) | 19.74 pp | ≈ 19.36 pp | 77.384 − 58.024 = 19.36 |
| Robots' share of Census I | 51.34% | ≈ 51.30% | 606,493 ÷ 1,182,231 = 0.51301 |
| Density on the 410 km² administrative extent | 1,158,314 ÷ 410 = 2,825.16 per km² | ≈ 2,883.49 per km² | 1,182,231 ÷ 410 = 2,883.49 |
| Humans departed (Census I − Census II, humans) | 126,176 = 22.39% of 563,599 | 130,207 ≈ 22.62% of 575,738 | 575,738 − 445,531 = 130,207; ÷ 575,738 = 0.22616 |
| People gone, Census I → II | 376,718 | 384,788 | 1,182,231 − 797,443 = 384,788 |
| `09` row (required workforce · workforce · share) | 309,368 · 876,515 · 35.3% | 315,832 · 894,362 · 35.3% | `09_Per_City_Baseline_Run.md` L79 (header L52); 606,493 + 575,738 ÷ 2 = 894,362 |
| `16` Half B row (workforce · base %) | 876,514 · 40.7% | 894,362 · 40.8% | `16_Per_City_Three_Tier_Run.md` L262 (header L247) |

**Where the pass rests on the old figures** (lines containing the figure, per file):
- Census I total 1,158,314: `00.1_Step_MINUS-1_Input_Contract` (3), `00_Frame` (5), `02_Spine` (2), `03_Research` (1), `04_Phase_02` (2), `04_Phase_04` (2), `07_QA` (1), `README` (2); also `00.0_Pre-Trip_Inspection` (1: the quotation of the `DR-4` ruling, left as that ruling's record).
- Census II total 781,596: `00.1` (2), `00_Frame` (2), `01_Inherited` (1), `02_Spine` (1), `04_Phase_02` (3), `07_QA` (1); also the Pre-Trip (1, the same ruling quotation).
- The four component counts (563,599 · 594,715 · 437,423 · 344,173): `00.1`, `00_Frame`, `04_Phase_02`, `04_Phase_09` (all four); `04_Phase_04` (563,599 only).
- Retention figures (67.48 · 77.61 · 57.87 · 19.74): `00_Frame`, `00.1`, `02_Spine`, `04_Phase_02`. Robots' share 51.34%: `00_Frame`, `02_Spine`, `04_Phase_02`, `04_Phase_04`, `04_Phase_08`. Departure figure 126,176 / 22.39%: `00_Frame`, `02_Spine`, `04_Phase_02`. The 376,718 total: `00_Frame`, `01_Inherited`, `02_Spine`, `04_Phase_02`.
- The density 2,825 per km²: `02_Spine` (2), `README` (1).
- Workforce 876,51x: `04_Phase_04` (3), `04_Phase_07` (2), `04_Phase_08` (1), `04_Phase_10` (2), `07_QA` (2). Required workforce 309,368 and base 40.7%: `04_Phase_04` (2 each).

**What stands.** The findings that rest on ratios (retention, the human and robot components, density, the robots' share) move by 0.03 to 0.4 percentage points, or about 2% for the density and the people-gone totals; the order of the retention figures is unchanged (humans retain more than robots) and robots are still just over half of Census I. **None of the shares changed.** `16` §19's worker counts were not recomputed (see `DV-006`).

---

## DV-002 — Phase 5's air claim is wrong, not just old: Davis has no air access

**What the pass says.** `04_Phase_05_Relation_and_Geometry.md` L23 (source table, row 3, `Airports.md`): "Davis holds a confirmed airport marker"; L203 (arrival types, type 3, "By air"): the same words. L196 introduces the arrival types as "four", so the enumeration carries a "by air" type on this premise; L345 (the Phase 10 handoff row) names "the airport" among the nameable relational features, with "None named here".

**What the source says (live).** `Infrastructure/Airports.md` lists Davis in "Everything Else Has No Air Access — all 23, named" (heading L40; the list is L50–52, Davis on L50), and the note that follows says many of those cities have a real-world station with a genuine airstrip today and that none of them has one in Tepenia (L54–56; Davis is named on L55); access is by the highway network only (L57–58). No marker for Davis exists among the file's thirteen.

**Related, added 2026-10-29.** `DR-82` placed the onward flights of winter arrivals at Mirny, not Davis (`Airports.md` L12), and added a "Winter Intake Airport" row (L23; intro L3) that is not a city and whose unruled map marker is placed "between Davis and Mirny". Neither gives Davis an airport.

**What stands.** Road (Hwy 110) and seasonal sea (Prydz Bay) are unaffected. The statement about air in the pass is as recorded at the pass; the source says otherwise.

---

## DV-003 — Davis's symbol pair was blanked on 2026-09-16

**What changed.** On 2026-09-16 the developer ruled, for Davis's symbol pair: "for now, for the current time, we can just make that blank", adding that it should not be filled from the breadbasket reading because Davis is also a port city and the symbol is open. `City_Symbolic_Substrate/City_Symbol_Assignments.md` shows Davis's row as BLANK at **L112**, records the earlier Earth / Earth pair as superseded at **L335–341**, and names Davis at L71 among the four cities that keep their entries. (The row was at L92 on 2026-09-11.)

**Where the pass rests on the old pair** ("Earth / Earth", with the standing built on it: Planet half ratified and readable, Element half reserved under `DR-1`):
- `00.1_Step_MINUS-1_Input_Contract.md` L133 (and the Element-half passage that follows at L141);
- `00_Frame.md` L292 (the symbol-assignment row) and L312 (reserved item 5, the Element half's meaning);
- `02_Spine.md` L416;
- the Pre-Trip `DR-1` block, which already carries a dated update (2026-10-21) and was given the live rows on 2026-10-30.

**What stands.** The reservation against reading a meaning off the bare word "Earth" is a rule about not reading meaning off names; it does not depend on the pair. Whether the pair stays blank, or is later set from Davis's own Phase 10, is the developer's (the symbol file notes that the determination "starts from a blank slate").

---

## DV-004 — Station-heritage and namesake rulings of 2026-10-01 (`DR-19`, `DR-24`, `DR-25`, `DR-32`)

**What changed.** On 2026-10-01 (commit `67d091af`) the spec's Significance line (L8) lost the phrase "Australian Antarctic Division heritage", and the Developer-vision paragraph (L143) was edited in the same commit. The live Significance line still says Davis "shares Australian founding-wave heritage" with Casey and Mirny, as the spec does again at L129.

**Check run 2026-10-30 (search only).**
- "Australian Antarctic Division" occurs in the 24 pass files once: `00.0_Pre-Trip_Inspection.md` L25, the real-world basis name in the alias table. The removed phrase "Australian Antarctic Division heritage" occurs in none.
- "AAD" occurs at `00.1` L269 (the contract's classification of spec L62, which still says the Division has operated the station since 1957) and `04_Phase_03` L36 (the climate data's authority).
- "Australian-heritage" occurs in `04_Phase_05` (L36, L105, L114, L305, L330, L346) only as the flagged, withheld-source material described below.

**Flags that must stay.** `City_National_Connections.md` L304–306 and `City_Cross_Subnet_Relationships.md` L123–131 (the Davis–Mawson connection; the second file cites a withheld megasheet at L125) and L139–147 (the real-world namesake detail) rest on a withheld source and on a namesake story; the pass flagged all of it and extracted none (`04_Phase_05`; `00_Frame` §0.5 reserved item 1). Whether to rewrite those two source passages is the developer's (ledger `DV-S02`). This check (search only) found nothing to correct in the pass files.

---

## DV-005 — The spec grew past the range the Step −1 contract classified

**What changed.** `Specs/Mirny subnet/Davis.md` is **236 lines** (`wc -l`, 2026-10-30; 236 since the commit of 2026-09-16 that added the port ruling). The contract (`00.1` §4.1 admitted ranges, §4.3 excluded ranges; and `00.1a`, which describes the file as 181 lines) classifies **L1–181 only**.

**Unclassified by the contract: L182–236.** Live headings: Economy & Industry continues to L206 (it begins at L147; L148, L153–155, L176 and L178–179 are in the admitted set); Notable Locations L207; Notable Figures L215; Connection to Concordia L220; Legacy L225; Open Questions L230.

**What this note does not do.** It does not classify those lines. Under `05` §6.1a, "outside the frame" is decided line by line, and a range may be excluded only after each span inside it has been classified; that is an act of Step −1, to be run if the pass is ever reopened. The contract has not ruled on those lines in either direction.

---

## DV-006 — `16`: Half B was refreshed, §19 was not; the 28.2% / 31.1% ruling lives only in §19

**What the source says (live).**
- Half B row (`16` L262, header L247): workforce 894,362 · base 40.7% → **40.8%** · MAND **20.7%** · FREE **38.5%** · src C. Refreshed by `DR-68` on 2026-10-28 with "mandate shares held", so the workforce and base % changed and the MAND / FREE pair did not.
- §19 (heading L2006): baseline 357,063 (40.7%), mandated 246,740 (28.2%), FREE 272,712 (31.1%), summing to 876,515 (357,063 + 246,740 + 272,712). The developer's ruling of 2026-09-16 is at **L2073–2076**: "Mandate 28.2% / free 31.1%", Option B stands. The file's first line states the per-city determinations were **not recomputed** after `DR-68`.
- The Option A alternative precomputed at `16` L3568 is mandate 20.7% / free 38.5%, which is the pair Half B still shows.

**Which governs.** For the mandate and free shares, the ruling in §19 (28.2% / 31.1%) governs; Half B's MAND / FREE pair is the first-pass split of 2026-09-02, and the pass already uses the ruled pair (`Datasheets/Step_1_and_2.md`, the "two figure-pairs" row). For the workforce and base %, Half B's row (894,362; 40.8%) is the current one; §19's worker counts are on the earlier workforce and re-run when the baselines are re-run (`16` L1287–1304). `04_Phase_07_Order.md` and `Datasheets/Phase_4.md` quote §19 and Half B as recorded at the pass. Whether Half B should itself say the ruling supersedes it is ledger `DV-S01`, for the developer.

**Pass citations into `16` that no longer land where they did.** `04_Phase_07_Order.md` (L31, L47, L251, L355, L426) and `04_Phase_10_Catalog.md` (L35, L43, L444) cite `16` by line; several match the file as it stood on 2026-09-06 or 2026-09-16, and none lands on the same line now. Live anchors, re-read 2026-10-30: Half B Davis row **L262** (header L247; cited L261); §19 heading **L2006**, the research-half argument and the ruling **L2033–2078** (cited L2028–2073); "Register item 11" block **L2089–2095** (cited L2056–2062); the Vestfold Hills sentence, §19 Notes **L2099–2100** (cited L2066); the namesake line **L2101** (cited L2068); the kinship note **L2103–2105** (cited L2070–2072); the other city's passage that contains the "100 Miles Davis Boulevard" false positive **L1575–1592**, the boulevard sentence **L1592** (cited L1570–1587, L1587; the city is not named here, as in the pass); the Davis row of the open-items table **L3568** (cited L3563 in the sheets).

---

## DV-007 — `DR-75` (Relung Panen): Davis is named as the national agricultural-research half

**What changed.** `Division_of_Industry/18_Relung_Panen_Determination_2026-10-29.md` names Davis in two places. L31 (the mandate table): Relung Panen's agricultural-research row is "A partner's stake in the joint research project with Davis, Ariun Nuur and Zhongshan. Davis holds the national research half". L48 (the result): a figure for Davis's share of export supply (39.6%, `17` section 5, convention B).

**Where it touches the pass.** `04_Phase_07_Order.md` treats the half-mandated research sector as part of Davis's determination (L175–178, L251–253; the source is `16` §19, L2033–2078). This is a cross-reference only: file 18 names Davis as holder of the national research half and adds a named joint project with Ariun Nuur and Zhongshan. **No change to Davis's own figures.** The 39.6% is an export-supply share of the kind the Davis sheets mark as not citable as an export headcount (`Datasheets/Phase_4.md` header, `Phase_7.md` row 2).

---

## DV-008 — Lines in `Highways.md`, `Ports.md` and `Airports.md` (and three neighbors) moved after the pass

The pass cites these files by name; its sheets cite them by line. Live positions, 2026-10-30:

| File | Davis lines now | Note |
|---|---|---|
| `Infrastructure/Highways.md` | L199 (Hwy 110: "Zhongshan → Davis → Mirny → Casey → Concordia") | The note first cited at L318 ("`Ports.md` EMPTY (0 bytes)") now stands at **L349**; live L318 is a different passage |
| `Infrastructure/Ports.md` | Davis row **L559**; the CONSTRUCTED tier list **L736** | The sheets cited L536 and L713. The file also now names Davis at L130, L201, L224 and L795 (neutral-transshipment and distance material) |
| `Infrastructure/Airports.md` | **L3**, **L23** (Winter Intake row), **L40** (heading), **L50**, **L55**, **L57** | See `DV-002` |
| `City_Relationship_Database.md` | Davis's entry **L186–187** | Was L175–176 until the edit of 2026-10-21 that followed the Pre-Trip refresh |
| `City_National_Connections.md` | Davis's section **L303–315**; the Davis–Mawson passage **L304–306**; the Casey and Mirny rows L307–308 | `04_Phase_05` cites L296–308 and L296–299 |
| `City_Cross_Subnet_Relationships.md` | Hwy 110 routing L53–54; Davis–Mawson L123–131 (withheld-source citation L125); the intra-subnet network bullet L128–131; the namesake paragraph L139–147; the vignette flag L232 | `04_Phase_05` cites L125–133, L127, L130, L139–147, L233–234 |

**Not assessed.** `Airports.md` L3 and L23 name Davis only as the placement of an unruled marker (see `DV-002`); the `Ports.md` mentions at L130, L201, L224 and L795 are cited by no pass file and have not been weighed against the pass.

---

*Filed 2026-10-30 by the manual input audit sweep. Companion record of the sheet edits: `Manual_Input_Audit_2026-10-29/Sweep_Reports/Davis_Sweep.md`.*


---

## Developer decisions at the walk-through (2026-10-30)

*"yup, all as recommended"* (Davis items 1–5). No pass file was edited. Edits were made only to the Pre-Trip and the datasheets, each marked as a dated record.

- **`DV-011` — population figures.** The sheets keep the figures the pass used and now show the live figures beside each one, marked "as recorded at the pass (2026-09-16)": Census I 575,738 H / 606,493 R / 1,182,231; Census II 445,531 H / 351,912 R / 797,443; retention combined 67.45%, human 77.38%, robot 58.02%, spread 19.36 pp (derived by hand: 797,443 ÷ 1,182,231 and so on); robots 51.30% of Census I; density 1,182,231 ÷ 410 = 2,883.49/km²; `09` L79 (Required 315,832, Workforce 894,362, 35.3% unchanged); `16` L262 (workforce 894,362, base 40.8%). Touched: `Step_-1`, `Step_0`, `Phase_2`, `Phase_4`, `Phase_9`, `Step_1_and_2` and the Pre-Trip. Left as a dated ruling: the Pre-Trip's quotation of `DR-4` ("1,158,314, not 781,596").
- **`DV-020` — conclusions written inside the sheets.** Kept as a record. They are the pass's own interpretations and must be stripped before the sheets are reused for a new run of Davis.
- **`DV-S01` — which split governs.** Davis's own ruling governs: `16` §19 (L2006) rules mandate 28.2% · free 31.1% (Option B). Half B's 20.7% / 38.5% is the first-pass split of 2026-09-02. `16` itself is untouched (its line numbers are cited everywhere); `Phase_4` and `Step_1_and_2` quote both and say so. §19's worker counts predate `DR-68`.
- **Corrections inside the sheets:** `Phase_5` Ports row marks the "road and air" wording as a record of text the 2026-09-16 port ruling replaced; `Phase_5` Airports row no longer quotes the later-era marker row (`Airports.md` L23); `Phase_7` row 12 no longer calls the `10_Validation_Findings` sentence a live violation (the line carries a correction dated 2026-09-26); `Phase_7` row 2 cites the `README` "First results" heading at L184 and the Davis line at L186; `Phase_2` cites the geography parenthetical at L390; Pre-Trip §K notes that the named ledger file does not exist; the Pre-Trip's Phase 2 `T8` line says 4 admissible rows.
- **`DV-S02` — the two relationship passages.** Re-grounded 2026-10-30 after the developer approved the drafted wording ("all as recommended"): `City_Cross_Subnet_Relationships.md` L123–131 and `City_National_Connections.md` L274–278, L293–295, L304–308 now rest on the Founding Register and Hwy 110 instead of naming heritage, the culture megasheet's heritage claim and the namesake story. Ratings and types unchanged; line counts unchanged (241 and 603). `City_Cross_Subnet_Relationships.md` Part 3 (L139–147) is untouched and still refers to "the existing 'shared naming heritage' treatment (Part 2)".
