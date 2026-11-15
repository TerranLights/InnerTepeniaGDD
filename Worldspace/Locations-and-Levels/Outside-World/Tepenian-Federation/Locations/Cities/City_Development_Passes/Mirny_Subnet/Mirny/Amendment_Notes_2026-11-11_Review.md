# Mirny — amendment note for the review of 2026-11-11

**What this is:** the fresh dated note for a simple review of Mirny (`STARTUP_Mirny_Review_then_Casey_ULM_2026-11-11.md`, Part A;
the finished-city cross-check method, `DR-104` item 3 and `DR-106`), sized to what changed after Mirny's last re-runs. It lists
every change that could bear on a Mirny conclusion, each with its source address, then (section F) the conclusions to test.
**Pass files are not edited** (`DR-101`); this note states what is true now, with its source (`DR-102`). Everything here is
PROPOSED; nothing is applied without the developer's word. Log: `Amendment_Log_2026-11-11.md` beside this file.

**The cut-off date.** Mirny's last re-runs (the QA re-run, the fresh Review Panel, the readiness re-run) were all written on
2026-11-08, the last file at 18:24; nothing in Mirny's folder changed after that (log MR-02). Every change below is dated
2026-11-09 or 2026-11-10. **None of the rulings below is cited anywhere in Mirny's folder** (log MR-05), so none was applied by
the re-runs.

---

## A · General rulings and canon of 2026-11-09 and 2026-11-10 (recorded for every city)

Only a ruling recorded for every city can bear on Mirny; an answer given for another city does not carry (standing line 25).

| # | Ruling | What is true now | Source | Applied by Mirny's re-runs? |
|---|---|---|---|---|
| A1 | `DR-125` item 6 | **New canon:** Hawaiian is a pidgin with a primary base of English and Japanese and a supporting base of Korean, Tagalog, Ilocano and Mexican Spanish; later, influence from many languages made it Tepenian, so the two are one language over time. How a robot built in a city gets a supporting-tier language stays open (stated there for Sinheung). | `DEVELOPER_RULINGS_LOG.md` L1894–1895 | No (MR-05) |
| A2 | `DR-125` item 3 | **"Time that is your own" is defined, so every future run reads it one way:** canon's leisure and nothing else (robots' leisure owed to nobody; the shared night for everyone). It does not mean the free tier of the workforce, and does not mean that any share of a person's life is free. | L1895 | No |
| A3 | `DR-127` item 2 | **New canon:** humans could keep arriving in Tepenia after the treaty was signed; they could not go back to Upper Earth. The robot half (whether robots kept arriving) is not answered: the robot channel is open in law, and no later arrival is recorded. Written into the treaty draft as Article II.2.5 (see C2). | L1912–1913 | No |
| A4 | `DR-128` item 1 | **An origin row applies to both humans and robots, each at its own percentage.** A row's practices are still sized on its human count; the total with robots is a conditional upper figure. Whether a row records nationality or residence at departure is not addressed. | L1921–1922 | No |
| A5 | `DR-130` item 7 | **For every city:** a row's own figure may be stated flatly and rows may be counted; no characterization may rest on a gap between two rows of one tier. | L1940 | No |
| A6 | `DR-131` item 3 | **For every city, "a city's own lines"** (`DR-122` item 5) are its own files and entries, plus lines about shared things it is named in (its port, airport, road, cluster), excluding any clause grounded only in another city's lines. | L1949 | No (the re-runs used `DR-122` item 5's shorter wording) |
| A7 | `DR-131` item 7 | **For every city:** tiers reached after the random draw stand as relabeled; the dividing rule stays the composition file's own (no row at 4.5% or more is Notable). | L1949 | No |
| A8 | `DR-124` item 4 | **"Records can draw people"** (the station-inheritance ruling's row) is a general mechanism any city may use. | L1886 | No |

**Process rulings of the same days (no conclusion rests on them):** `DR-126` (the rule rows: standing lines 21–25 and
amendment rules 5–6; they govern how this review's pieces run, L1904); `DR-129` (the plan, L1931). (`DR-132` is not a process
ruling for every city: its text covers two other cities' pointer lines only, L1958; it is listed in section E. Mirny's pointer
lines were applied on 2026-11-08 under `DR-123`.)

## B · `DR-133` item 1 — Australia is a four-node partner, Mirny one of the four

`DR-133` item 1 (L1967): Australia is a **four-node** partner: Dumont d'Urville, Mirny, Mawson and a cluster's shared harbor; the
developer reminder of 2026-10-03 ("a THREE-NODE partner") is superseded. In `Locations/Infrastructure/Ports.md` (881 lines, commit
`354c17f6`, 2026-11-10):
- **L129** (the partner table): Australia's row now reads "Dumont d'Urville · Mirny · Mawson · the Tri-Cities … ✅ four-node
  *(three-node until 2026-11-10)*".
- **L188** (the canon-nodes block): marked "SUPERSEDED IN PART 2026-11-10 (`DR-133`): Australia is now a FOUR-node partner"; the
  text below it (L189) is kept as recorded on 2026-10-03.
- **L386** (the receiving-node rows): "Dumont d'Urville · Mirny · the Tri-Cities' Nella Fjord port … ✅ Australia-partner receiving
  nodes".
Mirny stays a node in every one of these lines. Only the count changes. (The fourth node's own lines are another city's and are
not used here.)

## C · Sources Mirny's pass cites that changed since 2026-11-09

| # | Source | Change | Bears on Mirny? |
|---|---|---|---|
| C1 | `Infrastructure/Ports.md` | Section B above (commit `354c17f6`) | Yes: the node count |
| C2 | Treaty draft, `TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md` (142 lines) | Commit `23e5226`, 2026-11-09 23:42, "Add Falkland Treaty II.2.5: humans may relocate to Tepenia after signing": new **Article II.2.5 at L50** (a human who did not make the paragraph-3 election may at any time after the effective date elect to take up residence in Tepenia, and by that election loses legal personhood in Assembly Power territory); Article IV.2 paragraph 2 (L76) extended to cover a II.2.5 election; a drafting note added at L138. Every line after L49 moved down by one, and after the L138 note by two. | Yes: it writes A3 into the treaty. Mirny's files cite the treaty draft by article, not by line (a line-anchor pattern found none), so no anchor is stale; the article numbering of II.2.1–II.2.4 is unchanged. |
| C3 | `Cities/City_Relationship_Database.md` | One line in place, another city's entry (`DR-133` item 5) | No (not Mirny's line; no line moved) |
| C4 | `City_Symbolic_Substrate/City_Symbol_Assignments.md` | One line, another city's row (`DR-135`); changed lines naming Mirny: 0 | No |
| C5 | `Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` | Entries `DRQ-10`, `DRQ-11`, `DRQ-13` (another city's band, the oasis rock, another city's difficulty; `DR-131` item 1) | No (none is a Mirny entry) |
| — | Census, Founding Register, Highways, Airports, the cross-subnet and national relationship files, Division of Industry, the robot-culture sheets, the extent file | No commit and no uncommitted change since 2026-11-09 | — |

## D · Not changes (recorded so they are not re-listed)

- **Commit `b5824186` (2026-11-10 15:22)** on Mirny's spec, culture file, six datasheets and the symbol registry records the
  corrections applied on 2026-11-08 (`DR-123`); the files were last written on 2026-11-08 (spec 14:17; the others 11:48), before
  the re-runs read them (log MR-03).
- The rule-file changes of 2026-11-09 and 2026-11-10 (`T8_Standing_Brief_Lines.md`, `Amendment_Layer_Rules.md`, the observations
  log, `Tools/make_t8_required_list.py`) change how pieces are run, not what Mirny's sources say.

## E · Rulings of the same days recorded for another city only (do not carry; standing line 25)

`DR-124` items 1–3 and 5–13 (Davis); `DR-125` items 1, 2, 4, 5 and 7–9 (Sinheung); `DR-127` items 1, 3 and 4 (Davis; item 3's
sizing rule is carried for every city by `DR-128` item 1); `DR-128` item 2 (Sinheung); `DR-130` items 1–6 and 8–15 (Zhongshan);
`DR-131` items 1, 2, 4–6 and 8–13 (Shirayuki; item 2 says robot rows get "one rule for every city later", which is not yet that
rule); `DR-132` (two other cities' pointer lines; its open item, whether a pass's run log takes a pointer line at all, L1959, is
open, not ruled); `DR-133` items 2–6, `DR-134` and `DR-135` (another city's routes and Element).

## F · Conclusions to test

**How this list was built.** One locator reader searched Mirny's folder for the conclusions each change in sections A to C could
touch (its table, 302 lines, is kept beside this file as `.review_2026-11-11_locator_F_candidates.md`). The orchestrator printed and
read every line cited below (05:52). Each item names the conclusion as it stands now (an amendment piece's version where a piece
re-derived it), what it rests on, and the change that could move it. **Each item goes to one reader, who says whether it holds,
narrows or flips** (Part A item 2); only items that narrow or flip are re-derived.

| # | Conclusion as it stands (file, line: words on the line) | What it rests on | Change |
|---|---|---|---|
| **F-1** | **No human route in after the treaty date.** `04_Phase_02_Composition_and_Arrival.md` L165–166: "**no written human channel exists after the treaty date**, so humans arriving later are read as born here or unread (R-17)". `04_Phase_05_Relation_and_Geometry.md` L258: "A human from Upper Earth arriving after the treaty date has **no written route to membership**". | Treaty II.2.3's "prior to the date of this Treaty"; request R-17 | A3, C2 (treaty II.2.5, L50) |
| **F-2** | **Phase 9's memory line in Act 2.** `04_Phase_09_Populations.md` L201 ("After the treaty date the treaty text gives humans no admission channel"), L304 (Act 2: "with the human founders gone, and no human channel after the treaty in the treaty's own text (R-17), **the remembering side is robots**"), L508 (PA-59: "No post-treaty human admission from Upper Earth is assumed, and none is denied"); `Amendment_Rederivation_P9_Populations_2026-11-04.md` L109 ("If no later human channel opened… every human at Mirny in Act 2 is Tepenian-born and was taught the wind"), L165 ("Act 2, the remembering side is robots (conditional on Q-86)"). The same condition sits in the differentiation cell (the locator's pointers: `Amendment_Rederivation_ST6_Differentiation_2026-11-04.md` L298; `06_Differentiation.md` L67, L234). | Treaty II.2.3; `DR-51` (later immigration kept open); R-109, Q-86 | A3, C2 |
| **F-3** | **The native layer as the only thing met without translation.** `04_Phase_02_Composition_and_Arrival.md` L283: "the only layer every resident, in either body and from any stock, meets without translation." (Open question `DEC-228`.) | The phase's native-layer reading; `DR-100`'s civic tongue not yet beside it | A1 |
| **F-4** | **The newcomer told the wind's dangers in the supporting tier.** `Amendment_Rederivation_P9_Populations_2026-11-04.md` L175: "A newcomer who speaks the supporting tier can be told the wind's dangers in it before she has the dominant language, if the protocol is given in it." (third order, conditional on AR-45). | The supporting tier as a language apart from the dominant one; a newcomer existing at all | A1, A3 |
| **F-5** | **The caution on English authoring labels.** `Amendment_Rederivation_P10_Catalog_2026-11-04.md` L394: "With English Mirny's supporting tier, an English authoring label in this catalog could be read as an attested in-world English name." | English as supporting tier (now English and Russian, `DR-111`); the authoring-label rule | A1 |
| **F-6** | **The same shares in both bodies.** `Amendment_Rederivation_P08_Making_2026-11-03.md` L291: "Robot figures apply the same proportions as the human population." (`SPEC` L69); `Amendment_Rederivation_P2c_Composition_2026-11-03.md` L124 (the founding strata: "Same share in both bodies by construction"). | `SPEC` L69 | A4 |
| **F-7** | **A built-here robot's origin.** `04_Phase_02_Composition_and_Arrival.md` L512: "**PA-14.** Robots built at Mirny, if any, have a learned origin from Mirny's own cultures." | `DR-11`; the robot-physiology file's community rule; R-13 | A4 |
| **F-8** | **Naming the largest row.** `Amendment_Rederivation_P2c_Composition_2026-11-03.md` L15: "The largest share is 13.73 % (United Kingdom; Korea 13.71 %)."; L77: "UK 13.73 against Korea 13.71, and Idelsk-Uralia against Russia (core state), both 2.14 % and one robot apart." The applied spec wording (`Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` L624: "the largest the United Kingdom at 13.73 %"); the phrase "the largest share 13.73 %" in many pieces' "Live facts used" headers. | The spec's table; `DR-12` | A5 |
| **F-9** | **How the tier labels are read.** `Amendment_Rederivation_P2c_Composition_2026-11-03.md` L222: "**AQ-23 · How is "Primary" read at Mirny?** … Mirny has six. **Recommendation:** a tier label: the six largest communities jointly". `Amendment_Rederivation_PIU_IdelskUralia_2026-11-04.md` L126: "The window rule in `UEIC` gates the Notable tier only, and Idelsk-Uralia is Significant". | The census's tier definitions; the composition file's tiers | A7 |
| **F-10** | **A subnet member's road access withheld.** `04_Phase_05_Relation_and_Geometry.md` L463 (that member's road access: "Absent from the read set"); `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L609: "an admitted highway line added 2026-10-21 now gives this member's road access; it names other locations and is not used here (AR-242)". The fresh panel's Neighbor seat is thinned by the same withholding (per the locator: `Amendment_Rederivation_ST8b_FreshPanel_2026-11-08.md` L643). | `DR-122` item 5's shorter rule | A6 |
| **F-11** | **The hub's member count not proposed.** `Application_Batch_3_CultureFile_and_Spec_2026-11-08.md` L620: "its only source is the relationship database's subnet member list, a line that names other places. No Mirny line states the count without naming them". | `DR-122` item 5 (as DEC-183) | A6 |
| **F-12** | **The coastal supply line's grounding.** `04_Phase_05_Relation_and_Geometry.md` L321 (P5-28): "all three receive Australian freighter shipments on one coastal supply line", grounded in two other cities' relationship entries and Mirny's own; `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L340 marks the other entries "not used (other location)". | The relationship database (Mirny's own entry and two others) | A6 (the exclusion half: clauses grounded only in another city's lines) |
| **F-13** | **What the free tier measures (Q-43).** `04_Phase_04_Ordinary_Life.md` L149 ("47.1 % is the free tier, an upper bound"; the reading a developer question); `Amendment_Rederivation_PRT_RobotTerm_2026-11-04.md` L156: "Q-43 asks whether the freedom margin measures the share of people able to do work they want, or the share of a working life not spoken for by survival. … the question of meaning stays open". | `D09` L126–127; the robot-physiology file L364–371 | A2 |
| **F-14** | **The free tier read as a pool of hours.** `04_Phase_06_Meaning.md` L119 (canon's leisure, "the material proof that leaving worked", set beside "47.1 % is the free tier, an upper bound"); `04_Phase_07_Order.md` L168: "at Mirny the pool it would draw on is a quarter smaller than Phase 4 wrote"; `04_Phase_04_Ordinary_Life.md` L222: "nothing says every worker holds a share of the free hours equal to the average." Also the human counterpart of the robots' hours owed to nobody (per the locator: `04_Phase_04_Ordinary_Life.md` L129, L236, R-45). | The robot-physiology file L356–360; Phase 4's free-tier figure | A2 |
| **F-15** | **Australia's node count.** `04_Phase_05_Relation_and_Geometry.md` L179: Australia → "Dumont d'Urville · Mirny · Mawson", "three-node" (`PRT` L129); `Amendment_Rederivation_ST14_Phases4and5_2026-11-05.md` L662 (the geometry re-test: "the Australian three-node sea link and Mirny's port "tier not established" (`PRT` L129, L200; L793): **st[ands]**"). | `Ports.md` L129 as it read before 2026-11-10 | B, C1 |
| **F-16** | **What draws people to Mirny.** `04_Phase_02_Composition_and_Arrival.md` L72: "G3 (the hub, quarry and chamber-supply functions as the only admitted attractor for any later arrival)" (read in full); L341 (E5): "the place does not know what it attracts because it did not attract. (Later movers: unread.)"; `Amendment_Rederivation_S5_Reconciliation_2026-11-04.md` L448 (docket D-2: the "station-and-name draw" open to strike). | Founding by assignment; the station-inheritance rulings | A8, A3 |

**Considered and not made items (no conclusion rests on the change):** the language-bloc gap at
`Amendment_Rederivation_P9_Populations_2026-11-04.md` L174 is `DR-100`'s own 12-point arithmetic, not a gap between two rows of one
tier, and `DR-111` already sets Mirny's tier; the robot-half arrival lines (Phase 2 L478, L508; Phase 9 L305) concern robots after
2564, which `DR-127` did not rule; the body split ("robots 50.63 %") is a gap between the two bodies, not two rows of one tier; no
Mirny line reasons from what Hawaiian is made of, says robots have no national origin, names a draw or relabeling of tiers, or says
records can or cannot draw people (the locator's zeros, with its search strings in its table).

## G · Mirny's 29 open questions against the rulings of 2026-11-09 and 2026-11-10 (noted, not answered)

**The questions:** `DEC-220` to `DEC-230`, `DEC-240` to `DEC-245`, `DEC-260` to `DEC-271` (`Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`
L420–653). Classed by one reader against the rulings in sections A and B, in a closed set (settled / part / facts changed /
untouched); the reader's table is kept beside this file as `.review_2026-11-11_questions_class.md` (38 lines). **The reader
returned: `COUNTS: SETTLED 0 · PART 0 · FACTS CHANGED 3 · UNTOUCHED 26`, `COVERAGE: 29 of 29 rows`.** No ruling of these two days
settles any Mirny question, in whole or in part.

| DEC | Class | Ruling | What changed (the entry's own line, read by the orchestrator) |
|---|---|---|---|
| `DEC-223` | Facts changed | `DR-125` item 6 (L1895), with `DR-127` item 2, `DR-128` item 1, `DR-130` item 7, `DR-131` items 3 and 7 | L445: the four amendment-layer notes "have not caught up with the rulings on founders, language, the strongest finding, symbols and today's applications". The list of for-every-city rulings they lag has grown (section A). Whether to add the end lines is still the question. |
| `DEC-228` | Facts changed | `DR-125` item 6 (L1895) | L485: Phase 2's L283 says the native layer is "the only layer ... met without translation", and the question is whether to mark it beside `DR-100`'s common civic tongue. That tongue is now defined (a pidgin with an English and Japanese primary base). Whether to mark the line is still the question. This line is also a section F candidate. |
| `DEC-268` | Facts changed | `DR-129` items 1 and 2 (L1931) | L623: "Set a date for the weather-signs research session (05:00-14:59 window)". `DR-129` now gives that window to runs on cities not yet run, once the four finished cities are cross-checked. No date is set and Mirny's research is not mentioned. |

**The reader's two flags, checked:**
- **`DR-132` is not for every city.** Confirmed (L1958 names two other cities' pointer lines); `DEC-224`, `DEC-269` and `DEC-270`
  stay untouched, and section A of this note is corrected (log MR-10). For `DEC-270`, `DR-132` lists as not decided whether a pass's
  run log takes a pointer line at all (L1959); an open item settles nothing.
- **`DEC-245` (L549–553):** the reader could not tell from its ranges whether the numbering-frame rule (`Amendment_Layer_Rules.md`
  rule 6, L61–63) touches option C's counting convention. Checked: rule 6 makes a numeric read spec name "the commit or the line
  count it was computed against"; option C (L552) is about how the middle and last PROOF lines are counted. Rule 6 does not bear;
  **untouched stands.**

Four older Mirny entries are partly open or deferred and outside the 29: `DEC-041` (b), `DEC-042`, `DEC-080`, `DEC-081` (L186–217).
No ruling of these two days names them.

## H · The item checks (Part A item 2), as returned

One reader per item, each on a frozen brief (`.review_F-<n>_brief.md`, list `.review_F-<n>_required.txt`); each reader's output is
kept beside this file as `.review_F-<n>_reader.md`, and its Round 2 run as `.review_F-<n>_round2_raw.txt` (the one reader's output
passed in all three slots of `Tools/triple_read_verify.py`, which takes exactly three; log MR-13). The verdict word is the reader's.

| Item | Reader's verdict | Round 2 |
|---|---|---|
| F-1 | **FLIPS** | UNANIMOUS |
| F-2 | NARROWS | UNANIMOUS |
| F-3 | NARROWS | UNANIMOUS |
| F-4 | HOLDS | UNANIMOUS |
| F-5 | NARROWS | UNANIMOUS |
| F-6 | NARROWS | UNANIMOUS |
| F-7 | HOLDS | UNANIMOUS |
| F-8 | NARROWS | UNANIMOUS |
| F-9 | HOLDS | first run failed two fields; repaired by the same reader (`DR-117` item 2); re-run UNANIMOUS (log MR-16, MR-17) |
| F-10 | NARROWS | UNANIMOUS |
| F-11 | **FLIPS** | UNANIMOUS |
| F-12 | NARROWS | UNANIMOUS |
| F-13 | NARROWS | UNANIMOUS |
| F-14 | **FLIPS** | UNANIMOUS |
| F-15 | NARROWS | UNANIMOUS |
| F-16 | NARROWS | UNANIMOUS |

**Count: 3 flip, 10 narrow, 3 hold.** The three that hold (F-4, F-7, F-9) are not re-derived.

**The re-derivation pieces (Part A item 3), grouped by the conclusions they share; each runs the three-reader pipeline:**

| Piece | Items | What it re-derives |
|---|---|---|
| `ARR` | F-1, F-2, F-16 | The human admission route after the treaty date, the memory line in Act 2, and what draws people |
| `LANG` | F-3, F-5 | The native layer "met without translation" and the caution on English labels, beside the defined civic tongue |
| `COMP` | F-6, F-8 | The robot half of each origin row, and naming the largest row |
| `OWN` | F-10, F-11, F-12 | Mirny's own lines: the road, the subnet's member list, the coastal supply line |
| `FREE` | F-13, F-14 | The free tier and "time that is your own" |
| `NODE` | F-15 | Australia's receiving nodes |

The pieces do not depend on one another's results, so they may run side by side (`DR-107`); each is written to file before it is
counted done. Everything a piece writes is PROPOSED; nothing is applied without the developer's word.

## I · The re-derivation pieces (Part A item 3), as written

Each piece ran the three-reader pipeline: a frozen brief per reader, three Opus readers in private staging folders, Round 2
(`Tools/triple_read_verify.py`), Round 3 by `SendMessage`, one fresh merge writer (`M-246`), the quotation audit with a triage of
every miss, the American English sweep, and a round record with the raw tool output. **Every piece: Round 2 UNANIMOUS on the first
run; all six Round 3 cross-verdicts CONSISTENT.** Everything in the pieces is PROPOSED; no pass file was edited (`DR-101`).

| Piece | File (round record beside it, `…b_T8_Rounds.md`) | Findings | Docket rows | Questions | Quotation audit (triaged) |
|---|---|---|---|---|---|
| `ARR` | `Amendment_Rederivation_ARR_2026-11-11.md` | 6 | 39 | 5 | 54 misses: 0 misquotations |
| `LANG` | `Amendment_Rederivation_LANG_2026-11-11.md` | 4 | 11 | 3 | 23 misses: 0 misquotations |
| `COMP` | `Amendment_Rederivation_COMP_2026-11-11.md` | 3 | 13 | 2 | 40 misses: 0 misquotations |
| `OWN` | `Amendment_Rederivation_OWN_2026-11-11.md` | 5 (+2 reserved, not adopted) | 28 | 6 | 46 misses: 6 misquotations, fixed before the record (log MR-27) |
| `FREE` | `Amendment_Rederivation_FREE_2026-11-11.md` | 6 | 27 | 4 | 37 misses: 3 misquotations, fixed before the record (log MR-25) |
| `NODE` | `Amendment_Rederivation_NODE_2026-11-11.md` | 6 | 5 | 1 | 11 misses: 0 misquotations |

**What each piece re-derives (its own headings, read on the lines):**
- `ARR`: two written human routes into the Federation after the treaty date, and who a later human at Mirny can be; the legal edge at
  Mirny's door, crossable one way by election; the later human stratum; the memory line in Act 2 (certain in the robot half, possible
  in both bodies); what draws people to Mirny (at the founding nothing; later, two admissible attractors and no adopted mode); and
  "into Mirny" for a later elector, whose placement is an open slot.
- `LANG`: Mirny's two common layers (the conditions, met with no language; the civic tongue, national and learned); the relay and the
  record as things that carry language; English in two ruled places; Mirny's tier is English and Russian by ruling.
- `COMP`: the robot half of each origin row; naming the largest row; a superlative assumes one order shared by both bodies.
- `OWN`: the road between Mirny and the spur member; what Mirny's road lines give the Neighbor seat; the hub's member count
  (conditional on a question); the coastal supply line; the tie with the two road neighbors once "three" falls.
- `FREE`: what the free tier measures; canon's leisure and the free tier are two objects; where the two standards of worth meet;
  "time that is your own" at Mirny, by body; the averages caution; the pool a national call would draw on is work, never time.
- `NODE`: Mirny is one of Australia's receiving nodes and the partner now has four; the sea relation stays direct and bilateral; the
  port's tier stays "not established"; the sea row's class survives; the geometry re-test narrows in its qualifier only; the other
  counts on Mirny's lines are not the node count.

**Not applied:** every docket row (123 in all) waits for the developer's word; the pointer lines into the old pass files are not
written (`DR-116` item 2; the same hold `DR-132` set for two other cities). Questions are in the decisions file (section J).

## J · Questions and the close

**23 questions, `DEC-480` to `DEC-502`**, are in `Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md`, in a new section directly above
`## Answered` (21 from the six pieces, one each from items F-7 and F-9), each on its recommended answer, marked PROVISIONAL. The
review's summary is `REVIEW_SUMMARY_2026-11-11_Mirny_Review.md`; its log is `Amendment_Log_2026-11-11.md`. **Not declared
complete;** that is the developer's call.
