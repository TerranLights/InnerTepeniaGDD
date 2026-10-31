# Zukelli — manual input audit (2026-10-29)

Method: `README.md` in this folder. Read by hand: the spec in full (216 lines), the whole Pre-Trip (565 lines; the standard text compared line for line with Janbogo's — same bay, same subnet — and only the differing lines re-read), all 19 datasheets (the 2026-09-30 hand-built set, refreshed 2026-10-21), the pass README; every cited line opened against the live file. **Nothing was edited**; the edits are in `FIX_LEDGER.md` (entries `ZK-…`). Pass folder: `City_Development_Passes/Janbogo_Subnet/Zukelli/`. `LOC` = `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations`, `CITIES` = `LOC/Cities`. The city is not yet run. **The developer ruled on 2026-10-13 that this city, like Dumont d'Urville, needs a new name in line with its Australian founders; no name is chosen and no sweep is to be done unprompted** — the sheets carry that; the Pre-Trip and the spec do not. Zukelli's population changed in the 2026-10-28 scenario (`DR-68`: +12,139 H / +11,778 R; Census II +8,108 / +7,739).

**Verdict.** **Nothing blocks a run.** The Pre-Trip is already the refreshed one ("19 files, all present"), the Founding Register is named in its §J, and the `09` and `16` rows point at the right city's lines. What is left: **(1)** the sheets mix **old and new** census figures — `Step_0` and `Phase_2` retention (a new combined figure over old human and robot ones; `Phase_2` is wholly old), `Step_1_and_2` and `Phase_4` quote the `16` workforce as 944,859 (live 962,706) and `Phase_4` says `09` also equals 944,859 two rows below a row that gives 962,707; **(2)** `Step_0` cites the extent row at L618 and the shared-bay line at L602–603 (live L614 and L598); **(3)** the `16` determination §27 (the sheets already carry it, correctly) is cited one shift (+5) too early throughout; **(4)** the pending rename is in the sheets but not in the Pre-Trip's §A; **(5)** `Step_6` lacks the Subnet column and `Step_9` item 5; **(6)** source: the spec still says Janbogo's light figures are uncorrected (they were corrected on 2026-10-28), L158 gives a human retention (72.5%) that the census rows do not support, and the Jun / Oct means differ by 0.1 from the same station's file for Janbogo.

---

## PART 1 — ACCESS

### 1a. Checked and right
| Check | Result |
|---|---|
| Spec `CITIES/Specs/Janbogo subnet/Zukelli.md` (216 lines; `Step_-1` says 216 — exact). Later-era headings **L184**, **L192**, **L202** = the Step −1 list (L184–207); Gameplay Notes L127–134; Open Questions L208–216; `## Notable Locations` **L168**, `## Notable Figures` **L177**; spec L3, L6–9, L15–16, L18–22, L28, L32–45, L51, L55, L57, L61, L65–70, L74–77, L80, L83–93, L101–112, L117, L123–125, L140, L142, L144, L152, L154, L158, L164, L168–180 land on what the sheets say | ✅ |
| Census Section A heading **L250**, entry L252–256 (tier lines L254–256); Census I row **L491**; Census II row **L613**; others L780–781 and L804 | ✅ (L588 → **L589**, **A-01**) |
| Census I **639,723 H / 642,845 R / 1,282,568**; Census II **451,862 H / 501,644 R / 953,506** — the spec, `Step_-1`, `Step_0`, `Phase_2`, `Phase_4` (`09` row) agree with the live rows | ✅ |
| Extent file row **L614** (the 2026-09-05 snapshot: 1,258,651 → 126 / 180 km², Terra Nova Bay) and **L598** ("Terra Nova Bay carries two: Janbogo + Zukelli = 2,569,162, needing 257–367 km²") | ✅ (the sheet cites L618 and L602–603, **D-03**) |
| `09` row **L67** (header L52): D 1.25 · humans 639,723 · residents 1,282,568 · required **344,935** · workforce **962,707** (= 642,845 + 0.5 × 639,723 = 962,706.5, `09` rounds up) · **35.8%** (344,935 ÷ 962,707 = 35.83%); `16` Half B row **L268**: D 1.25 · workforce **962,706** · base **41.5** · MAND 14.6 · FREE 43.9 · src C; `11` no row | ✅ (the old workforce in sheets: **D-02**) |
| `16` §27 "ZUKELLI — DETERMINED" (heading **L2744**, table L2748–2750): baseline **391,579 (41.4%)** · mandated **55,328 (5.9%)** · FREE **497,952 (52.7%)** · distinctive tier 553,280 (58.6%); the three counts sum to 944,859 — the **pre-`DR-68` workforce** (631,067 + 0.5 × 627,584), so the shares are what matter; "This replaces a 14.6% mandate built on the commercial sector" at **L2761** | ✅ (the sheets carry §27 and the supersession — the model for the other cities; cited +5 early, **D-04**) |
| `READER/Zukelli.md` (16 lines; key `Mario_Zucchelli`; annual −14.0): the twelve monthly means equal the spec's Mean column; the sheets' L3–8 and L14 cites land | ✅ (but see **S-02**) |
| Stations L14, L26, L71 (Boulder Clay Runway, Enigma Lake Skiway, Zucchelli Ice Runway — all named as the sheet says); Founding Register row **L67** (founders: **Australia**, geography and access, `DR-20`, `DR-44`), L90, L94 — the Pre-Trip's §J names them; Cymatics L158; Topics L290, L320–322; Precip **L162** (145 / 55 / 90); Theoretical L985; Sweep row **L159** (`Zukelli | Y | . | Y | Y | . | . | 3/6`) and L218; Factions `Second_Interwar` L253–265 ("The Long Table — Zukelli"); Geothermal L6–9, L24 | ✅ |
| Zero-hit claims re-run: Energy grid, Holidays, Meme Machine, True Believer, NMCI, National Economy, Weapons, Weapon_Item_Catalog, Robot Physiology (both files), `Robot_Universals` (timeline repo; 33 files), Industry Staffing (4), SOC (4 `.md` + 1 PDF), Megacorps (3), Ice-Cold folder (7), `01` / `08`; Zodiac Full Attributes 267 lines; substrate folder 22 files (1 mention: `03_Gemini.md`); `06_Worked_Example_Provenance.md` (431 lines, 0 hits); `Laws_of_Robotics.md` L3–6 | ✅ |
| Characters: Momo (TCY-45) `PreWar_History.md` L98–100 and `Timeline.md` L33 (GDD tree) — right; the timeline-repo tree has 3 files naming the city (SE-031 `README.md` L61 and `Formative_History.md`, and TCY-42 Lillian's `README.md`) — the sheet's "one further mention … excluded" is Lillian; `Enneagram_Character_Index.md`: 0 | ✅ |
| Pass README: spec `../../../Specs/Janbogo subnet/Zukelli.md` ✓ (correct), local culture ✓, vision notes ✓, research log (does not exist yet) ✓, picks file ✓; `Step_3` picks: heading **L53**, picks L54–56 (Kraków [PRIMARY], Valparaíso, Venice) — before the Relung Panen insert, XS-15 does not apply | ✅ |
| Pre-Trip §C intro "19 files, all present"; §I `DATASHEET-NOT-YET-BUILT(N-5)=0`; the Run-mode and carve-out text equal Janbogo's | ✅ |

### 1b. Findings
| ID | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| **A-01** | STALE | **Line lists after later edits** (Pre-Trip, §C Step 2, §D, §E, vs live). Census L588 → **L589** (L780–781, L804 same). Highways L226, 231 → **L227, 232**. Airports L3, 11 same; L96 → **L99**. Ports L197, 224, 240, 244, 264 same; L337, 340, 346, 361, 550, 711, 755, 759, 802, 837 → **L360, 363, 369, 384, 573, 734, 778, 782, 825, 860**. CrossSub same. RelDB L30, 34, 50 same; L136, 301–302, 308, 501 → **L147, 312–313, 319, 512** (the city's entry is L312–L319). NatConn L9, 190 same; L400, 408, 440–442, 451, 454 → **L405, 413, 445–447, 456, 459** (the city's own section heading is **L459**). `09` L67 same. `16`: row **L267 → L268**; the other 15 entries L2648, 2754, 2763, 2774, 2776, 2781, 2787, 2798, 2812–2813, 2815, 2820–2821, 2881, 2902, 3086, 3479 → **L2653, 2759, 2768, 2779, 2781, 2786, 2792, 2803, 2817–2818, 2820, 2825–2826, 2886, 2907, 3091, 3484**; **missing:** the city's own section heading **L2744** ("ZUKELLI — DETERMINED", upper-case). Unchanged: Extent, Stations, Topics, Precip, Register. | live greps | Re-read each list live (SH-012) |
| **A-02** | NOTE | **Pending rename.** The sheets say "A new name in line with its Australian founders is pending" (`Step_-1`, `Step_1_and_2`, `Phase_2`); the Pre-Trip's §A says "No rename flagged — no *RENAMED* / *NAME RULED* notice in the spec's first 30 lines"; the spec itself carries no note of the 2026-10-13 ruling. | grep | Add a care-note to §A; consider a one-line note in the spec |
| **A-03** | NOTE | **Alias set** (mechanical draft: Mario Zucchelli Station · Terra Nova Bay · Victoria Land · Ross Sea). `Step_-1` row 18 lists more (Zucchelli Station, `Mario_Zucchelli`, `AYM00089662` / BASE BAIA TERRA NOVA, Terra Nova Bay); not in the Pre-Trip: the airstrip names (Boulder Clay, Enigma Lake — Stations L14, L26), "Zucchelli" alone, Mount Melbourne (Geothermal L24). Terra Nova Bay is shared with Janbogo (no "different place" note in §A). | live | Confirm; add |
| **A-04** | NOTE | **Zukelli-specific post-war and character files exist and are correctly outside the pass:** `PostWar_Refugee` "The Burning Witness — Zukelli Communities" (L35–45, "Zukelli (exclusively)"); Momo's six files in the GDD Characters tree (the sheet names two); the SE-031 / Lillian files. | grep | none (register in the sweep) |
| **A-05** | STALE | `PASS/README.md` is right (spec pointer correct), but `Step_3` cites "`PASS/README.md` L39" for the research-log note — it is **L40**. | README | Re-point |
| **A-06** | NOTE | Geothermal (Zukelli is one of the six geothermal cities): not a named input in the Pre-Trip; `Phase_3` and `Phase_5` carry L6–9, L24. | spec; Geothermal | DECIDE (with FM-005) |
| **A-07** | NOTE | Shared items SH-001 … SH-007, SH-010, SH-011, SH-013. | live | shared |

### 1c. Required inputs
T0-1…4 ✅ · G1 symbol pair present (not opened) · G2 climate ✅ · G3 `16` Half B ✅ (superseded by §27, which the sheets carry) · G4 Register row ✅ · G5 `Access type: SPUR` + Highways/Airports/Ports ✅ · G6 defining event: none (non-blocking) · G7 picks ✅ in `Step_3` · G8 census tier table ✅ · T2-8 extent ✅ (cited at the wrong line, **D-03**). **Nothing blocks.**

---

## PART 2 — ACCURACY

### 2a. The spec (read in full)
Checked right: Census I and II sum to their totals (639,723 + 642,845 = 1,282,568; 451,862 + 501,644 = 953,506); the 12 per-nation shares sum to **99.99%** (rounding); all four count columns sum **exactly**; tier lists equal the table (2 / 6 / 4) and the census Section A entry; tier totals are exactly the 8 : 3 : 1 share model (42.10 / 47.37 / 10.52 against 16 / 18 / 4 of 38); retention by hand: 953,506 ÷ 1,282,568 = **74.34%**, 451,862 ÷ 639,723 = **70.63%**, 501,644 ÷ 642,845 = **78.04%** (spread **7.41 pp** toward robots); monthly means average **−13.98 °C** (stated −14.0); in every month Avg High > Mean > Avg Low and **Avg Low > Rec Low**; the record extremes (+11.4 Feb; −32.4 Jul) equal the table — **this city's spec was reconciled with its table**, unlike several neighbors'; monthly precipitation sums to **144.7 mm**; falls 145 − lands 55 = lost 90 (37.9%); polar night May 6 → Aug 8 = 95 days, midnight sun Nov 2 → Feb 10 = **101 days** (the correction note's recomputed figures, which hold).

| ID | Sev | Source-level finding | Evidence |
|---|---|---|---|
| **S-01** | STALE | **The light-cycle correction note (L88–97)** says `Specs/Janbogo.md` "carries the identical wrong pair and is NOT corrected here … logged, not fixed". Janbogo's spec was corrected on 2026-10-28 (its L122 note: "~64 days" → ~95), so the sentence is out of date. | spec L95–97 |
| **S-02** | NOTE | **Two monthly means differ by 0.1 from the same BAS station's other file.** June −20.1 and October −15.1 here (and in `READER/Zukelli.md`), against −20.0 and −15.0 in `READER/Janbogo.md` and Janbogo's spec — both cite `Mario_Zucchelli`, 1991–2020. The 2026-10-21 recompute log (`READER_Recomputed_Normals_2026-10-21.md` L10) lists it as "worst Jun: spec −20.1 vs −20.0" and accepted the 0.1. | spec L106, L110 |
| **S-03** | STALE | **L158 "destroyed at 72.5% human retention, near peak"**: the census rows give human retention **70.63%** (robot 78.03% (corrected 2026-10-30; the audit first wrote 78.04), combined 74.34%). The same 72.5% / 77.7% / "~1,302,000" / "second-largest city" sit in census Section IV (**L781**) and `16` §27 (L2822); all three predate the census rewrites. | spec L158; census L781 |
| **S-04** | STALE | Peer-relative lines, none carried by the sheets: L80 "16 of the 37 Tepenian cities are colder" (38 now), L63 and L69 (the climate "applies here as well" as Janbogo's), L65, L129–130, L150–152 (Janbogo comparisons). | spec |
| **S-05** | NOTE | The composition keeps **Italy** at Significant (6.24%, spec L37) in a city whose founders are Australia (Register `DR-44`). The sheets record this as census deferred to the post-ULM review (`DR-23`). | spec L21, L37 |
| **S-06** | NOTE | The Daylight column shows May **0** and Nov **24** while polar night begins May 6 and midnight sun Nov 2; L129–133 (Gameplay Notes) hold the Zukelli Native perk and the structural-language mechanic (later-era / mechanics, correctly excluded). | spec |

### 2b. Datasheet rows
| File | Result |
|---|---|
| `Step_-1` | ✅ headings, header fields, census (exact), founding rows; ✅ length 216 |
| `Step_0` | ✅ combined retention, census rows; ❌ **D-01** (human / robot retention, spread), **D-03** (extent lines) |
| `Step_1_and_2` | ✅ climate rows 14–28, Stations, Register, §27 supersession noted; ❌ **D-02** (`16` row, workforce 944,859, base 41.4%), **D-04**, **D-05** ("10 files") |
| `Step_3` | ❌ **D-06** (`05` rule line), **A-05** |
| `Step_5` | ✅ |
| `Step_6`, `Step_9` | ❌ **D-07** (Subnet column; item 5) |
| `Step_7`, `Step_8` | ✅ (same content as Janbogo's; only the path form differs — absolute here, relative there) |
| `Step_10` | ❌ **D-08** ("428-line" → 431) |
| `Phase_2` | ❌ **D-01** (retention, wholly old), **D-09** (`§C.9b/d`) |
| `Phase_3` | ✅ every spec line; megasheet files named (filenames only) |
| `Phase_4` | ❌ **D-02** (workforce cross-check contradicts the row above it), **D-04**, **D-10** (`09` §3.5 line) |
| `Phase_5` | ❌ **D-11** (lines) |
| `Phase_6` | ✅ |
| `Phase_7` | ❌ **D-04** (`16` §27 cites all +5) |
| `Phase_8` | ✅ |
| `Phase_9` | ✅ robot share 50.12% (642,845 ÷ 1,282,568 = 50.122%) |
| `Phase_10` | ❌ **D-12** (runbook / spine lines) |

### 2c. Datasheet findings
| ID | Sev | File · row | Finding | Fix |
|---|---|---|---|---|
| **D-01** | STALE | `Step_0` rows 16–18; `Phase_2` row 5 | `Step_0`: combined 953,506 ÷ 1,282,568 = **74.34%** (new, right) but "human 443,754 ÷ 627,584 = 70.71%", "robot 493,905 ÷ 631,067 = 78.27%" and "spread 7.56 pp" are the pre-`DR-68` numbers, under "computed from the two rows above" (which show the new ones). By hand with the live rows: human **70.63%**, robot **78.04%**, spread **7.41 pp**. `Phase_2`: all four are old (combined **74.50%**, 70.71, 78.27, 7.56). | Replace in both |
| **D-02** | WRONG | `Step_1_and_2` · `16` row; `Phase_4` · "Workforce cross-check" | `16` Half B quoted as workforce **944,859**, base **41.4%** at row L267: live row **L268**: workforce **962,706** (= 642,845 + 0.5 × 639,723), base **41.5%** (MAND 14.6 / FREE 43.9 unchanged). `Phase_4` says "`09` 944,859 = `16` Half B 944,859 = the sum of §27's three tiers" — `09` is **962,707** (the same sheet's row 1 says so), `16` is 962,706; only §27's counts (391,579 + 55,328 + 497,952 = 944,859) are on the old workforce. | Replace; relabel §27's counts pre-`DR-68` |
| **D-03** | WRONG | `Step_0` rows 19–20 | Extent file cited **L618** (header "L607", section "L605") — Zukelli's row is **L614** (table header L603–604, section L601); the shared-bay line "L602–603" is **L598**. The values (1,258,651 → 126 / 180; on the live 1,282,568: 128 / 183 km²) are right as a labelled snapshot. | Re-point |
| **D-04** | STALE | `Step_1_and_2` row 19; `Phase_4` rows 3 and 5; `Phase_7` | `16` row **L267 → L268**; §27 cites all +5: **L2739–2745 → L2744–2750** (L2743–2745 → L2748–2750), **L2756 → L2761**, **L2747–2748 → L2752–2753**, **L2750–2754 → L2755–2759**, **L2758–2764 → L2763–2769**, **L2780–2781 → L2785–2786**, **L2776–2777 → L2781–2782**, **L2802–2808 → L2807–2813**, **L2812–2814 → L2817–2819**, **L2739–2825 → L2744–2830**; the "not carried" ranges (scope-word table L2768–2774, later-era L2783–2800 and L2815–2822) → **L2773–2779, L2788–2805, L2820–2827**. | Re-point (SH-012) |
| **D-05** | STALE | `Step_1_and_2` row 29; `Phase_5` row 14 | "**10** files" in the universe repo's `Worldspace/Locations/` → **4** `.md` files (README L18 still names the city). | Update |
| **D-06** | STALE | `Step_3` · picks row | the rule "`05_The_Input_Contract.md` L709–713": L709–713 now holds the Background-Lore exclusion; the ratification-by-root rule (item 6) is at **L719**. (As Cape Adare.) | Re-point |
| **D-07** | ADD | `Step_6` section 1 columns; `Step_9` | the Subnet column (live header L48); item 5 — as CASEY-048 / CASEY-049. | As Casey |
| **D-08** | STALE | `Step_10` | "the full 428-line file" → **431** (zero hits re-run). | Re-count |
| **D-09** | STALE | `Phase_2` row 10 | runbook §C.9b **L2088 → L2090**, §C.9d **L2147 → L2150**. | Re-point |
| **D-10** | STALE | `Phase_4` row 4 | `09` §3.5 "THE FREEDOM MARGIN" **L124 → L126**. | Re-point |
| **D-11** | STALE | `Phase_5` | Highways **L226, L231 → L227, L232**, the conflict row **L226–228 → L227–229**; RelDB entry **L301–307 → L312–318**, Notes **L308 → L319**, the "southern terminus" line **L306 → L317**, other entries **L136 → L147** (L30, L50 same); Ports **L335–337, L361 → L358–360, L384**, tier summary **L570 → L593**, Q&A **L661 → L684**, shared-infrastructure **L339–341 → L362–364** (the "L202–204" it mentions is unchanged); Airports **L96 → L99**; NatConn section **L449 → L459** and the other cities' sections **L184, L395, L403, L435–437, L446 → L190, L405, L413, L445–447, L456**; CrossSub unchanged; Geothermal unchanged. | Re-point |
| **D-12** | STALE | `Phase_10` · "No invented person names" | runbook **L1980 → L1982**; spine **L219 → L220**. (As Cape Adare.) Also `Step_0` row 21: the "location registries" item — runbook **L1970 → L1972**, spine **L284–285 → L285**. | Re-point |
| **D-13** | NOTE | counts | builder-convention / out-of-date counts: "428-line" `06` (above), "146-line" Energy etc. where present — per SH-009. | per SH-009 |

### 2d. DECIDE items (collected)
1. **S-03** Update L158 and census L781 (and `16` §27 L2822) to the live retention (70.63% / 78.03%), or drop the figure.
2. **A-02** Add the pending-rename care-note to the Pre-Trip (the new name is not chosen; no sweep unprompted).
3. **S-02** Settle the June / October means (−20.1 / −15.1 or −20.0 / −15.0) for the shared station.
4. **A-06** Geothermal as a named input (with Fort McMurdo).
