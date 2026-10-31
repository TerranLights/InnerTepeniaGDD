# Shirayuki — amendment notes, 2026-10-30 (manual input audit)

**What this file is.** Shirayuki's pass was run and closed on 2026-09-06 (last substantive change 2026-10-01). **No pass file is edited by this note, and none was.** The entry below says what has changed in one of Shirayuki's sources since the pass, where the pass rests on the earlier state, and the live text as it stands on 2026-10-30. **Everything quoted from a pass file is as recorded at the pass; the source has since changed.** The pass stays the record of what it worked from.

**Limit, stated plainly.** The pass files were not re-read line by line. The places listed below were found by searching the pass files for "Jeju" (read in context at the lines named), so a founding passage worded differently may exist that this note does not list. Nothing here classifies, rules on or re-derives a finding; it only records the change and points to the live source.

**Developer decisions of 2026-10-30.** The entries below were added after the walk-through (*"all as recommended"*). Entries `SRY-001` to `SRY-008` describe the pass; nothing in the pass was edited. `SRY-S01` was applied to the census; `SRY-S02` and `SRY-S03` were left in place and are recorded here. Evidence: `Manual_Input_Audit_2026-10-29/Shirayuki_Audit.md` and `FIX_LEDGER.md`. The entry uses the ledger's ID (`SRY-005`).

---

## SRY-005 — The Founding Register now states geography as an additional founding factor (`DR-44`); founders come only from the Register (`DR-19`)

**What changed.** On 2026-10-03 the developer ruled the remaining founding rows (`DR-44`, `DEVELOPER_RULINGS_LOG.md` L917). For Shirayuki and Sinheung the developer's words (verbatim, same ruling, L919): *"for Shirayuki and Sinheung … I would change that to geography being an additional factor, on top of the agreement at the Court of Jeju-Do"*. The ruling's table row (L930) reads: "Japan and Korea stay, **by the Jeju-do court's diplomatic allocation, with geography (zone gap 3 to the Prydz Bay coast) as an ADDITIONAL factor** on top of it. Not a rewrite of the basis. Closes `FQ-13c`".

**The live Register row** (`Founding_Register.md` **L61**, re-read 2026-10-30; it was also L61 at audit time). The table's header is `City | Subnet | Solar UTC | Status | Founders | Basis | Source | Not founders` (L36). The row, quoted exactly:

```
| Shirayuki | Mirny | +5 | ✅ | Japan, by the Jeju-do court's diplomatic allocation | The Jeju-do court's diplomatic allocation, **and, in addition, geography**: zone gap 3 to the Prydz Bay coast (the edge of the rule). Developer: geography is an *additional* factor, not a replacement. | `Specs/Mirny subnet/Shirayuki.md` L175; `DR-44` | — |
```

The Register's change log (L90) records the same ruling: "Shirayuki and Sinheung (the Jeju-do allocation, plus geography)". **Earlier text of the same row (from git, as recorded when the Register was created on 2026-10-01, commit `ede29386`, L61):** Status 🟡, Basis "Allocation, not geography". The live text above replaced it when `DR-44` (ruled 2026-10-03) was entered; it is in the Register by the commit of 2026-10-04, `582cb682`.

**The standing rule (`DR-19`, 2026-09-30).** The Register's rule 1 (L8–10): "Founders are decided here and nowhere else. No spec, culture sheet, megasheet, catalog, census tag, robot-culture sheet, datasheet or ULM pass may originate or restate a founding claim that this file doesn't hold. They **point to this file**." The Register's rule 2 (L11–13): "A founding nation stands on geography and access, never on the real station (`DEVELOPER_RULINGS_LOG.md` `DR-19`)." The `DR-19` table (`DEVELOPER_RULINGS_LOG.md` L552) puts it as: founding nations are "Legitimate on **geography and access**."

**Where the pass rests on the founding by allocation** (found by searching for "Jeju"; each opened and read in context; as recorded at the pass, 2026-09-06):
- `00_Frame.md` L65 (the epistemic-horizon lines) and L266 (the founding row of the frame's table);
- `01_Inherited.md` L197–204 (section `A1`, the Jeju-do allocation);
- `02_Spine.md` L87;
- `04_Phase_02_Composition_and_Arrival.md` L42 (the Primary-tier row) and L107;
- `04_Phase_07_Order.md` L106 (the legitimacy row);
- `04_Phase_10_Catalog.md` L158 (a "Traces to" line);
- `07_QA_Gates.md` L156, `04z_Post-Ruling_Enrichment_Review.md` L17, and the log `09.5_Log.md` (entries at L64, L206, L475, L567), which also mention the allocation.

**What the pass does not contain.** A search of the 23 pass files (as they stood before this note was added) for "zone gap", `DR-44`, "Founding Register" and `Founding_Register` returned no hit, so the pass does not cite the Register's Shirayuki row. The pass was closed on 2026-09-06, before the Register existed (created 2026-10-01) and before `DR-44` (2026-10-03); its last edit (the audit fixes of 2026-10-01, commit `4a59fab8`) added no reference to the Register's Shirayuki row.

**What this note does.** It adds the live Register row and the two rules above beside the pass's founding passages, so that a reader who reaches those passages sees the Register's current basis. It does not say which statements in the pass should change, and it does not rule on any finding.

---

*Filed 2026-10-30 by the manual input audit sweep. Record of the sweep: `Manual_Input_Audit_2026-10-29/Sweep_Reports/Finished_Cities_Sweep.md`.*


---

## SRY-001 — The census scenario of 2026-10-28 (`DR-68`) rescaled Shirayuki's population; the pass records the earlier set

**Where the pass stands.** The pass was run and closed on 2026-09-06 on the figures then in the census. Those values are kept below as "as recorded at the pass (2026-09-06)"; the live rows are `Official_Population_Census.md` L493 (Census I) and L620 (Census II).

| | As recorded at the pass | Live since `DR-68` | Files in the pass that carry the old value |
|---|---|---|---|
| Census I humans | 518,822 | **530,961** | 6 |
| Census I robots | 541,660 | **553,438** | 7 |
| Census I combined | 1,060,482 | **1,084,399** | 7 (16 occurrences) |
| Census II humans | 302,512 | **310,620** | 6 |
| Census II robots | 352,980 | **360,719** | 7 |
| Census II combined | 655,492 | **671,339** | 6 (15 occurrences) |

Both live rows carry the earlier −10% ruling of 2026-09-05 (the figures before it were 576,469 / 601,844 / 1,178,313 and 336,124 / 392,200 / 728,324). Counts of occurrences are from a search of the pass files for the old numbers and may miss a differently worded one.

## SRY-002 — Figures derived from the old census set (recomputed by hand from the live rows)

| Derived figure | As recorded at the pass | Live (by hand, 2026-10-30) | Files (occurrences) |
|---|---|---|---|
| Retention, combined (671,339 ÷ 1,084,399) | 61.81% | **61.91%** | 5 (13) |
| Retention, humans (310,620 ÷ 530,961) | 58.31% | **58.50%** | 4 (5) |
| Retention, robots (360,719 ÷ 553,438) | 65.17% | **65.18%** | 4 (5) |
| People not here (1,084,399 − 671,339) | 404,990 | **413,060** | 11 (23) |
| Humans gone | 41.69% | **41.50%** | 8 (15) |
| Robots gone | 34.83% | **34.82%** | 7 (13) |
| Gap, robots minus humans | +6.86 pp | **+6.68 pp** | 3 (7) |

`01_Inherited.md` carries the statement that *"the whole retention layer is immune to the census rebalancing."* That held for the 10% cut, which moved both censuses by the same factor. It did not hold for `DR-68`, which moved the two censuses by different amounts; the ratios changed in the second decimal place.

## SRY-003 — Band, footprint, rock and ice shares, workforce

| Statement | As recorded at the pass | Live (by hand, 2026-10-30) | Where |
|---|---|---|---|
| Distance above the one-million line (Band 4, `DRQ-10`) | 6% above (1,060,482) | **8.4% above** (1,084,399) | `00_Frame`, `02_Spine` L47, `09.5_Log` |
| Required footprint at 10,000 and 7,000 per km² | 106–152 km² | **108–155 km²** (1,084,399 ÷ 10,000 = 108.4; ÷ 7,000 = 154.9) | `00_Frame`, `02_Spine`, `09.5_Log` (1 each) |
| Share of the city on rock (the ~40 km² oasis shared three ways, about 13.3 km², ÷ footprint) | 9–13% | **about 9–12%** (13.3 ÷ 155 = 8.6%; 13.3 ÷ 108 = 12.3%) | 6 files, 8 lines |
| Share of the city on ice | about 87–91% | **about 88–91%** | 18 files, 35 lines |
| Workforce | about 801,070 | **818,919** (`09` L78: required 290,137, 35.4%) | `04_Phase_04`, `04_Phase_07` §7a, `07_QA_Gates` L96, `09.5_Log` (5 files, 6 lines) |
| 25% of the workforce | about 200,270 | **204,730** | 3 files, 4 lines |

The percentages and ratios the pass derives from these (for example the shares of the distinctive tier) are ratios and did not move; the counts did.

## SRY-004 — Retired names in the pass

The pass uses the names in force on 2026-09-06. Since then: Bunger Hills City is now **Relung Panen** (5 files, 11 lines: `00_Frame` 2, `01_Inherited` 1, `04_Phase_02` 1, `05_Reconciliation` 1, `07_QA_Gates` 6); Sayowa is now **Temirötkel** (4 files, 6 lines: `04_Phase_05` 1, `07_QA_Gates` 1, `09.5_Log` 2, `10_Readiness_Check` 2, including the quoted route "Sayowa Junction → …"); Princess Elisabeth is now **Utstein** (`04_Phase_05` 2, `09.5_Log` 1); and **Vostok** the city is now **Ariun Nuur** (`04_Phase_05` 1, `04_Phase_07` 2, `09.5_Log` 1, `09.6_Input_Audit` 1; read each: where it means the city it is the new name, where it means the central scientific district, Vostok Station or Lake Vostok it stays). **Bharati** stays: it is a coordinate. See `Cities/City_Renames_Alias_Table_2026-10-03.md`.

## SRY-006 — `16` §16's worker counts are on the pre-cut workforce

`16` L1754–1760 give 363,971 / 105,222 / 420,886, which sum to 890,079, the workforce before the −10% cut. The Half B row (`16` L277) is synced (818,918; 40.9 / 11.8 / 47.3). The pass knew: `04_Phase_04` L44 says the 890,078 was "pre-cut → ~801,070 post-cut — a COUNT, so it moved". The live workforce is 818,919. `16` L1 says the per-city determinations were not recomputed on 2026-10-28.

## SRY-007 — Two passages in `04_Phase_05` cite a line that does not say what they quote

`04_Phase_05` L82–L84 says a kinship tie runs to Vostok ("`Airports.md`: the tier structures share an origin profile") and quotes the Mountain Pass outpost as "pushed for by a neighbor, which 'had both reasons to push'". Neither phrase is in `Airports.md`, now or at the pass commit, and "had both reasons to push" appears nowhere else in the GDD. The Mountain Pass row (`Airports.md` L18) says a joint Ariun Nuur–Kunlun venture. L86–L87 call the Princess Elisabeth (now Utstein) tie "UNEXPLAINED in its own source"; `City_National_Connections.md` gives a reason ("both share genuine Japanese-heritage demographic presence"). Recorded, not ruled on.

## SRY-008 — Runbook line numbers in the record

`10_Readiness_Check.md` L78 and L237 cite `00_RUNBOOK.md` "L2126–2131" and "L2129" (the Sayowa/Shirayuki ethnicity restatement). The runbook has been edited since; read them as "runbook line numbers as of the pass", history rather than a live pointer.

## Source corrections (developer, 2026-10-30)

- **`SRY-S01` — applied.** `Official_Population_Census.md` L426–428 (the Shirayuki tier list) said Primary China, Significant Japan and six others, and 13 Notable nations; it now matches the spec (L44–50): Primary Japan; Significant Australia, Russia, South Korea, China, Germany; Notable Romania, Vietnam, Ukraine, Belarus, Thailand, New Zealand, Lithuania, South Africa, Bulgaria, Latvia, Estonia. The file is still 810 lines. Philippines and Malaysia are no longer listed there, as in the spec.
- **`SRY-S02` — left in place.** `Extent_and_Density_Per_City.md` L616 (Shirayuki 1,178,313 · 118 · 168) is in the table that note L631 labels a 2026-09-05 snapshot; L656 (the −10% scenario, 117,831 · 72,832) is a dated scenario. Live: 1,084,399 needs 108 km² at 10,000 per km² and 155 km² at 7,000.
- **`SRY-S03` — left in place.** `16` L1754–1760 (see `SRY-006`).

---

*Entries `SRY-001` to `SRY-008` filed 2026-10-30 at the developer's direction ("all as recommended"). The pass is to be re-analyzed with the current methods (developer, 2026-10-30; see the Weekly To-Do); these notes are the interim record.*
