# Mirny · Amendment notes · 2026-10-30 · from the manual input audit

> ## STATUS: **FILED BESIDE THE FINISHED PASS. Nothing in any pass file, in the 2026-10-29 amendment files, in the `DR-56` register or in any `.t8_*` file was changed.**
> Every figure and line number that a pass file carries and that this note names is **as recorded at the pass; the source has since changed.** The live value is given beside it, read from its source on 2026-10-30. This note records what moved and where; it re-derives nothing and rules nothing. It is append-only, like the other amendment files in this folder (`DR-74`).
> **Two notes are filed here:** (1) the census change of 2026-10-28 (`DR-68`) and the values derived from it; (2) the line movement in `Ports.md` after the insertions of 2026-10-29 (`DR-82`).
> **Not filed here:** the effect of `DR-82` on Phase 5's arrival types and air row (a separate decision is pending), and the Russia-label note (nothing is ruled).

---

## 1 · The census change of 2026-10-28 (`DR-68`) — pass figures are the old set; shares and axes unchanged

### 1.1 What changed, and the live figures

`Official_Population_Census.md` Section A row L488 and Section B row L609 carry the change ("Scenario `DR-68`, 2026-10-28"); `Specs/Mirny subnet/Mirny.md` L15–16 agrees with both rows.

| Item | As recorded at the pass | Live (2026-10-30) | Source line |
|---|---|---|---|
| Census I humans | 665,901 | **678,041** (+12,140) | census L488; spec L15 |
| Census I robots | 685,529 | **697,307** (+11,778) | census L488; spec L15 |
| Census I combined | 1,351,430 | **1,375,348** | census L488; spec L15 |
| Census II humans | 507,344 | **515,452** (+8,108) | census L609; spec L16 |
| Census II robots | 509,151 | **516,890** (+7,739) | census L609; spec L16 |
| Census II combined | 1,016,495 | **1,032,342** | census L609; spec L16 |

Sums, by hand: 678,041 + 697,307 = 1,375,348; 515,452 + 516,890 = 1,032,342.

### 1.2 Values derived from the census (live, recomputed by hand)

| Value | As recorded at the pass | Live | Arithmetic |
|---|---|---|---|
| Robot share of Census I | 50.73% | **50.70%** | 697,307 ÷ 1,375,348 = 0.5070 (1,375,348 × 0.5 = 687,674; remainder 9,633; 9,633 ÷ 1,375,348 = 0.0070) |
| Retention, combined | 75.22% | **75.06%** | 1,032,342 ÷ 1,375,348 (× 0.75 = 1,031,511; remainder 831; 831 ÷ 1,375,348 = 0.0006) |
| Retention, humans | 76.19% | **76.02%** | 515,452 ÷ 678,041 (× 0.76 = 515,311; remainder 141; 141 ÷ 678,041 = 0.0002) |
| Retention, robots | 74.27% | **74.13%** | 516,890 ÷ 697,307 (× 0.74 = 516,007; remainder 883; 883 ÷ 697,307 = 0.0013) |
| Relocated between Census I and Census II (Census I − Census II) | 334,935 (158,557 humans, 176,378 robots) | **343,006** (162,589 humans, 180,417 robots) | 1,375,348 − 1,032,342 = 343,006; 678,041 − 515,452 = 162,589; 697,307 − 516,890 = 180,417; 162,589 + 180,417 = 343,006 |
| Retention spread | 1.92 pp toward humans | **1.89 pp toward humans** | 76.02 − 74.13 = 1.89 (unrounded 76.021 − 74.127 = 1.894) |
| Workforce (humans count as half) | 1,018,480 | **1,036,328** | 697,307 + 0.5 × 678,041 = 697,307 + 339,020.5 = 1,036,327.5; printed 1,036,328 at `09` L71 and `16` L276 |
| Required workforce (`09`) | not quoted in the pass (it did not use that column of the `09` per-city row, `04_Phase_04_Ordinary_Life.md` L38); the datasheet carried 362,213 | **368,677** | `09_Per_City_Baseline_Run.md` L71; "% of workforce required" 35.6%, unchanged |
| Gate 11 area at 10,000 per km² | 135 km² (extent snapshot of 2026-09-05) | **137.5 km²** | 1,375,348 ÷ 10,000 = 137.53 |
| Gate 11 area at 7,000 per km² | 193 km² (same snapshot) | **196.5 km²** | 1,375,348 ÷ 7,000 = 196.48 |

`Extent_and_Density_Per_City.md` L611 still prints the snapshot row (1,351,430 · 135 · 193); its note at L631 says the table is the dated record and the census is the live source.

### 1.3 What did not change

- **The shares.** The 14 per-nation shares in the spec's table (L30–45) are the same before and after the change and sum to 100.00% (checked against the spec as it stood before 2026-10-28, commit `1a48edbc`, and the live spec). Every tier list (Primary: China; Significant: Japan, UK, South Korea, Russia, Indonesia, Australia; Notable: Thailand, Vietnam, Philippines, Malaysia, South Africa, New Zealand, Belarus) and every axis the pass derived from them is untouched by this change.
- **The per-nation counts did change** (for example, China's Census I robots 166,189 → 169,045). The pass files quote no per-nation count: a search for the old and the new China and Russia counts finds none.
- The 14 live per-nation columns sum to the live totals: Census I robots 697,307, humans 678,041; Census II robots 516,890, humans 515,452.

### 1.4 Where the old values are held in the pass (live counts, 2026-10-30)

The 21 pass outputs are `00.1`, `00_Frame`, `01`, `02`, `03`, the nine `04_Phase_02` … `04_Phase_10` files, `05`, `06`, `07`, `08`, `09`, `09.5` and `10`.

| Old value | Pass outputs (of 21 files) | Where else |
|---|---|---|
| 665,901 (Census I humans) | 14 files, 41 occurrences | `04b_T8_Rounds_Phase_6`, `_7`, `_8`; the two 2026-10-29 amendment files (`P06`, `P07`) |
| 685,529 (Census I robots) | 14 files, 39 occurrences | the two 2026-10-29 amendment files |
| 1,351,430 (Census I combined) | 15 files, 47 occurrences (18 of them in `07_QA_Gates.md`) | none among the amendment or round files |
| 507,344 and 509,151 (Census II humans, robots) | 1 file (`07_QA_Gates.md`), 5 occurrences each | — |
| 1,016,495 (Census II combined) | 3 files: `00.1`, `00_Frame`, `07_QA_Gates` | — |
| 1,018,480 (workforce) | 4 files: `04_Phase_04`, `04_Phase_07`, `04_Phase_10`, `07_QA_Gates` | — |
| 50.73% (robot share) | 14 files, 37 occurrences | the two 2026-10-29 amendment files |
| 75.22% (retention, combined) | 3 files: `00.1`, `00_Frame`, `07_QA_Gates` | — |
| 334,935 (relocated; with 158,557 humans and 176,378 robots) | 2 files: `00_Frame`, `07_QA_Gates` | — |

The two amendment files of 2026-10-29 record the pass figures **"as written"** (their own frame lines say so); they are not re-stated here.

**For a reader or a later re-run:** read every census-derived number in the pass as the old set. The live set is in 1.1 and 1.2. The shares, tier lists and axes need no re-derivation on account of this change; any figure that is a count, a share *of a count*, or an area does.

---

## 2 · `Ports.md`: the lines the pass cites have moved (insertions of 2026-10-29, `DR-82`)

On 2026-10-29 a note was inserted in `Infrastructure/Ports.md` at L274 and a new section (§3e, "THE AUSTRALIAN-SIDE INTERNATIONAL INTAKE", heading L285, section to L303) was added after the open-questions list. Every line after the note moved. **This is a line shift only; no finding the pass drew from `Ports.md` changes with it, and "tier not established" for Mirny's port is unchanged** (live L200, L386, L737).

### 2.1 Cited by the pass and now at a different line

| Pass cites (`PRT` L…) | Live line (2026-10-30) | Text at the live line | Shift |
|---|---|---|---|
| L276 | **L278** | open item 2, "Which Tepenian ports receive people from Hobart?" | +2 |
| L278 | **L280** | open item 4, "Era." (whether the same transfer role continues) | +2 |
| L363 | **L386** | "Dumont d'Urville · Mirny — Australia-partner receiving nodes — tier not established" | +23 |
| L536 | **L559** | the Davis row, "TEPENIA'S PRINCIPAL INDIAN-OCEAN-SECTOR IMPORT PORT" | +23 |
| L785 | **L808** | "Ask what the port COSTS before asking what it carries." | +23 |
| L787 | **L810** | "A CONSTRUCTED port implies a trade and a calendar." | +23 |
| L818 | **L841** | "RECOMMEND: no." (whether any grid-heated harbor ever existed) | +23 |
| L822 | **L845** | "better answered by each city's own pass than decided here in bulk" | +23 |
| L825 | **L848** | "Trade with Upper Earth is trade with real places, which is legitimate; a Tepenian city HAVING a nationality is not." | +23 |

The pass cites these in `04_Phase_05_Relation_and_Geometry.md` (all nine) and `04_Phase_07_Order.md` (L363 and the unchanged L129, L220).

### 2.2 Cited by the pass and still at the same line (checked)

L89–94 (the port-tier table) · L129 (the Australia three-node row) · L130 (neutral transshipment row) · L154 · L200 (Mirny's Hobart row, 4,159 km) · L207 (Fremantle) · L218 (the "roughly 10 to 11 days, each way" voyage figure) · L220 · L221 · L226–L230 (the terminal-distance rows) · L249 · L262 · L269.

### 2.3 Mirny's entries in `Ports.md` as they read now

For a later reader; the pass already cites L200, L207 and L226–L230, and does not cite L189 or the table header L224.

- **L189:** canon fixes the Australian freighter nodes as "Dumont d'Urville · Mirny · Mawson", with Mirny "staged via Hobart/Fremantle".
- **L200:** 4,159 km (Hobart) · "Mirny (canon node, subnet hub)" · "tier not established (§5.1)" · "Davis Sea coast" · "Direct, long haul. Canon: staged via Hobart/Fremantle; Fremantle is 4,121 km".
- **L224–L230:** the terminal-distance table; Mirny's column reads Bunbury 3,982 · Outer Harbor 4,580 · Torquay / Jan Juc 4,465 · Hobart 4,159 · Fremantle 4,121 km.

---

## 3 · Other anchors noticed while verifying (not part of the two notes above; the list is not exhaustive)

Each was read live on 2026-10-30. The pass cites the first number; the live line is the second.

| Source | Pass cites | Live | Text at the live line |
|---|---|---|---|
| `16_Per_City_Three_Tier_Run.md`, Half B row | `D16` L275 | **L276** | "Mirny \| Mirny \| 1.25 \| 1,036,328 \| 41.1% \| 11.8% \| 47.1% \| C" |
| `16_Per_City_Three_Tier_Run.md`, §20 | L2105–2122 | **L2110–2127** (heading L2110; mandate table to L2127) | "## 20. ✅ MIRNY — DETERMINED" |
| `Extent_and_Density_Per_City.md`, Mirny row | `EXT` L615 | **L611** | "Mirny \| Mirny \| 1,351,430 \| 135 \| 193 \| coastal ice" |

The §20 worker counts (418,565 / 239,966 / 359,949; sum 1,018,480) are the pre-`DR-68` set: `16` L1 says the per-city determinations were not recomputed on 2026-10-28; the shares stand.

---

## 4 · `DR-82` (2026-10-29): winter arrivals are processed at a separate coastal airport and fly on to Mirny — filed 2026-10-30 at the developer's direction ("as recommended")

**What changed.** The ruling (`DEVELOPER_RULINGS_LOG.md` L1494 ff.) sets out an Australian-side intake: in summer a seasonal sea gateway, in winter an air-only, fully isolated coastal airport (the *Winter Intake Airport*, working label, name not ruled, a non-city outpost like Mountain Pass) where customs and immigration processing happen, after which **processed arrivals fly on to Mirny**. Casey keeps its no-air-access status. The ruling's own "Not decided" list includes **how the Mirny onward airfield relates to Mirny's existing airport marker (`DR-51`'s deferral of in-frame existence is not closed)**, the winter airport's site, name, runway type and operating months, and passenger numbers.

**Where the pass rests on the old state.** The pass states, correctly for its time, that Mirny's air route is unknown and deferred on purpose; it never had an onward-flight role to record.
- `04_Phase_05_Relation_and_Geometry.md` L247 (arrival types, row **d, By air**): Mirny Airport (`AIR` L12) in a list of post-war airports; *"not at the founding"* (`DR-51`); *"when Mirny Airport was built is open"*; "not stated" for the other columns.
- Phase 5's open-question and premise entries: **R-57** (L454 table row; L493 entry: when Mirny Airport was built, whether it is domestic, where it sits, what it connects; "recorded only; `DR-51` is deferred on purpose and is not to be closed quietly") and **PA-25** (L524: no air arrivals at the founding; *"Overturned by: the deferred airports ruling"*).
- **R-57** is also cited in `04_Phase_02`, `04_Phase_03`, `04_Phase_04`, `04_Phase_06`, `04_Phase_08` and `04_Phase_10` (1, 1, 1, 6, 4 and 3 mentions), in `06_Differentiation.md` (4) and in `08_Review_Panel.md` (1). `04_Phase_10` lists "the airport marker (in-frame date open)" among its physical referents.

**What `DR-82` does and does not change for those entries.** It gives Mirny a **role** (the onward-flight destination for processed winter arrivals) but rules **nothing about the airport's date, site, form or whether it exists in the founding frame**; `DR-51`'s deferral stands. So R-57 and PA-25 are **not overturned**; they are **touched**: a reader of the pass should know that a later ruling now gives the marker a purpose, and that the in-frame question is still open. Nothing in the pass is wrong; the new fact simply was not available.

**Other lines that now name Mirny under `DR-82`** (found 2026-10-30; none is cited by a pass file): `Airports.md` L23 (the Winter Intake Airport row: "processed arrivals then fly on to Mirny") and L104 ("Mirny's onward-flight role (`DR-82`) does not move any city between lists; Casey stays in No Air Access"); `Ports.md` L295 (table row "Where people are processed": at the airport, then fly on to Mirny), L207 (Fremantle: Mirny at 4,121 km great-circle) and L232 (the Bunbury distances).

**Not decided here.** Whether Phase 5's arrival row, or R-57, should be re-derived in light of `DR-82` (that is amendment-work, to be done by the process the Mirny amendments follow, in the 05:00–14:59 window); whether `DR-51`'s deferral should now be closed. Nothing in the pass was edited.
