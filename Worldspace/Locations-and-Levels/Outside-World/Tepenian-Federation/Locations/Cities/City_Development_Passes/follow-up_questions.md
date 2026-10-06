# Follow-up questions — items that need a developer decision

**How this file works.** Anything the run cannot settle without you goes here, instead of stopping the run. Each item says what it
blocks (usually nothing yet), what the run is doing in the meantime, and what your answer would change. Answer in any order, any time;
the run continues on the stated default until you do. Newest section first.

---

## At a glance — 53 open items *(updated 2026-10-06)*

| # | Item | Where it bites | Default while open |
|--:|---|---|---|
| FQ-56–FQ-64 | **Mirny Phase 8 (Making), 9 questions** (Q-74…Q-82): the Borrowed Form at Phase 8 and whether a sky-name for a wind is an instrument · do the two bodies dress alike · siligel's lethality to humans · the record's language · siligel at Mirny's cold · the glitch-coolant placement · any food tier at Mirny · how a human child acquires speech · the catalog's windbreak premise (docket) | Phases 9–10; Step 5 | the stated defaults (PA-48…PA-56) |
| FQ-45–FQ-55 | **Mirny Phase 7 (Order), 11 questions** (Q-63…Q-73): what "mandated" means in-world · which figure governs, §20's 23.6 % or Half B's 11.8 % (docket) · the Industrial mandate's basis · a chamber at Mirny · whether the harbor watch's call is public and binding · which sector carries the watch and the extraction crews · Law 1 and handing off a post · the quarry's one fraction or two · the Register's justice line against `H42` · the superseded `01` on the MUST-OPEN list · the nineteenth slot | Phases 8–10; Step 5 | the stated defaults (PA-38…PA-47) |
| FQ-38–FQ-44 | **Mirny Phase 6 (Meaning), 7 questions** (Q-56…Q-62): the `National_Holidays` Mirny entry and `DS6`/`INH` docket · any faith meant at Mirny · whether the record is written in · Independence Day with a sunrise · robot death where no faith is sited (reserved) · who calls the open water · the Borrowed Form's trigger. Full text in the section below | Phases 7–10; Step 5 | stated defaults below; none blocks Phase 7 |
| FQ-26–FQ-37 | **Mirny Phase 5 (Relation & Geometry), 12 questions** (Q-44…Q-55): Idelsk-Uralia's founding role and the "stock" wording · who restores the relay · the port's tier · the inland spur · routing vs access · `RV-1` and the subnet's name · `CRD` L55 · 5b deferral · the radio-standard view · the L184 re-map docket. Full text in the section below | Phases 6–10, the Frame's wording | stated defaults below; none blocks Phase 6 |
| FQ-19 | **Batch 2 renames** (developer, 2026-10-03): ✅ Port Lockroy → **Puerto Abrigo** (`DR-40`) · ✅ Juan Carlos → **Pergamino** (`DR-41`) · ✅ Vostok → **Ariun Nuur** (`DR-42`, district keeps "Vostok") · ✅ Sejong → **Contrapunto** (`DR-43`). Mirny is "eventually". **Non-held files swept 2026-10-03** (alias table §7); open: demonyms, native-speaker slang checks (Chilean/Rioplatense), hyphenation and district boundaries for Ariun Nuur | the 6 held files get both batches after the Mirny pass (`Tools/rename_sweep_held_files.py`) | old names stay in the 6 held files until then |
| FQ-18 | **Rename follow-ups** (all four names ruled and swept 2026-10-03, `DR-36`–`DR-39`): demonyms for the four new names · Utstein vs Utsteinen in-game · ✅ the 6 held files (ruled: sweep after the Mirny pass) · Sayowa's first establisher · Santa Luce's two pronunciations · Relung Panen's Malay form | nothing blocks the Mirny run | old names kept in held files and records; `City_Renames_Alias_Table_2026-10-03.md` |
| FQ-5 | Finish the founding-nations sheet (`Founding_Register.md`): is it the right sheet; when; in what order. **You asked for this "sooner rather than later."** | every pass that needs founders (18 rows open or overturned) | Register untouched |
| FQ-12 | 47.1 % freedom margin: share of people or of a working life; the parked 11.8 % (**Phase 7 answered the 11.8 % half**, P7-2; the people-or-a-life half stays open and now attaches to 35.3 %) | Phases 4, 6, 7 | stated as printed, an upper bound |
| FQ-11 | Any public wind call at Mirny? | Phases 4–7 | none assumed; written as a fork |
| FQ-10 | What keeps the shared night where there is none (~29 days)? | Phases 4–7 | "whatever keeps time"; no hour claimed |
| FQ-6 | What is the ring (solid, porous, earthwork; closed; roofed)? | Phases 3, 5, 10 | unspecified wind-fortified perimeter |
| FQ-7 | Rock or "coastal ice" under the city? | Phases 3, 4, 5 | both branches carried |
| FQ-8 | Which sea-ice calendar governs (spec notes or research)? | Phases 3–5, 7 | both stated; neither adjudicated |
| FQ-9 | OK to re-map the contract's spec map (five lines edited 2026-10-01) and fix the Frame's L150 quote? | every later phase that reads the spec | five lines not used |
| FQ-1 | Human eligibility for exile: four ties or "could afford robots"? | Phase 9 | four ties (treaty text) |
| FQ-2 | Do robots keep arriving after 2564? | Phase 2 robot rows | unproven; not assumed |
| FQ-3 | Does the census's "founding wave" note constrain founding order? | Phases 6, 9 | nothing rests on it |
| FQ-4 | OK to stop the pass files saying "unratified"? | wording only | "draft, not locked" in new files |

*Datasheet docket (needs your OK, never applied): `Datasheets/Phase_4.md`'s header wording ("of the DISTINCTIVE tier") and its cold-file label ("the governing mechanic").*

---

## Mirny · Step 4 · Phase 8 (Making), written 2026-10-06

*Source: `Mirny_Subnet/Mirny/04_Phase_08_Making.md` (questions Q-74…Q-82). None of these blocks any phase.*

- **FQ-56 · The Borrowed Form at Phase 8, and whether a name is an instrument (Q-74).** Phase 8 fired the trigger at form level for the record (the amended copy) and for naming the winds. Confirm, or hold it for Step 5 (with FQ-44). Inside it: does a spoken name for a wind told by its sky count as an instrument that changes the compact? The three readers split three ways. **Default:** held as a test; no wind name written.
- **FQ-57 · Do robots and humans dress alike (Q-75)?** `D08` asks it nationally. At Mirny they are alike outdoors by function. Is a city meant to inflect it, and is indoor dress meant to differ? **Default:** alike outdoors by function; the rest open (PA-48).
- **FQ-58 · Is siligel lethal to humans as canon (Q-76)?** The brief says one dose "would absolutely kill a human", apart from the chemistry proposal. And does a robot take anything at all from human food? **Default:** developer-stated, not ruled; nothing crosses (PA-51).
- **FQ-59 · The record's language (Q-77).** It cannot be inferred from the station. Rule it, or leave it a mystery of the record? **Default:** open.
- **FQ-60 · Siligel at Mirny's ordinary cold (Q-78).** Does it keep its form below freezing, and can it be carried and eaten outdoors? **Default:** indoor replenishment only; no outdoor robot meal.
- **FQ-61 · Mirny on the glitch-coolant axis (Q-79).** A developer placement, or open until Step 5 / Phase 9? **Default:** not placed.
- **FQ-62 · Any food tier at Mirny (Q-80)?** Especially the summer outdoor tier on the coast. **Default:** none sited (PA-49).
- **FQ-63 · How a human born here comes to speak (Q-81).** By the robot Language Module's rule, or per city? **Default:** null for humans (PA-53).
- **FQ-64 · The catalog's Mirny premise (Q-82) — a docket.** `WIC`'s two Mirny items cite a windbreak/turbine city; the admitted lines give only an outer wind-fortified ring. Review when the catalog opens after the corpus. **Default:** nothing proposed.

---

## Mirny · Step 4 · Phase 7 (Order), written 2026-10-06

*Source: `Mirny_Subnet/Mirny/04_Phase_07_Order.md` (questions Q-63…Q-73). None of these blocks any phase.*

- **FQ-45 · What does "mandated" mean in-world? (Q-63).** In the Division of Industry the mandated tier is "would the nation suffer materially without it?" Is that only a classification of national need, or does any obligation attach to a person — may a refusal carry a consequence? This moves:
  - whether any sanction can exist for refusing mandated work (it would sit against Law 1);
  - who arbitrates a shortage at the quarry;
  - how a person moves between tiers.

  **Default:** a need-test only; no compulsion and no holder (PA-39).
- **FQ-46 · Which Mirny figure governs? (Q-64) — a docket, never applied.** `16` §20 (23.6 % mandated, 35.3 % free) was written after Half B's row (11.8 % / 47.1 %) and names the omission. **Default:** §20 governs (PA-38); nothing edited. Needs your OK to (a) annotate `16` L275 when the six held files are swept after the Mirny pass and (b) correct the earlier Mirny text listed in the 27-row table in the Phase 7 file after Phase 10.
- **FQ-47 · The Industrial mandate's basis (Q-65).** §20 grounds it on "developer ruling C" and on a developer-vision note that `DR-10` bars as an input. Is the ruling to stand without the note, or does its conclusion need a home in an admitted file? **Default:** the ruling stands; chain 1 rests on the spec, chain 2's national character on the ruling alone.
- **FQ-48 · A chamber at Mirny (Q-66).** The files say "almost every city" has an installed chamber and name one exception (not Mirny). Is Mirny meant to have one by default? This moves who is built here (Phases 4, 8, 9) and the build-initiation question. **Default:** a chamber by default, undated (PA-40).
- **FQ-49 · The harbor watch's call (Q-67).** Is the live call on wind and ice public, answered for, and binding on any ship or person — and who pays for harbor readiness? Pairs with FQ-11, FQ-33 and FQ-43. **Default:** a call by practice with no written authority; payer unstated.
- **FQ-50 · Where the harbor watch and the extraction crews are booked (Q-68).** Maritime (free) or baseline logistics; extraction under Industrial or Other; does the Maritime sector include ice-edge and fast-ice work; should the sector that carries the one inward lifeline be classed free? **Default:** the harbor watch unplaced; Maritime's breadth includes ice-edge work (PA-44).
- **FQ-51 · Law 1 and handing off a post (Q-69).** Does a robot's capacity to decide mean she may hand off any post, and does equality before the law give a human the same? **Default:** no admitted line compels anyone into a storm; a post may be handed off (PA-42).
- **FQ-52 · The quarry's two claims (Q-70).** Do the eastern-highway materials and the chamber raw material draw on one fraction of the output or separable ones? If separable, the conflict may not exist. **Default:** both carried; no arbiter in any admitted file.
- **FQ-53 · Justice (Q-71) — a docket.** The Division of Industry Register's C6 row says "Canon establishes a three-tier criminal justice system" and the Pre-Trip lists "Factions + criminal justice"; `H42` (2026-09-16) says per-area justice is undeveloped. **Default:** `H42` governs; nothing derived.
- **FQ-54 · The superseded `01` (Q-72) — a docket.** The spine's MUST-OPEN list and the Pre-Trip name `01_Burden_Scoring_Model.md`, which the Division of Industry README stamps superseded. Remove or annotate? **Default:** opened, no figure used.
- **FQ-55 · The nineteenth industry slot (Q-73).** The Register reserves each city a slot "the one that sounds insane until context makes it inevitable". Considered for Mirny inside the ULM at all, or only after the corpus? **Default:** an empty slot is a result; left open.

*Datasheet docket (needs your OK, never applied): `Datasheets/Phase_7.md`'s line anchors into `16` (it cites L2077–2128; Mirny's §20 is at L2105–2173), its "canon's own words" row that reproduces a developer-vision note, and its Sweep line (a text-coverage gap, not a fact about Mirny).*

---

## Mirny · Step 4 · Phase 6 (Meaning), written 2026-10-05

*Source: `Mirny_Subnet/Mirny/04_Phase_06_Meaning.md` (questions Q-56…Q-62). None of these blocks any phase.*

- **FQ-38 · Docket (Q-56; needs your OK, never applied).** `National_Holidays.md` L109–115, "Two Days a Year (Mirny)", has three problems:
  - its source is a Background-Lore vignette;
  - it calls itself "war-proof", which is post-war framing;
  - it uses the retracted symmetric light model.

  Related: `Datasheets/Phase_6.md` calls the entry "canon to build FROM" and mis-anchors it, and `01_Inherited.md` #1 quotes `SPEC` L150 from its EXCLUDED 613–701 span. **Options:** (a) correct; (b) withdraw; (c) leave for the post-ULM rewrite. **Default:** nothing edited; the entry is not an input.
- **FQ-39 · Any faith at Mirny? (Q-57).** On the opened roster no faith is sited at Mirny and none naturally fits; four roster folders are empty. Is "no faith sited" the intended state? **Default:** slot open; residents may hold national faiths as individuals.
- **FQ-40 · The record (Q-58).** Do Mirny's residents write in the inherited record (amend it, verify it, enter a loss in it), and did the founders keep a record of the founding? This moves:
  - the founding finding;
  - the "amended copy as the compact's dissent";
  - a yearly open-water record.

  **Default:** neither assumed.
- **FQ-41 · Independence Day with a sunrise (Q-59).** At Mirny the sun clears the horizon on June 21. Is the national "darkest day" reading meant to reach Mirny inflected? **Default:** relation only; whether residents mark the noon sun is reserved (RF-12).
- **FQ-42 · Reserved docket (Q-60).** When the mortuary question opens: `Robot_Physiology` L174 says robot death is handled by "religion and community"; at a city with no sited faith, does that leave community? **Default:** nothing written (`RV-4`).
- **FQ-43 · The called water (Q-61).** Does the harbor watch publicly call the year's first open water? Pairs with FQ-11 (public wind call) and FQ-33 (the harbor). **Default:** a candidate observance, called on the day.
- **FQ-44 · The Borrowed Form's trigger (Q-62).** Does an empty observance category fire the Borrowed Form, or is the trigger reserved for Phase 8? **Default:** fired narrowly — at §D as [D] (the amended record as the compact's dissent, not adopted) and as resemblance only in §E.

---

## Mirny · Step 4 · Phase 5 (Relation & Geometry), written 2026-10-05

*Source: `Mirny_Subnet/Mirny/04_Phase_05_Relation_and_Geometry.md` (questions Q-44…Q-55). None of these blocks any phase; each names the default the run uses meanwhile.*

- **FQ-26 · Idelsk-Uralia's role (Q-44).** Is Idelsk-Uralia only Mirny's sponsoring founding nation, or also one of its exile groups — and what, in-world, did its founding consist of (conveyance, materials, administration, people)? **Default:** sponsoring founding nation only (`DR-46`'s own reading), role unstated; "founding without residence" written as conditional.
- **FQ-27 · Did the founder choose the site? (Q-45).** **Moves** Phase 2's P2-1, *"Nobody chose Mirny."* **Default:** no resident chose it; whether the founding nation chose the site is not stated.
- **FQ-28 · Which names the "stock"? (Q-46).** `No_National_Stereotypes`' form (*"Stock: Japanese. People: Tepenian."*) assumes the founding nation and the stock coincide; at Mirny they may not. **Options:** (a) the three exile groups · (b) Idelsk-Uralia · (c) both, in different senses. **Default:** the three exile groups as the stock; the Frame's A.5 wording not edited.
- **FQ-29 · Relay failure (Q-47).** Who restores Mirny's relay (a Mirny body, a subnet body or a national one), and is there any fallback channel? Does Shape D's Belgrano–Casey radio chain serve Mirny and persist beside the Arcanet relay? **Default:** restoration by whoever is at the hardware; no second path; Shape D not equated with the relay.
- **FQ-30 · Routing vs access (Q-48).** `Arcanet.md` says Kunlun and Ariun Nuur have *"basically no Arcanet access"*; the spec routes them through Mirny's relay. Routing versus residents' access, or a contradiction? **Default:** both recorded, neither adjudicated.
- **FQ-31 · The inland spur (Q-49).** Does Mirny have an inland spur road (spec L140), or is the phrase residue from before the 2026-07-06 correction (`Highways.md` L204)? **Default:** recorded as a strain; no place is named after it.
- **FQ-32 · `RV-1` and the subnet's name (Q-50).** The subnet's official name is the hub city's name (`City_Relationship_Database.md` L42/L511), so Mirny's reserved official name also names the whole subnet. Decide `RV-1` with that in view? **Default:** no name proposed.
- **FQ-33 · Mirny's harbor (Q-51).** Does any rock shelter a berth (GEOLOGICAL, seasonal), or is it a seasonal offload (CONSTRUCTED)? Is Mirny the subnet's port of record for Australian freight (`CRD` L330 says "likely"), and does it receive people from Hobart? **Default:** tier not established; the CONSTRUCTED-seasonal lean recorded as a derivation.
- **FQ-34 · `CRD` L55 (Q-52).** Does the line saying Mirny's residents *"may find"* the "Australian" nickname inaccurate still stand after `DR-46` and `DR-47`? Its premise looks like the real station's nationality (GPS). **Default:** not an input; a null.
- **FQ-35 · 5b's own-eras set (Q-53).** Confirm the deferral with histories (`DR-16`, as the Frame applied it), or ask for an in-frame-only set. **Default:** deferred; three attempts recorded, not adopted.
- **FQ-36 · The radio-standard view (Q-54).** Your 2026-10-04 view (East Antarctica's comms posts largely staffed by Australian-stock people; their practice the standard) was **not used as an input**; the Timeline says the question *"rests on the in-world founders"*. Should it bind Mirny's relay? **Default:** written open.
- **FQ-37 · Docket (Q-55; needs your OK, never applied).** (a) Re-map the contract's §B row for spec L184 (the 2026-10-03 Ariun Nuur rename moved it +4 characters; found by all three readers). (b) Amend the Frame's D-1 "as of when" to: undated; after the subnet's connection; no later than ~2688 (its ~2614 start rests on a withheld source and a superseded B-Story reading).

---

## ⭐ City renaming — done, with follow-ups *(FQ-18, 2026-10-03)*

**Done:** all four names ruled (`DR-36` Santa Luce · `DR-37` Temirötkel · `DR-38` Utstein / Utsteinen · `DR-39` Relung Panen) and swept through the live canon in one sweep, as you ordered. Full report, name map, path map and the list of what was left untouched: `Cities/City_Renames_Alias_Table_2026-10-03.md`.
**Needs you:**
1. **Demonyms.** "Sayowan", "Abowasian" and "Princess Elisabethan" are unchanged; no new demonyms are ruled.
2. **Utstein vs Utsteinen** in-game: which contexts use which (the sweep used Utstein everywhere).
3. ✅ **The 6 held files: ruled 2026-10-03 — sweep them after the Mirny pass finishes.** Census and Division-of-Industry 09/10/11/13/16 still carry the old names until then. The tool is `Universal_Location_Methodology/Tools/rename_sweep_held_files.py`; the reminder is in the tracker's `📍 RESUME HERE` block.
4. **Sayowa's first establisher:** the CIN or Kazakhstan.
5. **Santa Luce's pronunciation:** keep Italian "LOO-cheh" vs Polish "LOO-tseh" as texture, or drop it.
6. **Relung Panen's Malay form:** the Malay-natural "Relung Tuaian" is unverified.

---

## ⭐ Founding Register work — time-zone audit and proposals, 2026-10-03 *(developer-requested; hours waived for this task)*

*Source: `Cities/Founding_Register_TimeZone_Audit_and_Proposals_2026-10-03.md`. The Register itself is unchanged; nothing below is canon until you rule.*

- ~~**FQ-13a · Mawson**~~ **RULED 2026-10-03 (`DR-33`): co-founded by Australia and Kazakhstan.** Signy's South African role was confirmed the same day. Closed.
- ~~**FQ-13b · Rothera and Argentina**~~ **RULED 2026-10-03 (`DR-44`):** Argentina stays a founder of Rothera (inferred from "all the ruled founders listings are right"). Closed.
- ~~**FQ-13c · Shirayuki and Sinheung Basis**~~ **RULED 2026-10-03 (`DR-44`):** the Jeju-do allocation stays; geography (gap 3) is an ADDITIONAL factor. Closed.
- ~~**FQ-14**~~ **ALL RULED (`DR-34`, `DR-35`, `DR-44`, 2026-10-03):** every row of the register is now ✅.
- ~~**FQ-16**~~ **RULED 2026-10-03 (`DR-35`):** Vostok = Künnarantaiga and Mongolia; Sejong = Chile first, then English-speaking arrivals, then Palmer City, then Korea (translators); Neumayer = the Netherlands and Austro-Bavaria. Kunlun's stock follows Vostok. Closed.
- **FQ-17 · The remaining options** (Signy co-founder, Denison, Dumont d'Urville, Zukelli, Cape Adare, Byrd): the proposals file now lists post-war option sets for each. Tell me which to narrow, or give a direction as you did for Sejong. **Default:** Register untouched.
- **Also noted:** `DR-9` names *Russia* for Mirny in pre-war terms; the CST recast will need a successor state (Siberia, Tuva or Künnarantaiga; Mirny is +6). Nothing changed now.
- **FQ-15 · Gateway research:** **RUN TWICE 2026-10-03: first pass (zero searches) and a RERUN with working search (~250 searches).** Logs: `Research_Logs/Founding_Gateway_Research_{A,B,C}_…` and `{A2,B2,C2}_…RERUN_…`. Primary ports ruled (`DR-48`). Ports files corrected; Round 2 wording options appended (none chosen). Bunger Hills corrected to the Knox Coast. **Open:** choose the Basis wordings (`Founding_Basis_Wording_Options_2026-10-03.md`); update `Ports.md` with Ushuaia and Hobart (needs go-ahead); post-war nation of Ushuaia; the RERUN logs' remaining gaps.
- **FQ-20 · Australia's share of the founders** (developer's thought, `DR-44`): six cities had Australian founders. Mawson's removed (`DR-45`); **five remain** (Mirny as an exile group, Casey, Davis, Denison, Zukelli). Any further change is optional. **Default:** no further change. **⚠ UPDATE 2026-10-04 (`DR-53`): Australia was RESTORED as a Mawson founder, so the count is back to SIX** (Mawson, Mirny as an exile group, Casey, Davis, Denison, Zukelli). Still optional; default unchanged. *Note for any future re-founding: the comms-posts idea (handoff §9) leans on Casey's 10 posts, so re-founding Casey would undercut it; Davis, Denison and Zukelli would not.*
- ~~**FQ-21 · Mawson's co-founder**~~ **RULED 2026-10-03 (`DR-46`): Russia (core state).** Closed.
- **FQ-22 · Mirny's live pass and `DR-46`.** The pass (Phases 2–4 done) was written on `DR-9` (exile groups Russia, China, Australia). `DR-46` adds Idelsk-Uralia as the founding nation and keeps those three as exile groups. Read the pass's founders usage and `Mirny.md`'s *"Primarily Russian exiles"* line in-window before a step that uses them; nothing in the pass was edited. ✅ **Founders read in-window at Phase 5 (2026-10-05):** the founders table and P5-10 of `04_Phase_05_Relation_and_Geometry.md` (the spec's founders line, L152, now cites the Register and is not used — FQ-9). **Open: FQ-26, FQ-27, FQ-28.**
- ~~**FQ-23 · The three Australian freighter terminals vs Hobart**~~ **RULED 2026-10-03 (`DR-49`):** the three carry the bulk freight; Hobart is the primary gateway. **Open:** Hobart's island-specific applications (research running); Fremantle next to Bunbury; iron-ore origin; site feasibility; east-coast sites.
- **FQ-24 · ⏸️ Three international airports (DEFERRED, `DR-51`).** The developer: Tepenia needs three, not one; early on only Marambio Airport exists; later non-Western-Hemisphere immigration needs the others. **Open:** which three; where; when; reconcile `Airports.md` (Marambio domestic, Machu Picchu the only international). **Wait for the country and the worldbuilding to be better-determined; do not close early.** Related: `Ports.md` §3d (Hobart and Ushuaia as people ports of transfer).
- **FQ-25 · 💡 THE TOWNS IDEA** (`DR-52`, 2026-10-03). Real Antarctic stations on stable ground that are not already cities become Tepenian **towns** (fuller country; DLC places between cities; *Southern Lights*; a natural path from the coast to Ariun Nuur, Kunlun and Dome Fuji). **Idea recorded only; nothing started.** **Open:** (1) is *"what each station is dedicated to can be part of the basis"* a TOWNS-ONLY exception to the station-history law?; (2) hours (05:00 to 14:59 for design); (3) where town populations come from (census hands-off, `DR-23`); (4) criteria for "steady" and which stations (year-round only? closed historical ones?); (5) scale, names, ports/airstrips/highway stops; (6) the Hwy 37 path. ✅ **(1) RESOLVED 2026-10-03:** the "dedication as basis" rule is the inheritance regime (`DR-24` to `DR-26`), not an exception. ✅ **2026-10-03 rulings:** hours = **data any time, town character only 05:00 to 14:59**; census **deferred**; "steady" = **ice not moving fast enough to force relocation, ideally bedrock some distance below**; scope = **collect every usable station location, decide the rest as we go**. **Data pass started; files in `Locations/Towns/`.**

---

## ⭐ Scheduled, "preferably sooner rather than later" — the founding nations reference sheet *(developer sidenote, 2026-10-03)*

*Not blocking Mirny. Logged so it is not lost.*

### FQ-5 · Finish the founding-nations reference sheet — which sheet, and in what order?
- **What I took you to mean.** `Cities/Founding_Register.md`, the single home for every city's founders (created 2026-10-01). Today it holds **40 rows**:
  **12 ruled** · **2 ruled in part** (Signy, Halley) · **6 canon but not re-ruled since `DR-19`** (Palmer City, Shirayuki, Sinheung, Cape Adare, Concordia, Amundsen Station) ·
  **9 open** (Port Lockroy, Neumayer, Lazar, Vostok, Kunlun, {{Bunger Hills City}}, Scott, Denison, Byrd) · **9 overturned and awaiting a ruling** (Rothera, Juan Carlos,
  Sejong, {{ Abowasa }}, {{ Princess Elisabeth }}, Dome Fuji, Zukelli, Fort McMurdo, Dumont d'Urville). Only you can mark a row ruled.
- **Why it speeds everything up.** Every city pass, spec, culture sheet and datasheet points to this file for founders; each open row is a place where a pass has to stop and say
  "founders unknown" (Mirny's own Phase 2 did this for the eleven non-founding stocks). The related sheet `Post-War_Nations_Founder_Reference.md` (time-zone spans, a working summary) is the
  tool for the geography half.
- **What I could do, if you say go.** Work through the 18 open + overturned rows with you, one subnet at a time: for each row I put the city's own geography and access
  (solar time zone, reachable nations from the post-war map summary) in front of you, propose candidates marked "proposed," and you rule. I never mark a row ruled myself, and no
  row is justified by comparison to another city.
- **Questions for you:** (a) Is the Register the sheet you meant, or did you mean a different or additional one (for example a one-page city → founding nations lookup)? (b) Should this
  run **between** Mirny pieces (it only needs your rulings, not a synthesis window) or after the Mirny subnet closes? (c) Any preferred order: the rows that block the most
  passes first, or subnet by subnet?
- **Default if you do not answer:** Mirny continues; I do nothing to the Register.

---

## Mirny · Step 4 · Phase 4 (Ordinary Life), written 2026-10-03

*Source: `Mirny_Subnet/Mirny/04_Phase_04_Ordinary_Life.md`. None of these blocks any phase.*

### FQ-10 · What keeps the shared night where there is no night? *(Phase 4 Q-41; R-39)*
- **The text.** Robot canon says *"Robots and humans stop at the same time, for different reasons."* (`Robot_Physiology_and_Cultural_Practices.md` L336): the robot recharges overnight, the human rests. Mirny has **no night at all for about 29 days** (midnight sun, Dec 8 → Jan 5) and no darkness beyond twilight for about 80; even in the rest of the year the sunset wanders by at least 9 h 27 min of solar time on monthly means (derived under a stated assumption).
- **What the run does now.** Treats the stop as kept by *whatever keeps time*, claims no hour, no device and no light-dependence (neither body's reason depends on the sun), and writes the day to stand under either answer.
- **What your answer changes.** Phase 4's first finding (P4-1), what a visitor reads in Phase 5, how the observances Phase 6 writes are timed, and how the continuous services are staffed in Phase 7.
- **Options:** (a) the stop is a convention kept by the city (a clock, a rhythm of work, a signal) · (b) it is each body's own cycle and happens to coincide · (c) it is a rule the two bodies keep by custom, not by the sky · (d) leave it open until the post-ULM vision pass.

### FQ-11 · Does Mirny have any public wind call? *(Phase 4 Q-42; R-38)*
- **The text.** The spine says *"since the sky can't be trusted, the signal decides when people move."* No admitted file contains a published wind or visibility report, a flag, an alarm or a scale; the research found no early warning with a demonstrated lead time; the relay is *noisiest exactly when the city most needs it*.
- **What the run does now.** Writes the decision at the door as a fork: with no public call every outing is a private judgment against an unread cue and a failure is read as the decider's act; with one, it is a published judgment (a Phase 6/7 fact). Neither is adopted.
- **What your answer changes.** The shape of the ordinary day, the blame pattern, what a visitor can read, and whether Phase 7 has a rule to write.
- **Options:** (a) none exists; residents judge for themselves · (b) a published call exists (say what: a flag, a number, a siren, a relayed report) · (c) the harbor watch makes calls and the city does not use them · (d) leave open.

### FQ-12 · Is the freedom margin a share of people or of a life? And the parked 11.8 % *(Phase 4 Q-43; R-24)*
- **The conflict.** Mirny's own Division of Industry row reads baseline 41.1 %, mandated 11.8 %, free 47.1 % (they sum to 100.0, so they are shares of one base: workforce units, where a robot counts 1 and a human 0.5). `09` §3.5 reads the free share as the share of people able to work in jobs they want to; Robot Physiology reads the same margin as *half to three-quarters of a Tepenian working life*. The datasheet's header calls the percentages "of the DISTINCTIVE tier", which contradicts the row's own sum. Your earlier parked question (is the 11.8 % really 11.8 % or 23.6 % of something?) is the same family.
- **What the run does now.** States the numbers as the row prints them, calls 47.1 % an upper bound (the robot-keyed industries are excluded from the margin), does not write the free tier as "what residents do instead of the headline function" (it can contain the quarry and the hub), and rests nothing on the base.
- **What your answer changes.** What 47.1 % means for ordinary leisure and chosen work (Phases 4, 6, 7).
- **Options:** (a) people able to do work they want · (b) a share of a working life · (c) both, at different levels · (d) keep parked.
- **Also needs your OK (docket):** a one-line fix to `Datasheets/Phase_4.md`'s header wording and its cold-file label ("the governing mechanic", the `M-151` trap); and softening in Phase 3 (already done in the phase file).

---

## Mirny · Step 4 · Phase 3 (Surface & Texture), written 2026-10-03

*Source: `Mirny_Subnet/Mirny/04_Phase_03_Surface_and_Texture.md`. None of these blocks any phase; each moves a conditional claim.*

### FQ-6 · What is the ring? *(Phase 3 Q-38; R-26)*
- **The text.** The only admitted words are *"the sheltered industrial core inside the city's outer wind-fortified ring"* (spec L174). The architecture and airlock detail (spec L162) is excluded by the
  contract; the building-layout paragraph (L168) is developer-vision material (`DR-10`); concept art is empty; the megasheet's physical-infrastructure file is withheld. So nothing says what the ring is.
- **What the run does now.** Treats it as a wind-fortified perimeter of unknown form: not assumed closed, solid or roofed. Everything that follows from a solid ring (drift belts on both faces, keepers who clear
  it, scoured entries, wear by arc) is written as conditional.
- **What your answer changes.** The seam (§D), the entry texture, the first-impression claims, Phase 10's naming referents, and whether the "enclosed" idea (one reader's wording) has any basis.
- **Options:** (a) a solid wall · (b) a porous fence that passes snow · (c) an earthwork that sheds snow · (d) closed all round, or open on the lee side · (e) roofed or enclosed in part · (f) leave it open until the post-ULM vision pass.

### FQ-7 · Does rock or "coastal ice" carry the built area? *(Phase 3 Q-39; R-25)*
- **The conflict.** The spec's admitted words are *"The coast here is rocky and exposed."* The Frame records "coastal ice" from the extent file (a corroboration-tier report) and says both are buildable;
  no admitted file chooses which carries the 135–193 km².
- **What the run does now.** Carries both branches and adopts neither.
- **What your answer changes.** Underfoot texture, how drift behaves, and any claim about the ground for most of the city (Phases 3, 4, 5).
- **Options:** (a) rock · (b) ice · (c) both, with a stated split (a number only you or the extent file can supply).

### FQ-8 · Which sea-ice calendar governs? *(Phase 3 Q-40; R-30)*
- **The conflict.** The spec's table notes put sea ice *beginning to form* in March and *breaking up* in October. The Step 3 research has fast ice from about April to February (break-up between Dec 17 and Mar 9,
  refreeze between Mar 18 and May 5; about ten months a surface). The research flagged the difference as material and changed nothing.
- **What the run does now.** States both and adjudicates neither; every finding is written to hold under either.
- **What your answer changes.** The length of the sea-as-road season, the harbor window, and what the winter commute is (Phases 4, 5, 7).
- **Options:** (a) the spec table governs (a shorter ice season; the research is a regional figure) · (b) the research governs (the spec's notes are onset markers, not season limits) · (c) decide later.

### FQ-9 · May the contract's map of the Mirny spec be re-derived? *(docket; found in Phase 3 Round 3)*
- **The issue.** The spec was edited on 2026-10-01 (the heritage cleanup). Five lines (L21, L150, L152, L154, L229) are now shorter than the contract's character-level admissibility spans assume, so those
  spans no longer align. Phase 3 used only text that is safe under both numberings (one L150 phrase and one L150 sentence) and nothing else on those lines. `00_Frame` A.1's quotation of L150 is also not
  verbatim (it omits one word), and the contract's `[VISION-DATED]` label is not in the spec text it annotates.
- **Needs your OK:** re-deriving the contract's §B rows for those five lines, and a one-word fix to the Frame's quotation (each is a change to an existing file). Until then, later phases must re-measure before
  using any text on those lines.

---

## Mirny · Step 4 · Phase 2 (Composition & Arrival), written 2026-10-03

*Source: `Mirny_Subnet/Mirny/04_Phase_02_Composition_and_Arrival.md`. None of these blocks any phase.*

### FQ-1 · Which rule governs human eligibility for exile? *(Phase 2 Q-36; R-19)*
- **The conflict.** The Falkland Treaty draft (`FTD` II.2.3, L48) lets a human accompany the robots on **four tie grounds**: living among
  robot communities, marrying or partnering with a robot, raising children in a robot household, or otherwise establishing a life among
  the robot population. **No means test.** `Robot_Physiology_and_Cultural_Practices.md` L87–88 quotes the census's source as saying
  eligibility was for *"people who could afford robots, or who loved/supported someone who owned one."* That adds an **ownership / means** ground.
- **What the run does now.** Uses the treaty's four tie grounds (the exact wording) and logs the difference.
- **What your answer changes.** If "afford" governs, the human founders may have been an owner or commissioner stratum, and the human–robot
  bond at the founding may have begun as ownership. That would reshape Phase 9's human populations and the founding households. If the four
  ties govern, `RP` L87–88 is a looser paraphrase and needs a fix.
- **Options:** (a) four ties govern; `RP` L87–88 gets a wording fix · (b) "afford" governs; the treaty needs a fifth ground · (c) both are true
  at different levels (the treaty states the right, the source describes who could actually use it).

### FQ-2 · Do robots keep arriving after 2564? *(Phase 2 Q-37; reserved finding RF-5)*
- **The text.** `FTD` II.2.1 says *"every robot presently residing… and every robot who may hereafter come into being within such territory,
  shall depart."* That implies robots continue to be made on Upper Earth after the treaty and continue to be sent.
- **What the run does now.** Reads it as unproven: nothing else in the admitted files says robots keep being made there after 2564.
- **What your answer changes.** If yes, Mirny's robot half has a continuing stream of **fresh-origin** robots (origin learned abroad, recently),
  so "origin is ancestry, not identity" would not hold uniformly in Act 2 for the robot half. It would also change the robot rows of the
  *Fled* and *Born here* modes. If no, the robot half is founding cohort plus robots built in Tepenia.
- **Options:** (a) yes, a continuing stream · (b) no, the clause covers only robots existing at signing and any created before departure ·
  (c) decide later, with the history pass.

### FQ-3 · Does the census's "founding wave" note constrain the founding order? *(Frame Q-35; Phase 2 R-10)*
- **The conflict.** The census (`CEN` L33) defines "founding wave" as a nation that set the city's early character *prior to the arrival of
  larger national communities*. Only Australia carries it at Mirny. Your ruling (`DR-9`) names three founders (Russia, China, Australia) with no
  order, and China is both a founder and the Primary (largest) tier. Read literally the note implies Australia first and China later.
  The Frame also calls the note "the GPS annotation" in one place (Q-34) and treats it as in-world content in another (R-10, datasheet L9).
- **What the run does now.** Rests nothing on the note; Australia's founder status stands on `DR-9` alone; order stays unknown.
- **What your answer changes.** Founding order and the early Act 1 character of the place (Phase 6, Phase 9); whether the note is in-world
  content, an authoring note to be removed, or a clue to be honored.
- **Options:** (a) it is an authoring note about long-run share; no order is implied · (b) it is in-world: Australia came first, then the
  others · (c) remove it from the census (a census edit; waits until all 38 cities finish, `DR-23`).

### FQ-4 · May the pass files stop saying "unratified"? *(wording docket)*
- **The issue.** Mirny's Frame (L457, PA-1) and other pass files call the treaty clauses "unratified." The treaty's own Art. VIII.1 says it
  enters into force **on signature, without ratification**, and its status line says *"Not locked canon."* Those are two different things; the
  accurate label is **"draft, not locked."**
- **What the run does now.** Uses "draft, not locked" in new files; leaves the old wording alone.
- **Needs your OK:** a one-line wording correction in the existing Mirny files (each is a change to an existing file).

---

## Standing Mirny questions still open from the Frame *(unchanged; listed so they live in one place)*

| Q | Question | Current default | Source |
|---|---|---|---|
| Q-23 | The Federation's band: Band 6 per the runbook, or Band 5 per its own census total (~32M)? | Band 5 | `00_Frame.md` |
| Q-24 | Language: is there an in-frame national language (perhaps only in Act 2), or is language local to each city? | No language named; later phases write it as REQUESTED | `00_Frame.md` |
| Q-25 | Does `DR-4` also suspend the Uniform / Patterned / Delegated tags? | Yes: no tag; every answer says "base-level (DR-4), not a Uniform claim" | `00_Frame.md` |
| Q-26 | Extent band for a continental city with no measured footprint | 5, matching the population band by construction | `00_Frame.md` |
| Q-33 | Where should the provisional assumptions (PA-1…PA-14) be registered so the Mirny subnet's eventual pass sees them? | Kept in the phase files | `00_Frame.md` |
| Q-34 | May the listed existing files be corrected (each one is a change, so each needs your OK)? | Nothing edited | `00_Frame.md` |

*Also parked, not blocking:* the **11.8 % vs 23.6 %** workforce-mandate question (**answered in Phase 7, P7-2: §20's 23.6 % governs; docket FQ-46**); the **17 open questions** in
`Cities/ULM_Files_Mistake_Audit.md` Part E.
