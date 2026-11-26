# LAW 0-P coverage tracker: has every inspiration pick been researched and used, city by city?

**Started 2026-11-19, at the developer's request.** It tracks one thing: whether each city's **whole** inspiration-picks list has been
researched and incorporated, as LAW 0-P now requires (project `CLAUDE.md`; `00_RUNBOOK.md`, its own section above the end pointer; `DR-144`
once filed). **The whole list** means the official picks (`Worldspace/.../Cities/Inspirational-Influences.md`) **plus every row of the city's
candidate list** (`candidates/<City>.md` in this folder), developer additions included, whatever its tier. The tiers decide only how
prominently a pick figures in the place, never how thoroughly it is researched (`DR-145`, 2026-11-20).

**Why it exists:** the Mirny subnet's passes were researched on the official picks only, so the developer has ruled that the Mirny subnet is
to be re-run (2026-11-19: *"next week, we have to go back and do the Mirny subnet all over again (a 3rd time)"*). This file is where that
re-run, and every later city, shows its coverage.

## How to read and update it

- **Official picks (R1 · R2):** the two inspiration-place research rounds on the official picks, from `_TRACKER.md` (2026-11-19 state).
  ✅ done · ◐ partial · ☐ not started.
- **Candidate rows:** the size of the city's candidate list, from `candidates/_DRAFTING_TRACKER.md`.
- **Candidate rows researched:** how many of those rows have had real web research with sources (not a reading check). Write it as
  *researched / total*, with the date and the file that holds the research.
- **Used in ULM · CST · RWBEM:** whether that pass's research steps read the **whole** list (official and candidates). **"Yes" needs a
  reading list that carried the whole list**: say which brief. Left blank where not yet checked; it is filled from each city's own pass
  records when that city is worked, never by comparing cities.
- **LAW 0-P met:** ✅ only when every row is researched AND each pass that reads picks used the whole list.
- Update a row in the same change that finishes the work it records. Never mark ✅ from memory: cite the file.

## Coverage, by city

| City | Subnet | Official picks | R1 · R2 | Candidate rows | Candidate rows researched | Used in ULM | Used in CST | Used in RWBEM | LAW 0-P met | Notes |
|---|---|--:|---|--:|---|---|---|---|---|---|
| Casey | Mirny | 3 | ✅ · ✅ | 124 (#1–#124; rows #85–#124 added in the 2026-10-27 top-up; the drafting tracker's 84 predates it). **Corrected 2026-11-20:** the subnet-wide road-music row **is** in this file, as **#25**; it waits for its own study after all the culture work (developer, 2026-11-20) | **105 / 124, two rounds each** (2026-11-21 ~12:45, end of day 4): the 3 official picks (unit `Casey`) + 102 candidate rows in units `Casey_C01`–`C17` (`Research_Logs/Casey_C<nn>_Inspiration_Place_Research_R1/R2.md`, all progress boxes checked). `C18` and `C19` have Round 1 only. 18 rows to go (`C18` and `C19` Round 2, `C20`); #25 waits. Paused since 2026-11-21; resumes after the Kunlun ULM run (from 2026-11-29), and the other Mirny cities' whole-list research follows Casey (developer, 2026-11-25). Then a gap-fill pass on C01, C12, C05 and C04 (whether C17 joins it is the developer's open question). Run log: `Casey_Pick_Research_LOG.md` | | | | ☐ | **Mirny subnet re-run** |
| Mirny | Mirny | 4 | ✅ · ✅ | 86 | 4 / 86 (the official picks only) | | | | ☐ | **Mirny subnet re-run** |
| Davis | Mirny | 3 | ✅ · ✅ | 89 | 3 / 89 (the official picks only) | | | | ☐ | **Mirny subnet re-run** |
| Ariun Nuur | Mirny | 3 | ✅ · ✅ | 86 | **85 / 86 researched** (rows 1–85, three readers each, 788 web calls; 2026-11-20, ULM Phase 10R2: `Research_Logs/Ariun_Nuur_Research_Log.md` Entries 4–6); row 86 waits by the developer's ruling (its own study after the CST); 85 / 85 also reading-checked, no web (2026-11-19, Phase 10C) | **Phase 10 (process B): yes** — the briefs `.t8_brief_04_Phase10R2u{1,2,3}.md` carried the whole candidate list, and `04_Phase_10_Catalog.md`'s pick-incorporation sections give every row a disposition (2026-11-20). **Step 3: no** (briefed on the official picks only, 2026-11-19) | | | ☐ | Official picks researched again in depth 2026-11-19 (ULM Phase 10R, 326 web calls; Entry 3). LAW 0-P not yet met: the CST and RWBEM are still to come. **Mirny subnet re-run** |
| Kunlun | Mirny | 4 | ✅ · ✅ | 98 | 4 / 98 (the official picks only). **The other 93 are researched inside Kunlun's ULM run, at full depth (two rounds, own units `Kunlun_K01` onward), from 2026-11-29** (developer, 2026-11-25; `Universal_Location_Methodology/HANDOFF_Kunlun_ULM_2026-11-29.md` §2.1) | | | | ☐ | **Mirny subnet re-run** |
| Zhongshan | Mirny | 3 | ✅ · ✅ | 79 | 3 / 79 (the official picks only) | | | | ☐ | **Mirny subnet re-run** |
| Sinheung | Mirny | 3 | ✅ · ✅ | 82 | 3 / 82 (the official picks only) | | | | ☐ | **Mirny subnet re-run** |
| Shirayuki | Mirny | 4 | ✅ · ◐ | 86 | 4 / 86 (the official picks only; Round 2 partial) | | | | ☐ | **Mirny subnet re-run** |
| Relung Panen | Mirny | 6 | ✅ · ✅ | 97 (#1–#97; the drafting tracker's 96 predates the developer-added #97) | ✅ **97 / 97, two rounds each** (verified 2026-11-19): #1–#26 in `Research_Logs/Relung_Panen_Inspiration_Research_2026-10-26_{A,B,C,D}…` and their Round 2 files (6 + 6 + 8 + 6 = 26 places, no unchecked progress box); #27–#97 in `Relung_Panen_B01`–`B12` R1 and R2 (all progress boxes checked) | | | | research ✅; use in passes to check | **Research should not need redoing.** What remains is only whether its ULM (run to Phase 10), CST and RWBEM briefs used the whole list. **Mirny subnet re-run** |
| Concordia | Janbogo | 4 | ◐ · ☐ | 89 (city level; district lists deferred) | 0 / 89 | | | | ☐ | District lists not drafted |
| Dumont d'Urville | Janbogo | 3 | ◐ · ☐ | 91 | 0 / 91 | | | | ☐ | |
| Denison | Janbogo | 4 | ◐ · ☐ | 93 | 0 / 93 | | | | ☐ | |
| Cape Adare | Janbogo | 3 | ☐ · ☐ | 76 | 0 / 76 | | | | ☐ | |
| Janbogo | Janbogo | 5 | ☐ · ☐ | 85 | 0 / 85 | | | | ☐ | |
| Zukelli | Janbogo | 3 | ☐ · ☐ | 84 | 0 / 84 | | | | ☐ | |
| Fort McMurdo | Janbogo | 3 | ☐ · ☐ | 109 | 0 / 109 | | | | ☐ | |
| Scott | Janbogo | 3 | ☐ · ☐ | 86 | 0 / 86 | | | | ☐ | |
| Mawson | Mawson | 4 | ☐ · ☐ | 86 | 0 / 86 | | | | ☐ | |
| Temirötkel | Mawson | 5 | ☐ · ☐ | 93 | 0 / 93 | | | | ☐ | |
| Dome Fuji | Mawson | 3 | ☐ · ☐ | 83 | 0 / 83 | | | | ☐ | |
| Belgrano | Halley | 6 | ☐ · ☐ | 95 | 0 / 95 | | | | ☐ | |
| Halley | Halley | 7 | ☐ · ☐ | 87 | 0 / 87 | | | | ☐ | |
| Santa Luce | Halley | 4 | covered inside C02 (its candidates #8–#13 include the four official picks) | 75 | **13 / 75, two rounds each** (verified 2026-11-19): `Research_Logs/Santa_Luce_C01` (#1–#7) and `C02` (#8–#13) R1 and R2, all progress boxes checked; #14–#75 not researched | | | | ☐ | 62 rows still to research |
| Neumayer | Halley | 7 | ☐ · ☐ | 103 | 0 / 103 | | | | ☐ | |
| Sanay | Halley | 4 | ☐ · ☐ | 87 | 0 / 87 | | | | ☐ | |
| Troll | Halley | 5 | ☐ · ☐ | 77 | 0 / 77 | | | | ☐ | |
| Lazar | Halley | 6 | ☐ · ☐ | 84 | 0 / 84 | | | | ☐ | |
| Utstein | Halley | 5 | ☐ · ☐ | 78 | 0 / 78 | | | | ☐ | |
| Signy | Palmer | 6 | ☐ · ☐ | 85 | 0 / 85 | | | | ☐ | Two units in `_TRACKER.md` |
| Contrapunto | Palmer | 4 | ☐ · ☐ | 82 | 0 / 82 | | | | ☐ | |
| Esperanza | Palmer | 7 | ☐ · ☐ | 93 | 0 / 93 | | | | ☐ | |
| Marambio | Palmer | 2 | ☐ · ☐ | 70 | 0 / 70 | | | | ☐ | |
| Pergamino | Palmer | 3 | ☐ · ☐ | 76 | 0 / 76 | | | | ☐ | |
| Palmer City | Palmer | 5 | ☐ · ☐ | 89 | 0 / 89 | | | | ☐ | |
| Puerto Abrigo | Palmer | 5 | ☐ · ☐ | 66 | 0 / 66 | | | | ☐ | |
| Rothera | Palmer | 5 | ☐ · ☐ | 87 | 0 / 87 | | | | ☐ | |
| Byrd | Byrd | 5 | ☐ · ☐ | 79 | 0 / 79 | | | | ☐ | Two units in `_TRACKER.md` |
| Amundsen Station | South Pole (special case) | 7 | ☐ · ☐ | 104 | 0 / 104 | | | | ☐ | Reference-only row in `_TRACKER.md` |

**Verified 2026-11-19 (the developer asked which cities already have their whole list researched):** of every inspiration-research file
in `Worldspace/.../Cities/Research_Logs/` (`*_Inspiration_Place_Research_R1/R2.md` and Relung Panen's 2026-10-26 group files), **only
Relung Panen has its whole candidate list researched** (97 of 97, two rounds), and **Santa Luce has 13 of 75**. Every other city has only its
official picks researched (or not yet): Casey, Mirny, Davis, Ariun Nuur, Kunlun, Zhongshan and Sinheung have both rounds; Shirayuki has
Round 1 and part of Round 2; Concordia, Denison and Dumont d'Urville have Round 1 only; the rest have neither. Checked by file name, file
header and progress boxes only (no content read); the folder `outputs/` holds one draft file and no research.

**Sources for this table (read 2026-11-19):** `_TRACKER.md` (the unit rows: city, subnet, pick count, Round 1, Round 2) and
`candidates/_DRAFTING_TRACKER.md` (candidate counts). The *researched* column starts at 0 for every city except where `_TRACKER.md`
itself records candidate-group units (Relung Panen, Santa Luce); those two are marked partial and are to be verified at source.
The *used in* columns are blank on purpose: they are filled city by city, from that city's own pass records.

## Mirny subnet: researched against on file (counted 2026-11-19)

*On file* = the rows of the city's candidate list, which already include its official picks (marked EXISTING) and, where present, the
subnet-wide developer row (solo road-travel music). *Researched* = rows with inspiration-place research rounds on file.

> ⏭️ **Solo road-travel music is its own topic of study, AFTER the CST** (developer, 2026-11-19: *"eventually, the road-travel music will be
> its own topic-of-study, so we can do that after the CST is complete (since it's dependent upon people's cultures)"*). It is **not**
> researched in any city's catch-up; its row stays on each list and is marked as waiting for that topic. (Relung Panen's #97 was already
> researched before this ruling; that research stands.)

| City | On file | Researched | Still to research now (the road-music row excluded) |
|---|--:|--:|--:|
| Casey | 124 | 105 (2026-11-21, end of day 4; see the coverage row) | 18 (#25, the road-music row, excluded; the earlier "121 / no road-music row" was wrong) |
| Mirny | 86 | 4 | 81 |
| Davis | 89 | 3 | 85 |
| Ariun Nuur | 86 | 85 (rows 1–85; rows 1–3 are the official picks) | 0 (row 86 waits; researched 2026-11-20, ULM Phase 10R2) |
| Kunlun | 98 | 4 | 93 |
| Zhongshan | 79 | 3 | 75 |
| Sinheung | 82 | 3 | 78 |
| Shirayuki | 86 | 4 (Round 2 partial) | 81 |
| Relung Panen | 97 | 97 | 0 |
| **Total** | **827** | **226** | **593** (2026-11-21, end of day 4: Casey 102 candidate rows researched, #25 excluded) |

> ⏭️ **Timing (developer, 2026-11-19): only Ariun Nuur is being worked now** (its ULM run continues 2026-11-20). **The other eight Mirny
> cities are tasks for a couple of weeks from now;** do not start them before the developer brings them up.

## Scope of the catch-up (developer, 2026-11-19)

> *"Just the ones in the Mirny subnet. We haven't done any ULM runs on any of the other cities, so there's no 'catching up' that needs to
> be done with them. Just, make sure you research all of them."*

- **Catch-up = the Mirny subnet only** (its nine cities). Relung Panen's research is already complete (97 / 97); the other eight need
  their whole candidate lists researched, and their passes re-run as the developer schedules.
- **Every other city: no catch-up.** No ULM run has been done on them. When each city's turn comes, its whole list (official picks and
  every candidate row) is researched as part of the normal work, under LAW 0-P, before its passes read the picks.

## The Mirny subnet re-run (developer, 2026-11-19)

The nine Mirny-subnet rows above carry **Mirny subnet re-run**. **Scope and schedule are the developer's**: which passes are re-run (ULM,
CST, RWBEM), whether in full or from the research steps on, and in what order. Record the developer's answer here when given, then work
the rows down: research every candidate row, re-run each pass's research steps with the whole list on its reading list, and mark the row.

## Budget note

A candidate list runs to about 66–109 rows. At the depth LAW 0-R asks, that is more web calls than one research unit's readers can spend
inside a 1,000-call session that also runs a pass. Plan each city's candidate research as its own unit (or units), in a session with a
fresh web budget, and record the calls spent here.
