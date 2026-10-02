# Mirny — Step 0 · `T8` Rounds

**Pass:** Mirny · ULM · Step 0 (Frame) · WARM · 2026-09-29 · **Written file:** `00_Frame.md`
**Procedure:** `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` §N.1–§N.2 (amended 2026-09-28, `M-246`).

## Round 0 — the reading list

`.t8_required_00_Step0.txt` — **18 entries, 4,478 admitted lines** (4 ranged). **Scope, by developer choice
("Split it", 2026-09-29):** the readers read the frame's sources; the orchestrator read the `Disciplines/` files
itself (Step 0.2). ⚠ The Pre-Trip's own Step 0 list omitted
`01_Frame_Typology_and_Inheritance.md` and the Disciplines — a recurrence of `M-247`; the list was rebuilt from the
runbook's own Step 0 text before dispatch.

⛔ **Later the same morning the developer ruled CST and RWBEM out of the ULM pass entirely** ("for later"). The
dispatch had told the readers the orchestrator would read "the five Disciplines," so all three §B tables repeated
that; `00_Frame.md` §B corrects it. No reader opened either file.

## Round 1 — three independent readers, identical prompt

| Reader | Agent | Output | Written |
|---|---|---|---|
| A | `a3e84802b147b8eb2` | `.t8_Step0_readerA.md` | 11:43 |
| B | `a884db57d490d2ae4` | `.t8_Step0_readerB.md` | 11:49 |
| C | `ab9b87b339283d238` | `.t8_Step0_readerC.md` | 11:49 |

## Round 2 — `triple_read_verify.py` (raw output, unedited)

```
required files: 18
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 428-548,598-609,1829-1992,2242-2362,2455-2518] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/01_Frame_Typology_and_Inheritance.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Run_Modes_Warm_and_Cold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/04_QA_Gates_and_Differentiation.md  [range 96-107] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Official_Population_Census.md  [range 1-41,368-457,476-482,487,490,492,495,496,499,504,510,519,527-541,590-598,604-606,610,613,616,617,638-654] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Extent_and_Density_Per_City.md  [range 525-544,605-609,615] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Repo_Scope.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Timeline Eras/2 The Second Interwar Period/Timeline.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/World_History_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Scaffold.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Real_World_Influences.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Reference/Falkland_Treaty/Falkland_Treaty_Draft_v1.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/Datasheets/Step_0.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

## Round 3 — `SendMessage` continuation of the same three readers

The recipe's four-part prompt plus section 5 (disposition differences: a · the other reader is right / b · mine is
right / c · a developer question), with eight named differences (i–viii) and two orchestrator notes: **n1** (the
CST/RWBEM ruling — flag any use of either as an instrument of this pass) and **n2** (Step 0 ends at `RB` L2518; the
asymmetry check is Step 1's, `RB` L2519–2528).

| From → about | Verdict | File |
|---|---|---|
| A → B | **CONSISTENT** | `.t8_Step0_round3_readerA.md` |
| A → C | **CONSISTENT** | 〃 |
| B → A | **CONSISTENT** | `.t8_Step0_round3_readerB.md` |
| B → C | **CONSISTENT** | 〃 |
| C → A | **CONSISTENT** | `.t8_Step0_round3_readerC.md` |
| C → B | **CONSISTENT** | 〃 |

**Gate (`§N.2`): Round 2 UNANIMOUS and Round 3 six of six CONSISTENT → cleared to write.**

### Where the readers stood after Round 3

| Item | A | B | C | Merge |
|---|---|---|---|---|
| (i) Type — Installation half | assign | hold | withdraw | **Contradiction → HELD** (conservative), Q-20 |
| (ii) Substitute (2) | out (`RB` L445) | out (both reasons) | out (`RB` L445) | Out; `RM` L124–126 → Q-27 |
| (iii) Founders' Act | open (withdrew "answered") | open (withdrew "probably") | open | **Unanimous: OPEN** |
| (iv) Out-migration as G6 | candidate | candidate | candidate | Candidate, Q-22 |
| (v) Federation band | mismatch real | mismatch real | mismatch real | Q-23 |
| (vi) §5.4 tags | none (withdrew rule) | "Patterned — deferred" | none | **Contradiction → no tag** + B's guard wording, Q-25 |
| (vii) Language family | developer question | developer question | developer question | Q-24 |
| (viii) Out-of-range material | none load-bearing | none load-bearing | none load-bearing | C's three citations replaced by n2; sibling sums dropped |
| — Substitute (3) under n1 | pending | pending | pending (raised) | Q-21 |

## Merge rule used

1. **Contradiction → the most conservative current (post-Round-3) view**, with the split named in the row.
2. **No contradiction → union**, with single-reader finds credited (`00_Frame.md` §I, U-1 … U-25).

## `§N.5` falsification check — **NOT met: `T8` did not pass trivially**

Round 2 was clean; **Round 3 moved every reader** and caught what no script could see:
- the Timeline's "Act 1" is a story-structure act, not the Grand-Timeline Act — found by **one** reader (C), and it
  withdrew two readers' Act answers;
- the Federation's own census total contradicts the runbook's "Band 6" — found by **one** reader (A);
- the "real-world comparables" substitute routes through RWBEM, so the developer's ruling leaves it without an
  in-run channel — found by **one** reader (C), the same morning as the ruling;
- two readers swapped positions on the Type after reading each other — the only live contradiction left.

## Orchestrator's own checks after Round 3

- **The `06` check** (late; see `00_Frame.md` §J): no Mirny worked example.
- **`World_History_Reference.md`:** the project copy is a stub pointing to the universe copy.
- **Pass `README.md` paths:** L37 broken.
- **Citation re-check by script** — raw output below. Every miss was a multi-line citation whose probe word sits on
  the adjacent line; each was then read at its full range (second block).

```
OK   RB L445 | | **"Unlike X, this city…" · "same as X" · "better/worse grounded than X"** | ⭐ **`01` §5.3a's PEER-FREE substitutes — the location's own earlier stat
OK   RB L1958 | | **Vostok** | **Settlement + Installation** — a research station that became a place people are from. ⭐ **The dual assignment is the finding**; every
OK   RB L1961 | | The Tepenian Federation | Polity, Band 6 |
OK   RB L1962 | | A Halley-subnet Arcanet region | Network locus |
OK   RB L1880 | > pass that means: the founding and its circumstances, allocation or charter decisions, migrations, a
OK   RB L1882 | > terminus, not an event inside it.*** **Addresses: `Worldspace/World_History_Reference.md` · **U**
OK   RB L1854 | > **⚠ And `Specs/` "Status:" fields are POST-WAR.** *("Damaged; partially operational," etc.)* ***They are
OK   RB L2258 | | ⭐ **ACT 1** | **2564 → early 2600s** *(~40–50 years)* | ***"Japanese who live in Antarctica."*** **Origin cultures still FRESH** |
OK   RB L2262 | > **Act 1 is roughly the first `18%` of it.** ***A pass that writes its city as its founding nation is writing
MISS RB L2290 | > **The Tower completes `~2688`, which sits exactly where the developer places the Act 1→2 transition.**
MISS RB L2294 | > **`~2688` carries the Tower's completion, the opening of the ORBITAL TIER, and the Census I → Census II
OK   RB L2476 | `Disciplines/Cultural_Synthesis_Techniques.md` · `Disciplines/Real-World_Basis_Extrapolation_Method.md` ·
OK   RB L2508 | > ⚠ **And `06_Worked_Example_Provenance.md` still applies in warm mode** — required reading may carry THIS
OK   RB L2519 | # Step 1 — Audit what is inherited
OK   RB L2528 | **Run the asymmetry check on existing findings before writing new ones.** For every inherited finding describing
OK   RB L533 | > | **3.** ⚠ **Admission carries NO distinctiveness claim.** *"This is what the place is like" is the finding; "and nowhere else is" is terminal, and 
OK   RB L602 | > ***Is this location's configuration typical, or exceptional? If exceptional, in what way — and which findings
OK   RB L1976 | | **4** | ⭐⭐ **`Worldspace/Robot_Biology_and_Culture/Robot_Physiology_and_Cultural_Practices.md` — THE LARGEST SINGLE INPUT TO THIS PHASE** *(§C.10; t
OK   RB L1839 | | **Second Interwar** | **2564–2812** ⭐ *(the default frame — see below)* |
OK   RB L469 | | **`Step 6` — Differentiate** + the `Cross_City_Culture_Differentiation_Table` | **read the row BEFORE writing a category** | ⭐ **WRITE-ONLY during t
OK   RB L446 | | **Using another city as a control, a baseline, or an implicit normal** | ⭐⭐ **RELATION — what this place needs from elsewhere, what flows, in which 
MISS RB L1881 | > discovery, a disaster, a founding crime — anything inside `2564–2812`.** ***The Long Night War is the frame's
OK   RB L2316 | ✅ ⭐ **"A Japan-FOUNDED TEPENIAN city."** ***Stock: Japanese. People: Tepenian. Local culture: its own.***
MISS RB L2331 | > ***Robots are the MAJORITY population in most Tepenian cities*** *(commonly 51–55%)*. **There is therefore no
OK   01 L100 | | **Settlement** | People live here as their home, by choice or necessity | *What is it like to be from here?* |
OK   01 L102 | | **Installation** | Purpose-built for a function, with a controlling institution, staffed rather than settled | *What happens to people who live insi
MISS 01 L113 | - ### ⭐ **A DUAL ASSIGNMENT IS ITSELF A FINDING.**
OK   01 L135 | | **Resettled** | What did the second population inherit, misread, or fail to notice about the first? *(Commonly assigned and systematically under-use
MISS 01 L179 | | **5 — Regional** | ~1M–50M | **Distributions**, not points | Mostly fail |
OK   01 L180 | | **6 — Civilizational** | 50M+ | The thin shared layer and its maintenance | Fail |
OK   01 L165 | **Declare two numbers, not one:** the **population band** and the **extent band**. They usually match. **When
MISS 01 L302 | > known, documented destination is not straining under that same pressure. **Where this applies, the correct
OK   01 L380 | 4. **State the choice explicitly in the Temporal frame line, even when it is simply "the default."** An
OK   01 L411 | | **Determined** | Fixed by the parent; the location has no say. Climate, currency, the calendar, the language family, physical law | **Writing a loca
OK   01 L399 | > **The `Determined` class WIDENS across the Act 1 → Act 2 boundary** *(by Act 2 a shared identity is among the
OK   01 L454 | > **A pass with no sibling set is the ordinary case, not a degraded one.** The entire spine — the generator
OK   01 L498 | 2. **The nearest analogous location at a different scale.** A unique station against the cities; a unique
OK   01 L500 | 3. **Real-world comparables**, via `Real-World_Basis_Extrapolation_Method.md` — **divergence stated
OK   01 L502 | 4. **The generator-conflict method** (`02` §5) — **which needs no comparison set at all, and is the reason
OK   01 L540 | - **Patterned** — varies, and the variation has a describable shape. **This is the usual answer and it is the
OK   01 L544 | **A Band 4+ pass that answers everything as Uniform has not been written at its own scale.**
OK   01 L566 | **Written:**         ALONE (default)  /  co-written with <what>  [if co-written: justify, per §5.3b]
OK   01 L576 | **Generators available:** <see 02>   **Generators selected:** <at least three>
OK   01 L437 | 4. **Do not build the location's single strongest finding on a provisional assumption.** If the spine depends
OK   01 L440 | 5. **Register the assumption where the parent's eventual pass will see it.** An assumption recorded only in the
OK   01 L412 | | **Inflected** | The parent supplies the form; the location supplies its version. A national holiday, observed *this* way | **This is where most good
OK   01 L414 | | **Aggregated** | The parent's own character is partly the sum or the tension of its children | Ignoring it produces a Band 5–6 polity written as if 
OK   01 L221 | ### Threshold 5→6 — the shared layer becomes thin and its maintenance becomes the subject
OK   01 L224 | things that are, plus the machinery that keeps them so.** Law, currency, calendar, a language family, a handful
OK   CEN L4 | **Coverage:** All chartered cities of the Tepenian Federation, founding era through Orbital Era  
OK   CEN L33 | National communities are classified by tier based on long-run population share. Where a founding wave nation set the city's early cultural character p
OK   CEN L36 | - **Primary** — Dominant national community; shapes the city's primary linguistic and cultural identity
OK   CEN L376 | | Primary | China |
OK   CEN L377 | | Significant | Japan, UK, South Korea, Russia, Indonesia, Australia *(founding wave)* |
OK   CEN L478 | *Taken after the initial founding period and long-run immigration equilibrium was established, before construction of Amundsen Tower and the onset of 
OK   CEN L490 | | 7 | Mirny | Mirny | 665,901 | 685,529 | **1,351,430** | *(revised 2026-07-04)* |
OK   CEN L504 | | — | **{{Bunger Hills City}}** | Mirny | **465,147** | **482,807** | **947,954** | ⭐⭐⭐ **FOUNDED 2026-09-05 — the 38th city, and the first added by t
OK   CEN L529 | *(Halley, Janbogo, and Palmer subnet totals revised 2026-07-03; Janbogo and Mirny also revised the same day (Concordia counts toward Janbogo subnet; V
OK   CEN L537 | | Mirny / Wilkes Land + Plateau | 3,820,557 | 4,224,724 | **8,045,281** |
OK   CEN L540 | | **TOTAL** | **15,623,523** | **16,403,077** | **32,026,600** |
OK   CEN L592 | *Taken immediately before the Long Night War, after decades of orbital migration via Amundsen Tower had moved a significant fraction of the population
OK   CEN L605 | | 6 | Mirny | Mirny | 507,344 | 509,151 | **1,016,495** | |
OK   CEN L368 | ### Mirny Subnet — Wilkes Land / East Antarctic Plateau
OK   EXT L527 | **Run 2026-09-05, immediately after Marambio.** ⛔ **Developer ruling that set the terms:** *"rock and/or ice,
OK   EXT L533 | **So Gate 11 inverts: population ÷ band = REQUIRED area, then ask what the site has.** ⭐ **And with ice
OK   EXT L543 | > on the 25. There is a **different question**, below.* **Do not open a "finish the other 26" task.**
OK   EXT L525 | # 10 · ⭐⭐⭐ THE OTHER 25 — and **why Gate 11 cannot catch them**
OK   EXT L615 | | **Mirny** | Mirny | 1,351,430 | 135 | 193 | **coastal ice** |
OK   EXT L542 | > ⛔ **Consequence for scope: the extent run is COMPLETE, not 30% done.** *There is no remaining Gate 11 work
MISS TL L47 | **RESOLVED 2026-08-05, developer-confirmed:** Amundsen Tower's completion sits at this
OK   TL L75 | | **Break into Two** | Save the Cat / Bell ("Doorway of No Return #1") | ~2614 | ~20.0% |
MISS TL L182 | extended here — while the robots present at the founding are still fully active,
MISS TL L227 | TBD in detail, but per already-established canon (see `Infrastructure Sequence` in
OK   TL L239 | above, cities come first, during Act 1), so the Arcanet beginning as a quiet,
MISS TL L253 | highway segment right at the start of this span. The Arcanet's national,
OK   TL L327 | entire population (~32M) roughly **6.4 times over**. See
MISS TL L348 | **Self-Revelation** can be placed anywhere across the entire second half of Act 2
OK   TL L365 | **The Long Night War's inciting incident** — placed here deliberately, per the
OK   SIR L27 | > **Act 1 is roughly the first `18%` of the period.** ***So a story or a location pass that writes its
OK   WHR L65 | **The name:** Antarctica's annual polar night lasts approximately three months — complete darkness. The extended darkness defined the war's conditions
OK   WHR L69 | - Destroyed the Amundsen Tower (Space Elevator), cutting off Tepenia's connection to the broader world; the scrap mountain of its remains still exists
OK   WHR L85 | **Signed:** June 21, 2564, at the city of Stanley, Falkland Islands. Ended the War of Upper Earth.
OK   WHR L120 | **Who built it:** The Tepenian Federation — both robot and human citizens, though predominantly robot labor due to the extreme altitude and conditions
OK   WHR L122 | **Destruction:** Upper Earth's militaries destroyed Amundsen Tower during the Long Night War. This was not incidental military damage — it was the del
OK   WHR L240 | **Geographic basis:** Every real Antarctic research station became a Tepenian city as the exile population expanded and built out permanent settlement
OK   WHR L275 | - The Federation's political structure and governance
OK   WHR L345 | **What it is:** The nationally used social media network/service across the Tepenian Federation during its Antarctic era, prior to the Long Night War 
OK   WHR L143 | - Exact construction start date for the Tower itself (phased sequence established above, but precise year Tower construction began — likely ~12–17 yea
OK   FTS L3 | **Status:** structure only, no final prose drafted yet. See `Real_World_Influences.md` in this folder for the real-world treaties behind each choice b
OK   FTS L9 | **Scope, confirmed 2026-07-08:** the treaty founds Tepenia as a sovereign entity and sets the terms of exile. It does **not** specify what kind of gov
OK   FTS L13 | **Confirmed authorship, same day:** the Tepenian Constitution was authored completely and entirely by robots — no human hand whatsoever in its actual 
OK   FTS L49 | **Article III.1 — Regional Arrangements.** Adapted directly from UN Charter Chapter VIII: local disputes handled by regional bodies before escalating 
OK   FTD L3 | **Status:** first full draft, 2026-07-08. Not locked canon. Drafted directly from `Scaffold.md` and `Real_World_Influences.md` in this folder — see bo
OK   FTD L35 | **Article I.3.** The internal form of government, the offices, and the laws by which the Federation of Tepenia governs itself are matters for its own 
OK   FTD L37 | **Article I.4.** The right of the Federation of Tepenia's own communities and settlements to organize their own local councils, to make and carry into
OK   FTD L53 | 2. The population departing under Article II.2 shall be settled at such existing scientific and research installations as are presently found upon tha
OK   FTD L54 | 3. Nothing in this Article requires that a population assigned to a given station share the national origin of the Power that formerly maintained it; 
OK   FTD L56 | **Article II.4 — Path to Full Civic Independence.** Any settlement founded under Article II.3, once established, may in time and by its own governance
OK   FTD L62 | **Article III.1 — Regional Arrangements.** The settlements established under Title II may, at their own initiative, associate into regional groupings 
OK   FTD L70 | 2. This withdrawal has no application within the territory of the Federation of Tepenia, where the legal standing of robots shall be a matter for that
OK   FTD L87 | **Article V.1 — Prohibition of Nuclear Devices.** No nuclear explosive device of any kind shall be constructed, tested, or detonated within the territ
OK   FTR L25 | **Scope, confirmed 2026-07-08:** the Falkland Treaty does not concern itself with what kind of government the exiled population sets up. That belongs 
OK   FTR L43 | **Contribution 1:** Article IV's sovereignty freeze (no claim strengthened, none renounced, none newly asserted) as the likely mechanism explaining ho
OK   FTR L46 | **Contribution 1:** the multi-organ institutional split (General Assembly vs. Security Council vs. ICJ vs. Secretariat) as a template for splitting Je
OK   RP L57 | > climate permits — and it is a GRADIENT across locations, never a gate.**
OK   RP L67 | They do not age in the biological sense, though components degrade over time and require maintenance or replacement.
MISS RP L105 |   them**, which means they die in *incidents*: a dome breach, a collapse, a grid failure, a war. **Many at
OK   RP L108 | - **It answers the permafrost problem.** Burial is impossible in Tepenia. Ossuaries are the historical
OK   RP L125 | > > ### ***"The reason why nobody would 'recycle' metal from ossuaries is because that metal is the bones of dead robots. They mine their metal from q
OK   RP L136 | > what makes leaving the dead alone affordable.*** **A necessary industry whose necessity is ethical as well as
OK   RP L170 | > ⚠ **Nothing above is adopted.** ⛔ **The mortuary question remains DEFERRED; this note only states its shape.**
OK   RP L215 | | ⭐ **Robots live longer, so a single individual spans more of the divergence** | *A robot built early in the era and one built late are **not carryin
OK   RP L338 | > the dark** — and it means the polar night falls on a population that is *all* resting, together.
OK   RP L377 | *(Established 2026-07-05, generalized from a Sanay developer-vision session — see `Cities/City_Vision_Notes/Sanay.md`.)* Sanay's specific labor dynami
OK   RP L409 | - **Robot creation mechanism — "fabrication-synthesis chambers" (placeholder name)** — established 2026-07-06, during the City Vision Notes session fo
OK   RP L422 |   - **Personality (the Personality Module)** is the *psychological* seed — not values-orientation tendencies themselves, but the underlying **conceptu
OK   RP L426 |   - **Language (the Language Module)** is a fully separate, third phenomenon — distinct from both Personality and Build, never a sub-part of either. *
OK   RP L432 |   **Clarified same day: ongoing manufacturing isn't actually required for this to keep working at all.** Chambers are durable apparatuses, not consuma
OK   RP L430 |   **Confirmed 2026-07-07: robots can still be built ("born") in the present-day game era.** Both currently-active manufacturing sites — Sinheung and B
OK   DRL L211 | > *"**Everything is assumed with Census I, because that's the maximum size per city that each city needs to
OK   DRL L248 | **What a pass DOES do in the meantime:** write the location at the level of **base-level fundamental facts** —
OK   DRL L303 | | ⛔ **This city's own culture material** — `Local_Cultures/`, `Local_Robot_Culture/` — **READ-LAST, at Step 5, as a CHECK** | **A query about Davis re
OK   DRL L341 | > # ***Would this material still be here if the originating nation had left and never returned?***
OK   DRL L345 | > | ✅ **YES** | **ADMISSIBLE.** *An artifact outlives its makers.* **Audio logs · journal entries · transport manifests · maps · records · orientation
OK   DRL L352 | | ⛔ **UNCHANGED — the law itself** | **A site's builders, flag, nationality, lineage and fate are still GPS-only** — *a coordinate, never a cause, an 
OK   DRL L424 | **Developer, verbatim:** *"Exiles from a combination of Russia, China, and Australia."*
OK   DRL L433 | | ⚠ **Spec lines now contradicted** | L152 "*Primarily* Russian" and L229's "non-founding status … here at Mirny" → **proposed-correction docket, neve
OK   DRL L434 | | ⛔ **Unchanged** | **The GPS law.** L152's reasoning — "Russia's Antarctic presence had always been significant; the exile city … reflected that weig
OK   DRL L435 | | ⏸️ **Not touched** | The deferred rename (`TODO.md` "Mirny Rename") |
OK   DRL L186 | | ⛔ **Gate** | **ALL 38 cities complete through ULM + CST + RWBEM.** Not "most." Not "the subnet in question." **All 38, all three.** |
OK   DRL L190 | its subnet's early money, its unit, its backing, or its harmonization story.** ✅ It **may** record what a place
OK   DRL L472 | | **For a location pass** | Per-nation figures are **weighting.** ✅ **The tiers and the city totals are the information.** ⛔ **No finding may rest on 
OK   DRL L479 | **Developer, verbatim:** *"That's just a nickname, because of its geographical placement."* Admitted as a name; no
OK   DRL L491 | | **`DR-10a`** | Is `DR-10` corpus-wide, as its wording reads? And `00_RUNBOOK.md` L2787 still lists "vision session" material as a Tier 2, primary in
OK   DRL L492 | | **`DR-11a`** | `00_RUNBOOK.md` §C.9b constraint 2 (L2119–2121) still calls robot national origin "an open reserved question" — amend in place. And i
OK   DS0 L12 | | Retention (computed; formula = retained ÷ Census-I count) | combined 75.22% · human 76.20% · robot 74.27% · spread **1.93 pp toward humans** | Compu
OK   DS0 L18 | | Real-world basis | Mirny Station (Soviet Union / Russia), Davis Coast, East Antarctica | `Specs/Mirny.md` L3 |
OK   DS0 L22 | declaration, Configuration, generator selection, the asymmetry check on inherited material — none of this
OK   CON L3 | **Pass:** Mirny (Mirny subnet) · ULM · **Step −1, the input contract before the frame** · **Run mode: WARM**
OK   CON L89 |                                   UNDETERMINED: whether the Planetary Split Brain falls inside the frame → R-4.
OK   CON L105 |                        - `Local_Cultures/…/Mirny.md`, `Local_Robot_Culture/…/Mirny.md` — READ LAST, Step 5
OK   CON L215 | | L3 | SPLIT — chars 1–27 ADMITTED · 28–51 EXCLUDED — GPS · 52–101 ADMITTED | 1–27: G7 · 52–101: G7 + Tier 0 position | 3-0 | G7 is GPS only (RB L2105
OK   CON L325 | | L150 | SPLIT — 1–34 ADMITTED · 35–361 EXCLUDED — GPS · 362–612 ADMITTED · 613–701 EXCLUDED — CONCLUSION · **702–716 ADMITTED-DEMOTED** · 717–786 ADM
OK   CON L353 | | L184 | SPLIT — 1–128 ADMITTED · 129–195 ADMITTED-DEMOTED · 196–433 EXCLUDED — CONCORDIA-FRAMED · 434–486 EXCLUDED — FRAME · 487–549 ADMITTED · 550–5
OK   CON L391 | | **C-6** | G6 Defining event | **PARTIAL** | L148 · L150 (1–34) | In-frame material: **the founding and its circumstances** only (RB L1880) — unanimo
OK   CON L393 | | **C-8** | G8 Demographic composition | **PRESENT** | L13 · L15–L16 · L18 · L20 · L21 (1–46, 78–119) · L22 · L24 · L28 · L47 | **Census I governs:** 
OK   CON L417 | | ~~RV-8~~ | ~~**Robot national origin**~~ — **REMOVED 2026-09-28: resolved by `DR-11`** (robots carry a national origin, learned by immersion) | ~~RB
MISS CON L484 |    cross-subnet links through the hub.
OK   CON L428 | Proposed: the four-quadrant profile and spine (Step 2) from rows C-2 … C-8 · Proposed: Phases 0–10, each with a
OK   RM L31 | > ⭐ ***Independent arrival at this file's own §1 framing.*** **The city run beginning 2026-09-06 is WARM
OK   RM L124 | **Until Gate 6 fires, run all four `04` Part III.4 substitutes and say in the pass that you did:**
OK   RM L138 | **Own culture material read at:**  Step 0.4 item 6, as a CHECK   [state where it was actually read]
OK   QR L4 | > Source: `Timeline Eras/2 The Second Interwar Period/README.md` (71 lines), extracted in full 2026-09-15.
OK   RD L37 | | **Spec** | `../../../Specs/Mirny.md` |
OK   RD L40 | | **Research log** | `../../../Research_Logs/Mirny_Research_Log.md` ⚠ *may not exist yet — Step F creates it* |
OK   PTR L824 | > 🧪 `T8` — **Step 3:** `Agent×3(general-purpose, T8_PROMPT{files: 00_RUNBOOK.md §"Step 3" + the deficits Step 2 named + Real-World_Basis_Extrapolation
MISSES: 14
```

Follow-up on the misses (raw):

```
RB 2289: > ### ⭐⭐ SO THE ACT BOUNDARY IS NOT A DATE — IT IS A CONSOLIDATION.
RB 2290: > **The Tower completes `~2688`, which sits exactly where the developer places the Act 1→2 transition.**
RB 2291: > ***Write Act 1 → Act 2 as a gradient with a decisive moment in it, never as a line crossed.***
RB 2292: 
RB 2293: > ### ⚠⚠ AND CHECK WHAT ELSE SITS AT THAT MOMENT, BECAUSE IT IS CROWDED
RB 2294: > **`~2688` carries the Tower's completion, the opening of the ORBITAL TIER, and the Census I → Census II
RB 2295: > boundary** *(which the census file states is **pre-war migration to orbit, not loss**)*.
RB 2296: > ⭐⭐⭐ ***So the same structure whose completion solidified a shared national identity is also the structure
01 113: - ### ⭐ **A DUAL ASSIGNMENT IS ITSELF A FINDING.**
01 114:   **Anywhere founded as an installation and now inhabited as a home carries `Settlement + Installation`**, and
01 115:   ***the tension between "staffed" and "settled" is a live source of material*** rather than a labeling
01 116:   awkwardness. **Expect this doubling wherever a setting's history includes purpose-built outposts that
01 117:   outlived their purpose.**
TL 225: **~2614 – ~2688**
TL 226: 
TL 227: TBD in detail, but per already-established canon (see `Infrastructure Sequence` in
TL 228: `TODO.md`), this span should cover: cities founded and built out → subnet-internal
TL 229: highways wired → the Arcanet gradually connected subnet by subnet → Hwy 22 (the
TL 230: Transcontinental Highway) built, reaching the South Pole/Amundsen Station directly →
TL 231: only then does Amundsen Tower's own construction begin, in the final ~12–17 years of
TL 232: this span (per already-established canon on the Tower's own construction timeline).
TL 47: **RESOLVED 2026-08-05, developer-confirmed:** Amundsen Tower's completion sits at this
TL 48: era's **Midpoint**, ~2688 — but explicitly **not** locked to an exact year. The
TL 49: developer's own framing: "the Midpoint plus-or-minus a couple of decades," given the
TL 50: Second Interwar Period's own ~248-year total span — so treat ~2688 as a working
TL 51: central value with a genuine ±~20-year tolerance (very roughly ~2668-2708), not a
RM 122: nothing — the pass will already have been shaped by them.**
RM 123: 
RM 124: **Until Gate 6 fires, run all four `04` Part III.4 substitutes and say in the pass that you did:**
RM 125: own earlier states · the nearest analogous location at another scale · real-world comparables ·
RM 126: the generator-conflict method.
```

## Baseline row (`§N.6`)

| Step/Phase | Date | Round 2 | Round 3 (6 cross-checks) | Caught | Written? |
|---|---|---|---|---|---|
| Mirny Step 0 | 2026-09-29 | UNANIMOUS, 18/18 | 6/6 CONSISTENT; 8 named differences worked, 7 settled by concession, 1 contradiction held for the developer | the four items above, plus 25 single-reader finds kept by union | ✅ `00_Frame.md` |
