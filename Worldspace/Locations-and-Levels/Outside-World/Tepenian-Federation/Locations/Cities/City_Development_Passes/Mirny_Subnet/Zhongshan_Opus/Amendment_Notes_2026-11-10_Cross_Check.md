# Zhongshan (Opus): amendment note for the cross-check (2026-11-10)

**What this is.** The fresh dated note for the finished-city cross-check of Zhongshan's Opus pass, run on 2026-11-10 under
`Universal_Location_Methodology/STARTUP_Finished_City_Cross_Check_Shirayuki_then_Zhongshan_2026-11-10.md` (plan: `DR-104` item 3,
moved forward by `DR-106`). For each place where the pass does not match its sources as they stand today, it names the pass
location and a neutral topic, and states the current fact with its source address (`DR-102`). Section F lists the conclusions
to test; section J will carry the first check's verdicts. **Everything here is PROPOSED** (`DR-101`, `DR-102`). **No pass file is
edited.** The `Zhongshan_Sonnet` trial folder is not opened (`DR-105` item 4; `DR-106`).
**Zhongshan on its own terms.** No other city is compared with it. A relation is taken only from Zhongshan's own lines
(`DR-122` item 5); any other location is named by role, "(another location: not used)". Fresh readers with clean briefs do the
checking (log Z-01).
**Replaces for this run:** `Amendment_Notes_2026-10-30_Manual_Input_Audit.md` (current as of 2026-11-03). That note stays; its entry
IDs (ZSO-nnn, SD-n, C1 to C7, U1 to U5) are kept here (`DR-102` item 3).
**How this note was built.** Every source line the 2026-11-03 note cites was re-read on 2026-11-10 (log Z-04). `git` shows no change
since that note's commit (`8777bb5f`) in the census, the spec, `09`, `11`, `16`, `Extent`, the Founding Register, the language files,
the alias table, the relationship database, `Ports`, `Highways`, `Airports`, `Geothermal`, the inspiration files, the culture file
or the pass folder; the rulings log grew by 216 lines after L1717 (rulings `DR-106` on). Counts in section B were recomputed by
script from `spec` L36-70 (log Z-04).

**Source key.** `Cities/` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. `ULM/` =
`Worldspace/Locations-and-Levels/Universal_Location_Methodology/`. `census` = `Cities/Official_Population_Census.md`. `spec` =
`Cities/Specs/Mirny subnet/Zhongshan.md`. `09`, `11`, `16` = `Cities/Division_of_Industry/09_Per_City_Baseline_Run.md`,
`11_Caloric_Rebuild_and_Livestock_Tier.md`, `16_Per_City_Three_Tier_Run.md`. `Extent` = `ULM/Extent_and_Density_Per_City.md`.
`rulings log` = `ULM/DEVELOPER_RULINGS_LOG.md`. `queue` = `Worldspace/Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md`.
`Ports`, `Highways`, `Geothermal` = `Locations/Infrastructure/*.md` beside `Cities/`. `startup` = the startup file named above.
`culture file` = `Cities/Local_Cultures/Mirny_Subnet/Zhongshan.md`. `shared table` = `Cities/Cross_City_Culture_Differentiation_Table.md`
(write-only in this run: only Zhongshan's own rows were extracted, by `scratchpad/zs/tools/own_rows.py`; no other row was read).

---

## A. Standing decisions (present-tense rules, with their dated words)

- **D-1 (developer, 2026-10-30; `DR-101`, `rulings log` L1673-1680).** *"yup, all as recommended"* (and, for Zhongshan, *"all as
  recommended"*, L1677). Rule in force: a finished pass's files are not edited; changes in its sources are recorded in its
  amendment note (L1678 item 1).
- **D-2 = ZSO-S01 (`DR-101` item 3; `DR-103` item 4).** The `Extent` rows are left in place. `Extent` L613 carries 1,203,607 people,
  120 and 172 km2; L593 gives the three-city Census I sum 3,330,740; L655 (127,944 and 99,668) is a dated scenario row.
- **D-3 = ZSO-S02 (`DR-101` item 3).** `16` section 18 (L1917, "ZHONGSHAN — DETERMINED") governs over the Half B row (`16` L275,
  source H).
- **D-6 (developer, 2026-11-03 night; `DR-105` item 4, `rulings log` L1711-1712).** Selections given: *"Divide by Census I share,
  labeled as arithmetic"* · *"Separate origins, as with every row"* · *"As arithmetic of the census"* · *"Yes, Zhongshan is a
  partner"* · *"Yes, correct both in place"* · *"Yes: a re-derivation uses the rulings as they stand"* · *"Opus is canonical; Sonnet
  stays as a trial"*. Recorded as (L1712 item 4): the Larsemann oasis rock (about 40 km2 for the three cities) is divided by Census I
  share, stated as arithmetic; the Russian-named rows are separate origins in every city; Zhongshan's retention rates are arithmetic
  of the census; Zhongshan is a partner in the joint agricultural research project (`DR-72`, `DR-75`); Zhongshan's spec L165 and L180
  are corrected; Zhongshan_Opus is canonical.
- **D-7 (developer, 2026-11-04; `DR-106`, L1723-1725).** *"add those cities to the tracker list and we'll go through them first."*
  The finished cities, Zhongshan (Opus) among them, are reviewed before the new runs, by `DR-104` item 3 (one reader per item;
  re-derive only what changes). Not decided (L1725): whether the Zhongshan Sonnet trial is reviewed at all.
- **General canon, developer 2026-11-09 (quoted in `startup` Section 4; the entries themselves are not opened in this run):**
  `DR-125` item 6 (language), `DR-127` item 2 (arrival after the signing), `DR-128` item 1 (the origin row), `DR-124` item 4 (records
  can draw people). Their words are quoted where each is used below.

## B. Population and the figures built on it

### ZSO-010 Headcounts (unchanged since 2026-11-03)

| Item | Current | Source address |
|---|---|---|
| Census I humans / robots / combined | 595,855 / 607,752 / **1,203,607** | `census` L502; `spec` L15 |
| Census II humans / robots / combined | 486,813 / 446,082 / **932,895** | `census` L643; `spec` L16 |

`census` L502 and L643 each carry the dated additions of `DR-68` (2026-10-28) and `DR-90` (2026-11-02), each marked "Arithmetic, NOT a
migration"; the −10% line of 2026-09-05 is marked "An authoring adjustment, NOT a migration — nobody left this city" (L502, L643).
Pass locations: as in the 2026-11-03 note, ZSO-010 (`00_Frame` L32-33, L124, L150-152, L180; `00.1` L44, L218, L221, L242;
`01_Inherited` L32; `04_Phase_02` L55-56; `04_Phase_04` L303, L315; `04_Phase_07` L151-152; `04_Phase_08` L349; `04_Phase_09` L101-102,
L127-128; `05_Reconciliation` L282, L417; `07_QA_Gates` L51; `04_Phase_06` L136).

### ZSO-011 Retention and mix (recomputed; unchanged since 2026-11-03)

Combined retention **77.51%** (932,895 / 1,203,607); humans **81.70%**; robots **73.40%**; spread **+8.30 pp**; not in Census II
**270,712** (22.49% of Census I). Robot / human share: Census I 50.49% / 49.51%; Census II 47.82% / 52.18%. National retention,
humans / robots: 67.12% / 69.71% (`census` L554, L694). **Standing rule (D-6):** Zhongshan's retention rates are arithmetic of the
census. Pass locations: as in the 2026-11-03 note, ZSO-011; shared output `shared table` L103 (Zhongshan's row carries "the `22.10%`
who went up").

### ZSO-012 Workforce and tiers (unchanged since 2026-11-03)

Workforce **905,680** (`09` L72; `16` L275). Requirement 323,017, 35.7% (`09` L72). Baseline / mandated / free **383,014 / 137,200 /
385,466** = 42.3% / 15.1% / 42.6% (`16` L1917-1923). Distinctive tier 522,666 (57.7%), mandated 26.25% of it (`16` L1925, L1932); the
robot term (9,572) is booked inside the baseline (`16` L1926). Phase 4's own formula (`09` L50) with B1 = 120.7 (`11` L292) gives
373,442 + 9,572 = 383,014. The free tier, 42.6%, lies inside the developer's 38 to 48% band (`16` L1934-1938). Pass locations: as in
the 2026-11-03 note, ZSO-012; shared output `shared table` L113 (Zhongshan's row carries "`15.4%` of the workforce").

### ZSO-013 Footprint, ice and rock (the rock now by ruling)

| Quantity | Current | Source address and computation |
|---|---|---|
| Zhongshan alone, area needed at 10,000 and 7,000 per km2 | **120.4 and 171.9 km2** | 1,203,607 / 10,000 and / 7,000; band `Extent` L84 |
| Three-city Census I sum (the oasis's three cities) | **3,330,740** | `census` L502, L505, L509; `Extent` L593 |
| **Zhongshan's share of the oasis rock, by Census I share (D-6)** | **36.136% of ~40 km2 = 14.45 km2** | 1,203,607 / 3,330,740; × 40 |
| Rock as a share of Zhongshan's footprint | **12.01% and 8.41%** (ice 87.99% and 91.59%) | 14.45 / 120.4 and / 171.9 |
| Gate 11's own method (one third of the oasis, 13.33 km2) | 11.08% and 7.75% | method at `07_QA_Gates` L59-63 |
| Three-city density on the 40 km2 oasis | 83,269 per km2 | 3,330,740 / 40 |

The division "by Census I share" is stated as arithmetic (D-6); `queue` L579-583 (`DRQ-11`, "who allocated the Larsemann Hills' ~40 km2
between three cities, or did nobody?") carries no recorded answer. Pass locations: as in the 2026-11-03 note, ZSO-013; also
`04_Phase_07` L475, L620, L917 (the oasis allocation as open; the pass does not divide the oasis) and `07_QA_Gates` L93.

## C. The composition table and the text about it

### ZSO-016 Composition table (recomputed by script from `spec` L36-70; unchanged since 2026-11-03)

| Item | Current |
|---|---|
| Rows and total | 35 rows, 99.986 by rounding; each row carries Census I and II counts for robots and humans; every row's robot and human counts are the same share of their population (to 0.01 point) |
| Tiers | Primary 1 row (Sinian Federation 35.83, "(founding wave)"); Significant 3 rows (Korea 9.70, Japan 7.30, Germany 7.10; 24.10); Notable 31 rows (40.056), 3.66 down to 0.013 (`spec` L20-22) |
| Small rows | 23 rows under 2%, 15 under 1%, 10 under 0.1% |
| Cumulative | three rows reach 52.83; ten rows 79.97; eleven rows 82.83 |
| Leader | 35.83 against 64.17 for the rest; 35.83 / 9.70 = 3.69 |
| Russian-named rows | twelve rows, 5.685 in all (Idelsk-Uralia 1.79, Russia (core state) 1.79, Siberia 0.71, Donska-Kubania 0.68, Künnarantaiga 0.41, six Caucasus rows 0.292, Tuva 0.013); Finland 0.021 is listed with them as a successor (`census` L857). **Standing rule (D-6):** separate origins |
| Other splits | Germany 7.10 + Austro-Bavaria 1.37 = 8.47 (`census` L862); Thailand 3.09 + Patani 0.09; Indonesia 2.86 + West Papua 0.061 + Aceh 0.059; Romania 2.58 + Hungary 0.30 (`census` L869-871) |
| Labels | Rows are written in their latest-period form (`DR-85` item 1, `rulings log` L1528); "the Sinian Federation" is the state's name where the period calls for it, the people are Chinese (`DR-21`, L575-587; Register `Cities/Founding_Register.md` L60) |
| "(founding wave)" | on the Sinian Federation only (`spec` L20); it means a founder named in the Founding Register (`DR-88`, L1555) |
| How the shares were set | the Sinian Federation's random multiplier did not apply to Zhongshan (`DR-85` item 3, L1528: Zhongshan is exempt, with one other location (not used)); Kazakhstan was not placed here (`DR-93`, L1602) |
| Standing of the figures | per-nation figures are weighting; the tiers and the city totals are the information; **no finding may rest on a within-tier difference**; robots and humans alike (`DR-12`, L463-475) |

Pass locations: as in the 2026-11-03 note, ZSO-016.

### ZSO-015 Spec text the pass leans on (two spec lines corrected by D-6)

- `spec` L165 now reads, of the Russian presence: *"(the twelve Russian-language successor rows total 5.685%, all in the Notable
  tier)"*. **`01_Inherited` L66-67 quotes this spec paragraph as it read before the correction** (a share of 5.72% and "its smallest
  Significant-tier nation"); that quotation no longer matches the spec.
- `spec` L180 now reads: *"Prydz Bay fishing and related industries, scientific research; commercial activity is modest and Zhongshan
  is not a trade hub (`Division_of_Industry/16` section 18)."* **`02_Spine` L45-50 flags this line as carrying withdrawn phrasing;**
  the flagged phrasing is no longer in the spec.
- Unchanged: the honorific sentence (`spec` L92); the Settled paragraph and the Jeju-do court's confirmation (`spec` L163, L173);
  Register row L60 (*"The Sinian Federation's (i.e. China's) immediate geographic and time-zone access to the site"*).

### ZSO-017 The Acts (unchanged)

`04_Phase_02` L153-160 describes the Act 1 date range as ending in the early 2600s. Current: Act 1 runs "2564 -> somewhere in the 2600s
(a hazy range)" (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md`
L105-106; no commit since 2026-10-01). `00.1` L60 carries the current wording.

### ZSO-021 Arrival after the signing (new; general canon of 2026-11-09)

Developer, 2026-11-09, `DR-127` item 2, general canon (quoted in `startup` Section 4): *"humans could continue arriving into Tepenia
after the signing. They just weren't allowed back to Upper Earth if they did"*. Recorded there as: humans could keep arriving after
the Falkland Treaty was signed; they could not go back to Upper Earth; whether robots kept arriving was not answered. The Treaty
text now carries it: Article II.2.5, *"Any human person who has not made the election described in paragraph 3 of this Article may,
at any time after the effective date of this Treaty, freely elect to take up residence within the Federation of Tepenia"*, with the
forfeiture of Article IV.2 (`Falkland_Treaty_Draft_v1.md` L50, L74-78; the draft's note at L138 dates the paragraph 2026-11-09;
Timeline commit `23e5226`). Path: `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md`.
Article II.2.1 (L46) makes every robot, present or later come into being in Assembly territory, depart to Tepenia. Pass locations
that rest on the opposite reading are listed in item C10 (section F).

### ZSO-022 The origin row and robots (new)

`DR-11` (L448-462, first recorded 2026-10-01, after the pass): robots carry a national origin, learned by immersion after coming
online; the composition tables' robot columns carry the same standing as the human columns. Developer, 2026-11-09, `DR-128` item 1,
general canon (quoted in `startup` Section 4): *"the "origin" row applies to both humans and robots, just at whatever percent makes
sense for them"*; recorded there as: an origin row covers both humans and robots, each at its own percentage. The spec's table still
gives robots and humans the same share in every row (ZSO-016). Pass locations: `04_Phase_02` L44-48 (LIMIT 1) and `04_Phase_08`
L130-134 (Guard 5); item C9.

### ZSO-023 Records can draw people (new; general mechanism)

Developer, 2026-11-09, `DR-124` item 4 (quoted in `startup` Section 4): the `DR-25` row headed "Records can draw people" (`rulings log`
L648) is a general mechanism any location may use. **No pass line was found that rests on it either way** (search of the pass's
numbered files for the station's records, logs, archives or translation, 2026-11-10, log Z-05). No item is opened for it.

## D. Language

### ZSO-018 Language (rule unchanged; general canon added 2026-11-09)

| Fact | Source address |
|---|---|
| The rule: Hawaiian (later Tepenian) is dominant everywhere; a city's supporting tier is every language group within 12 percentage points of its largest | `DR-100` (`rulings log` L1664-1672); developer's words `DR-89` L1563 and `DR-96` L1632; cutoff `Cities/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` L77 |
| Hawaiian is *"a Pidgin between a primary base of English and Japanese, with a supporting base of Korean, Tagalog, Ilocano, and Mexican Spanish. Later in the future, further influence from a wide variety of languages) resulted in Hawaiian later becoming Tepenian"* | developer, 2026-11-09, `DR-125` item 6, general canon (quoted in `startup` Section 4) |
| Zhongshan's groups: Mandarin 35.83; Korean 9.70; German 8.47; Japanese 7.30; English 4.94 to 10.90; Russian 3.59 to 5.685; Tatar and Bashkir 0 to 1.79 | `Cities/Research_Logs/Language_Blocs_By_City_2026-11-03.csv` L775-780, L790 |
| Supporting tier: Mandarin alone (35.83 − 12 = 23.83; no other group reaches it) | `Language_Sets_By_City_Reference_2026-11-03.md` L36 |
| `spec` carries no language field | `spec` (213 lines) |

Pass locations: `00_Frame` L48, L327, L350; `04_Phase_05` L155; `04_Phase_08` L806-856 (§8.8); `shared table` L125 (Zhongshan's
"Language / speech marker" cell). The pass names no language.

## E. Names, addresses, Pre-Trip

- **ZSO-014 Names.** Five pass places use retired names of other locations (`00.1` L48; `04_Phase_06` L129; `04_Phase_05` L56;
  `10_Readiness_Check` L40, L81, L100 and `04_Phase_08` L205, L207; `04_Phase_10` L82). Their current names are in
  `Cities/City_Renames_Alias_Table_2026-10-03.md` L11, L12, L102-105, L107 (another location: not used).
- **ZSO-019 Addresses.** Unchanged since 2026-11-03 (the 2026-11-03 note, section C). One cited source moved: the 12-point sentence
  of `Cities/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` is now at L25 (was L28); this note cites `DR-100` instead.
- **ZSO-020 Pre-Trip.** `00.0_Pre-Trip_Inspection.md` names `Zhongshan_Opus/09.6_Input_Audit.md`, which does not exist (2026-11-03
  count; folder listing 2026-11-10 agrees).
- **ZSO-001 to ZSO-006.** The dated Pre-Trip notes are unchanged; their current values are those of ZSO-010 to ZSO-013 above.
- **No datasheets.** The folder has a Pre-Trip and an input contract but no datasheets (`startup` Section 2 item 2; log Z-06).

## F. Conclusions to test (one reader each; no verdict stated here)

| ID | Pass location | Rests on | Current input and the rulings that bear on it |
|---|---|---|---|
| C1 | `04_Phase_08` L163-178 (shoulder and tail reading, R3), reused at L321-329, L388-390, L849-850 | the shape of the roster | ZSO-016: 3 Significant rows (24.10); 31 Notable rows, 3.66 to 0.013; three rows reach half, eleven reach 80%. `DR-12` (no finding on a within-tier difference); D-6 (Russian-named rows separate origins) |
| C2 | `04_Phase_08` L271-285 (rows too small to show, R7) | rows under the integration floor | 23 rows under 2%, 15 under 1%, 10 under 0.1% (`spec` L36-70); `DR-12` |
| C3 | `04_Phase_08` L232-250, L882-884, L947 (whether any origin assumes a polar climate) | the regions the roster spans | rows include Siberia 0.71, Künnarantaiga 0.41, Finland 0.021, Tuva 0.013 and six Caucasus rows (0.292) (`spec` L56, L58, L60, L63, L65-70) |
| C4 | `04_Phase_08` L880-890 (closing axis), L1041; `07_QA_Gates` L341-351 (Gate 4); `06_Differentiation` L121; `04.9_Step_4_Close-Out_Check` L155; `04_Phase_10` L374; Step 6 output `shared table` Zhongshan rows (write-only) | the plurality, the gap to second place, the tail shape | 35.83; 3.69 times the second row; tail as in C1; `DR-12` |
| C5 | `04_Phase_08` L806-856 (§8.8); `00_Frame` L48, L327, L350; `04_Phase_05` L155; `shared table` L125 (language cell) | the language facts | ZSO-018: Hawaiian dominant, a pidgin with a primary base of English and Japanese and a supporting base including Korean and Tagalog (`DR-125` item 6); supporting tier Mandarin alone (`DR-100`); `spec` has no language field |
| C6 | `04_Phase_02` L59-65; `04_Phase_09` L132-139, L396-398, L442; `04_Phase_05` L136-141; `01_Inherited` L88-116 (where the inversion between the censuses lies) | the census rows as in-world events | D-6: retention rates are arithmetic of the census; `census` L502, L643 additions marked "Arithmetic, NOT a migration"; ZSO-011 |
| C7 | `04_Phase_07` L160-179 (two derivations agree on the baseline) | which figures `16` contains | ZSO-012: `16` baseline 383,014 = Phase 4's formula 373,442 + the robot term 9,572 |
| C8 | `04_Phase_07` L475, L620, L917 (the oasis allocation open; the pass does not divide the oasis); `07_QA_Gates` L52-68, L93 (Gate 11; "at most a third"); `02_Spine` L279-293 (the rock as a class divide) | the division of the oasis being open | D-6: the rock is divided by Census I share, as arithmetic: 14.45 km2, 12.01% and 8.41% of the footprint (ZSO-013); `queue` L579-583, L602-606 (`DRQ-11`) |
| C9 | `04_Phase_02` L44-48 (LIMIT 1, robot figures a method); `04_Phase_08` L130-134 (Guard 5) | robot origin figures carrying no standing of their own | ZSO-022: `DR-11` (robots carry a national origin; robot columns same standing); `DR-128` item 1 (the origin row covers robots, at their own percentage); `DR-12` |
| C10 | `04_Phase_02` L215-224 (§2.5's last row and the block under it), L314; `04_Phase_08` L57, L343, L475, L830, L889; `04_Phase_09` L62; `04_Phase_05` L139; `05_Reconciliation` L117-120, L169; `shared table` L125 | no arrivals from outside after 2564 ("the door only opened one way"; "a closed system") | ZSO-021: `DR-127` item 2 (humans could keep arriving after the signing and could not go back; robots not answered); Treaty Article II.2.5 (L50, added 2026-11-09), IV.2.3 (L77), II.2.1 (L46) |
| U1 | `04_Phase_05` L89; `04_Phase_07` L255-280, L638 (what the city supplies; the technical mandate) | relations with other cities | Zhongshan is a partner in a joint agricultural research project with other locations (not used): `DR-72` L1386-1387, `DR-75` L1421 ("a partner's stake in the joint research project"), D-6; seed breeding and phosphorus and soil recovery, listed beside it at L1387 and L1421, are another location's own separate roles, not the project's (corrected 2026-11-10, log Z-14) |
| U2 | `04_Phase_08` L180-229 (pooling check: three candidate groups) | which groups could pool | a Russian-named group of twelve rows (5.685) and a German pair (8.47) are in the table (ZSO-016); Russian 3.59 to 5.685, Tatar and Bashkir 0 to 1.79 (`Language_Blocs` L780, L790); D-6: Russian-named rows are separate origins |
| U3 | `04_Phase_05` L323-333; `04_Phase_07` L421-425 (imports and the Ports file) | the gateways in `Ports` | `Ports` L129-130 (gateway assignments and the neutral transshipment route; other locations named there: not used), L202 (the Tri-Cities Port, Nella Fjord, 4,877 to 4,884 km), L229-230 (Hobart 4,877 km; Fremantle 4,817 km); `Cities/City_Relationship_Database.md` L495 |
| U4 | `04_Phase_05` L31, L250 (count of cities without geothermal heat) | the Geothermal file | `Geothermal` L38-39 and the open flag at L203-217 (a conflict with another location; options A to C not applied; the count 31 is 32 on the 38-city list, L205) |
| U5 | `03_Research` L36-58 (three inspiration picks) | the picks and later research on them | `Cities/Inspirational-Influences.md` L103-106 (Vilnius primary; Austin and Yekaterinburg secondary); `Cities/Research_Logs/Zhongshan_Inspiration_Place_Research_R1.md` (473 lines) and `_R2.md` (360 lines), 2026-10-26 |

## G. Source defects (two live sources disagree; neither chosen)

| ID | Statement and address | Against |
|---|---|---|
| SD-1 | `Extent` L577 gives 353 to 504 km2 and 89 to 92% on ice; `Cities/Division_of_Industry/05_Remaining_Cities_Assessment.md` L158, L193 give the three-city sum 3,527,096 | `census` L502, L505, L509: 3,330,740 (333 to 476 km2; 88.0% to 91.6% on ice) |
| SD-3 | `culture file` L22-24: China Primary; five Significant nations; twelve Notable | `spec` L20-22 |
| SD-4 | `culture file` L110: Mandarin is the city's sole public language | `DR-100`: Hawaiian is dominant everywhere |
| SD-5 (new) | `culture file` L23 tags Australia "(founding wave)"; L38 says Australian exiles "formed the founding wave of non-Chinese settlers" | `spec` L20 (the tag on the Sinian Federation only); `DR-88` L1555 (the tag means a Register founder); Register L60 |
| SD-6 (new) | `queue` L579-583 (`DRQ-11`) still asks who allocated the rock, with no recorded answer | D-6 (`DR-105` item 4) divides the rock by Census I share, as arithmetic |

## H. Open questions

1. **DEC-004** (2026-11-03, open): may the culture file be corrected (SD-3, SD-4)? SD-5 is new and belongs with it.
2. **Zhongshan's Element: Metal, kept by the developer on 2026-11-10 (`DR-135`); Saturn + Metal stands.** The one-word label stays provisional (`DR-1`).
   *(Open since 2026-09-23, `DR-1` L134; closed here.)*
3. Whether the Pre-Trip and datasheets are built for this pass (`DR-101` item 5); the builders' answer is in log Z-06.

## I. Checked, no mismatch (later-rulings scan, 2026-11-10)

Rulings named for Zhongshan in `startup` Section 1 item 3, plus every ruling after `DR-105` except the closed `DR-124` to `DR-128`
(their general canon is quoted in `startup` Section 4): `DR-21` (L575-587) and `DR-31` (L730), the founding rests on access: the pass
cites the Register and the access ground (`00.1` L60). `DR-26` (L664), Zhongshan's row: the pass's `05_Reconciliation` L434 (`R-24`)
records it as ruled on 2026-10-01. `DR-47` (L976): the Register count names Zhongshan's founder as China. `DR-93` (L1602): Kazakhstan
not placed here. `DR-106`: section A, D-7. `DR-107` to `DR-123` and `DR-129`: no Zhongshan-specific item; `DR-114` item 3
(symbols depend on the location itself) is general; `DR-1` L134 records that the pass's symbol declaration was re-derived on
2026-09-23 (see H.2).

## J. The first check's verdicts

One fresh reader per item (dispatched 07:00; all returned by 07:09). Each verdict line is as `grep` returns it from the reader's
output; each Round 2 result is the verifier's verdict line (`Tools/triple_read_verify.py`, last committed 2026-11-03; the reader's
single proof file passed as all three arguments). The outputs, Round 2 runs, briefs and lists are beside the pass as
`.xc_20261110_item_<ID>*` (log Z-12). **These verdicts are PROPOSED;** the pieces named re-derive each item that narrows or flips.

| Item | Verdict line (line in the output) | Round 2 | Output beside the pass | Questions raised | Piece |
|---|---|---|---|---|---|
| C1 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C1.md` (178 lines) | C1-Q1, C1-Q2 | P08A_Composition |
| C2 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C2.md` (184 lines) | C2-Q1, C2-Q2 | P08A_Composition |
| C3 | `VERDICT: NARROWS` (L7) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C3.md` (221 lines) | C3-Q1, C3-Q2, C3-Q3, C3-Q4 | P08A_Composition |
| C4 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C4.md` (270 lines) | C4-Q1, C4-Q2, C4-Q3, C4-Q4 | P08A_Composition |
| C5 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C5.md` (278 lines) | C5-Q1, C5-Q2, C5-Q3, C5-Q4, C5-Q5, C5-Q6 | P08B_Language |
| C6 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C6.md` (234 lines) | C6-Q1, C6-Q2 | P02_Arrival |
| C7 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C7.md` (115 lines) | C7-Q1 | P07_Order |
| C8 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C8.md` (233 lines) | C8-Q1, C8-Q2 | P07_Order |
| C9 | `VERDICT: NARROWS` (L7) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C9.md` (175 lines) | C9-Q1 | P02_Arrival |
| C10 | `VERDICT: FLIPS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_C10.md` (300 lines) | C10-Q1, C10-Q2, C10-Q3, C10-Q4 | P02_Arrival |
| U1 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_U1.md` (218 lines) | U1-Q1, U1-Q2, U1-Q3, U1-Q4, U1-Q5 | P07_Order |
| U2 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_U2.md` (208 lines) | U2-Q1, U2-Q2, U2-Q3 | P08A_Composition |
| U3 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_U3.md` (217 lines) | U3-Q1, U3-Q2 | P07_Order |
| U4 | `VERDICT: HOLDS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_U4.md` (146 lines) | U4-Q1, U4-Q2, U4-Q3 | none (holds) |
| U5 | `VERDICT: NARROWS` (L4) | "UNANIMOUS - CLEARED TO WRITE" | `.xc_20261110_item_U5.md` (112 lines) | U5-Q1, U5-Q2, U5-Q3, U5-Q4 | P03_Research |

### J.2 The pieces (PROPOSED)

Each piece ran three readers (Round 2 unanimous on the first run; Round 3, six cross-verdicts CONSISTENT), one merge writer, and
the merge checks; its round record gives every tool output. Wave 2 (the last two rows) ran after `P02_Arrival` was merged and
checked (`DR-107`). Item U4 holds and has no piece.

| Piece | Items | Lines | `sha256` | Round record |
|---|---|---|---|---|
| `P02_Arrival` | C10, C6, C9 | 844 | `455c82aeffbeb130` | `Amendment_Rederivation_P02_Arrival_2026-11-10b_T8_Rounds.md` (215 lines) |
| `P07_Order` | C7, C8, U1, U3 | 839 | `96e6212988e74d47` | `Amendment_Rederivation_P07_Order_2026-11-10b_T8_Rounds.md` (240 lines) |
| `P03_Research` | U5 | 506 | `503cd4a261df2fe1` | `Amendment_Rederivation_P03_Research_2026-11-10b_T8_Rounds.md` (152 lines) |
| `P08A_Composition` | C1, C2, C3, C4, U2 | 1159 | `7aefdb339015a5c0` | `Amendment_Rederivation_P08A_Composition_2026-11-10b_T8_Rounds.md` (225 lines) |
| `P08B_Language` | C5 | 783 | `0c76f24205437ca0` | `Amendment_Rederivation_P08B_Language_2026-11-10b_T8_Rounds.md` (177 lines) |
| `P07B_Imports` (after the developer's answer, `DR-130` item 6) | U3 | 661 | `c27b8e24c2cc7ec2` | `Amendment_Rederivation_P07B_Imports_2026-11-10b_T8_Rounds.md` (158 lines) |
| `P07C_Imports` (after `DR-133`) | U3 | 810 | `8c887322f9d0e906` | `Amendment_Rederivation_P07C_Imports_2026-11-10b_T8_Rounds.md` (160 lines) |

**Current fact added 2026-11-10 after the pieces (`DR-134`):** the coastal supply line's sea leg is seasonal, as in reality (by sea only about late November to mid-March; by highway all year); the `P07C_Imports` piece's open slot for the sea leg takes this answer. Australia is a four-node partner with the Tri-Cities' Nella Fjord port (`DR-133`; `Ports.md` L129).
