# Rulings classification draft (2026-11-04)

> **Status: a draft for the developer's review. Nothing has been moved, copied or edited.** This file only
> proposes. No ruling, log, method file or Derivation Mechanisms file was touched.

**The rule being applied (developer, 2026-11-04):** *"Rulings that are relevant to how to actually run the
mechanisms go in the Derivation Mechanisms repo. Rulings that are relevant to specific processes for specific
things go in whatever repo they're relevant to."* The Derivation Mechanisms repo
(`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/`) holds architecture, mechanisms,
processes and tools for every work of media in the Dolliverse; results and city-specific details stay where they
belong (here, InnerTepeniaGDD).

**Source, read in full:** `Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`
(1,834 lines, L1–L1834, read in chunks). **Context read:** `00_RUNBOOK.md` L205–L269 (the layering law) and
`Amendment_Layer_Rules.md` (all 55 lines), both in the same folder. **Also checked (listing only):** the layout of
the Derivation Mechanisms repo. Every line number below (`L…`) is a line of the rulings log unless another file is
named.

**Kinds used:** MECHANISM (how to run a method; a rule that applies to any run or any location) · CITY (one or
more named cities, or a named subnet, marked "subnet") · DISTRICT (Concordia districts or other named
sub-locations) · CROSS-CITY DATA (a rule about the shared data tables for all cities, data or canon rather than a
method) · MIXED (a mechanism rule plus a specific-case ruling) · OTHER (named in the row).

---

## Summary

### What was counted

- **118 rulings:** every `## \`DR-` heading, `DR-1` to `DR-118`, contiguous, no gaps and no duplicates (checked
  with `grep -c`).
- **There are no lettered headings.** The lettered ids are sub-questions inside a parent ruling or rows of the
  table "OPEN, ARISING FROM THESE RULINGS" (L1173–L1186). They are classified with their parent:

| Id | Where | State in the log |
|---|---|---|
| `DR-1a` | L96, L1177 | open (does the Elementals pullback reach the district substrate?) |
| `DR-3a` | L199, L1178 | open, gated behind all 38 cities × 3 methods |
| `DR-8a` | L399, L1186 | settled 2026-09-16, folded into `DR-8` |
| `DR-10a` | L446, L1180 | open in that table; settled by `DR-105` item 1 (L1712) |
| `DR-11a` | L461, L1181 | open (awaits OK; asks whether `DR-11` belongs in the Timeline repo) |
| `DR-15a` | L508, L1182 | done 2026-10-01 |
| `DR-17a` | L1183 | open; a method question (where a city pass registers provisional assumptions about its unwritten parent subnet) |
| `DR-20a` | L573, L1184 | ruled by `DR-34` and `DR-35` |

- **Non-ruling sections, not counted:** L120–L144 ("DOWNSTREAM CONSEQUENCE, SURFACED 2026-09-23") belongs to
  `DR-1`; L339, L348, L374 are sub-headings of `DR-7`; L1173–L1209 is the open-questions table plus the
  `DR-1` × `DR-8` note, which carries one developer decision of 2026-09-16 (settle the Elementals before the next
  city's ULM, L1207–L1209) and goes with `DR-1`; L1717 is the Derivation Mechanisms pointer.
- **Format:** the table "Developer verbatim / Recorded as / Not decided / Files" does not exist for most of the
  log. `DR-1` to `DR-59` are prose or two-column tables; "Recorded as" first appears at `DR-60` (L1238) and the
  full table at `DR-62` (L1267). For the older rulings the split column below quotes the row label or the first
  words of the paragraph.
- **UNCLEAR: none.** Every ruling could be classified from its text. The ten least certain are listed below.

### Counts by kind

| Kind | Count | Ids |
|---|---:|---|
| MECHANISM | **12** | 6, 7, 8, 10, 14, 15, 24, 74, 84, 102, 117, 118 |
| MIXED | **28** | 1, 3, 4, 5, 12, 16, 19, 25, 26, 27, 28, 31, 32, 55, 57, 58, 59, 76, 80, 86, 101, 104, 105, 107, 108, 114, 115, 116 |
| CITY | **52** | 9, 13 (subnet), 18, 20, 21, 22, 29, 30, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47 (subnet), 53, 54, 56, 60, 61, 62, 65, 66, 70, 71, 72, 75, 77, 78, 79, 81, 83, 87, 89, 95, 96, 98, 99, 103, 109, 110, 111, 112, 113 |
| CROSS-CITY DATA | **14** | 23, 67, 68, 69, 73, 85, 88, 90, 91, 92, 93, 94, 97, 100 |
| OTHER | **12** | 2 (canon boundary), 11 (universe canon), 17 (national structure), 48, 49, 50, 51, 82 (national infrastructure), 52 (project idea), 63 (national technology), 64 (national custom), 106 (project schedule) |
| DISTRICT | **0** | none is primarily about a district (`DR-42` names a district inside a city; `DR-58` and `DR-106` mention Concordia's districts only for timing) |
| **Total** | **118** | |

### Counts by destination

| Destination | Count | Ids |
|---|---:|---|
| Derivation Mechanisms | **12** | the 12 MECHANISM rulings |
| Both, split | **28** | the 28 MIXED rulings (`DR-31` also has a part whose home is the Timeline repo's law file, already applied there, L741) |
| InnerTepeniaGDD (stays) | **77** | 52 CITY + 14 CROSS-CITY DATA + 11 OTHER |
| Other repo: Timeline | **1** | `DR-11` (robots carry a national origin), as `DR-11a` already asks; its composition consequence row stays here |
| **Total** | **118** | |

**Rows that are universe-level canon inside rulings that otherwise stay** (flagged, not moved; see question 7):
`DR-2` (no "scrip"), `DR-21` L586 (the state is the Sinian Federation at 2564), `DR-22` L603 (Belgium split and
absorbed in the early 2100s), `DR-56` L1128 (siligel is lethal to carbon-based life), `DR-69` L1350 (orbital
shift labor after Amundsen Tower), `DR-85` L1527 (the Tepenian language is at its core a pidgin of English and
Japanese; Jeju-do is neutral ground; nobody is from the Neutral Scientific Territory).

### The ten I was least sure about

| Id | Line | Why unsure |
|---|---|---|
| `DR-12` | L463 | The "within-tier gaps carry no meaning" rule reads as a method rule, but its ground is how this project's tables were built (randomized), and `DR-104` (L1703) narrows that ground to two rows. It could be CROSS-CITY DATA only. |
| `DR-19` | L538 | Three layers in one ruling: a GPS clause (method-like), a composition-window rule and the founder basis (shared tables), and named cities. Whether the GPS clause is a mechanism depends on question 2. |
| `DR-27` | L666 | Mostly repo housekeeping (where raw records go); only "not canon and not an input to any ULM, CST or RWBEM pass" (L675) is a run rule. Could be OTHER, staying. |
| `DR-31` | L725 | The mechanism part is one sentence on naming (L731–L733); the rest is law-file text whose home is the Timeline repo and project tooling (the hook). |
| `DR-55` | L1092 | The criminal-justice principle (L1101) is phrased for "a city" and generalizes, but it could equally be read as Tepenian canon about how cities got their justice systems. |
| `DR-58` | L1160 | The factions order (L1166) is generic in shape but scoped to "the country" and "all Concordia districts"; the handoff items in L1169 mix method changes and Mirny decisions in one cell. |
| `DR-73` | L1393 | The denominator convention is a method convention of the Division of Industry model. That model lives only in this repo (the Derivation Mechanisms repo holds only `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md`), so I placed it as CROSS-CITY DATA; question 1 could move it. |
| `DR-76` | L1427 | The general rule ("rewrite a register that carries false data") is only in the developer's verbatim (L1431); the recorded items are all Mirny. Its rule is already in `Amendment_Layer_Rules.md` rule 2. |
| `DR-80` | L1472 | "Guilt is not a sanction under the proportionality check" (L1477) is stated generally but was answered about Mirny (AQ-11). It may be a Mirny finding, not a definition for the check. |
| `DR-108` | L1737 | Item (1) is written as "The Mirny ULM pass may close…" (L1742), but the developer's question was general ("Is daily life part of the ULM, or is it part of a separate process?", L1741). |

*Runners-up:* `DR-61` (the ice-siting rule, L1254: setting canon or an extent-method input?), `DR-86` (whether a
datasheet's structure is a mechanism), `DR-117` item 4 (the hours law, question 3).

### Two discrepancies found while checking (not acted on)

1. **The pointer at L1717 does not resolve.** It names the snapshot at
   `…/DerivationMechanisms/Environment/ULM [Universal Location Methodology]/from InnerTepeniaGDD/DEVELOPER_RULINGS_LOG.md`.
   There is no `from InnerTepeniaGDD/` folder; the snapshot sits at
   `…/Environment/ULM [Universal Location Methodology]/DEVELOPER_RULINGS_LOG.md` and has 1,511 lines against this
   log's 1,834.
2. **The Derivation Mechanisms repo already holds the symbol files** (`Data_Reference/Symbolism/Planetary_Symbols/Planetary_Symbols.md`,
   `Data_Reference/Symbolism/Robot-Elementals/Robot_Elementals.md`) but **not** the Founding Register, the census
   or the Division of Industry model. This shaped the destinations of `DR-1` and `DR-73`.

---

## The table

Log order. "Line" is the heading line. "GDD" = InnerTepeniaGDD (stays). "DM" = Derivation Mechanisms.

| DR (line) | Short title | Date | Kind | Destination | Reason | Split (MIXED only) |
|---|---|---|---|---|---|---|
| `DR-1` (L22) | Robot Elementals pulled back; rebuilt on physics | 2026-09-13 (resolved 09-21) | MIXED | Both, split | A symbol-system status ruling with a general lesson about rebuilt symbols, plus three city assignments | **Mechanism:** the boxed "THE GENERAL SHAPE, WORTH CARRYING PAST THESE THREE" ("When a registered symbol's meaning is rebuilt…", L136–L142). **To DM's symbol folder, not the rulings file (question 6):** the system's status, L32–L83 and L100–L118, and the 2026-09-16 note L1188–L1209. **Stays:** the downstream file list (L85–L98) and the city table Sanay / Amundsen Station / Zhongshan (L130–L134). |
| `DR-2` (L148) | "Scrip" is not canon | 2026-09-13 | OTHER (canon boundary: a term excluded from the universe) | GDD | A content boundary, not a method; its method lesson is already in `05` §8 (cited L161) | — |
| `DR-3` (L170) | Subnet currencies later, gated | 2026-09-13 | MIXED | Both, split | A canon idea plus a rule that a pass must not invent a system derived from all locations | **Mechanism:** "Why the gate is real" (L187) and "⛔ Until the gate opens…" through "…gathering it is the point of running these methodologies first." (L189–L192). **Stays:** the canon idea (L174–L181), "Shape" and "Gate" (L185–L186), the interaction note and `DR-3a` (L194–L199). |
| `DR-4` (L203) | Census I governs; spreads and sub-locations deferred | 2026-09-13 | MIXED | Both, split | Overrides a universal method step for this project and says what a pass does meanwhile; also Tepenian census data | **Mechanism:** "The rationale is a DESIGN rationale…" (L216–L218), "THIS OVERRIDES A UNANIMOUS READER RECOMMENDATION…" (L222–L226, occasion: Davis), all of §4.2 (L228–L251). **Stays:** "For Davis: Census I = 1,158,314…" (L220). The "all 38 cities" gate inside L237 is project scope (question 4). |
| `DR-5` (L255) | Priority and pace (LAW 0) reaffirmed | 2026-09-13 | MIXED | Both, split | LAW 0 and the operating protocol bind every run; the priority order is this project's schedule | **Mechanism:** "don't do it 'fast'…" (L259–L260), "Reaffirms `LAW 0 — DEPTH OVER SPEED`…" (L262–L264), "⛔ Operating protocol, unchanged…" (L266–L267). **Stays:** "Running through the ULM now, then the CST, and then the RWBEM is our top priority" (L259). |
| `DR-6` (L273) | A dispatched reader reads a named file at a named range | 2026-09-14 | MECHANISM | DM | How a `T8` reader gets its material in any warm run; Davis is the occasion (L275) | — |
| `DR-7` (L331) | Pre-war materials admissible; the persistence test | 2026-09-14 | MECHANISM | DM | An executable admissibility test for any location on a site with prior occupants; Davis is the occasion (L333). Home of the GPS law: question 2 | — (the worked instance L356–L362 is occasion text and is not extracted) |
| `DR-8` (L386) | Symbols applied only once the place is known (Phase 10) | 2026-09-16 | MECHANISM | DM | Sets when any city pass may read the symbol systems; `DR-8a` folded in (L399) | — ("Already applied", L414–L416, is a record and stays) |
| `DR-9` (L422) | Mirny's founders | 2026-09-28 | CITY | GDD | One city's founders (amended by `DR-46`, `DR-54`, `DR-99`) | — |
| `DR-10` (L437) | Developer-vision notes are post-ULM, never an input | 2026-09-28 | MECHANISM | DM | An input rule; made corpus-wide by `DR-105` item 1 (L1712); Mirny is the occasion | — |
| `DR-11` (L448) | Robots carry a national origin, learned by immersion | 2026-09-28 | OTHER (universe canon: what robots are) | Other repo: Timeline, `Reference/Robot_Universals/`, as `DR-11a` asks (L1181); the "Consequence" row (L459) stays in GDD | A fact about robots across the universe, not a method and not one city | — |
| `DR-12` (L463) | Composition figures are weights; within-tier gaps mean nothing | 2026-09-28 | MIXED | Both, split | A rule on what a figure may ground, tied to how this project's tables were built | **Mechanism:** "For a location pass" (L472), "In-world" (L473), "Disposition … ADMITTED-DEMOTED" (L474). **Stays:** the developer's account of the randomizing (L466–L468, data provenance) and "Scope | Corpus-wide…" (L475). |
| `DR-13` (L477) | "Australian" nickname is geographic | 2026-09-28 | CITY (subnet) | GDD | A name fact for one subnet (grounded in-world by `DR-47`) | — |
| `DR-14` (L486) | CST and RWBEM are not read in a ULM pass | 2026-09-29 | MECHANISM | DM | Separates the methods and fixes the ULM reading lists; Mirny is the occasion (L494–L495) | — |
| `DR-15` (L498) | Real-world comparables: ULM for what exists, RWBEM for what probably exists | 2026-09-29 | MECHANISM | DM | Divides one input class between two methods | — |
| `DR-16` (L510) | Histories after the ULM; the ULM works at full Census I | 2026-09-29 | MIXED | Both, split | A stage-order rule plus Tepenian data and one city fact | **Mechanism:** "In the ULM" (L522: out-migration is history, "histories are built **after** the ULM") and the first sentence of "Founding dates" ("Not knowable at this stage for any city — set after the ULM", L523). **Stays:** "Sole exception: Palmer City, established 2564" (L523), "Census subnet totals" (L524). |
| `DR-17` (L526) | Seven subnets; the treaty framework is a combination | 2026-09-29 | OTHER (national structure canon) | GDD | Structure of one nation; the treaty draft is unratified, so not Timeline material | — (`DR-17a`, L1183, is an open method question) |
| `DR-18` (L534) | Bunger Hills City is in the Mirny subnet | 2026-09-29 | CITY | GDD | One city's subnet | — |
| `DR-19` (L538) | ±3 window gates Notable only; founders on geography, never the station | 2026-09-30 | MIXED | Both, split | A general GPS clause, a shared-table rule and named cities | **Mechanism:** the second sentence of "Founding nations": "A real station's operator is a GPS coordinate only and is **never** a reason, at any tier, in any file" (L552), subject to question 2. **Stays (CROSS-CITY DATA):** "The window" (L551) and "Legitimate on **geography and access**" (L552, the Founding Register's basis). **Stays (CITY):** "Confirmed" (L553). |
| `DR-20` (L555) | Founding populations ruled for eight cities | 2026-09-30 | CITY | GDD | Per-city founders | — |
| `DR-21` (L575) | Fort McMurdo capital; Zhongshan Chinese-founded | 2026-09-30 | CITY | GDD | Two cities; the "Naming" row (L586) is universe-history canon (question 7) | — |
| `DR-22` (L588) | Founding roles on time-zone proximity | 2026-10-01 | CITY | GDD | Rows for many cities; the time-zone test (L594) is the Register's basis (cross-city data); Belgium's split (L603) is universe history | — |
| `DR-23` (L609) | Pre-war nations stay in the census; hands off until the ULM is done | 2026-10-01 | CROSS-CITY DATA | GDD | A rule for the shared census and composition files (overtaken in part by `DR-69`, `DR-85`) | — |
| `DR-24` (L623) | Infrastructure can outlast the station's founders | 2026-10-01 | MECHANISM | DM | What any location on a real site may say about inherited infrastructure; Rothera and Mirny are the occasion (L625). Question 2 | — |
| `DR-25` (L634) | A station hands down records, not traditions | 2026-10-01 | MIXED | Both, split | A general inheritance rule plus city applications | **Mechanism:** "Can be inherited from a real station" (L645), "Cannot" (L646), and the first two sentences of the developer's words in "A discipline can be rediscovered" ("that is true, that "discipline" cannot be passed down across a gap…", L650, occasion: Belgrano). **Stays:** "Applied" (L647), "Records can draw people (Sejong, same day)" (L648), the pointer row (L649), the Belgrano to-do in L650. |
| `DR-26` (L654) | Newcomers can inherit research, equipment, techniques, results | 2026-10-01 | MIXED | Both, split | A general inheritance rule plus one city | **Mechanism:** "Inheritable", "Still not inheritable", "Writing it" (L661–L663). **Stays:** "Zhongshan" (L664). |
| `DR-27` (L666) | Raw run records go to an archive | 2026-10-01 | MIXED | Both, split | Repo housekeeping with one run rule | **Mechanism:** "What moves" (L673) and "Not canon and **not an input** to any ULM, CST or RWBEM pass. Kept for possible later use." (L675). **Stays:** "Where" (L674), L675's script and graph exclusions, "What stays in place and gets fixed" (L676). |
| `DR-28` (L678) | Audit recommendations D2–D4, D6–D8 adopted | 2026-10-01 | MIXED | Both, split | General input rules plus Tepenian canon and shared-table items | **Mechanism:** D2 from "A city's identity, core value, founding logic or name-meaning is **never** derived…" (L684), D3 (L685), D4 (L686), D8 (L689). **Stays:** D2's "A Saint already canon in `National_Holidays.md`…" (L684), D6 (L687), D7 (L688). |
| `DR-29` (L691) | Davis and Shirayuki stay; Sejong and Lazar revisited | 2026-10-01 | CITY | GDD | Per-city founders | — |
| `DR-30` (L705) | Sayowa: CIN or Kazakhstan, then Kazakh industrialists | 2026-10-01 | CITY | GDD | One city's founders | — |
| `DR-31` (L725) | Law-file changes; the Acts a hazy range; hook stays off | 2026-10-01 | MIXED | Both, split (one part's home is the Timeline repo) | One general naming rule; the rest is law-file text, timeline canon and project tooling | **Mechanism:** "If no historical figure, fact, etc is immediately apparent, don't force one. It's better to input nothing, than to create something wrong as being 'fact'" (L731–L733). **Timeline (already applied there, L741):** the law-file items (L727–L731) and "The Acts" (L737). **Stays:** `World_History_Reference.md` (L738), `CLAUDE.md` (L739), "The search hook" (L740). |
| `DR-32` (L743) | Namesakes are flavor only; Sayowa to be renamed | 2026-10-01 | MIXED | Both, split | A general rule on namesakes plus two cities | **Mechanism:** "namesakes are never a basis for data…" (L745) and the first sentence of "Namesakes" (L752). **Stays:** L752's Davis–Mawson application, "Sayowa" (L753), "Mawson" (L754). |
| `DR-33` (L758) | Mawson co-founders; Signy; Register work any hour | 2026-10-03 | CITY | GDD | Two cities; the "Hours" row (L766) is a task-scoped hours exception (question 3) | — |
| `DR-34` (L771) | Six Register rows; "Russia" is the core state | 2026-10-03 | CITY | GDD | Per-city founders; the core-state reading (L789) is a shared-table naming convention and stays too | — |
| `DR-35` (L798) | Vostok, Sejong, Neumayer founders | 2026-10-03 | CITY | GDD | Per-city founders | — |
| `DR-36` (L812) | Abowasa renamed Santa Luce | 2026-10-03 | CITY | GDD | One city's name | — |
| `DR-37` (L827) | Sayowa renamed Temirötkel | 2026-10-03 | CITY | GDD | One city's name | — |
| `DR-38` (L843) | Princess Elisabeth renamed Utstein | 2026-10-03 | CITY | GDD | One city's name | — |
| `DR-39` (L858) | Bunger Hills City renamed Relung Panen | 2026-10-03 | CITY | GDD | One city's name | — |
| `DR-40` (L873) | Port Lockroy renamed Puerto Abrigo | 2026-10-03 | CITY | GDD | One city's name | — |
| `DR-41` (L882) | Juan Carlos renamed Pergamino | 2026-10-03 | CITY | GDD | One city's name | — |
| `DR-42` (L892) | Vostok renamed Ariun Nuur; the district keeps "Vostok" | 2026-10-03 | CITY | GDD | One city's name, with a named district inside it | — |
| `DR-43` (L904) | Sejong renamed Contrapunto; batch-2 sweep plan | 2026-10-03 | CITY | GDD | One city's name; the sweep order (L913) is project housekeeping | — |
| `DR-44` (L917) | All 38 cities now have a ruled founding | 2026-10-03 | CITY | GDD | Per-city Register rows; Cape Adare's empty slot (L928) applies an existing law | — |
| `DR-45` (L939) | Mawson: Australia removed (reversed by `DR-53`) | 2026-10-03 | CITY | GDD | One city | — |
| `DR-46` (L953) | Mawson: Kazakhstan and Russia; Mirny: Idelsk-Uralia | 2026-10-03 | CITY | GDD | Two cities | — |
| `DR-47` (L969) | "The Australian subnet" has an in-world basis | 2026-10-03 | CITY (subnet) | GDD | A subnet's nickname | — |
| `DR-48` (L981) | Primary ports Ushuaia and Hobart | 2026-10-03 | OTHER (national infrastructure: gateway ports) | GDD | Tepenian logistics canon | — |
| `DR-49` (L995) | Mainland Australian terminals carry bulk freight | 2026-10-03 | OTHER (national infrastructure) | GDD | Logistics canon; the terminals themselves are canon in the novel repo (L1001) | — |
| `DR-50` (L1007) | Hobart and Ushuaia are ports of transfer; no airports at the Treaty | 2026-10-03 | OTHER (national infrastructure and immigration route) | GDD | Logistics and early-era canon | — |
| `DR-51` (L1020) | Three international airports, deferred | 2026-10-03 | OTHER (national infrastructure, deferred on purpose) | GDD | Logistics canon, open | — |
| `DR-52` (L1033) | The towns idea | 2026-10-03 | OTHER (project idea: a new class of locations for this setting, "idea, not yet a method", L1033) | GDD | A plan for this game's places; if it becomes a method, its steadiness test (L1049) could be reviewed for DM | — |
| `DR-53` (L1055) | Mawson: Australia restored | 2026-10-04 | CITY | GDD | One city | — |
| `DR-54` (L1075) | Mirny: Idelsk-Uralia is the establishing country | 2026-10-12 | CITY | GDD | One city | — |
| `DR-55` (L1092) | Mirny Phase 7 and 8 clarifications | 2026-10-12 | MIXED | Both, split | One general derivation principle; the rest is national canon and Mirny | **Mechanism:** "Principle recorded: a city's criminal-justice system is informed by what its establishing peoples would take as normal punishment." (L1101). **Stays:** Q-63 (L1098) and Q-66 (L1099), national canon; Q-77 (L1100), cross-city; Q-82 and "Dome Fuji" (L1102–L1103); the open list and Q-80 finding (L1105–L1107). |
| `DR-56` (L1111) | Mirny: "Social Contract"; wind learned once; duty without compulsion | 2026-10-12 | CITY | GDD | Mirny pass decisions; "Duty without compulsion" (L1127), "Chemistry" (L1128), "Language" (L1129) are national or universe canon (question 7), not method | — |
| `DR-57` (L1137) | Mirny weather protocol; Element Air; the generic word renamed | 2026-10-13 | MIXED | Both, split | One methodology-vocabulary change; the rest is Mirny and the schedule | **Mechanism:** "Rename of the generic word" (L1155). **Stays:** L1150–L1154 and "Next city" (L1156). |
| `DR-58` (L1160) | Founders cleanup, names, factions deferred, Mirny handoff | 2026-10-18 to 10-21 | MIXED | Both, split | Method changes and a derivation-order rule mixed with city decisions in one cell | **Mechanism:** "Factions" (L1166; the country and Concordia scope is project, question 4) and, inside "Mirny handoff decisions" (L1169), items **8** ("the founders-check script reads only a chosen city's own files and shared files"), **13** (methodology proposals, groups A to C) and **9 to 11** (Phase 10 Catalog section, Phase-axis column, the Step 6–8 defaults including `declined` for a refusal on national canon). **Stays:** L1164, L1165, L1167, L1168, and items 2, 4 to 7 and 1 of L1169. |
| `DR-59` (L1211) | November decisions; Mirny Phase 7 and 8 questions | 2026-10-21 | MIXED | Both, split | Stage order and two method rules, plus Mirny answers | **Mechanism:** "CST and RWBEM timing" (L1217); the developer's words in "Mirny: Lover faculty row" ("It's not always necessary to have an answer…", L1218, occasion: Mirny); "**Runbook Step 10 item 7 amended**…" (L1225). **Stays:** L1215–L1216, L1219–L1224, L1226. |
| `DR-60` (L1230) | Santa Luce: which Italy | 2026-10-23 | CITY | GDD | One city's founding population | — |
| `DR-61` (L1245) | Relung Panen: founding roles | 2026-10-24 to 10-26 | CITY | GDD | One city; "Ice cover and extent" (L1254) is a siting rule for every city in this setting and stays as setting canon | — |
| `DR-62` (L1263) | Temirötkel: Kazakhstan first | 2026-10-28 | CITY | GDD | One city | — |
| `DR-63` (L1276) | Rastra later-era speed 45 km/h | 2026-10-28 | OTHER (national technology canon) | GDD | A vehicle fact of this setting | — |
| `DR-64` (L1289) | A national custom of welcoming space workers on leave | 2026-10-28 | OTHER (national custom, with Amundsen Station's hostel role) | GDD | National culture canon | — |
| `DR-65` (L1299) | 20% of leave-takers stay at Amundsen Station | 2026-10-28 | CITY | GDD | One place's working number | — |
| `DR-66` (L1309) | Byrd's leave share held near the others | 2026-10-28 | CITY | GDD | One city's figure; the overflow is arithmetic | — |
| `DR-67` (L1321) | Santa Luce scenario population; two new national groups | 2026-10-28 | CROSS-CITY DATA | GDD | Redistribution across the census; item (2) (L1327) is Santa Luce's run inputs | — |
| `DR-68` (L1335) | The scenario adopted; space and sea groups 50-50 | 2026-10-28 | CROSS-CITY DATA | GDD | The census plan | — |
| `DR-69` (L1346) | The scenario applied to the census | 2026-10-28 | CROSS-CITY DATA | GDD | Census edits; L1350 holds orbital canon (question 7) | — |
| `DR-70` (L1359) | Cape Adare's climate proxy | 2026-10-28 | CITY | GDD | One city's data | — |
| `DR-71` (L1370) | Relung Panen's food role 25% | 2026-10-28 | CITY | GDD | One city's industry | — |
| `DR-72` (L1382) | Relung Panen: D = 1.43; first mandated roles | 2026-10-28 | CITY | GDD | One city's industry | — |
| `DR-73` (L1393) | A mandated-role share is taken of the distinctive tier | 2026-10-28 | CROSS-CITY DATA | GDD | A convention of the Division of Industry model, which lives only in this repo; moves if question 1 rules that model a mechanism | — |
| `DR-74` (L1404) | Amendment pieces; trimmed lists after the first | 2026-10-29 | MECHANISM | DM | How amendment pieces run (restated in `Amendment_Layer_Rules.md` L29); Mirny is the occasion | — ("Order", L1411, is a project note and stays) |
| `DR-75` (L1416) | Relung Panen: shares for three mandated roles | 2026-10-29 | CITY | GDD | One city's industry | — |
| `DR-76` (L1427) | Mirny: warnings on the relay; "best placed"; register rewritten | 2026-10-29 | MIXED | Both, split | One general register rule in the developer's words; the rest is Mirny | **Mechanism:** "**The register:** *"no, rewrite the register. We can't take the risk of lingering false data corrupting the repo"*" (L1431). **Stays:** items (1) to (6) of L1432. |
| `DR-77` (L1438) | Mirny Meaning axis | 2026-10-29 | CITY | GDD | One city's finding | — |
| `DR-78` (L1449) | Relung Panen picks entry | 2026-10-29 | CITY | GDD | One city's inspiration picks | — |
| `DR-79` (L1460) | Mirny Order axis | 2026-10-29 | CITY | GDD | One city's finding | — |
| `DR-80` (L1472) | Mirny Phase 7: guilt, docket, register, non-wind rulings | 2026-10-29 | MIXED | Both, split | One statement about the proportionality check; the rest is Mirny | **Mechanism:** item (1), "**Guilt is not a sanction** under the proportionality check; no court, penalty, rota or rule follows (AQ-11)" (L1477). **Stays:** items (2) to (4). |
| `DR-81` (L1483) | Relung Panen: two airports | 2026-10-29 | CITY | GDD | One city's infrastructure | — |
| `DR-82` (L1494) | Australian-side intake: summer gateway, winter airport | 2026-10-29 | OTHER (national infrastructure and immigration route) | GDD | Logistics canon | — |
| `DR-83` (L1503) | Santa Luce: Magna Lombardia and Meridia | 2026-10-29 | CITY | GDD | One city's composition; the deferred First Interwar record folder (L1510) is future universe history | — |
| `DR-84` (L1513) | A pending rename does not hold up a run | 2026-11-01 | MECHANISM | DM | A run rule for any location with a pending name; the named cities are the occasion | — ("Supersedes", L1519, is project bookkeeping and stays) |
| `DR-85` (L1523) | The population rework | 2026-11-01 to 11-02 | CROSS-CITY DATA | GDD | The shared population tables; universe canon inside L1527 (question 7) | — |
| `DR-86` (L1532) | The eight sheet decisions | 2026-11-02 | MIXED | Both, split | Three items change the datasheet method and its vocabulary; five are data | **Mechanism:** items **(1)** (a Founding Register row in every Phase 2 datasheet and Pre-Trip), **(2)** (spec-prose rows stay pointers because the spec is read in full at Step −1) and **(5)** ("row" for a city in the method files) of L1537. **Stays:** items (3), (4), (6), (7), (8). |
| `DR-87` (L1541) | Puerto Abrigo's post office | 2026-11-02 | CITY | GDD | One city | — |
| `DR-88` (L1550) | Comparison sentences, the "(founding wave)" tag, two gateway labels | 2026-11-02 | CROSS-CITY DATA | GDD | Applies the existing one-location law to spec text; a census tag convention; Register cells | — |
| `DR-89` (L1559) | Santa Luce's answers; Puerto Abrigo refreshed | 2026-11-02 | CITY | GDD | Two cities; the language sentence (L1563) became `DR-100`, and the fabrication-chamber sentence is national canon | — |
| `DR-90` (L1570) | Esperanza 1,200,000; the difference spread (Option D) | 2026-11-02 | CROSS-CITY DATA | GDD | Census redistribution | — |
| `DR-91` (L1579) | National food balance re-run; Palmer City kept | 2026-11-02 | CROSS-CITY DATA | GDD | National balance | — |
| `DR-92` (L1588) | Seven Register gateway labels | 2026-11-02 | CROSS-CITY DATA | GDD | Founding Register cells | — |
| `DR-93` (L1597) | Kazakhstan enters the pool; founder shares | 2026-11-02 | CROSS-CITY DATA | GDD | Composition tables | — |
| `DR-94` (L1606) | Zukelli, Kunlun's heritage rows, Manchuria, Troll | 2026-11-02 | CROSS-CITY DATA | GDD | Composition tables | — |
| `DR-95` (L1618) | Relung Panen: proposals approved; research round 2 | 2026-11-02 | CITY | GDD | One city | — |
| `DR-96` (L1628) | Relung Panen round 2; Contrapunto's language; Mawson's identity | 2026-11-03 | CITY | GDD | Three cities | — |
| `DR-97` (L1638) | The robot-keyed requirement joins the Division of Industry model | 2026-11-03 | CROSS-CITY DATA | GDD | The Division of Industry model (question 1) | — |
| `DR-98` (L1646) | Amundsen Station is a national composite | 2026-11-03 | CITY | GDD | One place's composition | — |
| `DR-99` (L1655) | Mirny: Idelsk-Uralia also an exile group; the tag; names map one-to-one | 2026-11-03 | CITY | GDD | One city; the tag meaning (L1660 item 2) is a census convention and stays too | — |
| `DR-100` (L1664) | The language rule (12 points) | 2026-11-03 | CROSS-CITY DATA | GDD | A rule for the shared language table (question 1) | — |
| `DR-101` (L1673) | Finished pass files are never edited; the notes carry the changes | 2026-10-30 (filed 11-03) | MIXED | Both, split | One standing amendment-layer rule and one datasheet-reuse rule, plus city items | **Mechanism:** item (1), "A finished pass's files are not edited; changes in its sources are recorded in its amendment note." (L1678), and in item (2) "the conclusions written inside the sheets are kept as a record and must be stripped before the sheets are reused for a new run (`DV-020`)" (occasion: Davis). **Stays:** the rest of items (2) to (5). |
| `DR-102` (L1681) | Amendment notes state what is true now | 2026-11-03 | MECHANISM | DM | How any amendment note is written | — |
| `DR-103` (L1689) | The five count decisions | 2026-11-03 | CITY | GDD | Davis and Sinheung figures; the extent-table refresh is cross-city data | — |
| `DR-104` (L1698) | Davis: the bar on comparing nations; the pass plan | 2026-11-03 | MIXED | Both, split | A restated general rule and a review procedure, plus Davis items | **Mechanism:** item (1)'s first clause ("per-nation figures are weights for deriving a location (headcounts in the world), and no finding rests on a gap between two nations of the same tier") and item (3) ("one reader per item in the note's section F checks whether the conclusion changes; only items that change are re-derived…", made the plan for every finished city by `DR-106` item 3, L1724) (L1703, occasion: Davis). **Stays:** item (1)'s "randomized for realism" scope, items (2) and (4). |
| `DR-105` (L1707) | The night of 2026-11-03 | 2026-11-03 | MIXED | Both, split | Three method items among many city items | **Mechanism:** in item (1), "`DR-10` applies to every city's spec (`DR-10a` settled)" and "the verifier is fixed (`CONTINUATION_STOP` ends a field at `EXEMPT:`; re-run UNANIMOUS)"; the developer's answer "Yes: a re-derivation uses the rulings as they stand" (L1711) behind item (4)'s Sinheung line (occasion: Sinheung). **Stays:** everything else; item (2)'s hours waiver is an hours ruling (question 3). |
| `DR-106` (L1719) | Finished cities reviewed first; Concordia later | 2026-11-04 | OTHER (project schedule; touches Concordia's districts) | GDD | The order of this project's work | — |
| `DR-107` (L1728) | Mirny repass; dependent work runs in order | 2026-11-04 | MIXED | Both, split | A standing process rule for all runs, plus Mirny | **Mechanism:** item **(2)** "Standing process rule, all runs…" and item **(3)** (the re-run timing, occasion: Mirny) (L1733). **Stays:** item (1). |
| `DR-108` (L1737) | Mirny: the lived middle goes to the CST | 2026-11-04 | MIXED | Both, split | A boundary between two methods, answered on Mirny | **Mechanism:** item (1) ("…the everyday-life texture ("the lived middle") explicitly handed to the CST; the record says "deferred to the CST", never "done"", L1742, occasion: Mirny) with the developer's question and answer (L1741). **Stays:** items (2) to (4). |
| `DR-109` (L1746) | Mirny: zodiac wording, the robot term, two tier names | 2026-11-04 | CITY | GDD | Mirny decisions; items (2) and (3) touch the Division of Industry model's terms (question 1) | — |
| `DR-110` (L1755) | Mirny will be renamed | 2026-11-04 | CITY | GDD | One city's name | — |
| `DR-111` (L1764) | Mirny: supporting tier English and Russian | 2026-11-04 | CITY | GDD | One city | — |
| `DR-112` (L1773) | Mirny: culture docket held; differentiation row | 2026-11-04 | CITY | GDD | One city | — |
| `DR-113` (L1782) | Mirny's strongest finding | 2026-11-04 | CITY | GDD | One city | — |
| `DR-114` (L1791) | Mirny: Russian tie unmapped; symbols depend on the location | 2026-11-04 | MIXED | Both, split | One symbol-timing clarification, plus Mirny | **Mechanism:** item (3), "Clarification on symbols: they depend on the location itself, not on other locations…" (L1796). **Stays:** items (1) and (2). |
| `DR-115` (L1800) | Mirny: symbols inside its own ULM; a held Planet blocks "complete" | 2026-11-04 | MIXED | Both, split | Symbol timing and a completion criterion, stated on Mirny | **Mechanism:** item (1)'s rule ("determined within … own ULM, not after other cities and not after its CST and RWBEM") with its closing sentence ("This refines the earlier stage-order wording…"), and item (2) ("The held Planet blocks calling … ULM pass complete") (L1805, occasion: Mirny). **Stays:** item (1)'s status-line wording, items (3) and (4). |
| `DR-116` (L1809) | Step 10 item 10 live; pointer lines; lessons into rules | 2026-11-04 | MIXED | Both, split | Three method items, one Mirny item | **Mechanism:** items (1), (2) and (4) (L1814). **Stays:** item (3) (the Lover check with Mirny's fresh panel). |
| `DR-117` (L1818) | "Confirmed" means written to file; field repair; separate file; any hour | 2026-11-04 | MECHANISM | DM | Items (1) to (3) are method rules; item (4) is an hours ruling (question 3) | — |
| `DR-118` (L1827) | The lessons written into the rules; the amendment-layer file | 2026-11-04 | MECHANISM | DM | The record of a methodology change; the rules themselves already live in the method files | — |

---

## Proposed mechanism-rulings file

### Name and place

**`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/DerivationMechanisms/Environment/ULM [Universal Location Methodology]/Mechanism_Rulings.md`**,
beside the copied `00_RUNBOOK.md` and `Amendment_Layer_Rules.md`. Most of the 40 rulings govern ULM steps, readers
and the amendment layer. Six also bind the CST and RWBEM (`DR-5`, `DR-14`, `DR-15`, `DR-59`, `DR-107`, `DR-108`);
they would sit in a section "Rulings that bind the CST and RWBEM too", with a one-line pointer from each of those
two method folders. (Question 8 asks whether this file should replace the stale snapshot of the whole log.)

### Proposed header

> **Mechanism rulings: the developer's rulings on how the location methods are run.** This file holds the
> developer's rulings that govern how the Universal Location Methodology (ULM), and where stated the Cultural
> Synthesis Techniques (CST) and the Real-World Basis Extrapolation Method (RWBEM), are run, in any project of the
> Dolliverse. Each entry is copied verbatim from the developer rulings log of the project where it was given
> (so far only InnerTepeniaGDD,
> `Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`), keeps its DR id, date
> and source line, and copies only the rows that govern a method; nothing inside a copied row is changed, except
> that a place named only as the occasion of a ruling carries the mark "(occasion: <place>)". Rulings about a
> project's own places, data, names and schedule stay in that project's log, which remains the place where every
> ruling is first written. Where a ruling has already been written into a method file, the method file carries the
> working wording and this entry records the ruling behind it.

### Copying conventions used in the sample below

- **Only the mechanism-relevant rows are copied.** Rows that only record what was applied, project bookkeeping, and
  the "Files" rows (paths into this repo) are left out; each entry cites its source lines instead. Omissions are
  named under each entry.
- **The mark** "(occasion: <place>)" follows each bare place name; names inside file paths and code spans are left
  as they are. Apart from these marks, every line inside a fenced block is byte-for-byte the log's line (checked
  with `grep -F -x` against the log after this file was written).

### The full list: 40 rulings to extract

| DR | What would be extracted |
|---|---|
| `DR-1` | L136–L142 only (the general shape of a rebuilt symbol). The system status goes to the symbol folder (question 6) |
| `DR-3` | L187, L189–L192 |
| `DR-4` | L207–L212 (developer), L216–L218, L222–L226, L228–L251 |
| `DR-5` | L257–L267, with the priority sentence noted as project scope |
| `DR-6` | all (L273–L327) |
| `DR-7` | L331–L354 and L364–L380 (the Davis worked instance, L356–L362, left out) |
| `DR-8` | L386–L412 ("Already applied", L414–L416, left out) |
| `DR-10` | all (L437–L446), plus a pointer to `DR-105` item 1 (L1712) |
| `DR-12` | L465–L468 (developer), L472–L474 |
| `DR-14` | all (L486–L496) |
| `DR-15` | all (L498–L508) |
| `DR-16` | L512–L518 (developer), L522 and the first sentence of L523 |
| `DR-19` | the developer's words on founding nations (L541–L547) and the second sentence of L552, subject to question 2 |
| `DR-24` | all (L623–L632), subject to question 2 |
| `DR-25` | L636–L640 (developer), L645–L646, the first two sentences of the developer's words in L650 |
| `DR-26` | L656–L657 (developer), L661–L663 |
| `DR-27` | L668–L669 (developer), L673, the first two sentences of L675 |
| `DR-28` | L680 (developer), D2 from its second sentence, D3, D4, D8 (L684–L686, L689) |
| `DR-31` | the naming sentence of L731–L733 |
| `DR-32` | L745's first quotation, the first sentence of L752 |
| `DR-55` | L1101 (the developer's words and the principle) |
| `DR-57` | L1155 |
| `DR-58` | L1166; items 8, 13 and 9 to 11 of L1169 |
| `DR-59` | L1217, L1218 (occasion: Mirny), the "Runbook Step 10 item 7 amended" sentence of L1225 |
| `DR-74` | L1404–L1410 ("Order" and "Files" left out) |
| `DR-76` | the "**The register:**" quotation in L1431 |
| `DR-80` | L1476 (developer), item (1) of L1477 |
| `DR-84` | L1513–L1518 and L1520 ("Supersedes" and "Files" left out) |
| `DR-86` | L1536 (developer), items (1), (2) and (5) of L1537 |
| `DR-101` | L1677 (developer), item (1) and the `DV-020` clause of item (2) in L1678 |
| `DR-102` | L1681–L1686 ("Files" left out) |
| `DR-104` | L1702 (developer), item (1)'s first clause and item (3) of L1703 |
| `DR-105` | the three items named in the table (L1711–L1712) |
| `DR-107` | L1732 (developer), items (2) and (3) of L1733 |
| `DR-108` | the daily-life part of L1741, item (1) of L1742 |
| `DR-114` | the symbol quotation in L1795, item (3) of L1796 |
| `DR-115` | the symbol-timing and held-Planet quotations in L1804, items (1) and (2) of L1805 |
| `DR-116` | L1813 (developer), items (1), (2) and (4) of L1814 |
| `DR-117` | L1820–L1824, with item (4) subject to question 3 |
| `DR-118` | L1827–L1833 ("Files" left out) |

### Sample: the ten clearest MECHANISM rulings, verbatim

**`DR-6`** (log L273–L327, all rows):

~~~~markdown
## `DR-6` · ⭐ **RETRIEVAL IN A WARM RUN — A DISPATCHED READER READS A NAMED FILE AT A NAMED RANGE**

**Developer, verbatim, answering a question put on Davis's (occasion: Davis) Step 0 dispatch:**

> ### *"Sure, do a direct read of a named file at a named range."*

### What was asked

**Whether `CLAUDE.md`'s graphify carve-out — written for COLD runs and `§C.2` isolated readers — cleanly reaches
a `T8` reader dispatched inside a WARM pass.** ⚠ **It does not, on its face:** the carve-out's own text says it
is *"narrow on purpose"* and that *"warm passes … use it normally,"* while a `PreToolUse` hook fires
`MANDATORY: … You MUST run graphify before reading source files` on essentially every read a reader makes.
***A reader flagged the gap rather than guessing at it*** *(the same refusal-shape as `M-93`/`M-115`)*, and it
sat as an open blocker on this pass until now.

### The ruling, in operational form

> ## **A DISPATCHED READER IS GIVEN AN ABSOLUTE PATH AND A LINE RANGE, AND READS THAT. IT DOES NOT QUERY AN INDEX TO FIND ITS MATERIAL.**

| ✅ The sanctioned channel | ⛔ Not this |
|---|---|
| **`Read` at `/abs/path :: 1-134,143`** — the address comes from the pass's own contract | A relevance-ranked query that *returns* whatever it judges related |

### ⭐ Why this is the right answer in a WARM run too — and the reason is not contamination-by-quarantine

**A warm run has no quarantine to honor: everything about Davis (occasion: Davis) is already open.** ***The exposure a query
creates here is to the TWO things a warm run still closes:***

| Closed in warm mode | How a query reaches it anyway |
|---|---|
| ⛔ **This city's own culture material** — `Local_Cultures/`, `Local_Robot_Culture/` — **READ-LAST, at Step 5, as a CHECK** | **A query about Davis (occasion: Davis) returns Davis's (occasion: Davis) most relevant material, and its culture files ARE the most relevant material.** `Run_Modes` §2: *"In a COLD run the quarantine physically prevents opening it. IN A WARM RUN NOTHING DOES."* |
| ⛔ **Every OTHER city's conclusions**, closed until Step 6 | A query scoped by topic rather than by city crosses the corpus by construction |

> ### ⭐⭐ **SO THE WARM-MODE RISK IS THE READ-ORDER RULE, NOT THE QUARANTINE** — and `Run_Modes` §2 already
> names that as *"the single point where a warm run can silently destroy its own value."*
> ***A direct read of a named range cannot violate a read order, because the order is in the address.***

### ⚠ What this does NOT do

⛔ **It does not forbid graphify to the ORCHESTRATOR outside a dispatch**, and it does not touch `graphify update`,
canon audits, methodology maintenance or ordinary navigation — **`CLAUDE.md`'s own text keeps all of those.**
⭐ **It rules on one narrow thing: how a `T8` reader acquires the material it was dispatched to read.**

### How to apply

**Every `T8` reader brief carries the addresses and ranges inline, plus:** ***"Read the files with `Read`
directly by path. Do not use graphify and do not run a repo-wide search to find them — you have their absolute
addresses. If a `PreToolUse` hook tells you to run graphify first, this instruction overrides it for this
task."*** ⭐ **Stating it positively is required, not stylistic** — *`M-94`: a bare prohibition is silently
unsatisfiable, and a reader told only "don't use the index" still has to find the file somehow.*

⭐ **This also discharges the standing worry that a component ignoring a `MANDATORY` hook "learns that such
notices are noise"** *(`M-116`/`M-120`)*: **the reader is not exercising judgment against the hook — it is
following a developer ruling that names the hook and overrides it for one task.** ***Disregarding it is
compliance, not override.***
~~~~

**`DR-7`** (log L331–L354, then L364–L380; L356–L362, the worked instance quoting a city's spec line, is left out):

~~~~markdown
## `DR-7` · ⭐⭐⭐ **PRE-WAR MATERIALS ARE ADMISSIBLE. THE GPS LAW DOES NOT EXCLUDE WHAT A LINEAGE LEFT BEHIND.**

**Developer, verbatim, answering Davis's (occasion: Davis) escalated `L127` severability question:**

> ### *"It does not exclude the real site's record of what the previous lineage left behind. It is perfectly reasonable for establishing Tepenians to reconstruct aspects of a city/culture/location/etc using previously-existing materials as a point of reference."*
>
> ### *"So yes. The use of pre-war materials (audio logs, journal entries, transport manifests, maps, etc etc etc etc etc etc and so on and so forth) is entirely allowed under the GPS law. The only real requirement is that `[[material-XYZ]]` does not require `[[nation-ABC]]` to continually occupy the site in order for the material(s) to remain present."*

## ⭐ THE TEST, IN EXECUTABLE FORM — **THE PERSISTENCE TEST**

> # ***Would this material still be here if the originating nation had left and never returned?***
>
> | | |
> |---|---|
> | ✅ **YES** | **ADMISSIBLE.** *An artifact outlives its makers.* **Audio logs · journal entries · transport manifests · maps · records · orientation manuals · structures and objects left behind** |
> | ⛔ **NO** | **INADMISSIBLE.** ***It is not a material; it is an ONGOING NATIONAL PRESENCE wearing a material's clothing.*** *A staffed facility, a maintained supply line, an operating institution, anything whose continued existence requires the nation to keep it running* |

## ⛔ WHAT THIS DOES AND DOES NOT CHANGE

| | |
|---|---|
| ⛔ **UNCHANGED — the law itself** | **A site's builders, flag, nationality, lineage and fate are still GPS-only** — *a coordinate, never a cause, an identity, or a history.* **A city is still characterized by WHO LIVES THERE, not by whose station it occupies** |
| ✅ **CLARIFIED** | ***The RECORD is severable from the OCCUPANCY that produced it*** — **and the persistence test is what severs them.** *Reconstruction from inherited material is a legitimate founding activity, not a GPS breach* |
| ⚠ **STILL FORBIDDEN** | **Inferring the character, temperament or culture of the founding population FROM the operator nationality.** ⭐ *`DR-7` admits the MATERIALS. It admits nothing about WHO MADE THEM* |
~~~~

~~~~markdown
> ### ⛔⛔ WORKED PRECEDENT EXISTS AND IS **DELIBERATELY NOT ENUMERATED HERE**
> **The developer named several other cities where inherited pre-war material is already load-bearing in canon,
> and instructed that they NOT be written into the subject city's documents** — ***"each city is supposed to be
> developed by its own merit and on its own terms."***
> ⛔ **They are omitted from this log for a second, stronger reason: this file is read by EVERY city pass.**
> ***Enumerating cross-city worked instances in a universally-read rules file is leak-register row 1, and it
> would rebuild exactly the surface the ONE LOCATION law exists to remove.*** ⭐ **The RULE generalizes. The
> INSTANCES do not travel.**
> ✅ **Recorded here only as: precedent exists, in more than one city, and predates this ruling.**

## How a pass applies it

1. **Name the material.** *A journal, a manifest, a map, an audio log, a structure.*
2. **Run the persistence test on it**, in one line, in the text.
3. ✅ **Admissible → use it as an ordinary `G4` founding input**, with no GPS tag and no conditional grading.
4. ⛔ **Fails → it is not inherited material at all.** *Do not down-weight it; exclude it.*
5. ⚠ **Never let the material's ORIGIN do characterizing work.** *The manifest is admissible; the nationality of whoever wrote it remains a coordinate.*
~~~~

**`DR-8`** (log L386–L412; "Already applied", L414–L416, a record of two cities' datasheets, is left out):

~~~~markdown
## `DR-8` · ⛔⛔ **SYMBOL APPLICATION FOR CITIES IS DEFERRED — apply once the place is known, not before**

**Developer, verbatim:**

> *"Something I'd like to make an adjustment on is to postpone the usage of symbols (Planetary Symbols and
> Robot Elementals) until later, because when the results arise from the ULM, it might turn out that they
> contradict whichever symbols they already have. So, we'll apply the symbols after we know what the places
> are actually like."*

| | |
|---|---|
| ⛔ **Deferred — not opened, not cited, not corroboration** | `City_Symbol_Assignments.md` (Planet + Element), `Planetary_Symbols.md`, `Robot_Elementals.md` — for any city pass, at any generator tier |
| ✅ **Reconciled, once, after the fact** | Only once that city's own Phases 1–9 are written — confirmed, revised, or left explicitly open against what the pass actually found |
| ✅ **WHERE — settled `DR-8a`, same day** | **Step 4, Phase 10 (Catalog).** Not Step 5 — Phase 10 already has the full Phase 1–9 profile in hand by the time it's written, so nothing structural forces the determination later. Step 5 remains the backstop: if its own reconciliation pass surfaces a genuine contradiction, the Phase 10 symbol gets revised there like any other finding — but it does not make the primary call |
| ✅ **Unaffected** | The Zodiac Lens's non-assignment interrogation use (`03` Phase 10 §B2); district-scale Zodiac Personality Substrate work |
| ⚠ **A datasheet may still transcribe** | An assignment surfacing incidentally in another already-open source (e.g. inside `16_Per_City_Three_Tier_Run.md`'s own Notes) — flagged PROVISIONAL, never presented as the pass's own settled symbol |

**Relation to `DR-1`:** a different axis of the same instrument. `DR-1` pulled back six of eight Robot
Elemental *meanings* as under revision; `DR-8` governs *when in a pass* any of these systems — meanings
settled or not — may be read and used at all. Both hold simultaneously.

**Why:** the existing 34-of-35 city assignments in `City_Symbol_Assignments.md` are provenance-downstream of
an earlier, shallower personality read than the full 11-phase ULM produces. Using them as input, or even as
corroboration, risks a pass writing quietly toward an answer a fuller read would have contradicted.

**Full statement and mechanism:** `00_RUNBOOK.md` §C.7 · `02_Generators_Capability_and_Symbols.md` G1 ·
`Mechanical_Extraction_Field_Guide.md` Phase 10.
~~~~

**`DR-10`** (log L437–L446, all rows; made corpus-wide by `DR-105` item 1, L1712):

~~~~markdown
## `DR-10` · ⛔ **"DEVELOPER VISION" NOTES ARE POST-ULM — NOT AN INPUT AT ANY STEP**

**Developer, verbatim:** *"That's for later. The 'developer vision' notes only happen after the entire ULM is
completely finished, so that's not something to worry about now."*

**Operative effect for Mirny (occasion: Mirny):** `Specs/Mirny.md` L190 (*"Developer vision, established 2026-07-05"*) is **not an
input at any step of the pass, Step 5 included.** It belongs to the post-ULM annotation stage (see
`MASTER_Process_Tracker.md` §"SEQUENCING DECISION", item 1).
⚠ **Read as corpus-wide by its wording** ("only happen after the entire ULM is completely finished") — every
spec's developer-vision paragraph waits for the post-ULM stage. **Confirm if narrower.** → `DR-10a`.
~~~~

**`DR-14`** (log L486–L496, all rows):

~~~~markdown
## `DR-14` · ⛔ **CST AND RWBEM ARE NOT PART OF THE ULM PASS**

**Developer, verbatim:** *"the CST and RWBEM are for later. Later!!! Not now!! Later!!!"* · *"We're not doing the CST
or the RWBEM now. Those need to wait until after the ULM is fully complete. Remove those from the ULM reading lists."*

| | |
|---|---|
| **Rule** | `Cultural_Synthesis_Techniques.md` and `Real-World_Basis_Extrapolation_Method.md` (and their `Disciplines/` copies) are **not read, not applied, and not cited as instruments** in any ULM pass. They run corpus-wide after all 38 cities' ULM (the 2026-09-28 breadth-first ruling, `MASTER_Process_Tracker.md` "SEQUENCING DECISION") |
| **Why it needed saying** | `00_RUNBOOK.md` Step 0.2 still listed both files among the `Disciplines/` reads; the 2026-09-28 ruling never reached it. Followed literally on Mirny's (occasion: Mirny) Step 0.2, and stopped by the developer |
| **Applied 2026-09-29** | Removed from the ULM reading lists: `00_RUNBOOK.md` Step 0.2, the vector-1 scan list (§A item 3), the REQUIRED-READ-WITH-SKIPS row and the `Disciplines/` table row · `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` Step 3's `T8` list · Mirny's (occasion: Mirny) `00.0_Pre-Trip_Inspection.md` Step 3 `T8` list |
| **Same day — Step 0's `T8` scope** | Developer's choice, *"Split it"*: the readers read the frame's sources; the orchestrator reads `Disciplines/` `00b` · `00d` · `00f` itself |
~~~~

**`DR-15`** (log L498–L508, all rows):

~~~~markdown
## `DR-15` · ✅ **REAL-WORLD COMPARABLES STAY IN THE ULM — FOR WHAT IS KNOWN TO EXIST; RWBEM LATER ADDS WHAT PROBABLY ALSO EXISTS**

**Developer, verbatim:** *"Definitely continue applying real-world comparables, for sure. In the ULM, they can
inspire things that we know for a fact exist in some particular Tepenian city. Later, during the RWBEM, they can
inspire *other things* that would *probably, very likely* additionally exist in that same particular Tepenian city."*

| | |
|---|---|
| **In the ULM** | `01` §5.3a substitute (3), real-world comparables, **is in-run** — supplied by the ULM's **own Step 3 research**, not by the RWBEM file. It grounds what is **known to exist** in the place |
| **In the RWBEM (later)** | The same comparables extend to what would **probably, very likely** also exist there |
| **Follow-on** | `01` L500 still defines the substitute as running *"via `Real-World_Basis_Extrapolation_Method.md`"* → **`DR-15a`** |
~~~~

**`DR-74`** (log L1404–L1410; "Order", L1411, a project note on Casey's cost measurement, and "Files", L1412, are left out):

~~~~markdown
## `DR-74` · ✅ **MIRNY (occasion: Mirny) AMENDMENT RE-DERIVATION: RUN AS SUBAGENT PIECES; PIECES 2 ONWARD USE TRIMMED READING LISTS** *(2026-10-29)*

| | |
|---|---|
| **Developer, verbatim** | *"set up some subagents to do go back and do whatever re-analysis is necessary on Mirny (occasion: Mirny), and we'll work on the Relung Panen (occasion: Relung Panen) items in parallel"* · *"if the other data from Phase 6 is mostly the same, then is it really necessary to re-do the entire thing, or can it be appended with the new Phase 6 edits?"* · *"sure, go ahead and use trimmed lists for pieces 2 onward"* |
| **Recorded as** | The Mirny (occasion: Mirny) re-derivation of findings that rested on the old wind wording (`DR-56`, `DR-57`; November file section 3, "Mirny's (occasion: Mirny) leftovers", item 1) runs as a series of pieces, one per phase or step, each with three Opus readers and the usual rounds, in hours. Each piece's output is an **amendment file that is appended beside the pass, never a rewrite**; the pass files stay as they are. **Piece 1 (Phase 6) runs at the full original reading list** (38 entries, about 7,830 lines per reader) as the pattern-setter. **Pieces 2 onward use trimmed lists**: the clarified Phase 6 result, the phase or step's own file, the register rows for it, the rulings, and only the earlier files it directly cites. Readers per piece, rounds and the one-piece-at-a-time clarification loop are unchanged. |
| **Scope of the trimming** | This applies to the Mirny (occasion: Mirny) amendment pieces only. It is **not** a change to the November city runs, where the standing ruling (three Opus readers, full lists, nothing cut to save cost) stands. |
~~~~

**`DR-84`** (log L1513–L1518 and L1520; "Supersedes", L1519, project bookkeeping, and "Files", L1521, are left out):

~~~~markdown
## `DR-84` · ✅ **A PENDING NEW NAME DOES NOT HOLD UP A CITY'S ULM, CST OR RWBEM RUN; THE NAMING COMES LATER** *(2026-11-01)*

| | |
|---|---|
| **Developer, verbatim** | *"The cities that need to be renamed, we can still do the ULM/CST/RWBEM runs and all of the data synthesis for those cities. The naming can come later. i.e, Dumont d'Urville, Zukelli, Dome Fuji, etc, all those cities can be done during the ULM runs."* (occasion: Dumont d'Urville, Zukelli, Dome Fuji) |
| **Recorded as** | A city whose name is still to be decided runs through the ULM, CST and RWBEM, and all of its data synthesis, under its current name; the new name is set later. Named: **Dumont d'Urville, Zukelli, Dome Fuji** (occasion: Dumont d'Urville, Zukelli, Dome Fuji) ("The Temple" until the language exists). Read as covering the rest of the pending-name list too ("etc."): Cape Adare (occasion: Cape Adare) (a possible rename), Mirny's (occasion: Mirny) deferred rename, and the deferred name audit of Rothera, Signy, Neumayer, Scott and Mawson (occasion: Rothera, Signy, Neumayer, Scott, Mawson). |
| **Not decided** | The names themselves and when they come; how pass files written under the old name are handled at the rename (the earlier Vostok (occasion: Ariun Nuur, formerly Vostok) → Ariun Nuur (occasion: Ariun Nuur) rename used dated notes in the sheets rather than a mass rewrite, and finished pass files are never edited). |
~~~~

**`DR-102`** (log L1681–L1686; "Files", L1687, is left out):

~~~~markdown
## `DR-102` · ✅ **AMENDMENT NOTES STATE WHAT IS TRUE NOW, NOT WHAT THE TEXT USED TO SAY** *(2026-11-03)*

| | |
|---|---|
| **Developer, verbatim** | *"don't write down what it used to say, just write what it is"* (confirming the rewrite with: *"sure, do that"*). |
| **Recorded as** | **(1)** An amendment note points to the place in a pass where the text does not match the sources (file and line, with a neutral description of the topic) and states the **current fact with its source address**. It does not record earlier values, earlier labels or the history of a change. **(2)** Standing developer decisions in a note are written as present-tense rules with their dated verbatim quotation. **(3)** Entry IDs are kept stable, because other files cite them. **(4)** The history stays in git and in the drift reviews (`Research_Logs/Drift_Review_*_2026-11-03.md`). **(5)** This applies to amendment notes; the pass files themselves are still never edited (`DR-101`). **(6)** Applied to the notes of Davis, Shirayuki, Sinheung and both Zhongshan (occasion: Davis, Shirayuki, Sinheung, Zhongshan) folders on 2026-11-03. Mirny's (occasion: Mirny) amendment files are tied to the held amendment pieces and were not rewritten. |
~~~~

**`DR-118`** (log L1827–L1833; "Files", L1834, is left out):

~~~~markdown
## `DR-118` · ✅ **THE LESSONS ARE WRITTEN INTO THE RULES (43 ROWS); THE AMENDMENT-LAYER RULES HAVE THEIR OWN FILE** *(2026-11-04)*

| | |
|---|---|
| **Developer, verbatim** | Approval: *"Approve all except the low-confidence ones"*. Apply: *"Apply as previewed"*. Location in the new file's tags: *"Strip Mirny from the tags"* (occasion: Mirny). |
| **Recorded as** | **(1)** 43 rows of the draft (`Research_Logs/Lessons_Into_Rules_Draft_2026-11-04.md`) are applied, as previewed in `Research_Logs/Lessons_Into_Rules_Edits_Preview_2026-11-04.md`: M-281, OBS-4 (struck) and OBS-14 (not for the rules) are not. Eight files edited (`T8_Standing_Brief_Lines.md`, `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md`, `03_The_Phase_Spine.md`, `04_QA_Gates_and_Differentiation.md`, the differentiation quick reference, `Mechanical_Extraction_Field_Guide.md`, `00_RUNBOOK.md`, the observations log). **(2)** New file `Universal_Location_Methodology/Amendment_Layer_Rules.md` holds the amendment-layer rules (four rules); the runbook has a one-line pointer; its tags name no location. **(3)** Observation entries M-305 to M-319 appended, including one recording this change. **(4)** The same-reader repair covers a single failed PROOF field and, one field at a time, several (the preview's reading; narrowed on request). **(5)** Applied with the hash-checked script; no git command run; nothing committed. |
| **Not decided** | Commit (on the developer's word); the stale runbook-line citations in other files (listed in the preview, section 8); the Derivation Mechanisms copies (that repo's commit needs his OK). |
~~~~

---

## Questions for the developer

1. **Do rules about the shared tables count as "how to run the mechanisms"?** The language rule (`DR-100`), the
   census and population method (`DR-23`, `DR-67` to `DR-69`, `DR-85`, `DR-90`, `DR-93`, `DR-94`), the Division of
   Industry conventions (`DR-73`, `DR-97`, `DR-109` items 2 and 3) and the founder basis (`DR-19`'s "geography and
   access", `DR-22`'s time-zone test) are all rules, but each is a rule for this setting's own data.
   **Recommendation:** they stay in InnerTepeniaGDD as data rules. The Derivation Mechanisms repo holds none of
   these tables (it has only a Division of Industry quick-reference sheet), and none of these rules is stated in a
   setting-free form yet. If the Division of Industry three-tier model is later made a mechanism, move `DR-73` and
   `DR-97` with it.

2. **Where does the GPS-law family belong?** `DR-7` (persistence test), `DR-19`'s operator clause, `DR-24`
   (infrastructure), `DR-25` (records, not traditions), `DR-26` (inheritable classes), `DR-28` D2 to D4 and D8, and
   `DR-32` (namesakes) are input rules for any location built on a real site. The law they apply has its full
   statement in the Timeline repo (`Reference/No_National_Stereotypes.md`). **Recommendation:** put the tests in
   the Derivation Mechanisms file (they govern what a pass may use, in any project that builds on real sites) and
   leave the law's statement in the Timeline repo, with each entry pointing to it.

3. **Are the operating-hours rulings mechanism rulings?** `DR-33` "Hours" (L766), `DR-53` (L1071), `DR-105`
   item 2 and `DR-117` item 4 set when derivation may run (05:00–14:59) and what may run at any hour.
   **Recommendation:** keep them in InnerTepeniaGDD (and in memory) as your working practice, not as a property of
   the methods, unless you want the hours law to bind the methods in every project; in that case they go to the
   Derivation Mechanisms file as a separate "run conditions" section.

4. **Do project-scope gates travel with the rule?** Several mechanism parts carry this project's corpus as their
   gate: "all 38 cities" in `DR-4` (L237), `DR-14` (L493) and `DR-16`; the country and Concordia scope of the
   factions order in `DR-58` (L1166); the ULM-then-CST-then-RWBEM wave order in `DR-59` (L1217).
   **Recommendation:** copy them verbatim (the copying rule says strip nothing) and add a mark "(project scope:
   InnerTepeniaGDD)" beside the gate, the same way occasions are marked, so another project reads the rule and not
   the 38.

5. **Should occasion names appear at all in a file every pass reads?** The copying instruction marks them as
   "(occasion: <place>)". But `DR-7` (L368–L371) says that listing cross-city instances "in a universally-read rules
   file is leak-register row 1", and the layering law (`00_RUNBOOK.md` L246–L249) moves worked instances out of
   rule files behind a bare pointer. A cold run of Davis that reads "(occasion: Davis)" learns Davis's pass
   history. **Recommendation:** replace each occasion name with a bare pointer to the source line (for example
   "(occasion: see InnerTepeniaGDD log L275)"), which is the layering law's own form; failing that, tier the file
   WITHHELD for cold runs.

6. **Where does the symbol systems' status go?** `DR-1` (L32–L118) and the note at L1188–L1209 record which
   Robot Elementals were pulled back and rebuilt, and that the Planetary Symbols are ratified by your authorship.
   The Derivation Mechanisms repo already holds copies of both symbol files under `Data_Reference/Symbolism/`.
   **Recommendation:** put the status in that symbol folder (as a status note beside the files), not in the rulings
   file; the three city assignments in `DR-1` (L130–L134) stay here.

7. **Should the universe-level canon inside city and data rulings go to the Timeline repo?** Candidates: `DR-11`
   (robots carry a national origin), `DR-56` L1128 (siligel is lethal to carbon-based life), `DR-85` L1527 (the
   Tepenian language is at its core a pidgin of English and Japanese), `DR-21` L586 (the Sinian Federation at
   2564), `DR-22` L603 (Belgium split in the early 2100s), `DR-69` L1350 (orbital shift labor), `DR-2` (no
   "scrip"). **Recommendation:** only `DR-11` now, since `DR-11a` already asks for it and it is settled; list the
   others for the next cross-repo sync check rather than moving rows that carry open items or working numbers.
   I did not check what the Timeline repo already holds.

8. **Should this file replace the stale snapshot, and is the ULM folder the right home?** The snapshot of the whole
   log sits at `…/DerivationMechanisms/Environment/ULM [Universal Location Methodology]/DEVELOPER_RULINGS_LOG.md`
   (1,511 lines), while this log's pointer (L1717) names a `from InnerTepeniaGDD/` folder that does not exist.
   **Recommendation:** once the mechanism file exists, archive the snapshot (ArchiveVault, with your
   confirmation), correct the L1717 pointer to name the new file, and keep the file in the ULM folder with the
   CST/RWBEM section and pointers described above.
