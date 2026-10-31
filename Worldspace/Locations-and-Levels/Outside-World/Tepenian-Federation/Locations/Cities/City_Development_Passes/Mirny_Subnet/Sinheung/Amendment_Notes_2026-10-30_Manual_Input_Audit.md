# Sinheung — amendment notes, 2026-10-30 (manual input audit)

**What this file is.** Sinheung's pass was run and closed on 2026-09-07 (the folder's later changes: the audit fixes of 2026-10-01 and, on 2026-10-21, the READMEs). **No pass file is edited by this note, and none was.** The entry below says what has changed in one of Sinheung's sources since the pass, where the pass rests on the earlier state, and the live text as it stands on 2026-10-30. **Everything quoted from a pass file is as recorded at the pass; the source has since changed.** The pass stays the record of what it worked from.

**Limit, stated plainly.** The pass files were not re-read line by line. The places listed below were found by searching the pass files for "Jeju" and for "Founding Register" (each read in context at the lines named), so a founding passage worded differently may exist that this note does not list. Nothing here classifies, rules on or re-derives a finding; it only records the change and points to the live source.

**Developer decisions of 2026-10-30.** The entries below were added after the walk-through (*"all as recommended"*). Entries `SNH-001` to `SNH-009` describe the pass; nothing in the pass was edited. `SNH-S01`, `SNH-S02` and `SNH-S03` were applied to the spec and the census; `SNH-S04` was left in place and is recorded here. Evidence: `Manual_Input_Audit_2026-10-29/Sinheung_Audit.md` and `FIX_LEDGER.md`.

---

## SNH-006 — The Founding Register now states geography as an additional founding factor (`DR-44`); founders come only from the Register (`DR-19`)

**What changed.** On 2026-10-03 the developer ruled the remaining founding rows (`DR-44`, `DEVELOPER_RULINGS_LOG.md` L917). For Shirayuki and Sinheung the developer's words (verbatim, same ruling, L919): *"for Shirayuki and Sinheung … I would change that to geography being an additional factor, on top of the agreement at the Court of Jeju-Do"*. The ruling's table row (L930) reads: "Japan and Korea stay, **by the Jeju-do court's diplomatic allocation, with geography (zone gap 3 to the Prydz Bay coast) as an ADDITIONAL factor** on top of it. Not a rewrite of the basis. Closes `FQ-13c`".

**The live Register row** (`Founding_Register.md` **L62**, re-read 2026-10-30; it was also L62 at audit time). The table's header is `City | Subnet | Solar UTC | Status | Founders | Basis | Source | Not founders` (L36). The row, quoted exactly:

```
| Sinheung | Mirny | +5 | ✅ | Korea, by the Jeju-do court's diplomatic allocation | The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast (the edge of the rule). Developer: geography is an *additional* factor, not a replacement. | `Specs/Mirny subnet/Sinheung.md` L189; `DR-44` | — |
```

The Register's change log (L90) records the same ruling: "Shirayuki and Sinheung (the Jeju-do allocation, plus geography)". **Earlier text of the same row (from git, as recorded when the Register was created on 2026-10-01, commit `ede29386`, L62):** Status 🟡, Basis "Allocation, not geography". The live text above replaced it when `DR-44` (ruled 2026-10-03) was entered; it is in the Register by the commit of 2026-10-04, `582cb682`.

**The standing rule (`DR-19`, 2026-09-30).** The Register's rule 1 (L8–10): "Founders are decided here and nowhere else. No spec, culture sheet, megasheet, catalog, census tag, robot-culture sheet, datasheet or ULM pass may originate or restate a founding claim that this file doesn't hold. They **point to this file**." The Register's rule 2 (L11–13): "A founding nation stands on geography and access, never on the real station (`DEVELOPER_RULINGS_LOG.md` `DR-19`)." The `DR-19` table (`DEVELOPER_RULINGS_LOG.md` L552) puts it as: founding nations are "Legitimate on **geography and access**."

**Where the pass states or cites the founding** (as recorded at the pass; found by searching for "Jeju" and "Founding Register"):
- The two passages the audit named: `04_Phase_09_Populations.md` L317–320 (the quotation of the `§C.9c` ruling; its Sinheung words are on L318: "Sinheung Korea-founded … by the Jeju-do allocation AND THE CENSUS") and `09.6_Input_Audit.md` L150–152 (the same quotation; the ledger's L150 is its first line).
- Passages stating the founding by the allocation: `00_Frame.md` L87, L197, L226; `01_Inherited.md` L27; `02_Spine.md` L57; `04_Phase_02_Composition_and_Arrival.md` L94; `04_Phase_07_Order.md` L236; `04_Phase_10_Catalog.md` L116; `05_Reconciliation.md` L74; and `09.5_Log.md` (entries at L71, L352, L383).
- Passages that cite "the Founding Register" for the founding: `04_Phase_05_Relation_and_Geometry.md` L227 and L278, and `09.5_Log.md` L401. These were added by the audit-fix edit of 2026-10-01 (commit `4a59fab8`, found with `git log -S"Founding Register"`), the day the Register was created, when the row they cite read "Allocation, not geography" (above). The live row is the one quoted above.

**What this note does.** It adds the live Register row and the two rules above beside the pass's founding passages, so that a reader who reaches those passages sees the Register's current basis. It does not say which statements in the pass should change, and it does not rule on any finding.

---

*Filed 2026-10-30 by the manual input audit sweep. Record of the sweep: `Manual_Input_Audit_2026-10-29/Sweep_Reports/Finished_Cities_Sweep.md`.*


---

## SNH-001 — The census scenario of 2026-10-28 (`DR-68`) rescaled Sinheung's population; the pass records the earlier set

**Where the pass stands.** The pass was run and closed on 2026-09-07 on the figures then in the census. They are kept below as "as recorded at the pass (2026-09-07)"; the live rows are `Official_Population_Census.md` L497 (Census I) and L614 (Census II).

| | As recorded at the pass | Live since `DR-68` | Files in the pass that carry the old value |
|---|---|---|---|
| Census I humans | 467,272 | **479,411** | 6 |
| Census I robots | 495,143 | **506,921** | 7 |
| Census I combined | 962,415 | **986,332** | 7 (10 occurrences) |
| Census II combined | 799,463 | **815,309** (humans 402,176; robots 413,133) | 2 (`00_Frame`, `05_Reconciliation`; 4 occurrences) |

Both live rows carry the earlier −10% ruling of 2026-09-05. The counts are from a search of the pass files for the old numbers and may miss a differently worded one.

## SNH-002 — Retention figures derived from the old set (recomputed by hand from the live rows)

| | As recorded at the pass | Live (by hand, 2026-10-30) | Where |
|---|---|---|---|
| Combined (815,309 ÷ 986,332) | 83.07% | **82.66%** | `02_Spine` L108, `09.5_Log` |
| Humans (402,176 ÷ 479,411) | 84.33% | **83.89%** | `02_Spine`, `04_Phase_09` (2), `07_QA_Gates`, `09.5_Log` (2) |
| Robots (413,133 ÷ 506,921) | 81.87% | **81.50%** | `02_Spine`, `04_Phase_09` (3), `07_QA_Gates` (2), `09.5_Log` (2) |
| Spread, humans minus robots | +2.46 pp | **+2.39 pp** | 4 files, 11 occurrences |

The pass's "modest differential" argument stands: the spread is still small and in the same direction.

## SNH-003 — Workforce

The pass computes *495,143 + 233,636 = 728,779* (100% of robots plus half of the humans) in `04_Phase_04` L35, `04_Phase_07` L50, `07_QA_Gates` and `09.5_Log` (3). Live: **746,627** (`09_Per_City_Baseline_Run.md` L80: required 263,357, 35.3%; `16` L257 carries 746,626, a rounding difference: 506,921 + 239,705.5 = 746,626.5).

## SNH-004 — `16` does hold a determination for Sinheung: §17, which supersedes the Half B row

The pass (`04_Phase_04` A.1, `04_Phase_05`, `04_Phase_07`, `04_Phase_08`, `09.5_Log`; "no per-city determination" in `04_Phase_04`, `04_Phase_07` (2) and `09_Record`) says `16` has only a Half B row for Sinheung, and uses its split of **26.7% mandated and 32.6% free** (6 and 12 occurrences). But `16` has carried a determination since 2026-09-02: **`## 17. ✅ SINHEUNG — DETERMINED`** at L1834 (the upper-case spelling is why a search for "Sinheung" misses it). Its table: baseline **329,374 (40.7%)** · mandated **228,180 (28.2%)** · FREE **252,199 (31.2%)**, which sum to 809,753, the workforce before the −10% cut; the mandate is fabrication in full (45% of the distinctive tier, 216,171) plus half of Education/other, the Institute, 2.5% (12,010). **§17 governs; Half B's 26.7% / 32.6% is the first-pass split and is superseded for Sinheung.** §17's counts are on the pre-cut workforce (`16` L1 says the determinations were not recomputed). The pass wrote at a time when it did not know of §17; nothing in it is edited.

## SNH-005 — Climate: the Mean column was replaced on 2026-10-21

The pass states *"coldest months avg −22 °C"* and a deep-winter *"Mean −22 °C"* (`00_Frame` L159 and L164, `07_QA_Gates` L95, `04_Phase_03` L123), and treats `READER/Sinheung.md` as a stub on which the spec was correct (`04_Phase_03`, `09.5_Log` #98). Since then: the spec's Mean column was replaced with the `READER` `Zhongshan` surface means, 1991–2020 (January +0.2 … June −14.6, July −16.1, August −16.1 … December −0.5; annual **−9.9 °C**); the range line now reads *"coldest months avg −16 °C"*; and `READER/Sinheung.md` was rebuilt the same day and is no longer a stub (it names Zhongshan as the proxy station).

## SNH-007 — The spec's identity line (L4)

`00_Frame` L122–130 and `05_Reconciliation` L181 propose a correction to the spec's identity line: it said *"'Sinheung,' the old working label … is now fully retired"* and should read **"Soyuz"** (a find-and-replace error the pass reported on 2026-09-07). The correction was proposed but not made in the spec until **2026-10-30**, when it was applied (`SNH-S01`).

## SNH-008 — Retired names in the pass

Sayowa is now **Temirötkel** (`00_Frame` L210; `04_Phase_05`); Princess Elisabeth is now **Utstein** (`09.5_Log`); Sejong is now **Contrapunto** (`04_Phase_05` L228 and one more line; `09.5_Log` 3); **Vostok** the city is now **Ariun Nuur** (`01_Inherited` L32; where it means the district, the real station or the lake it stays). See `Cities/City_Renames_Alias_Table_2026-10-03.md`.

## SNH-009 — Pass `README.md` L51 points at the wrong spec path

L51 cites `Specs/Sinheung.md`; the spec is at `Specs/Mirny subnet/Sinheung.md`. The README is a pass file and was not edited.

## Source corrections (developer, 2026-10-30)

- **`SNH-S01` — applied.** `Specs/Mirny subnet/Sinheung.md` L4 now reads *"'Soyuz,' the old working label tied to the physical station's Russian namesake …"*. The file is still 243 lines.
- **`SNH-S02` — applied.** Spec L128 now reads: *"the monthly Mean column is the BAS READER `Zhongshan` surface series, 1991–2020 (replaced 2026-10-21; see the column provenance note below); Progress Station (AARI, Russia) is the site's real-world basis."*
- **`SNH-S03` — applied.** `Official_Population_Census.md` L416–418 (the Sinheung tier list: Primary China; 12 Notable nations) now match the spec (L76–78): Primary South Korea; Significant China, Japan, Germany, Russia, Indonesia, Australia; Notable Thailand, Estonia, Hungary, Lithuania, Malaysia, Vietnam, Philippines, Bulgaria, Latvia, South Africa. The census is still 810 lines.
- **`SNH-S04` — left in place.** `Extent_and_Density_Per_City.md` L620 (1,069,350 · 107 · 153) and L657 (the −10% scenario) are in the 2026-09-05 snapshot table and a dated scenario. Live: 986,332 people need 99 km² at 10,000 per km² and 141 km² at 7,000.

---

*Entries `SNH-001` to `SNH-009` filed 2026-10-30 at the developer's direction ("all as recommended"). The pass is to be re-analyzed with the current methods (see the Weekly To-Do); these notes are the interim record.*
