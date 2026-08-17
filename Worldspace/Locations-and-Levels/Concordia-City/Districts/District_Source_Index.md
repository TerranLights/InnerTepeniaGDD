# District Source Index

**Written 2026-08-16.** Companion file to `District_Culture_Development_Plan.md` — a full inventory of every
file in the repo that carries real content about each of Concordia's 13 districts, so Phases 1-8 have a known
source base to work from instead of re-discovering it district by district. Built from a direct structural
audit of the `Districts/` folder plus a dedicated repo-wide sweep (`Storyline/`, `Worldspace/` outside
Districts, `Game-Mechanics/`, `Dev-Road-Map/`, `Background-Lore/`, `Neo-Races-and-Cultures/`, `TODO.md`,
`DONE.md`) for cross-references living elsewhere. `Reference/Materials/` (real-world books/PDFs) was excluded —
not game content, pure noise for this purpose.

**How to read this file:** Part 1 lists sources that apply to all 13 districts uniformly (same file pattern,
different district plugged in, or one shared file with a section per district). Part 2 lists genuine
district-specific extras — the material that doesn't exist symmetrically across all 13, which is exactly the
material most worth knowing about before starting Phases 1-8.

---

## Part 1 — Universal sources (apply to all 13 identically)

### Per-district dedicated files (one set per district, `{NN}` = district number, `{Name}` = district name)

| File | What it is |
|---|---|
| `District_Megasheets/{NN}_{Name}/README.md` | current-era district overview |
| `District_Megasheets/{NN}_{Name}/{Name}_Mega_Init.md` | current-era Hard Facts / founding-init data |
| `District_Megasheets/{NN}_{Name}/{Name}_Full_Extrapolation.md` | current-era Roman-numeral Findings — **this is where Phases 1-8 content gets appended** |
| `District_Megasheets/{NN}_{Name}/{Name}_Cross_Reference_Synthesis.md` | current-era inter-district Findings |
| `District_Megasheets_PreWar/{NN}_{Name}/` (same 4 files) | identical structure, pre-war state |
| `Deep_Dives/{NN}_{Name}_Deep_Dive.md` | narrative-finding deep dive, diaspora-informed |
| `District_Vision_Notes/{Name}.md` | freeform developer vision notes |
| `District_History_Enhancement_Opportunities/{NN}_{Name}.md` | flagged history-enrichment opportunities |
| `Final_Megasheet_Data_Processing/Patterns/in-district_patterns/{NN}_{Name}.md` | 4 recurring narrative Patterns (indexed in `Patterns/pattern_sheet.md`) |
| `Final_Megasheet_Data_Processing/Questlines/in-district_questlines/{NN}_{Name}.md` | questline seed material |
| `Final_Megasheet_Data_Processing/Throughways/in-district_throughways/{NN}_{Name}.md` | physical throughway/circulation data |
| `Worldspace/Characters/District-Quest-NPCs/{Name}_Quest_NPCs.md` | named quest-NPC roster |

### Shared cross-district files (one file, section or row per district)

| File | What it is |
|---|---|
| `District_Canon_Reference.md` | canon reference — What It Really Is / Historical Pressures / Cultural Texture / Inhabitants / Community Infrastructure, per district |
| `District_Refugee_Diaspora_Composition.md` | weighted outer-city diaspora composition + named cultural transplants, per district |
| `Regional-Characteristics/district_summaries_with_traits_and_features.md` | quick-reference trait/feature summary |
| `Regional-Characteristics/District_Prominent_Features.md` | landmark features |
| `Regional-Characteristics/district_pairings_-_districts_and_their_natural_allies.md` | natural-ally pairings |
| `Regional-Characteristics/district_by_Enneagram_group_series.md` | Enneagram-group personality mapping |
| `Regional-Characteristics/Concordia_Radio_-_radio_stations_by_district.md` | radio station per district |
| `Historical_Pressures.md` | historical-pressure synthesis |
| `Historical_Inter-District_Effects.md` | how districts' histories affected each other |
| `District_Natural_Allies.md` | ally-relationship rationale |
| `District_Unity_of_Opposites.md` | paired-opposite thematic relationships |
| `general_problems.md` | known unresolved problems per district |
| `Cross_District_Additive_Lore_Prospects.md` | positive/additive cross-district lore opportunities |
| `Cross_District_Non_Malice_Audit.md` | audit ensuring no district's portrayal reads as malicious-by-default (complete, see `DONE.md`) |
| `Cross_District_Power_Leverage_Alternatives.md` | power-leverage dynamics between districts |
| `Quest-Triggers.md` | quest-trigger conditions tied to district state |
| `Hostility/District_Hostile_Actions.md`, `District_Hostile_Justifications.md`, `Player-Instigated_Violence_-_Understandable_Reasons.md`, `Overlapping_District_Hostile_Actions_-_01/02/03_*.md` (6 files) | district hostility mechanics and justification |
| `Continuity_and_Stability_Act_Requirements.md` | the founding legal framework binding all districts |
| `Independent_Lattice_Guidelines.md` | Lattice (energy grid) rules affecting all districts |
| `Tepenian_Criminal_Justice_System.md` | justice-system application across districts |
| `Concordia_Ultra_Megasheet/` (4 files: `README.md`, `Concordia_Mega_Init.md`, `Concordia_Full_Extrapolation.md`, `Concordia_Cross_Reference_Synthesis.md`) | city-wide synthesis sitting above all 13 districts |
| `00b_Two_Stage_Methodology.md`, `conflicts_in_relation_to_the_main_story_-_preliminary_suggestions.md` | methodology / main-story conflict framing |
| `../Concordia_Second_Interwar_Cultural_Sheet.md`, `../World_Map_Boundaries.md`, `../city-and-district_layout_-_preliminary_suggestions.md` | Concordia-level layout/founding/climate context |
| `Outside-World/Tepenian-Federation/Locations/Cities/Specs/Concordia.md` | Concordia's own city-spec entry among the outer-city Specs files |
| `Outside-World/Tepenian-Federation/Locations/Cities/City_Refugee_District_Affinities.md` | reverse-direction map: all 35 outer cities → their top-3 Concordia district refugee-affinity picks |
| `Reference/Images/Maps/Concordia_City_-_Extended_map_-_with_labels_-_Color-Coded_by_District.jpeg` | the actual color-coded radial city map — confirms Hub-centric layout, wildly uneven district sizes (Sagittarius/Capricorn huge outer-ring giants with no Hub contact vs. Gemini/Leo/Aquarius/Scorpio/Aries/Virgo/Libra small Hub-adjacent wedges), and the 3 highway ramps (2 in Sagittarius, 1 at Capricorn/Sagittarius border) — load-bearing for all 8 phases, see `District_Culture_Development_Plan.md`'s Governing Methodology §4 |

### Storyline / mechanics files with a per-district slice (confirmed genuinely symmetric)

| File | What it is |
|---|---|
| `Storyline/Side-Content/District_Under_Questlines.md` | 15-20 non-capstone quest candidates per district (~1500 lines) |
| `Storyline/Side-Content/District_Main_Questlines.md` | one capstone "internal conflict" quest per district |
| `Storyline/Side-Content/District_Quest_Consequence_Web.md` | capstone-resolution ripple effects across all 13 + Act 3 |
| `Storyline/Side-Content/District_Under_Questline_Design_Method.md` | the generation method itself |
| `Storyline/Endings/Main-Endings/Climax_Structure_and_District_Ending_Consequences.md` | per-district main-climax ending consequence |
| `Storyline/Endings/Secret-Endings/District_Idolized_Endings.md` | one "maximum commitment" secret ending per district |
| `Storyline/Endings/Secret-Endings/Failsafes.md` | 27 Pariah endings requiring Hated/Vilified across all 13 |
| `Storyline/Minmax-Builds/*/Unique_Interactions_-_High.md` + `*_-_Low.md` (35 build folders, ~70 files) | per-district (12, excludes Hub) quest-hook breakdown per build |
| `Game-Mechanics/Perks/SOC_Cross_Reference_Perk_Concepts.md`, `SOC_Archetype_Perk_Brainstorm.md`, `post-Idolization_Questline_Perks.md` | district-identity-keyed perk concepts, capstone signature perks |
| `Game-Mechanics/Combat/Damage_Types.md`, `District_Armor_Augmentations_and_Protection.md` | district-flavored damage sources/armor |
| `Worldspace/Locations-and-Levels/Player_Homes.md`, `Romance_Unlocked_Homes.md` | player/companion homes organized by district |

---

## Part 2 — District-specific material (the genuinely uneven part)

### 01 — Cancer
- **Extra Deep Dive:** `01b_Cancer_Rationing_of_Grief_Alternatives.md`
- **Staging:** `03_Calethina_Lab_Historical_Pressures_Fix.md` — Calethina's activation lab sits at the Cancer/Taurus/Capricorn corner (also relevant to Taurus, Capricorn)
- **Doll home (undecided candidates only):** `TBN [TCY-45 heavenly summertime Momo]` (Cancer/Leo/Taurus, undecided), `TBN [XT-03 thicc Chinese Mei-Li]` (Leo or Cancer, undecided)
- **Human recruitable:** `Worldspace/Characters/Humans/recruitable/Unnamed_Cancer_Defector/README.md` — home explicitly Cancer
- `Worldspace/Characters/Character_Concept_Bank.md` — a Cancer implant-practitioner concept
- `Game-Mechanics/Character-Creation/Permanent_MACHINE_Stat_Increases.md` — Cancer's implant practitioner is the system's own worked example
- `Dev-Road-Map/Demo_Content_Specification.md`, `Storyline/Main-Story/Main_Quest_Revised_Beat_Structure_TENTATIVE.md` — Calethina's lab/demo opener sits on the Cancer/Taurus border
- `TODO.md` — Ayako Hayashi's Wild Child/Cancer route (Red Spiral HQ)

### 02 — Taurus
- **Doll homes (confirmed):** `Favi della Torre`, `TBN [IT-021 white shirt Fenny]`, `Trisha Miller` (non-recruitable), `Majyao Bisyugota` (non-recruitable)
- **Doll home (undecided candidate):** `TBN [TCY-45 heavenly summertime Momo]` (Cancer/Leo/Taurus, undecided)
- `Romance_Unlocked_Homes.md` — Favi's and Majyao's Taurus dome-cluster residences described
- `Neo-Races-and-Cultures/Palmer_Subnet/Juan_Carlos/Juan_Carlos_Catalog.md` + `Background-Lore/Cities/Palmer_Subnet/Juan_Carlos/*` — Juan Carlos's hosted-gathering tradition exported into Taurus (also Leo, Pisces)
- `Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md` — Favi/Taurus is a Beat 2 critical-path companion
- `TODO.md` — Taurus security-network official name still open; Favi's Libra-antagonism companion-quest route

### 03 — Leo
- **Extra Deep Dive:** `03b_Leo_Star_War_Alternatives.md`
- **Staging:** `02_Cymatics_Leo_Reconciliation.md`
- **Doll homes (confirmed):** `Villena Hiresvett`, `TBN [FW-25 Pink Lucy]`, `TBN [TCY-06 red-dress Palmer City Elva]`, `TBN [TCY-42 ravishing extravagant Lillian]`
- **Doll homes (undecided candidates):** `TBN [TCY-45 heavenly summertime Momo]`, `TBN [XT-03 thicc Chinese Mei-Li]`
- `Neo-Races-and-Cultures/Palmer_Subnet/Juan_Carlos/*` — same diaspora-tradition export into Leo (also Taurus, Pisces)
- `TODO.md` — Star War house affiliations (Villena/Elva/Lillian); Cymaticism's effect on Leo's performance culture; "Golden Ring" confirmed NOT an official district name despite 18 files using it (see [[project_leo_star_war_resolution_and_rename_pending]]); Meyzan Yocazhda's Leo-vs-Capricorn job debate (resolved to Capricorn)
- `Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md` — Leo's music scene flagged for launch-quality original music; main quest route explicitly skips Leo (fully optional)

### 04 — Scorpio
- **Doll homes (confirmed):** `Seica Cenilaithe`, `TBN [TCY-25 smoldering darkness Rui]`
- **Staging:** `11_Scorpio_Aries_Black_Silence_Connection.md`
- `Game-Mechanics/Core-Mechanics/Player_Re-Spec_-_Complete_Design.md` — "Scorpio Rebirth Ritual," a named respec method with unique fragmentation-cost mechanics
- `Game-Mechanics/Core-Mechanics/Fragmentation_Matrix.md` — Scorpio tagged "high-Bond, low-Grief" (with Aries)
- `City_Refugee_District_Affinities.md` — Scorpio is the Stage 2 Override destination for the 4 destroyed/ruined cities' refugees (trauma-driven, not cultural affinity)
- `TODO.md` — Rui/Seica deferred-companion sequencing; Seica's occupation/Archive of Final Confessions engagement still open

### 05 — Aries
- **Doll home (confirmed):** `Lyuba (Lyubochka) Baranova` — specific building/area still TBD
- **Staging:** `01_Aries_Tower_Grid_Connection.md`, `11_Scorpio_Aries_Black_Silence_Connection.md`
- `Storyline/Endings/Secret-Endings/Hidden_Paths_And_Secret_Endings.md` — the Aries energy crisis is the central Lattice-bypass secret-ending mechanic
- `Game-Mechanics/Combat/Damage_Types.md` — destabilizing Aries increases Lightning/EMP/Plasma hazards city-wide
- `Worldspace/Energy_Grid_Failure_Rationale.md` — Aries-adjacent grid-crisis faction politics
- `TODO.md` — Lyuba confirmed for the final EA companion slot ("Aries, no district overlap")

### 06 — Capricorn
- **Extra Deep Dive:** `06b_Capricorn_Alternative_Conditions.md`
- **Staging:** `07_Capricorn_Robot_Rights_National_Parallel.md`, `03_Calethina_Lab_Historical_Pressures_Fix.md` (border)
- **Doll home (confirmed):** `IT-068 [Flora]`, `Meyzan Yocazhda` (resolved to Capricorn over Leo)
- **Resolved-negative:** `Still-Present_-_In-Game/recruitable/Kendra Heinrich/README.md` — Capricorn was previously stated as her home but flagged as never actually confirmed
- `TODO.md` — Flora's Capricorn industrial-maintenance background, recruitment at Thermal Distribution Junction 12; **Capricorn's core injustice mechanism still not chosen** (4 contenders shortlisted, see `Deep_Dives/06b_...`)
- `Dev-Road-Map/03-Phase-1-Foundations.md`, `01-Completion-Matrix.md`, `Weekly_To-Do_-_Current.md`, `Demo_Content_Specification.md` — Capricorn's open injustice-mechanism repeatedly flagged; demo's recommended endpoint is "end of Beat 1 (Capricorn)"

### 07 — Aquarius
- **Doll home (confirmed):** `Ji-Eun Kim` — hidden within the district, testing facility now ruins
- **Resolved-negative:** `Still-Present_-_In-Game/recruitable/TBN [XT-17 unorthodox science teacher Charlene]/README.md` — explicitly corrected AWAY from Aquarius, now placed at Vostok
- `TODO.md` — Ji-Eun's Wild Child/Aquarius persuasion-leverage route; Aquarius's "Lattice Swap" signature effect
- `Game-Mechanics/Character-Creation/Permanent_MACHINE_Stat_Increases.md` — Aquarius canonically has the city's highest rate of MACHINE stat implants

### 08 — Libra
- **Staging:** `12_Libra_Emergency_Timeline_Precision.md`
- **Doll home (confirmed):** `TBN [XT-30 professional can-do go-getter Luna]`
- `TODO.md` — Libra is the shared antagonist-institution for both Michelle Stanton's and Vosora Lashár Tanslock's companion quests (different sympathetic officials each); Villena's Wild Child/Libra route; relocated Antarctica flag debated for a Libra government building; Continuity & Stability Act citations partly in "Libra's Treaty Archive Vaults"
- `Storyline/Main-Story/Main_Quest_Revised_Beat_Structure_TENTATIVE.md` — Libra confirmed as a newly-added beat
- `City_Refugee_District_Affinities.md` / `DONE.md` — Palmer City's Libra affinity explicitly framed as "too small for anything beyond quiet private observance"

### 09 — Gemini
- **Staging:** `06_Gemini_Terra_Nova_Bay_Verify.md`
- **Doll homes (confirmed):** `Michelle Stanton`, `Vosora Lashár Tanslock` — both "Gemini / Janbogo (Information district)"
- `TODO.md` — Michelle and Vosora run the same Great Corruption investigation from different angles; Vosora deferred to Launch with an EA data-stash substitution; Gemini's official name resolved to "The Circuit" (2026-07-29)
- `Worldspace/Factions/district_conflicts_-_initial_preliminary_suggestions_-_001.md`, `District_Quest_Consequence_Web.md`'s "Gemini: The Speed of Truth" chain
- `Game-Mechanics/Core-Mechanics/Accomplishment_Weight_System.md` — Gemini is the worked example for the 100-point History Points mechanic

### 10 — Pisces
- **Extra Deep Dives:** `10b_Pisces_Flood_Mechanism.md`, `10c_Pisces_Black_Market_Origin.md`, `10d_Pisces_Tolerance_Pact.md`
- **Doll home (confirmed):** `Naizelle d'Edjordoś`
- **Doll home (undecided candidate):** `TBN [FR-03 billiards Maria]` (Hub or Pisces, undecided)
- `Neo-Races-and-Cultures/Palmer_Subnet/Juan_Carlos/*` — same diaspora-tradition export into Pisces (also Leo, Taurus)
- `TODO.md` — Naizelle's Wild Child/Pisces route; her own Design Notes flag she'd feel at home in Virgo despite living in Pisces (genuine Pisces↔Virgo cross-reference)
- `Game-Mechanics/Core-Mechanics/XP_System_Design_Reference.md` — Pisces black-market fence runs cited as a repeatable XP-farming example

### 11 — Sagittarius
- **Staging:** `09_Sagittarius_Long_Haul_Parallel.md`
- **Doll home (confirmed):** `Heather Wendell` — the Frostlands; main-game-vs-DLC placement still open
- `Worldspace/Characters/Upper-Earth_Defectors/Upper_Earth_Defectors_-_Main_Summary.md` — Sagittarius (the Frostlands) is the main Upper Earth defector settlement location
- `Game-Mechanics/Combat/Damage_Types.md` — Sagittarius Frostlands is the in-world source for Cold/Cryogenic damage
- `City_Refugee_District_Affinities.md` — repeatedly a top-3 pick for several outer cities

### 12 — Virgo
- **Staging:** `08_Virgo_National_Kinship_Recognition.md`
- **No doll currently has Virgo as a confirmed home district** — genuine anchor-character gap, worth flagging before Phase 6/7
- `Naizelle d'Edjordoś/README.md` — lives in Pisces but "would feel very much at home in Virgo," flagged for Undergrid-tie companion perks
- `IT-068 [Flora]/README.md` — approval gains tied to "Capricorn (TBN), Virgo/The Undergrid" industrial-worker sympathy
- `Worldspace/Characters/Character_Concept_Bank.md` — a reassigned concept built around Virgo's Undergrid oral tradition and "Deep Level" exploration (originally drafted for Naizelle)
- `Storyline/Endings/Secret-Endings/Hidden_Paths_And_Secret_Endings.md` — the Lattice bypass discovery trigger sits in a specific Virgo Undergrid corridor
- `Worldspace/Factions/Cross_City_Cultural_Patterns.md` — Virgo cited in a cross-district underappreciation pattern (Cancer/Taurus/Leo underappreciate Aries; Aries underappreciates Virgo)

### 13 — Hub (Axis Mundi)
- **Staging:** `10_Hub_Bridge_Memorial_Sayowa_Reading.md`
- **Doll homes (confirmed):** `TBN [XT-21 cool citygirl Angelina]`, `TBN [TCY-20 unimpressed bartender Miranda]`
- **Doll home (undecided candidate):** `TBN [FR-03 billiards Maria]` (Hub or Pisces, undecided)
- `TODO.md` — Hub's official name confirmed "Axis Mundi"; the Hub's Princess Elisabeth finding resolves the Bridge Memorial ceremony problem; Miranda's Hub-bartender role
- `District_Main_Questlines.md` — capstone quest "Without Inscription"; `District_Idolized_Endings.md` — "The True Nexus"
- `World_Map_Boundaries.md`, `City_Logistics.md` — Concordia is a radial city centered on the Hub, other 12 districts ringing it
- **False-positive warning:** the word "hub" appears constantly as a *generic* term (transit hub, Arcanet hub, Mawson's "The Hub That Chose Kindness," Lazar's "commercial hub") across `Background-Lore/` and `Neo-Races-and-Cultures/` — none of those are this district; already filtered out of this index

---

## Known real gaps this index surfaces

- **Virgo has no confirmed anchor doll/companion** — every other district has at least one. Worth deciding
  whether this matters before Phase 6 (Thematic Breadth) or Phase 8 (Robot-Specific Culture) reach Virgo.
- **Capricorn's core injustice mechanism** is still an open decision (4 contenders, `06b_Capricorn_Alternative_Conditions.md`) — this plausibly blocks a clean Phase 5/6 pass for Capricorn specifically.
- **Three dolls have undecided district homes** touching Cancer/Leo/Taurus (`Momo`, `Mei-Li`) and Hub/Pisces
  (`Maria`) — resolving these isn't required to run Phases 1-8, but content written for the affected districts
  should stay compatible with either outcome until resolved.
