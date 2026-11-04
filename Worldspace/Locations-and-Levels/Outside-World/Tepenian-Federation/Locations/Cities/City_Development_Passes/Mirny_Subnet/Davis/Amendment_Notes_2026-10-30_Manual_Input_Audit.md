# Davis: amendment notes (current as of 2026-11-03)

**What this is.** A record of where Davis's pass text does not match the sources as they stand on 2026-11-03, and what those sources say. It also carries Davis's standing developer decisions in the present tense (section "Standing decisions").
**No pass file has been edited.** Compared: the 24 pass files and `README.md`. The Pre-Trip, ledger and datasheets are support files; they appear only where a standing decision names them.
**How an entry is built:** the pass location (file and line, with a neutral description of the topic), then the current fact, then the source address. Every figure is read from the live source (2026-11-03) and every derived figure is recomputed by command.
**Pass dates:** run 2026-09-14 to 2026-09-16, complete; last edit 2026-10-01. **Limit:** pass locations come from pattern search, not a line-by-line re-read, so a differently worded occurrence may exist.
**IDs:** DV-001 to DV-008, DV-011, DV-020, DV-S01 and DV-S02 are cited by other files and keep their numbers. New entries start at DV-021 (the numbers between DV-008 and DV-021 belong to ledger items for other files).

---

## Paths and rulings named in this note

`CITIES` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`. `ULM` = `Worldspace/Locations-and-Levels/Universal_Location_Methodology/`. `SPEC` = `CITIES/Specs/Mirny subnet/Davis.md`. `CENSUS` = `CITIES/Official_Population_Census.md`. `LOG` = `ULM/DEVELOPER_RULINGS_LOG.md`. `DOI` = `CITIES/Division_of_Industry/`. `PASS` = `CITIES/City_Development_Passes/Mirny_Subnet/Davis/`.

| Ruling | In plain words | Address in `LOG` |
|---|---|---|
| `DR-1` | Six of the eight robot Elementals are pulled back from canon; Davis's Element is one of the six | L22, L98 |
| `DR-4` | Census I (the larger, pre-orbital count) governs a city's size and band | L203 |
| `DR-12` | Per-nation figures are weights for a location pass; values inside a tier are randomized for realism and carry no meaning | L463 |
| `DR-19` | A city's founders stand on geography and access, never on the real station | L538 |
| `DR-24`, `DR-25`, `DR-26` | A station's infrastructure, records, research, equipment, techniques and results can be inherited; its operator and its traditions cannot | L623, L634, L654 |
| `DR-32` | A namesake is never a basis for data | L743 |
| `DR-68` | The Santa Luce population scenario (2026-10-28) is adopted; every city's totals change | L1335 |
| `DR-73` | A mandated-role percentage is a share of the distinctive tier (the workforce left after the baseline) | L1393 |
| `DR-75` | Relung Panen's first new mandated roles; phosphorus and seed are national | L1416 |
| `DR-82` | Australian-side international intake: sea gateway in summer, air-only isolated airport in winter, onward flights to Mirny | L1494 |
| `DR-85` | The 2026-11-02 population rebuild: every country in its latest-period form, split by headcount; the Sinian Federation's share reduced and refilled; tiers relabeled | L1523 |
| `DR-88` | Comparison sentences in specs neutralized; the "(founding wave)" tag means a nation named as a founder in the Founding Register | L1549 (tag clause L1555) |
| `DR-90` | Esperanza cut to 1,200,000; the 702,205 difference divided across 26 other cities (2026-11-02) | L1570 |
| `DR-93`, `DR-94` | Kazakhstan added to the nation pool; Manchuria's share reduced like the Sinian Federation's (2026-11-02) | L1597, L1606 |
| `DR-96` | Relung Panen round-2 decisions, including the winter-intake island (properties only), and Hawaiian as the national language with supporting-tier languages (2026-11-03) | L1628 (language quote L1632) |
| `DR-97` | The robot-keyed term (robot maintenance 12.5 and robot sustenance 3.25 workers per 1,000 robots) joins the three-tier model in file 16 (2026-11-03) | L1638 |
| `DR-99` | Idelsk-Uralia is also an exile group at Mirny; the "(founding wave)" tag means the establishing country named in the Register, not people who arrived in a wave (2026-11-03) | L1655 (tag clause L1660) |

---

# A. Population and workforce

## DV-001 — Census totals, retention, density and workforce

**Current figures.**

| Figure | Current | Source and working |
|---|---|---|
| Census I humans · robots · total | 590,668 · 619,764 · **1,210,432** | `CENSUS` L506; `SPEC` L15; 590,668 + 619,764 = 1,210,432 |
| Census II humans · robots · total | 454,101 · 363,374 · **817,475** | `CENSUS` L650; `SPEC` L16; 454,101 + 363,374 = 817,475 |
| Band | Census I total lies in Band 5 (about 1M–50M); Census II total is below 1,000,000 | `PASS` `00_Frame.md` L65 (band range); totals above |
| Retention, combined · humans · robots | 67.54% · 76.88% · 58.63% | 817,475 ÷ 1,210,432 = 0.67536; 454,101 ÷ 590,668 = 0.76879; 363,374 ÷ 619,764 = 0.58631 |
| Spread (humans − robots) | 18.25 pp | 76.879 − 58.631 = 18.248 |
| Robots' share of Census I · of Census II | 51.20% · 44.45% (humans 48.80% · 55.55%) | 619,764 ÷ 1,210,432; 363,374 ÷ 817,475 |
| Humans departed (Census I − II) | 136,567 = 23.12% of 590,668 | 590,668 − 454,101 |
| Robots departed | 256,390 = 41.37% of 619,764; ratio of the two rates 1.79; robots are 65.25% of all departures | 619,764 − 363,374 |
| People gone, Census I → II | 392,957 | 1,210,432 − 817,475 |
| Density on 410 km² | 2,952.27 per km² (Census I); 1,993.84 (Census II) | 1,210,432 ÷ 410; 817,475 ÷ 410; extent 410 km² at `ULM/Extent_and_Density_Per_City.md` L617, L636 |
| Density grid at 200 / 400 / 420 / 512 km² | Census I 6,052 / 3,026 / 2,882 / 2,364; Census II 4,087 / 2,044 / 1,946 / 1,597 per km² | same division, four areas |
| `09` row (header L52, row L79) | humans 590,668 · residents 1,210,432 · required workforce 323,548 · workforce 915,098 · 35.4% | `DOI` `09_Per_City_Baseline_Run.md` L79; workforce = 619,764 + 590,668 ÷ 2 = 915,098; required by the L50 formula at D 1.25 = 323,548.4; 323,548 ÷ 915,098 = 35.36% |
| `16` Half B row (header L247, row L262) | workforce 915,098 · base 41.9% · MAND 20.3% · FREE 37.8% · D 1.25 | `DOI` `16_Per_City_Three_Tier_Run.md` L262; check: 186,131 (file 16 L2022) ÷ 915,098 = 20.34%; (915,098 − 383,295 − 186,131) ÷ 915,098 = 37.77% |

**Where pass text carries population figures** (found by pattern search; the current value for each topic is in the table above).

| Topic | Pass locations |
|---|---|
| Census I total and band | `00_Frame.md` L65, L89, L136, L236, L269; `00.1_Step_MINUS-1_Input_Contract.md` L64, L70, L168; `02_Spine.md` L318, L321; `03_Research.md` L164; `04_Phase_02` L287, L947; `04_Phase_04` L28, L265; `07_QA.md` L319; `README.md` L49, L75 |
| Census II total | `00.1` L71, L168; `00_Frame.md` L89, L269; `01_Inherited.md` L68; `02_Spine.md` L382; `04_Phase_02` L221, L287, L1484; `07_QA.md` L319 |
| The four human and robot counts | `00.1` L70–71, L169–170; `00_Frame.md` L90, L236; `04_Phase_02` L285–286; `04_Phase_04` L28, L265; `04_Phase_09` L16–17, L59–60, L67 |
| Retention and spread | `00.1` L168–171; `00_Frame.md` L269, L279, L342–343; `02_Spine.md` L112–113, L389, L394; `04_Phase_02` L214, L291–292, L1210, L1218, L1241–1242, L1279, L1474, L1487 |
| Robots' share of Census I; human and robot split | `00_Frame.md` L236; `02_Spine.md` L113; `04_Phase_02` L285–286, L607, L903; `04_Phase_04` L244; `04_Phase_08` L18, L106; `04_Phase_09` L59, L62, L143, L174 |
| Departures (humans; robots' share of departures) | `00_Frame.md` L90; `02_Spine.md` L113, L369; `04_Phase_02` L290–291, L1217, L1262 |
| People gone | `00_Frame.md` L89; `01_Inherited.md` L52; `02_Spine.md` L113; `04_Phase_02` L289, L497, L1140 |
| Density; the density grid (Gate 11) | `02_Spine.md` L318–326; `README.md` L75; `07_QA.md` L319–330 |
| Workforce, required workforce, share required | `04_Phase_04` L27–28, L266–267, L269; `04_Phase_07` L32, L87; `04_Phase_08` L146; `04_Phase_10` L475, L564; `07_QA.md` L133, L138 |

## DV-006 — File 16 (three-tier run): Half B, section 19, and what the file holds

**Pass locations.** `04_Phase_04` L27, L201, L269–270, L284–285, L418–419 (the three-tier split and Davis's free-tier figure); `04_Phase_07` L31 (the source row for file 16), L91, L99–100, L110, L116–123 (own-need table), L389, L407; `04_Phase_08` L224; `05_Reconciliation.md` L102; `08_Review_Panel.md` L164, L308; `10_Readiness_Check.md` L104; `00.1` L351–353. Citations into file 16 by line: `04_Phase_07` L31, L47, L251, L355, L426 and `04_Phase_10` L35, L43, L444.

**What file 16 says now** (`DOI` `16_Per_City_Three_Tier_Run.md`):

| Item | Value | Address |
|---|---|---|
| Section 19 heading | "19. DAVIS — DETERMINED (Option B, flagged for post-pass review)" | L2006 |
| Baseline · mandated · free (workers; share of 915,098) | 383,295 (41.89%) · 252,606 (27.60%) · 279,197 (30.51%); sum 915,098 | L2010–2012; shares recomputed |
| Distinctive tier | 531,803 (58.11%) | L2014 |
| Mandate itemized | agriculture 35% = 186,131; technical/scientific half 12.5% = 66,475; together 47.5% = 252,606 | L2022–2024; 531,803 × 0.35 = 186,131.05 and × 0.125 = 66,475.4 |
| Robot term inside the baseline | 619,764 × 15.75 ÷ 1,000 = 9,761 workers | L2016 (text); recomputed |
| Developer's ruling text on the split | "Mandate 28.2% / free 31.1% … Option B stands: mandate 28.2% · free 31.1%" | L2073–2076 |
| End-of-pass review register, Davis row | "Mandate 28.2%, free 31.1%"; alternatives listed: A 20.7% / 38.5%, C 35.6% / 23.7%, D 32.6% / 26.7% | L3568 (register heading L3549) |
| Half B row | MAND 20.3% · FREE 37.8% | L262 |
| Register item 11 prose | Davis's agriculture 186,131 (35% of distinctive) against 320,284 (35% of the whole workforce), 134,153 workers apart; file 04 §3 quotes 306,780 for the whole-workforce figure and is not recomputed | L2089–2095; three independent counts (2026-11-03) give 186,131, 320,284 and 134,153 |

**Source defects (file 16 disagrees with itself or with the census).** (1) The split: 27.6% / 30.5% at L2011–2012 against 28.2% / 31.1% at L2073–2076 and L3568, and 20.3% / 37.8% at L262. The robot-term ruling is labeled `DR-97` in file 16 and in `LOG` L1638. No choice is made here.

**Citations into file 16 by line.** Current anchors: Half B header L247 and Davis row L262; section 19 heading L2006; the research-half argument L2026–2046; "What stays FREE" L2048; the ruling L2073–2076; Register item 11 block L2089–2095; Notes L2097–2106 (Vestfold Hills sentence L2099–2100; namesake line L2101; kinship note L2103–2105); end-of-pass register row L3568. The line holding the string "100 Miles Davis Boulevard" is L1592 (another city's passage; the city is not named, as in the pass).

**Own-need table (`04_Phase_07` L116–123).** The pass's own-need figures reproduce as humans × rate × D ÷ 1,000 with the rates 53 and 120.7 (live at `DOI` `09` L50 and `DOI` `19` L16). Recomputed on 590,668 humans, D 1.25, sector 186,131: rate 53 gives 39,132 and an export of 146,999; rate 120.7 gives 89,117 and an export of 97,014; the third basis gives 0 and 186,131. The same formula reproduces the pass's printed 85,031 as 85,033, so the recomputed pair carries a margin of 2.

## DV-007 — Food files 17, 18 and 19 name Davis

**Pass locations.** `04_Phase_07` L175–178 and L251–253 (the half-mandated research sector and the kinship note that sits on it); L102–138 (the export headcount argument).

**Current facts.** `DOI` `18_Relung_Panen_Determination_2026-10-29.md` L31: "Davis holds the national research half" and a joint project with Ariun Nuur and Zhongshan (`DR-75`). `DOI` `19_National_Balance_Refresh_2026-11-02.md` holds two runs side by side. Section 5 (robot-term run, 2026-11-03): Davis's agriculture is 186,131 workers (L62), Davis's share of export supply is 44.2% (L81), balance of Davis and Esperanza together without Relung Panen 83.7% (L84). Sections 1–3 of the same file give 189,548 workers (L11), 44.3% (L34) and "feeds about 1,309,000 people beyond itself" (L44); 186,131 × 6.904 people per farm worker = 1,285,048, a figure file 19 does not state. `DOI` `18` L49 carries 44.3% and, in its dated parenthetical, 44.2%. File 19 L50 states that the Davis/Esperanza denominator question (file 16, Register item 11) is unchanged. No change to Davis's own sector counts follows from file 18.

## DV-021 — The composition table: rows, tiers, shares, counts

**Pass locations (found by pattern search).**
- The number of origins and of nations per tier: `04_Phase_02` L26, L67, L297–309 (tier table and a "sole occupant" tier), L318, L349, L357, L485, L859, L949, L955, L960, L963, L972, L975, L1014, L1071, L1397, L1482, L1492; `02_Spine.md` L37, L107; `01_Inherited.md` L50; `04_Phase_06` L21, L204, L207, L347; `04_Phase_07` L379; `04_Phase_08` L247, L294, L320; `04_Phase_09` L77, L96; `CITIES/Cross_City_Culture_Differentiation_Table.md` L145 (Davis's cell).
- Which origin is largest and what share it holds; the "plurality" statement: `02_Spine.md` L107; `01_Inherited.md` L70; `04_Phase_02` L227, L236, L240, L305, L309, L324.
- The size of the largest origin and of the "(founding wave)" origin at Census I: `04_Phase_02` L948–949; the founding-wave share: `01_Inherited.md` L70; `02_Spine.md` L108, L250; `04_Phase_02` L226, L306, L324, L585, L631, L1452.
- The scale check on the smallest origins: `04_Phase_02` L939–950, L1448.

**Current facts** (`SPEC` L20–22 tier lines, L32–76 table; `CENSUS` L392–396; counts and shares recomputed from the table by script):
- 45 rows: Primary 5, Significant 2, Notable 38. Primary: Japan 10.42%, Sinian Federation 9.72%, United Kingdom 9.36%, Germany 8.54%, Korea 8.35% (together 46.39%). Significant: Indonesia 5.74%, Australia 5.74%.
- Largest row: Japan, 10.42% = 126,123 people at Census I (64,576 + 61,547, `SPEC` L32). Second: the Sinian Federation, 9.72% = 117,596 (L33). Gap 0.70 points. No row exceeds 10.5%.
- The row tagged "(founding wave)": Australia, 5.74% = 69,475 at Census I (35,573 + 33,902, L38), level with Indonesia at 5.74% = 69,512 (L37).
- Small rows: 21 rows under 1%, 17 under 0.5%, 10 under 0.1%. The ten smallest at Census I: Tuva 152 (L76), Karachay-Cherkessia 212 (L75), Ingushetia 230 (L74), Finland 240 (L73), North Ossetia-Alania 309 (L72), Kabardino-Balkaria 405 (L71), Tibet 572 (L70), Chechnya 680 (L69), Patani 1,142 (L68), Aceh 1,162 (L67).
- Rows named for regional or successor units include Idelsk-Uralia (L49), Siberia (L58), Donska-Kubania (L59), Mongolia (L60), Künnarantaiga (L61), East Turkestan (L62), Dagestan (L65), West Papua (L66), Aceh (L67), Patani (L68), Chechnya (L69), Tibet (L70), Manchuria (L57); the names are explained at `CENSUS` L839 (Section E).
- Shares are identical across the two censuses (Census II ÷ Census I = 0.6754 for Japan and for the Sinian Federation; `SPEC` L78 states it).
- Derivation file: `CITIES/Upper_Earth_Immigration_Composition.md` `### Davis` L593 holds a pool-based derivation table (L597–599: one Primary nation, seven Significant, thirteen Notable) and, at L601, a final-composition line naming five Primary, two Significant and 38 Notable.

## DV-022 — How the per-nation figures and the tiers are produced

**Pass locations.** `01_Inherited.md` L78 (a guard about the tiers), L87–88, L274 (a guard about comparing nations' figures); `02_Spine.md` L116–118, L129–132; `04_Phase_02` L50, L317–320.

**Current facts.** `SPEC` L28: the table is rebuilt under `DR-85`; successor states are split by headcount; the Sinian Federation's share is multiplied by 0.5719 (a draw from 0.55 to 0.65) and the freed points go in proportion to size to Japan, Germany, the United Kingdom, Korea, Indonesia and Australia; Kazakhstan is added at 1.45% (`DR-93`); Manchuria's share is multiplied by 0.5855 (a draw from 0.55 to 0.65, seed 2026110215, `DR-94`). `SPEC` L78: tier labels follow the final shares, with Primary and Significant ending at the largest ratio gaps among the rows at 4.5% or more (Primary never more than six rows); the 8 / 3 / 1 share weights do not produce the figures; percentages are identical between the censuses. `LOG` L463–474 (`DR-12`) states that per-nation values are weights and that no finding may rest on a within-tier difference; both texts stand (see the conclusions section, C-4).

## DV-023 — The "(founding wave)" tag and the Founding Register row

**Pass locations.** `04_Phase_02` L89–105 (the collision about the tag), L334–345 (the two annotations), L583–636 (the born-here mode); `04_Phase_02` L1400 and L1598 (the open question about the tag's layer).

**Current facts.** `LOG` L1555 (`DR-88`, 2026-11-02): "(founding wave)" means a nation named as a founder in the Founding Register, and nothing else. `LOG` L1660 (`DR-99`, 2026-11-03): the tag "means the establishing country named in the Register, not people who arrived in a wave", and Australia in the Register maps to Australia in the table. `CITIES/Founding_Register.md` L59: Davis, founder Australia, basis "extremely close… comparatively easy access", ruling `DR-19`. The tag stands on Australia only (`SPEC` L21, L38; `CENSUS` L395). `CENSUS` L33 describes the tag as a nation that set the city's early character before larger communities arrived; `LOG` L1661 lists `CENSUS` L33 among the edits not applied yet.

---

# B. Founding, relations, symbol, infrastructure

## DV-002 — Air access

**Pass locations.** `04_Phase_05_Relation_and_Geometry.md` L23 (source table row 3, `Airports.md`: statement about an airport marker); L197 (the heading that gives the number of arrival types); L203 (arrival type 3, "by air"); L345 (Phase 10 handoff row that names the airport among nameable relational features).

**Current facts** (`Locations/Infrastructure/Airports.md`). Davis is in the list headed "Everything Else Has No Air Access — all 23, named" (heading L40; the names are L50, Davis on L50). L54–56 states that many of those cities have a real-world station with a genuine airstrip today and that none has one in Tepenia (Davis named at L55). L57: access is by the highway network only. The thirteen markers in the file number thirteen rows, none for Davis (basis note L47). The Winter Intake Airport row (L23; intro L3) is not a city: its map marker, placed between Davis and Mirny, is a placeholder; `DR-96` (2026-11-03, `LOG` L1633, text at `Airports.md` L23) rules properties only: an ice-cap island "on the Davis/Shackleton coast", unnamed, reached only by air in winter; onward flights go to Mirny (`DR-82`, `Airports.md` L12). Davis's road route is Hwy 110 (`Highways.md` L199) and its seasonal sea route is Prydz Bay (`Ports.md` L559).

## DV-003 — Symbol pair

**Pass locations.** `00.1_Step_MINUS-1_Input_Contract.md` L122 (address of the symbol file's Davis row), L131–134 (the statement of Davis's pair); `00_Frame.md` L292 (symbol-assignment row), L312 (reserved item about the Element half's meaning); `02_Spine.md` L416 (the statement of the pair).

**Current facts.** `CITIES/City_Symbolic_Substrate/City_Symbol_Assignments.md` L112: Davis's row is BLANK, "Deliberately unset, developer ruling 2026-09-16", and carries the instruction not to fill it from the breadbasket reading because Davis is also a port city and the symbol is open. L335–341 states that whenever the determination is run it "starts from a blank slate". L71 lists Davis among four cities that keep their entries; L112 shows the row blank (both stand in the file). **Standing ruling, 2026-09-16, developer:** *"for now, for the current time, we can just make that blank."*

## DV-004 — Founders, station heritage and namesake

**Pass locations.** `00.1` L269 (classification of the spec sentence about the real station operator since 1957); `04_Phase_03` L36 (the climate data's authority); `04_Phase_05` L36, L105, L114, L305, L330, L346 (the "Australian-heritage" material).

**Current facts.**
- `CITIES/Founding_Register.md` L59: Davis's founder is Australia, on geography and access (`DR-19`). Casey: Australia (L58). Mirny: founded by Idelsk-Uralia, exile groups present Russia, Australia and the Sinian Federation (L57). Mawson: Kazakhstan, Russia and Australia jointly (L54).
- `SPEC` L8 (Significance line), L86, L153 and L257 describe Davis, Casey and Mirny as sharing Australian "founding-wave" heritage; the Register's Mirny row (L57) names a different founder. The sentence the pass classifies at `00.1` L269 is `SPEC` L86.
- `LOG` L743 (`DR-32`): a namesake is flavor only. `CITIES/City_Cross_Subnet_Relationships.md` L137 repeats the rule; the paragraph at L139–147 still develops the namesake story.
- `CITIES/City_Cross_Subnet_Relationships.md` L125–126 cites `Davis_Full_Extrapolation.md` (a withheld source) for the character of the Davis–Mawson tie, and L128–130 for the subnet's internal links.
- The relationship passages are covered by DV-S02 below.

## DV-008 — Line positions in infrastructure and relationship files

| File | Davis lines now |
|---|---|
| `Locations/Infrastructure/Highways.md` | L199 (Hwy 110: Zhongshan → Davis → Mirny → Casey → Concordia); the note "`Ports.md` EMPTY (0 bytes)" stands at L349 |
| `Locations/Infrastructure/Ports.md` | Davis row L559; CONSTRUCTED tier list L736; also L130, L201, L224, L795 (neutral-transshipment and distance material) |
| `Locations/Infrastructure/Airports.md` | L3, L12, L23, L40, L50, L55, L57 (see DV-002) |
| `CITIES/City_Relationship_Database.md` | Davis entry L186–193 (heading L186) |
| `CITIES/City_National_Connections.md` | Davis section L303–315 (Mawson L304–306; Casey L307; Mirny L308; Kunlun L309–311; Dome Fuji L312–313; Neumayer L314–315) |
| `CITIES/City_Cross_Subnet_Relationships.md` | Hwy 110 routing L53–54; Davis–Mawson L123–127; intra-subnet bullet L128–131; Part 3 heading L135, namesake rule L137, paragraph L139–147; open-item line L232 |

Pass citations into these files by line: `04_Phase_05` L21 (cross-subnet file L53), L26 (connections file L296–308), L35 (cross-subnet file L125–133; connections file L296–299), L36 (cross-subnet file L130; connections file L300–301). The Ports mentions at L130, L201, L224 and L795 are cited by no pass file.

---

# C. Spec, contract and citation numbering

## DV-005 — The spec's size and the Step −1 contract's coverage

**Pass locations.** `00.1_Step_MINUS-1_Input_Contract.md` §4.1 (the read-spec numbers `1-3,5-8,10-87,90-120,122-134,143,148,153-155,176,178-179`, 137 lines, at L223 and L238) and §4.2–4.3 (strikes and exclusions by number, L259–286); `00.1a_RULING_Vision_Notes_and_Specs_L135-181.md` L232 (the spec's length) and L251.

**Current facts.** `SPEC` has 260 lines (`wc -l`, 2026-11-03). The composition block is L13–78 (45 rows). Spec text from the pass-cited L58 onward sits 24 lines lower (checked by comparing the two texts line by line); two lines, a sentence of the wind-versus-cold callout (L113) and the developer-vision paragraph (L167), carry wording that differs from the text at the pass-cited positions. Run as numbers against the spec as it stands, the read spec takes in the whole composition block and excludes L88 (the namesake paragraph) and L121 (a climate-table row). The contract lists no admitted-set entry or exclusion by number for pass-cited L200–203 and L206–236, which are current L224–227 and L230–260 (Economy open items, Notable Locations L231, Notable Figures L239, Connection to Concordia L244, Legacy L249, Open Questions L254). The contract does not classify the current composition block.

## DV-024 — Spec line numbers cited inside the pass

Pass files cite the spec under two numberings, and a reader following a citation lands on the right text only after adding 24 for any pass-cited number from L58 up. Examples verified in both texts: pass-cited L60 → `SPEC` L84; L62 → L86; L117 → L141; L120 → L144; L127 (the documentary-starting-point sentence) → L151; L129 → L153; L131 → L155; L143 → L167; L207 → L231. Lines containing the string `L127` (not all are spec citations): `00.1` 3, `00_Frame` 3, `01_Inherited` 12, `02_Spine` 3, `04_Phase_02` 2, `04_Phase_05` 1; `L143`: `00.1` 8, `00.1a` 12, `00_Frame` 3, `01_Inherited` 2, `02_Spine` 6, `04_Phase_02` 3, `09.5_Log` 1; `L151`: `00_Frame` 1; `L167`: `00.1a` 6, `00.1` 2. Census citations in the pass use the Section A range L392–398 (current Davis tier table L392–396) and the Census I and II rows at L506 and L650.

---

# D. Rule texts, language, and neighboring files

## DV-025 — The language rule

**Pass locations.** `04_Phase_08` L241–248 (the robot language mechanism and the statement about what any community speaks), L250 (the marker of belonging), L320 (open hole about the languages); `04_Phase_09` L92 (the Language row of the robot module). The word "Hawaiian" occurs in none of the pass files (pattern search).

**Current facts.** Hawaiian (later Tepenian) is the de-facto national language (`LOG` L1632, the developer's words). A city's supporting-tier languages are every language group within 12 percentage points of the largest group's mid-point (`CITIES/Research_Logs/ULM_Runs_Casey_Then_Mirny_Handoff_2026-11-03.md` L25–29; cutoff ruling at `CITIES/Research_Logs/Language_Sets_By_City_Reference_2026-11-03.md` L75–80, which also states it is "Not yet written into any culture file"). Davis's language blocs (`CITIES/Research_Logs/Language_Blocs_By_City_2026-11-03.md` L916–): English 17.02–25.78 (mid-point 21.40, L922); Mandarin 13.29–14.08 (13.685; 7.7 points below, L923); Japanese 10.42 (11.0 below, L925); German 9.93 (11.5 below, L926); Korean 8.35 (13.05 below, L927) and Russian 4.46–11.61 (8.035; 13.4 below, L924) fall outside. The set at 12 points is English, Mandarin, Japanese and German (`Language_Sets_By_City_Reference_2026-11-03.md` L30 for Mandarin, L71 for Japanese 10.4 and German 9.9, set size 4).

## DV-026 — Rule texts that the pass read

**Pass locations.** `04_Phase_02` L852–888 ("once per Act"), L859; `00_Frame.md` L99; `04_Phase_09` L76 (the Acts used as identity phases); `02_Spine.md` G4 block L90–101, L158–182 and `04_Phase_02` L708–743 (what crosses the founding gap).

**Current facts.**
- `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/No_National_Stereotypes.md` (174 lines): L9 "Who founded each city is a separate question, answered only by the Founding Register"; L21 "Records, research, results, equipment and techniques can cross the gap; personhood cannot" (`DR-25`, `DR-26`); L105–106 define Act 1 (2564 to somewhere in the 2600s, a hazy range) and Act 2 (by the late 2600s or early 2700s, onward) as phases of what the people are.
- `.../TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md` L251–258 separates the structural Act 2 (begins about 2614) from "national identity's own date" (late 2600s or early 2700s, by Amundsen Tower's completion, about 2688). Both texts stand.
- `DOI` `README.md` L3–7 (banner): a station's inherited infrastructure, records, research, equipment and techniques are facts a city may build on; the station's operator is never the cause of a sector; founders come only from the Register.

## DV-027 — The extent file's population figures

`ULM/Extent_and_Density_Per_City.md` L617 and L636 carry Census I 1,158,314 and a density of 2,825 per km², and L617 gives 116 and 165 as the two required-area figures (km²). `CENSUS` L506 gives 1,210,432; 1,210,432 ÷ 10,000 = 121.0 and ÷ 7,000 = 172.9. The pass cites the density at `02_Spine.md` L318–326 and `README.md` L75. The two files disagree; no choice is made here.

## DV-028 — The check files read at Step 5

**Pass locations.** `05_Reconciliation.md` L64–69 (polar-night length compared across sources), L185; whole file (the check files are tier 3).

**Current facts.** `CITIES/Local_Cultures/Mirny_Subnet/Davis.md` L28 calls Davis "sole-China-Primary"; L104 gives "Mandarin (Primary tier)"; L107 and L199 give "thirteen nations"; L53 gives polar night and midnight sun "roughly 66-67 days". `SPEC` L99–100 gives polar night about Jun 4 → Jul 10 (~37 days) and midnight sun about Nov 25 → Jan 18 (~55 days); the composition is at `SPEC` L20–22 and L32–76. `CITIES/Local_Robot_Culture/Mirny_Subnet/Davis.md` exists and is the other check file.

## DV-029 — A character draft sited in Davis

**Pass location.** `04_Phase_10_Catalog.md` L499–503 (character canon returns nothing for Davis).

**Current facts.** `Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/TBN [STP-06 thicc Chinese Hao]/README.md` L22 names "Davis, Tepenian Federation" as her present-day primary location; L44–47 cite Davis's "China-Primary founding tier" and a Davis China share of 20.51%. `SPEC` L33 gives the Sinian Federation 9.72%; `Founding_Register.md` L59 gives Australia as Davis's founder.

## DV-030 — Spec climate retention

`SPEC` L109 gives "Lands ~28 mm/yr (~45% retention)" and L108 "Falls ~73 mm/yr". 28 ÷ 72.8 = 38.46% (28 ÷ 73 = 38.36%). The pass states 38.5% at `02_Spine.md` L82, `01_Inherited.md` L242, `00.1` L330 and `04_Phase_02` L980.

---

# E. Standing decisions

These are Davis's developer decisions of 2026-10-30 and the rulings the sheets rest on. Each is a present-tense rule. Recorded in `Manual_Input_Audit_2026-10-29/Walkthrough_Decisions.md` L70–86 and `FIX_LEDGER.md` L236, L245, L262, L263 (both under `ULM/`); none appears in `LOG`.

**Developer, 2026-10-30, on Davis items 1 to 5:** *"yup, all as recommended"*.

## DV-011 — Population figures in the sheets

The datasheets keep the figures the pass applied, each labeled "as recorded at the pass (2026-09-16)", with the current figure beside it. Current figures (DV-001): Census I 590,668 H / 619,764 R / 1,210,432; Census II 454,101 H / 363,374 R / 817,475; retention 67.54% combined, 76.88% humans, 58.63% robots, spread 18.25 pp; robots 51.20% of Census I; density 1,210,432 ÷ 410 = 2,952.27 per km²; `09` L79 (required 323,548, workforce 915,098, 35.4%); `16` L262 (workforce 915,098, base 41.9%). The sheets involved: `Step_-1`, `Step_0`, `Phase_2`, `Phase_4`, `Phase_9`, `Step_1_and_2` and the Pre-Trip. The Pre-Trip's quotation of `DR-4` stays as that ruling's dated record. Every datasheet line found by pattern search (2026-11-03) that quotes a pass-applied figure carries the current figure beside it: `Datasheets/Phase_2.md` L44; `Step_0.md` L47; `Step_1_and_2.md` L27, L53, L55.

## DV-020 — Conclusions written inside the sheets

The conclusions inside the sheets are kept as a record. They are the pass's own interpretations and are stripped before the sheets are reused for a new run of Davis.

## DV-S01 — Which split governs

Davis's own ruling governs the mandate and free split: file 16 section 19 (heading L2006) rules Option B, and Half B's pair is not cited as Davis's. The developer's words, 2026-09-16: *"Mandate 28.2% / free 31.1% actually does make sense within the context of the city setting, since it's the sort of thing they'd need."* (`DOI` `16` L2074–2075). File 16 itself is untouched; `Phase_4` and `Step_1_and_2` quote both pairs and say so. Current values: ruling text 28.2% / 31.1% (`16` L2076, L3568); section 19 table 27.6% / 30.5% (L2011–2012); Half B 20.3% / 37.8% (L262). The disagreement among these is source defect (1) under DV-006 and open question 1 below.

## DV-S02 — The two relationship passages

`CITIES/City_Cross_Subnet_Relationships.md` L123–131 and `CITIES/City_National_Connections.md` L274–278, L293–295, L304–308 (L274–278 and L293–295 sit in sections of other cities and are not re-read here) rest on the Founding Register and on Hwy 110 (`Highways.md` L199) and do not name heritage, the culture megasheet's heritage claim or the namesake story; ratings and types are unchanged. Current text: Mawson, "Australia is among the founders of both" (`City_National_Connections.md` L304–306); Casey, "Both founded by Australia (`DR-19`; Founding Register), on the same highway, Hwy 110" (L307); Mirny, "Australia is among the exile groups present at Mirny (Founding Register); Hwy 110, plus Mirny's own Relay Vaults link" (L308). `City_Cross_Subnet_Relationships.md` Part 3 (L135–147) is untouched and refers to the "shared naming heritage" treatment of Part 2; L125–126 still cites `Davis_Full_Extrapolation.md`. Approved with *"all as recommended"*, 2026-10-30.

## Corrections inside the sheets (walk-through item 5, same quote and date)

- The `Phase_5` Ports row marks the "road and air" wording as a record of text the 2026-09-16 port ruling replaced.
- The `Phase_5` Airports row states no airport in Tepenia (DV-002) and does not quote the Winter Intake Airport row.
- The `Phase_7` row 12 does not call the `10_Validation_Findings` sentence a live violation; the line carries a correction dated 2026-09-26.
- The `Phase_7` row 2 cites the `README` "First results" heading at L184 and the Davis line at L186.
- `Phase_2` cites the census geography parenthetical at L390.
- The as-run Pre-Trip (`00.0_Pre-Trip_Inspection_AS_RUN_2026-09-11.md` L582) notes the named ledger file as nonexistent; the ledger file now exists (`00.2_Position_Coverage_Ledger.md`) and the rebuilt Pre-Trip section K (`00.0_Pre-Trip_Inspection.md` L588) points to it.
- The as-run Pre-Trip's Phase 2 `T8` line (L285) says 4 admissible rows. The rebuilt Pre-Trip's Phase 2 `T8` line (`00.0_Pre-Trip_Inspection.md` L281) names 5 admissible rows: the stereotype law, the Falkland Treaty, the census, the Founding Register row and the composition file's Davis section.

## Rulings the sheets and spec rest on

- **Port ruling, 2026-09-16 (developer):** Davis is Tepenia's principal Indian-Ocean-sector import port, where Hwy 110 meets deep sheltered water; trade direction is inbound; the maritime sector is free, not mandated (`SPEC` L173–227; `Ports.md` L559; file 16 L2048–2076).
- **Symbol blank, 2026-09-16:** see DV-003.

---

# F. Conclusions that rest on current inputs and may change on re-derivation

Pass location, the input it rests on, and that input's current value. No verdict is given.

| # | Pass location (topic) | Input | Current value and address |
|---|---|---|---|
| C-1 | `04_Phase_02` H-2 (L224–258), A.2 closing (L324–331), A.3 (L334–345), B.4 (L583–636), L1400, L1598; `02_Spine.md` L250; `01_Inherited.md` L70 (the contrast between the founding stock and the plurality stock, and the reading of the "(founding wave)" tag) | What the tag means; who is largest | Tag clause `LOG` L1555, L1660; Register `Founding_Register.md` L59; Australia 5.74% (`SPEC` L38), Japan 10.42% (L32), Sinian Federation 9.72% (L33) |
| C-2 | `04_Phase_02` C.2 (L939–950), C.3 (L953–976), C.5 (L1012–1021), L1448, L1482 (the scale check on origin communities and the rich-internal-layer conclusion) | Number and size of origin rows | 45 rows; 10 under 0.1% (152 to 1,162 people); 17 under 0.5%; 21 under 1% (`SPEC` L32–76); regional and successor names at `CENSUS` L839 |
| C-3 | `04_Phase_02` E.1 (L1060–1081) (the origins as a sample of the places robots occupied) | The list of origins | Rows listed at `SPEC` L32–76, including Taiwan (L43), Kazakhstan (L51), Manchuria (L57), Mongolia (L60), East Turkestan (L62), Tibet (L70) |
| C-4 | `01_Inherited.md` L87–88, L274; `04_Phase_02` L50, L318–320, L324; `02_Spine.md` L116–118 (the seal on comparing nations' figures and its stated ground) | How the figures are produced | `SPEC` L28 and L78 (DV-022); `LOG` L463–474 (`DR-12`); `LOG` L1523 (`DR-85`) |
| C-5 | `04_Phase_05` L35–36, L303–306, L330, L346, L383–386 (heritage relations treated as excluded for want of an independent route) | What the relationship files rest on | `City_National_Connections.md` L304–308 rests on the Register and Hwy 110 (DV-S02); `City_Cross_Subnet_Relationships.md` L125–126 cites a withheld source (DV-004) |
| C-6 | `04_Phase_08` L241–250, L320; `04_Phase_09` L92 (what any community speaks; the dominant local layer; the marker of belonging) | The language rule | DV-025: Hawaiian national language; supporting set English, Mandarin, Japanese, German |
| C-7 | `02_Spine.md` L107, L116–118; `04_Phase_02` A.4 (L347–363), B.2 chain (L461–476) (nothing load-bearing can be tacit, given the number of origins and the largest share) | Number of rows; largest share | 45 rows; largest 10.42% (`SPEC` L32) |
| U-1 | `04_Phase_07` A.2 (L102–123), A.2b (L125–138), L407; `05_Reconciliation.md` L102–110 (the export headcount that the pass declines to state) | The national food files | DV-007: 44.2% of export supply (`DOI` `19` L81); two run values for Davis's farm workforce, 189,548 (L11) and 186,131 (L62); file 16 L2091–2094 vs L2022 |
| U-2 | `02_Spine.md` L90–101, L158–182; `04_Phase_02` L708–743 (what crossed the founding gap) | The inheritance rules | `LOG` L623–660; `No_National_Stereotypes.md` L21 (DV-026) |
| U-3 | `04_Phase_10` L499–503 (no figure sited in Davis) | Character drafts | DV-029 |
| U-4 | `00.1` §4 (L205–286), `00.1a` (the composition region of the contract) | The spec's composition block | `SPEC` L13–78 (DV-005) |
| U-5 | `05_Reconciliation.md` (whole; the check files) | The check files' text | DV-028 |

---

# G. Source defects found while writing this note

Each is stated with both addresses; none is resolved here.

1. File 16: split 27.6% / 30.5% (L2011–2012) against 28.2% / 31.1% (L2073–2076, L3568) and 20.3% / 37.8% (L262).
2. File 19 holds two runs. Its latest run (section 5, L62 and L81) gives Davis's farm workforce 186,131 and share 44.2%, which three independent counts reproduce from file 16; section 1 (L11) and section 2 (L34-L35) belong to the first run, and people fed is 1,309,000 (L44). File 18 L49 carries both shares (44.3% and 44.2%).
3. `ULM/Extent_and_Density_Per_City.md` L617, L636 against `CENSUS` L506 (DV-027).
4. `Local_Cultures/Mirny_Subnet/Davis.md` L53 (66–67 days) against `SPEC` L99–100 (37 and 55 days); three independent counts at latitude 68°35′S give 37 days without sunrise and 54 days without sunset; its composition text against `SPEC` L20–22 (DV-028).
5. `SPEC` L109 (~45% retention) against 28 ÷ 72.8 = 38.46% (DV-030).
6. `SPEC` L8, L86, L153, L257 against `Founding_Register.md` L57 for Mirny's founder (DV-004).
7. `City_Symbol_Assignments.md` L71 against L112 (DV-003).
8. `City_Cross_Subnet_Relationships.md` L137 against L139–147 (DV-004).
9. `No_National_Stereotypes.md` L105–106 against `Timeline.md` L251–258 (DV-026).
10. `CENSUS` L33 (tag described as an arrival) against `LOG` L1555 and L1660.

---

# H. Open questions for the developer

1. **Which split is Davis's?** Your 2026-09-16 ruling reads mandate 28.2% and free 31.1%. File 16's section 19 table now counts 27.6% and 30.5% on the current workforce of 915,098 (L2011–2012), its own text still quotes your ruling (L2076), and Half B shows 20.3% and 37.8% (L262). Three independent counts (2026-11-03) confirm the arithmetic: the rule behind your ruling (agriculture 35% plus half of technical/scientific 12.5% of the distinctive tier, 47.5%) gives 252,606 mandated and 279,197 free workers on 915,098, which is 27.6% and 30.5%; Half B's 20.3% and 37.8% is the agriculture-only mandate (186,131). Which pair do you want carried as Davis's?
2. **The seal on comparing nations' figures.** The pass bars comparing any two nations' figures; the stated ground is that values inside a tier are randomized (`DR-12`). The table now comes from headcounts, with a random multiplier only on the Sinian Federation (0.5719) and Manchuria (0.5855). Does the bar stay, and on what ground?
3. **The very small rows.** 21 of the 45 origin rows are under 1% and the smallest, Tuva, is 152 people at Census I. Do the smallest rows count as origin communities, or as a tail?
4. **The language rule in a finished pass.** Davis's pass never mentions Hawaiian. The set at 12 points is English, Mandarin, Japanese and German. Should the rule enter this pass as a dated note, or should the language sections (Phase 8 section E, Phase 9 Language row) be re-derived?
5. **Re-derive or annotate.** Phase 2 (composition) and Phase 5 (relations) rest on inputs that changed most (section F). Do you want these re-derived, or only carried by this note?
6. **The symbol pair.** It is blank by your 2026-09-16 ruling. It stays blank until Davis's own Phase 10 sets it; is that still the plan?
7. **The character draft in Davis.** Her README cites a China share of 20.51% (L47) and a China-Primary founding tier (L45). Should it be brought in line when Davis's composition is settled?

# I. Decisions pending elsewhere that touch Davis

- **The Idelsk-Uralia change.** `LOG` L1661 lists as not applied yet the Register's Mirny row (adding Idelsk-Uralia to the exile groups), `CENSUS` L33, and the relationship database's Mirny line; they await the developer's word. Idelsk-Uralia is a Davis row (1.67%, `SPEC` L49), and Davis's Mirny relation (`City_National_Connections.md` L308) reads the Register's Mirny row (L57).
- **The language rule's entry into finished passes.** `CITIES/Research_Logs/Drift_Review_SUMMARY_Finished_Passes_2026-11-03.md` §5 item 6 asks how it enters a pass that never mentioned Hawaiian (Davis, Shirayuki, Sinheung, Zhongshan); `Language_Sets_By_City_Reference_2026-11-03.md` L80 states it is not yet written into any culture file.
- **The national food denominator.** `DOI` `16` L2089–2095 and `19` L50: the Davis/Esperanza denominator question is unchanged.
- **The winter-intake island.** Unnamed, with two candidates (`Airports.md` L23); the map marker between Davis and Mirny is a placeholder.
- **The end-of-pass review of Davis's split.** `DOI` `16` L3568: Davis is marked for review after all cities are determined.

---

*Filed 2026-11-03. Read for this note: the 24 pass files and `README.md` by pattern search; `SPEC`; `CENSUS`; `DOI` files 09, 16, 17, 18, 19 and `README.md`; the Founding Register; the relationship, symbol, airport, highway and port files; the language reference tables; `LOG`; the Universe-repo rule texts; the drift review `CITIES/Research_Logs/Drift_Review_Davis_2026-11-03.md`.*
